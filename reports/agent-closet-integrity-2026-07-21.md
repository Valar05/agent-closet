# Agent Closet Integrity Report — 2026-07-21

Type: Repository integrity review  
Status: Active findings  
Owner: Quartermaster  
Verification owner: Auditor  
Scope: `Valar05/agent-closet` on `main` at `5c4e82365fe75c09715e272a47be1c111b4dc60d`

## Executive verdict

Overall health: **Yellow**.

The July 14 repository-map repair materially improved orientation. `steering.md`, hazards, factories, reports, tools, and legacy roots are now reachable from the bootstrap route. Prompt Hydraulics also provides a good positive example of a promoted skill with an owner, input/output contract, failure modes, acceptance tests, and explicit proof debt.

The limiting defects remain authority and disposition:

- agent status still conflicts across current manifests and indexes;
- promoted doctrine still lives under three active-looking roots;
- scratch mixes candidates, promoted items, proof debt, and archaeology;
- ownership metadata is not required by the doctrine schema;
- open doctrine PRs remain drafts without a recorded disposition;
- repository-wide link, orphan, duplicate, owner, and status validation is still absent.

No new mainline commit after Prompt Hydraulics on July 15 resolves those findings.

## Integrity summary

| Area | Verdict | Highest-value defect |
|---|---|---|
| Broken links | Yellow-green | No confirmed broken ordinary Markdown links in the audited bootstrap path; repository-wide proof is absent. |
| Duplicate doctrine | Red-yellow | Three doctrine roots and exact semantic duplication remain active-looking. |
| Orphaned files | Yellow | Several valuable lineage and origin files still lack durable inbound retrieval paths. |
| Scratch disposition | Red-yellow | The ore queue contradicts its own anti-graveyard rule. |
| Retrieval paths | Yellow | The repository map improved, but doctrine, agent, and skill authority remain split and stale. |
| Ownership | Red-yellow | Templates and registries do not require implementation and verification ownership. |
| Promotion queue | Yellow | Good candidates exist, but four open doctrine PRs and several ore entries lack disposition. |

## 1. Broken-link and portability verdict

### Confirmed

No broken ordinary relative Markdown link was confirmed in the current bootstrap route:

- `README.md`
- `steering.md`
- `MANIFEST.md`
- `shared/index/repository-map.md`
- `shared/index/doctrine-index.md`
- `shared/index/agent-index.md`
- `shared/index/skill-index.md`
- `skills/prompt-hydraulics.md`

The Prompt Hydraulics related-skill paths are present and indexed.

### Not proved

`tools/validate-scratch-links.py` is still a narrow checker. It:

- defaults to `scratch/` and `procedures/`;
- checks ordinary Markdown links only;
- does not inspect repository-relative paths inside code spans;
- does not find files unreachable from indexes;
- does not detect conflicting status, duplicate canonical names, missing owners, or semantic duplicates.

A clean run of that script is useful evidence, not a repository-wide integrity receipt.

### Portable-retrieval defects

`shared/doctrine-registry.md` still embeds device-local absolute paths under Home Center and Visual Truth Authority evidence. `MANIFEST_AGENTS_AND_HAZARDS.md` still cites sibling-workspace paths such as `../droobiedoo/`, `../prism-league/`, and `../legion-writing-tool/` as if the clone topology were stable.

**Repair:** introduce an external-evidence reference shape containing repository identity, canonical URL or resolver key, commit/blob identity when available, and optional local cache path. Local paths may be preserved as provenance but must not be the only retrieval route.

**Implementation owner:** Compiler  
**Verification owner:** Auditor

## 2. Agent authority remains split

Current sources still disagree:

- `MANIFEST.md` lists Sommelier under candidate missing agents and omits Wallfly from Known Agents.
- `shared/index/agent-index.md` lists Sommelier and Wallfly as current packs.
- `shared/agent-ecosystem.md` includes Sommelier but omits Command Center and Wallfly from its current-agent descriptions.
- `MANIFEST_AGENTS_AND_HAZARDS.md` still says no first-class Wallfly pack exists and that no known-hazards registry exists.
- `known-hazards/README.md` and `agents/wallfly/` now provide those missing authorities.

The repository map correctly labels `MANIFEST_AGENTS_AND_HAZARDS.md` as legacy archaeology, but the file itself is not marked obsolete and still reads as active authority when opened directly.

A second status problem has emerged: Cartographer, Crucible, Archivist, and Compiler are repeatedly assigned real operational ownership in reports, manifests, and glue work while remaining classified only as candidate agents. The repository needs to distinguish an active responsibility from a complete agent pack.

**Repair:**

1. Make `shared/index/agent-index.md` the canonical role inventory.
2. Add explicit status fields: `active responsibility`, `complete pack`, `candidate concept`, `diagnostic hazard`, `obsolete`.
3. Reconcile Sommelier and Wallfly everywhere.
4. Add Command Center and Wallfly to `shared/agent-ecosystem.md`.
5. Mark `MANIFEST_AGENTS_AND_HAZARDS.md` obsolete in its own header and point to the agent and hazard indexes.

**Implementation owner:** Quartermaster  
**Verification owner:** Auditor

## 3. Doctrine duplication and status conflict remain unresolved

### Three active-looking roots

Doctrine still appears under:

- `shared/doctrine/` — declared canonical target;
- `doctrine/` — legacy but unmarked inside individual files;
- `doctrines/` — legacy/domain notes that often claim promotion.

Location alone still cannot tell a cold reader whether a rule is inherited.

### Exact semantic duplication

`doctrine/combined_arms_with_swords_and_identity.md` and `doctrine/human_ai_symbiosis_mirror_problem.md` repeat the same Mirror Problem, Viral Infrastructure, and Floor-Is-A-Job compressions nearly verbatim.

### Status conflict

Feed Is The Battlefield and Dashboard Failure are simultaneously:

- inherited defaults in `shared/doctrines.md`;
- pending review in `shared/doctrine-registry.md`;
- promoted inside their own `doctrines/*.md` files;
- weak or disposition-required in `scratch/ore-worth-promoting.md`.

`shared/recursive-sense-synthesis.md` also remains separately named while the ore queue says it may belong inside Artificial Continuity.

**Repair:**

1. Crucible decides `promote`, `merge`, `demote`, or `obsolete` for each conflict.
2. Registry status changes first.
3. Defaults and indexes update from the registry decision.
4. Legacy files receive metadata naming canonical replacement or preservation reason.
5. Extract one lineage artifact for Mirror Problem / Viral Infrastructure / Floor-Is-A-Job, then retire duplicate authorities.

**Disposition owner:** Crucible  
**Implementation owner:** Quartermaster  
**Verification owner:** Auditor

## 4. Orphaned and weakly routed files

### Confirmed weak routes

- `shared/timeline.md` is valuable lineage but is only directly named by the previous integrity report. It is absent from the repository map, doctrine index, and README retrieval route.
- `discoveries/agent-closet-origin.md` declares itself promoted but has no direct inbound path from the repository map, doctrine index, or discovery index.
- `shared/registry-addenda/` contains promotion receipts but the folder is absent from the repository map and has no dedicated index.
- the top-level `simulation/`, `sim/`, and `doctrine/` roots are described as legacy in the repository map, but most contained files do not carry a canonical replacement, owner, or disposition.

### Improved since the previous report

- `steering.md` is now in the bootstrap route.
- reports, hazards, factories, tools, and legacy roots are represented in `shared/index/repository-map.md`.
- the prior capability report is reachable from the reports section.

**Repair:**

- add a small `shared/index/lineage-and-promotion-receipts.md` index for `shared/timeline.md`, origin records, and registry addenda;
- require every legacy-root file to name `canonical`, `superseded by`, `merge target`, or `archaeology only`;
- extend the future integrity checker to emit an inbound-link count and owning index for every durable Markdown file.

**Architecture owner:** Cartographer  
**Preservation owner:** Archivist  
**Verification owner:** Auditor

## 5. The ore queue is still a mixed graveyard

`scratch/ore-worth-promoting.md` has not been reconciled after the July 14 integrity report.

Stale or misclassified entries include:

- Agent Closet — operative system, still labeled `likely gold`.
- Artificial Continuity — already promoted, still in the candidate queue.
- Accessibility as First-Class Constraint — says a doctrine file is needed although `shared/accessibility-first.md` exists.
- Engineer Wizard + Goblin Familiar — says promoted but remains in ore.
- Agent Closet, Judgment Packs, and Portable Judgment Repository — overlapping names for the runtime-projection / portable-judgment product family.
- Feed Is The Battlefield, Dashboard Failure, and Recursive Sense Synthesis — unresolved doctrine-status conflicts.

Perspective Coding has accumulated enough repeated visual-truth incidents to deserve a formal Crucible decision rather than indefinite `one more incident` language. Sense Simulation and Drink Simulation remain legitimate scratch, but should live in a domain proof queue rather than beside repository-governance candidates.

**Repair:** split ore into explicit ledgers:

1. `promotion-candidates.md`
2. `proof-debt.md`
3. `disposition-required.md`
4. optional domain experiment ledgers such as sense/drink simulation

Every entry should require:

- disposition;
- decision date;
- implementation owner;
- verification owner;
- canonical target;
- remaining proof debt;
- next review date.

**Disposition owner:** Crucible  
**Index owner:** Quartermaster  
**Verification owner:** Auditor

## 6. Missing ownership is structural, not incidental

`templates/doctrine-template.md` still contains only Rule, Why, When, and Example.

`shared/doctrine-registry.md` still omits:

- Date
- Owner
- Verification owner
- Canonical path
- Source evidence identity
- Supersedes / superseded by
- Acceptance criteria
- Retrieval keywords

`glue/missing-glue-layers.md` assigns some work to stores or incomplete candidate roles such as Agent Closet, Dispatcher, Quartermaster Prime, and WWDD. Open PRs #2–#5 have no requested reviewers and no recorded Crucible disposition.

**Repair:** update the doctrine template and registry schema first, then backfill metadata when a doctrine is next touched. Do not create a giant all-files metadata churn PR.

**Schema owner:** Compiler  
**Implementation owner:** Quartermaster  
**Verification owner:** Auditor

## 7. Retrieval indexes are internally useful but temporally stale

The doctrine, agent, and skill indexes still display `Date: 2026-06-24`.

The skill index now contains Prompt Hydraulics from July 15, so its date no longer describes its actual content. The repository map is newer and explicitly acknowledges unresolved index debt, but a cold reader cannot tell whether an old date means stale content or merely an unrevised header.

The doctrine index and doctrine registry still compete rather than serving distinct declared roles. The intended distinction should be:

- doctrine index: retrieval and canonical path;
- doctrine registry: status, provenance, ownership, evidence, and supersession.

**Repair:** reconcile the three indexes in one bounded metadata and authority pass. Record `Last reviewed` separately from `Last content change` so automated edits do not create meaningless date churn.

**Implementation owner:** Quartermaster  
**Verification owner:** Auditor

## 8. Open promotion PRs need decisions

### PR #2 — Context Firewall

- open draft;
- mergeable;
- four commits, eight files;
- based on repository truth from July 4;
- touches README, scratch, registry, defaults, doctrine index, and the new doctrine.

**Recommendation:** rebase, inspect overlaps with newer sense-simulation and index changes, run the broad bootstrap validator, then promote or split. The doctrine remains high-value.

### PR #3 — World Simulation / Forbidden Stale Premise / Humane Guardrail

- open draft;
- non-mergeable;
- twelve commits, eleven files;
- combines protocol publication, memory adapter, stale-premise doctrine, humane guardrail doctrine, fixtures, validation, and index changes.

**Recommendation:** extract into at least two current-main lanes: World Simulation cold-start protocol and Humane Guardrail / stale-premise doctrine. Do not resolve a merge conflict by preserving the bundle.

### PR #4 — Scene Compiler reconciliation

- open draft;
- mergeable;
- one commit, one file;
- five additions and three deletions.

**Recommendation:** this is the smallest disposition win. Review the changed wording against the promotion receipt, merge if accurate, and close the stale doctrine gap.

### PR #5 — Contagious Operational Memes

- open draft;
- mergeable;
- two commits, two files;
- 189 additions;
- overlaps Artificial Continuity, Simulation as Learning Infrastructure, Viral Infrastructure, prompt phrases, and registry addenda.

**Recommendation:** require an overlap map, owner, verification owner, canonical relationship, and Crucible verdict before promotion.

**Disposition owner:** Crucible  
**Branch owner:** Foreman  
**Verification owner:** Auditor

## Archaeology worth preserving

Preserve these as lineage, not competing authority:

- `shared/timeline.md` — evolution from memory to portable judgment.
- `discoveries/agent-closet-origin.md` — storage medium versus continuity framework distinction.
- unique material from `MANIFEST_AGENTS_AND_HAZARDS.md` after stale claims are removed from authority.
- Mirror Problem / Viral Infrastructure / Floor-Is-A-Job compressions from the two legacy doctrine files.
- dated registry addenda as immutable promotion receipts linked to current canonical doctrine.
- `reports/end_of_day_capability_report_2026_06_23.md` as an ecosystem convergence snapshot.

**Preservation owner:** Archivist  
**Verification owner:** Quartermaster

## Promotion opportunities

### 1. Repository Integrity Graph

Generate a machine-readable graph of files, indexes, owners, statuses, doctrine names, inbound links, supersession, and canonical paths.

Promotion gate: identify and correctly route one broken path, one orphan, one duplicate doctrine, one stale status, and one missing owner.

**Owner:** Cartographer  
**Implementation partner:** Compiler  
**Verification:** Auditor

### 2. Context Firewall

Promote after current-main rebase and negative fixtures proving stale project assumptions, proxy artifacts, and outdated acceptance paths cannot silently control a fresh task.

**Owner:** Quartermaster  
**Verification:** Auditor

### 3. Prompt Hydraulics Gold proof

Prompt Hydraulics is a good Silver artifact. It should reach Gold only after its stated three-domain runs, one safe relief-valve failure, and one cold-start worker execution are preserved and independently read back.

**Owner:** Quartermaster  
**Execution:** Foreman  
**Verification:** Auditor

### 4. Doctrine Registry v2

Promote the registry from a list into the authority ledger it claims to be by requiring owners, evidence identity, canonical path, supersession, acceptance criteria, and retrieval keywords.

**Owner:** Compiler  
**Verification:** Auditor

### 5. Artifact-Borne Instruction Trust Receipt

Promote the Prompt Injection Through Procedure candidate through a bounded test comparing canonical base instructions with branch- or artifact-supplied instructions before an agent is allowed to inherit them.

**Owner:** Auditor  
**Implementation partner:** Compiler

## Recommended repair order

1. Merge or reject PR #4 after a focused readback.
2. Run one bounded authority reconciliation for agent status and obsolete manifests.
3. Split the ore queue by candidate, proof debt, and disposition.
4. Establish Doctrine Registry v2 metadata and backfill only touched doctrines.
5. Build the repository-wide integrity graph/checker.
6. Rebase/extract PRs #2, #3, and #5 according to Crucible decisions.
7. Preserve lineage files through a dedicated retrieval index.

## Next smallest useful action

Review and disposition **PR #4: Reconcile Scene Compiler doctrine**.

Acceptance criteria:

1. Compare its one-file wording change against `shared/registry-addenda/2026-06-26-scene-compiler-runtime-promotion.md` and current `skills/scene-compiler.md`.
2. Confirm it removes stale Field Guide ore wording without weakening repository evidence gates.
3. Run `git diff --check` and the broad Markdown validator against `skills/`, `shared/`, `procedures/`, and `scratch/`.
4. Merge if accurate; otherwise close with a precise replacement note.
5. Update the affected skill/index review date only if the canonical content actually changes.

This is small enough to finish cleanly and removes one stale-doctrine branch before larger authority surgery begins.
