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
| `shared/skills/` | Reusable behaviors and applied procedures. | Teaching agents how to perform a recurring move. |
| `shared/theory/` | Higher-level explanatory models. | Connecting doctrine to research, design theory, or learning models. |
| `shared/index/` | Retrieval layer. | Finding what exists and what to read next. |
| `procedures/` | Step-by-step operating procedures. | Running a repeatable workflow. |
| `templates/` | Reusable file shapes. | Creating new entries consistently. |
| `glue/` | Interface and workflow connection layers. | Fixing translation problems between tools, agents, or artifacts. |
| `scratch/` | Ore, dumps, fragments, and proof notes. | Capturing before refining. |

## Current Bottleneck

The repo has enough value that retrieval is now the limiting factor.

Primary defects to reduce:

- important docs can require filename memory
- status is inconsistent across older files
- cross-links are incomplete
- scratch can hide promotable ore
- related concepts appear in multiple places without a graph

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
