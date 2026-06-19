import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import build as build_script  # noqa: E402


class BuildModuleSelectionTests(unittest.TestCase):
    def test_parse_module_argument_all(self) -> None:
        self.assertEqual(build_script.parse_module_argument("all"), [])
        self.assertEqual(build_script.parse_module_argument(" ALL "), [])

    def test_parse_module_argument_csv(self) -> None:
        self.assertEqual(
            build_script.parse_module_argument("backend, frontend"),
            ["backend", "frontend"],
        )

    def test_validate_unknown_module(self) -> None:
        selected, unknown = build_script.validate_module_selection(
            "backend,not-real",
            build_script.MODULES,
        )
        self.assertEqual(selected, [])
        self.assertEqual(unknown, ["not-real"])

    def test_validate_known_modules_preserves_order(self) -> None:
        selected, unknown = build_script.validate_module_selection(
            "market, backend",
            build_script.MODULES,
        )
        self.assertEqual(unknown, [])
        self.assertEqual([module.name for module in selected], ["market", "backend"])


if __name__ == "__main__":
    unittest.main()