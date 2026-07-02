# Perspective Coding Doctrine Notes

Status: running notes / scratch  
Owner: Quartermaster  
Started: 2026-07-02

Related:

- `../shared/doctrine/perspective-guided-command.md`
- `../shared/perspective-routing.md`
- `ore-worth-promoting.md`

## Purpose

Develop coding-specific doctrine for Perspective-Guided Command from real implementation failures.

This is not canon yet. It is scratch evidence for later promotion.

## Ledger Format

For each incident, record:

- observed failure
- perspective used
- artifact changed
- whether repo truth changed
- whether runtime truth changed
- whether visual truth changed
- whether human perception changed
- leverage gained
- leverage missed
- doctrine candidate
- promotion status

Before claiming success, implementation work must state the truth ledger:

- repo truth
- runtime truth
- visual truth
- human truth

If any truth layer remains red, the output must be framed as preservation, diagnosis, or blocker. It must not be framed as progress.

## Incident 2026-07-02 - Pose Lab Meshy FK Red Build

Context:
Pose Lab Meshy Ready / saber FK work produced clean-looking guardrail commits while the user's visual review remained red.

Observed failure:
A perspective-coded session produced guardrails and baseline artifacts but did not produce a user-visible improvement. The commit changed code and generated an offline schematic, but the user read it as visual no-op and churn.

Perspective used:

- Quartermaster preserved facts and contracts.
- Foreman shipped a clean slice.
- Gasket challenged false green gates.
- Prospector found useful ore in the failure.
- Wallfly should have been used earlier because the failure was visual.

Artifacts changed:

- Pose Lab `src/weapon-fk-contract.mjs`
- Pose Lab `tools/meshy_tpose_weapon_baseline_render.mjs`
- Pose Lab `generated/offline_render/meshy_tpose_weapon_baseline/baseline_render.json`
- Pose Lab `generated/offline_render/meshy_tpose_weapon_baseline/baseline_render.svg`

Truth comparison:

- Repo truth: improved. Known-bad metrics now fail.
- Runtime truth: unchanged. No runtime FK fix landed.
- Visual truth: unchanged from the user's perspective.
- Human perception: red build, visual no-op, churn edit.

Leverage gained:

- The bad Ready metrics cannot be reported as green by that contract.
- The offline baseline exposed a `socketToAuthoredLocalDistance` divergence of about `1.00297`, warning that pure authored-local FK would move the accepted T-pose surface.

Leverage missed:

- The artifact was not a before/after visual proof.
- The process did not require the generated artifact to answer the user's visible failure.
- The commit was framed as progress even though it was infrastructure only.

Doctrine candidates:

- During visual red builds, perspective coding must produce a changed visual artifact, an exact red artifact, or a concrete blocker. Guardrail-only commits are not enough.
- "Perspective used" is not evidence. Artifact delta is evidence.
- Perspective coding for implementation should require a truth ledger before claiming success: repo, runtime, visual, human.
- If any truth remains red, the output must be framed as preservation, diagnosis, or blocker, not progress.
- Gasket must be allowed to stop a Foreman commit when human visual truth says red.
- Wallfly should run before Foreman when the failure is visual.
- Quartermaster must distinguish preservation leverage from progress leverage.

Promotion status:
Strong ore. Keep in scratch. Promote only after the same rule survives another coding incident or after a follow-up process prevents a similar false-progress commit.

## Open Questions

- What minimum artifact proves "visual changed" without depending on unreliable browser capture?
- Should every visual red build require a before/after sheet checked into `generated/`?
- Should Gasket have an explicit stop phrase for "repo true, runtime unchanged, visual red"?
