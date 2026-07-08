# Discovery Promotion Record - 2026-07-08 - Storage Intent + Cloud Pixels + Pose Authoring Controls

Status: promoted / routed

## Reviewed artifacts

- Home Center commit `f7708242680cbf7d087ddd5ccc80d85138f999e4` - `Expose storage tools for reading log updates`.
- Pose Lab V2 commit `0b0e89860674cb44f569e06f6e2b814c3ae9f482` - `Expose fist controls and clip selection`.
- Tanks for the Memories commits `865b98d4fb352667e7162c7ad1fab1460fe26241`, `b5b9c1fd7f9be2c244dd931a2149c94d9829fc64`, and `00cb2735563206eda0e2064229131ee4f025a399` - cloud pixel workflow registration and Playwright repair.
- Availity/sdk-js PR #1018 - merged documentation update.
- Availity/sdk-js PR #1020 - open Dependabot `js-yaml` security bump.
- Drive promotion / cluster documents modified in the prior run were treated as mirror/index evidence, not new source-of-truth discoveries.

## Promoted discoveries

### 1. Storage Intent Must Expose Storage Tools

Observation: Home Center now recognizes reading-log, review, rating, score, and grade language as durable storage intent and exposes Drive, Docs, and Knowledge before planner selection. Regression tests enforce the routing and explicitly block manual-only log entries while storage tools are available.

Why it matters: The user should not have to debug why a reading-log request turned into advice. If the requested artifact is durable state, the tool palette must expose state-changing tools before the model plans.

Reusable rule: When the user asks to update, append, log, record, score, grade, or review a durable record, classify it as storage-write intent first. Expose the relevant storage tools before planner execution. Manual text is a fallback only when no write path is available.

Canonical evidence:

- https://github.com/Valar05/home-center/commit/f7708242680cbf7d087ddd5ccc80d85138f999e4
- https://github.com/Valar05/home-center/blob/f7708242680cbf7d087ddd5ccc80d85138f999e4/functions/index.js
- https://github.com/Valar05/home-center/blob/f7708242680cbf7d087ddd5ccc80d85138f999e4/tools/home_center_regression_tests.py

Confidence: High. Implementation and regression coverage both exist.

Owning clusters: Home Center Skill Cluster Index, AI Orchestration, Accessibility Engineering, Project Archaeology.

### 2. Pose Authoring Controls Are Evidence Handles

Observation: Pose Lab V2 now exposes clip selection, attack playback, scrubber, prime keys, save-key and export controls, fist visual review routing, and FPV-editable FistReady state. Smoke coverage preserves quarantine, explicit bake/review scripts, and review URL boundaries.

Why it matters: Pose work cannot stay as invisible generated math. The reviewer needs handles that make the candidate observable, editable, reversible, and exportable before any animation is promoted.

Reusable rule: A pose candidate is not promotion-ready until the review surface exposes the clip, time, prime keys, visible reference overlays, save/export path, and quarantine/provenance tests.

Canonical evidence:

- https://github.com/Valar05/pose-lab-v2/commit/0b0e89860674cb44f569e06f6e2b814c3ae9f482
- https://github.com/Valar05/pose-lab-v2/blob/0b0e89860674cb44f569e06f6e2b814c3ae9f482/src/main.js
- https://github.com/Valar05/pose-lab-v2/blob/0b0e89860674cb44f569e06f6e2b814c3ae9f482/scripts/smoke.mjs

Confidence: High for authoring-surface existence; Medium for final animation quality until hosted visual review accepts a candidate.

Owning clusters: Animation and Pose Systems, Game Development, Project Archaeology.

### 3. Cloud Pixels as Hosted Visual Evidence

Observation: Tanks for the Memories now has a manually dispatched GitHub Actions workflow that captures cloud-rendered page pixels from a live URL, supports named material-debug variants, installs Playwright/Chromium in CI, and uploads screenshot artifacts.

Why it matters: Phone screenshots and chat descriptions are not durable visual evidence. Hosted visual truth needs a repo-owned workflow that can be rerun and attached as artifacts.

Reusable rule: If acceptance depends on hosted rendering, the repo must own the capture workflow: target URL, wait budget, named variants, browser setup, and uploaded artifacts. Browser install fixes belong in the workflow, not in operator memory.

Canonical evidence:

- https://github.com/Valar05/tanks-for-the-memories/commit/865b98d4fb352667e7162c7ad1fab1460fe26241
- https://github.com/Valar05/tanks-for-the-memories/commit/b5b9c1fd7f9be2c244dd931a2149c94d9829fc64
- https://github.com/Valar05/tanks-for-the-memories/commit/00cb2735563206eda0e2064229131ee4f025a399
- https://github.com/Valar05/tanks-for-the-memories/blob/00cb2735563206eda0e2064229131ee4f025a399/.github/workflows/cloud-pixels.yml

Confidence: High for workflow existence; Medium for asset acceptance until a successful artifact run is linked.

Owning clusters: Game Development, Project Archaeology, AI Orchestration.

### 4. API Defaults Are Routing Contracts

Observation: Availity/sdk-js PR #1018 turns thin AvMicroserviceApi documentation into explicit default configuration, URL pattern, usage example, when-to-use guidance, and full URL override behavior.

Why it matters: Shared platform SDK behavior becomes safer when implicit routing defaults are documented where consumers actually look. This prevents every app team from rediscovering path/version/cache/polling behavior by failure.

Reusable rule: In shared SDKs, document defaults as routing contracts: base path, version behavior, cache/polling defaults, method expectations, override behavior, and examples.

Canonical evidence:

- https://github.com/Availity/sdk-js/pull/1018
- https://github.com/Availity/sdk-js/blob/60cec1b737b7a07f6705ad5f40808efc678ee996/docusaurus/docs/api/getting-started.md

Confidence: High. PR is merged and doc surface is explicit.

Owning clusters: Software Delivery, Project Archaeology.

## Held / project-local discoveries

### Dependency Security PRs Are Watch Items Until Merged

Observation: Availity/sdk-js PR #1020 is an open Dependabot bump from `js-yaml` 3.14.2 to 3.15.0 with a security backport around `maxTotalMergeKeys`.

Why held: This is active Software Delivery evidence but not a new doctrine promotion until it is reviewed/merged or creates a reusable dependency policy finding.

Canonical evidence:

- https://github.com/Availity/sdk-js/pull/1020

Confidence: Medium. Open and mergeable, but not merged.

Owning clusters: Software Delivery.

## Source-of-truth and mirror decisions

- Home Center GitHub is canonical for reading-log storage routing, planner palette, and regression tests.
- Pose Lab V2 GitHub is canonical for authoring controls, candidate quarantine, smoke contracts, and visual-review tooling.
- Tanks for the Memories GitHub is canonical for cloud-pixel capture workflow and visual artifact generation.
- Availity/sdk-js PRs are canonical Software Delivery evidence for SDK documentation and dependency hygiene.
- Drive promotion reports and skill clusters are summary/index layers.
- Thunder Brainstorm carries source routes only; it must not become doctrine authority.

## Duplicate / archive calls

- Do not re-promote the July 7 creative finalizer work. Today's Home Center promotion is storage-intent exposure, not creative-output delivery.
- Do not re-promote Visual Truth Authority wholesale. Cloud Pixels is a concrete workflow implementation under that parent doctrine.
- Keep Pose Lab candidate quality separate from Pose Lab authoring-surface capability. Controls exist; accepted animation still requires hosted visual review.
- Keep Availity PR #1020 as a watch item, not a promoted rule, until merged or used as reusable dependency-governance evidence.

## Final compression

Storage intent must expose storage tools.
Visual truth must leave artifacts.
Pose candidates need handles before judgment.
Shared SDK defaults are routing contracts, not trivia.
