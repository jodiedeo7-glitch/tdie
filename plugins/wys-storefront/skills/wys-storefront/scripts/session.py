"""Private preference and decision state. No network or generation calls."""
import argparse
import copy
from contextlib import contextmanager
from datetime import datetime
import hashlib
import json
import math
import os
from pathlib import Path
import tempfile
from zoneinfo import ZoneInfo
try:
    import fcntl
except ImportError:
    fcntl = None

BANK = json.loads((Path(__file__).parents[1] / 'references/question-bank.json').read_text())
QUESTIONS = {q['id']: q for q in BANK['questions']}
OPERATOR_FIELDS = ('reference_assets', 'disclosure', 'connected_capabilities', 'state_location')


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                    separators=(',', ':'), allow_nan=False).encode()).hexdigest()


@contextmanager
def write_lease(path):
    """Kernel-released lease; retain the inode so concurrent writers share it."""
    if fcntl is None:
        raise ValueError('OS_LOCK_UNAVAILABLE')
    fd = os.open(str(path) + '.write-lease', os.O_CREAT | os.O_RDWR, 0o600)
    try:
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            raise ValueError('WRITE_IN_PROGRESS') from error
        if Path(str(path) + '.lock').exists():
            raise ValueError('LEGACY_LOCK_RECONCILE_REQUIRED')
        yield
    finally:
        os.close(fd)


def load(path):
    state = json.loads(Path(path).read_text())
    check = copy.deepcopy(state)
    if check.pop('sha256', None) != digest(check) or state.get('schema') != 1:
        raise ValueError('STATE_INTEGRITY_MISMATCH')
    if state.get('questionnaire_version') != BANK['schema_version']:
        raise ValueError('QUESTIONNAIRE_VERSION_CHANGED')
    return state


def write(path, state):
    state.pop('sha256', None)
    state['sha256'] = digest(state)
    fd, temporary = tempfile.mkstemp(prefix='.wys-', dir=path.parent)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            json.dump(state, f, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False)
            f.flush()
            os.fsync(f.fileno())
        os.replace(temporary, path)
        fd = os.open(path.parent, os.O_RDONLY)
        try:
            os.fsync(fd)
        finally:
            os.close(fd)
        if load(path) != state:
            raise ValueError('STATE_READBACK_MISMATCH')
        return state
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def next_question(state):
    persona = state['answers'].get('persona_choice', {}).get('value', {}).get('selected', [])
    for q in BANK['questions']:
        if q['id'] in state['answers']:
            continue
        if q['id'] == 'persona_world' and any(x.startswith('No person:') for x in persona):
            continue
        q = copy.deepcopy(q)
        if q['id'] == 'category_preferences':
            cats = state['answers'].get('categories', {}).get('value', {}).get('selected', [])
            q['branches'] = {k: BANK['category_branches'][k] for k in cats}
        return q
    return None


def envelope(data):
    if not isinstance(data, dict) or 'value' not in data:
        raise ValueError('ENVELOPE_REQUIRED')
    if not isinstance(data.get('evidence'), str) or not data['evidence'].strip():
        raise ValueError('SOURCE_EVIDENCE_REQUIRED')
    recovered = data.get('source_kind') == 'recovered_direct_instruction'
    if recovered and data.get('answered_at') is not None:
        raise ValueError('ORIGINAL_ANSWER_TIME_NOT_KNOWN')
    stamp = data.get('recorded_at' if recovered else 'answered_at')
    if datetime.fromisoformat(stamp).tzinfo is None:
        raise ValueError('TIMESTAMP_TIMEZONE_REQUIRED')
    digest(data)


def choices(value, options, multi=True):
    if not isinstance(value, dict):
        raise ValueError('GUIDED_ANSWER_OBJECT_REQUIRED')
    selected, detail = value.get('selected', []), value.get('detail', '')
    if not isinstance(selected, list) or not all(isinstance(x, str) for x in selected):
        raise ValueError('CHOICE_LIST_REQUIRED')
    if len(set(selected)) != len(selected) or any(x not in options for x in selected):
        raise ValueError('CHOICE_INVALID')
    if not isinstance(detail, str) or (not selected and not detail.strip()):
        raise ValueError('QUESTION_UNANSWERED')
    if not multi and len(selected) > 1:
        raise ValueError('SINGLE_CHOICE_REQUIRED')
    return selected, detail


def validate(state, qid, data):
    if qid not in QUESTIONS:
        raise ValueError('QUESTION_UNKNOWN')
    envelope(data)
    value = data['value']
    if qid == 'category_preferences':
        cats = state['answers'].get('categories', {}).get('value', {}).get('selected', [])
        responses = value.get('categories') if isinstance(value, dict) else None
        if not cats or not isinstance(responses, dict) or set(responses) != set(cats):
            raise ValueError('SELECTED_CATEGORY_BRANCHES_REQUIRED')
        for cat in cats:
            if not isinstance(responses[cat], dict):
                raise ValueError('CATEGORY_BRIEF_REQUIRED')
            for branch in BANK['category_branches'][cat]:
                choices(responses[cat].get(branch['id']), branch['options'])
        return
    q = QUESTIONS[qid]
    selected, detail = choices(value, q['options'], q['multi'])
    if qid == 'categories' and not selected:
        raise ValueError('KNOWN_CATEGORY_SELECTION_REQUIRED')
    if qid == 'timezone':
        ZoneInfo(detail.strip() if not selected or selected == ['Another timezone'] else selected[0])
    if qid == 'generation_budget':
        if len(selected) != 1:
            raise ValueError('BUDGET_ROUTE_REQUIRED')
        attempts = value.get('max_attempts_per_role')
        if type(attempts) is not int or attempts < 1:
            raise ValueError('FINITE_ATTEMPT_LIMIT_REQUIRED')
        if not isinstance(value.get('period'), str) or not value['period'].strip():
            raise ValueError('BUDGET_PERIOD_REQUIRED')
        if selected != ['No paid generation']:
            for key in ('per_look_limit', 'period_limit'):
                n = value.get(key)
                if type(n) not in (int, float) or not math.isfinite(n) or n <= 0:
                    raise ValueError('FINITE_PAID_LIMIT_REQUIRED:' + key)
            if not isinstance(value.get('unit'), str) or not value['unit'].strip():
                raise ValueError('BUDGET_UNIT_REQUIRED')


def mutate(path, command, customer=None, qid=None, data=None, revision=None, correction=False):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with write_lease(path):
        if command == 'init':
            if not isinstance(customer, str) or not customer.strip():
                raise ValueError('CUSTOMER_ID_REQUIRED')
            if path.exists():
                state = load(path)
                if state['customer_id'] != customer:
                    raise ValueError('CUSTOMER_ID_MISMATCH')
                return state
            return write(path, {'schema': 1, 'questionnaire_version': BANK['schema_version'],
                                'customer_id': customer, 'revision': 0,
                                'answers': {}, 'events': [], 'history': []})
        state = load(path)
        if customer is not None and state['customer_id'] != customer:
            raise ValueError('CUSTOMER_ID_MISMATCH')
        if state['revision'] != revision:
            raise ValueError('REVISION_CONFLICT')
        envelope(data)
        previous = state['sha256']
        invalidated = None
        invalidated_verifications = None
        if command == 'answer':
            validate(state, qid, data)
            if qid in state['answers'] and not correction:
                raise ValueError('EXPLICIT_CORRECTION_REQUIRED')
            if qid == 'categories' and 'category_preferences' in state['answers']:
                if state['answers']['categories']['value']['selected'] != data['value']['selected']:
                    invalidated = state['answers'].pop('category_preferences')
            state['answers'][qid] = copy.deepcopy(data)
            invalidated_verifications = state.pop('operator_verifications', None)
        elif command == 'operator':
            if qid not in OPERATOR_FIELDS:
                raise ValueError('OPERATOR_FIELD_UNKNOWN')
            if (data.get('source_kind') != 'operator_verified'
                    or data.get('verification_status') != 'VERIFIED'
                    or data.get('answers_sha256') != digest(state['answers'])):
                raise ValueError('OPERATOR_VERIFICATION_BINDING_REQUIRED')
            if data['value'] is None or data['value'] == '' or data['value'] == {} or data['value'] == []:
                raise ValueError('OPERATOR_VALUE_REQUIRED')
            verified = state.setdefault('operator_verifications', {})
            if qid in verified and not correction:
                raise ValueError('EXPLICIT_CORRECTION_REQUIRED')
            verified[qid] = copy.deepcopy(data)
        else:
            state['events'].append(copy.deepcopy(data))
        state['revision'] += 1
        state['history'].append({'type': command, 'question_id': qid,
                                 'correction': correction, 'revision': state['revision'],
                                 'previous_sha256': previous, 'record': copy.deepcopy(data),
                                 'invalidated_category_brief': invalidated,
                                 'invalidated_operator_verifications': invalidated_verifications})
        return write(path, state)


def status(state):
    q = next_question(state)
    return {'customer_id': state['customer_id'], 'revision': state['revision'],
            'sha256': state['sha256'], 'answers_recorded': len(state['answers']),
            'answers_sha256': digest(state['answers']),
            'operator_fields_recorded': sorted(state.get('operator_verifications', {})),
            'events_recorded': len(state['events']), 'next': q,
            'intake_status': 'RECORDED' if q is None else 'INCOMPLETE',
            'capabilities': 'NOT_VERIFIED', 'generation': 'NOT_RUN', 'publication': 'NOT_RUN'}


def main():
    p = argparse.ArgumentParser()
    p.add_argument('command', choices=('init', 'next', 'answer', 'event', 'operator', 'status'))
    p.add_argument('--state', required=True)
    p.add_argument('--customer')
    p.add_argument('--question')
    p.add_argument('--input')
    p.add_argument('--revision', type=int)
    p.add_argument('--correction', action='store_true')
    a = p.parse_args()
    try:
        if a.command in ('next', 'status'):
            state = load(a.state)
            result = next_question(state) if a.command == 'next' else status(state)
        else:
            if a.command != 'init' and (a.input is None or a.revision is None):
                raise ValueError('INPUT_AND_REVISION_REQUIRED')
            data = json.loads(Path(a.input).read_text()) if a.input else None
            state = mutate(a.state, a.command, a.customer, a.question, data, a.revision, a.correction)
            result = status(state)
        print(json.dumps(result, ensure_ascii=False, allow_nan=False))
    except (ValueError, TypeError, KeyError, OSError) as e:
        p.exit(2, 'BLOCKED: ' + str(e) + '\n')


if __name__ == '__main__':
    main()
