"""Persist attempt reservations BEFORE submission; failed jobs still count.

No tool is called here. Actual generation adapters must call this guard and
record owning-service evidence. A reservation is not an executed generation.
"""
import math
from pathlib import Path
from profile import Blocked, atomic_write, digest, read, write_lease


def reserve(path, policy, attempt_id, payload_hash, expected_revision):
    required = ('provider', 'model', 'unit', 'per_attempt', 'limit', 'max_attempts',
                'profile_sha256', 'authorization_evidence', 'paused')
    if any(k not in policy for k in required) or not policy['authorization_evidence']:
        raise Blocked('SPEND_POLICY_INCOMPLETE')
    if policy['paused'] is not False:
        raise Blocked('GENERATION_PAUSED')
    if not all(isinstance(policy[k], (int, float)) and not isinstance(policy[k], bool)
               and math.isfinite(policy[k]) and policy[k] >= 0
               for k in ('per_attempt', 'limit')):
        raise Blocked('SPEND_AMOUNT_INVALID')
    if not isinstance(policy['max_attempts'], int) or isinstance(policy['max_attempts'], bool) or policy['max_attempts'] < 1:
        raise Blocked('ATTEMPT_LIMIT_INVALID')
    if not all(isinstance(policy[k], str) and policy[k].strip() for k in
               ('provider', 'model', 'unit', 'profile_sha256', 'authorization_evidence')):
        raise Blocked('SPEND_POLICY_INCOMPLETE')
    if not attempt_id or not payload_hash:
        raise Blocked('WRITE_INTENT_MISSING')
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with write_lease(path, 'SPEND'):
        policy_hash = digest(policy)
        state = read(path) if path.exists() else {'revision': 0, 'policy_sha256': policy_hash, 'attempts': {}}
        if state['policy_sha256'] != policy_hash:
            raise Blocked('SPEND_POLICY_CHANGED_RECONCILE_FIRST')
        # A repeated submission is not authorization to call the provider twice.
        if attempt_id in state['attempts']:
            raise Blocked('ATTEMPT_EXISTS_RECONCILE_NOT_RESUBMIT')
        if state['revision'] != expected_revision:
            raise Blocked('SPEND_REVISION_CONFLICT')
        if any(a['status'] in ('reserved', 'write_outcome_unknown') for a in state['attempts'].values()):
            raise Blocked('UNCERTAIN_ATTEMPT_RECONCILE_FIRST')
        if len(state['attempts']) >= policy['max_attempts']:
            raise Blocked('ATTEMPT_LIMIT_REACHED')
        # Charge reservations conservatively, including failures and corrections.
        committed = sum(a['reserved_cost'] for a in state['attempts'].values())
        if committed + policy['per_attempt'] > policy['limit']:
            raise Blocked('SPEND_LIMIT_REACHED')
        state['attempts'][attempt_id] = {'payload_sha256': payload_hash,
                'reserved_cost': policy['per_attempt'], 'status': 'reserved',
                'provider': policy['provider'], 'model': policy['model']}
        state['revision'] += 1
        atomic_write(path, state)
        return state


def record_result(path, attempt_id, status, evidence, expected_revision, actual_cost=None):
    if status not in ('succeeded', 'failed', 'write_outcome_unknown') or not evidence:
        raise Blocked('ATTEMPT_RESULT_EVIDENCE_MISSING')
    path = Path(path)
    with write_lease(path, 'SPEND'):
        state = read(path)
        if state['revision'] != expected_revision:
            raise Blocked('SPEND_REVISION_CONFLICT')
        attempt = state['attempts'][attempt_id]
        if attempt['status'] not in ('reserved', 'write_outcome_unknown'):
            raise Blocked('ATTEMPT_ALREADY_RESOLVED')
        if actual_cost is not None:
            if not isinstance(actual_cost, (int, float)) or isinstance(actual_cost, bool) or not math.isfinite(actual_cost) or actual_cost < 0:
                raise Blocked('ACTUAL_COST_INVALID')
            attempt['actual_cost'] = actual_cost
            # Unexpected overage is recorded, never hidden; it blocks further jobs.
            attempt['reserved_cost'] = max(attempt['reserved_cost'], actual_cost)
        attempt.update(status=status, evidence=evidence)
        state['revision'] += 1
        atomic_write(path, state)
        return state
