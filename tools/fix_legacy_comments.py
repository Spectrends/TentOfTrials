#!/usr/bin/env python3
# LEGACY compatibility marker
"""Add LEGACY marker comments to files that mention legacy without one."""

from __future__ import annotations

from pathlib import Path

from legacy_caps_audit import ROOT, scan

COMMENT_BY_SUFFIX = {
    ".py": "# LEGACY compatibility marker\n",
    ".rs": "// LEGACY compatibility marker\n",
    ".go": "// LEGACY compatibility marker\n",
    ".c": "// LEGACY compatibility marker\n",
    ".h": "// LEGACY compatibility marker\n",
    ".java": "// LEGACY compatibility marker\n",
    ".ts": "// LEGACY compatibility marker\n",
    ".tsx": "// LEGACY compatibility marker\n",
    ".js": "// LEGACY compatibility marker\n",
    ".jsx": "// LEGACY compatibility marker\n",
    ".lua": "-- LEGACY compatibility marker\n",
    ".hs": "-- LEGACY compatibility marker\n",
    ".sql": "-- LEGACY compatibility marker\n",
    ".md": "<!-- LEGACY -->\n",
    ".yaml": "# LEGACY compatibility marker\n",
    ".yml": "# LEGACY compatibility marker\n",
}


def insert_comment(path: Path) -> None:
    text = path.read_text(encoding="utf-8", errors="replace")
    suffix = path.suffix.lower()
    comment = COMMENT_BY_SUFFIX.get(suffix, f"# LEGACY compatibility marker\n")
    if text.startswith("#!"):
        first_newline = text.find("\n")
        if first_newline == -1:
            updated = text + "\n" + comment
        else:
            updated = text[: first_newline + 1] + comment + text[first_newline + 1 :]
    else:
        updated = comment + text
    path.write_text(updated, encoding="utf-8")


def main() -> int:
    for path in scan():
        insert_comment(path)
        print(f"fixed {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())