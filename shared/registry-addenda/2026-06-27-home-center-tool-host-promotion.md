# Discovery Promotion Record - 2026-06-27 - Home Center Tool Host + Holding Vigil Military Reality

Status: Promoted / source-routed

Purpose: Preserve the reusable discoveries from the Home Center tool-host work and the Holding Vigil military-reality extraction without letting Drive summaries, Thunder mirrors, or stale troubleshooting notes become false source of truth.

## Reviewed artifacts

### GitHub canonical implementation sources

- Home Center recent commits: `5e10773`, `dbafd46`, `c52ce34`, `0ef9752`, `1f29a9f`, `2693b15`, `c73cd27`, `d1fa42f`.
- `Valar05/home-center` live repo.
- `README.md`.
- `docs/CURRENT_TROUBLESHOOTING_STATE.md`.
- `docs/AGENT_CONTRACT.md`.
- `app/src/main/java/com/dclar/homecenter/ToolRegistry.java`.
- `app/src/main/java/com/dclar/homecenter/OpenAiAgentClient.java`.
- `app/src/main/java/com/dclar/homecenter/GoogleDriveClient.java`.
- `app/src/main/java/com/dclar/homecenter/GoogleGmailClient.java`.
- `app/src/main/java/com/dclar/homecenter/GoogleCalendarClient.java`.
- `app/src/main/java/com/dclar/homecenter/MainActivity.java`.
- `functions/index.js`.
- `tools/home_center_regression_tests.py`.

### Drive canonical writing source

- Holding Vigil - Corpus Mining Pass 1
- Pass 2 - Institution Extraction
- Pass 3 - Military Reality Extraction

### Mirror / registry destinations

- Thunder Brainstorm generated source refs.
- Drive promotion report.
- Drive skill cluster docs.

## Promotion 1 - Home Center GPT-Directed Tool Host

Observation:
Home Center is no longer just a command parser or Android utility shell. The current implementation moves toward a GPT-directed tool host: GPT decides intent, requests registry-advertised tools, and Android executes those tools through scoped clients.

Why it matters:
A blind-user assistant cannot depend on admin surfaces, debug menus, local proxy rituals, or fake provider status. It needs a simple surface that asks for Google sign-in, knows which tools are available, routes natural requests through a reasoning layer, and executes real provider actions only when permitted.

Reusable rule:
The model thinks. The app is the hands. The hands must be scoped, registered, confirmed, dispatched, and tested.

Supporting evidence:
- Home Center commit sequence shows the work moved from Drive diagnostic repair into GPT-directed tool-host implementation.
- `ToolRegistry.java` defines Drive, Docs, Gmail, Calendar, and list tool capabilities with scopes, write flags, confirmation requirements, and argument lists.
- `OpenAiAgentClient.java` sends available tools, unavailable groups, tool results, transcript, and summary to the gateway.
- `functions/index.js` instructs the planner to request available tools instead of saying it cannot do the work, while hiding plumbing from the user.
- `MainActivity.java` keeps secondary controls available while preserving the main voice-first chat surface.
- `tools/home_center_regression_tests.py` enforces the registry, dispatch, confirmation, and stale-router invariants.

Confidence: High.

Owning skill clusters:
- Accessibility Engineering
- AI Orchestration
- Project Archaeology
- Software Delivery / Work Platform candidate
- Home Center project-local cluster

Promotion status:
Promote as reusable product/agent doctrine candidate.

## Promotion 2 - Capability Registry Contract

Observation:
Home Center now treats tool availability as a registry contract rather than scattered prompt text or local routing heuristics.

Why it matters:
Hardcoded capability claims rot immediately. A registry gives the assistant a current machine-readable view of what it can do, what requires scopes, what requires confirmation, and what is unavailable.

Reusable rule:
A capability exists only when it is registered, scoped, advertised, dispatched, and covered by a regression test.

Supporting evidence:
- `ToolRegistry.allTools()` enumerates every allowed tool.
- `ToolRegistry.availableTools()` and `unavailableToolGroups()` derive runtime tool availability from Google account scopes and Home Center sign-in state.
- `ToolRegistry.signInScopes()` centralizes Google sign-in scope requests.
- The regression harness compares the exact expected tool set with the registry and verifies dispatch coverage across Drive, Gmail, Calendar, and list clients.

Confidence: High.

Owning skill clusters:
- AI Orchestration
- Accessibility Engineering
- Project Archaeology
- Software Delivery / Work Platform candidate

Promotion status:
Promote as reusable agent/platform doctrine.

## Promotion 3 - Confirmation-Gated Writes

Observation:
The gateway and Android executor both participate in write safety. The planner may request dangerous tools, but confirmation is enforced outside prompt prose and marked mechanically before Android execution.

Why it matters:
Prompt obedience is not a permission system. A real assistant touching Drive, Gmail, Calendar, or shared household lists must prevent accidental writes and sends even if the model gets overconfident.

Reusable rule:
Dangerous writes require executor-side confirmation gates, not just model-side caution.

Supporting evidence:
- Tool definitions include `write` and `confirmationRequired` flags.
- `functions/index.js` refuses confirmation-required tools unless the user confirms, then injects `_confirmedByGateway`.
- `tools/home_center_regression_tests.py` requires both `definition.confirmationRequired` handling and `_confirmedByGateway` checks.
- The registry intentionally excludes destructive delete tools such as Drive, Gmail, Calendar, and list delete operations.

Confidence: High.

Owning skill clusters:
- Accessibility Engineering
- AI Orchestration
- Software Delivery / Work Platform candidate

Promotion status:
Promote as reusable safety/agent-execution doctrine.

## Promotion 4 - Provider Truth Probe

Observation:
Home Center's troubleshooting work made a hard distinction between identity, claimed capability, and real provider access. Firebase sign-in proves identity; it does not prove Drive access. Drive status must be probed against Google APIs.

Why it matters:
An assistant that tells a blind user it can access Drive when it cannot has removed agency and created emotional harm. Capability truth must come from provider probes, not model guesses.

Reusable rule:
Capability status must be probed against the provider. Never let the answer model claim access from vibes.

Supporting evidence:
- `docs/CURRENT_TROUBLESHOOTING_STATE.md` records the correction that Firebase sign-in is not Google automation.
- The same doc states that Drive questions should not go to GPT and produce guesses.
- `googleDriveProbe` checks Google Drive through the API and returns connected, missing, insufficient-scope, or failure states.
- Android's `Check Google Drive` action performs direct Drive validation.

Confidence: High.

Owning skill clusters:
- Accessibility Engineering
- AI Orchestration
- Project Archaeology
- Home Center project-local cluster

Promotion status:
Promote as reusable accessibility/product doctrine.

## Promotion 5 - Installed Artifact Freshness Gate

Observation:
The active red state separated source/provider success from installed-app success. Source green did not mean the phone was running the new APK.

Why it matters:
For mobile accessibility tools, the thing that matters is the installed user path. A green build that never reached the user's phone is a lie with a prettier hat.

Reusable rule:
Source green is not product green. Installed-app validation must fail fast on stale runtime versions.

Supporting evidence:
- `docs/CURRENT_TROUBLESHOOTING_STATE.md` records stale APK failure and explicitly warns not to judge current source behavior from an old installed build.
- The user-path smoke requires runtime version markers and reports `installedBuildIsStale`, `runtimeVersionMatches`, and `installedBuildFreshEnoughForBehaviorAssertions`.
- The README preserves APK build, export, and smoke-check commands.

Confidence: High.

Owning skill clusters:
- Accessibility Engineering
- Project Archaeology
- Software Delivery / Work Platform candidate

Promotion status:
Promote as reusable delivery validation doctrine.

## Promotion 6 - Holding Vigil Military Reality Chain

Observation:
Holding Vigil's Pass 3 reframed military realism away from weapons and toward authority, responsibility, reporting, consequences, accountability gaps, blame, protection, and paperwork. The dramatic engine is the mismatch among authority, competence, information, and responsibility.

Why it matters:
This strengthens the institution-first rewrite approach. It also generalizes beyond Holding Vigil into writing systems: believable institutions are not made by jargon; they are made by how responsibility moves after harm occurs.

Reusable rule:
In institutional scenes, ask who has authority, who has competence, who has information, and who has responsibility. Those four answers should rarely be the same person.

Supporting evidence:
- Holding Vigil - Corpus Mining Pass 1 defines the manuscript as a corpus extraction project before rewrite.
- Pass 2 defines Paradise as a mature institution built by incentives, with Paradise abstracting and Lexen restoring concrete human detail.
- Pass 3 defines the reporting chain and military/security reality patterns: Useful People Become Traps, Report Drift, Four Versions of Every Event, and Accountability Gradient.

Confidence: Medium-high.

Owning skill clusters:
- Writing Systems
- Project Archaeology

Promotion status:
Promote as project-local writing doctrine candidate. Do not treat as universal doctrine until cross-corpus evidence confirms recurrence.

## Source-of-truth decisions

- Home Center GitHub repository is canonical for implementation, tests, tool registry, provider routing, and mobile validation.
- Home Center Drive cluster/index docs are registry and planning mirrors, not implementation truth.
- Thunder Brainstorm is a reusable source-reference mirror only. It should point back to Home Center live GitHub evidence and should not fork Home Center doctrine.
- Agent Closet registry addenda preserve the promotion decision and cross-cluster rules; they are not implementation sources.
- Holding Vigil Drive doc remains canonical for Holding Vigil mining until imported into Agent Closet fiction corpus.
- Drive promotion reports summarize sweeps and source-of-truth decisions; they are not a substitute for live GitHub tests or Drive-native writing docs.

## Duplicates and false-source risks

- Legacy Drive diagnostic notes and hosted Google probe notes should merge under Provider Truth Probe rather than becoming separate doctrines.
- Old Drive-readonly or Drive-file-only assumptions are superseded by the current full Drive + Docs tool-host scope model.
- Cartesia proxy setup instructions are project-local troubleshooting evidence; the promoted doctrine is Hosted Provider Reality, not "run a local proxy".
- Netrunner remains a Home Center adjacent surface, not the canonical Home Center tool-host doctrine.
- Shattered Bonds Dorian files remain under the prior evidence-gate hold; no new promotion from those duplicates in this sweep.

## Archive / merge guidance

Archive or demote:
- stale status docs that claim source green equals user-path green;
- Drive mirrors that do not point back to live Home Center GitHub evidence;
- prompt-only tool capability claims not backed by registry, dispatcher, and tests.

Merge into reusable doctrine:
- capability registry contract;
- confirmation-gated writes;
- provider truth probe;
- installed artifact freshness gate;
- model-thinks/app-hands execution split.

Keep project-local:
- exact Home Center scopes and Android implementation details;
- Firebase deployment details;
- Cartesia proxy implementation;
- Holding Vigil Pass 3 until fiction corpus import and cross-corpus validation.

## Final promoted operating rule

A personal assistant becomes trustworthy when every claimed capability has a live provider proof, a scoped executor, a confirmation boundary for writes, and an installed-user-path test.
