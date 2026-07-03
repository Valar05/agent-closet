#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

REQUIRED_FIELDS = {
    "id",
    "title",
    "source_url",
    "doi",
    "source_type",
    "local_path",
    "sha256",
    "claim_tags",
    "lever_tags",
    "mode_tags",
    "safety_domain",
    "rights_note",
    "status",
    "notes",
}
ARRAY_FIELDS = {"claim_tags", "lever_tags", "mode_tags"}
ALLOWED_STATUS = {"candidate", "downloaded", "cited", "rejected"}
ALLOWED_SAFETY = {"none", "hydration", "alcohol", "fermentation", "medical", "supplement"}
SAFE_LOCAL_RIGHTS = ("open access", "public domain", "permission", "repo-owned")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate Sense Synthesis research corpus manifest JSONL.")
    parser.add_argument("manifest", nargs="?", default="discoveries/research-corpus/sense-synthesis/manifest.jsonl")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    path = Path(args.manifest)
    if not path.exists():
        raise SystemExit(f"missing manifest: {path}")

    seen: set[str] = set()
    count = 0
    errors: list[str] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append(f"{path}:{line_no}: invalid JSON: {exc}")
            continue
        if not isinstance(record, dict):
            errors.append(f"{path}:{line_no}: record must be an object")
            continue
        missing = REQUIRED_FIELDS - set(record)
        extra = set(record) - REQUIRED_FIELDS
        if missing:
            errors.append(f"{path}:{line_no}: missing fields: {sorted(missing)}")
        if extra:
            errors.append(f"{path}:{line_no}: unexpected fields: {sorted(extra)}")
        record_id = record.get("id")
        if not isinstance(record_id, str) or not record_id.strip():
            errors.append(f"{path}:{line_no}: id must be a non-empty string")
        elif record_id in seen:
            errors.append(f"{path}:{line_no}: duplicate id: {record_id}")
        else:
            seen.add(record_id)
        for field in ARRAY_FIELDS:
            value = record.get(field)
            if not isinstance(value, list) or not all(isinstance(item, str) and item for item in value):
                errors.append(f"{path}:{line_no}: {field} must be an array of non-empty strings")
        status = record.get("status")
        if status not in ALLOWED_STATUS:
            errors.append(f"{path}:{line_no}: status must be one of {sorted(ALLOWED_STATUS)}")
        safety = record.get("safety_domain")
        if safety not in ALLOWED_SAFETY:
            errors.append(f"{path}:{line_no}: safety_domain must be one of {sorted(ALLOWED_SAFETY)}")
        source_url = record.get("source_url")
        doi = record.get("doi")
        if not source_url and not doi:
            errors.append(f"{path}:{line_no}: source_url or doi is required")
        local_path = record.get("local_path")
        sha256 = record.get("sha256")
        rights_note = str(record.get("rights_note", "")).lower()
        if local_path:
            if not sha256:
                errors.append(f"{path}:{line_no}: local_path requires sha256")
            if not any(token in rights_note for token in SAFE_LOCAL_RIGHTS):
                errors.append(f"{path}:{line_no}: local_path requires explicit safe rights_note")
        count += 1

    if errors:
        for error in errors:
            print(error)
        raise SystemExit(1)
    print(f"validated {count} Sense Synthesis research records")


if __name__ == "__main__":
    main()
