# Discovery Promotion Record — 2026-06-26 — Scene Compiler Runtime + AI Substrate

Status: promoted runtime/interface layer; Drive judgment guide routed; content claims still evidence-gated
Owning clusters: Writing Systems, AI Orchestration, Project Archaeology
Source-of-truth: Agent Closet repo for runtime, tests, and glue contracts; Drive Field Guide for Drew narrative judgment substrate; Thunder Brainstorm for reusable source-reference mirrors only

## Reviewed Artifacts

Canonical GitHub evidence:

- `skills/scene-compiler-runtime.md`
- `skills/scene-compiler-tests.md`
- `skills/scene-compiler.md`
- `skills/world-pressure-engine.md`
- `glue/ai-substrate-contract.md`
- `glue/README.md`
- `scratch/scene-compiler-runtime-dogfood.md`

GitHub commits:

- `9e9869fef37346d52a887008fecb61d22b654dd7` — Foreman: add Scene Compiler runtime
- `0acf2138b31fb7716b72ecc85af2cc3505ac29c0` — Foreman: dogfood Scene Compiler runtime
- `18010e529f1e3741f54dbf923d4ee71843324aec` — Foreman: add doctrine combination policy
- `fcc4ae829ce883f2435262b83460710bda1cdd9d` — Foreman: add AI substrate contract

Drive evidence:

- `Field Guide - Simulating Drew's Narrative Judgment`
- `Skill Cluster - Writing Systems`
- `Skill Cluster - AI Orchestration`
- `Skill Cluster - Project Archaeology`
- `Drive Knowledge Index - Daily Delta`

Thunder mirror patch:

- `generated/source_refs_github/2026-06-26_scene_compiler_runtime_source_refs.jsonl`

## Promotions

### 1. Scene Compiler Runtime Loop

Observation:
The Scene Compiler is no longer only a prompt/skill. It now has a runtime loop that starts from explicit story state, selects pressure, selects doctrine, generates a candidate scene, validates it, repairs failures, and accepts only state-changing output.

Why it matters:
This blocks prose imitation and vibe-driven generation. Future agents can run the same loop instead of rewriting the same advice in new words.

Reusable rule:
Creative generation becomes reusable when it has explicit state, pressure selection, doctrine selection, validation, repair, acceptance, state delta, and next pressure.

Evidence:

- `skills/scene-compiler-runtime.md` defines world state, character state, pressure state, relationship state, doctrine selection, scene draft, compiler loop, repair order, and acceptance criteria.
- `skills/scene-compiler-tests.md` turns doctrines into pass/fail scene tests.
- Commit `9e9869fef37346d52a887008fecb61d22b654dd7` indexes and adds the runtime.

Confidence: High for structure; Medium until more live scenes run through the harness.

Owning cluster: Writing Systems / scene generation runtime; AI Orchestration / validated generation loops.

### 2. Drew Narrative Judgment As Substrate, Not Style

Observation:
The Drive Field Guide expresses the narrative judgment layer: restore agency, repair before destruction, competence as ethical obligation, power as interface, maintenance as meaningful action, logistics/recovery as narrative events, and action as multi-layer state change.

Why it matters:
This preserves decision architecture without asking agents to imitate surface voice.

Reusable rule:
When simulating a creator's writing judgment, model repeated choices and state-selection heuristics. Do not model only tone, trope preference, or prose texture.

Evidence:

- `Field Guide - Simulating Drew's Narrative Judgment` states the prime directive: do not ask what would be cool; ask what system is breaking.
- The same guide lists core judgment rules and the success test: the reader should understand why it happened while still being surprised.
- The Scene Compiler runtime operationalizes this by converting state and pressure into testable scene output.

Confidence: High for source fidelity; Medium for automation until encoded examples expand.

Owning cluster: Writing Systems / author judgment simulation; AI Orchestration / judgment substrate.

### 3. Doctrine Combination Anti-Soup Policy

Observation:
The runtime now has a policy for when a second doctrine is allowed: it must add a distinct observable requirement that the primary doctrine cannot force by itself.

Why it matters:
Without this, agents will stack doctrines because they sound good, creating doctrine soup and untestable scenes.

Reusable rule:
Default to one doctrine. Use two only when each controls a separable visible behavior. Three is exceptional and must have three independently testable layers.

Evidence:

- Commit `18010e529f1e3741f54dbf923d4ee71843324aec` adds the Doctrine Combination Policy to `skills/scene-compiler-runtime.md`.

Confidence: High.

Owning cluster: AI Orchestration / selection policy; Writing Systems / scene harness discipline; Project Archaeology / anti-duplication governance.

### 4. AI Substrate Contract / Branch Trace Layer

Observation:
The AI Substrate Contract defines the agent as transformation substrate and repository docs as the decision layer. It adds machine-readable input/output state, branch protocol, rejected-branch preservation, trace records, and acceptance criteria.

Why it matters:
This makes fiction simulation resumable, auditable, branchable, and eventually executable. It also prevents documentation from pretending to be runtime.

Reusable rule:
For complex agent workflows, create a glue contract that defines input state, output state, trace format, branch comparison, and acceptance criteria before building UI or prose polish.

Evidence:

- `glue/ai-substrate-contract.md` defines input state, output state, branch flow, trace record, and runtime behavior.
- Commit `fcc4ae829ce883f2435262b83460710bda1cdd9d` creates the glue directory and AI substrate contract.

Confidence: High for interface design; Medium for implementation until a machine runner consumes the contract.

Owning cluster: AI Orchestration / runtime contracts; Project Archaeology / glue layers; Writing Systems / simulation state transition.

### 5. Runtime Dogfood Specimen

Observation:
The dogfood pass proves the runtime can take a minimal damaged-shelter scenario, select physical/logistical pressure, apply `Make Repair the Dramatic Act`, validate the scene, emit state delta, next pressure, and remaining consequence debt.

Why it matters:
This is the first concrete acceptance specimen for the runtime. It should remain evidence, not become canon doctrine by itself.

Reusable rule:
The first dogfood pass should be promoted as a validation specimen only. Promote doctrine after repeated successful runs across different scene types.

Evidence:

- Commit `0acf2138b31fb7716b72ecc85af2cc3505ac29c0` adds `scratch/scene-compiler-runtime-dogfood.md` with runtime state, pressure selection, doctrine selection, scene draft, harness validation, state delta, next pressure, and remaining consequence debt.

Confidence: Medium-High for single-case validation; Low for broad generalization until more specimens exist.

Owning cluster: Writing Systems / test specimens; AI Orchestration / dogfooding; Project Archaeology / promotion evidence.

## Duplicate And Source-Of-Truth Decisions

- `Field Guide - Simulating Drew's Narrative Judgment` overlaps with `skills/scene-compiler.md`, but it is not the canonical runtime. Treat it as Drive-native author judgment substrate.
- `skills/scene-compiler.md` and `skills/scene-compiler-runtime.md` are not duplicates. The first defines the orchestration skill; the second runs the state/pressure/doctrine/test/repair loop.
- `glue/ai-substrate-contract.md` is not a new doctrine source. It is the interface contract that lets existing doctrine operate through a machine-readable substrate.
- `scratch/scene-compiler-runtime-dogfood.md` remains specimen evidence. Do not cite it as canonical doctrine.
- Thunder Brainstorm source refs remain mirror routing metadata. They must point back to Agent Closet and Drive evidence, not fork the runtime.

## Archive / Merge Guidance

Archive candidates:

- stale Drive mirrors of Scene Compiler text that do not link back to Agent Closet runtime files
- chat-only summaries of the runtime after this addendum and source refs are present

Hold:

- `Field Guide - Simulating Drew's Narrative Judgment` as a Drive-native active source until intentionally imported or mirrored into Agent Closet
- `scratch/scene-compiler-runtime-dogfood.md` as scratch/specimen until at least two more dogfood passes exist

Merge later:

- Promote a stable `scene-runtime-specimen-index.md` after three validated dogfood passes.
- Convert the AI Substrate Contract into executable schema/tests only after the current text contract survives at least one branch/what-if run.
- Consider importing the Drive Field Guide into Agent Closet as `corpus/fiction/judgment/field-guide-drew-narrative-judgment.md` if future agents repeatedly need it.

## Acceptance Criteria

This promotion is valid when future agents:

- choose `skills/scene-compiler-runtime.md` for execution, not the Drive Field Guide
- cite the Drive Field Guide for Drew-specific narrative judgment substrate
- use the doctrine combination policy to prevent doctrine soup
- preserve branch traces and rejected alternatives when simulating what-if scenes
- route Thunder mirror claims back to live GitHub and Drive source evidence
