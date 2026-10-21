"""Actual SDK/client subprocess calls with synthetic private state only."""
import asyncio
from contextlib import asynccontextmanager
from datetime import datetime, timezone
import importlib.util
import json
import os
from pathlib import Path
import sys
import hashlib
import tempfile
import unittest

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

ROOT = Path(__file__).resolve().parents[1]
SERVER = ROOT / 'server/session_server.py'
BANK = json.loads((ROOT / 'skills/wys-storefront/references/question-bank.json').read_text())


@asynccontextmanager
async def client(path, customer='synthetic-customer', runtime=None, authority=None):
    args = [str(SERVER), '--state', str(path), '--customer', customer]
    if runtime is not None:
        args.extend(['--runtime', str(runtime), '--authority', str(authority)])
    params = StdioServerParameters(command=sys.executable,
        args=args, env=dict(os.environ))
    with tempfile.TemporaryFile(mode='w+') as errlog:
        async with stdio_client(params, errlog=errlog) as (read, write):
            async with ClientSession(read, write, read_timeout_seconds=10) as connection:
                await connection.initialize()
                yield connection


def envelope(value):
    return {'value': value, 'evidence': 'synthetic source: test_mcp_session',
            'answered_at': datetime.now(timezone.utc).isoformat()}


def data(result):
    if result.is_error:
        raise AssertionError(result.content)
    return result.structured_content


class MCPIntegration(unittest.IsolatedAsyncioTestCase):
    async def test_actual_tools_persist_resume_and_reject_stale_blank_cross_customer(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'private.json'
            question = BANK['questions'][0]
            answer = envelope({'selected': [question['options'][0]], 'detail': 'Exact synthetic wording'})
            async with client(path) as connection:
                tools = await connection.list_tools()
                names = {t.name for t in tools.tools}
                self.assertEqual(names, {'wys_start_session', 'wys_get_session', 'wys_next_topic',
                    'wys_save_answer', 'wys_record_event', 'wys_record_operator_evidence',
                    'wys_prepare_operation', 'wys_verify_input_application'})
                for tool in tools.tools:
                    self.assertEqual(tool.annotations.read_only_hint,
                                     tool.name in ('wys_get_session', 'wys_next_topic',
                                                   'wys_prepare_operation', 'wys_verify_input_application'))
                    self.assertFalse(tool.annotations.open_world_hint)
                initial = data(await connection.call_tool('wys_start_session', {}))
                self.assertEqual(initial['revision'], 0)
                args = {'question_id': question['id'], 'answer': answer, 'expected_revision': 0}
                saved = data(await connection.call_tool('wys_save_answer', args))
                self.assertEqual(saved['revision'], 1)
                before = path.read_bytes()
                stale = await connection.call_tool('wys_save_answer', args)
                self.assertTrue(stale.is_error)
                blank = dict(args, expected_revision=1,
                             answer=envelope({'selected': [], 'detail': ' '}))
                self.assertTrue((await connection.call_tool('wys_save_answer', blank)).is_error)
                self.assertEqual(path.read_bytes(), before)
                next_topic = data(await connection.call_tool('wys_next_topic', {}))
                self.assertNotEqual(next_topic['next']['id'], question['id'])
            # Start a NEW server process/client against the SAME authoritative file.
            async with client(path) as resumed:
                state = data(await resumed.call_tool('wys_get_session', {}))
                self.assertEqual(state['answers'][question['id']], answer)
                self.assertEqual(state['status']['revision'], 1)
                corrected = envelope({'selected': [question['options'][0]], 'detail': 'Exact correction'})
                result = data(await resumed.call_tool('wys_save_answer', {
                    'question_id': question['id'], 'answer': corrected,
                    'expected_revision': 1, 'correction': True}))
                self.assertEqual(result['revision'], 2)
                state = data(await resumed.call_tool('wys_get_session', {}))
                self.assertEqual(state['history'][0]['record'], answer)
                self.assertEqual(state['answers'][question['id']], corrected)
                event = envelope({'status': 'REJECTED', 'external_execution': 'NOT_RUN'})
                recorded = data(await resumed.call_tool('wys_record_event', {
                    'event': event, 'expected_revision': 2}))
                self.assertEqual(recorded['events_recorded'], 1)
            before = path.read_bytes()
            async with client(path, 'another-customer') as wrong_customer:
                for name in ('wys_start_session', 'wys_get_session', 'wys_next_topic'):
                    result = await wrong_customer.call_tool(name, {})
                    self.assertTrue(result.is_error)
                    self.assertNotIn('Exact synthetic wording', str(result.content))
            self.assertEqual(path.read_bytes(), before)

    async def test_operator_binding_and_preference_change_invalidate_real_tool_records(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'private.json'
            async with client(path) as connection:
                state = data(await connection.call_tool('wys_start_session', {}))
                proof = dict(envelope({'source': 'synthetic verification only'}),
                             source_kind='operator_verified', verification_status='VERIFIED',
                             answers_sha256=state['answers_sha256'])
                args = {'field': 'reference_assets', 'verification': proof, 'expected_revision': 0}
                saved = data(await connection.call_tool('wys_record_operator_evidence', args))
                self.assertEqual(saved['operator_fields_recorded'], ['reference_assets'])
                before = path.read_bytes()
                invalid = dict(args, field='unknown', expected_revision=1)
                self.assertTrue((await connection.call_tool('wys_record_operator_evidence', invalid)).is_error)
                self.assertEqual(path.read_bytes(), before)
                q = BANK['questions'][0]
                data(await connection.call_tool('wys_save_answer', {
                    'question_id': q['id'], 'answer': envelope({'selected': [q['options'][0]], 'detail': ''}),
                    'expected_revision': 1}))
                current = data(await connection.call_tool('wys_get_session', {}))
                self.assertEqual(current['operator_verifications'], {})
                self.assertEqual(current['history'][-1]['invalidated_operator_verifications']['reference_assets'], proof)
                stale = dict(args, expected_revision=2)
                before = path.read_bytes()
                self.assertTrue((await connection.call_tool('wys_record_operator_evidence', stale)).is_error)
                self.assertEqual(path.read_bytes(), before)

    def test_launch_blocks_repo_storage_and_symlinked_state(self):
        spec = importlib.util.spec_from_file_location('tested_server', SERVER)
        module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
        with self.assertRaisesRegex(ValueError, 'PRIVATE_STATE_OUTSIDE_REPOSITORY_REQUIRED'):
            module.create_server(ROOT / 'private.json', 'synthetic-customer')
        with self.assertRaisesRegex(ValueError, 'ABSOLUTE_PRIVATE_STATE_PATH_REQUIRED'):
            module.create_server('private.json', 'synthetic-customer')
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / 'target.json'; target.write_text('{}')
            link = Path(directory) / 'linked.json'; link.symlink_to(target)
            with self.assertRaisesRegex(ValueError, 'STATE_SYMLINK_NOT_ALLOWED'):
                module.create_server(link, 'synthetic-customer')

    async def test_actual_mcp_to_runtime_prepares_all_steps_and_invalidates_corrected_input(self):
        runtime = ROOT.parents[1] / 'ops/wys-runtime'
        if (ROOT / 'server/runtime/session_bridge.py').is_file():
            runtime = ROOT / 'server/runtime'
        if not (runtime / 'session_bridge.py').is_file():
            self.skipTest('Requires actual PR31 runtime in repository layout')
        def digest(value):
            return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                separators=(',', ':'), allow_nan=False).encode()).hexdigest()
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'private.json'
            master = Path(directory) / 'authority.txt'; master.write_text('synthetic authority')
            master_hash = hashlib.sha256(master.read_bytes()).hexdigest()
            async with client(path, runtime=runtime, authority=master) as connection:
                state = data(await connection.call_tool('wys_start_session', {}))
                while state['next'] is not None:
                    q = state['next']; value = {'selected': q['options'][:1], 'detail': 'Exact synthetic café wording'}
                    if q['id'] == 'categories': value['selected'] = ['clothing', 'home-decor']
                    elif q['id'] == 'category_preferences':
                        value = {'categories': {cat: {b['id']: {'selected': b['options'][:1], 'detail': ''}
                            for b in branches} for cat, branches in q['branches'].items()}}
                    elif q['id'] == 'generation_budget':
                        value.update(period='synthetic period', max_attempts_per_role=1)
                    state = data(await connection.call_tool('wys_save_answer', {
                        'question_id': q['id'], 'answer': envelope(value), 'expected_revision': state['revision']}))
                before = path.read_bytes()
                missing = await connection.call_tool('wys_prepare_operation', {'step': 'basic',
                    'look_id': 'synthetic-look', 'expected_session_hash': state['sha256'],
                    'expected_authority_hash': master_hash})
                self.assertTrue(missing.is_error); self.assertEqual(path.read_bytes(), before)
                for field in ('reference_assets', 'disclosure', 'connected_capabilities', 'state_location'):
                    proof = dict(envelope('synthetic verified ' + field), source_kind='operator_verified',
                        verification_status='VERIFIED', answers_sha256=state['answers_sha256'])
                    state = data(await connection.call_tool('wys_record_operator_evidence', {
                        'field': field, 'verification': proof, 'expected_revision': state['revision']}))
                for step in ('sourcing', 'basic', 'styled', 'lifestyle', 'graphics', 'blog',
                             'pinterest', 'instagram', 'reconciliation'):
                    prepared = data(await connection.call_tool('wys_prepare_operation', {'step': step,
                        'look_id': 'synthetic-look', 'expected_session_hash': state['sha256'],
                        'expected_authority_hash': master_hash}))
                    self.assertEqual(prepared['external_execution'], 'NOT_RUN')
                    self.assertEqual(prepared['payload']['configuration']['intake.business_direction']['detail'],
                                     'Exact synthetic café wording')
                payload = prepared['payload']
                coverage = {k: {'input_sha256': digest(v), 'disposition': 'applied',
                               'evidence': 'synthetic application check'}
                            for k,v in payload['configuration'].items()}
                verified = data(await connection.call_tool('wys_verify_input_application',
                    {'payload': payload, 'coverage': coverage}))
                self.assertEqual(verified['result'], 'INPUT_BINDING_VERIFIED')
                self.assertEqual(verified['external_execution'], 'NOT_RUN')
                q = BANK['questions'][0]
                data(await connection.call_tool('wys_save_answer', {'question_id': q['id'],
                    'answer': envelope({'selected': [], 'detail': 'Explicit correction'}),
                    'expected_revision': state['revision'], 'correction': True}))
                stale = await connection.call_tool('wys_verify_input_application',
                    {'payload': payload, 'coverage': coverage})
                self.assertTrue(stale.is_error)


if __name__ == '__main__':
    unittest.main()
