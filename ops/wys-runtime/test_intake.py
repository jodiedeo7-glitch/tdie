import tempfile
import hashlib
import unittest
from pathlib import Path
import intake
import profile


class IntakeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name) / 'private.json'

    def record(self, question, value, revision):
        return intake.record_answer(self.path, 'fixture', question, value,
                                    'synthetic test only', '2026-10-09T13:30:00+00:00',
                                    revision, 'fixture')

    def test_resume_survives_disk_reload_and_preserves_literal_answer(self):
        self.assertEqual(intake.next_question(self.path)['question_id'], 'business_direction')
        self.record('business_direction', 'Book finds for readers; NOT fashion', 0)
        self.assertEqual(intake.next_question(self.path)['question_id'], 'categories')
        self.assertEqual(profile.load(self.path)['answers']['curation_profile']['value']['business_direction'],
                         'Book finds for readers; NOT fashion')

    def test_grouped_preferences_merge_without_losing_sources(self):
        self.record('aesthetic', 'colorful illustrated reading corners', 0)
        self.record('visual_exclusions', ['no pink', 'no glitter'], 1)
        answer = profile.load(self.path)['answers']['personal_visual_signature']
        self.assertEqual(answer['value']['aesthetic'], 'colorful illustrated reading corners')
        self.assertEqual(answer['value']['visual_exclusions'], ['no pink', 'no glitter'])
        self.assertEqual(set(answer['component_evidence']), {'aesthetic', 'visual_exclusions'})

    def test_recovered_instructions_survive_new_answers_with_original_provenance(self):
        prior = {'value': {'palette': 'source-backed literal'}, 'evidence': 'synthetic recovered archive',
                 'source_kind': 'recovered_direct_instruction', 'answered_at': None,
                 'recorded_at': '2026-10-09T13:30:00+00:00'}
        profile.save(self.path, 'fixture', {'personal_visual_signature': prior}, 0, 'fixture')
        self.record('aesthetic', 'new exact answer', 1)
        answer = profile.load(self.path)['answers']['personal_visual_signature']
        self.assertEqual(answer['value']['palette'], 'source-backed literal')
        self.assertIsNone(answer['component_evidence']['_recovered_or_prior']['answered_at'])
        self.assertEqual(profile.load(self.path)['history'][0]['answers']['personal_visual_signature'], prior)

    def test_no_selection_is_not_an_answer(self):
        for value in (None, '', 'No selection'):
            with self.assertRaisesRegex(profile.Blocked, 'QUESTION_UNANSWERED'):
                self.record('business_direction', value, 0)
        self.assertFalse(self.path.exists())

    def test_no_persona_skips_only_persona_world(self):
        revision = 0
        for question, field, prompt in intake.QUESTIONS:
            if question == 'persona_world':
                continue
            self.record(question, 'no_persona' if question == 'persona_choice' else 'synthetic answer', revision)
            revision += 1
        self.assertEqual(intake.next_question(self.path)['result'], 'PREFERENCE_INTAKE_RECORDED')

    def test_stale_answer_cannot_overwrite_profile(self):
        self.record('business_direction', 'first literal', 0)
        with self.assertRaisesRegex(profile.Blocked, 'REVISION_CONFLICT'):
            self.record('business_direction', 'stale replacement', 0)
        self.assertEqual(profile.load(self.path)['answers']['intake.business_direction']['value'], 'first literal')

    def test_partially_grouped_answer_does_not_make_interview_complete(self):
        saved = self.record('business_direction', 'synthetic reader niche', 0)
        master = self.path.parent / 'master.txt'
        master.write_text('synthetic authority')
        with self.assertRaisesRegex(profile.Blocked, 'INTERVIEW_INCOMPLETE:categories'):
            profile.prepare(self.path, 'fixture', 'basic', 'fixture-look', master,
                            saved['sha256'], hashlib.sha256(master.read_bytes()).hexdigest(),
                            'fixture', 'visual_pilot')

    def test_finished_interview_reaches_each_step_without_losing_raw_answers(self):
        revision = 0
        for question, field, prompt in intake.QUESTIONS:
            if question == 'persona_world':
                continue
            self.record(question, 'no_persona' if question == 'persona_choice' else 'fixture ' + question,
                        revision)
            revision += 1
        additions = {key: {'value': 'verified synthetic ' + key, 'evidence': 'fixture only',
                           'answered_at': '2026-10-09T13:30:00+00:00'}
                     for key in intake.OPERATOR_FIELDS}
        saved = profile.save(self.path, 'fixture', additions, revision, 'fixture')
        master = self.path.parent / 'master.txt'
        master.write_text('synthetic authority')
        for step in profile.STEPS:
            payload = profile.prepare(self.path, 'fixture', step, 'fixture-look', master,
                                      saved['sha256'], hashlib.sha256(master.read_bytes()).hexdigest(), 'fixture')
            for question, field, prompt in intake.QUESTIONS:
                if question != 'persona_world':
                    self.assertEqual(payload['configuration']['intake.' + question],
                                     saved['answers']['intake.' + question]['value'])


if __name__ == '__main__':
    unittest.main()
