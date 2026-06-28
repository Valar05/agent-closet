# Discovery Promotion Record - 2026-06-28 - Terrain Grammar + Ritual Ascension + Tool Surface Hygiene

Status: Promoted / source-routed

Purpose: Preserve the reusable discoveries from Infinite Brutality terrain grammar, Prism League ritual ascension reorientation, Thunder Brainstorm source-ref behavior, and Home Center surface-hygiene evidence without letting Drive summaries or mirror docs become false source of truth.

## Reviewed artifacts

### GitHub canonical implementation sources

- `Valar05/infinite-brutality` PR #2: `[codex] Carve imperial structure terrain slice`.
- Infinite Brutality merge commit `10fe9027a1e33e701c17bb53fd6ff756e3e5193e`.
- Infinite Brutality source commits: `1577e99`, `99452fc`, `893af8d`, `687dd0e`, `10fe902`.
- `Valar05/prism-league` PR #1: `[codex] Rebuild procedural ascension voxel climb`.
- Prism League merge commit `eaacfe5bb05d453af30543fb0e1db66b74e0ef67`.
- Prism League source commits: `ece402a`, `5bf35f8`, `62fba9f`, `f09d1e1`, `2f5c664`, `4e057ca`, `ff57481`, `48bedf5`, `e7ae1cc`, `57a2579`, `eaacfe5`.
- `Valar05/thunder-brainstorm` PR #1: `Mirror Infinite Brutality terrain lessons`.
- `Valar05/home-center` issues #3, #4, #5, #6.

### Drive and mirror sources

- Drive promotion report: `Discovery Promotion Report - 2026-06-28 - Terrain Grammar + Ritual Ascension + Tool Surface Hygiene`.
- Drive skill clusters updated on 2026-06-28: Game Development, Project Archaeology, AI Orchestration, Accessibility Engineering, Writing Systems, Home Center Skill Cluster Index, and Daily Delta.
- Thunder Brainstorm source refs patched in `generated/source_refs_github/2026-06-28_terrain_ritual_tool_surface_source_refs.jsonl`.

## Promotion 1 - Function-First Terrain Grammar

Observation:
Infinite Brutality terrain work moved from generic performant rock slabs toward imperial floating strata and carved imperial structure: geology fused with roads, retaining walls, fortifications, quarry cuts, causeways, dock logic, and logistics.

Why it matters:
A procedural level that cannot explain what it is for reads as junk geometry even when the mesh is efficient. The player needs place-function before decoration.

Reusable rule:
Terrain is not scenery. Terrain is a place with a job.

Supporting evidence:
- Infinite Brutality PR #2 says the branch adds `imperial_floating_strata` and `carved_imperial_structure` terrain metadata/field routing.
- The PR replaces active proof-slice terrain away from floating islands/ramp rubble and toward carved imperial structure terrain.
- The PR body states isolated floating rocks and ramp rubble are regressions for the Napoleon proof slice.
- `docs/IMPERIAL_FLOATING_STRATA_GRAMMAR.md` defines the doctrine questions: what was built here, what fragment was seized, what function it serves, where the player moves/fights/retreats/recovers, and what silhouette names it from far away.

Confidence: High.

Owning skill clusters:
- Game Development
- Project Archaeology
- AI Orchestration, as generation-contract discipline

Promotion status:
Promote as reusable procedural terrain / level grammar doctrine.

## Promotion 2 - Collision Truth As Acceptance Gate

Observation:
Both Infinite Brutality and Prism League converged on visible geometry needing collision/support truth. Infinite Brutality validated terrain layer architecture, collision, mesh integrity, surface truth, geometry quality, and Android visual QA. Prism League replaced decorative board-wrapper assumptions with deterministic voxel/field terrain and collision extraction.

Why it matters:
When the visible route lies about support, the game trains the player not to trust the world. That is not just a bug; it is agency damage.

Reusable rule:
If the visible surface lies about support, the generator is untrustworthy.

Supporting evidence:
- Infinite Brutality PR #2 validation includes terrain-layer architecture contract, island collision contract, mesh integrity, terrain visual contract, surface truth contract, geometry quality, and Android visual QA.
- Prism League PR #1 says it generates route graph nodes/connectors, carves cells, extracts voxel-boundary surfaces for collision, and validates with `npm test` plus `npm run validate`.

Confidence: High.

Owning skill clusters:
- Game Development
- Project Archaeology
- Accessibility Engineering, where player-visible truth preserves user agency

Promotion status:
Promote as reusable game validation doctrine.

## Promotion 3 - Preserve Control Fantasy, Replace Board Fantasy

Observation:
Prism League rejected fixed pinball table framing while preserving Gasket-as-ball, aim commitment, velocity damping, release, ricochet, and physics consequence.

Why it matters:
The durable mechanic was not the pinball machine. The durable mechanic was the control fantasy: briefly arrest momentum, commit to a shot, release into consequences, and recover generously.

Reusable rule:
Preserve the control fantasy while replacing the board fantasy.

Supporting evidence:
- Prism League PR #1 replaces the fixed-layout wrapper with deterministic 2D voxel/field climb generation.
- The PR switches to a portrait vertical ascension follow camera and rocky cave/shaft terrain.
- The PR explicitly keeps anchor-chain controls and aim commitment lockout intact.

Confidence: High.

Owning skill clusters:
- Game Development
- Writing Systems, because character-as-mechanic and co-commentary remain narrative interface

Promotion status:
Promote as reusable mechanic-preservation doctrine.

## Promotion 4 - Persistent Visual QA Surface

Observation:
Recent visual/gameplay work repeatedly needed reusable review surfaces: Prism League added cloud-smoke and QA URL smoke workflows, while Infinite Brutality recorded Android visual QA with a contact sheet.

Why it matters:
Visual fixes rot into unverifiable claims when a future agent cannot reopen the same surface. Local green tests are useful; persistent review surfaces are evidence.

Reusable rule:
A visual fix is not done until the review surface can be reopened.

Supporting evidence:
- Prism League PR #1 adds cloud-smoke and `qa-url-smoke` workflows.
- The QA URL workflow accepts a persistent base URL and runs source checks, Playwright Chromium, and smoke tests against that URL.
- Infinite Brutality PR #2 records Android visual QA loading build `0.8.176` successfully with a contact sheet path.

Confidence: High.

Owning skill clusters:
- Project Archaeology
- Game Development
- Accessibility Engineering

Promotion status:
Promote as reusable visual evidence doctrine.

## Promotion 5 - Mirror Carries Routes, Not Authority

Observation:
Thunder Brainstorm continues to be useful as a mirror for source refs, skill notes, project links, and reusable discoveries, but it is explicitly dangerous if it forks active implementation truth.

Why it matters:
A mirror that stops pointing back to live evidence becomes doctrine sludge. It may look organized while silently detaching from the work.

Reusable rule:
Mirrors carry routes, not authority.

Supporting evidence:
- Thunder Brainstorm PR #1 is still open/draft and exists to mirror Infinite Brutality terrain lessons.
- The current sweep added GitHub source refs that point back to Infinite Brutality, Prism League, Thunder, and Home Center live evidence.

Confidence: High.

Owning skill clusters:
- Project Archaeology
- AI Orchestration

Promotion status:
Promote as source-of-truth governance doctrine.

## Promotion 6 - Home Center Surface Hygiene

Observation:
Home Center recent issues did not prove a new capability. They proved that assistive surfaces need fewer tool-taxonomy decisions, better mobile presentation, and stricter context-appropriate next-step routing.

Why it matters:
A blind-user assistant can have real tools and still fail if the surface makes the user manage upload/attach concepts, tolerate cramped mobile chrome, or parse irrelevant helper suggestions.

Reusable rule:
Assistive UI must not make the user manage tool taxonomy.

Supporting evidence:
- Issues #3 and #4 duplicate the unified file-intake request.
- Issue #5 records browser chrome and safe-area/footer crowding in a mobile game/surface screenshot.
- Issue #6 records irrelevant ingredient next steps leaking into a Holocron cycle answer and was closed.

Confidence: Medium-high.

Owning skill clusters:
- Accessibility Engineering
- AI Orchestration
- Project Archaeology
- Home Center project-local cluster

Promotion status:
Promote as accessibility/product-surface doctrine candidate.

## Source-of-truth decisions

- Infinite Brutality GitHub is canonical for terrain implementation, validation commands, and current Napoleon proof-slice contracts.
- Prism League GitHub is canonical for runtime ritual ascension behavior, controls, camera, tests, and QA workflows.
- Thunder Brainstorm is a source-ref and reusable-mirror layer only. It should not fork Infinite Brutality or Prism League doctrine bodies.
- Home Center GitHub issues are canonical for current product-surface bug/UX signals.
- Drive promotion reports summarize the sweep; Drive skill clusters index promoted rules; neither replaces live repo evidence.

## Duplicates and false-source risks

- Home Center issues #3 and #4 duplicate the same file-intake need. Collapse into one implementation track and keep the better acceptance criteria.
- Infinite Brutality terrain docs overlap by design: `TERRAIN_GENERATION_TECHNIQUES` is implementation inventory; `ROCK_SHAPE_GRAMMAR` is geological base grammar; `IMPERIAL_FLOATING_STRATA_GRAMMAR` is Napoleon art/design grammar; `TerrainLayer` is runtime ownership boundary.
- Thunder Brainstorm copies of full doctrine should be demoted unless they route back to live evidence.
- Marker-only Drive docs such as `HomeCenter` should remain notes until expanded into real doctrine or reports.

## Archive / merge guidance

Archive or demote:
- generic floating-rock/slab terrain directions superseded by carved imperial structure grammar;
- duplicate Home Center file-intake issue once acceptance criteria are merged;
- Thunder doctrine copies without source refs;
- marker-only Drive docs without body content.

Keep project-local:
- exact Infinite Brutality terrain implementation details and mobile budgets;
- exact Prism League control/camera implementation;
- exact Home Center issue-level remediation plans.

Promote reusable:
- Function-First Terrain Grammar;
- Collision Truth As Acceptance Gate;
- Preserve Control Fantasy, Replace Board Fantasy;
- Persistent Visual QA Surface;
- Mirror Carries Routes, Not Authority;
- Assistive UI Must Not Manage Tool Taxonomy.

## Final promoted operating rule

A generated space must have a job, a readable route, a collision truth, and a review surface.
