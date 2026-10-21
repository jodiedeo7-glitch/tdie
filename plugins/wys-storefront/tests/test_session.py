"""Relocated package/CLI regressions with synthetic customers; no external calls."""
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class CustomerSessionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)
        self.package = self.directory / 'relocated-plugin'
        shutil.copytree(ROOT, self.package, ignore=shutil.ignore_patterns('__pycache__'))
        self.script = self.package / 'skills/wys-storefront/scripts/session.py'
        self.state = self.directory / 'private/customer.json'
        self.payload = self.directory / 'answer.json'
        spec = importlib.util.spec_from_file_location('customer_session', self.script)
        self.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.module)
        self.cli('init', '--customer', 'synthetic-customer')

    def cli(self, command, *arguments, error=None):
        result = subprocess.run([sys.executable, str(self.script), command,
                                 '--state', str(self.state), *arguments],
                                capture_output=True, text=True, timeout=10)
        if error:
            self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
            self.assertIn(error, result.stderr)
            return
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)

    def answer(self, question, value, *, correction=False, revision=None, error=None):
        data = {'value': value, 'evidence': 'synthetic fixture: exact customer wording',
                'answered_at': '2026-10-09T12:00:00+00:00'}
        self.payload.write_text(json.dumps(data, ensure_ascii=False))
        current = self.cli('status')['revision'] if revision is None else revision
        options = ['--question', question, '--input', str(self.payload),
                   '--revision', str(current)]
        if correction:
            options.append('--correction')
        self.cli('answer', *options, error=error)
        return data

    def complete(self, no_person=False):
        expected = {}
        while (question := self.cli('next')) is not None:
            qid = question['id']
            value = {'selected': question['options'][:1],
                     'detail': 'Exact synthetic wording — preserve punctuation and café.'}
            if qid == 'categories':
                value['selected'] = list(self.module.BANK['category_branches'])
            elif qid == 'category_preferences':
                value = {'categories': {
                    cat: {branch['id']: {'selected': branch['options'][:1],
                                        'detail': 'Exact ' + cat + ' requirement'}
                          for branch in branches}
                    for cat, branches in question['branches'].items()}}
            elif qid == 'persona_choice' and no_person:
                value['selected'] = [question['options'][-1]]
            elif qid == 'generation_budget':
                value.update(period='per synthetic edit', max_attempts_per_role=1)
            expected[qid] = self.answer(qid, value)
        saved = self.module.load(self.state)
        self.assertEqual(saved['answers'], expected)
        self.assertEqual(self.cli('status')['intake_status'], 'RECORDED')
        self.assertEqual(self.cli('status')['generation'], 'NOT_RUN')
        self.assertEqual(self.cli('status')['publication'], 'NOT_RUN')
        return saved

    def test_relocated_cli_retains_all_answers_and_all_ten_category_briefs(self):
        saved = self.complete()
        self.assertEqual(len(saved['answers']), 21)
        self.assertEqual(len(saved['answers']['category_preferences']['value']['categories']), 10)
        before = self.state.read_bytes()
        self.cli('init', '--customer', 'synthetic-customer')
        self.assertIsNone(self.cli('next'))
        self.assertEqual(self.state.read_bytes(), before)

    def test_no_person_resume_skips_only_persona_world(self):
        saved = self.complete(no_person=True)
        self.assertNotIn('persona_world', saved['answers'])
        self.assertEqual(len(saved['answers']), 20)

    def test_blank_stale_and_unapproved_correction_preserve_saved_bytes(self):
        before = self.state.read_bytes()
        self.answer('business_direction', {'selected': [], 'detail': '  '}, error='QUESTION_UNANSWERED')
        self.assertEqual(self.state.read_bytes(), before)
        value = {'selected': self.module.QUESTIONS['business_direction']['options'][:1], 'detail': 'precise'}
        self.answer('business_direction', value)
        before = self.state.read_bytes()
        self.answer('business_direction', value, revision=0, error='REVISION_CONFLICT')
        self.answer('business_direction', value, error='EXPLICIT_CORRECTION_REQUIRED')
        self.assertEqual(self.state.read_bytes(), before)

    def test_category_correction_preserves_old_brief_and_requests_new_one(self):
        self.complete()
        self.answer('categories', {'selected': ['clothing'], 'detail': 'explicit correction'}, correction=True)
        saved = self.module.load(self.state)
        self.assertEqual(self.cli('next')['id'], 'category_preferences')
        self.assertNotIn('category_preferences', saved['answers'])
        self.assertEqual(len(saved['history'][-1]['invalidated_category_brief']['value']['categories']), 10)

    def test_live_writer_blocks_and_killed_writer_releases_lease(self):
        if self.module.fcntl is None:
            self.skipTest('POSIX flock required')
        child = subprocess.Popen([sys.executable, '-c',
            'import importlib.util,signal,sys; from pathlib import Path; '
            's=importlib.util.spec_from_file_location("session",sys.argv[1]); '
            'm=importlib.util.module_from_spec(s); s.loader.exec_module(m); '
            'lease=m.write_lease(Path(sys.argv[2])); lease.__enter__(); '
            'print("READY",flush=True); signal.pause()', str(self.script), str(self.state)],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        try:
            self.assertEqual(child.stdout.readline().strip(), 'READY')
            before = self.state.read_bytes()
            self.cli('init', '--customer', 'synthetic-customer', error='WRITE_IN_PROGRESS')
            self.assertEqual(self.state.read_bytes(), before)
            child.kill()
            child.wait(timeout=5)
            self.answer('business_direction', {'selected': [], 'detail': 'recovered after process death'})
            self.assertEqual(self.cli('status')['revision'], 1)
            self.assertTrue(Path(str(self.state) + '.write-lease').exists())
        finally:
            if child.poll() is None:
                child.kill()
                child.wait(timeout=5)
            child.stdout.close()
            child.stderr.close()

    def test_legacy_marker_is_never_removed_by_age(self):
        legacy = Path(str(self.state) + '.lock')
        legacy.write_text('existing version marker')
        before = self.state.read_bytes()
        self.cli('init', '--customer', 'synthetic-customer', error='LEGACY_LOCK_RECONCILE_REQUIRED')
        self.assertEqual(self.state.read_bytes(), before)
        self.assertTrue(legacy.exists())


if __name__ == '__main__':
    unittest.main()
