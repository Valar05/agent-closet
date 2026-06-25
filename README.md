# Agent Closet

Agent Closet is a small, versioned store of orientation packs for agents and humans.

It exists to make the useful parts easy to clone, read, update, and reuse:

- agent identity and working style
- shared doctrine and recurring patterns
- concise examples and operating loops
- scratch notes that can later be mined into stable doctrine

There is no app here. No build. No dashboard. Just markdown files.

This is a living inheritance system for agent behavior. The repo keeps the rules that survive repeated use so future agents inherit judgment instead of starting from zero.

## Start here

1. Read `MANIFEST.md`.
2. Read `shared/index/repository-map.md`.
3. Read `shared/index/doctrine-index.md`.
4. Read `shared/index/agent-index.md` if the task involves agent routing or agent design.
5. Read `shared/index/skill-index.md` if the task involves a reusable behavior, procedure, template, or theory.
6. Read the target agent pack or task-specific file.

## How to use it

1. Clone the repo.
2. Read the relevant agent pack and the shared pages.
3. Update the files when you discover something durable.
4. Commit the change so the next run gets the better version.

## How an AI should orient

1. Read `MANIFEST.md`, `shared/doctrine-registry.md`, `shared/doctrines.md`, `shared/glossary.md`, and the target agent pack.
2. Read `shared/index/repository-map.md` and `shared/index/doctrine-index.md`.
3. Scan `shared/patterns.md`, `shared/prompt-phrases.md`, and `shared/wwdd-protocol.md` for reusable language.
4. Check `scratch/ore-worth-promoting.md` for pending material before inventing anything new.
5. Treat examples as guidance, not as sacred output.
6. Prefer the shortest accurate update to the docs over a big explanation.
7. If a decision repeats, promote it into doctrine.

## Rule

Clone, read, update. Do not worship the prompt blob.

## Scratch Area

Use `scratch/` as the dump ground for rough notes, fragments, and half-formed observations.

The rule is simple: dump first, then mine the useful parts into shared doctrine or agent packs.

## What belongs here

- stable working rules
- repeated decisions
- useful examples
- concise orientation notes
- scratch material that is explicitly marked for later mining

## Current durable stores

- `MANIFEST.md`: repo truth and governance map.
- `shared/doctrine-registry.md`: doctrine ledger with evidence and status.
- `shared/doctrines.md`: shared defaults and promoted doctrines.
- `shared/recursive-sense-synthesis.md`: the continuity framework note.
- `discoveries/`: promoted discovery notes and origin records.
- `discoveries/drive-corpus/`: exported Drive source evidence, manifest, and sync notes.
- `doctrines/`: focused doctrine pages that have already earned storage.
- `scratch/ore-worth-promoting.md`: intake queue for rough ore and promotion candidates.

## What does not belong here

- app code
- unnecessary process theater
- long manifestos
- volatile chatter that should live in a session note instead

Manifesto comes later. Merge request comes first.

## Google Drive Corpus

The Drive corpus workflow lives in `procedures/drive-corpus-sync.md`.

Use `tools/configure-drive-remote.sh` once to create the read-only rclone remote, then use `tools/refresh-drive-corpus.sh` as the single refresh command.

Exported Drive material is stored under `discoveries/drive-corpus/` so repository workflows can read it locally without touching the original Drive documents.
