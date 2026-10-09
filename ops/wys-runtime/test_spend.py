import copy
from pathlib import Path
import tempfile
import unittest
from profile import Blocked
from spend import reserve, record_result


class SpendTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name) / 'ledger.json'
        self.policy = {'provider': 'synthetic', 'model': 'fixture', 'unit': 'synthetic',
                       'per_attempt': 2, 'limit': 6, 'max_attempts': 3,
                       'profile_sha256': 'synthetic', 'authorization_evidence': 'FIXTURE',
                       'paused': False}

    def test_no_policy_and_paused_policy_block(self):
        with self.assertRaisesRegex(Blocked, 'POLICY_INCOMPLETE'):
            reserve(self.path, {}, 'a', 'payload', 0)
        self.policy['paused'] = True
        with self.assertRaisesRegex(Blocked, 'GENERATION_PAUSED'):
            reserve(self.path, self.policy, 'a', 'payload', 0)

    def test_failed_jobs_and_corrections_exhaust_attempt_limit(self):
        revision = 0
        for n in range(3):
            state = reserve(self.path, self.policy, str(n), 'payload', revision)
            state = record_result(self.path, str(n), 'failed', 'synthetic failure', state['revision'])
            revision = state['revision']
        with self.assertRaisesRegex(Blocked, 'ATTEMPT_LIMIT_REACHED'):
            reserve(self.path, self.policy, 'fourth', 'payload', revision)

    def test_budget_limits_submission_before_cost_is_incurred(self):
        self.policy['limit'] = 1
        with self.assertRaisesRegex(Blocked, 'SPEND_LIMIT_REACHED'):
            reserve(self.path, self.policy, 'a', 'payload', 0)
        self.assertFalse(self.path.exists())

    def test_lost_response_blocks_new_attempt_and_duplicate_retry(self):
        state = reserve(self.path, self.policy, 'a', 'payload', 0)
        state = record_result(self.path, 'a', 'write_outcome_unknown', 'response lost', state['revision'])
        with self.assertRaisesRegex(Blocked, 'UNCERTAIN_ATTEMPT'):
            reserve(self.path, self.policy, 'b', 'payload', state['revision'])
        with self.assertRaisesRegex(Blocked, 'ATTEMPT_EXISTS'):
            reserve(self.path, self.policy, 'a', 'payload', state['revision'])

    def test_reconciliation_releases_next_attempt_without_erasing_old_cost(self):
        state = reserve(self.path, self.policy, 'a', 'payload', 0)
        state = record_result(self.path, 'a', 'succeeded', 'synthetic job id', state['revision'], 2)
        state = reserve(self.path, self.policy, 'b', 'new payload', state['revision'])
        self.assertEqual(sum(a['reserved_cost'] for a in state['attempts'].values()), 4)

    def test_silent_provider_or_model_swap_blocked(self):
        state = reserve(self.path, self.policy, 'a', 'payload', 0)
        state = record_result(self.path, 'a', 'failed', 'synthetic', state['revision'])
        changed = copy.deepcopy(self.policy)
        changed['provider'] = 'higgsfield'
        with self.assertRaisesRegex(Blocked, 'POLICY_CHANGED'):
            reserve(self.path, changed, 'b', 'payload', state['revision'])

    def test_observed_overage_blocks_more_work(self):
        state = reserve(self.path, self.policy, 'a', 'payload', 0)
        state = record_result(self.path, 'a', 'succeeded', 'observed cost', state['revision'], 8)
        with self.assertRaisesRegex(Blocked, 'SPEND_LIMIT_REACHED'):
            reserve(self.path, self.policy, 'b', 'payload', state['revision'])

    def test_nonfinite_or_negative_budget_blocks(self):
        for value in (-1, float('nan'), float('inf'), True):
            with self.subTest(value=value):
                changed = copy.deepcopy(self.policy)
                changed['limit'] = value
                with self.assertRaisesRegex(Blocked, 'SPEND_AMOUNT_INVALID'):
                    reserve(self.path, changed, 'a', 'payload', 0)


if __name__ == '__main__':
    unittest.main()
