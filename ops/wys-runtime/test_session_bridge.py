"""Integration between the actual customer plugin writer and runtime reader."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import profile
import intake


PLUGIN = Path(__file__).parents[2] / 'plugins/wys-storefront/skills/wys-storefront'


class SessionBridgeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not (PLUGIN / 'scripts/session.py').exists():
            raise unittest.SkipTest('Requires the customer plugin from PR30 in the repository layout')

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / 'customer.json'
        spec = importlib.util.spec_from_file_location('plugin_session', PLUGIN / 'scripts/session.py')
        self.writer = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.writer)
        self.assertEqual(self.writer.BANK, intake.BANK)
        self.writer.mutate(self.path, 'init', customer='synthetic-customer')
        while (question := self.writer.next_question(self.writer.load(self.path))) is not None:
            qid = question['id']
            value = {'selected': question['options'][:1], 'detail': 'Exact café wording — keep this.'}
            if qid == 'categories':
                value['selected'] = ['clothing', 'home-decor']
            elif qid == 'category_preferences':
                value = {'categories': {cat: {branch['id']: {'selected': branch['options'][:1],
                         'detail': 'Exact branch detail'} for branch in branches}
                         for cat, branches in question['branches'].items()}}
            elif qid == 'generation_budget':
                value.update(period='per synthetic edit', max_attempts_per_role=1)
            self.writer.mutate(self.path, 'answer', qid=qid,
                data={'value': value, 'evidence': 'synthetic original source',
                      'answered_at': '2026-10-09T12:00:00+00:00'},
                revision=self.writer.load(self.path)['revision'])

    def prepare(self, digest, customer='synthetic-customer', step='basic'):
        return profile.prepare(self.path, customer, step, 'synthetic-edit', 'unused-master',
                               digest, 'unused-master-hash')

    def test_same_file_reads_complete_intake_and_exact_sources_without_copy(self):
        before = self.path.read_bytes()
        original = self.writer.load(self.path)
        compiled = profile.load(self.path)
        self.assertEqual(compiled['sha256'], original['sha256'])
        self.assertEqual(compiled['history'], original['history'])
        for qid, envelope in original['answers'].items():
            for key, value in envelope.items():
                self.assertEqual(compiled['answers']['intake.' + qid][key], value)
        self.assertEqual(intake.next_question(self.path)['result'], 'PREFERENCE_INTAKE_RECORDED')
        self.assertEqual(self.path.read_bytes(), before)

    def test_every_operation_blocks_missing_verified_operator_configuration(self):
        original_hash = self.writer.load(self.path)['sha256']
        for step in profile.STEPS:
            with self.subTest(step=step), self.assertRaisesRegex(profile.Blocked, 'SETUP_INCOMPLETE'):
                self.prepare(original_hash, step=step)

    def test_correction_in_same_file_invalidates_prepared_hash(self):
        original_hash = self.writer.load(self.path)['sha256']
        self.writer.mutate(self.path, 'answer', qid='business_direction', correction=True,
            data={'value': {'selected': [], 'detail': 'Explicit customer correction'},
                  'evidence': 'synthetic explicit correction', 'answered_at': '2026-10-09T13:00:00+00:00'},
            revision=self.writer.load(self.path)['revision'])
        self.assertNotEqual(profile.load(self.path)['sha256'], original_hash)
        with self.assertRaisesRegex(profile.Blocked, 'PROFILE_CHANGED_REBUILD_INPUTS'):
            self.prepare(original_hash)

    def test_runtime_writer_cannot_overwrite_plugin_state(self):
        before = self.path.read_bytes()
        current = self.writer.load(self.path)
        with self.assertRaisesRegex(profile.Blocked, 'SESSION_REQUIRES_PLUGIN_WRITER'):
            profile.save(self.path, 'synthetic-customer', {'state_location': {
                'value': 'synthetic private location', 'evidence': 'synthetic source',
                'answered_at': '2026-10-09T13:00:00+00:00'}}, current['revision'])
        self.assertEqual(self.path.read_bytes(), before)
        self.assertEqual(self.writer.load(self.path), current)

    def test_other_customer_cannot_use_this_session(self):
        with self.assertRaisesRegex(profile.Blocked, 'PROFILE_IDENTITY_MISMATCH'):
            self.prepare(self.writer.load(self.path)['sha256'], customer='another-customer')

    def test_operator_evidence_unblocks_preparation_and_corrections_invalidate_it(self):
        for field in self.writer.OPERATOR_FIELDS:
            raw = self.writer.load(self.path)
            self.writer.mutate(self.path, 'operator', qid=field,
                revision=raw['revision'], data={
                    'value': 'synthetic verified ' + field, 'evidence': 'synthetic readback only',
                    'answered_at': '2026-10-09T13:00:00+00:00',
                    'source_kind': 'operator_verified', 'verification_status': 'VERIFIED',
                    'answers_sha256': profile.digest(raw['answers'])})
        raw = self.writer.load(self.path)
        compiled = profile.load(self.path)
        master = self.path.with_name('synthetic-master.txt')
        master.write_text('synthetic governing instructions')
        import hashlib
        payload = profile.prepare(self.path, 'synthetic-customer', 'basic', 'fixture-edit',
            master, raw['sha256'], hashlib.sha256(master.read_bytes()).hexdigest())
        self.assertEqual(payload['configuration']['state_location'], 'synthetic verified state_location')
        self.assertEqual(compiled['answers']['reference_assets']['evidence'], 'synthetic readback only')
        self.writer.mutate(self.path, 'answer', qid='business_direction', correction=True,
            revision=raw['revision'], data={'value': {'selected': [], 'detail': 'explicit new direction'},
                'evidence': 'synthetic correction', 'answered_at': '2026-10-09T14:00:00+00:00'})
        updated = self.writer.load(self.path)
        self.assertNotIn('operator_verifications', updated)
        self.assertEqual(len(updated['history'][-1]['invalidated_operator_verifications']), 4)
        with self.assertRaisesRegex(profile.Blocked, 'SETUP_INCOMPLETE'):
            self.prepare(updated['sha256'])

    def test_operator_record_with_wrong_answer_binding_preserves_bytes(self):
        raw = self.writer.load(self.path)
        before = self.path.read_bytes()
        with self.assertRaisesRegex(ValueError, 'OPERATOR_VERIFICATION_BINDING_REQUIRED'):
            self.writer.mutate(self.path, 'operator', qid='state_location', revision=raw['revision'],
                data={'value': 'synthetic location', 'evidence': 'synthetic source',
                      'answered_at': '2026-10-09T13:00:00+00:00',
                      'source_kind': 'operator_verified', 'verification_status': 'VERIFIED',
                      'answers_sha256': 'stale-answer-hash'})
        self.assertEqual(self.path.read_bytes(), before)

    def test_hashed_blank_answer_still_fails_semantic_validation(self):
        document = self.writer.load(self.path)
        document['answers']['business_direction']['value'] = {'selected': [], 'detail': ''}
        document.pop('sha256')
        document['sha256'] = profile.digest(document)
        self.path.write_text(json.dumps(document))
        with self.assertRaisesRegex(profile.Blocked, 'SESSION_QUESTION_UNANSWERED'):
            profile.load(self.path)


if __name__ == '__main__':
    unittest.main()
