# Discovery Promotion Record - 2026-07-01 - Pose Lab Synthetic Socket + Home Center Tool Recovery + Software Delivery Activation

Status: Promoted / source-routed

Purpose: Preserve reusable discoveries from Pose Lab synthetic socket work, Home Center provider-boundary failures, and repeated Availity workflow maintenance without letting Drive reports or Thunder mirrors become false source of truth.

## Reviewed artifacts

### Drive sources

- Drive report: `Discovery Promotion Report - 2026-07-01 - Pose Lab Synthetic Socket + Home Center Tool Recovery + Software Delivery Activation`.
- Drive cluster indexes patched on 2026-07-01: AI Orchestration, Animation and Pose Systems, Accessibility Engineering, Project Archaeology, Home Center Skill Cluster Index, Software Delivery, and Daily Delta.

### GitHub canonical implementation sources

- `Valar05/pose-lab` PR #1: `[codex] Mirror FPS weapon socket for Meshy`.
  - State: open draft.
  - Head: `codex/meshy-weapon-fps-parity` at `39fa21deabef56ef6dce0bfa5288bf373101efcf`.
  - Core change: mirror FPS Arms hierarchy as `RightHand -> synthetic WeaponR -> WeaponGrip -> visible sabre`.
  - Validation: `node --check src/pose-lab.js`, asset manifest JSON validation, FK attachment contract, Meshy FPS upper key convert contract, and live browser synthetic-source-socket follow check.
  - Changed-file surface includes `src/pose-lab.js`, `src/rig-profiles.js`, `docs/ANIMATION_WORKFLOW_TOOLING.md`, visual parity JSON/SVG evidence, FK/visual-follow tooling, generated-clip ownership tests, and diagnostics write-protection tests.
- `Valar05/home-center` issue #14: `Home Center lists fail with Firestore permission denied`.
- `Valar05/home-center` issue #15: `Home Center stalled before Google Docs update after reading source and target documents`.
- `Availity/availity-workflow` PR #877: `fix(workflow-vite): resolve lint hanging in TypeScript-only projects`.
- `Availity/availity-workflow` PR #879: `feat(workflow-vite): export globals types for vitest and jest-dom`.
- `Availity/availity-workflow` PR #881: `fix(workflow-vite): replace deprecated advancedChunks with codeSplitting`.
- `Availity/availity-workflow` PR #883: `fix: resolve dayjs ESM resolution and improve vitestOverrides API`.
- `Availity/availity-workflow` PR #884: `Release: Version Updates`.
- `Availity/availity-starter-vite-typescript` PR #1: `chore: modernize starter template with simplified examples`.

## Promotion 1 - Synthetic Socket Parity Before Visual Tuning

Observation:
Pose Lab stopped treating the Meshy saber as a loose visible mesh and mirrored the FPS source hierarchy: `RightHand -> synthetic WeaponR -> WeaponGrip -> visible sabre`.

Why it matters:
The old loop was haunted offset tuning. The durable fix is structural parity: preserve the authored source rig semantics before chasing visual placement numbers.

Reusable rule:
Synthetic targets should preserve source hierarchy semantics before visual tuning.

Supporting evidence:
- Pose Lab PR #1 summary explicitly mirrors the FPS Arms weapon hierarchy and preserves manual Meshy offsets while mapping authored FPS Weapon.R basis onto the synthetic socket.
- PR #1 includes FK/offline attachment contracts, upper-key conversion contracts, architecture-aware live/offline weapon follow diagnostics, and live browser validation.

Confidence: High for Pose Lab; Medium-high as reusable animation tooling doctrine until repeated outside this rig family.

Owning skill clusters:
- Animation and Pose Systems
- Game Development
- Project Archaeology

Promotion status:
Promote as reusable rig/retargeting doctrine; keep exact Meshy implementation project-local until PR #1 merges.

## Promotion 2 - Generated Artifact Ownership Must Be Exact

Observation:
Pose Lab introduced generationGroup ownership boundaries and tests so generated clips cannot erase sibling candidates or accepted baselines through broad prefix cleanup.

Why it matters:
Generated art/tooling surfaces become dangerous when cleanup rules are approximate. A prefix accident can destroy the exact comparison artifact needed for acceptance.

Reusable rule:
Generated artifact ownership must be exact, testable, and unable to erase sibling candidates by prefix accident.

Supporting evidence:
- Pose Lab PR #1 changed-file list includes `tools/test_generated_clip_group_replacement_does_not_delete_siblings.mjs` and diagnostics write-protection tests.
- The Drive report records broad string prefixes as banned because they can delete sibling candidates or accepted baselines.

Confidence: High.

Owning skill clusters:
- Animation and Pose Systems
- Project Archaeology
- AI Orchestration

Promotion status:
Promote as reusable generated-artifact governance doctrine.

## Promotion 3 - Real Ready Clip Beats Probe Evidence

Observation:
Pose Lab now distinguishes injected transform proof from acceptance evidence taken from the real ready clip: loaded cache token, parent chain, screen-space motion, and relative drift.

Why it matters:
Probe mode can prove that transforms are possible, but not that the production animation path is correct. This prevents lab demos from laundering themselves into acceptance.

Reusable rule:
A visual animation fix is accepted by non-probe evidence from the real ready clip, not by injected transform demos.

Supporting evidence:
- Pose Lab PR #1 includes `generated/visual_parity/meshy_onehand_ready/visual_parity.json`, `visual_parity_sheet.svg`, `tools/meshy_onehand_ready_visual_parity.mjs`, and visual-follow contract tests.
- The PR body reports live browser validation of Meshy Ready weapon follow as synthetic-source-socket.

Confidence: High.

Owning skill clusters:
- Animation and Pose Systems
- Game Development
- Project Archaeology

Promotion status:
Promote as reusable visual-acceptance doctrine.

## Promotion 4 - Provider-Specific Failure Attribution

Observation:
Home Center issue #14 shows Google Docs and Calendar access succeeded while Firestore list operations failed with `PERMISSION_DENIED`.

Why it matters:
A multi-provider assistant must not flatten failures into `Google broke` or `the assistant failed`. The exact failing boundary is the actionable product bug.

Reusable rule:
When a multi-provider assistant fails, name the exact failing provider/tool boundary and preserve successful partial work.

Supporting evidence:
- Issue #14 records that `lists.read` and `lists.add_item` failed with Firestore permission errors while Google Docs and Calendar searches succeeded in the same flow.
- The issue body explicitly routes the bug to Home Center list storage / Firestore access rather than general Google auth.

Confidence: High.

Owning skill clusters:
- AI Orchestration
- Accessibility Engineering
- Home Center project-local cluster
- Project Archaeology

Promotion status:
Promote as reusable provider-boundary failure doctrine.

## Promotion 5 - Read-to-Write Continuation Gate

Observation:
Home Center issue #15 shows the assistant found and read both source and target Google Docs, then stalled before submitting a Docs update confirmation request.

Why it matters:
This is not retrieval failure. It is a workflow continuation failure at the safety boundary. The next safe action was known and should have been requested.

Reusable rule:
After source and target reads succeed, the assistant must either request write confirmation or state the missing blocker. Silent stall is a bug.

Supporting evidence:
- Issue #15 records successful `docs.read` for `Vacation of a Lifetime Story Bible` and `Final`.
- Expected behavior in the issue is to continue and request Google Docs update confirmation unless a missing detail blocks the workflow.

Confidence: High.

Owning skill clusters:
- AI Orchestration
- Accessibility Engineering
- Project Archaeology
- Home Center project-local cluster

Promotion status:
Promote as reusable workflow-continuation doctrine.

## Promotion 6 - Software Delivery Is Shared Pain Absorption

Observation:
Availity workflow PRs #877, #879, #881, #883 and starter template PR #1 form a repeated pattern: fix platform/toolchain pain once, prove it with representative specimens, and let consumer apps inherit the repair.

Why it matters:
This crosses the threshold from isolated work churn into a reusable Software Delivery skill cluster. CI hangs, deprecated build options, CJS/ESM incompatibility, globals typing, and starter template friction are platform responsibilities when many downstream apps pay the cost.

Reusable rule:
Shared workflow maintenance becomes reusable skill when one fix prevents repeated consumer pain across many apps.

Supporting evidence:
- PR #877 fixes TypeScript-only lint hangs by allowing unmatched patterns and terminating failing processes instead of leaving hanging event-loop handles.
- PR #879 adds a `./globals` export for Vitest, jest-dom, and workflow globals.
- PR #881 replaces deprecated `advancedChunks` with `codeSplitting` and validates production build silence.
- PR #883 repairs dayjs / CJS package resolution under ESM imports and adds regression tests using `@availity/yup` avDate in example apps.
- Starter PR #1 upgrades workflow-vite, simplifies domain-heavy examples into a contact form, adds an ErrorBoundary, adds a `useSubmission` hook, and expands teaching docs.

Confidence: High.

Owning skill clusters:
- Software Delivery
- Project Archaeology
- AI Orchestration

Promotion status:
Promote Software Delivery from candidate to active cluster, with work-platform details held at the evidence/routing layer.

## Source-of-truth decisions

- Pose Lab GitHub PR #1 is canonical draft evidence for synthetic socket parity, generated clip ownership, and live visual-follow proof until merged.
- Pose Lab main becomes canonical only after PR #1 lands.
- Home Center GitHub issues #14 and #15 are canonical product-friction sources until resolved by regression and installed-path proof.
- Availity GitHub PRs are canonical for Software Delivery promotion evidence. Release PR #884 is publication/support evidence, not behavior-bearing doctrine.
- Drive reports summarize promotion sweeps; Drive skill clusters index promoted rules.
- Thunder Brainstorm is source-ref mirror only and must point back to live GitHub evidence.
- Agent Closet records promotion decisions and cross-project doctrine; it does not supersede implementation truth.

## Duplicates and false-source risks

- Do not create a new `Visual Production / Asset Tooling` top-level cluster yet. Pose Lab evidence belongs under Animation and Pose Systems, with Game Development as a use-case cluster.
- Do not merge Home Center issues #14 and #15. They share tool-host context but represent different failure classes: provider authorization failure versus continuation failure.
- Do not treat release PR #884 as behavior-bearing evidence. It is archive/supporting evidence for published workflow changes.
- Do not duplicate Software Delivery doctrine into AI Orchestration. AI Orchestration may reference it, but Software Delivery owns platform/toolchain maintenance patterns.
- Do not promote company-specific Availity implementation details beyond the generalizable platform-maintenance rule.

## Archive / merge guidance

Archive or demote:
- blind numeric offset logs after synthetic hierarchy parity exists;
- diagnostic probe outputs presented as visual acceptance;
- broad-prefix generated clip cleanup logic;
- assistant failure messages that hide the provider/tool boundary;
- release-only PR summaries with no reusable behavior change;
- domain-heavy starter examples after simpler teaching infrastructure replaces them.

Keep project-local:
- exact Meshy socket names and generated JSON/SVG artifact shapes;
- Home Center issue-specific reproduction logs and provider configuration details;
- Availity package internals, version numbers, and repository-specific release mechanics.

Promote reusable:
- Synthetic Socket Parity Before Visual Tuning;
- Generated Artifact Ownership Must Be Exact;
- Real Ready Clip Beats Probe Evidence;
- Provider-Specific Failure Attribution;
- Read-to-Write Continuation Gate;
- Software Delivery Is Shared Pain Absorption.

## Final compression

Do not tune around a missing structure.
Recreate the structure, protect the generated surfaces, prove the live visual path, then promote.

Do not say the tool failed.
Say which provider boundary failed, what already worked, what was preserved, and what the next safe action is.

Do not make every app rediscover the same platform cut.
Absorb it once, prove it with a representative specimen, and let every consumer inherit the fix.
