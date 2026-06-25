#!/bin/sh
set -eu

REPO_ROOT="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
SOURCE_MAP="${FICTION_SOURCE_MAP:-$REPO_ROOT/corpus/fiction/fiction-source-map.md}"
MANIFEST_PATH="${FICTION_MANIFEST:-$REPO_ROOT/discoveries/fiction-corpus/manifest.jsonl}"
OBSERVATION_ROOT="${FICTION_OBSERVATION_ROOT:-$REPO_ROOT/corpus/fiction/observations}"

usage() {
  cat <<'EOF_USAGE'
Usage:
  tools/mine-fiction-work.sh [--json] <slug>

Valid slugs:
  omnitread
  holding-vigil
  lighter-than-air
  revelation
  jumpy-bug
  inhuman-reaches
  shattered-bonds-online
  fatal-vow-exception
  veil-of-liquid-stars
  aegis-of-victory
EOF_USAGE
}

json_mode=0
if [ "${1:-}" = "--json" ]; then
  json_mode=1
  shift
fi

slug="${1:-}"
if [ -z "$slug" ]; then
  usage >&2
  exit 2
fi

if [ ! -f "$SOURCE_MAP" ]; then
  printf '%s\n' "Missing source map: $SOURCE_MAP" >&2
  exit 1
fi
if [ ! -f "$MANIFEST_PATH" ]; then
  printf '%s\n' "Missing fiction export manifest: $MANIFEST_PATH" >&2
  exit 1
fi
if [ ! -d "$OBSERVATION_ROOT" ]; then
  printf '%s\n' "Missing observation root: $OBSERVATION_ROOT" >&2
  exit 1
fi

python3 - "$slug" "$json_mode" "$SOURCE_MAP" "$MANIFEST_PATH" "$OBSERVATION_ROOT" <<'EOF_PY'
from __future__ import annotations

import json
import sys
from pathlib import Path

slug = sys.argv[1]
json_mode = sys.argv[2] == '1'
source_map = Path(sys.argv[3])
manifest_path = Path(sys.argv[4])
observation_root = Path(sys.argv[5])

slug_info = {
    'omnitread': {
        'work': 'Omnitread',
        'observation': 'omnitread.md',
        'export_prefixes': ['omnitread/Omnitread'],
        'status': 'Mined / direct pass recorded',
        'evidence_status': 'Direct evidence present; not promoted',
    },
    'holding-vigil': {
        'work': 'Holding Vigil',
        'observation': 'holding-vigil.md',
        'export_prefixes': ['holding-vigil/Holding Vigil - Revised and Improved'],
        'status': 'Pending direct mining / version verify',
        'evidence_status': 'Placeholder only; no direct book-local observations yet',
    },
    'lighter-than-air': {
        'work': 'Lighter Than Air',
        'observation': 'lighter-than-air.md',
        'export_prefixes': [
            'lighter-than-air/book-1/Lighter Than Air 1',
            'lighter-than-air/book-2/Lighter Than Air 2',
        ],
        'status': 'Pending direct mining',
        'evidence_status': 'Placeholder only; no direct book-local observations yet',
    },
    'revelation': {
        'work': 'Revelation',
        'observation': 'revelation.md',
        'export_prefixes': ['revelation/Revelation'],
        'status': 'Mined / substantial observation pass recorded',
        'evidence_status': 'Direct evidence present; not promoted',
    },
    'jumpy-bug': {
        'work': 'Jumpy Bug / Biblical',
        'observation': 'jumpy-bug.md',
        'export_prefixes': ['jumpy-bug/Biblical'],
        'status': 'Mined / scene index started',
        'evidence_status': 'Direct scene evidence present; observation artifact and scene index exist',
    },
    'inhuman-reaches': {
        'work': 'Inhuman Reaches',
        'observation': 'inhuman-reaches.md',
        'export_prefixes': [
            'inhuman-reaches/part-1-revised/Inhuman Reaches 1, Revised',
            'inhuman-reaches/part-2-revised/Inhuman Reaches Pt 2 Revised',
        ],
        'status': 'Mined / sequence verify complete enough for first-pass routing',
        'evidence_status': 'Direct evidence present; not promoted',
    },
    'shattered-bonds-online': {
        'work': 'Shattered Bonds / Shattered Bonds Online',
        'observation': 'shattered-bonds-online.md',
        'export_prefixes': ['shattered-bonds-online/Shattered Bonds Online v2'],
        'status': 'Pending version verify',
        'evidence_status': 'Placeholder only; version reconciliation pending',
    },
    'fatal-vow-exception': {
        'work': 'Fatal Vow Exception',
        'observation': 'fatal-vow-exception.md',
        'export_prefixes': ['fatal-vow-exception/Fatal Vow Exception v2'],
        'status': 'Pending direct mining',
        'evidence_status': 'Placeholder only; no direct book-local observations yet',
    },
    'veil-of-liquid-stars': {
        'work': 'Veil of Liquid Stars',
        'observation': 'veil-of-liquid-stars.md',
        'export_prefixes': ['veil-of-liquid-stars/Veil of Liquid Stars'],
        'status': 'Mined / observation artifact present',
        'evidence_status': 'Direct evidence present; not promoted',
    },
    'aegis-of-victory': {
        'work': 'Aegis of Victory',
        'observation': 'aegis-of-victory.md',
        'export_prefixes': ['aegis-of-victory/Aegis of Victory'],
        'status': 'Pending direct mining',
        'evidence_status': 'Placeholder only; no direct book-local observations yet',
    },
}

valid_slugs = list(slug_info)
if slug not in slug_info:
    print('Unknown slug: %s' % slug, file=sys.stderr)
    print('Valid choices: %s' % ', '.join(valid_slugs), file=sys.stderr)
    raise SystemExit(2)

info = slug_info[slug]
source_text = source_map.read_text(encoding='utf-8')
if info['work'].split(' / ')[0] not in source_text:
    print(f"Could not locate work in source map: {info['work']}", file=sys.stderr)
    raise SystemExit(1)

observation_file = observation_root / info['observation']
if not observation_file.exists():
    print(f"Missing observation artifact: {observation_file}", file=sys.stderr)
    raise SystemExit(1)

rows = []
for line in manifest_path.read_text(encoding='utf-8').splitlines():
    if line.strip():
        rows.append(json.loads(line))

matches = []
for row in rows:
    export_path = row.get('export_path', '')
    if any(export_path.startswith(prefix) for prefix in info['export_prefixes']):
        matches.append(row)

if not matches:
    print(f"Export not found in manifest for slug '{slug}'", file=sys.stderr)
    raise SystemExit(1)

row = matches[0]
export_path = row.get('local_path')
if not export_path:
    print(f"Manifest entry missing local_path for slug '{slug}'", file=sys.stderr)
    raise SystemExit(1)

export_file = Path(export_path)
if not export_file.exists():
    print(f"Export file missing on disk: {export_file}", file=sys.stderr)
    raise SystemExit(1)

hash_value = row.get('sha256')
if not hash_value:
    print(f"Manifest entry missing hash for slug '{slug}'", file=sys.stderr)
    raise SystemExit(1)

timestamp = row.get('exported_at')
if not timestamp:
    print(f"Manifest entry missing export timestamp for slug '{slug}'", file=sys.stderr)
    raise SystemExit(1)

packet = {
    'work': info['work'],
    'slug': slug,
    'export_path': str(export_file),
    'observation_file': str(observation_file),
    'status': info['status'],
    'evidence_status': info['evidence_status'],
    'hash': hash_value,
    'exported_at': timestamp,
    'ready': True,
}

if json_mode:
    print(json.dumps(packet, ensure_ascii=False, sort_keys=True, indent=2))
    raise SystemExit(0)

print('================================')
print(f"WORK:\n{info['work']}")
print('\nSOURCE:\n')
print(export_file)
print('\nOBSERVATION TARGET:\n')
print(observation_file)
print('\nCURRENT STATUS:\n')
print(info['status'])
print('\nEVIDENCE:\n')
print(info['evidence_status'])
print('\nREADY FOR:\nProspector')
print('================================')
print()
print('Suggested next command:')
print(f'/prospector {slug}')
print()
print('Objective:')
print('Strengthen existing observations.')
print('Do not rewrite.')
print('Append evidence.')
print('Cross-link to ledger.')
print('Stop before doctrine promotion.')
EOF_PY
