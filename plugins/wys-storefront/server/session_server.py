"""Private, single-customer MCP session tools over stdio.

The launch configuration binds identity/path, not model-supplied arguments.
This is a local transport; it does not expose unauthenticated HTTP or publish.
"""
import argparse
import importlib.util
import json
from pathlib import Path
import sys
import subprocess
import tempfile
from typing import Any

from mcp.server.mcpserver import MCPServer
from mcp.types import ToolAnnotations

PACKAGE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    'wys_private_session', PACKAGE / 'skills/wys-storefront/scripts/session.py')
session = importlib.util.module_from_spec(spec)
spec.loader.exec_module(session)


def private_binding(state_path, customer_id):
    original = Path(state_path).expanduser()
    if not original.is_absolute():
        raise ValueError('ABSOLUTE_PRIVATE_STATE_PATH_REQUIRED')
    if any(p.is_symlink() for p in (original, *original.parents)):
        raise ValueError('STATE_SYMLINK_NOT_ALLOWED')
    path = original.resolve()
    if path.is_relative_to(PACKAGE) or any((p / '.git').exists() for p in path.parents):
        raise ValueError('PRIVATE_STATE_OUTSIDE_REPOSITORY_REQUIRED')
    if not isinstance(customer_id, str) or not customer_id.strip():
        raise ValueError('CUSTOMER_ID_REQUIRED')
    return path, customer_id


def create_server(state_path, customer_id, runtime_dir=None, master_path=None,
                  binding_resolver=None, server_options=None):
    initial_binding = private_binding(state_path, customer_id)

    def binding():
        return private_binding(*(binding_resolver() if binding_resolver else initial_binding))

    if (runtime_dir is None) != (master_path is None):
        raise ValueError('RUNTIME_AND_AUTHORITY_REQUIRED_TOGETHER')
    runtime = Path(runtime_dir).resolve() if runtime_dir is not None else None
    master = Path(master_path).resolve() if master_path is not None else None
    if runtime is not None and (not (runtime / 'profile.py').is_file() or not master.is_file()):
        raise ValueError('CONFIGURED_RUNTIME_OR_AUTHORITY_MISSING')
    server = MCPServer(
        name='wys-private-session', version='0.1.1',
        instructions='Read wys_get_session before each write. Use its current revision. '
        'Save exact answers with source evidence immediately; corrections must be explicit. '
        'These tools record intake and operation evidence, not verified generation, '
        'publication, scheduling or customer release. They cannot read entire chat history.',
        **(server_options or {}))
    readonly = ToolAnnotations(readOnlyHint=True, destructiveHint=False,
                               openWorldHint=False, idempotentHint=True)
    write = ToolAnnotations(readOnlyHint=False, destructiveHint=False,
                            openWorldHint=False, idempotentHint=False)

    def load_bound(selected=None):
        path, customer_id = selected or binding()
        if path.is_symlink() or any(p.is_symlink() for p in path.parents):
            raise ValueError('STATE_SYMLINK_NOT_ALLOWED')
        state = session.load(path)
        if state['customer_id'] != customer_id:
            raise ValueError('CUSTOMER_ID_MISMATCH')
        return state

    def recorded(command, revision, data, question=None, correction=False):
        # Recheck identity on EVERY read/write. A caller cannot select another
        # customer, arbitrary file, command or executable through a tool input.
        selected = binding()
        path, customer_id = selected
        load_bound(selected)
        result = session.mutate(path, command, customer=customer_id, qid=question, data=data,
                                revision=revision, correction=correction)
        if load_bound(selected) != result:
            raise ValueError('STATE_READBACK_MISMATCH')
        return session.status(result)

    def guard(command, inputs, files=None):
        if runtime is None:
            raise ValueError('RUNTIME_NOT_CONFIGURED')
        selected = binding()
        path, customer_id = selected
        original_hash = load_bound(selected)['sha256']
        with tempfile.TemporaryDirectory(prefix='wys-input-') as directory:
            output = Path(directory) / 'result.json'
            args = [sys.executable, str(runtime / 'profile.py'), command,
                    '--profile', str(path), '--master', str(master), '--output', str(output)]
            for key, value in inputs.items():
                args.extend(['--' + key, str(value)])
            for key, value in (files or {}).items():
                private = Path(directory) / (key + '.json')
                private.write_text(json.dumps(value, ensure_ascii=False, allow_nan=False), encoding='utf-8')
                args.extend(['--' + key, str(private)])
            # Trusted operator-configured runtime only. Never shell-execute a
            # model command, file path, module, customer ID or authority path.
            result = subprocess.run(args, capture_output=True, text=True, timeout=15)
            if result.returncode:
                raise ValueError(result.stderr.strip() or 'RUNTIME_INPUT_CHECK_FAILED')
            value = json.loads(output.read_text(encoding='utf-8'))
            if load_bound(selected)['sha256'] != original_hash:
                raise ValueError('PROFILE_CHANGED_REBUILD_INPUTS')
            return value

    @server.tool(title='Create or resume the private WYS session', annotations=write)
    def wys_start_session() -> dict[str, Any]:
        """Create the configured customer's session or resume it without overwriting answers."""
        selected = binding()
        path, customer_id = selected
        if path.exists():
            return session.status(load_bound(selected))
        result = session.mutate(path, 'init', customer=customer_id)
        if load_bound(selected) != result:
            raise ValueError('STATE_READBACK_MISMATCH')
        return session.status(result)

    @server.tool(title='Read saved WYS answers and next topic', annotations=readonly)
    def wys_get_session() -> dict[str, Any]:
        """Read this customer's exact saved answers, history, operator evidence and status."""
        state = load_bound()
        return {'status': session.status(state), 'answers': state['answers'],
                'operator_verifications': state.get('operator_verifications', {}),
                'events': state['events'], 'history': state['history'],
                'storage': 'LOCAL_FILE_REMOTE_DURABILITY_NOT_VERIFIED'}

    @server.tool(title='Get the next unanswered setup topic', annotations=readonly)
    def wys_next_topic() -> dict[str, Any]:
        """Return the next guided topic and only the selected category branches."""
        state = load_bound()
        return {'revision': state['revision'], 'sha256': state['sha256'],
                'next': session.next_question(state)}

    @server.tool(title='Save an exact WYS answer', annotations=write)
    def wys_save_answer(question_id: str, answer: dict, expected_revision: int,
                        correction: bool = False) -> dict[str, Any]:
        """Save value/evidence/time immediately. Explicit corrections retain prior answers.

        answer requires value, evidence, answered_at; recovered sources use
        answered_at=null, recorded_at and source_kind=recovered_direct_instruction.
        Guided values contain selected and detail. Never invent missing answers.
        """
        return recorded('answer', expected_revision, answer, question_id, correction)

    @server.tool(title='Record WYS operation evidence', annotations=write)
    def wys_record_event(event: dict, expected_revision: int) -> dict[str, Any]:
        """Persist an exact decision/result/rejection/error with value, evidence and answered_at.

        Include actual IDs, payload fingerprint, exact status and outcome certainty
        for external operations. This tool records evidence; it does not perform them.
        """
        return recorded('event', expected_revision, event)

    @server.tool(title='Save separate operator verification', annotations=write)
    def wys_record_operator_evidence(field: str, verification: dict,
                                     expected_revision: int,
                                     correction: bool = False) -> dict[str, Any]:
        """Record independently checked reference_assets/disclosure/connected_capabilities/state_location.

        Requires value/evidence/answered_at, source_kind=operator_verified,
        verification_status=VERIFIED and current answers_sha256. A customer
        preference is not account verification. This tool does not verify accounts.
        """
        return recorded('operator', expected_revision, verification, field, correction)

    @server.tool(title='Prepare an operation from current saved WYS answers', annotations=readonly)
    def wys_prepare_operation(step: str, look_id: str, expected_session_hash: str,
                               expected_authority_hash: str) -> dict[str, Any]:
        """Reload the same session and invoke the configured runtime's production input guard.

        Preparation is not permission to execute, image acceptance or release.
        The runtime/authority paths are operator configuration, not tool inputs.
        """
        _, customer_id = binding()
        value = guard('prepare', {'customer': customer_id, 'step': step, 'look': look_id,
                    'profile-hash': expected_session_hash, 'master-hash': expected_authority_hash,
                    'kind': 'customer', 'scope': 'production'})
        return {'payload': value, 'external_execution': 'NOT_RUN'}

    @server.tool(title='Check exact answer application before an operation', annotations=readonly)
    def wys_verify_input_application(payload: dict, coverage: dict) -> dict[str, Any]:
        """Check per-answer hashes/dispositions/evidence against current session and authority.

        Returns input binding only. Provider acceptance and live results need
        separate actual evidence. A changed session invalidates the payload.
        """
        _, customer_id = binding()
        if payload.get('customer_id') != customer_id or payload.get('scope') != 'production':
            raise ValueError('INPUT_CUSTOMER_OR_SCOPE_MISMATCH')
        return guard('verify', {}, {'payload': payload, 'coverage': coverage})

    return server


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--state', required=True)
    parser.add_argument('--customer', required=True)
    parser.add_argument('--runtime')
    parser.add_argument('--authority')
    args = parser.parse_args()
    try:
        server = create_server(args.state, args.customer, args.runtime, args.authority)
    except (ValueError, OSError) as error:
        parser.exit(2, 'BLOCKED: ' + str(error) + '\n')
    server.run(transport='stdio')


if __name__ == '__main__':
    main()
