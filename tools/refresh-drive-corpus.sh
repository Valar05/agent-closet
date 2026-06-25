#!/bin/sh
set -eu

REPO_ROOT="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
REMOTE_NAME="${RCLONE_REMOTE_NAME:-agentcloset-drive}"
CONFIG_FILE="${RCLONE_CONFIG:-$HOME/.config/rclone/rclone.conf}"
EXPORT_ROOT="${RCLONE_DRIVE_EXPORT_ROOT:-$REPO_ROOT/discoveries/drive-corpus/exports}"
MANIFEST_PATH="${RCLONE_DRIVE_MANIFEST:-$REPO_ROOT/discoveries/drive-corpus/manifest.jsonl}"
SOURCE_LISTING="${RCLONE_DRIVE_SOURCE_LISTING:-$REPO_ROOT/discoveries/drive-corpus/source-listing.json}"
REMOTE_ROOT="${RCLONE_DRIVE_REMOTE_ROOT:-Corpus}"
EXPORT_FORMATS="${RCLONE_DRIVE_EXPORT_FORMATS:-txt,docx,pdf}"

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || {
    printf '%s\n' "Missing required command: $1" >&2
    exit 1
  }
}

require_cmd rclone
require_cmd python3

python3 - "$MANIFEST_PATH" "$EXPORT_ROOT" <<'PY'
from pathlib import Path
import sys

Path(sys.argv[1]).expanduser().parent.mkdir(parents=True, exist_ok=True)
Path(sys.argv[2]).expanduser().mkdir(parents=True, exist_ok=True)
PY

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

REMOTE_PATH="${REMOTE_NAME}:"
[ -n "$REMOTE_ROOT" ] && REMOTE_PATH="${REMOTE_NAME}:$REMOTE_ROOT"

printf '%s\n' "Checking remote directories..."
rclone lsd "$REMOTE_PATH" --config "$CONFIG_FILE"

printf '%s\n' "Capturing source listing..."
rclone lsjson "$REMOTE_PATH" \
  --config "$CONFIG_FILE" \
  --recursive \
  --files-only \
  --metadata \
  > "$SOURCE_LISTING"

printf '%s\n' "Copying corpus into $EXPORT_ROOT ..."
rclone copy "$REMOTE_PATH" "$EXPORT_ROOT" \
  --config "$CONFIG_FILE" \
  --drive-export-formats "$EXPORT_FORMATS" \
  --create-empty-src-dirs

printf '%s\n' "Generating manifest..."
python3 "$REPO_ROOT/tools/drive_corpus_manifest.py" \
  --source-listing "$SOURCE_LISTING" \
  --export-root "$EXPORT_ROOT" \
  --manifest-path "$MANIFEST_PATH" \
  --remote-name "$REMOTE_NAME" \
  --remote-root "$REMOTE_ROOT"

printf '%s\n' "Drive corpus refresh complete."
