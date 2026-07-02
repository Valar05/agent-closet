# Discovery Promotion Record - 2026-07-02 - Home Center Red-Build Recovery + Historical Learning Map

Status: Promoted / source-routed

Purpose: Preserve reusable discoveries from late 2026-07-01 Home Center implementation commits, the red-build self-test prompt, Home Center issue #16, and the new historical documentary roadmap without allowing Drive notes or Thunder mirrors to become false source of truth.

## Reviewed artifacts

### Drive sources

- `June test prompt` (`1u20vyUKZViJR4iPv12Sxq1ecvJXXiA5x567V61-_Y0k`).
  - Role: red-build journey specification for Home Center.
  - Created/modified 2026-07-01.
- `Historical Documentary Roadmap - How We Got Here` (`1TdsCvo2104uQGG2h1G_PdGf2Re6tn9HGjsve7Viri6Q`).
  - Role: learning-map / research-curation artifact.
  - Created 2026-07-01, modified 2026-07-02.
- Existing Drive cluster indexes modified on 2026-07-01: Home Center Skill Cluster Index, AI Orchestration, Accessibility Engineering, Project Archaeology, Software Delivery, Animation and Pose Systems, and Daily Delta.

### GitHub canonical implementation sources

- `Valar05/home-center` issue #16: `Red-build self-test returned forbidden “tool plan did not converge” instead of failure details`.
- `Valar05/home-center` commit `3e8d778d4198be481a427c0e25cc56f95da43c9c`: `Fix list permissions and doc workflow planning`.
- `Valar05/home-center` commit `b3d308d3b463c3bbe56197772606f9cad59e77b3`: `Fix tool-loop convergence fallback`.
- `Valar05/home-center` files observed at those commits:
  - `tools/home_center_regression_tests.py`
  - `functions/index.js`
  - `app/src/main/java/com/dclar/homecenter/MainActivity.java`
  - `app/src/main/java/com/dclar/homecenter/HomeTaskClient.java`
  - `firebase/firestore.rules`

## Promotion 1 - Red-Build Journey As Regression Spec

Observation:
`June test prompt` defines a full user journey: read live list, add a Shipyard item, find Holocron, find Reading Log, recommend audiobooks, read two Docs, prepare a Story Bible update, and read the final response aloud. It also explicitly bans the generic phrase `tool plan did not converge` and requires concrete failure/progress/next-action reporting.

Why it matters:
This is not a unit test. It is a household-reality integration test. The system only matters if the whole journey survives provider boundaries, list storage, Drive/Docs retrieval, write confirmation, and narration. Half-success with a generic final failure is exactly the product failure this project exists to eliminate.

Reusable rule:
A red-build prompt should describe the user journey, the forbidden failure mode, the required recovery shape, and the final acceptance behavior.

Supporting evidence:
- Drive `June test prompt` steps 1-6 define the full journey and final read-aloud requirement.
- The same prompt states that failures must report exactly what failed, what succeeded before it, and the next action needed.
- Home Center issue #16 records the forbidden output after partial tool success.

Confidence: High.

Owning skill clusters:
- Accessibility Engineering
- AI Orchestration
- Home Center project-local cluster
- Project Archaeology

Promotion status:
Promote as reusable red-build / accessibility journey testing doctrine.

## Promotion 2 - Tool Loop Progress Fallback

Observation:
Home Center now guards both gateway-side and Android-side tool-loop exits against the forbidden generic convergence failure. When the loop stops, the implementation synthesizes a concrete report from toolResults: failed tool, failed message, succeeded steps, and next action.

Why it matters:
The user should not debug orchestration. When a multi-tool workflow fails, the assistant must preserve partial progress and report the next actionable boundary. This is the difference between an assistive system and a haunted call stack wearing a friendly hat.

Reusable rule:
Tool loops must carry enough progress state to produce a useful failure report without model cooperation.

Supporting evidence:
- `functions/index.js` adds `containsForbiddenToolPlanPhrase`, `toolProgressSummary`, `synthesizeToolLoopProgressReply`, and `sanitizeFinalPlannerReply`.
- `MainActivity.java` adds `finishFromToolResultsAfterLimit`, Android-side forbidden-phrase detection, and tool-result progress synthesis.
- `tools/home_center_regression_tests.py` asserts that these fallback and reporting paths exist.

Confidence: High.

Owning skill clusters:
- AI Orchestration
- Accessibility Engineering
- Home Center project-local cluster
- Project Archaeology

Promotion status:
Promote as reusable multi-tool assistant failure-recovery doctrine.

## Promotion 3 - Runtime Truth Beats Static Capability Copy

Observation:
The Android client sends available tools, unavailable tool groups, working memory, device time context, evidence context, and attachment image payloads into the gateway. Regression tests also assert that the OpenAI client sends registry-provided tools and does not hardcode the old tool list.

Why it matters:
A tool-host assistant becomes untrustworthy when it reasons from stale claims. Runtime truth must travel with the request: what tools exist now, what scopes are missing, what entity was last read, what time it is, what files/images are attached, and what evidence exists.

Reusable rule:
The planner should reason from current runtime truth, not a memorized capability list.

Supporting evidence:
- `MainActivity.java` sends available tools, unavailable groups, working memory, current time context, evidence context, and attachment images into every tool turn.
- `functions/index.js` receives tool lists, unavailable groups, working memory, evidence context, attachment images, and time context.
- Regression tests require registry-provided tool advertisement, unavailable tool groups, working memory, time context, evidence context, trace details, and no hardcoded `drive.search` tool list.

Confidence: High.

Owning skill clusters:
- AI Orchestration
- Accessibility Engineering
- Home Center project-local cluster

Promotion status:
Promote as reusable tool-host substrate doctrine.

## Promotion 4 - Permission Repair Requires Data + Rule + Bootstrap

Observation:
Home Center repaired Firestore list access by pairing list metadata and member bootstrap with Firestore rule changes. Lists now carry visibility/owner/updater metadata, read/write paths call `ensureListForAccess`, and rules allow visible household/personal repair without opening deletes.

Why it matters:
Permission failures are not fixed by randomly loosening rules. A durable fix aligns data shape, membership bootstrap, read/write paths, rule predicates, and regression checks.

Reusable rule:
Backend permission repair must update the data contract, bootstrap path, security rule, and regression test together.

Supporting evidence:
- `HomeTaskClient.java` calls `ensureListForAccess` before reads/writes and writes visibility/owner/updater metadata for list bootstrap.
- `firebase/firestore.rules` gates list visibility through `listVisibleData` / `validListWrite`, preserves membership checks, and keeps deletes disabled.
- `tools/home_center_regression_tests.py` asserts both metadata write and Firestore rule repair patterns.

Confidence: High.

Owning skill clusters:
- Accessibility Engineering
- Software Delivery
- Project Archaeology
- Home Center project-local cluster

Promotion status:
Promote as reusable backend-permission repair doctrine.

## Promotion 5 - Preference Memory Beats Repeated Shopping Search

Observation:
Home Center persists item preferences and Walmart store targets as list-scoped household memory, including canonical item names, preferred labels, SKUs, product URLs, quantities, source, confidence, and updater metadata.

Why it matters:
A grocery assistant should not rediscover the same purchase decision every week. Repeated shopping judgments should become household state with enough provenance to audit and revise.

Reusable rule:
When a repeated shopping choice is confirmed, store the canonical item, preferred label, store target, source, confidence, and updater instead of forcing future rediscovery.

Supporting evidence:
- `HomeTaskClient.java` implements `savePreference`, `saveStoreTarget`, `parseStoreTargetSpec`, `readPreferences`, and display-name resolution from `itemPreferences`.
- The same file stores `storeTargets` with SKU/product URL/product name/quantity/source/confidence metadata.

Confidence: Medium-high. Strong for Home Center; broader reusable doctrine should wait for another shopping/import workflow specimen.

Owning skill clusters:
- Accessibility Engineering
- Home Center project-local cluster
- Project Archaeology

Promotion status:
Promote inside Home Center; hold cross-project promotion until repeated outside grocery/shopping workflows.

## Promotion 6 - Documentary Roadmap As Cause-Effect Learning Graph

Observation:
The historical documentary roadmap is organized around causal comprehension rather than strict chronology. It includes a main path, an immediate interest detour, a taste marker, a no-retread rule, non-canonical drama bin, and a return path.

Why it matters:
This is a reusable learning pattern: follow curiosity without letting it destroy the curriculum. The detour is allowed, bounded, documented, and connected back to the larger map.

Reusable rule:
A learning roadmap should preserve curiosity by naming the detour, recording taste signal, banning low-value retreads, separating canonical sources from drama/fiction, and defining the return path.

Supporting evidence:
- The roadmap states the purpose: build intuitive modern-world understanding by following cause-and-effect rather than strict chronology.
- The Soviet submarine detour defines documented-history rules, a through-line, watch order, taste marker, no-retread rule, non-canonical/drama bin, detour takeaway, and return path.

Confidence: Medium. Strong as a personal learning artifact; candidate reusable doctrine until repeated across other learning maps.

Owning skill clusters:
- Project Archaeology
- AI Orchestration
- Candidate: Learning Systems / Research Curation

Promotion status:
Keep project-local / candidate. Do not create a new top-level cluster from one roadmap.

## Source-of-truth decisions

- Home Center GitHub is canonical for issue #16, Firestore/list permission repair, tool-loop fallback, runtime capability truth, working-memory/time-context plumbing, and regression tests.
- `June test prompt` is canonical as the red-build journey spec because it is a Drive-native test prompt, but implementation proof lives in Home Center GitHub.
- `Historical Documentary Roadmap - How We Got Here` remains Drive-native personal learning evidence. It is not a GitHub project artifact.
- Thunder Brainstorm is source-ref mirror only and must point back to live GitHub/Drive evidence.
- Agent Closet records the promotion decision and cross-project doctrine; it does not supersede Home Center implementation truth.
- Drive reports summarize promotion sweeps; Drive skill clusters index promoted rules.

## Duplicates and false-source risks

- Issue #16 overlaps with issues #7, #12, and #13, but it is not a duplicate. It captures the red-build journey failing after prior fixes and should remain open until the installed path proves the full journey.
- Tool-loop progress fallback is related to Provider-Specific Failure Attribution and Read-to-Write Continuation Gate, but it owns a different layer: failure reporting after orchestration stalls.
- Do not let `June test prompt` become a vague QA note. Treat it as a named red-build spec.
- Do not create a new Learning Systems cluster yet. The documentary roadmap is a strong candidate pattern, not enough cluster mass.

## Archive / merge guidance

Archive or demote:
- screenshots or notes showing only the forbidden generic failure message once issue #16 and the fallback implementation are linked;
- Drive mirrors that restate Home Center fixes without commit/issue links;
- stale capability descriptions that omit runtime unavailable groups or continue to hardcode old Google tool sets;
- documentary recommendations that do not distinguish documented history from docudrama/fiction.

Keep project-local:
- exact Firebase collection/rule shape;
- exact Home Center regression-test strings;
- the current Soviet submarine watch order;
- the `June test prompt` body as a concrete red-build specimen.

Promote reusable:
- Red-Build Journey As Regression Spec;
- Tool Loop Progress Fallback;
- Runtime Truth Beats Static Capability Copy;
- Permission Repair Requires Data + Rule + Bootstrap.

Promote as candidate / local:
- Preference Memory Beats Repeated Shopping Search;
- Documentary Roadmap As Cause-Effect Learning Graph.

## Final compression

Do not make the user debug the orchestra.
Preserve runtime truth, preserve partial progress, and say the exact next repair boundary.

Do not loosen permissions blindly.
Repair the data contract, the bootstrap path, the rule, and the regression together.

Do not let curiosity wreck the learning map.
Name the detour, preserve the taste signal, and define the road back.
