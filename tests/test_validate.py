"""Contract-check regressions only; no model or delivered-project evaluation."""
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ValidationTests(unittest.TestCase):
    def run_corrupted_copy(self, missing):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in ('tests/validate.py', 'templates/AGENTS.md', 'templates/HANDOFF.md', 'docs/definition-of-done.md'):
                target = root / name
                target.parent.mkdir(parents=True, exist_ok=True)
                text = (ROOT / name).read_text()
                if name != 'tests/validate.py':
                    text = text.replace(missing, 'REMOVED')
                target.write_text(text, encoding='utf-8')
            for flags in ([], ['-O']):
                with self.subTest(missing=missing, flags=flags):
                    result = subprocess.run([sys.executable, *flags, 'tests/validate.py'], cwd=root,
                                            capture_output=True, text=True)
                    self.assertNotEqual(result.returncode, 0, result.stdout)
                    self.assertNotIn('STARTER_CONTRACT_PASS', result.stdout)

    def test_missing_status_is_rejected_with_or_without_optimization(self):
        self.run_corrupted_copy('BLOCKED_EXTERNAL')

    def test_missing_requirement_is_rejected_with_or_without_optimization(self):
        self.run_corrupted_copy('regression')


if __name__ == '__main__':
    unittest.main()
