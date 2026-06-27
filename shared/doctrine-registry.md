# Doctrine Registry

This registry tracks promoted doctrine and the evidence that earned it storage.

## Entry Format

- `Name`
- `Status`
- `Confidence`
- `Evidence Files`
- `Supporting Doctrines`
- `Supporting Agents`
- `Counterexamples`
- `Why It Matters`

## Current Entries

### Evidence-Pressure Loop

- `Status`: promoted
- `Confidence`: high
- `Evidence Files`: `shared/crucible-protocol.md`, `shared/wwdd-protocol.md`, `scratch/wwdd-proof.md`
- `Supporting Doctrines`: `Evidence beats activity`, `WWDD`, `Crucible Protocol`
- `Supporting Agents`: `Foreman`, `Quartermaster`, `Prospector`
- `Counterexamples`: chat-only claims, untested doctrine
- `Why It Matters`: keeps claims tied to files, logs, and visible output change

### Continuity Without Memory Theater

- `Status`: promoted
- `Confidence`: high
- `Evidence Files`: `shared/artificial-continuity.md`, `shared/recursive-sense-synthesis.md`, `agents/holocron/identity.md`
- `Supporting Doctrines`: `Save -> Read -> Verify`, `Artificial Continuity`, `Recursive Sense Synthesis`
- `Supporting Agents`: `Holocron`, `Quartermaster`
- `Counterexamples`: raw memory reliance, unstated assumptions
- `Why It Matters`: preserves useful shape across sessions without pretending recall is truth

### Extract-Compact-Promote

- `Status`: promoted
- `Confidence`: high
- `Evidence Files`: `agents/prospector/doctrine.md`, `agents/quartermaster/doctrine.md`, `scratch/dump-ground.md`
- `Supporting Doctrines`: `Dump and Drop`, `Repeated decisions become doctrine`, `If it appears three times, capture it`
- `Supporting Agents`: `Prospector`, `Quartermaster`
- `Counterexamples`: one-off drama, giant explanations
- `Why It Matters`: turns messy intake into reusable doctrine

### Delivery-Handoff Loop

- `Status`: promoted
- `Confidence`: high
- `Evidence Files`: `agents/foreman/operating-loop.md`, `agents/foreman/doctrine.md`, `README.md`
- `Supporting Doctrines`: `Do It protocol`, `Manifesto comes later. Merge request comes first.`
- `Supporting Agents`: `Foreman`
- `Counterexamples`: sprawling plans, explanation without action
- `Why It Matters`: keeps action small, verifiable, and shippable


### Home Center Doctrine

- `Status`: promoted silver
- `Confidence`: medium-high
- `Evidence Files`: `/storage/emulated/0/Documents/GodotProjects/home-center/README.md`, `/storage/emulated/0/Documents/GodotProjects/home-center/docs/AGENT_CONTRACT.md`, `/storage/emulated/0/Documents/GodotProjects/home-center/docs/DATA_MODEL.md`, `/storage/emulated/0/Documents/GodotProjects/home-center/docs/netrunner/learning-model.md`, `/storage/emulated/0/Documents/GodotProjects/home-center/app/src/main/java/com/dclar/homecenter/ToolRegistry.java`, `/storage/emulated/0/Documents/GodotProjects/home-center/tools/home_center_regression_tests.py`, `shared/doctrine/home-center-doctrine.md`
- `Supporting Doctrines`: `Evidence beats activity`, `Save -> Read -> Verify`, `Human Offloading Doctrine`, `Infrastructure Doctrine`, `Accessibility First`
- `Supporting Agents`: `Foreman`, `Quartermaster`, `Auditor`, `Holocron`
- `Counterexamples`: personality cloning, chat-only memory, fake provider access, dashboard-only state, unconfirmed risky writes
- `Why It Matters`: generalizes Home Center beyond one user's preferences into a portable life-operations pattern for organization, research, memory, writing, and reusable skills

## Registry Notes

- The registry is a promotion ledger, not a scrapbook.
- A rule stays promoted only while evidence and retrieval paths remain easy to verify.
- Keep the strongest canonical file and fold weaker duplicates into it.

## Imported Governance Line

The repo also carries a broader living-inheritance framing from the governance-glue line:

- Agent Closet stores portable doctrine and agent profiles.
- Shared pages should make it obvious what exists, what is missing, and what doctrine governs behavior.
- Scratch is staging, not storage.
- Promotion should require repeated, useful, compressible, transferable, inheritable, behavior-changing evidence.

## Pending Review

- `Feed Is The Battlefield`
- `Dashboard Failure`
- `Capability Distillation`
- `Agent Closet Origin`
- `TFTM Discovery Chain`

These remain in review until they have stronger evidence or are merged into a canonical page.
