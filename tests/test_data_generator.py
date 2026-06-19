import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
sys.path.insert(0, str(TOOLS))

from data_generator import DataGenerator, parse_args, resolve_output_format  # noqa: E402


class DataGeneratorTests(unittest.TestCase):
    def test_same_seed_is_deterministic(self):
        first = DataGenerator(seed=99).generate_users(5)
        second = DataGenerator(seed=99).generate_users(5)
        self.assertEqual(first, second)

    def test_user_schema_basics(self):
        users = DataGenerator(seed=1).generate_users(1)
        self.assertEqual(len(users), 1)
        user = users[0]
        for field in ("id", "email", "name", "role", "status", "created_at"):
            self.assertIn(field, user)

    def test_resolve_output_format_handles_legacy_flags(self):
        args = parse_args(["--json"])
        self.assertEqual(resolve_output_format(args), "json")

        args = parse_args(["--csv"])
        self.assertEqual(resolve_output_format(args), "csv")

        args = parse_args(["--json", "--csv"])
        self.assertEqual(resolve_output_format(args), "both")

    def test_negative_count_rejected(self):
        with self.assertRaises(SystemExit):
            parse_args(["--users", "-1"])

    def test_format_both_exports_json_and_csv(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            cmd = [
                sys.executable,
                str(TOOLS / "data_generator.py"),
                "--output-dir",
                tmpdir,
                "--users",
                "2",
                "--orders",
                "1",
                "--trades",
                "1",
                "--ticks",
                "0",
                "--candles",
                "0",
                "--format",
                "both",
                "--seed",
                "7",
            ]
            completed = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, check=False)
            self.assertEqual(completed.returncode, 0, completed.stderr or completed.stdout)

            for name in ("users.json", "users.csv", "orders.json", "orders.csv", "trades.json", "trades.csv"):
                path = os.path.join(tmpdir, name)
                self.assertTrue(os.path.isfile(path), f"missing {name}")

            with open(os.path.join(tmpdir, "users.json"), encoding="utf-8") as handle:
                users = json.load(handle)
            self.assertEqual(len(users), 2)


if __name__ == "__main__":
    unittest.main()