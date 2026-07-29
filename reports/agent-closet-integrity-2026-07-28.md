# Agent Closet Integrity Report — 2026-07-28

Type: Repository integrity review  
Status: Active findings  
Owner: Quartermaster  
Verification owner: Auditor  
Scope: `Valar05/agent-closet` on `main` at `956ac840e7faee4a93e52aa2c77c45d9f8988e25`

## Executive verdict

Overall health: **Yellow**.

The repository has improved its bootstrap path and recently promoted two useful artifacts cleanly enough to be found: `shared/doctrine/intent-integrity-bounded-initiative.md` is loaded during orientation, and `procedures/vanilla-chatgpt-rotoscoping-packet.md` is indexed as a bounded fallback procedure.

The limiting defects are still authority, disposition, and machine-verifiable integrity:

- agent status conflicts remain between `MANIFEST.md` and `shared/index/agent-index.md`;
- doctrine remains split across three active-looking roots and exact semantic duplication persists;
- scratch still mixes live systems, promoted doctrine, proof debt, product ideas, and domain experiments;
- durable lineage and promotion receipts remain weakly routed;
- templates and registries still do not require complete ownership, verification, canonical-path, or supersession metadata;
- open doctrine PRs remain undecided;
- the repository still lacks a repository-wide link, orphan, owner, status, and duplicate validator.

## Integrity summary

| Area | Verdict | Highest-value defect |
|---|---|---|
| Broken links | Yellow-green | No confirmed broken bootstrap link, but repository-wide proof and CI are absent. |
| Duplicate doctrine | Red-yellow | Three doctrine roots and exact repeated compressions still look authoritative. |
| Orphaned files | Yellow | Lineage and promotion receipts still lack stable inbound indexes. |
| Scratch disposition | Red-yellow | The ore queue contradicts its own anti-graveyard rule. |
| Retrieval paths | Yellow | Bootstrap is strong; agent, doctrine, skill, lineage, and authority records still disagree. |
| Ownership | Red-yellow | Canonical schemas do not require implementation and verification owners. |
| Promotion queue | Yellow | Valuable candidates exist, but four old draft PRs and several scratch entries lack a verdict. |

## 1. Broken links and portability

### Confirmed working in the reviewed path

The current bootstrap paths resolve:

- `README.md`
- `MANIFEST.md`
- `shared/index/repository-map.md`
- `shared/index/doctrine-index.md`
- `shared/index/agent-index.md`
- `shared/index/skill-index.md`
- `shared/doctrine/intent-integrity-bounded-initiative.md`
- `procedures/vanilla-chatgpt-rotoscoping-packet.md`
- `glue/missing-glue-layers.md`

The related files named by Intent Integrity also resolve.

### Repository-wide proof is still absent

`tools/validate-scratch-links.py` remains a narrow checker:

- default scope is only `scratch/` and `procedures/`;
- it checks ordinary Markdown links, conflict markers, duplicate headings, and fenced-code balance;
- it does not inspect repository paths inside code spans;
- it does not calculate inbound links or orphan status;
- it does not detect conflicting statuses, duplicate canonical names, missing owners, or semantic duplication.

No workflow run is attached to the current `main` head.

### Non-portable evidence routes remain

`shared/doctrine-registry.md` still uses device-local `/storage/emulated/0/...` paths as evidence for Home Center and Visual Truth Authority. `MANIFEST_AGENTS_AND_HAZARDS.md` still uses sibling-workspace paths such as `../droobiedoo/`, `../prism-league/`, and `../legion-writing-tool/` as if clone topology were stable.

**Recommended repair**

Create an external-evidence reference schema with:

- repository or system identity;
- canonical URL or resolver key;
- commit, blob, artifact, or request identity;
- optional local cache path;
- evidence owner;
- verification date.

Then expand the validator to scan every durable Markdown root and emit a repository-wide integrity receipt.

**Implementation owner:** Compiler  
**Verification owner:** Auditor

## 2. Agent authority is still split

Current authorities disagree:

- `MANIFEST.md` omits Wallfly from Known Agents and lists Sommelier as a missing candidate.
- `shared/index/agent-index.md` lists both Wallfly and Sommelier as current packs.
- Cartographer, Crucible, Archivist, and Compiler carry real work in reports, glue, and manifests while remaining classified only as candidates.
- `MANIFEST_AGENTS_AND_HAZARDS.md` is labeled legacy only from the repository map; its own header still reads as active authority and it still says no `known-hazards/` registry exists.

The real missing distinction is not simply current versus candidate. The repository needs separate states for:

- active responsibility;
- complete agent pack;
- candidate concept;
- diagnostic hazard;
- obsolete or historical authority.

**Recommended repair**

1. Make `shared/index/agent-index.md` the canonical role inventory.
2. Add the five status states above.
3. Reconcile Wallfly and Sommelier in `MANIFEST.md`.
4. Mark `MANIFEST_AGENTS_AND_HAZARDS.md` obsolete in its own header and point it to the current agent and hazard indexes.
5. Assign current operational responsibilities to Cartographer, Crucible, Archivist, and Compiler without pretending their packs are complete.

**Implementation owner:** Quartermaster  
**Verification owner:** Auditor

## 3. Doctrine duplication and status conflict remain

### Three active-looking doctrine roots

Doctrine still appears under:

- `shared/doctrine/` — declared canonical target;
- `doctrine/` — legacy but usually unmarked inside individual files;
- `doctrines/` — legacy/domain material that often claims promotion.

A cold reader still cannot infer inheritance or authority from location alone.

### Exact semantic duplication

`doctrine/combined_arms_with_swords_and_identity.md` and `doctrine/human_ai_symbiosis_mirror_problem.md` repeat the same Mirror Problem, Viral Infrastructure, Floor-Is-A-Job, and city-road compressions nearly verbatim.

### Status conflict

Feed Is The Battlefield and Dashboard Failure remain simultaneously:

- inherited defaults in `shared/doctrines.md`;
- pending review in `shared/doctrine-registry.md`;
- promoted in their own `doctrines/*.md` files;
- disposition-required or weak in `scratch/ore-worth-promoting.md`.

`shared/recursive-sense-synthesis.md` remains a separate named doctrine while the ore queue says it may belong inside Artificial Continuity.

### New promotion-process evidence

Intent Integrity and Bounded Initiative is a strong doctrine and is correctly reachable from README, manifest, defaults, registry, and doctrine index. Its promotion nevertheless arrived as a sequence of direct commits, beginning with a `test` commit that wrote only `x`, followed by separate definition, inheritance, indexing, registry, manifest, and orientation commits.

The final state is useful. The transaction shape is not.

**Promotable discovery:** **Promotion Is One Atomic Receipt.**

A promotion receipt should bind:

- canonical file;
- status and confidence;
- implementation owner and verification owner;
- source evidence identity;
- registry entry;
- indexes and inherited defaults;
- supersession or duplicate disposition;
- acceptance criteria and validation result;
- readback from the final commit.

**Disposition owner:** Crucible  
**Implementation owner:** Quartermaster / Compiler  
**Verification owner:** Auditor

## 4. Orphaned and weakly routed files remain

Confirmed weak routes:

- `shared/timeline.md` is valuable lineage but is only named by dated integrity reports.
- `discoveries/agent-closet-origin.md` declares itself promoted but is only named by the previous integrity report.
- `shared/registry-addenda/` contains durable promotion receipts but has no dedicated index and is absent from the repository map.
- legacy roots `doctrine/`, `doctrines/`, `simulation/`, and `sim/` lack per-file canonical replacement or archaeology metadata.

Positive delta:

- the July 27 research radar is routed from both `MANIFEST.md` and the glue registry;
- the vanilla ChatGPT rotoscoping packet is indexed in the skill/procedure index;
- the current integrity report route exists in the repository map, although it now needs this report as the current target.

**Recommended repair**

Add `shared/index/lineage-and-promotion-receipts.md` covering:

- `shared/timeline.md`;
- origin records;
- registry addenda;
- dated promotion records;
- archaeology packets and successors.

Require every legacy-root file to state one of:

- canonical;
- superseded by;
- merge target;
- archaeology only;
- disposition required.

**Architecture owner:** Cartographer  
**Preservation owner:** Archivist  
**Verification owner:** Auditor

## 5. Scratch remains a mixed graveyard

`scratch/ore-worth-promoting.md` still contains stale or misclassified entries:

- Agent Closet is an operative system but remains `likely gold`.
- Artificial Continuity is promoted but remains in the candidate queue.
- Accessibility as First-Class Constraint says it needs a dedicated doctrine file although `shared/accessibility-first.md` already exists.
- Engineer Wizard + Goblin Familiar says it is promoted but remains in ore.
- Agent Closet, Judgment Packs, and Portable Judgment Repository overlap as one portable-judgment/runtime-projection product family.
- Feed Is The Battlefield, Dashboard Failure, and Recursive Sense Synthesis remain unresolved status conflicts.

Perspective Coding has enough repeated visual-truth incidents to require a Crucible verdict rather than indefinite `one more incident` language.

Sense Simulation and Drink Simulation remain legitimate experiments, but they should not share a queue with repository governance and doctrine disposition.

**Recommended repair**

Split scratch disposition into:

1. `promotion-candidates.md`
2. `proof-debt.md`
3. `disposition-required.md`
4. domain experiment ledgers, beginning with sense/drink simulation

Each entry should require:

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

## 6. Missing ownership is structural

`templates/doctrine-template.md` still contains only Rule, Why, When, and Example.

`shared/doctrine-registry.md` still omits mandatory fields for:

- Date and last reviewed;
- implementation owner;
- verification owner;
- canonical path;
- source evidence identity;
- supersedes / superseded by;
- acceptance criteria;
- retrieval keywords.

The latest canon doctrine, Intent Integrity, has an owner but no verification owner or explicit supersession field. `shared/accessibility-first.md` is indexed as a shared default but has no Type, Status, Date, Owner, Verification owner, or source identity header.

`glue/missing-glue-layers.md` assigns several layers to stores or incomplete candidate roles, including Agent Closet, Dispatcher, Quartermaster Prime, and WWDD. Responsibility should be executable even when a full agent pack is not yet present.

**Recommended repair**

Update the doctrine template and registry schema first. Backfill metadata when a doctrine is next touched; do not create a giant all-files metadata-churn branch.

**Schema owner:** Compiler  
**Implementation owner:** Quartermaster  
**Verification owner:** Auditor

## 7. Retrieval indexes are useful but stale in authority metadata

`shared/index/doctrine-index.md`, `shared/index/agent-index.md`, and `shared/index/skill-index.md` still display `Date: 2026-06-24` despite later content changes. The skill index now includes July 15 and July 27 additions. The doctrine index includes the July 27 Intent Integrity doctrine.

The intended split should be explicit:

- doctrine index: retrieval and canonical path;
- doctrine registry: status, ownership, evidence, confidence, and supersession;
- manifest: estate-level current priorities and authority stack;
- repository map: navigation and root disposition.

Add separate fields for `Last reviewed` and `Last content change` so automated edits do not produce meaningless date churn.

**Implementation owner:** Quartermaster  
**Verification owner:** Auditor

## 8. Open promotion PRs still need disposition

### PR #2 — Context Firewall

- open draft;
- mergeable;
- four commits;
- based on July 4 repository truth;
- still high-value, but overlaps newer Intent Integrity and index changes.

**Recommendation:** rebase and split only if necessary. Crucible should decide whether Context Firewall is a narrower operational doctrine under Intent Integrity or a distinct quarantine doctrine.

### PR #3 — World Simulation / Forbidden Stale Premise / Humane Guardrail

- open draft;
- non-mergeable;
- combines a cold-start protocol, memory adapter, stale-premise doctrine, humane guardrail, fixtures, validation, and index updates.

**Recommendation:** extract two current-main lanes: World Simulation cold-start protocol, and Humane Guardrail / Forbidden Stale Premise doctrine.

### PR #4 — Scene Compiler reconciliation

- open draft;
- mergeable;
- one commit and one file;
- five additions and three deletions.

**Recommendation:** this remains the smallest disposition win. Rebase or verify against current `main`, merge if the promotion receipt still supports the wording, then close the stale gap.

### PR #5 — Contagious Operational Memes

- open draft;
- non-mergeable;
- overlaps Artificial Continuity, Simulation as Learning Infrastructure, Viral Infrastructure, prompt phrases, and registry addenda.

**Recommendation:** require an overlap map, owner, verifier, canonical relationship, and Crucible verdict before extraction or promotion.

**Disposition owner:** Crucible  
**Branch owner:** Foreman  
**Verification owner:** Auditor

## Archaeology worth preserving

Preserve these as lineage, not competing authority:

1. `shared/timeline.md` — evolution from memory to portable judgment.
2. `discoveries/agent-closet-origin.md` — storage medium versus continuity framework.
3. the Intent Integrity incident chain and the six-commit promotion sequence, including the placeholder `test` commit, as evidence for atomic promotion receipts.
4. one compact Mirror Problem / Viral Infrastructure / Floor-Is-A-Job lineage record before duplicate doctrine authorities are retired.
5. unique hazard evidence from `MANIFEST_AGENTS_AND_HAZARDS.md` after its stale authority claims are removed.
6. dated `shared/registry-addenda/` files as immutable promotion receipts linked to current canonical doctrine.
7. closed or superseded doctrine PRs after their useful content and rejection reasons are extracted.

**Preservation owner:** Archivist  
**Verification owner:** Quartermaster

## Promotion opportunities

### 1. Repository Integrity Graph

Generate a machine-readable graph of:

- files;
- canonical names;
- roots;
- statuses;
- owners and verification owners;
- inbound and outbound links;
- index membership;
- supersession;
- duplicate candidates;
- open promotion branches.

This should power a CI check and a human-readable conflict report.

**Owner:** Compiler  
**Verification:** Auditor

### 2. Atomic Promotion Receipt

Turn the current multi-commit promotion ritual into one schema and validation path that proves doctrine, indexes, registry, inheritance, owners, evidence, and readback moved together.

**Owner:** Compiler / Quartermaster  
**Verification:** Auditor

### 3. Agent Responsibility Status Model

Separate active responsibility from complete pack. This resolves the current contradiction around Cartographer, Crucible, Archivist, Compiler, Wallfly, and Sommelier without inventing more agents.

**Owner:** Quartermaster  
**Verification:** Auditor

### 4. Perspective Coding disposition

Repeated visual no-op and false-green incidents now exceed the original one-more-incident threshold. Crucible should decide whether this becomes a focused doctrine, merges into Visual Truth Authority, or remains a named test family.

**Owner:** Crucible  
**Implementation:** Quartermaster  
**Verification:** Auditor

### 5. Accessibility doctrine metadata plus disabled-user evidence route

`shared/accessibility-first.md` is already behavior-changing and inherited. Promote its metadata and connect it to the Disabled-User Verdict Ledger rather than creating a duplicate accessibility doctrine.

**Owner:** Holocron / Quartermaster  
**Verification:** Auditor

## Prioritized repair order

1. **Dispose PR #4.** It is the smallest open authority gap and prevents Scene Compiler wording from remaining stale.
2. **Reconcile the agent inventory.** Fix Wallfly/Sommelier and active-responsibility status; mark the legacy manifest obsolete in its own header.
3. **Upgrade doctrine template and registry schema.** Make complete ownership and supersession unavoidable for the next promotion.
4. **Split the ore queue.** Move stale items to disposition and domain experiments to their own ledgers.
5. **Build the repository integrity graph and CI receipt.** Stop relying on recurring human archaeology to rediscover the same contradictions.
6. **Add the lineage and promotion-receipt index.** Preserve the fossils without leaving them in the road.

## Next smallest useful action

Crucible reviews PR #4 against `shared/registry-addenda/2026-06-26-scene-compiler-runtime-promotion.md` and issues one verdict: `merge`, `revise`, or `close as superseded`.

If the wording is still supported, Foreman rebases or verifies the one-file branch against current `main`, Auditor checks the exact diff, and the PR is merged immediately. No new doctrine proposal should be added before this smallest old decision is closed.