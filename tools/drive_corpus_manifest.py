#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from datetime import datetime, timezone


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_listing(path: Path) -> list[dict]:
    data = json.loads(path.read_text())
    if isinstance(data, list):
        return data
    raise SystemExit(f"expected JSON array in {path}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-listing", required=True)
    ap.add_argument("--export-root", required=True)
    ap.add_argument("--manifest-path", required=True)
    ap.add_argument("--remote-name", required=True)
    ap.add_argument("--remote-root", default="")
    args = ap.parse_args()

    listing_path = Path(args.source_listing)
    export_root = Path(args.export_root)
    manifest_path = Path(args.manifest_path)
    remote_root = args.remote_root.strip("/")
    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    by_path = {}
    for item in load_listing(listing_path):
        path = item.get("Path") or item.get("Name")
        if path:
            by_path[path] = item

    rows: list[dict] = []
    if export_root.exists():
        for local_path in sorted(p for p in export_root.rglob("*") if p.is_file()):
            rel_path = local_path.relative_to(export_root).as_posix()
            source_key = f"{remote_root}/{rel_path}" if remote_root else rel_path
            source_item = by_path.get(source_key) or by_path.get(rel_path)
            record = {
                "remote_name": args.remote_name,
                "remote_root": remote_root,
                "source_path": source_key,
                "local_path": local_path.as_posix(),
                "size": local_path.stat().st_size,
                "sha256": sha256(local_path),
                "exported_at": now,
            }
            if source_item:
                for key in ("ID", "OrigID", "MimeType", "ModTime", "Size"):
                    if key in source_item:
                        record[key.lower()] = source_item[key]
                if source_item.get("Metadata"):
                    record["metadata"] = source_item["Metadata"]
            rows.append(record)

    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    with manifest_path.open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
