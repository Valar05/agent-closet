# Agent Closet Manifest

Type: Registry / governance manifest
Status: Active bootstrap
Date: 2026-07-13
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

Command work defaults to `Quartermaster` under `shared/doctrine/perspective-guided-command.md`: preserve repository truth, verify evidence, and consult another perspective only when it would notice what Quartermaster would miss.

Visual work inherits `shared/doctrine/visual-truth-authority.md`: screenshots, contact sheets, video, live captures, and human visual reports are the authority. Telemetry and green checks are support evidence only.

Current external research and promotion intake lives in `discoveries/agent-closet-research-radar-2026-07-13.md`.

## Known Agents

| Agent | Role | Primary Question | Current Status |
|---|---|---|---|
| Command Center | Orchestration / action | What is the smallest useful action? | Existing pack |
| Foreman | Build / delivery | What needs to be built, tested, and delivered? | Existing pack |
| Prospector | Value mining | Is there ore here? | Existing pack |
| Quartermaster | Preservation | Is it preserved? | Existing pack |
| Holocron | June / accessibility continuity | What context and accessibility support matters? | Existing pack |
| Auditor | Verification / red-build detection | What claim outruns the evidence? | Existing pack |
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
| Compiler | Convert doctrine into prompts, tests, workflows | Doctrine must change behavior |
| Sommelier | Sense Synthesis specialist | Drinks, food, sensory experiments need a domain agent |
| Mediator | Translate goals across people/agents | Useful for Drew, June, and multi-agent handoffs |
| Quartermaster Prime | Cross-agent governance | Needed when doctrine changes all agents |

## Missing Glue Layers

See `glue/missing-glue-layers.md`.

Highest-value current gaps:

1. Runtime Projection / Doctrine Compiler.
2. Policy Envelope / Authority Intersection.
3. Delivered-Artifact Acceptance Packet.
4. Disabled-User Verdict Ledger.
5. Web Capability and Fallback Matrix.
6. Comprehension-Debt Handoff Packet.

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
- Perspective-Guided Command.
- Visual Truth Authority.

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
- Writing anonymous implementation prompts with no responsibility owner.
- Treating telemetry or green CI as visual proof when the artifact is visibly red.
- Explaining instead of making the requested artifact.
- Creating agent names without responsibility boundaries.
- Treating written doctrine as inherited before the acting runtime loads it.
- Treating authentication as sufficient authorization.
- Accepting accessibility from automation without a disabled-user task verdict.
- Assuming browser capabilities instead of probing and preserving fallback truth.

## Next Work

1. Compile the Quartermaster pack into a versioned runtime manifest and cold-agent test.
2. Draft Authority Intersection with negative tests for actor, project, tool, and mutation scope.
3. Define the Delivered-Artifact Acceptance Packet across repo, runtime, visual, accessibility, and human truth.
4. Add the Accessibility Doctrine Pack and first Disabled-User Verdict Ledger entry.
5. Add a privacy-aware web capability matrix and fallback-routing procedure.

## Acceptance Criteria

This manifest is working when a future agent can read it and know:

- what exists,
- what is missing,
- which doctrine governs behavior,
- which agent owns the next action,
- what glue layer is missing before another agent is invented.
