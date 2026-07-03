# Chat Export Corpus Mining

Type: Procedure
Status: Scratch-supported active procedure
Date: 2026-07-03
Related:

- `../tools/mine-chat-export.py`
- `../tools/validate-scratch-links.py`
- `../scratch/deep-ocean-corpus-support-audit-2026-07-03.md`
- `../scratch/droobiedoo-chat-corpus-sense-synthesis-mining.md`

## Purpose

Mine a local ChatGPT export into derivative Agent Closet evidence without committing raw corpus blobs.

## Raw Corpus Rule

Raw exports stay local-only. For `droobiedoo`, the source corpus is `/storage/emulated/0/Documents/GodotProjects/droobiedoo/wwdd/` and repository policy allows only intentionally curated or indexed derivatives.

Do not commit:

- `chat.html`
- `conversations-*.json`
- `shared_conversations.json`
- `file-*.dat` attachments
- full conversation dumps

## Workflow

1. Name the target concept.
2. Choose explicit search terms.
3. Run `python tools/mine-chat-export.py` with bounded snippet limits.
4. Review the generated source index and identify high-signal conversations.
5. Write or update a scratch synthesis note that extracts rules, patterns, gaps, and promotion gates.
6. Add or strengthen the relevant queue entry in `scratch/ore-worth-promoting.md`.
7. Run `tools/validate-scratch-links.py` and `git diff --check` before committing.

## Example

```sh
tools/mine-chat-export.py   --root /storage/emulated/0/Documents/GodotProjects/droobiedoo/wwdd   --terms "sense synthesis,drink compiler,mocktail,gentian,bitters,carbonation,tannin,dilution,mouthfeel,aroma,electrolyte,hydration,kvass,kilju"   --title "Droobiedoo Sense Synthesis Source Index"   --out scratch/droobiedoo-sense-synthesis-source-index.md   --max-conversations 30   --max-snippets 2
```

## Safety Tags

The miner tags conversations containing likely medical, alcohol, nicotine, or inhalation material. A tag does not reject the record; it warns future agents not to promote advice casually.

## Acceptance Criteria

The procedure passes when:

- the raw corpus remains untracked,
- the derivative index has stable source handles,
- snippets are bounded,
- safety-sensitive records are tagged,
- the scratch synthesis links back to the source index or source conversations,
- markdown validation and `git diff --check` pass.
