# Deep Ocean Corpus Support Audit - 2026-07-03

Status: scratch capture
Owner: Quartermaster
Date: 2026-07-03
Scope: Drink Simulation / Sense Synthesis mining across Agent Closet and local `droobiedoo/wwdd` corpus.

Related:

- [Deep Ocean Protocol](../procedures/deep-ocean-protocol.md)
- [Capture, Save, Promote](../procedures/capture-save-promote.md)
- [Drink Simulation Sense Synthesis Collation](drink-simulation-sense-synthesis-collation.md)
- [Droobiedoo Chat Corpus Sense Synthesis Mining](droobiedoo-chat-corpus-sense-synthesis-mining.md)
- [Ore Worth Promoting](ore-worth-promoting.md)
- [Missing Glue Layers](../glue/missing-glue-layers.md)
- [Sommelier](../agents/sommelier/identity.md)

## Capability Gained

Agent Closet can now preserve a domain-specific simulation capability from a raw chat corpus without publishing the raw corpus.

Before this pass, Drink Compiler was a queue item and Sense Synthesis was a promoted general doctrine. After this pass, the repo has a scratch evidence chain:

1. `scratch/drink-simulation-sense-synthesis-collation.md` defines Drink Simulation as perceptual composition with levers, modes, failure modes, and promotion gates.
2. `scratch/droobiedoo-chat-corpus-sense-synthesis-mining.md` grounds the drink/sense model in local `droobiedoo/wwdd` corpus evidence.
3. `scratch/ore-worth-promoting.md` links Drink Compiler and Drink Simulation / Perceptual Composition as strong ore rather than isolated recipe notes.

The practical unlock: future agents can ask `what perceptual levers, modes, and corpus evidence support this drink simulation idea?` and get a repository answer instead of re-mining the chat export from scratch.

## Knowledge Capture

### Rules

- Raw `droobiedoo/wwdd` corpus exports stay local-only. Commit only derivative scratch, indexed, or curated artifacts.
- Corpus-derived claims need shard/date/title or another stable source handle. Raw JSON line numbers are not stable enough by themselves.
- Sense Synthesis work must model ingredients by perceptual jobs, not recipe identity.
- Drink Simulation remains scratch until prediction/build/observation/deviation records exist.
- Medical, supplement, fermentation, alcohol, nicotine, and inhalation material from raw chat must be treated as safety-sensitive and not promoted as casual advice.

### Patterns

- Query broad, then narrow to high-signal conversations before writing doctrine.
- Preserve a derivative mining note rather than copying long chat passages.
- Separate general doctrine (`shared/sense-synthesis.md`) from domain scratch (`scratch/drink-simulation-sense-synthesis-collation.md`).
- Use `scratch/ore-worth-promoting.md` as the queue hook so the scratch file is findable.
- During rebase conflicts, preserve the richer remote artifact and fold local additions into it rather than overwriting repository truth.

### Design Decisions

- Saved the mining result in Agent Closet scratch, not `droobiedoo`, because the user asked for Agent Closet continuity and the artifact is doctrine/simulation ore.
- Left raw corpus untouched in `droobiedoo` to honor the local-only policy.
- Treated missing `wwdd/indexed/` and `wwdd/curated/` folders as friction, not a blocker.
- Kept Drink Simulation below promotion level because it still lacks logged experiments, a schema, and a contribution ledger.

### Discoveries

- The corpus supports at least four drink modes: Hydration, Ritual, Compiler, and Fermentation.
- The strongest reusable claim is not `mocktail recipes`; it is `componentized perceptual levers plus feedback`.
- `droobiedoo` already contains a capability-archaeology pattern that can be reused for narrower domains like Sense Synthesis.
- The current Agent Closet corpus toolchain is stronger for Drive/fiction exports than for local ChatGPT export mining.

## What Supports The Corpus Now

### Tools

Existing useful tools:

- `tools/refresh-drive-corpus.sh` and `tools/drive_corpus_manifest.py` support the shared Drive support corpus.
- `tools/refresh-fiction-corpus.sh`, `tools/fiction_corpus_manifest.py`, and `tools/mine-fiction-work.sh` support the fiction manuscript corpus.
- Ad hoc defensive Python scripts can parse `droobiedoo/wwdd/conversations-*.json`, but this is not yet durable tooling.

Missing tools:

- `tools/mine-chat-export.py`: query local ChatGPT export shards, emit source handles, hit counts, and compact snippets.
- `tools/chat-export-source-index.py`: build a stable derivative index with conversation id, shard, title, date, tags, and allowed excerpt policy.
- `tools/sense-synthesis-extract.py`: domain-specific extractor for levers, modes, components, processes, failures, and safety flags.
- `tools/validate-scratch-links.py`: cheap markdown link/fence/duplicate-heading check used before committing scratch notes.

### Workflows

Existing workflows:

- Agent Closet scratch intake: capture rough ore in `scratch/`, then queue promotion in `scratch/ore-worth-promoting.md`.
- Capture, Save, Promote: name, store, index, read back, and verify.
- Deep Ocean: identify repeated friction, convert it into reusable cargo, avoid creating a new platform.
- Droobiedoo raw-local policy: raw export stays on disk; derivatives can be committed intentionally.

Missing workflows:

- Chat export mining workflow: target concept -> query list -> high-signal conversation set -> derivative note -> promotion queue link.
- Safety-sensitive corpus workflow: tag medical/alcohol/nicotine/inhalation/supplement material so future agents do not promote advice without review.
- Rebase conflict workflow for doctrine stores: compare remote/current/local, preserve richer repo truth, document resolution note when source evidence names disagree with tracked files.

### Documents

Existing support documents:

- `MANIFEST.md`: authority stack, scratch role, promotion rule, and repo shape.
- `README.md`: Agent Closet orientation and scratch usage.
- `procedures/deep-ocean-protocol.md`: reusable audit loop.
- `procedures/capture-save-promote.md`: capture requirements and readback rule.
- `glue/missing-glue-layers.md`: names `Sense Synthesis Log` as missing glue.
- `agents/sommelier/identity.md`: owner for drink, food, and sensory experiments.
- `shared/sense-synthesis.md`: promoted general doctrine.
- `/storage/emulated/0/Documents/GodotProjects/droobiedoo/README.md`: raw corpus export policy.
- `/storage/emulated/0/Documents/GodotProjects/droobiedoo/reports/capability-timeline.md`: proven pattern for corpus archaeology.

Missing documents:

- `scratch/sense-synthesis-log-template.md`: the experiment record future agents should fill in.
- `scratch/drink-compiler-schema.md`: schema for inventory, constraints, target state, levers, process stage, feedback, and safety notes.
- `scratch/droobiedoo-sense-synthesis-source-index.md`: stable source index for the high-signal chat threads.
- `procedures/chat-export-corpus-mining.md`: generic local ChatGPT export mining procedure.
- `glue/corpus-boundary-map.md`: one place distinguishing Drive support corpus, fiction manuscript corpus, local ChatGPT export corpus, project repos, and scratch derivatives.

## Friction Audit

### Missing Scripts

Manual Python was used to inspect JSON shape, scan terms, score conversations, extract snippets, and validate markdown links. This should be one reusable script.

### Missing Tools

There is no dedicated local ChatGPT export miner. Existing corpus tools serve Drive and fiction workflows, not `droobiedoo/wwdd` shards.

### Missing Tests

No validator proves that derivative scratch notes avoid raw-corpus leakage, preserve stable source handles, and keep links valid.

### Missing Documentation

The raw-local policy exists in `droobiedoo/README.md`, but Agent Closet does not yet have a corpus boundary map explaining which corpus lives where and where derivatives belong.

### Missing Automation

No automation updates `scratch/ore-worth-promoting.md` or source indexes when a new scratch mining note is added.

## Build Next

Build `tools/mine-chat-export.py` in Agent Closet.

Minimum useful behavior:

- Input: root path, query terms, optional max results.
- Reads `conversations-*.json` defensively.
- Outputs a derivative markdown source index with shard, conversation id, date, title, matched terms, and short bounded snippets.
- Refuses to include raw full conversations.
- Tags safety-sensitive domains.
- Can be reused for Sense Synthesis, agent behavior, game-design patterns, or capability archaeology.

This is the smallest tool that saves future time, reduces raw-corpus risk, and supports the next scratch artifacts.
