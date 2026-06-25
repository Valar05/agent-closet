#!/bin/sh
set -eu

REPO_ROOT="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
REMOTE_NAME="${RCLONE_FICTION_REMOTE_NAME:-agentcloset-drive}"
CONFIG_FILE="${RCLONE_CONFIG:-$HOME/.config/rclone/rclone.conf}"
SOURCE_MAP="${RCLONE_FICTION_SOURCE_MAP:-$REPO_ROOT/corpus/fiction/fiction-source-map.md}"
EXPORT_ROOT="${RCLONE_FICTION_EXPORT_ROOT:-$REPO_ROOT/discoveries/fiction-corpus/exports}"
MANIFEST_PATH="${RCLONE_FICTION_MANIFEST:-$REPO_ROOT/discoveries/fiction-corpus/manifest.jsonl}"
SOURCE_LISTING="${RCLONE_FICTION_SOURCE_LISTING:-$REPO_ROOT/discoveries/fiction-corpus/source-listing.json}"

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || {
    printf '%s\n' "Missing required command: $1" >&2
    exit 1
  }
}

require_cmd rclone
require_cmd python3

python3 - "$MANIFEST_PATH" "$SOURCE_LISTING" "$EXPORT_ROOT" <<'EOF_PY'
from pathlib import Path
import sys

Path(sys.argv[1]).expanduser().parent.mkdir(parents=True, exist_ok=True)
Path(sys.argv[2]).expanduser().parent.mkdir(parents=True, exist_ok=True)
Path(sys.argv[3]).expanduser().mkdir(parents=True, exist_ok=True)
EOF_PY

if ! rclone listremotes --config "$CONFIG_FILE" | grep -qx "${REMOTE_NAME}:"; then
  cat <<EOF_NOT_CONFIGURED >&2
Rclone remote '$REMOTE_NAME' is not configured in $CONFIG_FILE.

Configure it first:
  RCLONE_DRIVE_TOKEN_JSON='<token-json>' tools/configure-drive-remote.sh

The token comes from:
  rclone authorize drive eyJzY29wZSI6ImRyaXZlLnJlYWRvbmx5In0
EOF_NOT_CONFIGURED
  exit 2
fi

python3 "$REPO_ROOT/tools/fiction_corpus_manifest.py" \
  --source-map "$SOURCE_MAP" \
  --export-root "$EXPORT_ROOT" \
  --manifest-path "$MANIFEST_PATH" \
  --source-listing-path "$SOURCE_LISTING" \
  --remote-name "$REMOTE_NAME" \
  --config-file "$CONFIG_FILE"
