# Discovery Promotion Record - 2026-06-29 - Home Center Local Knowledge + Infinite Brutality Foundry

Status: Promoted / source-routed

Purpose: Preserve reusable discoveries from late 2026-06-28 Home Center capability hardening and Infinite Brutality foundry/material work without letting Drive reports or Thunder mirrors become false source of truth.

## Reviewed artifacts

### GitHub canonical implementation sources

- `Valar05/home-center` compare `096131d3..cf7ce057`: three commits after the previous promotion sweep.
  - `50477831ef71907b1e8182c63aa393a0dca1f5c1` - Recover tool loops and harden narration.
  - `8ba5fb5aabe91f9d45bf757da68f78638a509ea8` - Fix Firebase Functions deploy from Termux.
  - `cf7ce05722aedf200d3009f55f4105ba1ab82147` - Add local knowledge tools.
- `Valar05/home-center` issues #7-#13, especially #12 and #13, as canonical product-friction evidence.
- `Valar05/infinite-brutality` compare `b87c2784..e4d6e5b`: foundry district assembly, material provenance, runtime PBR manifest, collision/walkability tests, assembly workbench, and `ib_doctor` tooling.
- `Valar05/infinite-brutality` docs:
  - `docs/DEEP_OCEAN_TOOL_NEEDS.md`
  - `docs/TOOL_FIRST_ENGINEERING_DOCTRINE.md`
  - `docs/LEVEL_DESIGN_WORKFLOW.md`

### Drive and mirror sources

- Prior Drive report: `Discovery Promotion Report - 2026-06-28 - Terrain Grammar + Ritual Ascension + Tool Surface Hygiene`.
- Drive cluster indexes patched on 2026-06-29: AI Orchestration, Project Archaeology, Game Development, Accessibility Engineering, Home Center Skill Cluster Index, and Daily Delta.
- Thunder Brainstorm source refs patched in `generated/source_refs_github/2026-06-29_home_center_foundry_source_refs.jsonl`.

## Promotion 1 - Local Knowledge As App-Private Memory Layer

Observation:
Home Center added `knowledge.read` and `knowledge.append`, backed by app-private files seeded as `SKILLS.md`, `AGENTS.md`, and `MEMORY.md`. The tool contract marks them as local tools with no cloud scopes, and the Android dispatcher routes the knowledge group to `LocalKnowledgeClient`.

Why it matters:
A life-operations assistant cannot depend only on transient chat history, cloud docs, or remote memory. Some steering notes, repeated procedures, and durable local facts need a low-friction, app-private capture layer that is close to execution.

Reusable rule:
Local memory should be file-scoped by purpose: repeatable procedures, agent steering, and durable facts are different storage lanes.

Supporting evidence:
- `LocalKnowledgeClient` creates `home_center_knowledge`, seeds `SKILLS.md`, `AGENTS.md`, and `MEMORY.md`, caps read/append size, rejects obvious secrets, and canonicalizes allowed file names.
- `home_center_tool_contract.json` registers `knowledge.read` and `knowledge.append` under the `knowledge` group with no cloud scopes.
- `MainActivity` dispatches the `knowledge` group through `LocalKnowledgeClient` and records the last local knowledge file in working memory.
- `tools/home_center_regression_tests.py` requires local knowledge registration, dispatch, seeds, app-private storage, sensitive-content rejection, and planner steering.

Confidence: High.

Owning skill clusters:
- AI Orchestration
- Accessibility Engineering
- Project Archaeology
- Home Center project-local cluster

Promotion status:
Promote as reusable personal-assistant memory-boundary doctrine.

## Promotion 2 - Tool Failure Must Translate To User Problem

Observation:
Home Center issues #12 and #13 show the same user-visible failure mode: the system surfaced `tool plan did not converge` after useful tool work or repeated malformed retries instead of explaining the actual problem and next step.

Why it matters:
Internal planner terminology steals agency from the user. A blind or overloaded user does not need a tool-loop postmortem; they need the concrete failed action, the cause, what still happened, and what to do next.

Reusable rule:
Never expose orchestration failure jargon when a plain-English cause and next action are available.

Supporting evidence:
- Issue #13 records a direct user complaint that Home Center should stop saying `tool plan did not converge` and explain the actual problem.
- Issue #12 records a Drive move retry loop where invalid extra fields were sent repeatedly, then hidden behind convergence failure.
- `MainActivity` contains explicit tool-loop recovery copy that tries to return a final answer or asks the user to repeat only the missing last step.
- Regression tests require blocking raw tool-call JSON from chat/narration and preventing malformed tool JSON parse failures from surfacing raw planner artifacts.

Confidence: High.

Owning skill clusters:
- Accessibility Engineering
- AI Orchestration
- Project Archaeology

Promotion status:
Promote as user-facing failure-boundary doctrine.

## Promotion 3 - Tool Contract Coverage Is The Trust Boundary

Observation:
Home Center now tests tool registry, JSON contract, dispatchers, scopes, write confirmation, forbidden delete tools, Google reconnect behavior, working memory, evidence context, GitHub issue reporting, local knowledge, and installed conversation state in one regression harness.

Why it matters:
The assistant becomes trustworthy only when claimed capabilities are contract-visible, dispatcher-backed, scoped, confirmed when dangerous, and regression-tested. Prompt steering alone is not enough.

Reusable rule:
A tool exists only when registry, dispatcher, scopes, confirmation policy, and regression tests agree.

Supporting evidence:
- `home_center_tool_contract.json` enumerates Drive, Docs, Sheets, Gmail, Calendar, Contacts, Lists, Knowledge, and GitHub issue tools with operation/write/confirmation metadata.
- `tools/home_center_regression_tests.py` checks registry/contract equality, dispatcher presence for every registered tool, external write confirmation, forbidden delete tools, scope wiring, working memory, evidence context, and reconnect copy.
- `MainActivity` rejects registered tools requiring confirmation unless `_confirmedByGateway` is present.

Confidence: High.

Owning skill clusters:
- AI Orchestration
- Accessibility Engineering
- Project Archaeology

Promotion status:
Promote as reusable tool-host validation doctrine.

## Promotion 4 - Material Provenance Before Runtime Approval

Observation:
Infinite Brutality moved material work from placeholder/procedural mush toward source albedos/emissive masks, derived PBR channels, manifest entries, cache-bust tokens, runtime approval flags, and tests.

Why it matters:
Procedural derivation can produce useful technical maps, but final art identity cannot be faked by local scripts. Runtime needs to know whether a material is approved source art or still placeholder sludge.

Reusable rule:
Source art is provenance; derived maps are tooling; runtime approval is explicit state.

Supporting evidence:
- `docs/DEEP_OCEAN_TOOL_NEEDS.md` says runtime material art must come from real image sources, local scripts may derive technical channels, manifest entries are not enough, and runtime material entries need `runtimeApproved: true`.
- `docs/TOOL_FIRST_ENGINEERING_DOCTRINE.md` says not to ship locally synthesized placeholder art as final art direction and to use OpenAI or another real texture source for albedo/emissive art.
- The Infinite Brutality compare added a PBR material manifest, source generated texture inputs, runtime textures, material preview images, `derive_ib_pbr_from_albedo.py`, and `test_material_manifest_contract.mjs`.

Confidence: High.

Owning skill clusters:
- Game Development
- Project Archaeology
- AI Orchestration

Promotion status:
Promote as reusable art-pipeline/provenance doctrine.

## Promotion 5 - Walkability First, Collision Classification Second, Screenshot Third

Observation:
Infinite Brutality foundry work refined the previous collision-truth rule. Build `0.8.208` made player walkability the first district assembly contract. Build `0.8.209` corrected the blind spot: walkability tests alone do not prove visible collision truth, so visible assemblies need explicit collider classification.

Why it matters:
A generated district can look supported and still fail traversal. It can also pass broad walkability while invisible or inappropriate colliders damage movement. The route contract must precede machinery, supports, skyline, and screenshot polish.

Reusable rule:
Build the player route first; classify every visible part as player, solid, none, or explicit decorative exemption; only then count the screenshot.

Supporting evidence:
- `docs/LEVEL_DESIGN_WORKFLOW.md` records the district assembly correction, walkability-first correction, and explicit visible collision truth correction for builds `0.8.205`, `0.8.208`, and `0.8.209`.
- `docs/DEEP_OCEAN_TOOL_NEEDS.md` says visible architecture needs collision by default and every visible part must declare `player`, `solid`, or an explicit exemption.
- The Infinite Brutality compare added `test_district_assembly_contract.mjs`, `test_district_walkability_contract.mjs`, `test_foundry_invisible_collider_contract.mjs`, `test_player_walkability_route_contract.mjs`, and related district assembly emitters/planners.

Confidence: High.

Owning skill clusters:
- Game Development
- Accessibility Engineering, as agency/trust surface
- Project Archaeology

Promotion status:
Promote as reusable procedural level validation doctrine.

## Promotion 6 - Workbench Before Full Runtime

Observation:
Infinite Brutality added `tools/assembly_workbench.html` and `tools/ib_doctor.sh` alongside foundry assembly emitters and contracts.

Why it matters:
Full game boot is too heavy for every design iteration. The right review surface is the smallest surface that reveals the failure: top-down assembly review for shape/route/silhouette, doctor script for cache/server/contract drift, full runtime only when needed.

Reusable rule:
Create the smallest review surface that can catch the current class of failure before booting the whole product.

Supporting evidence:
- `docs/LEVEL_DESIGN_WORKFLOW.md` instructs future agents to use `assembly_workbench.html` for fast top-down assembly review before the full game and `ib_doctor.sh` before handoff to catch cache-bust drift, stale server state, and broken district contracts.
- The Infinite Brutality compare added both tools plus new district assembly contracts.

Confidence: Medium-high.

Owning skill clusters:
- Project Archaeology
- Game Development
- AI Orchestration

Promotion status:
Promote as review-surface / validation-loop doctrine candidate.

## Source-of-truth decisions

- Home Center GitHub is canonical for tool contract, local knowledge implementation, regression tests, deployment scripts, issue evidence, and installed app behavior.
- Home Center issues #12 and #13 are canonical for the current failure-message UX bug class until fixed and closed.
- Infinite Brutality GitHub is canonical for foundry implementation, material pipeline, collision/walkability contracts, and current build notes.
- Thunder Brainstorm is a source-ref and reusable-mirror layer only. It carries routes back to live GitHub evidence.
- Drive reports summarize the sweep; Drive skill clusters index promoted rules. Neither replaces live repo evidence.

## Duplicates and false-source risks

- Do not create a second Home Center memory doctrine that ignores the existing capability registry and confirmation-gated tool host record. Local knowledge is an extension of that tool-host doctrine.
- Do not duplicate `Collision Truth As Acceptance Gate`; refine it with explicit collider classification and walkability-first district assembly.
- Do not treat `docs/DEEP_OCEAN_TOOL_NEEDS.md` as general doctrine by itself. Its reusable pieces are material provenance, runtime approval state, and missing-tool audit.
- Keep Termux/Firebase deploy fixes project-local unless the same mobile-deploy failure appears in another repo.
- Keep exact PBR material IDs, foundry build numbers, and asset paths project-local.

## Archive / merge guidance

Archive or demote:
- notes that say `source green` or screenshot green is enough without installed/runtime validation;
- Home Center error reports that only preserve planner jargon and not user-visible cause;
- material docs that treat locally derived placeholder art as final art;
- old foundry/floating-rock directions superseded by walkable foundry assembly routes.

Keep project-local:
- Home Center Android/Firebase deployment mechanics;
- exact Home Center tool list and Java dispatch implementation;
- Infinite Brutality material IDs, texture manifests, and foundry assembly parameters.

Promote reusable:
- Local Knowledge As App-Private Memory Layer;
- Tool Failure Must Translate To User Problem;
- Tool Contract Coverage Is The Trust Boundary;
- Material Provenance Before Runtime Approval;
- Walkability First, Collision Classification Second, Screenshot Third;
- Workbench Before Full Runtime.

## Final promoted operating rule

A claimed assistant capability is not real until it has the right memory lane, a visible contract, a dispatcher, a recovery path, and a test that proves the user does not have to debug the machine.
