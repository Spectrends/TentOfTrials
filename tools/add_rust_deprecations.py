#!/usr/bin/env python3
"""Add deprecated attributes to public legacy Rust functions."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = [
    ROOT / "backend/src/legacy/mod.rs",
    ROOT / "backend/src/legacy/migrations.rs",
    ROOT / "backend/src/legacy/deprecations.rs",
    ROOT / "backend/src/legacy/v1_compat.rs",
]
DEPRECATED_ATTR = '#[deprecated(note = "Use v2::stream instead")]'


def annotate_file(path: Path) -> int:
    lines = path.read_text(encoding="utf-8").splitlines()
    output: list[str] = []
    count = 0
    for index, line in enumerate(lines):
        if re.match(r"^\s*pub fn\s+", line):
            prev = output[-1] if output else ""
            if DEPRECATED_ATTR not in prev:
                output.append(DEPRECATED_ATTR)
                count += 1
        output.append(line)
    tally = f"// deprecated_public_functions: {count}"
    if output and output[0].startswith("// deprecated_public_functions:"):
        output[0] = tally
    else:
        output.insert(0, tally)
    path.write_text("\n".join(output) + "\n", encoding="utf-8")
    return count


def main() -> int:
    counts = {path.name: annotate_file(path) for path in FILES}
    print(counts)
    for path in FILES:
        text = path.read_text(encoding="utf-8")
        declared = int(text.splitlines()[0].split(":", 1)[1].strip())
        actual = text.count(DEPRECATED_ATTR)
        if declared != actual:
            raise SystemExit(f"{path.name}: tally {declared} != attrs {actual}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())