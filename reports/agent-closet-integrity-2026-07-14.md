# Agent Closet Integrity Report — 2026-07-14

Type: Repository integrity review  
Status: Active findings  
Owner: Quartermaster  
Verification owner: Auditor  
Scope: `Valar05/agent-closet` on `main`

## Executive verdict

Overall health: **Yellow**.

The repository contains strong doctrine, useful agent packs, real retrieval indexes, and valuable archaeology. The main integrity risk is no longer missing material. It is competing authority: several manifests, indexes, roots, and promotion queues describe the same estate differently.

The audited entry path contains no confirmed broken relative Markdown links. That is not a repository-wide clean bill of health: the current validator defaults to `scratch/` and `procedures/`, checks only ordinary Markdown links, and does not validate backtick path references, index coverage, owners, canonical paths, duplicates, or orphaned files.

## Highest-value findings

### 1. Agent authority is split across stale sources

Repository truth currently disagrees across:

- `MANIFEST.md`
- `shared/index/agent-index.md`
- `shared/agent-ecosystem.md`
- `MANIFEST_AGENTS_AND_HAZARDS.md`
- `known-hazards/README.md`

Concrete drift:

- `MANIFEST.md` still lists Sommelier as a candidate, while `shared/index/agent-index.md` lists Sommelier as a current pack.
- `MANIFEST.md` omits Wallfly from Known Agents, while the agent index lists Wallfly and the repository contains a complete `agents/wallfly/` pack.
- `shared/agent-ecosystem.md` omits current Command Center and Wallfly responsibilities.
- `MANIFEST_AGENTS_AND_HAZARDS.md` says no first-class Wallfly pack exists and says the known-hazards registry is missing, but both now exist.

**Repair:** Make `shared/index/agent-index.md` the canonical role inventory. Reconcile `MANIFEST.md` and `shared/agent-ecosystem.md` against it. Mark `MANIFEST_AGENTS_AND_HAZARDS.md` obsolete and preserve only unique archaeology that is not already represented by the agent index or `known-hazards/README.md`.

**Implementation owner:** Quartermaster  
**Verification owner:** Auditor

### 2. Doctrine has three active-looking roots and conflicting status

Doctrine currently appears under:

- `shared/doctrine/`
- `doctrine/`
- `doctrines/`

The singular `doctrine/` root contains overlapping Mirror Problem, Viral Infrastructure, and Floor-Is-A-Job material in:

- `doctrine/combined_arms_with_swords_and_identity.md`
- `doctrine/human_ai_symbiosis_mirror_problem.md`

The plural `doctrines/` root contains short legacy doctrine notes that claim promotion but lack owner, date, acceptance criteria, canonical path, and retrieval keywords.

Status also contradicts itself:

- `shared/doctrines.md` presents Feed Is The Battlefield and Dashboard Failure as inherited defaults.
- `shared/doctrine-registry.md` leaves both pending review.
- `scratch/ore-worth-promoting.md` says both need stronger evidence or demotion.

**Repair:** Declare `shared/doctrine/` the canonical promoted-doctrine root. Treat `doctrine/` and `doctrines/` as legacy intake until each file is merged, promoted, or marked obsolete. Normalize status in the registry first, then update defaults and indexes from that decision.

**Implementation owner:** Quartermaster  
**Disposition owner:** Crucible  
**Verification owner:** Auditor

### 3. Valuable files are orphaned or weakly routed

High-value files without a reliable main-entry retrieval path include:

- `steering.md`
- `shared/timeline.md`
- `reports/end_of_day_capability_report_2026_06_23.md`
- `MANIFEST_AGENTS_AND_HAZARDS.md`
- large parts of `content-factories/`, `known-hazards/`, `reports/`, `sim/`, `simulation/`, and `tools/`

`shared/index/repository-map.md` still reflects an older, smaller repository shape and omits several current roots. Its current external-code-review route also includes a device-local absolute path, which cannot orient a clean clone.

**Repair:** Update the repository map from the current tree, link `steering.md` in the bootstrap route, add explicit routes for hazards, factories, reports, and tools, and replace device-local references with repository-relative or externally identified dependencies.

**Implementation owner:** Cartographer  
**Preservation owner:** Quartermaster  
**Verification owner:** Auditor

### 4. Goblin generation exists in three competing homes

The same generation substrate appears under:

- `content-factories/goblin/`
- `simulations/goblin/`
- `sim/goblin/`

The first two include overlapping behavior models and queryable-generation concepts; the third is an active seven-line stub. `shared/doctrine/content-factory-pattern.md` already names `content-factories/goblin/` as its source artifact.

**Repair:** Preserve `content-factories/goblin/` as the canonical generation factory. Compare the simulation package for unique stateful or consequence-bearing behavior. Move only genuinely distinct simulation behavior into a named simulation layer; mark the remaining duplicates obsolete with canonical-path pointers. Remove or redirect the `sim/goblin/` stub.

**Implementation owner:** Foreman  
**Architecture owner:** Cartographer  
**Verification owner:** Auditor

### 5. The ore queue has become a mixed promotion, proof-debt, and archaeology ledger

`scratch/ore-worth-promoting.md` says it must not become a graveyard, but several entries have already crossed their stated state:

- Accessibility as First-Class Constraint still says it needs a dedicated doctrine file, although `shared/accessibility-first.md` exists.
- Artificial Continuity is already promoted and belongs in a proof-debt ledger, not the promotion queue.
- Agent Closet, Judgment Packs, and Portable Judgment Repository substantially overlap the current Doctrine-to-Runtime Compiler candidate.
- Engineer Wizard + Goblin Familiar is described as promoted but remains in ore.
- Feed Is The Battlefield, Dashboard Failure, and Recursive Sense Synthesis remain unresolved across scratch, registry, and defaults.

**Repair:** Split the file into three explicit queues:

1. promotion candidates;
2. promoted items awaiting proof/examples;
3. disposition required: merge, reject, or obsolete.

Merge Judgment Packs and Portable Judgment Repository into the Doctrine-to-Runtime Compiler experiment. Replace the stale accessibility candidate with the narrower Disabled-User Authority Loop proof task.

**Disposition owner:** Crucible  
**Index owner:** Quartermaster  
**Verification owner:** Auditor

### 6. Ownership metadata is optional where it must be mandatory

`templates/doctrine-template.md` asks only for rule, rationale, application, and example. `shared/doctrine-registry.md` does not require Owner, Verification Owner, Canonical Path, Supersedes, or Acceptance Criteria. This produces doctrine that is meaningful but operationally unowned.

`glue/missing-glue-layers.md` also assigns some gaps to stores or candidate roles rather than an accountable current owner, including Agent Closet, Dispatcher, Quartermaster Prime, and WWDD.

**Repair:** Expand the doctrine template and registry entry format to require:

- Type
- Status
- Date
- Owner
- Verification owner
- Canonical path
- Source evidence
- Related doctrine
- Supersedes / Superseded by
- Acceptance criteria
- Retrieval keywords

Until candidate agents become real packs, assign implementation to current operational owners such as Quartermaster, Foreman, Compiler, or Auditor.

**Implementation owner:** Quartermaster  
**Schema owner:** Compiler  
**Verification owner:** Auditor

### 7. Link validation provides a false sense of completeness

`tools/validate-scratch-links.py` is useful but narrow:

- defaults only to `scratch/` and `procedures/`;
- checks ordinary Markdown links, conflict markers, duplicate headings, and fenced-code balance;
- ignores backtick path references, orphaned files, missing index entries, status contradictions, duplicate canonical names, absolute workspace dependencies, and missing owners.

No confirmed broken relative Markdown links were found in the audited bootstrap and index files. Repository-wide path integrity remains unproven.

**Repair:** Build a repository-wide integrity checker that emits a machine-readable report for:

- broken Markdown links;
- unresolved repository-relative code-span paths;
- device-local absolute paths;
- files unreachable from an index;
- duplicate doctrine titles and likely semantic duplicates;
- missing owner/status/canonical-path metadata;
- conflicting promotion status;
- stale scratch entries.

**Implementation owner:** Compiler  
**Verification owner:** Auditor

### 8. Open doctrine PRs need disposition, not another intake lane

Current open draft PRs show two different failure classes:

- PRs #2 and #3 are non-mergeable and based on older repository truth.
- PRs #4 and #5 are mergeable, but #5 introduces a large new theory that overlaps Artificial Continuity, operational phrases, prompt phrases, and Viral Infrastructure.

**Repair:** Rebase or close-and-extract #2 and #3 into bounded current-main changes. Review #4 as a narrow stale-doctrine reconciliation. Hold #5 until it has an explicit owner, verification owner, canonical doctrine relationship, overlap analysis, and Crucible disposition.

**Branch owner:** Foreman  
**Doctrine disposition owner:** Crucible  
**Verification owner:** Auditor

## Broken-link verdict

- **Confirmed broken relative Markdown links in the audited bootstrap path:** none found.
- **Confirmed portable-retrieval defects:** yes. Device-local absolute paths and unindexed roots remain.
- **Repository-wide integrity proof:** absent. The current validator is not broad enough to make that claim.

## Archaeology worth preserving

Preserve these as lineage rather than active competing authority:

- `shared/timeline.md` — the clearest early evolution from memory to continuity to portable judgment.
- `reports/end_of_day_capability_report_2026_06_23.md` — a compact record of the ecosystem becoming one system.
- the unique Combined Arms, Mirror Problem, Viral Infrastructure, and Floor-Is-A-Job compressions — after merging them into one canonical lineage artifact.
- registry addenda — as provenance records pointing to canonical doctrine, not substitute doctrine.
- the early markdown-only origin claim — as historical context, while correcting the current README because tools and generated corpus assets now exist.

**Owner:** Archivist  
**Verification owner:** Quartermaster

## Promotion opportunities

### Doctrine-to-Runtime Compiler

Promote by experiment, not prose: compile Quartermaster into a versioned runtime manifest with source hashes, responsibility, tool boundaries, approval policy, evidence contract, and cold-agent test.

**Owner:** Compiler  
**Verification:** Auditor

### Scope and Authority Intersection

Promote after negative tests for wrong actor, wrong project, disallowed tool, and missing mutation approval.

**Owner:** Auditor  
**Implementation partner:** Compiler

### Delivered-Artifact Acceptance Packet

Promote after one artifact proves repository, runtime, visual, accessibility, and human truth without collapsing them into a single green badge.

**Owner:** Auditor  
**Implementation partner:** Foreman

### Disabled-User Authority Loop

Promote after one intended-user task card records screen-reader, voice/keyboard, recovery, completion, and the disabled user's verdict separately from automated checks.

**Owner:** Holocron  
**Verification:** Auditor

### Repository Integrity Graph

Promote a generated graph only after it can identify one real orphan, one duplicate, one stale status, and one missing owner, then route each to the correct repair.

**Owner:** Cartographer  
**Implementation partner:** Compiler  
**Verification:** Auditor

## Recommended repair order

1. **Authority reconciliation:** agent lists, manifest status, bootstrap route, and obsolete duplicate manifest.
2. **Crucible disposition pass:** ore queue and doctrine-status contradictions.
3. **Canonical path pass:** doctrine roots and Goblin package roots.
4. **Integrity checker:** automate links, ownership, indexes, duplicates, and stale-state detection.
5. **Archaeology preservation:** timeline, early capability report, and merged lineage artifact.

## Next smallest useful action

Create one bounded **Authority Reconciliation** change touching only:

- `README.md`
- `MANIFEST.md`
- `shared/index/repository-map.md`
- `shared/index/agent-index.md`
- `shared/agent-ecosystem.md`
- `MANIFEST_AGENTS_AND_HAZARDS.md`

Acceptance criteria:

1. One canonical current-agent list exists.
2. Sommelier and Wallfly have consistent status everywhere.
3. Reflective Cartographer is not confused with the repository-topology Cartographer candidate.
4. `steering.md`, hazards, factories, reports, and tools are reachable from the repository map.
5. The duplicate hazards manifest is marked obsolete and points to canonical replacements.
6. Every next-work item names implementation and verification ownership.
7. Auditor reads the repository from the bootstrap path and reports no contradictory role status.
