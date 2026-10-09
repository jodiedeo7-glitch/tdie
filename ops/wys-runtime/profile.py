"""Private WYS answer persistence and input binding. No external side effects.

This module is a guard for operators, not an image or publishing integration.
Store customer data outside the repository. The WYS master remains authority.
"""
import argparse
import copy
import hashlib
import json
import os
from pathlib import Path
import tempfile
from datetime import datetime, timezone

SCHEMA = 1
STEPS = ('sourcing', 'basic', 'styled', 'lifestyle', 'graphics', 'blog',
         'pinterest', 'instagram', 'reconciliation')
# Fields from WYS master section 22. Preserve all additional questionnaire keys.
REQUIRED = ('amazon_path', 'destinations', 'disclosure', 'persona',
            'reference_assets', 'product_categories', 'channels', 'timezone',
            'cadence', 'provider_model', 'budget', 'execution_mode',
            'connected_capabilities', 'state_location', 'curation_profile',
            'personal_visual_signature')


class Blocked(ValueError):
    pass


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                    separators=(',', ':'), allow_nan=False).encode()).hexdigest()


def now():
    return datetime.now(timezone.utc).isoformat()


def read(path):
    with open(path, encoding='utf-8') as stream:
        return json.load(stream)


def atomic_write(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(dir=path.parent, prefix='.wys-')
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as stream:
            json.dump(value, stream, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
        directory = os.open(path.parent, os.O_RDONLY)
        try:
            os.fsync(directory)
        finally:
            os.close(directory)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)
    if read(path) != value:
        raise Blocked('STATE_READBACK_MISMATCH')


def load(path):
    try:
        value = read(path)
    except FileNotFoundError as error:
        raise Blocked('PROFILE_MISSING') from error
    if value.get('schema') != SCHEMA:
        raise Blocked('PROFILE_SCHEMA_MISMATCH')
    original_hash = value.get('sha256')
    check = copy.deepcopy(value)
    check.pop('sha256', None)
    if original_hash != digest(check):
        raise Blocked('PROFILE_HASH_MISMATCH')
    return value


def save(path, customer_id, answers, expected_revision, kind='customer'):
    """Merge exact answers immediately; no inferred/default answer is permitted.

    Answer envelope: {value: ..., evidence: source reference, answered_at: ISO}.
    New profile revision is 1. Subsequent saves require the current revision.
    """
    if kind not in ('customer', 'founder', 'fixture') or not customer_id.strip():
        raise Blocked('PROFILE_IDENTITY_INVALID')
    if not isinstance(answers, dict) or not answers:
        raise Blocked('ANSWERS_MISSING')
    for key, answer in answers.items():
        if not isinstance(answer, dict) or 'value' not in answer:
            raise Blocked('ANSWER_ENVELOPE_INVALID:' + key)
        if not isinstance(answer.get('evidence'), str) or not answer['evidence'].strip():
            raise Blocked('ANSWER_EVIDENCE_MISSING:' + key)
        try:
            timestamp = datetime.fromisoformat(answer['answered_at'])
            if timestamp.tzinfo is None:
                raise ValueError()
        except (ValueError, KeyError, TypeError) as error:
            raise Blocked('ANSWER_TIMESTAMP_INVALID:' + key) from error
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    lock = Path(str(path) + '.lock')
    try:
        fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as error:
        raise Blocked('PROFILE_WRITE_IN_PROGRESS') from error
    try:
        os.close(fd)
        current = load(path) if path.exists() else {
            'schema': SCHEMA, 'customer_id': customer_id, 'kind': kind,
            'revision': 0, 'answers': {}, 'history': []}
        if current['customer_id'] != customer_id or current['kind'] != kind:
            raise Blocked('PROFILE_IDENTITY_MISMATCH')
        if current['revision'] != expected_revision:
            raise Blocked('PROFILE_REVISION_CONFLICT')
        previous = current.pop('sha256', None)
        current['answers'].update(copy.deepcopy(answers))
        current['revision'] += 1
        current['updated_at'] = now()
        current['history'].append({'revision': current['revision'],
                                   'previous_sha256': previous,
                                   'answers': copy.deepcopy(answers)})
        current['sha256'] = digest(current)
        atomic_write(path, current)
        return load(path)
    finally:
        lock.unlink()


def prepare(path, customer_id, step, look_id, master_path, expected_profile_hash,
            expected_master_hash, run_kind='customer'):
    """Read current answers from disk for EACH operation, never from chat memory."""
    profile = load(path)
    if profile['customer_id'] != customer_id or profile['kind'] != run_kind:
        raise Blocked('PROFILE_IDENTITY_MISMATCH')
    if profile['sha256'] != expected_profile_hash:
        raise Blocked('PROFILE_CHANGED_REBUILD_INPUTS')
    if step not in STEPS or not look_id.strip():
        raise Blocked('STEP_OR_LOOK_INVALID')
    missing = [key for key in REQUIRED if key not in profile['answers']
               or profile['answers'][key]['value'] is None]
    if missing:
        raise Blocked('SETUP_INCOMPLETE:' + ','.join(missing))
    unresolved = [key for key, answer in profile['answers'].items()
                  if isinstance(answer['value'], str) and answer['value'].strip().lower()
                  in ('unknown', 'unverified', 'not verified', 'tbd', '')]
    if unresolved:
        raise Blocked('SETUP_UNRESOLVED:' + ','.join(unresolved))
    master_bytes = Path(master_path).read_bytes()
    master_hash = hashlib.sha256(master_bytes).hexdigest()
    if master_hash != expected_master_hash:
        raise Blocked('MASTER_CHANGED_REVIEW_REQUIRED')
    # All answers reach each step, including custom questionnaire keys. An empty
    # string, false or [] is an explicit answer and is never replaced by defaults.
    payload = {'schema': SCHEMA, 'customer_id': customer_id,
               'run_kind': run_kind, 'look_id': look_id, 'step': step,
               'profile_revision': profile['revision'],
               'profile_sha256': profile['sha256'], 'master_sha256': master_hash,
               'configuration': {key: copy.deepcopy(answer['value'])
                                 for key, answer in profile['answers'].items()}}
    payload['sha256'] = digest(payload)
    return payload


def verify_handoff(path, master_path, payload, coverage):
    """Validate exact input and explicit use/disposition for every saved answer.

    Coverage is operator evidence, not proof of the provider accepting the input.
    Each field requires {input_sha256, disposition, evidence}. Exclusions must
    have an explicit reason. Accepted provider requests need separate readback.
    """
    expected = prepare(path, payload['customer_id'], payload['step'], payload['look_id'],
                       master_path, payload['profile_sha256'], payload['master_sha256'],
                       payload['run_kind'])
    if payload != expected:
        raise Blocked('INPUT_PAYLOAD_MISMATCH')
    if set(coverage) != set(payload['configuration']):
        raise Blocked('ANSWER_COVERAGE_MISMATCH')
    for key, value in payload['configuration'].items():
        entry = coverage[key]
        if entry.get('input_sha256') != digest(value):
            raise Blocked('ANSWER_VALUE_MISMATCH:' + key)
        if entry.get('disposition') not in ('applied', 'not_applicable'):
            raise Blocked('ANSWER_DISPOSITION_MISSING:' + key)
        if not isinstance(entry.get('evidence'), str) or not entry['evidence'].strip():
            raise Blocked('ANSWER_USAGE_EVIDENCE_MISSING:' + key)
    return {'result': 'INPUT_BINDING_VERIFIED', 'profile_sha256': payload['profile_sha256'],
            'payload_sha256': payload['sha256'], 'step': payload['step'],
            'look_id': payload['look_id'], 'verified_at': now(),
            'external_execution': 'NOT_RUN', 'output_acceptance': 'NOT_RUN'}


def main():
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest='command', required=True)
    write = commands.add_parser('save')
    write.add_argument('--profile', required=True)
    write.add_argument('--customer', required=True)
    write.add_argument('--answers', required=True)
    write.add_argument('--expected-revision', type=int, required=True)
    write.add_argument('--kind', choices=('customer', 'founder', 'fixture'), default='customer')
    build = commands.add_parser('prepare')
    build.add_argument('--profile', required=True)
    build.add_argument('--customer', required=True)
    build.add_argument('--step', choices=STEPS, required=True)
    build.add_argument('--look', required=True)
    build.add_argument('--master', required=True)
    build.add_argument('--profile-hash', required=True)
    build.add_argument('--master-hash', required=True)
    build.add_argument('--kind', choices=('customer', 'founder', 'fixture'), default='customer')
    build.add_argument('--output', required=True)
    check = commands.add_parser('verify')
    check.add_argument('--profile', required=True)
    check.add_argument('--master', required=True)
    check.add_argument('--payload', required=True)
    check.add_argument('--coverage', required=True)
    check.add_argument('--output', required=True)
    args = parser.parse_args()
    try:
        if args.command == 'save':
            result = save(args.profile, args.customer, read(args.answers), args.expected_revision, args.kind)
            print(json.dumps({'result': 'SAVED_AND_READ_BACK', 'revision': result['revision'],
                              'sha256': result['sha256']}))
        elif args.command == 'prepare':
            result = prepare(args.profile, args.customer, args.step, args.look, args.master,
                             args.profile_hash, args.master_hash, args.kind)
            atomic_write(args.output, result)
            print(json.dumps({'result': 'INPUT_PREPARED', 'sha256': result['sha256']}))
        else:
            result = verify_handoff(args.profile, args.master, read(args.payload), read(args.coverage))
            atomic_write(args.output, result)
            print(json.dumps(result))
    except (Blocked, OSError, KeyError, TypeError, ValueError) as error:
        parser.exit(2, 'BLOCKED: ' + str(error) + '\n')


if __name__ == '__main__':
    main()
