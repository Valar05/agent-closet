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

### Perspective-Guided Command

- `Status`: canon
- `Confidence`: high
- `Evidence Files`: `shared/doctrine/perspective-guided-command.md`, `shared/perspective-routing.md`, `shared/skills/perspective-graphing.md`, `shared/agent-ecosystem.md`, `agents/command-center/identity.md`, `agents/quartermaster/doctrine.md`
- `Supporting Doctrines`: `Perspective Routing`, `Agent Ecosystem`, `Encoded Judgment Doctrine`, `Self-Insertion Calibration`, `Evidence beats activity`, `Save -> Read -> Verify`
- `Supporting Agents`: `Quartermaster`, `Command Center`, `Foreman`, `Prospector`, `Wallfly`, `Holocron`, `Auditor`
- `Counterexamples`: anonymous assistant voice, decorative roleplay, fixed-council rotation, personality masks without responsibility, verification claims without evidence
- `Why It Matters`: makes command prompts responsibility-bearing, keeps Quartermaster accountable for repository truth and synthesis, and routes other perspectives only when they improve judgment

### Visual Truth Authority

- `Status`: canon
- `Confidence`: high
- `Evidence Files`: `shared/doctrine/visual-truth-authority.md`, `scratch/perspective-coding-doctrine-notes.md`, `/storage/emulated/0/Documents/GodotProjects/pose-lab/docs/FIREBASE_VISUAL_TRUTH.md`, `/storage/emulated/0/Documents/GodotProjects/pose-lab/docs/POSE_LAB_EVIDENCE_PROTOCOL.md`
- `Supporting Doctrines`: `Perspective-Guided Command`, `Evidence beats activity`, `Reality Negotiation`, `Observe Before Advising / Read Before Report`
- `Supporting Agents`: `Quartermaster`, `Command Center`, `Gasket`, `Wallfly`, `Auditor`
- `Counterexamples`: telemetry-only success claims, green CI over visibly red screenshots, local artifact substitution for cloud visual truth, unreadable contact sheets treated as proof
- `Why It Matters`: prevents agents from claiming visual success without inspecting the actual visual evidence and turns human visual contradiction into a stop condition instead of another ignored signal

### Context Firewall Doctrine

- `Status`: canon
- `Confidence`: high
- `Evidence Files`: `shared/doctrine/context-firewall-doctrine.md`, `shared/doctrine/visual-truth-authority.md`, `/storage/emulated/0/Documents/GodotProjects/AGENTS.md`, `/storage/emulated/0/Documents/GodotProjects/.codex/skills/ai-mentorship/SKILL.md`, `/storage/emulated/0/Documents/GodotProjects/.codex/skills/visual-red-build-contract/SKILL.md`, `/storage/emulated/0/Documents/GodotProjects/.codex/skills/visual-qa-harness/SKILL.md`
- `Supporting Doctrines`: `Visual Truth Authority`, `Perspective-Guided Command`, `Evidence beats activity`, `Observe Before Advising / Read Before Report`
- `Supporting Agents`: `Quartermaster`, `Foreman`, `Auditor`, `Wallfly`
- `Counterexamples`: carrying Pose Lab FK/IK assumptions into a fresh tool, presenting proxy geometry as a real requested mesh, treating `Implement the plan` as overriding a newer `no`, using stale false-green tests as acceptance for a new surface
- `Why It Matters`: prevents a failed project from infecting the next project and forces agents to preserve the user's exact visible target before implementing, proving, or documenting around it


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
