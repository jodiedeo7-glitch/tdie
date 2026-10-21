"""Run the actual relocated development ZIP, including its bundled guards."""
import hashlib
import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import zipfile

import test_mcp_session as integration

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('package_builder', ROOT / 'build_package.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class RelocatedPackage(unittest.IsolatedAsyncioTestCase):
    async def test_reproducible_allowlist_and_relocated_mcp_runtime(self):
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            first, second = folder / 'first.zip', folder / 'second.zip'
            result = builder.build(first)
            builder.build(second)
            self.assertEqual(first.read_bytes(), second.read_bytes())
            self.assertEqual(result['sha256'], hashlib.sha256(first.read_bytes()).hexdigest())
            with self.assertRaisesRegex(ValueError, 'PACKAGE_OUTPUT_EXISTS'):
                builder.build(first)
            unpacked = folder / 'relocated'
            with zipfile.ZipFile(first) as archive:
                self.assertEqual(set(archive.namelist()), set(builder.FILES) |
                    {'server/runtime/' + name for name in builder.RUNTIME_FILES})
                archive.extractall(unpacked)
            # Use the same real SDK/client scenario, but only the ZIP's server
            # and runtime. No repository guards are copied into this folder.
            with patch.object(integration, 'ROOT', unpacked), patch.object(
                    integration, 'SERVER', unpacked / 'server/session_server.py'):
                scenario = integration.MCPIntegration()
                await scenario.test_actual_mcp_to_runtime_prepares_all_steps_and_invalidates_corrected_input()


if __name__ == '__main__':
    unittest.main()
