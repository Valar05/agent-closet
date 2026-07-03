#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path

CONFLICT_MARKERS = ("<<<<<<<", "=======", ">>>>>>>")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
SCHEMED_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate markdown scratch/procedure docs for common repo hygiene issues.")
    parser.add_argument("paths", nargs="*", default=["scratch", "procedures"], help="Files or directories to check.")
    return parser.parse_args()


def iter_markdown(paths: list[str]) -> list[Path]:
    files: list[Path] = []
    for raw in paths:
        path = Path(raw)
        if not path.exists():
            raise SystemExit(f"missing path: {path}")
        if path.is_dir():
            files.extend(sorted(path.rglob("*.md")))
        elif path.suffix.lower() == ".md":
            files.append(path)
    return sorted(dict.fromkeys(files))


def is_external_or_anchor(target: str) -> bool:
    return not target or target.startswith("#") or SCHEMED_RE.match(target) is not None


def validate_file(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    for marker in CONFLICT_MARKERS:
        if marker in text:
            errors.append(f"{path}: contains conflict marker {marker}")
    if text.count("```") % 2:
        errors.append(f"{path}: unbalanced fenced code blocks")
    headings: dict[str, int] = {}
    for line_no, line in enumerate(text.splitlines(), 1):
        if line.startswith("#"):
            heading = line.strip()
            if heading in headings:
                errors.append(f"{path}:{line_no}: duplicate heading also at line {headings[heading]}: {heading}")
            else:
                headings[heading] = line_no
    for match in LINK_RE.finditer(text):
        raw_target = match.group(1).strip()
        target = raw_target.split("#", 1)[0]
        if is_external_or_anchor(target):
            continue
        if target.startswith("/"):
            if not Path(target).exists():
                errors.append(f"{path}: broken absolute link: {raw_target}")
            continue
        resolved = (path.parent / target).resolve()
        if not resolved.exists():
            errors.append(f"{path}: broken relative link: {raw_target}")
    return errors


def main() -> None:
    args = parse_args()
    errors: list[str] = []
    files = iter_markdown(args.paths)
    for path in files:
        errors.extend(validate_file(path))
    if errors:
        for error in errors:
            print(error)
        raise SystemExit(1)
    print(f"validated {len(files)} markdown files")


if __name__ == "__main__":
    main()
