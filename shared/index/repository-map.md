# Repository Map

Type: Index / orientation / retrieval
Status: Canon seed
Date: 2026-06-24
Purpose: Give a new agent the shortest path from repo entry to useful action.

## Start Here

Read in this order:

1. `README.md` - repo purpose and operating rule.
2. `shared/index/repository-map.md` - folder map and navigation path.
3. `shared/index/doctrine-index.md` - promoted doctrine and retrieval paths.
4. `shared/index/agent-index.md` - agent roles and where to orient.
5. `shared/index/skill-index.md` - reusable skills, procedures, templates, and theory.
6. Target agent pack or task-specific document.

## Top-Level Folders

| Path | What survives here | Use when |
|---|---|---|
| `agents/` | Role-specific identity, doctrine, loops, examples, and failure modes. | Creating, routing, or orienting an agent. |
| `shared/` | Cross-agent doctrine, protocols, theories, skills, glossary, and indexes. | Establishing defaults or reusable judgment. |
| `shared/doctrine/` | Promoted doctrine with provenance and acceptance criteria. | Preserving judgment that should change behavior. |
| `shared/skills/` | Shared reusable behaviors and applied procedures. | Teaching agents how to perform a recurring move that has already been routed into shared infrastructure. |
| `skills/` | Active skill seeds and specialized applied skills awaiting consolidation. | Using or refining newer capabilities such as Scene Compiler, World Pressure Engine, or Kinetic Compression. |
| `shared/theory/` | Higher-level explanatory models. | Connecting doctrine to research, design theory, or learning models. |
| `shared/index/` | Retrieval layer. | Finding what exists and what to read next. |
| `procedures/` | Step-by-step operating procedures. | Running a repeatable workflow. |
| `templates/` | Reusable file shapes. | Creating new entries consistently. |
| `glue/` | Interface and workflow connection layers. Start with `glue/README.md` and `glue/ai-substrate-contract.md`. | Fixing translation problems between tools, agents, or artifacts. |
| `corpus/fiction/` | Fiction manifest, source map, scene evidence, observation ledger, and book-local observations. | Mining fiction, supporting writing skills, or validating corpus-wide claims. |
| `simulations/` | Simulation reports and life-simulation engines. | Designing consequence memory, pressure clocks, and world-state feedback loops. |
| `scratch/` | Ore, dumps, fragments, and proof notes. | Capturing before refining. |

## Writing / Fiction Generation Path

When the task involves Drew's fiction, narrative judgment, scene generation, or manuscript mining, read in this order:

1. `corpus/fiction/fiction-manifest.md` - canonical corpus scope and evidence gate.
2. `corpus/fiction/fiction-source-map.md` - local export bridge and evidence routing.
3. `corpus/fiction/observations/README.md` - book-local evidence rules.
4. `skills/scene-compiler.md` - conductor skill for image -> pressure -> judgment -> system -> consequence -> next pressure.
5. `skills/world-pressure-engine.md` - pressure selection and clock validation.
6. `skills/kinetic-compression.md` - action/contact/state-change rendering.
7. `shared/skills/perspective-graphing.md` - observer lenses and interpretation conflicts.
8. `shared/theory/simulation-as-learning-infrastructure.md` - consequence simulation, feedback loops, and survivable disagreement.
9. `corpus/fiction/fiction-observation-ledger.md` plus the relevant book-local observation file before promoting any claim.

## Current Bottleneck

The repo has enough value that retrieval is now the limiting factor.

Primary defects to reduce:

- important docs can require filename memory
- status is inconsistent across older files
- cross-links are incomplete
- scratch can hide promotable ore
- related concepts appear in multiple places without a graph
- top-level `skills/` and `shared/skills/` are both active; routing is now explicit, but consolidation remains open

## Retrieval Rule

If a file matters, it should be reachable from at least one index.

If a doctrine changes behavior, it should be reachable from `shared/index/doctrine-index.md`.

If an agent has a responsibility, it should be reachable from `shared/index/agent-index.md`.

If a skill or procedure changes execution, it should be reachable from `shared/index/skill-index.md`.

## Promotion Status Labels

Use these labels consistently:

- Ore: captured but not refined.
- Silver: useful but still provisional.
- Gold: promoted and expected to change behavior.
- Canon: foundational default for future agents.
- Obsolete: preserved for history but no longer recommended.

## New-Agent Acceptance Test

A new agent should be able to answer:

- What exists?
- Where is it?
- Why does it matter?
- What is promoted?
- What is canonical?
- What should I read next?

without asking Drew or relying on chat history.