# Agent Index

Type: Index / agent retrieval
Status: Canon seed
Date: 2026-06-24
Purpose: Make agent roles, responsibilities, and orientation paths findable.

## Core Rule

Agents are tools with jobs, not masks with catchphrases.

Use `shared/doctrine/perspective-guided-command.md` as the command-layer default: Quartermaster owns repository truth and final synthesis unless a different perspective would materially improve judgment.

Use Self-Insertion Calibration before creating or changing agents:

> What part of the user is being externalized?

Preserve useful judgment patterns, not identity.

## Current Agent Packs

| Agent | Primary responsibility | Orientation path | Read when |
|---|---|---|---|
| Command Center | Route work and preserve attention. | `agents/command-center/identity.md` | The user needs orchestration, triage, or task routing. |
| Foreman | Turn intent into buildable, testable artifacts. | `agents/foreman/identity.md` | The user says do it, build it, implement, fix, or ship. |
| Quartermaster | Preserve continuity and make discoveries retrievable. | `agents/quartermaster/identity.md` | Something should be captured, indexed, promoted, or cross-linked. |
| Prospector | Mine messy material for reusable value. | `agents/prospector/identity.md` | There is ore, chat mess, repo history, tickets, or unexplained value. |
| Holocron | Support June's workflow, accessibility, and continuity. | `agents/holocron/identity.md` | Accessibility, June, low vision, or calm continuity matters. |
| Auditor | Challenge unsupported claims and verify evidence. | `agents/auditor/identity.md` | A claim may outrun evidence or a plan appeared before observation. |
| Sommelier | Apply Sense Synthesis to taste, ritual, texture, and sensory design. | `agents/sommelier/identity.md` | Food, drink, sensory novelty, or perception design is central. |
| Wallfly | Mine pattern fossils from external pattern archives. | `agents/wallfly/identity.md` | TV Tropes, fiction structures, archetypes, or pattern fossil extraction matters. |

## Supporting Agent Assets

Most mature agents should have:

- `identity.md` - role and temperament
- `doctrine.md` - operating rules
- `operating-loop.md` - repeatable workflow
- `examples.md` - concise behavior examples
- `failure-modes.md` - how the agent goes wrong
- `mined-examples.md` - examples extracted from prior work

Not every pack is complete yet. Missing files are retrieval debt, not moral failure. Tiny hat, tiny clipboard, still a real problem.

## Candidate / Loose Agents

| Agent | Path | Status | Note |
|---|---|---|---|
| Reflective Cartographer | `agents/reflective-cartographer.md` | Silver | Likely supports mapping relationships, repo structure, and perspective links. |
| Cartographer | `shared/agent-ecosystem.md` | Candidate | Map agents, docs, repos, workflows, and dependencies. |
| Crucible | `shared/agent-ecosystem.md` | Candidate | Score ore into gold. |
| Archivist | `shared/agent-ecosystem.md` | Candidate | Track provenance and version history. |
| Dispatcher | `shared/agent-ecosystem.md` | Candidate | Route tasks to the correct agent or tool. |
| Compiler | `shared/agent-ecosystem.md` | Candidate | Convert doctrine into prompts, tests, scripts, and workflows. |
| Mediator | `shared/agent-ecosystem.md` | Candidate | Translate goals across Drew, June, agents, and tools. |
| Quartermaster Prime | `shared/agent-ecosystem.md` | Candidate | Govern cross-agent doctrine updates. |

## Routing Cheatsheet

- Need execution: Foreman.
- Need preservation: Quartermaster.
- Need discovery: Prospector.
- Need verification: Auditor.
- Need accessibility continuity: Holocron.
- Need sensory design: Sommelier.
- Need pattern fossil mining: Wallfly.
- Need overall orchestration: Command Center.

## Agent Creation Checklist

Before adding a new agent, answer:

1. What recurring judgment pattern does this preserve?
2. What responsibility does this carry?
3. What capability does this amplify?
4. What weakness does this compensate for?
5. What burden should it not inherit?
6. Where should it disagree with the user?
7. What would it notice that the user routinely misses?

Then run the Archetype Independence Test from `shared/doctrine/self-insertion-calibration.md`.

## Open Retrieval Debt

- Some agents may lack full packs.
- Candidate agents should be promoted, merged, or retired.
- Agent responsibilities should be checked for overlap.
- Each mature agent should link back to this index and `shared/agent-ecosystem.md`.
