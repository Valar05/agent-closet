# Discovery Promotion Record — 2026-06-25 — Fiction Corpus Evidence Gate

Status: promoted method / content claims gated
Owning clusters: Writing Systems, Project Archaeology, AI Orchestration; light cross-link to Game Development
Source-of-truth: Agent Closet repo for corpus evidence; Drive report for promotion summary; Drive manuscripts for active prose surfaces until reconciled

## Reviewed Artifacts

Canonical GitHub evidence:

- `corpus/fiction/fiction-manifest.md`
- `corpus/fiction/canonical-corpus-map.md`
- `corpus/fiction/fiction-scene-index.md`
- `corpus/fiction/kinetic-action-evidence.md`
- `corpus/fiction/fiction-observation-ledger.md`
- `corpus/fiction/observations/README.md`
- `corpus/fiction/observations/*.md`

Drive evidence:

- `Discovery Promotion Report - 2026-06-25 - Fiction Corpus Evidence Gate + Shattered Bonds`
- `Shattered Bonds -Dorian beginning`
- `Shattered Bonds -Dorian beginning.pdf`
- `Skill Cluster - Writing Systems`
- `Drive Knowledge Index - Daily Delta`

Thunder mirror patch:

- `generated/source_refs_github/2026-06-25_fiction_corpus_promotion_source_refs.jsonl`

## Promotions

### 1. Fiction Corpus Evidence Gate

Observation:
The corpus now has enough size and alternate-source complexity that memory-based writing claims are unsafe.

Why it matters:
Without a gate, agents will overfit to favorite excerpts, recent chats, or impressive but unverified patterns.

Reusable rule:
Do not promote a full-corpus writing claim from memory, vibe, or a favorite excerpt. Promote only after the corpus has a manifest, canonical map, scene evidence, book-local observations, and cross-book corroboration.

Evidence:

- `fiction-manifest.md` defines corpus scope, priority works, and the rule that no full-corpus style claim is valid until Priority A works are verified and indexed.
- `canonical-corpus-map.md` selects mining targets without deleting alternates.
- `observations/README.md` defines the evidence ladder: scene evidence -> book observation artifact -> corpus observation ledger -> doctrine/theory promotion.

Confidence: High for method; Low-to-Medium for any specific full-corpus style doctrine until more Priority A works are indexed.

Owning cluster: Writing Systems / story archaeology; Project Archaeology / evidence gates; AI Orchestration / anti-vibe governance.

### 2. Manifest / Canonical Map Split

Observation:
The manifest and canonical map are intentionally different artifacts.

Why it matters:
A manifest preserves what exists. A canonical map chooses what gets mined first. Combining them creates source confusion and premature deletion.

Reusable rule:
Inventory and canonical target selection should be separate files when a corpus has alternates, exports, branches, or uncertain versions.

Evidence:

- `fiction-manifest.md` records Priority A and B works, alternates, exports, folders, and missing items.
- `canonical-corpus-map.md` applies selection rules: prefer Google Docs, revised/v2/v3 versions, verified user links, and `NEEDS VERIFY` when uncertain.

Confidence: High.

Owning cluster: Project Archaeology / source-of-truth selection; Writing Systems / version-aware manuscript mining.

### 3. Book-Local Observation Layer

Observation:
The new `corpus/fiction/observations/` layer prevents direct promotion from raw manuscript or chat memory into doctrine.

Why it matters:
Large creative corpora need a place to preserve local observations that are real but not yet general.

Reusable rule:
For each source artifact, preserve book-local evidence before updating cross-corpus doctrine.

Evidence:

- `observations/README.md` states that book observation files answer where evidence came from, while the corpus ledger answers what patterns recur.
- Substantial observed files exist for `revelation.md`, `omnitread.md`, `inhuman-reaches.md`, `veil-of-liquid-stars.md`, and `the-harroway-connection.md`.
- Pending placeholder files exist for works that still need direct mining, preventing memory holes without overclaiming.

Confidence: High for structure; Medium for content coverage.

Owning cluster: Writing Systems / corpus mining workflow; AI Orchestration / repository-first guardrails.

### 4. Action As State Conversion

Observation:
The Jumpy Bug / Biblical scene and action ledgers show that the useful unit of action analysis is changed state, not decorative motion.

Why it matters:
This turns prose action into a reusable diagnostic for writing and game design.

Reusable rule:
An action beat is useful when it changes tactical state, emotional state, resource state, relationship state, or institutional state.

Evidence:

- `fiction-scene-index.md` indexes Jumpy Bug scenes by scene type, density, action evidence, and notes.
- `kinetic-action-evidence.md` captures setup, movement compression, contact/interruption, consequence, new state, and pattern note.
- The Jumpy Bug entries include fly-cloud ignition, scorpion ambush, forced retreat, baby scorpion kill, web command, locust joint kill, and chitin spear build.

Confidence: High for method; Medium for corpus-wide style claim.

Owning cluster: Writing Systems / kinetic prose analysis; Game Development / action-state design.

### 5. Shattered Bonds Dorian Beginning — Local Evidence Only

Observation:
Dorian beginning produces strong local signals around armor as externalized burnout, AI auditing as moral repair, and game invite as agency trigger.

Why it matters:
This may be important Shattered Bonds evidence, but version reconciliation is not complete.

Reusable rule:
Do not promote version-local discoveries to corpus doctrine until the artifact is classified as revision, branch, prelude, replacement opening, or orphan fragment.

Evidence:

- Drive active surface: `Shattered Bonds -Dorian beginning`.
- Drive PDF export exists and should remain secondary unless it proves structurally different.
- `shattered-bonds-online.md` is still marked placeholder / needs version reconciliation and direct mining.
- `canonical-corpus-map.md` marks Shattered Bonds / Shattered Bonds Online as `NEEDS VERSION VERIFY`.

Confidence: Medium for local observations; Low for corpus-level promotion.

Owning cluster: Writing Systems / wound-to-mechanic mapping; AI Orchestration / assistant-as-conscience interface.

## Duplicate And Source-Of-Truth Decisions

- Agent Closet corpus files are canonical for fiction archaeology evidence.
- Drive promotion reports are summary mirrors and routing records, not canonical corpus evidence.
- Drive manuscripts remain source-of-truth for prose until represented by repo evidence or explicit exports.
- Shattered Bonds Google Doc is active review surface; PDF is export/archive evidence unless newer/cleaner/different.
- Fiction manifest and canonical map are not duplicates.
- Book observation files and corpus observation ledger are not duplicates.

## Archive / Merge Guidance

Archive candidates:

- exact PDF exports when equivalent Google Docs exist
- stale Drive mirrors of Agent Closet corpus files that do not link back to repo truth
- raw chat-only fiction claims after captured into repo artifacts

Hold:

- Shattered Bonds Online v2, v3, and Dorian beginning until version reconciliation completes
- old manuscript alternates until the canonical map marks them obsolete
- full-corpus action/style claims until at least three Priority A works corroborate them

Merge later:

- Reusable fiction archaeology method should be merged into a durable Writing Systems subskill.
- `kinetic-compression.md` should be patched after two more Priority A action ledgers corroborate Jumpy Bug.

## Acceptance Criteria

This promotion is valid when future agents:

- start fiction mining from the manifest and canonical map
- create or update book-local observation artifacts before corpus-level promotion
- treat Shattered Bonds Dorian beginning as local evidence until version reconciliation
- route Thunder mirror claims back to live Agent Closet evidence
- avoid confident full-corpus claims from chat memory
