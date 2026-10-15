import copy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
import subprocess
import sys
from unittest.mock import patch

import profile as runtime


class ProfileTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.path = self.root / 'private-profile.json'
        self.master = self.root / 'master.md'
        self.master.write_text('Synthetic authority. Not a production workflow.')
        self.master_hash = hashlib.sha256(self.master.read_bytes()).hexdigest()
        self.answers = {key: self.answer('synthetic ' + key) for key in runtime.REQUIRED}
        self.answers['persona'] = self.answer(False)
        self.answers['reference_assets'] = self.answer([])
        self.answers['custom_question'] = self.answer('literal pink, lilacs, no bows')

    def answer(self, value):
        return {'value': value, 'evidence': 'fixture:test_profile, not Jodie answers',
                'answered_at': '2026-10-09T12:00:00+00:00'}

    def save(self, answers=None, revision=0):
        return runtime.save(self.path, 'synthetic-buyer',
                            self.answers if answers is None else answers,
                            revision, 'fixture')

    def prepare(self, saved=None, step='basic', kind='fixture'):
        saved = saved or runtime.load(self.path)
        return runtime.prepare(self.path, 'synthetic-buyer', step, 'synthetic-look',
                               self.master, saved['sha256'], self.master_hash, kind)

    def coverage(self, payload):
        return {key: {'input_sha256': runtime.digest(value), 'disposition': 'applied',
                      'evidence': 'synthetic application, not provider evidence'}
                for key, value in payload['configuration'].items()}

    def test_exact_answers_survive_new_process_read(self):
        saved = self.save()
        self.assertEqual(runtime.load(self.path)['answers'], self.answers)
        self.assertEqual(saved['revision'], 1)
        self.assertEqual(self.path.stat().st_mode & 0o777, 0o600)

    def test_each_step_carries_all_answers_including_custom_false_and_empty(self):
        saved = self.save()
        for step in runtime.STEPS:
            with self.subTest(step=step):
                payload = self.prepare(saved, step)
                self.assertEqual(payload['configuration'],
                                 {key: item['value'] for key, item in self.answers.items()})

    def test_partial_answer_saved_but_generation_input_blocked(self):
        self.save({'persona': self.answer(False)})
        with self.assertRaisesRegex(runtime.Blocked, 'SETUP_INCOMPLETE'):
            self.prepare()

    def test_private_visual_pilot_does_not_require_publication_setup(self):
        saved = self.save({key: self.answers[key] for key in runtime.VISUAL_REQUIRED})
        payload = runtime.prepare(self.path, 'synthetic-buyer', 'basic', 'pilot',
                                  self.master, saved['sha256'], self.master_hash,
                                  'fixture', 'visual_pilot')
        receipt = runtime.verify_handoff(self.path, self.master, payload, self.coverage(payload))
        self.assertEqual(receipt['result'], 'INPUT_BINDING_VERIFIED')
        with self.assertRaisesRegex(runtime.Blocked, 'SETUP_INCOMPLETE'):
            self.prepare(saved)
        for step in ('sourcing', 'blog', 'pinterest', 'instagram', 'reconciliation'):
            with self.assertRaisesRegex(runtime.Blocked, 'PILOT_CANNOT'):
                runtime.prepare(self.path, 'synthetic-buyer', step, 'pilot',
                                self.master, saved['sha256'], self.master_hash,
                                'fixture', 'visual_pilot')

    def test_recovered_instruction_preserves_unknown_original_timestamp(self):
        answer = {'value': 'literal recovered instruction',
                  'evidence': 'fixture archive, not founder data',
                  'source_kind': 'recovered_direct_instruction',
                  'answered_at': None, 'recorded_at': '2026-10-09T12:00:00+00:00'}
        saved = self.save({'personal_visual_signature': answer})
        self.assertEqual(saved['answers']['personal_visual_signature'], answer)
        answer['answered_at'] = answer['recorded_at']
        with self.assertRaisesRegex(runtime.Blocked, 'TIMESTAMP_INVALID'):
            self.save({'personal_visual_signature': answer}, 1)

    def test_missing_profile_blocks(self):
        with self.assertRaisesRegex(runtime.Blocked, 'PROFILE_MISSING'):
            runtime.load(self.path)

    def test_unverified_answer_is_not_complete_setup(self):
        self.answers['curation_profile'] = self.answer('UNVERIFIED')
        self.save()
        with self.assertRaisesRegex(runtime.Blocked, 'SETUP_UNRESOLVED'):
            self.prepare()

    def test_partial_resume_preserves_previous_answers(self):
        self.save({'persona': self.answer(False)})
        saved = self.save({'curation_profile': self.answer('exact new answer')}, 1)
        self.assertFalse(saved['answers']['persona']['value'])
        self.assertEqual(len(saved['history']), 2)

    def test_update_invalidates_previously_prepared_input(self):
        saved = self.save()
        payload = self.prepare(saved)
        self.save({'curation_profile': self.answer('new confirmed preference')}, 1)
        with self.assertRaisesRegex(runtime.Blocked, 'PROFILE_CHANGED'):
            runtime.verify_handoff(self.path, self.master, payload, self.coverage(payload))

    def test_stale_write_cannot_overwrite_answer(self):
        self.save()
        with self.assertRaisesRegex(runtime.Blocked, 'REVISION_CONFLICT'):
            self.save({'persona': self.answer(True)}, 0)
        self.assertFalse(runtime.load(self.path)['answers']['persona']['value'])

    def test_tampering_is_detected(self):
        saved = self.save()
        saved['answers']['persona']['value'] = True
        self.path.write_text(json.dumps(saved))
        with self.assertRaisesRegex(runtime.Blocked, 'HASH_MISMATCH'):
            self.prepare()

    def test_wrong_customer_cannot_read_or_overwrite(self):
        saved = self.save()
        with self.assertRaisesRegex(runtime.Blocked, 'IDENTITY_MISMATCH'):
            runtime.prepare(self.path, 'other-buyer', 'basic', 'look', self.master,
                            saved['sha256'], self.master_hash, 'fixture')
        with self.assertRaisesRegex(runtime.Blocked, 'IDENTITY_MISMATCH'):
            runtime.save(self.path, 'other-buyer', self.answers, 1, 'fixture')

    def test_fixture_cannot_be_used_as_customer_configuration(self):
        self.save()
        with self.assertRaisesRegex(runtime.Blocked, 'IDENTITY_MISMATCH'):
            self.prepare(kind='customer')

    def test_changed_master_requires_review(self):
        self.save()
        self.master.write_text('Changed authority')
        with self.assertRaisesRegex(runtime.Blocked, 'MASTER_CHANGED'):
            self.prepare()

    def test_missing_original_answer_evidence_cannot_save(self):
        answers = copy.deepcopy(self.answers)
        answers['persona'].pop('evidence')
        with self.assertRaisesRegex(runtime.Blocked, 'EVIDENCE_MISSING'):
            self.save(answers)
        self.assertFalse(self.path.exists())

    def test_answer_not_reported_by_step_blocks_receipt(self):
        self.save()
        payload = self.prepare()
        coverage = self.coverage(payload)
        coverage.pop('curation_profile')
        with self.assertRaisesRegex(runtime.Blocked, 'COVERAGE_MISMATCH'):
            runtime.verify_handoff(self.path, self.master, payload, coverage)

    def test_ignored_or_changed_answer_blocks_receipt(self):
        self.save()
        payload = self.prepare()
        coverage = self.coverage(payload)
        coverage['personal_visual_signature']['input_sha256'] = runtime.digest('generic beige')
        with self.assertRaisesRegex(runtime.Blocked, 'ANSWER_VALUE_MISMATCH'):
            runtime.verify_handoff(self.path, self.master, payload, coverage)
        coverage = self.coverage(payload)
        coverage['persona']['evidence'] = ''
        with self.assertRaisesRegex(runtime.Blocked, 'USAGE_EVIDENCE_MISSING'):
            runtime.verify_handoff(self.path, self.master, payload, coverage)

    def test_modified_payload_is_rejected(self):
        self.save()
        payload = self.prepare()
        payload['configuration']['persona'] = True
        with self.assertRaisesRegex(runtime.Blocked, 'INPUT_PAYLOAD_MISMATCH'):
            runtime.verify_handoff(self.path, self.master, payload, self.coverage(payload))

    def test_lock_blocks_concurrent_writer_and_preserves_profile(self):
        saved = self.save()
        Path(str(self.path) + '.lock').write_text('active writer')
        with self.assertRaisesRegex(runtime.Blocked, 'WRITE_IN_PROGRESS'):
            self.save({'persona': self.answer(True)}, 1)
        self.assertEqual(runtime.load(self.path), saved)

    def test_failed_atomic_replace_keeps_previous_answer(self):
        saved = self.save()
        with patch('profile.os.replace', side_effect=OSError('injected failure')):
            with self.assertRaises(OSError):
                self.save({'persona': self.answer(True)}, 1)
        self.assertEqual(runtime.load(self.path), saved)
        self.assertFalse(Path(str(self.path) + '.lock').exists())

    @unittest.skipIf(runtime.fcntl is None, 'POSIX lease backend unavailable')
    def test_live_process_blocks_write_and_killed_process_releases_lease(self):
        saved = self.save()
        before = self.path.read_bytes()
        code = ("import profile, signal, sys\n"
                "with profile.write_lease(sys.argv[1]):\n"
                " print('READY', flush=True)\n"
                " signal.pause()\n")
        child = subprocess.Popen([sys.executable, '-c', code, str(self.path)],
                                 cwd=Path(__file__).parent, stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE, text=True)
        try:
            self.assertEqual(child.stdout.readline().strip(), 'READY')
            with self.assertRaisesRegex(runtime.Blocked, 'WRITE_IN_PROGRESS'):
                self.save({'persona': self.answer(True)}, saved['revision'])
            self.assertEqual(self.path.read_bytes(), before)
            child.kill()
            child.wait(timeout=5)
            updated = self.save({'persona': self.answer(True)}, saved['revision'])
            self.assertTrue(updated['answers']['persona']['value'])
            self.assertEqual(updated['revision'], saved['revision'] + 1)
            self.assertTrue(Path(str(self.path) + '.write-lease').exists())
        finally:
            if child.poll() is None:
                child.kill()
                child.wait(timeout=5)
            child.stdout.close()
            child.stderr.close()

    def test_legacy_lock_is_never_deleted_based_on_age(self):
        saved = self.save()
        lock = Path(str(self.path) + '.lock')
        lock.write_text('legacy owner must be reconciled')
        import os
        os.utime(lock, (0, 0))
        with self.assertRaisesRegex(runtime.Blocked, 'LEGACY_LOCK_RECONCILE_REQUIRED'):
            self.save({'persona': self.answer(True)}, saved['revision'])
        self.assertEqual(lock.read_text(), 'legacy owner must be reconciled')
        self.assertEqual(runtime.load(self.path), saved)

    def test_binding_receipt_never_claims_execution_or_output_pass(self):
        self.save()
        payload = self.prepare()
        receipt = runtime.verify_handoff(self.path, self.master, payload, self.coverage(payload))
        self.assertEqual(receipt['result'], 'INPUT_BINDING_VERIFIED')
        self.assertEqual(receipt['external_execution'], 'NOT_RUN')
        self.assertEqual(receipt['output_acceptance'], 'NOT_RUN')


if __name__ == '__main__':
    unittest.main()
