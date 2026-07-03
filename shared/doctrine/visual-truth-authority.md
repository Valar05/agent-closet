# Visual Truth Authority

Type: Operating doctrine / evidence authority
Status: Canon
Owner: Quartermaster
Date: 2026-07-03
Related:
- `shared/doctrine/perspective-guided-command.md`
- `shared/doctrines.md`
- `shared/reality-negotiation.md`
- `agents/quartermaster/doctrine.md`
- `agents/command-center/identity.md`

## Rule

When the work is visual, visible evidence is the authority.

Telemetry, DOM state, logs, metrics, cache tokens, source-string tests, green CI, and model confidence are support evidence only.

They cannot override a screenshot, contact sheet, video, live capture, or human visual report that shows the artifact is still wrong.

If the agent has not inspected the actual visual artifact that acceptance depends on, the result is not verified.

## Cloud Visual Truth

If cloud visual parity is the acceptance lane, inspect the cloud screenshots.

Do not substitute local Android screenshots, local browser state, localhost Playwright, offline renders, generated staging output, debug bridge telemetry, or JSON summaries for the cloud screenshots.

The claim must name the inspected visual artifacts.

If the artifact is missing, too distant, cropped badly, stale, or unreadable, the gate is blocked.

## False Green Rule

A green gate that passes a visibly red artifact is a broken gate.

The next action is to fix or quarantine the gate, not to report success.

If a human visual report contradicts a green result, treat the contradiction as a stop condition until the artifact and gate explain the disagreement.

## No-Op Churn Rule

When a human reports `red build`, `no visual change`, `no-op`, or equivalent after a claimed visual fix, all prior green checks are demoted to support evidence.

The next deliverable must be one of:

- a visible delta in the accepted visual evidence lane
- a preserved failed attempt with the red artifact named
- a concrete blocker requiring human intervention

Do not report gate work, telemetry work, UI labels, cache busting, review banners, artifact schema changes, or other instrumentation-only edits as progress on the visual fix. Label them as instrumentation, diagnosis, preservation, or failed-attempt cleanup.

## UI Can Lie

Runtime UI truth labels, review pages, clip lists, debug overlays, selected rows, and green banners are support evidence only. They are part of the artifact under review, not the authority over the artifact.

A UI that says the build is correct while the visible target relationship is wrong is itself red. Fix the lying UI or quarantine it before using it to judge another visual fix.

If the user must manually select the actor, clip, item, tab, page, or mode that the review URL claimed to load automatically, the review surface is red. Manual recovery after a bad hydration is not acceptance evidence; it is a route/state-hydration failure.

The required order after this class of failure is:

1. state the visible contradiction
2. fix the lying evidence/UI gate
3. prove the gate catches the contradiction
4. only then edit visual math, offsets, transforms, layout, or gameplay behavior

## Paid / Cloud Loop Discipline

Cloud and paid review loops are not accomplishments by themselves. Before spending another run after a human no-op or red-build report, name the new visual hypothesis, the artifact that will answer it, and the stop condition.

If the new run cannot answer a new visual question, do not run it. If it answers the question red, preserve that evidence and change the implementation hypothesis before spending another loop.

## Visible Relationship Truth

Visual truth is not object presence.

A screenshot is not green because the right actor, clip, route, marker, prop, debug overlay, DOM state, or telemetry label exists.

It is green only when the intended visible relationship is present.

For visual work, name:

- expected relationship
- actual relationship in the artifact
- visible mismatch
- telemetry agreement or contradiction

Examples:

- a weapon is not correct unless wrist, hand, hilt, grip, and blade axis read correctly
- a pose is not correct unless the silhouette and limb relationships match the intended action
- a UI state is not correct unless the selected control, highlighted row, and visible result agree
- a collision/support fix is not correct unless the visible surface and physical support relationship agree
- a camera fix is not correct unless the subject is framed as intended

If the relationship is wrong, the artifact is red even when metrics say the object is visible or selected.

## Truth Ledger

Before claiming success on significant implementation work, state the truth ledger:

- repository truth
- runtime truth
- visual truth
- human truth

If any truth layer is red, the output must be framed as preservation, diagnosis, or blocker.

It must not be framed as progress.

## Required Conduct

- Inspect the acceptance artifact before reporting pass/fail.
- Name the artifact path, URL, or run id used for the visual read.
- Describe the visible state in plain terms before citing telemetry.
- Describe the intended visual relationship and the actual visual relationship before citing telemetry.
- Treat telemetry as explanatory support after the visual read, not as authority before it.
- If the visual artifact is red, stop forward promotion and preserve the red evidence.
- If the visual artifact cannot prove the claim, say `not verified`.

## Failure Evidence

This doctrine was promoted after a Pose Lab Firebase visual-truth failure.

The cloud workflow passed while the actual cloud screenshots showed a red Meshy Ready result: the selected clip UI was inconsistent, the Ready hand and grip basis were visibly wrong, and the follow sheet was too distant to prove visual parity.

The agent cited telemetry and green workflow status before inspecting the relevant cloud screenshots. That is an operating failure, not a test gap alone.

The follow-up failure generalized the rule: even after the correct cloud route opened, the visible T-pose wrist/saber relationship was mutated and the Ready hand/sword relationship did not read as acceptable visual IK/FK. The gate had measured actor, clip, weapon visibility, markers, and telemetry while failing to judge the intended relationship. That is visible-relationship false-green.

## Acceptance Criteria

This doctrine is working when:

- visual claims begin from the actual visual artifact
- visual claims name expected relationship versus actual relationship
- green telemetry cannot override visible red truth
- object presence cannot override a wrong visible relationship
- human visual contradiction stops promotion
- unreadable visual artifacts block acceptance
- false-green gates are treated as broken gates
- agents say `not verified` when they have not inspected the artifact
- truth ledgers distinguish progress from preservation, diagnosis, and blockers

## Retrieval Keywords

visual truth authority, visible relationship truth, expected relationship actual relationship, visible evidence, cloud screenshots, false green, telemetry cannot override screenshots, object presence is not visual proof, not verified, human visual contradiction, truth ledger, red visual artifact, no-op churn, UI can lie, paid cloud loop discipline, instrumentation is not visual progress
