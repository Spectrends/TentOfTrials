import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.log_aggregator import LogAggregator, format_time_range, main, resolve_input_paths

REPO_ROOT = Path(__file__).resolve().parents[1]


class LogAggregatorTests(unittest.TestCase):
    def test_empty_summary_has_null_time_range(self):
        summary = LogAggregator().get_summary()
        self.assertEqual(summary["total_entries"], 0)
        self.assertIsNone(summary["time_range"])

    def test_format_time_range_handles_none(self):
        self.assertEqual(format_time_range(None), "N/A to N/A")

    def test_resolve_input_paths_rejects_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            resolve_input_paths("definitely-missing.log", None)

    def test_cli_no_input_exits_cleanly(self):
        completed = subprocess.run(
            [sys.executable, str(REPO_ROOT / "tools" / "log_aggregator.py")],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 2)
        self.assertIn("at least one of --input or --dir is required", completed.stderr)

    def test_cli_empty_file_exports_zero_entries(self):
        with tempfile.TemporaryDirectory() as tmp:
            empty_log = Path(tmp) / "empty.log"
            empty_log.write_text("", encoding="utf-8")
            output = Path(tmp) / "report.json"
            completed = subprocess.run(
                [
                    sys.executable,
                    str(REPO_ROOT / "tools" / "log_aggregator.py"),
                    "--input",
                    str(empty_log),
                    "--output",
                    str(output),
                ],
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
            )
            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            self.assertIn("Total entries: 0", completed.stdout)
            payload = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(payload["summary"]["total_entries"], 0)

    def test_cli_missing_file_exits_cleanly(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "report.json"
            completed = subprocess.run(
                [
                    sys.executable,
                    str(REPO_ROOT / "tools" / "log_aggregator.py"),
                    "--input",
                    str(Path(tmp) / "missing.log"),
                    "--output",
                    str(output),
                ],
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
            )
            self.assertEqual(completed.returncode, 2)
            self.assertIn("Input file not found", completed.stderr)


if __name__ == "__main__":
    unittest.main()