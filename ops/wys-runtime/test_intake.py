import tempfile
import hashlib
import unittest
from pathlib import Path
import intake
import profile
import json


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

    def test_blank_structured_answer_does_not_advance_or_mutate_profile(self):
        self.record('aesthetic', 'Existing exact style', 0)
        before = self.path.read_bytes()
        for value in ({}, [], {'selected': [], 'detail': ''},
                      {'selected': [], 'detail': '   '}):
            with self.subTest(value=value):
                with self.assertRaisesRegex(profile.Blocked, 'QUESTION_UNANSWERED'):
                    self.record('business_direction', value, 1)
                self.assertEqual(self.path.read_bytes(), before)
                self.assertEqual(intake.next_question(self.path)['question_id'], 'business_direction')

    def test_custom_structured_answer_and_false_persona_are_preserved(self):
        answer = {'selected': [], 'detail': 'Exact custom audience'}
        saved = self.record('business_direction', answer, 0)
        self.assertEqual(saved['answers']['intake.business_direction']['value'], answer)
        saved = self.record('persona_choice', False, 1)
        self.assertNotIn('persona_world', intake.missing_questions(saved['answers']))

    def form_file(self, answers):
        file = self.path.parent / 'form.json'
        file.write_text(json.dumps({'schema_version': 2, 'questionnaire_version': 2,
                                    'answers': answers}))
        return file

    def form_answer(self, selected=None, detail='', **extra):
        return {'value': {'selected': selected or [], 'detail': detail, **extra},
                'answered_at': '2026-10-09T14:00:00+00:00'}

    def test_form_import_preserves_exact_answer_and_does_not_record_blank(self):
        answer = self.form_answer(['Complete outfits they can recreate'], 'My exact words')
        file = self.form_file({'business_direction': answer,
                              'aesthetic': self.form_answer()})
        result = intake.import_form(self.path, 'fixture', file, 0, 'fixture')
        self.assertEqual(result['imported'], 1)
        self.assertEqual(profile.load(self.path)['answers']['intake.business_direction']['value'], answer['value'])
        self.assertEqual(intake.next_question(self.path)['question_id'], 'categories')

    def test_form_import_refuses_overwriting_existing_answer_before_any_save(self):
        self.record('business_direction', 'Existing exact answer', 0)
        file = self.form_file({'business_direction': self.form_answer(['Complete outfits they can recreate'])})
        with self.assertRaisesRegex(profile.Blocked, 'EXPLICIT_CORRECTION_REQUIRED'):
            intake.import_form(self.path, 'fixture', file, 1, 'fixture')
        self.assertEqual(profile.load(self.path)['revision'], 1)

    def test_selected_category_requires_its_complete_branch(self):
        file = self.form_file({'categories': self.form_answer(['car']),
                              'category_preferences': self.form_answer(categories={'car': {'shopper_use': ['Daily commute']}})})
        with self.assertRaisesRegex(profile.Blocked, 'CATEGORY_BRIEF_INCOMPLETE:car:style_function'):
            intake.import_form(self.path, 'fixture', file, 0, 'fixture')
        self.assertFalse(self.path.exists())

    def test_custom_category_brief_survives_import_and_resume(self):
        category = 'Pet supplies'
        brief = {'shopper_use': 'Indoor adult cats', 'style_function': 'Washable feeding area',
                 'requirements': 'Exact bowl dimensions and dishwasher-safe listing evidence'}
        file = self.form_file({'categories': self.form_answer([category])})
        intake.import_form(self.path, 'fixture', file, 0, 'fixture')
        file = self.form_file({'category_preferences': self.form_answer(categories={category: brief})})
        intake.import_form(self.path, 'fixture', file, 1, 'fixture')
        saved = profile.load(self.path)
        self.assertEqual(saved['answers']['product_categories']['value']['selected'], [category])
        self.assertEqual(saved['answers']['curation_profile']['value']['category_preferences']['categories'][category], brief)

    def test_custom_category_cannot_skip_its_requirements(self):
        file = self.form_file({'categories': self.form_answer(['Pet supplies']),
                              'category_preferences': self.form_answer(categories={'Pet supplies': {
                                  'shopper_use': 'Cats', 'style_function': 'Feeding', 'requirements': '   '}})})
        with self.assertRaisesRegex(profile.Blocked, 'CATEGORY_BRIEF_INCOMPLETE:Pet supplies:requirements'):
            intake.import_form(self.path, 'fixture', file, 0, 'fixture')
        self.assertFalse(self.path.exists())

    def test_invalid_category_names_do_not_mutate_profile(self):
        for category in ('', '   ', '__proto__', 'constructor', 'prototype', 12):
            with self.subTest(category=category):
                file = self.form_file({'categories': self.form_answer([category])})
                with self.assertRaisesRegex(profile.Blocked, 'CATEGORY_SELECTION_INVALID'):
                    intake.import_form(self.path, 'fixture', file, 0, 'fixture')
                self.assertFalse(self.path.exists())

    def test_guided_no_persona_answer_skips_persona_world(self):
        self.record('persona_choice', {'selected': ['No person: use the separately tested no-persona version'], 'detail': ''}, 0)
        self.assertNotIn('persona_world', intake.missing_questions(profile.load(self.path)['answers']))

    def test_paid_budget_checkbox_without_amounts_cannot_be_imported(self):
        file = self.form_file({'generation_budget': self.form_answer(
            ['A finite credit allowance'], max_attempts_per_role=2, period='one mini test')})
        with self.assertRaisesRegex(profile.Blocked, 'FINITE_PAID_ALLOWANCE_REQUIRED'):
            intake.import_form(self.path, 'fixture', file, 0, 'fixture')
        self.assertFalse(self.path.exists())

    def test_no_paid_generation_still_requires_a_finite_attempt_limit(self):
        file = self.form_file({'generation_budget': self.form_answer(['No paid generation'])})
        with self.assertRaisesRegex(profile.Blocked, 'FINITE_ATTEMPT_ALLOWANCE_REQUIRED'):
            intake.import_form(self.path, 'fixture', file, 0, 'fixture')

    def test_cadence_has_no_invented_frequency_tiers(self):
        self.assertEqual(intake.CHOICES['cadence'],
                         ['Use my existing confirmed posting plan', 'Configure a new posting plan'])
        self.record('cadence', {'source': 'synthetic confirmed schedule',
                               'looks_per_week': 11, 'spacing_days': 3}, 0)
        self.assertNotIn('cadence', intake.missing_questions(profile.load(self.path)['answers']))
        self.assertEqual(profile.load(self.path)['answers']['cadence']['value']['looks_per_week'], 11)

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

