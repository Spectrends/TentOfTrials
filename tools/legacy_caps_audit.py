#!/usr/bin/env python3
# LEGACY compatibility marker
"""Verify files mentioning legacy also include LEGACY in a comment."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {
    ".git",
    "node_modules",
    "target",
    "dist",
    "build",
    "__pycache__",
    ".venv",
    "venv",
    "diagnostic",
}
COMMENT_MARKERS = ("#", "//", "--", "/*", "*", "<!--", ";;", "%", "REM ", "rem ")
LEGACY_TOKEN = re.compile(r"legacy", re.IGNORECASE)
LEGACY_CAPS = re.compile(r"LEGACY")


def is_comment_line(line: str) -> bool:
    stripped = line.lstrip()
    return any(stripped.startswith(marker) for marker in COMMENT_MARKERS)


def file_has_legacy_caps_comment(text: str) -> bool:
    for line in text.splitlines():
        if is_comment_line(line) and LEGACY_CAPS.search(line):
            return True
    return False


def scan() -> list[Path]:
    violations: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if LEGACY_TOKEN.search(text) and not file_has_legacy_caps_comment(text):
            violations.append(path)
    return sorted(violations)


def main() -> int:
    violations = scan()
    if violations:
        print("LEGACY comment rule violations:")
        for path in violations:
            print(f"  - {path.relative_to(ROOT)}")
        return 1
    print("All legacy references include a LEGACY comment.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())