# Agent Closet Manifest

Type: Registry / governance manifest
Status: Active bootstrap
Date: 2026-06-22
Source anchors:
- START HERE - Shared Corpus Master Index: https://docs.google.com/document/d/1uovqqBhtcKdykzodSS3LOrMpdNgAlY_pyXcWhBFNfyY
- Doctrine Registry: https://docs.google.com/document/d/1gGaoyUkXqOlISKrI95L9a27TkNxu6FO9I9FTRiZQ6EQ
- 01 - SUPPLEMENTAL: https://docs.google.com/document/d/1CcpJD5CNIS2io_ZW9FeEMgO1OzAQFw0ptPFnxuFtUoU

## Purpose

Agent Closet is a living inheritance system for agent behavior.

It tracks:

- known agents
- missing personalities
- missing glue layers
- doctrine inheritance
- agent profile cards
- failure modes
- update paths

## Core Loop

1. `scratch/` captures messy discoveries.
2. `Prospector` mines repeated signal.
3. `Crucible` pressure-tests claims against evidence.
4. `Quartermaster` promotes durable findings into doctrine.
5. `Foreman` turns doctrine into action or handoff.
6. Future agents inherit the repo, not the chat transcript.

## Repository Shape

- `agents/`: role packs for specialized agents.
- `shared/`: common doctrine, protocols, glossary, phrases, patterns, and registry files.
- `scratch/`: staging area for rough ore and pending promotion candidates.
- `discoveries/`: durable discoveries that need later curation.
- `doctrines/`: focused doctrine pages that have already earned storage.
- `procedures/`: operational sequences that support doctrine execution.

## Authority Stack

```text
Agent Closet -> Drive Brain -> project repositories
```

Agent Closet stores portable doctrine and agent profiles.
Drive Brain stores corpus, registries, promotion logs, and retrieval paths.
Project repos store execution evidence.

## Known Agents

| Agent | Role | Primary Question | Current Status |
|---|---|---|---|
| Command Center | Orchestration / action | What is the smallest useful action? | Needs explicit profile |
| Foreman | Build / delivery | What needs to be built, tested, and delivered? | Existing pack |
| Prospector | Value mining | Is there ore here? | Existing pack |
| Quartermaster | Preservation | Is it preserved? | Needs explicit pack |
| Holocron | June / accessibility continuity | What context and accessibility support matters? | Existing pack |
| WWDD | Judgment service | What has Drew repeatedly done here? | Shared protocol exists |
| Home Center | Household operations | What household state must persist? | Needs profile |
| Pose Lab | Animation workflow | What pose/animation state must persist? | Needs profile |
| Thunderbrainstorm | Artifact/repo mining | What fossils reveal recurring judgment? | Needs profile |

## Candidate Missing Agents

| Agent | Purpose | Why It Exists |
|---|---|---|
| Cartographer | Map agents, docs, repos, workflows, dependencies | The ecosystem needs navigable topology |
| Crucible | Score ore into gold | Promotion needs a dedicated evaluator |
| Archivist | Track provenance and version history | Retrieval without provenance decays |
| Dispatcher | Route tasks to agents/tools | Prevents agent soup |
| Auditor | Detect red builds | Catches plans-before-observation and fake progress |
| Compiler | Convert doctrine into prompts, tests, workflows | Doctrine must change behavior |
| Sommelier | Sense Synthesis specialist | Drinks, food, sensory experiments need a domain agent |
| Mediator | Translate goals across people/agents | Useful for Drew, June, and multi-agent handoffs |
| Quartermaster Prime | Cross-agent governance | Needed when doctrine changes all agents |

## Missing Glue Layers

See `glue/missing-glue-layers.md`.

Highest-value gaps:

1. Agent profile cards for every named agent.
2. Doctrine registry inside repo.
3. Promotion log tied to source evidence.
4. Update pipeline: doctrine change -> affected agents -> file edits -> readback.
5. Red-build detector.
6. Handoff prompt generator.

## Doctrine Inheritance

All agents inherit:

- Evidence beats activity.
- Save -> Read -> Verify.
- Observe Before Advising / Read Before Report.
- Manifesto Comes Later / Merge Request Comes First.
- Doctrine is capability unlocks.
- Reality Negotiation.
- Operational Archaeology.
- Crucible Protocol.
- Human Offloading Doctrine.
- Location-Aware Continuity.

## Promotion Rule

A discovery is not captured until it has:

- name
- durable content
- retrieval keywords
- source/context
- related assets
- acceptance criteria
- readback verification

## Red-Build Triggers

- Advising before reading available artifacts.
- Inventing a new registry when one exists.
- Saving ideas without retrieval paths.
- Treating titles as memory.
- Treating personality as role.
- Explaining instead of making the requested artifact.
- Creating agent names without responsibility boundaries.

## Next Work

1. Add explicit `agents/quartermaster/` pack.
2. Add explicit `agents/command-center/` pack.
3. Add `shared/doctrine-registry.md`.
4. Add `glue/update-pipeline.md`.
5. Add `agents/auditor/` pack for red-build detection.

## Acceptance Criteria

This manifest is working when a future agent can read it and know:

- what exists,
- what is missing,
- which doctrine governs behavior,
- which agent owns the next action,
- what glue layer is missing before another agent is invented.
