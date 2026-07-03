# Sense Synthesis Research Corpus

Status: discovery metadata scaffold
Date: 2026-07-03
Owners: Quartermaster / Prospector

Related:

- [Sense Synthesis Research Manifest](../../../scratch/research-manifest-sense-synthesis.md)
- [Sense Synthesis Evidence Matrix](../../../scratch/sense-synthesis-evidence-matrix.md)
- [Drink Simulation Sense Synthesis Collation](../../../scratch/drink-simulation-sense-synthesis-collation.md)

## Purpose

Hold metadata for external research used to support or challenge Drink Simulation / Sense Synthesis claims.

This directory is not a dumping ground for full-text research blobs.

## Allowed Contents

- `manifest.jsonl` source metadata.
- Short derivative notes when needed.
- Local copies only when redistribution or local archival rights are clear.

## Not Allowed

- Raw `droobiedoo/wwdd` chat export files.
- Copyrighted full-text blobs without rights clarity.
- Recipe archives that do not test a doctrine claim.
- Wellness or supplement claims without safety review.

## Manifest Schema

Each line in `manifest.jsonl` should be one JSON object with these fields:

```json
{
  "id": "sense-synthesis-0001",
  "title": "",
  "source_url": "",
  "doi": "",
  "source_type": "journal article / government guidance / book metadata / university reference / other",
  "local_path": "",
  "sha256": "",
  "claim_tags": [],
  "lever_tags": [],
  "mode_tags": [],
  "safety_domain": "none / hydration / alcohol / fermentation / medical / supplement",
  "rights_note": "metadata only / open access / public domain / permission needed",
  "status": "candidate / downloaded / cited / rejected",
  "notes": ""
}
```

## Acceptance Criteria

This corpus scaffold is working when every added source can answer:

- Which doctrine claim does it support or challenge?
- Which lever, mode, or interaction does it explain?
- Is it safe to cite casually, or does it require safety review?
- Are rights clear enough for the stored artifact?

## Retrieval Keywords

sense synthesis research corpus, drink simulation research metadata, perceptual composition evidence sources, flavor interaction research, hydration mode research, ritual mode research

## Validation

Run this after adding or changing source records:

```sh
python tools/validate-sense-synthesis-research.py discoveries/research-corpus/sense-synthesis/manifest.jsonl
python tools/validate-scratch-links.py scratch procedures discoveries/research-corpus
```
