# Missing Glue Layers

Type: Architecture debt registry
Status: Active
Date: 2026-07-13
Related doctrine: Reality Negotiation, Location-Aware Continuity, Human Offloading Doctrine

## Definition

A missing glue layer is the absent translation/interface layer between agents, artifacts, evidence, doctrine, and action.

When a workflow fails repeatedly, the answer is often not a better agent. It is a missing layer that lets the existing agents coordinate, inherit, verify, or act.

## Known Missing Glue

| Glue Layer | Purpose | Symptom When Missing | Candidate Owner |
|---|---|---|---|
| Agent Profile Cards | Define role, inputs, outputs, failure modes | Agent soup / personality drift | Agent Closet |
| Doctrine Registry | Locate active rules | Doctrine exists but cannot be found | Quartermaster |
| Promotion Log | Track ore into gold decisions | Discoveries get repeated instead of reused | Crucible / Quartermaster |
| Evidence Schema | Preserve source and confidence | Claims become detached from artifacts | Archivist |
| Task Router | Route requests to correct agent | One agent tries to do everything | Dispatcher |
| Handoff Generator | Produce continuation prompts | Sessions restart cold | Command Center |
| Workflow Defect Detector | Catch bad workflow patterns | Plans before observation, fake progress | Auditor |
| Update Pipeline | Apply doctrine changes across agents | Doctrine changes do not change behavior | Quartermaster Prime |
| WWDD API Contract | Query repeated behavior service | WWDD stays conceptual | WWDD / Compiler |
| Sense Synthesis Log | Store drink, food, and sensory experiments | Recipes do not become reusable rules | Sommelier |
| Accessibility Doctrine Pack | Preserve June-first design rules | Accessibility becomes afterthought | Holocron |
| Artifact Index | Map repo, docs, and tickets to doctrine | Evidence trails are hard to retrieve | Cartographer |
| Runtime Projection / Doctrine Compiler | Convert versioned doctrine into machine-readable agent manifests, prompts, tool policies, hooks, and tests | Written doctrine exists but the acting runtime never inherits it | Compiler |
| Policy Envelope / Authority Intersection | Intersect caller identity, delegated authority, project scope, tool policy, and mutation approval before execution | Authentication silently becomes excessive authorization | Auditor / Compiler |
| Delivered-Artifact Acceptance Packet | Join repository, runtime, visual, accessibility, and human evidence without collapsing their authority | Green patches and telemetry conceal a red delivered experience | Auditor |
| Disabled-User Verdict Ledger | Preserve task-level accessibility evidence and the disabled user's verdict separately from automated checks | Accessibility is claimed from linting without proving usable completion | Holocron / Auditor |
| Web Capability and Fallback Matrix | Record browser, device, WebGPU/WebGL, local-AI, storage, and fallback capability | Web features are assumed available and fail on real devices | Cartographer / Foreman |
| Comprehension-Debt Handoff Packet | Explain generated systems, decisions, dependencies, build steps, ownership, and recovery paths | AI-built systems function but the team cannot maintain them independently | Quartermaster / Compiler |

## Current Research Anchor

- `discoveries/agent-closet-research-radar-2026-07-13.md` records the external evidence and smallest experiments behind the six added glue layers.

## Rule

Before creating a new personality, check whether the missing piece is actually glue.

## Diagnostic Questions

1. What failed twice?
2. Did an agent lack role clarity?
3. Did doctrine lack a retrieval path?
4. Did an artifact lack an index?
5. Did a handoff lack state?
6. Did a decision lack evidence?
7. Did the system need routing, not reasoning?
8. Did written doctrine fail to reach the acting runtime?
9. Did authentication get mistaken for authorization?
10. Did a green implementation fail at the delivered artifact?
11. Was accessibility accepted without a disabled-user task verdict?
12. Was a browser capability assumed instead of probed?
13. Can the team explain and recover the AI-generated system without the generating agent?

## Acceptance Criteria

This registry is working when future agents can name the missing interface before inventing another role.

## Retrieval Keywords

missing glue layer, architecture debt, agent profile cards, doctrine registry, promotion log, evidence schema, task router, workflow defect detector, update pipeline, runtime projection, doctrine compiler, authority intersection, policy envelope, delivered artifact acceptance, disabled-user verdict, web capability matrix, fallback routing, comprehension debt, handoff packet
