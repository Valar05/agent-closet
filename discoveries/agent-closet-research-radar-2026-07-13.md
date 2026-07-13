# Agent Closet Research Radar — 2026-07-13

Type: Operational research brief / promotion intake
Status: Silver — evidence-backed candidates awaiting Crucible disposition
Owner: Prospector
Verification owner: Quartermaster

## Repository truth reviewed

- `README.md`
- `MANIFEST.md`
- `shared/index/repository-map.md`
- `shared/index/doctrine-index.md`
- `shared/index/agent-index.md`
- `shared/index/skill-index.md`
- `scratch/ore-worth-promoting.md`
- `glue/missing-glue-layers.md`

## Executive finding

Agent Closet already has the correct core model: versioned judgment, promotion from ore to doctrine, role-specific responsibility, and repository truth over chat. The external ecosystem is now converging on the same primitives—agent skills, custom instructions, MCP tools, approval gates, session persistence, hooks, browser-native runtime evaluation, and local AI—but with weak continuity, incomplete security boundaries, and shallow delivered-artifact verification.

The opportunity is not to invent more agents. It is to compile the Closet into enforceable runtime contracts and evidence loops.

## Notable ecosystem developments

### AI tooling and agent architecture

- OpenAI's Agents SDK now supports hosted and local MCP transports, per-tool approval policies, static and dynamic tool filtering, tenant metadata injection, caching, tracing, and MCP prompts. This makes doctrine-to-runtime compilation practical rather than conceptual.
  - https://openai.github.io/openai-agents-python/mcp/
- The MCP specification explicitly states that the protocol cannot enforce its own security principles. Implementers must provide consent, authorization, access controls, data protection, and clear review surfaces.
  - https://modelcontextprotocol.io/specification/2025-11-25
- GitHub Copilot cloud agent now exposes custom instructions, custom agents, hooks, skills, MCP configuration, and persistent cloud sessions, but each task is still constrained to one repository, one branch, one pull request, and a maximum 59-minute session. Cross-repository continuity remains an unsolved layer above the agent.
  - https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent

### Browser AI

- Chrome's Prompt API supports streaming, session cloning, context-overflow events, and local execution, but foundation-model APIs remain desktop-only, require substantial free storage, and are unavailable on Android and iOS. Capability detection and fallback routing are mandatory.
  - https://developer.chrome.com/docs/ai/prompt-api
- Browser-local model research continues to improve memory efficiency and portability, but device variability remains a first-class systems constraint.
  - https://arxiv.org/abs/2605.20706

### Accessibility

- A 2026 systematic review of LLM-assisted web accessibility found that most work remains text-centric, evaluation methods vary widely, cognitive accessibility receives limited attention, and disabled users are rarely directly involved in evaluation.
  - https://arxiv.org/abs/2605.13873
- Accessibility automation therefore remains support evidence, not human acceptance. This strongly reinforces `shared/accessibility-first.md`, `shared/doctrine/visual-truth-authority.md`, and the pending Accessibility Doctrine Pack.

### Three.js, WebGPU, Unity, and browser games

- Three.js r185 shipped on 2026-07-01 with continued WebGPU/TSL expansion, renderer fixes, deprecations, WebXR support, shader diagnostics, and backend churn. WebGPU is useful but still a moving compatibility surface.
  - https://github.com/mrdoob/three.js/releases/tag/r185
- WebGameBench found that the best coding-agent configuration produced browser games judged usable 76.9% of the time, but excellent only 20.2% of the time. Source changes and green tests remain weak proxies for delivered experience.
  - https://arxiv.org/abs/2605.17637
- WebGPU research has also identified privacy-relevant cross-context signals, especially pipeline compilation state, so browser capability probes should collect only what is needed and document privacy implications.
  - https://arxiv.org/abs/2606.26412

### Indie business and community pain

- AI-assisted indie teams are accumulating "comprehension debt": systems function, but the team cannot independently explain or maintain them. This is a direct business opening for evidence-backed handoff, generated orientation, and repository archaeology products.
  - https://arxiv.org/abs/2512.08942
- Indie pre-release experimentation remains constrained by scarce participants, limited time, biased feedback, and weak access to representative users. A cheap browser-native evidence harness can lower this burden.
  - https://arxiv.org/abs/2411.17183

## Highest-value promotion candidates

### 1. Doctrine-to-Runtime Compiler

Status: Strong gold candidate
Recommended owner: Compiler
Verification: Quartermaster

Core claim:

> Doctrine is not inherited until it can be projected into the runtime surface that will act on it.

Compile Agent Closet packs into a versioned machine-readable manifest containing:

- source repository and commit
- source file paths and hashes
- responsibility boundary
- required inputs
- output contract
- tool allowlist
- approval policy
- evidence requirements
- failure modes
- affected tests and agents

Why now:

OpenAI Agents, GitHub Copilot, MCP servers, hooks, skills, and custom agents all expose compatible runtime attachment points. Agent Closet already names the missing Update Pipeline, Handoff Generator, Agent Profile Cards, and doctrine registry. The missing piece is compilation.

Promotes or strengthens:

- `scratch/ore-worth-promoting.md` → Judgment Packs / Portable Judgment Repository
- `glue/missing-glue-layers.md` → Update Pipeline / Handoff Generator / Agent Profile Cards
- `shared/doctrine/encoded-judgment-doctrine.md`
- `shared/doctrine/agent-closet-persistence-protocol.md`

Smallest experiment:

Compile the Quartermaster pack into `generated/quartermaster.runtime.json`, then verify that a cold agent can identify its responsibility, tool limits, evidence gate, and output contract without reading chat history.

### 2. Authority Intersection

Status: Strong gold candidate
Recommended owner: Auditor
Implementation partner: Compiler

Core claim:

> A tool operation is authorized only where caller identity, delegated provider authority, tool policy, project scope, and mutation approval overlap.

Why now:

MCP standardizes tool access but explicitly leaves enforcement to implementers. Current SDKs provide approvals, tool filtering, metadata propagation, and tracing, but those primitives need one policy envelope and hostile tests.

Promotes or strengthens:

- `glue/missing-glue-layers.md` → Evidence Schema / Workflow Defect Detector / WWDD API Contract
- `scratch/ore-worth-promoting.md` → Cloud-Hosted WWDD Service / Prompt Injection Through Procedure
- new doctrine candidate: `shared/doctrine/authority-intersection.md`

Smallest experiment:

Create one policy-envelope schema and prove four negative cases: wrong actor, wrong project, disallowed tool, and missing mutation approval. The tool must reject before provider execution and emit actor-scoped audit evidence.

### 3. Delivered-Artifact Acceptance Harness

Status: Strong gold candidate
Recommended owner: Auditor
Implementation partner: Foreman

Core claim:

> Agent work is accepted at the delivered artifact, not at the patch, transcript, telemetry, or test suite.

Required truth lanes:

1. repository truth
2. runtime behavior
3. visual evidence
4. accessibility evidence
5. human verdict

Why now:

WebGameBench's large usable-to-excellent gap validates the existing Visual Truth Authority and the Perspective Coding truth-ledger candidate. Browser games are a compact proving ground because input, state, rendering, restart, accessibility, and visible consequence can all be tested cheaply.

Promotes or strengthens:

- `shared/doctrine/visual-truth-authority.md`
- `scratch/ore-worth-promoting.md` → Perspective Coding Doctrine / Sense Simulation
- `glue/missing-glue-layers.md` → Evidence Schema / Workflow Defect Detector / Artifact Index

Smallest experiment:

Define `acceptance-packet.json` for one Three.js or Unity Web build with:

- build provenance
- browser/device matrix
- scripted interaction trace
- screenshots or video
- accessibility tree and keyboard path
- human verdict
- explicit unresolved red lanes

### 4. Disabled-User Authority Loop

Status: Strong gold candidate
Recommended owner: Holocron
Verification partner: Auditor

Core claim:

> Accessibility automation may find defects; disabled-user task completion decides whether the experience works.

Why now:

Current LLM accessibility research rarely includes disabled users directly and undercovers cognitive accessibility. Browser AI is also unevenly available across devices, so an AI feature can be technically impressive while excluding the person it is intended to help.

Promotes or strengthens:

- `scratch/ore-worth-promoting.md` → Accessibility as First-Class Constraint
- `glue/missing-glue-layers.md` → Accessibility Doctrine Pack
- `shared/accessibility-first.md`
- `agents/holocron/`

Smallest experiment:

Create one June-first acceptance card for a live web tool:

- intended task
- screen-reader path
- voice/keyboard path
- semantic status announcements
- recovery from error
- task completion verdict from June
- developer-observed defects kept separate from June's verdict

### 5. Capability-Aware Web Runtime Broker

Status: Silver-to-gold candidate
Recommended owner: Cartographer
Implementation partner: Foreman

Core claim:

> Browser features are routes, not assumptions. Probe capabilities, preserve the result, and select the least expensive viable backend.

Why now:

Three.js WebGPU/TSL is advancing quickly but continues to change. Chrome built-in AI excludes mobile foundation-model use and requires substantial storage. Unity and browser-native engines increasingly target web delivery, while device capability and privacy remain uneven.

The broker should route among:

- WebGPU
- WebGL fallback
- browser-local AI
- remote AI
- static/non-AI fallback
- unsupported with an honest explanation

Promotes or strengthens:

- `glue/missing-glue-layers.md` → Task Router / Artifact Index
- `shared/reality-negotiation.md`
- `shared/doctrine/visual-truth-authority.md`
- new procedure candidate: `procedures/web-capability-routing.md`

Smallest experiment:

Build a read-only capability probe page that emits a versioned JSON report without fingerprinting beyond operational need. Test it on one desktop Chrome, one Android browser, and one low-power fallback device, then route a small Three.js scene and a text-assistance feature accordingly.

## Missing glue updates indicated by this research

Add or refine these glue layers:

- Runtime Projection / Doctrine Compiler
- Policy Envelope and Authority Intersection
- Delivered-Artifact Acceptance Packet
- Disabled-User Verdict Ledger
- Web Capability and Fallback Matrix
- Comprehension-Debt Handoff Packet

## Promising indie experiments

1. **Portable Judgment Kit** — a small open-source template plus paid setup service that turns team docs into versioned agent packs, runtime manifests, and acceptance tests.
2. **Browser Acceptance Clerk** — CI service for agent-built web apps and games combining scripted runtime checks, screenshots, accessibility evidence, and human review packets.
3. **Accessibility Review Packet Generator** — produces a screen-reader task script, semantic evidence, and user-verdict ledger without pretending automated WCAG checks equal usability.
4. **AI Comprehension Debt Scanner** — detects generated systems with missing orientation, unowned dependencies, absent decision records, and unverifiable build steps.
5. **Web Runtime Capability Broker** — drop-in library for WebGPU/WebGL/local-AI/cloud fallback with privacy-aware capability reports.

## Community pain worth preserving

- Agents can act faster than teams can understand or maintain the resulting system.
- Single-repository cloud agents do not provide cross-repository continuity.
- Protocol interoperability is arriving faster than authorization and audit discipline.
- Automated accessibility work often excludes disabled people from evaluation.
- Browser-native artifacts can be technically runnable yet visibly mediocre or inaccessible.
- WebGPU and local browser AI are powerful but heterogeneous, storage-heavy, and not mobile-universal.
- Indie teams lack cheap representative playtesting and trustworthy delivered-artifact evaluation.

## Top-five execution order

1. Compiler — compile Quartermaster into a runtime manifest.
2. Auditor — define Authority Intersection policy envelope and negative tests.
3. Auditor — define the delivered-artifact acceptance packet.
4. Holocron — create the first disabled-user authority card.
5. Cartographer — create the web capability matrix and routing procedure.

## Crucible gate

Do not promote these directly from this brief. Each candidate must receive:

- one repository-backed incident or experiment
- one counterexample or falsification attempt
- explicit overlap check against existing doctrine
- named implementation and verification owners
- retrieval path from the appropriate index
- readback proving the promoted artifact changes behavior
