# Fiction Corpus

This directory holds exported fiction manuscripts for repository-local reading.

Policy:

- Fiction manuscripts are source material.
- Observation files, ledgers, and scene indexes are downstream evidence only.
- Do not edit canonical manuscripts in place here.
- Do not route the shared Drive support corpus through this tree.

Expected outputs from `tools/refresh-fiction-corpus.sh`:

- `exports/` - exported Priority A fiction manuscripts, preserved in the directory layout from `corpus/fiction/fiction-source-map.md`
- `manifest.jsonl` - one JSON object per exported artifact
- `source-listing.json` - source-map-driven export listing plus rclone metadata for the exported manuscripts

Fallback policy:

- Prefer Markdown only if a real conversion path exists.
- Otherwise keep the repository-readable export that Drive provides, usually `TXT`.
- Keep alternate manuscript versions in sibling paths, not by overwriting the canonical export.
