#!/bin/sh
set -eu

REMOTE_NAME="${RCLONE_REMOTE_NAME:-agentcloset-drive}"
CONFIG_FILE="${RCLONE_CONFIG:-$HOME/.config/rclone/rclone.conf}"
TOKEN_FILE="${RCLONE_DRIVE_TOKEN_BLOB_FILE:-${RCLONE_DRIVE_TOKEN_JSON_FILE:-}}"
TOKEN_BLOB="${RCLONE_DRIVE_TOKEN_BLOB:-${RCLONE_DRIVE_TOKEN_JSON:-}}"
EXPORT_FORMATS="${RCLONE_DRIVE_EXPORT_FORMATS:-txt,docx,pdf}"
ROOT_FOLDER_ID="${RCLONE_DRIVE_ROOT_FOLDER_ID:-}"
TEAM_DRIVE="${RCLONE_DRIVE_TEAM_DRIVE:-}"
SCOPE="${RCLONE_DRIVE_SCOPE:-drive.readonly}"

usage() {
  cat <<EOF_USAGE
Usage: RCLONE_DRIVE_TOKEN_BLOB=<token-blob> $0
   or: RCLONE_DRIVE_TOKEN_BLOB_FILE=/path/to/token.txt $0

Optional env:
  RCLONE_REMOTE_NAME           remote name to create (default: agentcloset-drive)
  RCLONE_CONFIG                config file path (default: ~/.config/rclone/rclone.conf)
  RCLONE_DRIVE_EXPORT_FORMATS   export formats preference (default: txt,docx,pdf)
  RCLONE_DRIVE_ROOT_FOLDER_ID   corpus root folder ID
  RCLONE_DRIVE_TEAM_DRIVE       shared drive ID
  RCLONE_DRIVE_SCOPE            Google scope (default: drive.readonly)
EOF_USAGE
}

if [ "${1:-}" = "-h" ] || [ "${1:-}" = "--help" ]; then
  usage
  exit 0
fi

if [ -n "$TOKEN_FILE" ] && [ -f "$TOKEN_FILE" ]; then
  TOKEN_BLOB="$(tr -d '\r\n' < "$TOKEN_FILE")"
fi

if [ -z "$TOKEN_BLOB" ]; then
  cat <<EOF_NO_TOKEN
No token blob provided.

Run the browser-side authorization flow first:
  rclone authorize drive eyJzY29wZSI6ImRyaXZlLnJlYWRvbmx5In0

Then re-run this command with either:
  RCLONE_DRIVE_TOKEN_BLOB='<authorize-output-blob>'
or:
  RCLONE_DRIVE_TOKEN_BLOB_FILE=/path/to/token.txt
EOF_NO_TOKEN
  exit 2
fi

python3 - "$CONFIG_FILE" <<'PY'
from pathlib import Path
import sys

Path(sys.argv[1]).expanduser().parent.mkdir(parents=True, exist_ok=True)
PY

if RCLONE_CONFIG="$CONFIG_FILE" rclone listremotes | grep -qx "${REMOTE_NAME}:"; then
  cat <<EOF_EXISTS
Remote '$REMOTE_NAME' already exists in $CONFIG_FILE.
Delete or update it before re-running this helper.
EOF_EXISTS
  exit 0
fi

set -- rclone config create "$REMOTE_NAME" drive \
  config_token "$TOKEN_BLOB" \
  config_is_local false \
  scope "$SCOPE" \
  export_formats "$EXPORT_FORMATS"

if [ -n "$ROOT_FOLDER_ID" ]; then
  set -- "$@" root_folder_id "$ROOT_FOLDER_ID"
fi

if [ -n "$TEAM_DRIVE" ]; then
  set -- "$@" team_drive "$TEAM_DRIVE"
fi

RCLONE_CONFIG="$CONFIG_FILE" "$@"

printf '%s\n' "Configured $REMOTE_NAME in $CONFIG_FILE"
