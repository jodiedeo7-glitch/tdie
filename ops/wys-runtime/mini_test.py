"""One-look category acceptance records. Never treat static QA as visual QA."""
import hashlib
import json
import re
from pathlib import Path

from profile import Blocked, digest

CHECKS = ('answers_applied', 'product_facts_and_variants', 'source_rights',
          'product_reference_attachments', 'basic_product_inventory',
          'styled_role_distinction', 'lifestyle_role_and_identity',
          'personalization_and_exclusions', 'physical_scene_plausibility',
          'prompt_length', 'three_actual_images', 'visual_inspection',
          'finished_typography', 'pin_and_carousel_copy',
          'destination_and_disclosure', 'budget_and_attempt_log',
          'resume_without_duplicate_generation')


def category_inventory(source_path):
    """Read actual registered categories, so a new category cannot be skipped."""
    text = Path(source_path).read_text(encoding='utf-8')
    match = re.search(r'export const CATEGORIES\s*=\s*\[(.*?)\];', text, re.S)
    if not match:
        raise Blocked('CATEGORY_SOURCE_UNRECOGNIZED')
    values = re.findall(r'slug:\s*["\']([^"\']+)["\']', match.group(1))
    if not values or len(values) != len(set(values)):
        raise Blocked('CATEGORY_SOURCE_INVALID')
    return values


def blank_suite(source_path, profile_hash, master_hash):
    return {'schema': 1, 'category_source_sha256':
            hashlib.sha256(Path(source_path).read_bytes()).hexdigest(),
            'profile_sha256': profile_hash, 'master_sha256': master_hash,
            'categories': {category: {'status': 'NOT_RUN', 'look_id': None,
                                     'checks': {}, 'assets': []}
                           for category in category_inventory(source_path)}}


def validate_category(record, profile_hash, master_hash, fixture=False, expected_category=None,
                      rejection_path=None):
    if not record.get('category') or (expected_category is not None and record['category'] != expected_category):
        raise Blocked('MINI_TEST_CATEGORY_MISMATCH')
    if record.get('fixture', False) != fixture:
        raise Blocked('FIXTURE_PRODUCTION_MISMATCH')
    if record.get('profile_sha256') != profile_hash:
        raise Blocked('MINI_TEST_PROFILE_CHANGED')
    if record.get('master_sha256') != master_hash:
        raise Blocked('MINI_TEST_MASTER_CHANGED')
    if not record.get('look_id'):
        raise Blocked('MINI_TEST_LOOK_MISSING')
    # A later PASS checkbox cannot erase a recorded rejection of the same bytes.
    registry = Path(rejection_path) if rejection_path else Path(__file__).with_name('rejected-assets.json')
    try:
        rejected = json.loads(registry.read_text())
        if rejected.get('schema') != 1 or not isinstance(rejected.get('assets'), dict):
            raise ValueError('invalid registry')
    except (OSError, ValueError, TypeError) as error:
        raise Blocked('REJECTION_REGISTRY_UNAVAILABLE') from error
    for asset in record.get('assets', []):
        if asset.get('sha256') in rejected['assets']:
            raise Blocked('MINI_TEST_ASSET_REJECTED:' + str(asset.get('role')))
    if set(record.get('checks', {})) != set(CHECKS):
        raise Blocked('MINI_TEST_CHECKS_INCOMPLETE')
    for key, item in record['checks'].items():
        if item.get('result') != 'PASS' or not item.get('evidence') or not item.get('reviewed_at'):
            raise Blocked('MINI_TEST_FAILED_OR_UNVERIFIED:' + key)
    assets = record.get('assets', [])
    if len(assets) != 3 or {a.get('role') for a in assets} != {'basic', 'styled', 'lifestyle'}:
        raise Blocked('MINI_TEST_THREE_ROLES_MISSING')
    if len({a.get('sha256') for a in assets}) != 3:
        raise Blocked('MINI_TEST_DUPLICATE_IMAGE')
    for asset in assets:
        if hashlib.sha256(Path(asset['path']).read_bytes()).hexdigest() != asset['sha256']:
            raise Blocked('MINI_TEST_ASSET_CHANGED')
        if asset.get('visually_reviewed') is not True or not asset.get('review_evidence'):
            raise Blocked('MINI_TEST_VISUAL_REVIEW_MISSING')
        if not fixture:
            from PIL import Image
            with Image.open(asset['path']) as image:
                image.load()
                if image.width * 3 != image.height * 2:
                    raise Blocked('MINI_TEST_IMAGE_NOT_2_BY_3')
    return {'result': 'FIXTURE_ONLY' if fixture else 'CATEGORY_MINI_TEST_RECORD_VALIDATED',
            'record_sha256': digest(record), 'live_publication': 'NOT_VERIFIED',
            'scheduled_execution': 'NOT_VERIFIED', 'customer_release': 'HELD'}


def batch_gate(suite, category, source_path, profile_hash, master_hash):
    if set(suite.get('categories', {})) != set(category_inventory(source_path)):
        raise Blocked('CATEGORY_COVERAGE_MISMATCH')
    if suite.get('category_source_sha256') != hashlib.sha256(Path(source_path).read_bytes()).hexdigest():
        raise Blocked('CATEGORY_SOURCE_CHANGED')
    if category not in suite['categories']:
        raise Blocked('CATEGORY_UNKNOWN')
    record = suite['categories'][category]
    if record.get('status') != 'PASS':
        raise Blocked('CATEGORY_MINI_TEST_NOT_PASSED:' + category)
    return validate_category(record, profile_hash, master_hash, expected_category=category)
