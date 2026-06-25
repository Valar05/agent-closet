# Drive Corpus

This directory holds exported Google Drive source material for repository workflows.

Policy:

- Drive is source material.
- Repository artifacts are the truth store.
- Do not edit the original Drive documents from here.
- Preserve folder hierarchy where practical.
- Preserve provenance in `manifest.jsonl` and `source-listing.json`.

Expected outputs from `tools/refresh-drive-corpus.sh`:

- `exports/` - repository-readable exported manuscripts and supporting documents.
- `manifest.jsonl` - one JSON object per exported file.
- `source-listing.json` - the rclone source listing used to build the manifest.

If Markdown export is available, prefer it.
Otherwise keep the best repository-readable fallback: `TXT`, `DOCX`, or `PDF`.
