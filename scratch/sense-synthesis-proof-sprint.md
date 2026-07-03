# Sense Synthesis Proof Sprint

Status: scratch workflow
Date: 2026-07-03
Owners: Quartermaster / Prospector

Related:

- [Sense Synthesis Research Manifest](research-manifest-sense-synthesis.md)
- [Sense Synthesis Evidence Matrix](sense-synthesis-evidence-matrix.md)
- [Drink Observation Ledger](drink-observation-ledger.md)
- [Bitters Contribution Map](bitters-contribution-map.md)
- [Research Corpus Sense Synthesis README](../discoveries/research-corpus/sense-synthesis/README.md)

## Purpose

Exploit the Sense Synthesis scaffold to the hilt without skipping the proof loop.

The sprint turns research, experiments, and pantry mapping into promotion-quality evidence while preserving the scratch boundary.

## Sprint Loop

1. Select one matrix claim.
2. Check whether it already has internal corpus evidence.
3. Attach at least one research source ID from `discoveries/research-corpus/sense-synthesis/manifest.jsonl`.
4. Pre-register a drink experiment in [Drink Observation Ledger](drink-observation-ledger.md).
5. Build and taste only after prediction is written.
6. Record observation and deviation.
7. Update the matrix status.
8. Run Quartermaster and Prospector gates.

## Quartermaster Gate

Pass only when:

- links resolve,
- raw chat exports remain local-only,
- unlicensed full-text research is not committed,
- safety-sensitive notes stay scratch,
- no promoted `shared/` doctrine is created,
- observations are not backfilled as if they were predicted.

## Prospector Gate

Pass only when:

- the claim matters beyond a recipe,
- the experiment can falsify or narrow the claim,
- the source changes confidence rather than adding decoration,
- the next ore target is explicit: `Drink Simulation` domain pack or parent `Perceptual Composition`.

## Sprint Backlog

| Order | Work item | Output | Gate |
|---|---|---|---|
| 1 | Validate research packet | `manifest.jsonl` passes validator | Quartermaster |
| 2 | Run Preserved Orange hydration test | ledger observation and deviation | Quartermaster / Prospector |
| 3 | Run still vs carbonated base test | matrix update for carbonation hidden work | Prospector |
| 4 | Run two gentian tonic illusion tests | matrix update for emergent tonic perception | Prospector |
| 5 | Run shared backbone mode split | matrix update for Hydration vs Ritual rubrics | Quartermaster / Prospector |
| 6 | Fill bitters contribution map for at least two bottles | contribution records with dose/failure | Quartermaster |
| 7 | Decide parent target | scratch recommendation: Drink Simulation or Perceptual Composition | Quartermaster / Prospector |

## Validation Commands

```sh
python tools/validate-scratch-links.py scratch procedures discoveries/research-corpus
python tools/validate-sense-synthesis-research.py discoveries/research-corpus/sense-synthesis/manifest.jsonl
git diff --check
git status --short
```

## Promotion Hold

Do not create `skills/drink-simulation.md` or move this into `shared/` until:

- five experiments have observations and deviations,
- at least one bitters contribution map has real observations,
- the matrix shows which claims survived falsification,
- Quartermaster and Prospector both sign off.

## Retrieval Keywords

sense synthesis proof sprint, drink simulation sprint, Quartermaster Prospector gate, perceptual composition proof loop, drink compiler evidence workflow
