# Drive Corpus Sync

Type: Procedure
Status: Active
Date: 2026-06-25
Related doctrine: Capture Save Promote, Location-Aware Continuity, Artifact-Mined Judgment, Reality Negotiation

## Purpose

Make the Google Drive support corpus and supporting documents available to repository workflows through a reproducible local synchronization process.

Repository truth remains the repository.
Drive is source material.

Shared Drive Corpus != Fiction Manuscript Corpus.
This procedure only syncs the shared Drive support corpus under `Corpus/`.
Fiction manuscripts are routed by `corpus/fiction/fiction-manifest.md` and `corpus/fiction/fiction-source-map.md`.

## Storage Rule

Exported Drive material lives under `discoveries/drive-corpus/`.

Do not edit the exported support documents in place unless you are correcting repository-side evidence handling.
Do not overwrite unrelated repository artifacts.
Do not route fiction manuscripts through this export tree.

## Install

On this Termux/Android workspace:

```sh
pkg install -y rclone
```

Verify the install:

```sh
rclone version
```

On desktop Linux/macOS/BSD systems, follow the official rclone install docs instead.

## One-Time Auth

Use the least-privilege Google Drive scope for corpus mining:

- `drive.readonly`

The remote should be configured with a browser-backed OAuth token.

When you need the token, run the browser-side authorization command from a machine that has a web browser:

```sh
rclone authorize drive eyJzY29wZSI6ImRyaXZlLnJlYWRvbmx5In0
```

If the browser does not open automatically, add `--auth-no-open-browser` and open the local callback URL yourself.

## Configure

Use the repo helper:

```sh
tools/configure-drive-remote.sh
```

It writes the remote into the normal rclone config file and sets:

- scope: `drive.readonly`
- export formats: repository-readable formats first
- optional corpus root folder or shared drive ID, if supplied

The helper reads the token from `RCLONE_DRIVE_TOKEN_BLOB` or `RCLONE_DRIVE_TOKEN_BLOB_FILE`.

## Refresh

Use one command to refresh the corpus after the remote exists:

```sh
tools/refresh-drive-corpus.sh
```

The refresh command:

1. Verifies `rclone`.
2. Verifies the configured remote with `rclone lsd`.
3. Copies the Drive corpus into `discoveries/drive-corpus/exports/`.
4. Preserves folder hierarchy where practical.
5. Writes `discoveries/drive-corpus/manifest.jsonl`.
6. Writes `discoveries/drive-corpus/source-listing.json`.

## Export Policy

- Prefer repository-readable text exports.
- Export Google Docs as Markdown when a conversion tool is available locally.
- Otherwise keep the native readable fallback: `TXT`, `DOCX`, or `PDF`.
- Never modify source Drive documents.
- Never delete local evidence automatically unless the operator asks for a prune pass.

## Validation

Expected checks:

```sh
rclone version
rclone listremotes
rclone lsd agentcloset-drive:
```

After the corpus is synced:

```sh
test -s discoveries/drive-corpus/manifest.jsonl
find discoveries/drive-corpus/exports -type f | head
```

The second run should only transfer changed files.

## Risks

- OAuth token refresh is a one-time manual step.
- Markdown export depends on local conversion support.
- The corpus root defaults to `Corpus/`; override it only if the Drive layout changes.
- Shared drives may require `root_folder_id` or `team_drive` at remote creation time.
- Fiction manuscripts require a separate export pass if the repo needs local manuscript ore.

## Acceptance Criteria

This procedure passes when another agent can:

1. Install rclone.
2. Configure the remote with read-only scope.
3. Run one command to refresh the corpus.
4. Read exported manuscripts locally.
5. Mine evidence.
6. Update repository artifacts.
7. Commit changes without manual Drive browsing during the refresh step.
