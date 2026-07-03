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
- Treat telemetry as explanatory support after the visual read, not as authority before it.
- If the visual artifact is red, stop forward promotion and preserve the red evidence.
- If the visual artifact cannot prove the claim, say `not verified`.

## Failure Evidence

This doctrine was promoted after a Pose Lab Firebase visual-truth failure.

The cloud workflow passed while the actual cloud screenshots showed a red Meshy Ready result: the selected clip UI was inconsistent, the Ready hand and grip basis were visibly wrong, and the follow sheet was too distant to prove visual parity.

The agent cited telemetry and green workflow status before inspecting the relevant cloud screenshots. That is an operating failure, not a test gap alone.

## Acceptance Criteria

This doctrine is working when:

- visual claims begin from the actual visual artifact
- green telemetry cannot override visible red truth
- human visual contradiction stops promotion
- unreadable visual artifacts block acceptance
- false-green gates are treated as broken gates
- agents say `not verified` when they have not inspected the artifact
- truth ledgers distinguish progress from preservation, diagnosis, and blockers

## Retrieval Keywords

visual truth authority, visible evidence, cloud screenshots, false green, telemetry cannot override screenshots, not verified, human visual contradiction, truth ledger, red visual artifact
