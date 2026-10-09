import copy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from profile import Blocked
from mini_test import CHECKS, blank_suite, batch_gate, category_inventory, validate_category


class MiniTestTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.source = self.root / 'categories.js'
        self.names = ['clothing', 'accessories', 'jewelry', 'beauty', 'perfume',
                      'home-decor', 'dorm', 'car', 'books', 'gifts']
        self.source.write_text('export const CATEGORIES = [' +
                               ','.join('{ slug: "' + n + '" }' for n in self.names) + '];')

    def record(self):
        assets = []
        for role in ('basic', 'styled', 'lifestyle'):
            path = self.root / (role + '.txt')
            path.write_text('Synthetic test bytes, not image acceptance: ' + role)
            assets.append({'role': role, 'path': str(path),
                           'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                           'visually_reviewed': True, 'review_evidence': 'FIXTURE ONLY'})
        return {'category': 'clothing', 'fixture': True, 'profile_sha256': 'profile', 'master_sha256': 'master',
                'look_id': 'SYNTHETIC', 'checks': {k: {'result': 'PASS', 'evidence': 'FIXTURE',
                'reviewed_at': '2026-10-09T12:00:00+00:00'} for k in CHECKS}, 'assets': assets}

    def test_all_ten_categories_start_not_run_and_block_batches(self):
        suite = blank_suite(self.source, 'profile', 'master')
        self.assertEqual(category_inventory(self.source), self.names)
        for category in self.names:
            with self.subTest(category=category):
                with self.assertRaisesRegex(Blocked, 'MINI_TEST_NOT_PASSED'):
                    batch_gate(suite, category, self.source, 'profile', 'master')

    def test_new_category_cannot_escape_test_matrix(self):
        suite = blank_suite(self.source, 'profile', 'master')
        self.source.write_text(self.source.read_text().replace('];', ',{slug:"new-category"}];'))
        with self.assertRaisesRegex(Blocked, 'CATEGORY_COVERAGE_MISMATCH'):
            batch_gate(suite, 'clothing', self.source, 'profile', 'master')

    def test_every_missing_check_blocks_each_category(self):
        for category in self.names:
            for check in CHECKS:
                with self.subTest(category=category, check=check):
                    record = self.record()
                    record['checks'].pop(check)
                    with self.assertRaisesRegex(Blocked, 'CHECKS_INCOMPLETE'):
                        validate_category(record, 'profile', 'master', fixture=True)

    def test_failed_visual_check_blocks(self):
        record = self.record()
        record['checks']['visual_inspection']['result'] = 'FAIL'
        with self.assertRaisesRegex(Blocked, 'FAILED_OR_UNVERIFIED'):
            validate_category(record, 'profile', 'master', fixture=True)

    def test_recorded_rejection_overrides_later_pass_checkboxes(self):
        record = self.record()
        registry = self.root / 'rejected.json'
        registry.write_text(json.dumps({'schema': 1, 'assets': {
            record['assets'][1]['sha256']: {'reason': 'synthetic rejection evidence'}}}))
        with self.assertRaisesRegex(Blocked, 'ASSET_REJECTED:styled'):
            validate_category(record, 'profile', 'master', fixture=True, rejection_path=registry)

    def test_missing_rejection_registry_cannot_silently_pass(self):
        with self.assertRaisesRegex(Blocked, 'REJECTION_REGISTRY_UNAVAILABLE'):
            validate_category(self.record(), 'profile', 'master', fixture=True,
                              rejection_path=self.root / 'missing.json')

    def test_missing_and_duplicate_images_block(self):
        record = self.record()
        record['assets'].pop()
        with self.assertRaisesRegex(Blocked, 'THREE_ROLES_MISSING'):
            validate_category(record, 'profile', 'master', fixture=True)
        record = self.record()
        record['assets'][1]['sha256'] = record['assets'][0]['sha256']
        with self.assertRaisesRegex(Blocked, 'DUPLICATE_IMAGE'):
            validate_category(record, 'profile', 'master', fixture=True)

    def test_changed_asset_or_profile_invalidates_pass(self):
        record = self.record()
        Path(record['assets'][0]['path']).write_text('Changed')
        with self.assertRaisesRegex(Blocked, 'ASSET_CHANGED'):
            validate_category(record, 'profile', 'master', fixture=True)
        record = self.record()
        with self.assertRaisesRegex(Blocked, 'PROFILE_CHANGED'):
            validate_category(record, 'changed', 'master', fixture=True)

    def test_fixture_pass_never_enables_production(self):
        record = self.record()
        self.assertEqual(validate_category(record, 'profile', 'master', fixture=True)['result'],
                         'FIXTURE_ONLY')
        with self.assertRaisesRegex(Blocked, 'FIXTURE_PRODUCTION_MISMATCH'):
            validate_category(record, 'profile', 'master')

    def test_one_category_pass_cannot_be_transferred_to_another(self):
        with self.assertRaisesRegex(Blocked, 'MINI_TEST_CATEGORY_MISMATCH'):
            validate_category(self.record(), 'profile', 'master', fixture=True, expected_category='car')


if __name__ == '__main__':
    unittest.main()
