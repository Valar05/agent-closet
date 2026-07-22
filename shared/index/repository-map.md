# Repository Map

Type: Index / orientation / retrieval  
Status: Canon seed  
Date: 2026-07-21  
Owner: Quartermaster  
Verification owner: Auditor  
Purpose: Give a new agent the shortest path from repo entry to useful action.

## Start Here

Read in this order:

1. `README.md` - repo purpose and operating rule.
2. `steering.md` - short operational steering and clean-worker bootstrap.
3. `MANIFEST.md` - current governance, agents, glue gaps, and next work.
4. `shared/index/repository-map.md` - folder map and navigation path.
5. `shared/index/doctrine-index.md` - promoted doctrine and retrieval paths.
6. `shared/doctrine/perspective-guided-command.md` - default command perspective and responsibility-bearing prompt doctrine.
7. `shared/index/agent-index.md` - canonical agent-role inventory and orientation paths.
8. `shared/index/skill-index.md` - reusable skills, procedures, templates, and theory.
9. Target agent pack or task-specific document.

## Top-Level Files

| Path | Authority | Use when |
|---|---|---|
| `README.md` | Repository purpose and operating rule. | Entering the repository cold. |
| `steering.md` | Short operational bootstrap. | Building prompts or initializing a clean worker. |
| `MANIFEST.md` | Current governance and estate status. | Checking what exists, what is missing, and who owns next work. |
| `MANIFEST_AGENTS_AND_HAZARDS.md` | Legacy mixed manifest pending reconciliation. | Archaeology only; current role truth lives in the agent index and `known-hazards/README.md`. |
| `simulation-spaces.md` | Legacy partial simulation-space index. | Archaeology until reconciled with the current simulation roots. |

## Top-Level Folders

| Path | What survives here | Use when |
|---|---|---|
| `agents/` | Role-specific identity, doctrine, loops, examples, and failure modes. | Creating, routing, or orienting an operational agent. |
| `content-factories/` | Queryable generation factories. | Generating repeatable content from a bounded parameter and behavior model. |
| `corpus/fiction/` | Fiction manifest, source map, scene evidence, observation ledger, and book-local observations. | Mining fiction, supporting writing skills, or validating corpus-wide claims. |
| `discoveries/` | Promoted discoveries, origin records, and bounded imported evidence. | Tracing where doctrine or research candidates came from. |
| `docs/` | Public explanation and repository-facing documentation. | Explaining Agent Closet outside the operational bootstrap path. |
| `doctrine/` | Legacy doctrine root pending canonical-path reconciliation. | Archaeology and duplicate review; do not add new promoted doctrine here. |
| `doctrines/` | Legacy and domain doctrine root pending reconciliation. | Reading existing simulation or legacy doctrine; do not assume promotion status from location alone. |
| `shared/` | Cross-agent doctrine, protocols, theories, skills, glossary, and indexes. | Establishing defaults or reusable judgment. |
| `shared/doctrine/` | Canonical promoted-doctrine target. | Preserving judgment that should change behavior. |
| `shared/skills/` | Shared reusable behaviors and applied procedures. | Teaching a recurring move routed into shared infrastructure. |
| `skills/` | Active skill seeds and specialized applied skills awaiting consolidation. | Using or refining newer capabilities such as Scene Compiler, World Pressure Engine, or Kinetic Compression. |
| `shared/theory/` | Higher-level explanatory models. | Connecting doctrine to research, design theory, or learning models. |
| `shared/index/` | Retrieval layer. | Finding what exists and what to read next. |
| `procedures/` | Step-by-step operating procedures. | Running a repeatable workflow. |
| `templates/` | Reusable file shapes. | Creating new entries consistently. |
| `glue/` | Interface and workflow connection layers. Start with `glue/README.md` and `glue/ai-substrate-contract.md`. | Fixing translation problems between tools, agents, or artifacts. |
| `known-hazards/` | Diagnostic lenses and simulation models distinct from operational agents. | Selecting a perspective that exposes burden, cost, obvious truth, release pressure, or mechanism debt. |
| `reports/` | Time-bounded health, capability, and integrity reports. | Reviewing estate condition without treating a report as permanent doctrine. |
| `simulations/` | Active simulation packages and life-simulation engines. | Designing consequence memory, pressure clocks, and world-state feedback loops. |
| `simulation/` | Legacy or specialized simulation material pending reconciliation. | Archaeology and migration review. |
| `sim/` | Legacy simulation stubs pending reconciliation. | Archaeology only; do not create new packages here. |
| `scratch/` | Ore, dumps, fragments, proof notes, and promotion candidates. | Capturing before refining. |
| `tools/` | Repository maintenance, corpus refresh, mining, and validation scripts. | Running repeatable repository operations or integrity checks. |

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

## Hazard / Perspective Path

When a task needs a diagnostic lens rather than an operational agent:

1. Read `known-hazards/README.md`.
2. Read `shared/perspective-routing.md`.
3. Select only the hazard that materially increases information gain.
4. Return to the owning operational agent for implementation and verification.

## Integrity Reports

- Current: `reports/agent-closet-integrity-2026-07-21.md`
- Previous: `reports/agent-closet-integrity-2026-07-14.md`
- Historical capability snapshot: `reports/end_of_day_capability_report_2026_06_23.md`

Reports describe repository state at a date. They do not override current manifests, indexes, or canonical doctrine.

## Current Bottleneck

The repo has enough value that retrieval and authority reconciliation are now the limiting factors.

Primary defects to reduce:

- important docs can require filename memory
- status is inconsistent across older files
- cross-links are incomplete
- scratch can hide promotable ore
- related concepts appear in multiple places without a graph
- top-level `skills/` and `shared/skills/` are both active; routing is explicit, but consolidation remains open
- legacy doctrine and simulation roots appear authoritative without a canonical-path rule
- duplicate manifests and agent lists can contradict current packs

## Retrieval Rule

If a file matters, it should be reachable from at least one index.

If a doctrine changes behavior, it should be reachable from `shared/index/doctrine-index.md`.

If an agent has a responsibility, it should be reachable from `shared/index/agent-index.md`.

If a skill or procedure changes execution, it should be reachable from `shared/index/skill-index.md`.

If a report identifies a durable finding, promote the finding into the canonical doctrine, agent, skill, glue, or index path rather than making the report permanent authority.

Current external-code-review route: start with `procedures/independent-code-review-with-external-critic.md`. Workspace-specific critic adapters are external dependencies and must be resolved from the current environment rather than encoded as a device-local canonical path.

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
