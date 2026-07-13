# Skill and Procedure Index

Type: Index / skill retrieval / procedure retrieval
Status: Canon seed
Date: 2026-06-24
Purpose: Make reusable behaviors, procedures, templates, and theory easier to find.

## Skills

| Skill | Path | Use when |
|---|---|---|
| Perspective Graphing | `shared/skills/perspective-graphing.md` | Comparing encoded perspectives and observer models. |
| Kinetic Compression | `skills/kinetic-compression.md` | Rendering motion, action, contact, and consequence as legible state change. |
| Scene Compiler | `skills/scene-compiler.md` | Generating fiction scenes from image -> pressure -> judgment -> system -> consequence -> next pressure rather than prose imitation. |
| Scene Compiler Runtime | `skills/scene-compiler-runtime.md` | Running the Scene Compiler loop: state, pressure selection, doctrine selection, scene generation, harness validation, repair, and acceptance. |
| World Pressure Engine | `skills/world-pressure-engine.md` | Selecting the next natural story pressure from world state, active clocks, consequence debt, and character judgment. |

## Procedures

| Procedure | Path | Use when |
|---|---|---|
| Capture Save Promote | `procedures/capture-save-promote.md` | Turning chat discoveries into durable repo assets. |
| Deep Ocean Protocol | `procedures/deep-ocean-protocol.md` | Improving cargo/structure before scaling the vessel. |
| Drive Corpus Sync | `procedures/drive-corpus-sync.md` | Syncing Google Drive support corpus exports into repository-readable local evidence. Fiction manuscripts are routed separately. |
| Chat Export Corpus Mining | `procedures/chat-export-corpus-mining.md` | Mining local ChatGPT export shards into bounded derivative scratch/source indexes without committing raw corpus blobs. |
| Independent Code Review With External Critic | `procedures/independent-code-review-with-external-critic.md` | Reviewing PRs with Claude as an external critic through Thunder Brainstorm read-only repo tools, with Quartermaster verification before reporting or posting. |

## Templates

| Template | Path | Use when |
|---|---|---|
| Doctrine Template | `templates/doctrine-template.md` | Creating a new doctrine with consistent metadata. |
| Question Ledger Entry | `templates/question-ledger-entry.md` | Capturing questions, provenance, and follow-up investigation. |

## Glue Layers

| Asset | Path | Use when |
|---|---|---|
| Missing Glue Layers | `glue/missing-glue-layers.md` | A workflow repeatedly fails because tools, agents, or artifacts cannot translate into each other. |
| Chat Export Miner | `tools/mine-chat-export.py` | Querying local ChatGPT export shards and emitting bounded derivative markdown source indexes. |
| Scratch Link Validator | `tools/validate-scratch-links.py` | Checking markdown links, conflict markers, duplicate headings, and fenced code sanity before committing scratch/procedure notes. |

## Theories

| Theory | Path | Use when |
|---|---|---|
| Artificial Continuity | `shared/artificial-continuity.md` | Preserving useful decision-making machinery across sessions and agents. |
| Contagious Operational Memes | `shared/theory/contagious-operational-memes.md` | Transmitting compact, executable judgment that changes behavior in fresh actors. |
| Learning Is Play | `shared/theory/learning-is-play.md` | Connecting play, exploration, feedback, and learning. |
| Simulation as Learning Infrastructure | `shared/theory/simulation-as-learning-infrastructure.md` | Treating simulation as practice infrastructure. |

## Writing / Fiction Generation Route

Use this route when a future agent needs to generate, evaluate, or improve fiction scenes without copying Drew's surface prose:

1. Read `corpus/fiction/fiction-manifest.md` for corpus scope and evidence gate.
2. Read `corpus/fiction/fiction-source-map.md` for local export routing and evidence bridge.
3. Read `skills/scene-compiler.md` for conductor procedure.
4. Read `skills/world-pressure-engine.md` when selecting the next pressure from world state.
5. Read `skills/kinetic-compression.md` when the scene contains motion, contact, combat, rescue, or machine procedure.
6. Read `shared/skills/perspective-graphing.md` when the scene requires multiple observer lenses or interpretation layers.
7. Read `shared/theory/simulation-as-learning-infrastructure.md` when designing repeatable simulations, feedback loops, or consequence memory.
8. Check `corpus/fiction/observations/` and `corpus/fiction/fiction-observation-ledger.md` before promoting any corpus-wide claim.

## Scratch / Ore

| Scratch asset | Path | Use when |
|---|---|---|
| Scratch README | `scratch/README.md` | Understanding the dump-ground rules. |
| Dump Ground | `scratch/dump-ground.md` | Capturing rough notes before refinement. |
| Ore Worth Promoting | `scratch/ore-worth-promoting.md` | Reviewing candidates for promotion. |
| WWDD Proof | `scratch/wwdd-proof.md` | Holding proof notes before mining into stable doctrine. |

## Skill Promotion Rule

A skill is ready for promotion when it changes behavior across more than one task.

A procedure is ready for promotion when repeated execution becomes safer, faster, or less dependent on chat memory.

A template is ready for promotion when repeated files start needing the same shape.

## Open Retrieval Debt

- More skills probably exist as doctrine but are not yet extracted into `shared/skills/`.
- Procedures and skills should be separated by behavior type after another inventory pass.
- Theory docs should point back to doctrines and skills they support.
- Scratch files need periodic Crucible review.
- Top-level `skills/` and `shared/skills/` both exist; future hygiene pass should decide whether to consolidate paths or preserve the split with explicit routing.