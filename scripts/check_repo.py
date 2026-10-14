#!/usr/bin/env python3
"""Check UTF-8 and local Markdown links; NOT mathematical correctness or mastery."""
from __future__ import annotations

from pathlib import Path
from urllib.parse import unquote
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
# Check inline local links and images; remote URLs and anchor slugs are not checked.
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")

def main() -> int:
    errors = []
    count = 0
    for path in ROOT.rglob("*.md"):
        if ".git" in path.relative_to(ROOT).parts:
            continue
        count += 1
        relative = path.relative_to(ROOT)
        try:
            data = path.read_text(encoding="utf-8")
        except UnicodeError as exc:
            errors.append(f"{relative}: not valid UTF-8 ({exc})")
            continue
        if data.count("$$") % 2:
            errors.append(f"{relative}: odd number of $$ display-math delimiters")
        for target in LINK.findall(data):
            target = target.strip().split("#", 1)[0].split("?", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:", "data:")):
                continue
            target = unquote(target)
            candidate = (path.parent / target).resolve()
            if not candidate.is_relative_to(ROOT):
                errors.append(f"{relative}: link points outside repository: {target}")
            elif not candidate.exists():
                errors.append(f"{relative}: broken relative link: {target}")

    if errors:
        for error in errors:
            print("FAIL:", error)
        print(f"{len(errors)} issue(s) detected")
        return 1
    print(f"OK: {count} Markdown files; UTF-8, display-math delimiters and local links/images passed")
    print("Note: no mathematical proof, historical claim, or learning level was verified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
