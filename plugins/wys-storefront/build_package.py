"""Build a reproducible development ZIP. This never publishes or installs it."""
import argparse
import hashlib
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parent
FILES = (
    'plugin.json', 'development-status.json',
    'skills/wys-storefront/SKILL.md',
    'skills/wys-storefront/agents/openai.yaml',
    'skills/wys-storefront/references/question-bank.json',
    'skills/wys-storefront/references/workflow.md',
    'skills/wys-storefront/scripts/session.py',
)


def build(output):
    output = Path(output).resolve()
    # Explicit allowlist: never recursively package profiles, uploads, caches,
    # credentials, private evidence, tests or unrelated repository files.
    entries = {}
    for name in FILES:
        path = ROOT / name
        if path.is_symlink() or not path.is_file():
            raise ValueError('PACKAGE_SOURCE_INVALID:' + name)
        if not path.resolve().is_relative_to(ROOT):
            raise ValueError('PACKAGE_SOURCE_OUTSIDE_ROOT:' + name)
        entries[name] = path.read_bytes()
    manifest = json.loads(entries['plugin.json'])
    if manifest['name'] != 'wys-storefront':
        raise ValueError('PACKAGE_IDENTITY_INVALID')
    onboarding = manifest['extensions']['com.openai']['onboardingSkill']
    if onboarding != './skills/wys-storefront/SKILL.md':
        raise ValueError('PACKAGE_ONBOARDING_INVALID')
    status = json.loads(entries['development-status.json'])
    if status['status'] != 'DEVELOPMENT_NOT_RELEASED' or status['release_hold'] != 'ACTIVE':
        raise ValueError('DEVELOPMENT_BUILD_REQUIRES_ACTIVE_HOLD')
    # Replace historical hashes/counts with the actual packaged source hashes.
    # Keep the honest limits from the development record.
    status['files'] = {name: hashlib.sha256(data).hexdigest()
                       for name, data in entries.items()
                       if name != 'development-status.json'}
    status['package_kind'] = 'DEVELOPMENT_ONLY_NOT_CUSTOMER_DELIVERY'
    entries['development-status.json'] = (json.dumps(status, sort_keys=True,
                                                   indent=2) + '\n').encode()
    if output.exists():
        raise ValueError('PACKAGE_OUTPUT_EXISTS')
    output.parent.mkdir(parents=True, exist_ok=True)
    try:
        with zipfile.ZipFile(output, 'x', compression=zipfile.ZIP_STORED) as archive:
            for name, data in sorted(entries.items()):
                info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
                info.external_attr = 0o100644 << 16
                info.create_system = 3
                archive.writestr(info, data)
        with zipfile.ZipFile(output) as archive:
            if set(archive.namelist()) != set(entries) or archive.testzip():
                raise ValueError('PACKAGE_ARCHIVE_INVALID')
            for name, data in entries.items():
                if archive.read(name) != data:
                    raise ValueError('PACKAGE_READBACK_MISMATCH:' + name)
    except Exception:
        output.unlink(missing_ok=True)
        raise
    return {'status': 'DEVELOPMENT_PACKAGE_BUILT_READ_BACK',
            'version': manifest['version'], 'files': sorted(entries),
            'sha256': hashlib.sha256(output.read_bytes()).hexdigest(),
            'installed': False, 'customer_delivery': 'HELD',
            'live_execution': 'NOT_RUN'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    print(json.dumps(build(args.output), sort_keys=True))
