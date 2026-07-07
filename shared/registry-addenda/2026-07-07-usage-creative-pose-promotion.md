# Discovery Promotion Record — 2026-07-07 — Usage Dashboard + Creative Finalizer + Pose Authoring

Status: promoted addendum.

This record captures the July 7 sweep over newly modified Home Center and Pose Lab V2 artifacts, with Drive writing-context evidence routed as source context rather than implementation truth.

## Reviewed artifacts

### Home Center

Canonical evidence:

- Compare: https://github.com/Valar05/home-center/compare/2c4cb4c93600a56335dd5d08e2b497958e802f86...a1a9291ab02a51267d8325cf89ee39536c862385
- Head commit: https://github.com/Valar05/home-center/commit/a1a9291ab02a51267d8325cf89ee39536c862385
- `docs/DATA_MODEL.md`: https://github.com/Valar05/home-center/blob/a1a9291ab02a51267d8325cf89ee39536c862385/docs/DATA_MODEL.md
- `functions/index.js`: https://github.com/Valar05/home-center/blob/a1a9291ab02a51267d8325cf89ee39536c862385/functions/index.js
- `tools/home_center_regression_tests.py`: https://github.com/Valar05/home-center/blob/a1a9291ab02a51267d8325cf89ee39536c862385/tools/home_center_regression_tests.py
- Creative failure issues: #38-#45, especially https://github.com/Valar05/home-center/issues/42 and https://github.com/Valar05/home-center/issues/44

### Pose Lab V2

Canonical evidence:

- Compare: https://github.com/Valar05/pose-lab-v2/compare/c26c2436dafadf26a205204d2f97dd807fa35eef...cfadd35b508427385dfda7bdc299f259d3b03efc
- Head commit: https://github.com/Valar05/pose-lab-v2/commit/cfadd35b508427385dfda7bdc299f259d3b03efc
- `docs/ATTACK_AUTHORING_LEARNINGS.md`: https://github.com/Valar05/pose-lab-v2/blob/cfadd35b508427385dfda7bdc299f259d3b03efc/docs/ATTACK_AUTHORING_LEARNINGS.md
- `docs/POSE_LAB_V2_ATTACK_BAKE_DOCTRINE.md`: https://github.com/Valar05/pose-lab-v2/blob/cfadd35b508427385dfda7bdc299f259d3b03efc/docs/POSE_LAB_V2_ATTACK_BAKE_DOCTRINE.md
- `docs/VISUAL_VERIFICATION_DOCTRINE.md`: https://github.com/Valar05/pose-lab-v2/blob/cfadd35b508427385dfda7bdc299f259d3b03efc/docs/VISUAL_VERIFICATION_DOCTRINE.md
- `package.json`: https://github.com/Valar05/pose-lab-v2/blob/cfadd35b508427385dfda7bdc299f259d3b03efc/package.json

### Drive context

Canonical Drive context remains Drive-native:

- `Lexen Green Commander Doctrine Updates and Simulation`
- `Discovery Promotion Report - 2026-07-06 - Cost Governor + Creative Turn Kernel + Lexen Simulation Constants`
- Existing skill cluster docs and Daily Delta index

Drive Lexen doctrine is writing truth. Home Center issues are delivery/runtime truth. Do not collapse those two layers.

---

## Promotion Records

### 1. Spend Telemetry Without Content Leakage

**Observation:** Home Center now records usage events, usage daily aggregates, and pricing records. The data model explicitly forbids storing prompts, document contents, email bodies, OAuth tokens, API keys, Authorization headers, and raw tool arguments in usage telemetry. Missing pricing appears as unpriced events instead of fake zero-dollar truth.

**Why it matters:** The previous cost-governor doctrine said cost was architecture leaking money. This adds the missing operating surface: owner/admin spend visibility without turning the telemetry table into a surveillance swamp.

**Reusable rule:** Cost telemetry must count calls, tokens, tools, providers, status, latency, and pricing state as safe metadata. It must not store content. Unknown pricing is `unpriced`, not free.

**Owning clusters:** Home Center, AI Orchestration, Software Delivery, Accessibility Engineering.

**Confidence:** High. Backed by data model, gateway implementation, and regression surface.

**Evidence:** Home Center `DATA_MODEL.md`, `functions/index.js`, usage dashboard commit `d75a236`, and head compare through `a1a9291`.

---

### 2. Economy Tool Palette Before Planner

**Observation:** Home Center now filters the available tool registry per request, gates web search, lowers reasoning effort, caps normal output, and regression-tests that the planner receives a smaller tool surface instead of the whole registry.

**Why it matters:** The model should not be handed every possible action on every turn. Broad tool exposure increases cost, prompt bloat, confusion, and accidental routing into unrelated workflows.

**Reusable rule:** Expose the smallest useful tool palette derived from current user intent, working memory, and recent tool evidence. Add web search only when the request needs it. A capability registry is not a prompt buffet.

**Owning clusters:** AI Orchestration, Home Center, Software Delivery.

**Confidence:** High. Backed by gateway code and regression assertions.

**Evidence:** `economyToolPalette`, `shouldEnableWebSearch`, low-reasoning normal turns, and regression tests in Home Center.

---

### 3. Remembered Context Inspection Must Read Before Answer

**Observation:** Home Center now detects questions about remembered documents, context, logs, messages, conversations, and memory; if a remembered document is present, it routes through `docs.read` before answering. The evidence finalizer is instructed to answer from the read evidence and to distinguish “I read it and did not find that” from “I could not inspect it.”

**Why it matters:** The assistant cannot claim uncertainty about a remembered document while carrying a live pointer to it. That creates false helplessness and burns user trust.

**Reusable rule:** When the user asks what is in remembered context, inspect the remembered artifact first. If the artifact was read and the phrase is absent, say that. Do not pretend the context was unavailable after a successful read.

**Owning clusters:** AI Orchestration, Writing Systems, Home Center.

**Confidence:** Medium-high. Strong gateway implementation; installed-path proof should continue through user reports.

**Evidence:** Home Center `rememberedContextDocToolCall`, evidence finalizer context-inspection rules, and commit `a1a9291`.

---

### 4. Creative Finalizer / Report Loop Breaker

**Observation:** Home Center issues #38-#45 show repeated Lexen creative-writing requests being routed into report confirmation loops, stalling after `docs.read`, or cutting off before completion. Home Center now routes creative requests through bounded finalizer/draft/repair flows, forbids tool calls during finalization, preserves explicit story premises, and covers the issue #42 docs-read-finalization path in metal smoke.

**Why it matters:** Search/read/save/report workflows do not substitute for the requested creative artifact. For voice-first writing, the output surface is the prose itself.

**Reusable rule:** A successful context read followed by an unfinished creative task must become a bounded complete draft. If the user asks for prose, do not answer with process, report confirmation, or another tool loop.

**Owning clusters:** AI Orchestration, Writing Systems, Accessibility Engineering, Home Center.

**Confidence:** High as a rule; medium-high as installed behavior until repeated installed-path success closes the issue cluster.

**Evidence:** Home Center issues #38-#45, evidence finalizer code, creative provider/repair prompts, and regression/metal smoke assertions.

---

### 5. Narration Delivery Boundary

**Observation:** Home Center now includes media-session narration controls, visible working state, haptic working feedback, Cartesia zero-write/incomplete-write fallback behavior, and raw tool-call JSON blocking before chat/narration display.

**Why it matters:** A voice-first assistant is not done when text exists somewhere. It is done when the user can receive, pause, stop, recover, and trust the delivery surface.

**Reusable rule:** Delivery is part of completion. For accessibility-first assistants, narration failure, stuck working state, raw tool JSON, or silent truncated playback is a failed user path.

**Owning clusters:** Accessibility Engineering, Home Center, AI Orchestration.

**Confidence:** High for regression coverage; medium-high for full installed behavior until user-path validation repeats.

**Evidence:** Home Center regression tests and commit `833d8e4` under the July 7 head.

---

### 6. Quarantined Candidate Animation Authoring

**Observation:** Pose Lab V2 attack work became usable only after narrowing the job: preserve the visible saber/hand relationship, preserve manual Meshy keys as truth, use FPS clips as choreography reference, bake static candidates under review surfaces, and quarantine candidates until hosted visual acceptance.

**Why it matters:** Pose Lab V1 repeatedly let metrics, smoke, and source transformations masquerade as visual success. V2’s safer move is to create small inspectable candidate surfaces and keep runtime ownership boring.

**Reusable rule:** Author animation candidates as quarantined, reviewable data. FPS source may guide choreography, timing, and wrist/blade intent, but manual accepted keys and human-visible cloud review own promotion.

**Owning clusters:** Animation and Pose Systems, Game Development, AI Orchestration.

**Confidence:** High as local project doctrine; medium as cross-project animation doctrine until another asset class repeats it.

**Evidence:** Pose Lab V2 attack authoring learnings, bake doctrine, package scripts, and compare through `cfadd35`.

---

### 7. Fist Limb Body-Space Pinning

**Observation:** Weaponless fist clips failed when FPV screen/camera positions were treated as body targets. The promoted fix maps FPS upper-arm and forearm vectors through the body frame, anchors them at the Meshy arm joint, and solves Meshy elbow/wrist world occupancy before judging fist orientation.

**Why it matters:** Screen-space pinning can create convincing numbers while putting the body into impossible positions. The review surface must distinguish perceptual inspection from skeletal truth.

**Reusable rule:** For body-owned limb poses, preserve the source limb chain in body space before judging hand/fist orientation. FPV projection is a diagnostic readout after body-space occupancy is true, not the source target for the full body.

**Owning clusters:** Animation and Pose Systems, Game Development.

**Confidence:** High for Pose Lab V2 fist family; medium as general body-retarget doctrine until reused outside Meshy/FPS assets.

**Evidence:** Pose Lab V2 attack authoring learnings and attack bake doctrine.

---

### 8. Visual Predicate Before Rig Math — Updated Evidence

**Observation:** Pose Lab V2 now restates visual instructions as screen-space predicates before editing. Smoke/build/route/asset checks are classified as guardrails, not visual acceptance. Hosted visual review remains the acceptance surface.

**Why it matters:** This updates prior Visual Truth Authority doctrine with a concrete V2 implementation pattern: translate user-visible corrections into the relationship a human should see before touching rig math.

**Reusable rule:** Do not ship rig-space guesses for visual choreography. Convert the user correction into a visible predicate, then treat all metrics as diagnostics until hosted visual evidence matches the predicate.

**Owning clusters:** Animation and Pose Systems, AI Orchestration, Game Development.

**Confidence:** High as a refinement of already-promoted doctrine.

**Evidence:** Pose Lab V2 visual verification doctrine and attack bake doctrine.

---

## Source-of-truth decisions

- **Home Center GitHub** owns runtime behavior, gateway code, tool routing, spend telemetry, issues, regression tests, and installed-path fixes.
- **Pose Lab V2 GitHub** owns animation authoring/bake/review doctrine, candidate quarantine, Meshy/FPS evidence, and cloud-review scripts.
- **Drive Lexen doctrine** owns the writing-canon content and scene doctrine.
- **Home Center Lexen issues** are delivery/runtime bug evidence, not replacement writing doctrine.
- **Thunder Brainstorm** carries source routes only. It must not become fake authority for the project evidence.
- **Agent Closet** records the promotion decision and reusable rules.

## Duplicate / merge / archive calls

- Collapse Home Center issues #38-#45 into one creative-output delivery epic once installed proof confirms the finalizer/repair path. Keep individual issues as specimens until then.
- Do not re-promote Lexen premise custody as new doctrine today. It was already promoted; today’s Home Center failures are delivery-path failures around that canon.
- Keep Visual Truth Authority as the parent doctrine. Today’s Visual Predicate Before Rig Math record is an implementation refinement, not a new top-level doctrine.
- Keep Pose Lab V2 candidates quarantined. Review URLs, smoke passes, and build passes are not accepted animation evidence.
- Archive/demote telemetry or dashboard notes that store content, raw arguments, tokens, or secrets as “usage evidence.”

## Final compression

```text
Count the spend without recording the soul.
Expose the tool the turn needs, not the whole garage.
A read context must become an answer.
A prose request must become prose.
A voice assistant is not done until delivery is controllable.
A pose candidate is not accepted until the visible predicate is true.
```
