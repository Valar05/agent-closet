# Agent Closet Integrity Report — 2026-08-04

Type: Repository integrity review  
Status: Active findings  
Owner: Quartermaster  
Verification owner: Auditor  
Scope: `Valar05/agent-closet` on `main` at `efbecf370f09fbb5c6b5391695d89798d7deb61d`  
Previous report: `reports/agent-closet-integrity-2026-07-28.md`

## Executive verdict

Overall health: **Yellow**.

The repository remains useful, navigable from the primary bootstrap, and increasingly explicit about mission boundaries and visual truth. The latest change also added a concrete mechanical-authoring skill and routed it through the manifest and skill index.

The integrity bottleneck did not move. The defects identified on 2026-07-28 remain substantially unresolved:

- agent authority still disagrees between `MANIFEST.md`, `shared/index/agent-index.md`, and the legacy mixed manifest;
- doctrine still appears under three active-looking roots, with exact semantic duplication and conflicting promotion states;
- scratch still mixes operating systems, promoted doctrine, proof debt, product concepts, and domain experiments;
- lineage, origin records, and promotion receipts remain reachable mainly through dated reports;
- ownership and supersession metadata remain optional in the canonical templates and registry;
- four doctrine pull requests remain open without disposition;
- repository-wide link, orphan, owner, status, duplicate, and index-membership proof still does not exist.

The new mechanical-authoring skill is a useful positive delta, but it also demonstrates the metadata problem: it is active and inherited while lacking an explicit owner, verification owner, date, evidence identity, supersession relationship, and retrieval keywords.

## Integrity summary

| Area | Verdict | Highest-value defect |
|---|---|---|
| Broken links | Yellow-green | No broken primary bootstrap path was confirmed; repository-wide proof is still absent. |
| Duplicate doctrine | Red-yellow | Exact repeated doctrine and conflicting authority remain across three roots. |
| Orphaned files | Yellow | Lineage, origin, and registry-addendum records still lack a durable index. |
| Scratch disposition | Red-yellow | The ore queue still violates its own anti-graveyard rule. |
| Retrieval paths | Yellow | Primary routing works, but authority, status, lineage, and legacy-root routing disagree. |
| Ownership | Red-yellow | Canonical schemas do not require implementation and verification owners. |
| Promotion queue | Red-yellow | Four July draft PRs and several scratch entries still lack a verdict. |

## 1. Broken links and portability

### Primary bootstrap remains readable

The reviewed bootstrap files exist and resolve on current `main`:

- `README.md`
- `steering.md`
- `MANIFEST.md`
- `shared/index/repository-map.md`
- `shared/index/doctrine-index.md`
- `shared/index/agent-index.md`
- `shared/index/skill-index.md`
- `scratch/ore-worth-promoting.md`
- `glue/missing-glue-layers.md`

No broken link was confirmed in that narrow route.

### Repository-wide proof remains absent

`tools/validate-scratch-links.py` still defaults to `scratch/` and `procedures/`. It checks ordinary Markdown links, conflict markers, duplicate exact headings, and fenced-code balance. It does not prove integrity across the full repository and does not detect:

- paths written in code spans;
- inbound-link counts or orphan status;
- missing index membership;
- missing owners or verifiers;
- conflicting promotion states;
- duplicate canonical names;
- semantic doctrine duplication;
- stale external evidence references.

### Non-portable evidence remains in authority-bearing files

`shared/doctrine-registry.md` still cites device-local `/storage/emulated/0/...` paths for Home Center and Visual Truth Authority. `MANIFEST_AGENTS_AND_HAZARDS.md` still cites sibling-workspace paths such as `../droobiedoo/`, `../prism-league/`, and `../legion-writing-tool/` as if clone topology were stable.

**Recommended repair**

Expand the validator into a repository-wide integrity graph and add an external-evidence reference shape containing:

- system or repository identity;
- canonical URL or resolver key;
- commit, blob, artifact, or request identity;
- optional local cache path;
- evidence owner;
- verification date.

**Implementation owner:** Compiler  
**Verification owner:** Auditor

## 2. Duplicate doctrine and conflicting status

### Three doctrine roots still look authoritative

Doctrine remains distributed across:

- `shared/doctrine/` — declared canonical target;
- `doctrine/` — legacy root, usually not marked inside individual files;
- `doctrines/` — legacy/domain root containing files that still claim promotion.

A cold reader cannot determine authority from file location alone.

### Exact semantic duplication remains

`doctrine/combined_arms_with_swords_and_identity.md` and `doctrine/human_ai_symbiosis_mirror_problem.md` repeat the same Mirror Problem, Viral Infrastructure, Floor-Is-A-Job, and city-road compressions nearly verbatim.

### Promotion state still conflicts

`Feed Is The Battlefield` and `Dashboard Failure` remain simultaneously:

- inherited defaults in `shared/doctrines.md`;
- pending review in `shared/doctrine-registry.md`;
- promoted in their own `doctrines/*.md` files;
- disposition-required or weak in `scratch/ore-worth-promoting.md`.

`shared/recursive-sense-synthesis.md` remains a durable store and inherited default while the ore queue says it may need to merge into Artificial Continuity.

**Recommended repair**

1. Select one canonical destination for each repeated doctrine family.
2. Preserve legacy files with explicit `Status: Obsolete`, `Superseded by`, and archaeology notes.
3. Resolve promotion status in one atomic change across the canonical file, doctrine registry, doctrine index, inherited defaults, and ore queue.
4. Add duplicate and supersession output to the proposed Resource Conflict and Supersession Report.

**Disposition owner:** Crucible  
**Implementation owner:** Quartermaster / Compiler  
**Verification owner:** Auditor

## 3. Orphaned and weakly routed files

The following durable material remains reachable primarily through dated integrity reports rather than a stable lineage index:

- `shared/timeline.md`;
- `discoveries/agent-closet-origin.md`;
- `shared/registry-addenda/` and its dated promotion receipts.

The repository map names the legacy roots, but individual files under `doctrine/`, `doctrines/`, `simulation/`, and `sim/` generally do not identify their canonical successor or disposition.

**Recommended repair**

Add `shared/index/lineage-and-promotion-receipts.md` containing:

- origin records;
- timeline and major architectural transitions;
- promotion receipts and registry addenda;
- incident archaeology;
- canonical successor;
- current status;
- preservation owner;
- verification owner.

Require each legacy-root file, when next touched, to declare one of:

- canonical;
- superseded by;
- merge target;
- archaeology only;
- disposition required.

**Architecture owner:** Cartographer  
**Preservation owner:** Archivist  
**Verification owner:** Auditor

## 4. Scratch remains a mixed graveyard

`scratch/ore-worth-promoting.md` still contains stale or misclassified entries:

- Agent Closet is an operating repository but remains `likely gold`.
- Artificial Continuity is promoted but remains in the candidate queue.
- Accessibility as First-Class Constraint says it needs a dedicated doctrine file although `shared/accessibility-first.md` already exists.
- Engineer Wizard + Goblin Familiar is labeled promoted but remains in ore.
- Agent Closet, Judgment Packs, and Portable Judgment Repository overlap as one portable-judgment product family.
- Feed Is The Battlefield, Dashboard Failure, and Recursive Sense Synthesis remain unresolved authority conflicts.
- Perspective Coding remains parked behind an indefinite “one more incident” gate despite repeated false-green and visual-no-op evidence.
- Sense Simulation and Drink Simulation are legitimate experiments but share a queue with governance and doctrine disposition.

The file says it must not become a graveyard, but it lacks required decision dates, owners, canonical targets, or next-review dates.

**Recommended repair**

Split the queue into:

1. `scratch/promotion-candidates.md`
2. `scratch/proof-debt.md`
3. `scratch/disposition-required.md`
4. domain experiment ledgers, beginning with sense and drink simulation

Require each entry to contain:

- current disposition;
- decision date;
- implementation owner;
- verification owner;
- canonical target;
- remaining proof debt;
- next review date.

**Disposition owner:** Crucible  
**Index owner:** Quartermaster  
**Verification owner:** Auditor

## 5. Retrieval and authority still disagree

### Agent inventory conflict

`MANIFEST.md` omits Wallfly from Known Agents and lists Sommelier as a missing candidate. `shared/index/agent-index.md` lists both as current packs.

Cartographer, Crucible, Archivist, and Compiler already carry active responsibilities in reports, manifests, and glue entries while remaining classified only as candidate concepts.

The needed distinction is:

- active responsibility;
- complete agent pack;
- candidate concept;
- diagnostic hazard;
- obsolete or historical authority.

### The legacy mixed manifest is still self-authoritative

`shared/index/repository-map.md` correctly labels `MANIFEST_AGENTS_AND_HAZARDS.md` as legacy archaeology. The file itself does not. It still claims:

- no Wallfly pack exists;
- no `known-hazards/` registry exists;
- no `shared/perspective-routing.md` exists.

All three claims are stale. A reader opening the file directly receives false current-state guidance.

### Index metadata is stale

`shared/index/doctrine-index.md`, `shared/index/agent-index.md`, and `shared/index/skill-index.md` still show `Date: 2026-06-24` despite later content changes. The skill index now contains the 2026-07-30 mechanical-authoring skill. The doctrine index contains later canon doctrine.

The manifest and missing-glue registry still point to the 2026-07-27 research radar as current.

**Recommended repair**

1. Make `shared/index/agent-index.md` the canonical role inventory.
2. Add the five agent status states above.
3. Reconcile Wallfly and Sommelier in `MANIFEST.md`.
4. Mark `MANIFEST_AGENTS_AND_HAZARDS.md` obsolete in its own header and point to the current agent and hazard indexes.
5. Add `Last reviewed` and `Last content change` fields to indexes instead of overloading one date.
6. Update research pointers only when a newer research artifact is actually committed.

**Implementation owner:** Quartermaster  
**Verification owner:** Auditor

## 6. Missing ownership remains structural

`templates/doctrine-template.md` still contains only Rule, Why, When, and Example.

`shared/doctrine-registry.md` does not require:

- date and last reviewed;
- implementation owner;
- verification owner;
- canonical path;
- source evidence identity;
- supersedes / superseded by;
- acceptance criteria;
- retrieval keywords.

`shared/accessibility-first.md` is inherited, indexed, and behavior-changing but has no Type, Status, Date, Owner, Verification owner, source identity, or supersession metadata.

The latest active skill, `skills/model-mechanical-hard-surfaces.md`, has Type, Status, and Kernel but no owner, verification owner, date, source evidence identity, retrieval keywords, or supersession field. Its addition proves that the schema gap is still creating fresh debt.

Several glue layers are assigned to stores or incomplete roles such as Agent Closet, Dispatcher, Quartermaster Prime, and WWDD. An executable responsibility must exist even before a full pack does.

**Recommended repair**

Upgrade the doctrine and skill metadata template first. Backfill metadata only when a file is next touched; avoid a repository-wide metadata-confetti branch.

**Schema owner:** Compiler  
**Implementation owner:** Quartermaster  
**Verification owner:** Auditor

## 7. Open promotion PRs still lack disposition

### PR #2 — Context Firewall

- open draft since 2026-07-04;
- mergeable;
- based on substantially older repository truth;
- overlaps newer Intent Integrity doctrine.

**Recommendation:** Crucible decides whether it is a narrower quarantine doctrine under Intent Integrity or a distinct doctrine. Rebase only after that verdict.

### PR #3 — World Simulation / Forbidden Stale Premise / Humane Guardrail

- open draft since 2026-07-12;
- non-mergeable;
- combines protocol, adapter, doctrine, fixtures, validation, and indexes.

**Recommendation:** extract two current-main proposals: World Simulation cold-start protocol, and Humane Guardrail / Forbidden Stale Premise doctrine.

### PR #4 — Scene Compiler reconciliation

- open draft since 2026-07-13;
- mergeable;
- one commit, one file, five additions, three deletions;
- reconciles Field Guide judgment substrate with the existing promotion receipt.

**Recommendation:** this remains the smallest authority-disposition win. Crucible should issue `merge`, `revise`, or `close as superseded` against current `main`.

### PR #5 — Contagious Operational Memes

- open draft since 2026-07-13;
- currently mergeable;
- overlaps Artificial Continuity, Simulation as Learning Infrastructure, Viral Infrastructure, prompt phrases, and registry addenda.

**Recommendation:** require an overlap map, canonical relationship, owner, verifier, and Crucible verdict before promotion.

**Disposition owner:** Crucible  
**Branch owner:** Foreman  
**Verification owner:** Auditor

## Archaeology worth preserving

Preserve these as lineage without leaving them as parallel authority:

1. `shared/timeline.md` — the transition from chat memory to portable judgment.
2. `discoveries/agent-closet-origin.md` — storage medium versus continuity framework.
3. the Intent Integrity promotion sequence, including the placeholder `test` commit and separate definition, inheritance, indexing, promotion, and orientation commits, as evidence for atomic promotion receipts.
4. one compact Mirror Problem / Viral Infrastructure / Floor-Is-A-Job lineage record before duplicate authorities are retired.
5. unique evidence from `MANIFEST_AGENTS_AND_HAZARDS.md` after stale current-state claims are removed.
6. dated `shared/registry-addenda/` files as immutable promotion receipts linked to canonical successors.
7. closed or superseded doctrine PRs after useful content and rejection reasons are extracted.

**Preservation owner:** Archivist  
**Verification owner:** Quartermaster

## Promotion opportunities

### 1. Repository Integrity Graph

Generate a machine-readable graph of files, canonical names, roots, statuses, owners, verifiers, inbound and outbound links, index membership, supersession, duplicate candidates, and open promotion branches.

**Owner:** Compiler  
**Verification:** Auditor

### 2. Atomic Promotion Receipt

Bind canonical content, status, confidence, owners, evidence, registry, indexes, inheritance, supersession, acceptance criteria, validation, and final readback into one promotion transaction.

**Owner:** Compiler / Quartermaster  
**Verification:** Auditor

### 3. Agent Responsibility Status Model

Separate active responsibility from complete pack so Cartographer, Crucible, Archivist, Compiler, Wallfly, and Sommelier can be represented without contradiction.

**Owner:** Quartermaster  
**Verification:** Auditor

### 4. Accessibility metadata and disabled-user evidence route

Do not create another accessibility doctrine. Add complete metadata to `shared/accessibility-first.md` and connect it to the Disabled-User Verdict Ledger.

**Owner:** Holocron / Quartermaster  
**Verification:** Auditor

### 5. Perspective Coding disposition

The evidence threshold has been met often enough to require a verdict: promote as focused doctrine, merge into Visual Truth Authority, or preserve as a named test family.

**Owner:** Crucible  
**Implementation:** Quartermaster  
**Verification:** Auditor

## Prioritized repair order

1. **Dispose PR #4.** It is the smallest open authority gap.
2. **Reconcile the agent inventory and tombstone the legacy mixed manifest inside its own file.**
3. **Upgrade doctrine and skill metadata schemas.** Make ownership, evidence, and supersession unavoidable for new promotions.
4. **Split the ore queue.** Separate promotion, proof debt, disposition, and domain experiments.
5. **Add the lineage and promotion-receipt index.** Preserve fossils without making reports their only doorway.
6. **Build the repository integrity graph and CI receipt.** Stop paying a human archaeology tax to rediscover the same contradictions.

## Next smallest useful action

**Crucible reviews PR #4 against current `main` and records exactly one verdict: `merge`, `revise`, or `close as superseded`.**

Acceptance criteria:

- the 2026-06-26 Scene Compiler promotion receipt still supports the proposed wording;
- no newer canonical file already supersedes it;
- the branch is checked against current `main` rather than its July base snapshot;
- the verdict and rationale are preserved on the PR;
- if merged, the final commit is read back and the stale wording is no longer present;
- if rejected, the useful evidence and rejection reason remain retrievable.

This is one file, one existing branch, and one unresolved authority claim. It closes a real lane before the repository invents another doctrine-shaped hat.