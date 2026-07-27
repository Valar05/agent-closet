# Agent Closet Research Radar — 2026-07-27

Type: Operational research brief / promotion intake  
Status: Silver — evidence-backed candidates awaiting Crucible disposition  
Owner: Prospector  
Verification owner: Quartermaster  
Independent claim verification: Auditor

## Repository truth reviewed

- `README.md`
- `MANIFEST.md`
- `shared/index/repository-map.md`
- `shared/index/doctrine-index.md`
- `shared/index/agent-index.md`
- `shared/index/skill-index.md`
- `scratch/ore-worth-promoting.md`
- `glue/missing-glue-layers.md`
- `reports/agent-closet-integrity-2026-07-21.md`
- open promotion PRs #2, #3, #4, and #5

## Repository delta

Agent Closet has not absorbed a new mainline promotion since the July 21 integrity and repository-map repairs. The doctrine, agent, and skill indexes still carry June 24 review dates. The manifest and glue registry still point to the July 13 research radar. Four doctrine PRs remain open without a recorded Crucible disposition.

The current architecture is not short of ideas. It is short of compilation, conflict reporting, disposition, and executed proof.

## Executive finding

External agent platforms are converging on discoverable resource catalogs, stateless protocols, suggestion-and-approval workflows, conformance suites, browser capability routing, and local assistive AI. Agent Closet already names most of the corresponding doctrine and glue.

The decisive new requirement is this:

> Portable judgment cannot depend on a session, and discoverability cannot silently become authority.

Agent Closet should compile its current repository truth into a read-only resource catalog plus an explicit execution-context receipt. The compiler must report contradictory authority instead of choosing whichever file it read last.

## Notable ecosystem developments

### 1. MCP is moving to a stateless core

GitHub announced on July 23 that the MCP protocol's new stateless core arrives July 28, 2026. Sessions and `initialize` are removed, each round trip can stand alone, and official conformance tests are now available.

Source:
- https://github.blog/changelog/2026-07-23-github-mcp-server-supports-the-next-mcp-specification/

Agent Closet implication:

Artificial Continuity must be explicit state, not transport-session memory. Runtime projection needs to preserve:

- actor identity;
- delegated authority;
- exact resource catalog revision;
- request and input identity;
- idempotency key;
- checkpoint or continuation pointer;
- required evidence and terminal disposition.

Promotion candidates:

- **Continuity Is Explicit State, Not Session Memory**
- **Every Stateless Action Carries Its Authority and Evidence Context**
- **Protocol Conformance Is a Testable Product Surface**

Missing glue:

- **Stateless Execution Context Receipt**
- **MCP Conformance Fixture**

Recommended owner: Compiler  
Verification owner: Auditor

### 2. Agent suggestions now expose rationale and confidence, but not a security boundary

GitHub Issues added agent suggestions, confidence levels, rationale, and optional approval. GitHub explicitly states that approval is workflow convenience rather than server-side security; an already-authorized agent can still apply changes directly.

Source:
- https://github.blog/changelog/2026-07-23-agent-automation-controls-in-github-issues-in-public-preview/

Agent Closet implication:

This directly validates the existing distinction between authentication, approval UX, and actual authorization. Confidence may decide review priority; it must never create permission.

Promotion candidates:

- **Confidence Is Triage, Not Authority**
- **Suggestion, Approval, and Mutation Are Separate States**
- **Rationale Is Audit Evidence, Not Permission**

Missing glue:

- **Suggestion-to-Mutation Receipt**
- **Authority Intersection Enforcement Fixture**

Recommended owner: Auditor  
Implementation partner: Compiler

### 3. Agent resource discovery is becoming infrastructure

GitHub Agent Finder now implements the open Agentic Resource Discovery specification. It searches an allowed registry of MCP servers, skills, agents, canvases, and tools, ranks matches, and deliberately does not install them automatically.

Source:
- https://github.blog/changelog/2026-06-17-agent-finder-for-github-copilot-now-available/

Agent Closet implication:

The repository is already shaped like a resource registry, but humans still perform the compilation step. The current split among manifest, agent index, skill index, doctrine index, registry, and scratch also means a catalog generator must emit conflicts rather than laundering them into runtime truth.

Promotion candidates:

- **Discovery Is Not Installation**
- **Installation Is Not Authorization**
- **One Resource Identity Requires One Authority Record**

Missing glue:

- **ARD-Compatible Catalog Projection**
- **Resource Conflict and Supersession Report**

Recommended owner: Compiler  
Authority owner: Quartermaster  
Verification owner: Auditor

### 4. Browser AI is becoming a routed capability, not one local feature

Chrome's built-in AI APIs require runtime availability checks and substantial desktop resources; mobile foundation-model support remains unavailable. Chrome also provides task-API polyfills that can route to alternate backends, while WebMCP is being prototyped as a structured page-tool surface for agents.

Sources:
- https://developer.chrome.com/docs/ai/get-started
- https://developer.chrome.com/docs/ai/task-api-polyfill
- https://developer.chrome.com/docs/ai

Agent Closet implication:

The existing Web Capability and Fallback Matrix should distinguish:

- native local model;
- downloadable or downloading model;
- polyfilled local model;
- remote model;
- non-AI fallback;
- unavailable with an honest explanation;
- structured page tools and their authority boundary.

Promotion candidates:

- **Capability Must Be Proven Before Affordance**
- **Fallback Is Product Behavior, Not Error Cleanup**
- **Page-Exposed Agent Tools Need the Same Authority Envelope as Remote MCP Tools**

Missing glue:

- **Browser AI Backend Receipt**
- **WebMCP Tool Authority Manifest**

Recommended owner: Cartographer  
Implementation owner: Foreman  
Verification owner: Auditor

### 5. Android assistive AI now needs model-state and finality contracts

ML Kit's GenAI Speech Recognition API is alpha. Streaming partial transcripts may change before the final transcript, model readiness varies by device, and advanced recognition has narrower hardware support. The Image Description API is beta, produces short generated descriptions, and also requires model-status handling.

Sources:
- https://developers.google.com/ml-kit/genai/speech-recognition/android
- https://developers.google.com/ml-kit/genai/image-description/android

Research on assistive agents also warns that ordinary agent behavior often assumes sighted interaction, trial-and-error recovery, and easy verification that blind users may not have.

Source:
- https://arxiv.org/abs/2605.13579

Agent Closet implication:

June-first design needs four separate authorities:

1. literal observation or OCR;
2. generated interpretation;
3. model and device capability state;
4. disabled-user task verdict.

Promotion candidates:

- **Final Transcript Is Authority**
- **Literal Before Inferred**
- **Model Availability and Version Are Evidence**
- **Assistive Agents Need Accessibility Alignment**

Missing glue:

- **Assistive Model Capability Receipt**
- **Interruptible Task Contract**
- **Disabled-User Task Replay Packet**

Recommended owner: Holocron  
Implementation owner: Foreman  
Verification owner: Auditor

### 6. Engines expose better accessibility APIs while web complexity regresses

Unity 6.3 adds broader native screen-reader roles, containers, controls, scrolling support, and accessibility overrides. Three.js's migration guide already documents 184-to-185 renderer and WebGPU changes even while r184 remains the latest tagged release. The 2026 WebAIM Million found 56.1 detectable errors per homepage, up 10.1 percent in a year, and linked growing complexity and ARIA usage with more detected errors.

Sources:
- https://unity.com/releases/editor/whats-new/6000.3.0f1
- https://github.com/mrdoob/three.js/wiki/Migration-Guide
- https://webaim.org/projects/million/

Agent Closet implication:

Engine capability is not an accessible experience, and version movement can invalidate evidence without changing product intent.

Promotion candidates:

- **Engine Capability Is Not User Completion**
- **Version Upgrade Requires a Migration Receipt**
- **Simpler Systems Are an Accessibility Strategy**

Missing glue:

- **Cross-Engine Accessibility Fixture**
- **Renderer and Engine Migration Receipt**

Recommended owner: Foreman  
Accessibility authority: Holocron  
Verification owner: Auditor

### 7. Community pain still points toward verification and continuity products

The 2025 Stack Overflow survey found that 46 percent of developers distrust AI output accuracy compared with 33 percent who trust it; only 17 percent of agent users said agents improved team collaboration. GDC's 2026 survey found widespread layoffs, strong concern among students, and majority-negative sentiment about generative AI's effect on games. Patreon reports that 78 percent of creators say burnout affects motivation, 75 percent feel platforms punish inconsistent posting, and 81 percent want more direct connection with fans.

Sources:
- https://survey.stackoverflow.co/2025/ai
- https://gdconf.com/article/gdc-2026-state-of-the-game-industry-reveals-impact-of-layoffs-generative-ai-and-more/
- https://news.patreon.com/articles/Strengthening-transparency-mental-health-support-and-community-guidelines-in-2025

Agent Closet implication:

The strongest commercial wedge remains proof and continuity:

- developers need trustworthy acceptance and maintainable handoff;
- indie teams need a bounded finishing department;
- disabled users need task completion rather than demo intelligence;
- creators need direct-audience and obligation continuity.

## Top five opportunities

### 1. ARD Catalog plus Stateless Context Receipt

Priority: 1  
Owner: Compiler  
Verification: Auditor

Build a generated, read-only catalog from current canonical repository truth. Every resource should include:

- unique resource ID and type;
- responsibility;
- canonical source path and blob hash;
- promotion status;
- implementation and verification owners;
- runtime availability;
- required authority;
- supersession or conflict state.

Pair every invocation with a stateless context receipt containing actor, authority, exact catalog revision, request identity, idempotency, and evidence contract.

Smallest experiment:

Compile the current repository and run five cold queries. The compiler must fail or report a conflict for Sommelier, Wallfly, Cartographer, Crucible, Archivist, and Compiler status disagreements instead of silently choosing a source.

### 2. Authority Intersection plus Suggestion Receipt

Priority: 2  
Owner: Auditor  
Implementation partner: Compiler

Define one machine policy that separates:

- proposed change;
- confidence and rationale;
- human approval;
- caller authorization;
- provider authority;
- completed mutation.

Smallest experiment:

Prove rejection for wrong actor, wrong project, missing mutation approval, and an agent attempting to bypass suggestion mode with direct write authority.

### 3. June-First Assistive Task Contract

Priority: 3  
Owner: Holocron  
Implementation partner: Foreman  
Verification: Auditor

Smallest experiment:

Build one `Read This` task flow that preserves literal OCR, optional labeled interpretation, final-transcript-only actions, model readiness, stop/repeat/resume, uncertainty, and a disabled-user verdict separate from automation.

### 4. Cross-Engine Delivered-Artifact Fixture

Priority: 4  
Owner: Foreman  
Accessibility authority: Holocron  
Verification: Auditor

Smallest experiment:

Run one Unity 6.3 sample and one Three.js sample through the same:

- keyboard and controller task;
- screen-reader route;
- mobile viewport;
- runtime capture;
- version manifest;
- human verdict packet.

The fixture should prove that engine APIs exist and separately whether a person can complete the task.

### 5. Acceptance Clerk / Indie Finishing Bench

Priority: 5  
Owner: Prospector  
Product implementation: Foreman  
Verification contract: Auditor

Smallest experiment:

Accept one deployed browser game and return a tamper-evident packet covering repository identity, exact build, first-minute comprehension, task completion, screenshots, accessibility, performance, unresolved red lanes, and a human release verdict.

This is the strongest business wedge because it packages existing Agent Closet doctrine into a service that small teams cannot cheaply assemble themselves.

## Doctrine gaps exposed

- Continuity Is Explicit State, Not Session Memory.
- Discovery Is Not Installation; Installation Is Not Authorization.
- Confidence Is Triage, Not Authority.
- Suggestion, Approval, Authorization, and Mutation Are Separate States.
- Model Availability and Version Are Evidence.
- Engine Capability Is Not User Completion.
- Version Upgrade Requires a Migration Receipt.
- AI Activity Metrics Are Not Delivery Evidence.

## Missing glue additions indicated

- ARD-Compatible Catalog Projection.
- Stateless Execution Context Receipt.
- Resource Conflict and Supersession Report.
- Suggestion-to-Mutation Receipt.
- Browser AI Backend Receipt.
- WebMCP Tool Authority Manifest.
- Assistive Model Capability Receipt.
- Cross-Engine Accessibility Fixture.
- Renderer and Engine Migration Receipt.

These should be mapped into existing glue families before creating new top-level systems. Runtime projection, authority intersection, delivered-artifact acceptance, disabled-user verdicts, capability fallback, and comprehension-debt handoff remain the parent layers.

## Repository repairs exposed by this scan

### Authority reconciliation

The manifest treats Sommelier as a candidate and omits Wallfly, while the agent index treats both as current packs. Cartographer, Crucible, Archivist, and Compiler carry active responsibilities while remaining classified only as candidate concepts.

Repair owner: Quartermaster  
Verification owner: Auditor

Required status vocabulary:

- active responsibility;
- complete pack;
- candidate concept;
- diagnostic hazard;
- obsolete.

### Index freshness and role separation

The doctrine, agent, and skill indexes still show June 24 dates. The doctrine index and doctrine registry still need explicit separation:

- index: retrieval and canonical path;
- registry: status, provenance, owners, evidence, and supersession.

Repair owner: Quartermaster  
Schema owner: Compiler  
Verification owner: Auditor

### Ore disposition

The ore queue still contains Agent Closet as likely gold, Artificial Continuity as promoted, Accessibility First as needing a doctrine that already exists, and other promoted material beside legitimate experiments.

Disposition owner: Crucible  
Index owner: Quartermaster

Split the queue into:

- promotion candidates;
- proof debt;
- disposition required;
- domain experiments.

### Open promotion branches

PRs #2 through #5 remain open. No new research candidate should be added as a separate doctrine PR before Scene Compiler, Context Firewall, World Simulation / Humane Guardrail, and Operational Memes receive explicit dispositions.

Disposition owner: Crucible  
Branch owner: Foreman  
Verification owner: Auditor

## Discoveries worth preserving

1. Agent Closet anticipated resource discovery before external catalogs became ordinary platform infrastructure.
2. Artificial Continuity becomes more valuable, not less, when the transport becomes stateless.
3. Prompt Injection Through Procedure now extends naturally to branch instructions, page-exposed tools, resource catalogs, and automation rationale.
4. Approval UX is not an authorization boundary.
5. Accessibility authority requires literal perception, generated interpretation, model capability, and disabled-user judgment to remain separate.
6. Engine accessibility APIs and AI activity dashboards increase the need for delivered-artifact evidence; they do not replace it.
7. Small teams are not short of generators. They are short of finishing, comprehension, and trustworthy receipts.

## Next smallest useful action

### Compile a conflict-reporting ARD catalog from current `main`

Compiler:

1. Read only the current canonical bootstrap and indexes.
2. Emit a generated read-only catalog with source paths and blob hashes.
3. Exclude scratch, candidates, legacy roots, and open-PR behavior from executable availability.
4. Emit explicit conflicts instead of choosing authority silently.
5. Add a stateless context-receipt schema beside the catalog.
6. Run cold discovery queries for preservation, verification, accessibility, Prompt Hydraulics, and a candidate-only capability.

Auditor:

- reject discovery interpreted as installation or authorization;
- reject candidate ore exposed as executable;
- reject any resource without traceable current source identity;
- require Sommelier, Wallfly, and active-candidate responsibility conflicts to appear in the report;
- run the official MCP conformance suite against any resulting MCP projection.

This is smaller than a repository-wide doctrine cleanup and forces the cleanup target to become measurable. The compiler should bring back a map of the contradictions instead of politely eating them.
