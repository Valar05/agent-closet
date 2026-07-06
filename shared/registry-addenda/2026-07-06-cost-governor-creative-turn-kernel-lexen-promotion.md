# Discovery Promotion Addendum — 2026-07-06 — Cost Governor + Creative Turn Kernel + Lexen Simulation Constants

Status: promoted addendum
Owner: Quartermaster
Date: 2026-07-06
Drive report: https://docs.google.com/document/d/18vHgYjVASB3NqNg22uO-zbUax5m6lPgfI9mbX8--fik

## Reviewed artifacts

### Drive

- `Discovery Promotion Report - 2026-07-06 - Cost Governor + Creative Turn Kernel + Lexen Simulation Constants`
- `Lexen Green Commander Doctrine Updates and Simulation`
- `Home Center - Skill Cluster Index`
- `Skill Cluster - AI Orchestration`
- `Skill Cluster - Software Delivery`
- `Skill Cluster - Accessibility Engineering`
- `Skill Cluster - Writing Systems`
- `Skill Cluster - Project Archaeology`
- `Drive Knowledge Index - Daily Delta`
- `Discovery Promotion Report - 2026-07-05 - Context Firewall + Green Commander + Pose Lab V2`

### GitHub

- `Valar05/home-center` issues #31-#45, especially #45 as the fixed live installed-path specimen and #37 as the open clickable-link surface bug.
- `Valar05/home-center` commits:
  - https://github.com/Valar05/home-center/commit/9fc3b862102d05f91a6177eb81e0186fdd5d7e24 — Add gateway turn kernel.
  - https://github.com/Valar05/home-center/commit/304693176692ad5865a9cde935f6ceab0fc7209e — Finalize active tasks from tool evidence.
  - https://github.com/Valar05/home-center/commit/20f7352cfefb4b3fb558b2c9695608675871d975 — Guard against truncated prompt replies.
  - https://github.com/Valar05/home-center/commit/1db2c9a805c4c36632845f97088b97d8bde93213 — Complete bounded evidence finalizer prose.
  - https://github.com/Valar05/home-center/commit/91a286d872d919b48e1826b7f1ebb19ca26b24d1 — Route report-contaminated creative turns to context.
  - https://github.com/Valar05/home-center/commit/2c4cb4c93600a56335dd5d08e2b497958e802f86 — Reduce agent cost and harden evidence finalizer.
  - https://github.com/Valar05/home-center/commit/833d8e4e0fe51104f383fdf7ebc0defd7a188ad2 — Fix installed app creative turn and Cartesia proxy playback.
- `Valar05/home-center` `docs/AI_COST_AUDIT.md`.

No newly updated pull requests were found in the reviewed active repositories for this window.

## Promoted discoveries

### 1. Cost Governor / Cheapest Capable Call

Observation: Home Center's cost problem is not one expensive request. Repository evidence shows a multiplicative cost surface: GPT-5.5 on normal turns, medium reasoning, always-on hosted web search, broad tool registry exposure, repeated tool-loop calls, duplicated tool evidence JSON, production smoke calls, and creative recovery passes.

Why it matters: billing pain is architectural feedback. If simple acknowledgements, list navigation, confirmations, CRUD success messages, and post-tool success states still invoke premium reasoning, the assistant pays for judgment when it already has truth.

Reusable rule:

```text
The cheapest capable model call is no model call.
```

Evidence: `docs/AI_COST_AUDIT.md` identifies the OpenAI call graph, prompt/runtime caps, always-enabled web search, tool-loop multiplication, and deterministic commands that should bypass GPT. The cost-hardening commit reduces agent cost and hardens the evidence finalizer.

Confidence: high for Home Center; medium-high reusable AI Orchestration / Software Delivery doctrine until repeated outside one assistant host.

Owning clusters: AI Orchestration, Software Delivery, Project Archaeology.

### 2. Turn Kernel Before Planner

Observation: Home Center now normalizes pending confirmations, confirm/cancel language, stale pending actions, active task continuation, report-contaminated context, and latest user intent before handing the turn to the model.

Why it matters: raw transcript is not the user's current command. Without a turn kernel, yesterday's confirmation, issue report, or unfinished tool loop can hijack today's creative request.

Reusable rule:

```text
Do not let yesterday's pending confirmation become today's user intent.
```

Evidence: commit `9fc3b862102d05f91a6177eb81e0186fdd5d7e24` adds the gateway turn kernel. Commit `91a286d872d919b48e1826b7f1ebb19ca26b24d1` routes report-contaminated creative turns back to context instead of letting issue/report state win.

Confidence: high for Home Center; high reusable assistant-orchestration rule.

Owning clusters: AI Orchestration, Software Delivery, Accessibility Engineering.

### 3. Evidence Finalizer After Context Read

Observation: issues #31-#45 repeat a single failure family: the assistant successfully reads or knows the Lexen context, then still fails to deliver the requested visible/listenable creative artifact and falls back into docs/read/report/confirmation loops.

Why it matters: reading evidence is not completing the task. A successful content-bearing tool result must be converted into an answer when the active task is still unfinished.

Reusable rule:

```text
content-bearing tool success + unfinished active task
    -> evidence finalizer
    -> final answer, no tools available
```

Evidence: issue #45 records the fixed specimen class: the Lexen doctrine document had already been read, but Home Center reported instead of writing. Commit `304693176692ad5865a9cde935f6ceab0fc7209e` finalizes active tasks from tool evidence. Commit `1db2c9a805c4c36632845f97088b97d8bde93213` completes bounded evidence-finalizer prose.

Confidence: high for Home Center and high as reusable AI Orchestration doctrine.

Owning clusters: AI Orchestration, Accessibility Engineering, Project Archaeology.

### 4. Bounded Completion Beats Long Broken Output

Observation: installed-app behavior proved that an ambitious long chapter is worse than a shorter complete scene when output truncates, times out, fails narration, or leaves the app in a bad active-task state.

Why it matters: output length is a delivery contract, not only a writing preference. For a voice-first assistant, complete usable output and narration delivery are part of the product surface.

Reusable rule:

```text
Small complete output beats ambitious broken output.
```

Evidence: commit `20f7352cfefb4b3fb558b2c9695608675871d975` guards against truncated prompt replies. Commit `833d8e4e0fe51104f383fdf7ebc0defd7a188ad2` fixes the installed app creative turn and Cartesia proxy playback.

Confidence: high for Home Center; medium-high reusable Accessibility / Software Delivery rule.

Owning clusters: Accessibility Engineering, Software Delivery, AI Orchestration, Writing Systems.

### 5. Narration Delivery Boundary

Observation: Cartesia playback had to be fixed through the hosted Firebase proxy and Android PCM streaming path, not treated as optional UI polish.

Why it matters: Home Center is voice-first and assistive. If the prose is correct but read-aloud delivery fails, the answer still failed for the household use case.

Reusable rule:

```text
For a voice-first assistant, failed narration is failed delivery.
```

Evidence: commit `833d8e4e0fe51104f383fdf7ebc0defd7a188ad2` fixes installed-app creative turn and Cartesia proxy playback. Issue #37 remains open for clickable links, preserving the related accessible-output surface bug.

Confidence: high for Home Center; high reusable Accessibility Engineering doctrine.

Owning clusters: Accessibility Engineering, AI Orchestration, Software Delivery.

### 6. Simulation Constants Before Prose

Observation: the Lexen material shows that creative failure often starts before style: vehicle, crew roles, authority chain, physical constraints, and historical constraint must be locked before drafting.

Why it matters: pretty prose can silently violate command structure. Lexen must remain commander. Tango must be one fixed thing. Crew help may complicate Lexen's authority, but it must not replace it.

Reusable rule:

```text
Simulation constants outrank pretty prose.
```

Evidence: Drive Lexen Green Commander doctrine and the July 6 promotion report preserve the constants: vehicle, crew roles, authority chain, physical constraints, historical constraint. The Home Center issue family shows why this became product-critical: the assistant repeatedly read the canon and still failed to deliver a grounded scene.

Confidence: high for Lexen/Tanks writing; medium-high reusable Writing Systems doctrine.

Owning clusters: Writing Systems, Project Archaeology, Game Development.

### 7. Operational Fear Becomes Specificity

Observation: the strongest Green Lexen pattern is not fear-as-decoration. Fear improves observation: angle, range, traverse, smoke, second weapon, uncertain hit state, crew readiness, and responsibility under incomplete information.

Why it matters: this preserves Lexen as a green commander becoming operationally specific, not a generic hero becoming fearless.

Reusable rule:

```text
Lexen does not become fearless.
He becomes more specific.
```

Evidence: Drive Lexen Green Commander doctrine and the July 6 promotion report record the Writing Systems upgrade.

Confidence: medium-high as writing doctrine; Drive remains canonical until repo-backed scene cards exist.

Owning clusters: Writing Systems, Game Development.

## Duplicate and boundary calls

- Cost Governor belongs under AI Orchestration and Software Delivery. Do not activate an AI FinOps cluster unless the pattern repeats outside Home Center or produces cross-project telemetry/process doctrine.
- Turn Kernel Before Planner refines Context Firewall, Output Surface Must Match User Intent, and Active Task State Must Resume. It does not replace them.
- Evidence Finalizer refines Tool Loop Progress Fallback and Read-to-Write Continuation. It is the answer-producing state after source/context acquisition succeeds.
- Bounded Creative Output refines Creative Output Surface and Accessibility delivery. It is not a separate prompt-length doctrine.
- Lexen scene docs remain source evidence. Promote reusable simulation rules, not the whole scene as universal doctrine.

## Source-of-truth decisions

- Home Center GitHub issues, commits, tests, app behavior, and `docs/AI_COST_AUDIT.md` are canonical for cost, turn-kernel, evidence-finalizer, creative-output, installed-path, and narration-delivery evidence.
- Drive Lexen doctrine remains canonical for green-commander writing extraction until Tanks scene cards or repo-backed story cards exist.
- Drive report and skill clusters summarize and index the sweep.
- Agent Closet preserves this promotion decision; it does not supersede Home Center implementation truth or Drive story truth.
- Thunder Brainstorm carries source routes only; it must not fork doctrine bodies.

## Archive / merge guidance

Archive or demote:

- stale report-loop issue records after they are linked into the #31-#45 regression family and #45 fixed specimen;
- old long-output creative finalizer settings superseded by installed-app-safe budgets;
- broad tool-palette assumptions that advertise expensive capabilities on every turn;
- smoke logs that spend production GPT without call counters or explicit spend gates;
- raw story drafts that do not record simulation constants, observation, and promotion status.

Hold:

- Home Center issue #37 remains an open Accessibility Engineering surface bug for clickable links.
- AI Cost Governance stays a cluster candidate, not a top-level cluster.
- Link rendering and output delivery remain under installed user-path verification until the surface is proven fixed.

## Final rule

```text
Cheapest capable call is no call.
Context reads must become answers.
Small complete beats long broken.
Simulation constants outrank pretty prose.
```