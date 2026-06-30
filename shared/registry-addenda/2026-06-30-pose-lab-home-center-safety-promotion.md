# Discovery Promotion Record - 2026-06-30 - Pose Lab Direct Manipulation + Home Center Destructive Safety

Status: Promoted / source-routed

Purpose: Preserve reusable discoveries from the 2026-06-30 Pose Lab Meshy weapon alignment work and Home Center destructive-tool safety work without letting Drive reports or Thunder mirrors become false source of truth.

## Reviewed artifacts

### GitHub canonical implementation sources

- `Valar05/pose-lab` commits after the previous promotion sweep:
  - `c31050c2afacbe312f01ea8f0103ae323058842c` - Add Meshy weapon tuning workflow.
  - `419fe58c065afbb9af01c837a4c7e3dba96acf43` - Add Meshy projection diagnostic workspace.
  - `ae409d045b8fe535b5d66a147e45771ccb57b1e4` - Improve Meshy projection diagnostics.
  - `983dca0ca130bec110b54cfb6dc0c943da102a86` - Add Meshy weapon basis diagnostic workspace.
- `Valar05/pose-lab` files discovered in the live repo index:
  - `tools/meshy_projection_workspace.mjs`
  - `tools/meshy_weapon_basis_workspace.mjs`
  - `tools/test_meshy_weapon_basis_workspace.mjs`
  - `docs/ANIMATION_WORKFLOW_TOOLING.md`
  - `generated/weapon_basis_workspace/diagnostic_summary.md`
- `Valar05/home-center` commit:
  - `8f4720b0a4eeedba14d6bb411bbbc9992aea46fb` - Add double-confirm delete tools.
- `Valar05/home-center` files discovered in the live repo index:
  - `tools/home_center_tool_contract.json`
  - `tools/home_center_regression_tests.py`
  - `app/src/main/java/com/dclar/homecenter/ToolRegistry.java`
  - `app/src/main/java/com/dclar/homecenter/MainActivity.java`
  - `functions/index.js`

### Drive and mirror sources

- Drive report: `Discovery Promotion Report - 2026-06-30 - Pose Lab Direct Manipulation + Home Center Destructive Safety`.
- Drive cluster indexes patched on 2026-06-30: AI Orchestration, Project Archaeology, Game Development, Accessibility Engineering, Home Center Skill Cluster Index, and Daily Delta.
- Thunder Brainstorm source refs patched in `generated/source_refs_github/2026-06-30_pose_lab_home_center_safety_source_refs.jsonl`.

## Promotion 1 - Direct Manipulation After Numeric Edit Failure

Observation:
Pose Lab surfaced a repeated spatial-alignment loop: the user sees a visible misalignment, the assistant adjusts numeric offsets, the user sends another screenshot, and the cycle repeats without enough physical control or measurement.

Why it matters:
Visible 3D alignment problems should not be solved by haunted spreadsheet combat. Numeric edit loops consume attention, create brittle guesses, and make the operator narrate geometry that the tool should expose directly.

Reusable rule:
If a visible spatial alignment problem survives one numeric edit, stop guessing numbers and build a direct manipulation control.

Supporting evidence:
- `Valar05/pose-lab` commit `c31050c2afacbe312f01ea8f0103ae323058842c` added the Meshy weapon tuning workflow.
- Later Pose Lab commits added projection and weapon-basis diagnostic workspaces instead of treating offset strings as the final answer.
- The Drive report records the next useful feature as a viewport gizmo / Pick Grip Center style control for model-space socket offset and attachment rotation.

Confidence: Medium-high.

Owning skill clusters:
- Game Development
- Accessibility Engineering
- AI Orchestration

Promotion status:
Promote as reusable spatial-tooling doctrine.

## Promotion 2 - Diagnostic Workspace Is Not Promotion Evidence

Observation:
Pose Lab added Meshy projection and weapon-basis workspaces that isolate variables such as projected pins, FK, IK, sword observations, local basis, roll, grip, blade tip, attachment rotation, and scale.

Why it matters:
Diagnostic surfaces are valuable because they reveal the failure. They are not proof that production behavior is accepted. A lab can explain the wound; it is not the scar healing.

Reusable rule:
A diagnostic workspace can explain a problem, but production promotion still requires visual evidence, metric evidence, baseline protection, and acceptance checks.

Supporting evidence:
- `tools/meshy_projection_workspace.mjs` and `tools/meshy_weapon_basis_workspace.mjs` exist as diagnostic workspaces in `Valar05/pose-lab`.
- `tools/test_meshy_weapon_basis_workspace.mjs` anchors the workspace as a tested diagnostic artifact.
- The Drive report explicitly holds diagnostic workspaces as local laboratories rather than accepted runtime behavior.

Confidence: High.

Owning skill clusters:
- AI Orchestration
- Project Archaeology
- Game Development

Promotion status:
Promote as reusable validation-boundary doctrine.

## Promotion 3 - Spatial Attachment Anchor Split

Observation:
Meshy saber alignment exposed that a weapon attachment is not one magic offset. It has distinct anchors: synthetic socket, hand-local offset, model-local offset, model grip landmark, blade tip landmark, attachment rotation, and attachment scale.

Why it matters:
Collapsing multiple anchors into one fuzzy numeric blob makes every correction ambiguous. The operator cannot tell whether they are fixing socket placement, grip center, blade axis, local basis, roll, or scale.

Reusable rule:
When a spatial tool has multiple anchors, expose each anchor as a named control and measured error.

Supporting evidence:
- Pose Lab commits created projection and weapon-basis workspaces for making pins, observations, basis, roll, grip, tip, and attachment state inspectable.
- `generated/weapon_basis_workspace/diagnostic_summary.md` and `generated/weapon_basis_workspace/weapon_basis_workspace.json` preserve the diagnostic state separately from production acceptance.

Confidence: Medium-high.

Owning skill clusters:
- Game Development
- Accessibility Engineering

Promotion status:
Promote as reusable 3D-art tooling doctrine.

## Promotion 4 - Cache Token Is Visual Truth

Observation:
Browser-based visual labs can be source-green while the page still loads stale JS/CSS/profile imports. Screenshot feedback taken against a stale bundle is false evidence.

Why it matters:
Visual QA depends on the runtime actually being the runtime under review. Cache state is not housekeeping; it is part of the evidence chain.

Reusable rule:
Do not ask for screenshot feedback until the page is known to be loading the intended runtime bundle.

Supporting evidence:
- The Drive report records cache-token validation as a promoted project archaeology rule.
- Pose Lab work happened in browser-facing diagnostic surfaces where visible proof depends on active bundle freshness.

Confidence: Medium.

Owning skill clusters:
- Game Development
- Project Archaeology

Promotion status:
Promote as reusable visual-QA evidence doctrine candidate.

## Promotion 5 - Destructive Tool Safety Belongs In The Contract

Observation:
Home Center added delete/trash/remove tools with destructive metadata and double-confirmation requirements in the tool contract and related dispatcher/test surfaces.

Why it matters:
Deleting user data is not merely a model-caution problem. Safety must be represented where tools are registered, dispatched, confirmed, and regression-tested.

Reusable rule:
Destructive actions must be marked destructive, require confirmation, require double confirmation, and be covered by contract/dispatcher tests.

Supporting evidence:
- `Valar05/home-center` commit `8f4720b0a4eeedba14d6bb411bbbc9992aea46fb` is titled `Add double-confirm delete tools`.
- Live repo search found the destructive-tool change touching `tools/home_center_tool_contract.json`, `tools/home_center_regression_tests.py`, `ToolRegistry.java`, `MainActivity.java`, and `functions/index.js`.

Confidence: High.

Owning skill clusters:
- AI Orchestration
- Accessibility Engineering
- Project Archaeology
- Home Center project-local cluster

Promotion status:
Promote as a refinement of `Tool Contract Coverage Is The Trust Boundary` and `Confirmation-Gated Writes`.

## Promotion 6 - Plain-English Failure Remains Part Of Tool Safety

Observation:
Home Center issue #13 and #12 remain relevant to destructive action safety because a confirmed destructive capability still needs user-readable recovery language when the plan fails.

Why it matters:
A safe assistant must not only prevent accidental damage; it must also explain partial work, failed action, retry path, and user action without leaking tool-loop sludge.

Reusable rule:
Tool safety includes recovery language, not just confirmation gates.

Supporting evidence:
- Prior Home Center issues #12 and #13 are still the canonical product-friction examples for planner failure surfacing as user-hostile language.
- The 2026-06-30 Drive report reattaches plain-English recovery to the destructive-tool safety boundary.

Confidence: High.

Owning skill clusters:
- Accessibility Engineering
- AI Orchestration
- Project Archaeology

Promotion status:
Promote as an extension of failure-boundary doctrine.

## Source-of-truth decisions

- Pose Lab GitHub is canonical for Meshy weapon tuning implementation, diagnostic workspaces, tests, generated diagnostic summaries, and current art-tooling evidence.
- Home Center GitHub is canonical for destructive-tool contracts, tool registry behavior, dispatcher behavior, cloud function implementation, and regression tests.
- Home Center issues #12 and #13 remain canonical for the planner-failure UX bug class until closed by installed-path proof.
- Thunder Brainstorm is source-ref mirror only. It carries routes back to live GitHub evidence.
- Drive reports summarize the promotion sweep; Drive skill clusters index promoted rules. Neither replaces live repo evidence.

## Duplicates and false-source risks

- Do not create a new doctrine for delete tools. This is a refinement of `Tool Contract Coverage Is The Trust Boundary` plus `Confirmation-Gated Writes`.
- Do not create a new doctrine for every Pose Lab workbench. Projection and weapon-basis workspaces belong under the existing workbench / diagnostic surface family.
- Do not treat generated diagnostics as production acceptance. They are lab evidence until paired with visual/metric/baseline promotion proof.
- Do not count screenshots taken against stale cache tokens as acceptance evidence.
- Keep `Visual Production / Asset Tooling` as a candidate subdomain until the pattern repeats outside Pose Lab.

## Archive / merge guidance

Archive or demote:
- numeric offset guess logs after a direct manipulation handle exists;
- screenshots taken against stale runtime bundles;
- diagnostic workspaces treated as accepted runtime behavior;
- prompt-only delete safety claims not backed by contract fields and tests;
- Thunder mirrors that do not point back to live GitHub evidence.

Keep project-local:
- exact Meshy basis/projection file formats;
- exact saber model tuning offsets;
- Home Center delete tool names and Java/Cloud Function implementation details;
- Home Center issue-specific reproduction logs.

Promote reusable:
- Direct Manipulation After Numeric Edit Failure;
- Diagnostic Workspace Is Not Promotion Evidence;
- Spatial Attachment Anchor Split;
- Cache Token Is Visual Truth;
- Destructive Tool Safety Belongs In The Contract;
- Plain-English Failure Remains Part Of Tool Safety.

## Final compression

If the user is trying to line up a visible thing, do not make them debug invisible numbers forever.

Build the handle.
Measure the error.
Protect the baseline.
Promote only with evidence.
Double-confirm anything that destroys user data.
