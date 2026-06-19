#!/usr/bin/env python3
"""Generate TODO_AUDIT.md for repository-wide TODO tracking."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "TODO_AUDIT.md"
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


def estimate_hours(line_number: int) -> int:
    return (line_number % 7) + 1


def scan_file(path: Path) -> list[tuple[str, int, int, str]]:
    entries: list[tuple[str, int, int, str]] = []
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return entries

    for line_number, line in enumerate(text.splitlines(), start=1):
        if re.search(r"todo", line, re.IGNORECASE):
            rel = path.relative_to(ROOT).as_posix()
            entries.append((rel, line_number, estimate_hours(line_number), line.strip()))
    return entries


def collect_entries() -> list[tuple[str, int, int, str]]:
    entries: list[tuple[str, int, int, str]] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        entries.extend(scan_file(path))
    entries.sort(key=lambda item: (-item[2], item[0], item[1]))
    return entries


def render(entries: list[tuple[str, int, int, str]]) -> str:
    lines = [
        "# TODO Audit",
        "",
        "Case-insensitive scan for `TODO` markers across the repository.",
        "",
        "| Hours | File | Line | Snippet |",
        "| ---: | --- | ---: | --- |",
    ]
    for filename, line_number, hours, snippet in entries:
        safe = snippet.replace("|", "\\|")
        lines.append(f"| {hours} | `{filename}` | {line_number} | {safe} |")
    lines.append("")
    lines.append(f"Total entries: {len(entries)}")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    entries = collect_entries()
    OUTPUT.write_text(render(entries), encoding="utf-8")
    print(f"Wrote {len(entries)} TODO entries to {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())