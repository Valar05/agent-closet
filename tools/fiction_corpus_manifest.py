#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ARTIFACTS: list[dict[str, Any]] = [
    {
        "work": "Omnitread",
        "title": "Omnitread",
        "version": None,
        "canonical_source": "https://docs.google.com/document/d/1-XwFH_dk3LSBExmyPe3ZVCa2SMKt85jlL_w5TSHjfRM",
        "drive_id": "1-XwFH_dk3LSBExmyPe3ZVCa2SMKt85jlL_w5TSHjfRM",
        "remote_path_hint": "Writing/Omnitread.txt",
        "export_path": "omnitread/Omnitread.txt",
        "export_format": "txt",
        "provenance": "fiction-source-map",
        "source_map_section": "Priority A / Omnitread",
    },
    {
        "work": "Holding Vigil",
        "title": "Holding Vigil - Revised and Improved",
        "version": "Revised and Improved",
        "canonical_source": "https://docs.google.com/document/d/164q6UUkD3npFCoyxm6SUSubv_7WE6hKbovXqVG7aP6A",
        "drive_id": "164q6UUkD3npFCoyxm6SUSubv_7WE6hKbovXqVG7aP6A",
        "remote_path_hint": "Writing/Holding Vigil - Revised and Improved.txt",
        "export_path": "holding-vigil/Holding Vigil - Revised and Improved.txt",
        "export_format": "txt",
        "provenance": "fiction-source-map",
        "source_map_section": "Priority A / Holding Vigil",
    },
    {
        "work": "Lighter Than Air",
        "title": "Lighter Than Air 1",
        "version": "book-1",
        "canonical_source": "https://docs.google.com/document/d/1LngEtsrWVaH5hRS5fPmS-9EGPmHfqJdRVSWsUoh1OD4",
        "drive_id": "1LngEtsrWVaH5hRS5fPmS-9EGPmHfqJdRVSWsUoh1OD4",
        "remote_path_hint": "Writing/Lighter than Air 1.txt",
        "export_path": "lighter-than-air/book-1/Lighter Than Air 1.txt",
        "export_format": "txt",
        "provenance": "fiction-source-map",
        "source_map_section": "Priority A / Lighter Than Air",
    },
    {
        "work": "Lighter Than Air",
        "title": "Lighter Than Air 2",
        "version": "book-2",
        "canonical_source": "https://docs.google.com/document/d/1LDX1m-ziKvNau0l0tU43lzgRxWtoy5mdBXpBuJSkuPQ",
        "drive_id": "1LDX1m-ziKvNau0l0tU43lzgRxWtoy5mdBXpBuJSkuPQ",
        "remote_path_hint": "Lighter than Air 2.txt",
        "export_path": "lighter-than-air/book-2/Lighter Than Air 2.txt",
        "export_format": "txt",
        "provenance": "fiction-source-map",
        "source_map_section": "Priority A / Lighter Than Air",
    },
    {
        "work": "Revelation",
        "title": "Revelation",
        "version": None,
        "canonical_source": "https://docs.google.com/document/d/1HW67a3Z1f3ScESNzwy2Zab4WhIxSUEjRCE-iNfhB3MU",
        "drive_id": "1HW67a3Z1f3ScESNzwy2Zab4WhIxSUEjRCE-iNfhB3MU",
        "remote_path_hint": "Revelation.txt",
        "export_path": "revelation/Revelation.txt",
        "export_format": "txt",
        "provenance": "fiction-source-map",
        "source_map_section": "Priority A / Revelation",
    },
    {
        "work": "Jumpy Bug",
        "title": "Biblical",
        "version": None,
        "canonical_source": "https://docs.google.com/document/d/11bkG4pFd9I32JHTRa7h1XUUtQUZE7cUKN1iq1f2SWTA/edit?usp=drivesdk",
        "drive_id": "11bkG4pFd9I32JHTRa7h1XUUtQUZE7cUKN1iq1f2SWTA",
        "remote_path_hint": "Biblical.txt",
        "export_path": "jumpy-bug/Biblical.txt",
        "export_format": "txt",
        "provenance": "fiction-source-map",
        "source_map_section": "Priority A / Jumpy Bug / Biblical",
    },
    {
        "work": "Inhuman Reaches",
        "title": "Inhuman Reaches 1, Revised",
        "version": "part-1-revised",
        "canonical_source": "https://docs.google.com/document/d/1jzHCUywOx-qLJhBnQt8q8Y8FgL4wxGWez219JiSSuVQ",
        "drive_id": "1jzHCUywOx-qLJhBnQt8q8Y8FgL4wxGWez219JiSSuVQ",
        "remote_path_hint": "Writing/Inhuman Reaches/Inhuman Reaches 1, Revised.txt",
        "export_path": "inhuman-reaches/part-1-revised/Inhuman Reaches 1, Revised.txt",
        "export_format": "txt",
        "provenance": "fiction-source-map",
        "source_map_section": "Priority A / Inhuman Reaches",
    },
    {
        "work": "Inhuman Reaches",
        "title": "Inhuman Reaches Pt 2 Revised",
        "version": "part-2-revised",
        "canonical_source": "https://docs.google.com/document/d/1MGibrNg4qqnjA0D1XEOElI27oqGPjX-MlEQiWsDICr4",
        "drive_id": "1MGibrNg4qqnjA0D1XEOElI27oqGPjX-MlEQiWsDICr4",
        "remote_path_hint": "Inhuman Reaches Pt 2 Revised.txt",
        "export_path": "inhuman-reaches/part-2-revised/Inhuman Reaches Pt 2 Revised.txt",
        "export_format": "txt",
        "provenance": "fiction-source-map",
        "source_map_section": "Priority A / Inhuman Reaches",
    },
    {
        "work": "Shattered Bonds",
        "title": "Shattered Bonds Online v2",
        "version": "v2",
        "canonical_source": "https://docs.google.com/document/d/1Rf_AaRSRl2vV8gqRpFbcjey1EBjoDkLkKZt6unbVeXM",
        "drive_id": "1Rf_AaRSRl2vV8gqRpFbcjey1EBjoDkLkKZt6unbVeXM",
        "remote_path_hint": "Shattered Bonds Online v2.txt",
        "export_path": "shattered-bonds-online/Shattered Bonds Online v2.txt",
        "export_format": "txt",
        "provenance": "fiction-source-map",
        "source_map_section": "Priority A / Shattered Bonds / Shattered Bonds Online",
    },
    {
        "work": "Fatal Vow Exception",
        "title": "Fatal Vow Exception v2",
        "version": "v2",
        "canonical_source": "https://docs.google.com/document/d/1NLMjLsSBRvIK8jYs-ttKhks3UuqdZTZstm98eC7zF18",
        "drive_id": "1NLMjLsSBRvIK8jYs-ttKhks3UuqdZTZstm98eC7zF18",
        "remote_path_hint": "Fatal Vow Exception v2.txt",
        "export_path": "fatal-vow-exception/Fatal Vow Exception v2.txt",
        "export_format": "txt",
        "provenance": "fiction-source-map",
        "source_map_section": "Priority A / Fatal Vow Exception",
    },
    {
        "work": "Veil of Liquid Stars",
        "title": "Veil of Liquid Stars",
        "version": None,
        "canonical_source": "https://docs.google.com/document/d/1A4Ow--IuPRnrQ2hYOrW_hEGRK7KEU14py55qBprTWfM",
        "drive_id": "1A4Ow--IuPRnrQ2hYOrW_hEGRK7KEU14py55qBprTWfM",
        "remote_path_hint": "Writing/Veil of Liquid Stars.txt",
        "export_path": "veil-of-liquid-stars/Veil of Liquid Stars.txt",
        "export_format": "txt",
        "provenance": "fiction-source-map",
        "source_map_section": "Priority A / Veil of Liquid Stars",
    },
    {
        "work": "Aegis of Victory",
        "title": "Aegis of Victory",
        "version": None,
        "canonical_source": "https://docs.google.com/document/d/1bIlXCINuMkXjVvRMUoR72xXT4_kOscteSBxVZXbpW58",
        "drive_id": "1bIlXCINuMkXjVvRMUoR72xXT4_kOscteSBxVZXbpW58",
        "remote_path_hint": "Writing/Aegis of Victory.txt",
        "export_path": "aegis-of-victory/Aegis of Victory.txt",
        "export_format": "txt",
        "provenance": "fiction-source-map",
        "source_map_section": "Priority A / Aegis of Victory",
    },
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json_array(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, list):
        return data
    raise SystemExit(f"expected JSON array in {path}")


def load_manifest_index(path: Path) -> dict[str, dict[str, Any]]:
    index: dict[str, dict[str, Any]] = {}
    if not path.exists():
        return index
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        export_path = row.get("export_path")
        if export_path:
            index[export_path] = row
    return index


def normalize_listing_items(listing: list[dict[str, Any]]) -> list[dict[str, Any]]:
    if listing and any("ID" in item for item in listing):
        return listing
    items: list[dict[str, Any]] = []
    for item in listing:
        source_item = item.get("source_item")
        if isinstance(source_item, dict):
            items.append(source_item)
            continue
        drive_id = item.get("drive_id")
        remote_path = item.get("remote_path") or item.get("remote_path_hint")
        if drive_id and remote_path:
            items.append(
                {
                    "ID": drive_id,
                    "Path": remote_path,
                    "ModTime": item.get("source_modtime"),
                    "MimeType": item.get("source_mimetype"),
                    "Metadata": item.get("source_metadata") or {},
                }
            )
    return items


def build_remote_index(listing: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    by_id: dict[str, dict[str, Any]] = {}
    for item in normalize_listing_items(listing):
        item_id = item.get("ID")
        if item_id:
            by_id[item_id] = item
    return by_id


def run_rclone_copyto(
    remote_name: str,
    remote_path: str,
    config_file: Path,
    local_path: Path,
) -> None:
    local_path.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            "rclone",
            "copyto",
            f"{remote_name}:{remote_path}",
            str(local_path),
            "--config",
            str(config_file),
        ],
        check=True,
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-map", required=True)
    ap.add_argument("--export-root", required=True)
    ap.add_argument("--manifest-path", required=True)
    ap.add_argument("--source-listing-path", required=True)
    ap.add_argument("--remote-name", required=True)
    ap.add_argument("--config-file", required=True)
    args = ap.parse_args()

    source_map = Path(args.source_map)
    if not source_map.exists():
        raise SystemExit(f"missing source map: {source_map}")

    export_root = Path(args.export_root)
    manifest_path = Path(args.manifest_path)
    source_listing_path = Path(args.source_listing_path)
    config_file = Path(args.config_file)

    result = subprocess.run(
        [
            "rclone",
            "lsjson",
            f"{args.remote_name}:",
            "--config",
            str(config_file),
            "--recursive",
            "--files-only",
            "--metadata",
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    source_listing = json.loads(result.stdout)

    remote_by_id = build_remote_index(source_listing)
    prior_manifest = load_manifest_index(manifest_path)
    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    manifest_rows: list[dict[str, Any]] = []
    failures = 0
    copied = 0
    skipped = 0

    for artifact in ARTIFACTS:
        export_rel = Path(artifact["export_path"])
        local_path = export_root / export_rel
        source_item = remote_by_id.get(artifact["drive_id"])
        record: dict[str, Any] = {
            "title": artifact["title"],
            "work": artifact["work"],
            "canonical_source": artifact["canonical_source"],
            "source_url": artifact["canonical_source"],
            "drive_id": artifact["drive_id"],
            "local_path": str(local_path),
            "export_path": str(export_rel),
            "export_format": artifact["export_format"],
            "provenance": artifact["provenance"],
            "version": artifact["version"],
            "source_map_section": artifact["source_map_section"],
            "remote_name": args.remote_name,
            "remote_path_hint": artifact["remote_path_hint"],
            "exported_at": now,
        }

        if source_item:
            record["remote_path"] = source_item.get("Path")
            record["source_modtime"] = source_item.get("ModTime")
            record["source_mimetype"] = source_item.get("MimeType")
            record["source_metadata"] = source_item.get("Metadata", {})
        else:
            record["status"] = "missing-source"
            record["error"] = "canonical source not found in remote listing"
            manifest_rows.append(record)
            failures += 1
            continue

        existing = prior_manifest.get(str(export_rel))
        should_copy = True
        if local_path.exists() and existing:
            try:
                if (
                    existing.get("drive_id") == artifact["drive_id"]
                    and existing.get("sha256") == sha256(local_path)
                ):
                    should_copy = False
            except OSError:
                should_copy = True

        if should_copy:
            try:
                run_rclone_copyto(
                    args.remote_name,
                    str(source_item["Path"]),
                    config_file,
                    local_path,
                )
                copied += 1
            except subprocess.CalledProcessError as exc:
                record["status"] = "copy-failed"
                record["error"] = f"rclone copyto failed with exit code {exc.returncode}"
                manifest_rows.append(record)
                failures += 1
                continue
        else:
            skipped += 1

        if local_path.exists():
            record["sha256"] = sha256(local_path)
            record["size"] = local_path.stat().st_size
            record["status"] = "exported" if should_copy else "unchanged"
        else:
            record["status"] = "missing-local-output"
            record["error"] = "export completed without creating the destination file"
            failures += 1

        manifest_rows.append(record)

    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    with manifest_path.open("w", encoding="utf-8") as fh:
        for row in manifest_rows:
            fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")

    source_listing_path.parent.mkdir(parents=True, exist_ok=True)
    source_listing_payload = []
    for artifact in ARTIFACTS:
        source_item = remote_by_id.get(artifact["drive_id"])
        source_listing_payload.append(
            {
                "title": artifact["title"],
                "work": artifact["work"],
                "canonical_source": artifact["canonical_source"],
                "drive_id": artifact["drive_id"],
                "remote_path_hint": artifact["remote_path_hint"],
                "remote_path": source_item.get("Path") if source_item else None,
                "source_modtime": source_item.get("ModTime") if source_item else None,
                "source_mimetype": source_item.get("MimeType") if source_item else None,
                "source_metadata": source_item.get("Metadata") if source_item else None,
                "export_path": artifact["export_path"],
                "version": artifact["version"],
                "provenance": artifact["provenance"],
                "source_map_section": artifact["source_map_section"],
                "source_item": source_item,
            }
        )
    source_listing_path.write_text(
        json.dumps(source_listing_payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print(
        f"Fiction corpus refresh complete: {copied} copied, {skipped} skipped, "
        f"{failures} failed."
    )


if __name__ == "__main__":
    main()
