# Fiction Source Map

Status: routing bridge / active
Created: 2026-06-25
Depends on:

- `corpus/fiction/fiction-manifest.md`
- `corpus/fiction/observations/README.md`
- `corpus/fiction/fiction-observation-ledger.md`
- `corpus/fiction/fiction-scene-index.md`

## Purpose

This file connects the fiction manifest to local exports and evidence artifacts.

Shared Drive Corpus != Fiction Manuscript Corpus.

- `tools/refresh-drive-corpus.sh` syncs the shared Drive support corpus into `discoveries/drive-corpus/exports/`.
- `corpus/fiction/fiction-manifest.md` defines the canonical fiction manuscript sources.
- `corpus/fiction/observations/` stores book-local evidence.
- `corpus/fiction/fiction-observation-ledger.md` stores cross-book recurring evidence.

The shared Drive sync does not automatically export fiction manuscripts.
This map tells mining agents where fiction lives, what has evidence, and what still needs direct reading.

## Routing Rule

Do not treat support corpus exports as manuscript exports.
Do not treat observation artifacts as source manuscripts.
Do not treat the ledger as a replacement for direct reading.

Use the fiction manifest first, then this source map, then the relevant observation file.

## Priority A Works

### Omnitread

- Canonical Drive document:
  - `https://docs.google.com/document/d/1-XwFH_dk3LSBExmyPe3ZVCa2SMKt85jlL_w5TSHjfRM`
- Alternate export:
  - `https://drive.google.com/file/d/1StNk-lctRPXJieleBueKJS39yqJ0aZxd` (PDF)
- Expected local export location:
  - `discoveries/fiction-corpus/exports/omnitread/Omnitread.md` if Markdown conversion is available
  - otherwise `discoveries/fiction-corpus/exports/omnitread/Omnitread.txt`
- Observation artifact:
  - `corpus/fiction/observations/omnitread.md`
- Mining status:
  - Mined / direct pass recorded
- Evidence status:
  - Direct evidence present; not promoted

### Holding Vigil

- Canonical Drive document:
  - `https://docs.google.com/document/d/164q6UUkD3npFCoyxm6SUSubv_7WE6hKbovXqVG7aP6A` (`Revised and Improved`)
- Alternate exports:
  - `https://docs.google.com/document/d/15OMFBJakwqjr0pie4oMddstug3kTRYjWvzXoj9kqxKk` (`V2`)
  - `https://docs.google.com/document/d/1gSPbvAMc3CbPpjrbAivemL5xRJU8kz_aN77_qoP2Prk` (mining/support doc)
- Expected local export location:
  - `discoveries/fiction-corpus/exports/holding-vigil/Holding Vigil - Revised and Improved.md` if Markdown conversion is available
  - otherwise `discoveries/fiction-corpus/exports/holding-vigil/Holding Vigil - Revised and Improved.txt`
- Observation artifact:
  - `corpus/fiction/observations/holding-vigil.md`
- Mining status:
  - Pending direct mining / version verify
- Evidence status:
  - Placeholder only; no direct book-local observations yet

### Lighter Than Air

- Canonical Drive documents:
  - `https://docs.google.com/document/d/1LngEtsrWVaH5hRS5fPmS-9EGPmHfqJdRVSWsUoh1OD4` (book 1)
  - `https://docs.google.com/document/d/1LDX1m-ziKvNau0l0tU43lzgRxWtoy5mdBXpBuJSkuPQ` (book 2)
- Alternate exports:
  - `https://drive.google.com/file/d/12rVDpC-4L-qOtpZrA-aDNPY8rZnY8GC2` (TXT)
  - `https://drive.google.com/file/d/1XWpegAZDCEryoR-YCPaWCBG8NnZYJEUE` (DOCX)
  - `https://drive.google.com/file/d/1unzBvkJLxfS3A_A1lw2rr3QvekNIA4uh` (DOCX)
  - `https://drive.google.com/file/d/1Tv2l_EFFldyd229oDLtfUO-H3ypaLieL` (DOCX)
- Expected local export location:
  - `discoveries/fiction-corpus/exports/lighter-than-air/book-1/Lighter Than Air 1.md` if Markdown conversion is available
  - `discoveries/fiction-corpus/exports/lighter-than-air/book-1/Lighter Than Air 1.txt` fallback
  - `discoveries/fiction-corpus/exports/lighter-than-air/book-2/Lighter Than Air 2.md` if Markdown conversion is available
  - `discoveries/fiction-corpus/exports/lighter-than-air/book-2/Lighter Than Air 2.txt` fallback
- Observation artifact:
  - `corpus/fiction/observations/lighter-than-air.md`
- Mining status:
  - Pending direct mining
- Evidence status:
  - Placeholder only; no direct book-local observations yet

### Revelation

- Canonical Drive document:
  - `https://docs.google.com/document/d/1HW67a3Z1f3ScESNzwy2Zab4WhIxSUEjRCE-iNfhB3MU`
- Alternate exports:
  - none recorded in the manifest beyond the canonical candidate
- Expected local export location:
  - `discoveries/fiction-corpus/exports/revelation/Revelation.md` if Markdown conversion is available
  - otherwise `discoveries/fiction-corpus/exports/revelation/Revelation.txt`
- Observation artifact:
  - `corpus/fiction/observations/revelation.md`
- Mining status:
  - Mined / substantial observation pass recorded
- Evidence status:
  - Direct evidence present; not promoted

### Jumpy Bug / Biblical

- Canonical Drive document:
  - `https://docs.google.com/document/d/11bkG4pFd9I32JHTRa7h1XUUtQUZE7cUKN1iq1f2SWTA/edit?usp=drivesdk`
- Drive title:
  - `Biblical`
- Alternate exports:
  - none recorded beyond the canonical target
- Expected local export location:
  - `discoveries/fiction-corpus/exports/jumpy-bug/Biblical.md` if Markdown conversion is available
  - otherwise `discoveries/fiction-corpus/exports/jumpy-bug/Biblical.txt`
- Observation artifact:
  - `corpus/fiction/observations/jumpy-bug.md`
- Mining status:
  - Mined / scene index started
- Evidence status:
  - Direct scene evidence present; observation artifact and scene index exist

### Inhuman Reaches

- Canonical Drive documents:
  - `https://docs.google.com/document/d/1jzHCUywOx-qLJhBnQt8q8Y8FgL4wxGWez219JiSSuVQ` (revised part 1)
  - `https://docs.google.com/document/d/1MGibrNg4qqnjA0D1XEOElI27oqGPjX-MlEQiWsDICr4` (revised part 2)
- Alternate exports:
  - `https://drive.google.com/drive/folders/1_KUKqClm_ilPtmyhyHSczUsAckM9gg2T` (folder)
  - `https://docs.google.com/document/d/1DIuCFUJ7Coe49IaxWYXnNYizWiNaaGWlAQ_xQxNBt0w` (original)
  - `https://docs.google.com/document/d/18yYUeEhysOXf6x7h13TKJnQQaH8fn2cynrM9-_6BCWw` (original part 2)
  - `https://docs.google.com/document/d/1pUs6SGdz2dQ7hUB1ftQnhkh7XRiQvoTS-jGDjgdmfS0` (juicy bits)
  - `https://drive.google.com/drive/folders/1RVvFExoAvq9FDRKK7_H_gPlCUvj09qtc` (rooms folder)
- Expected local export location:
  - `discoveries/fiction-corpus/exports/inhuman-reaches/part-1-revised/Inhuman Reaches 1, Revised.md` if Markdown conversion is available
  - `discoveries/fiction-corpus/exports/inhuman-reaches/part-1-revised/Inhuman Reaches 1, Revised.txt` fallback
  - `discoveries/fiction-corpus/exports/inhuman-reaches/part-2-revised/Inhuman Reaches Pt 2 Revised.md` if Markdown conversion is available
  - `discoveries/fiction-corpus/exports/inhuman-reaches/part-2-revised/Inhuman Reaches Pt 2 Revised.txt` fallback
- Observation artifact:
  - `corpus/fiction/observations/inhuman-reaches.md`
- Mining status:
  - Mined / sequence verify complete enough for first-pass routing
- Evidence status:
  - Direct evidence present; not promoted

### Shattered Bonds / Shattered Bonds Online

- Canonical Drive document:
  - `https://docs.google.com/document/d/1Rf_AaRSRl2vV8gqRpFbcjey1EBjoDkLkKZt6unbVeXM` (`Shattered Bonds Online v2`)
- Alternate exports:
  - `https://drive.google.com/drive/folders/1wTCgBF1H_eL8PJWmYHph0l2vrHrrNzv9` (folder)
  - `https://docs.google.com/document/d/1D8WXnzNDCICTAW2C5eIh0-zK6oXRGNP9CU7XA-WnHSk` (`Shattered Bonds - Dorian beginning`)
  - `https://docs.google.com/document/d/1xvVjWImYPVxW5UKovf-PhZ6wJ0yZqopnrNfJrFPnD4g` (`Shattered Bonds v3`)
  - DOCX alternates and fragments recorded in `corpus/fiction/fiction-manifest.md`
- Expected local export location:
  - `discoveries/fiction-corpus/exports/shattered-bonds-online/Shattered Bonds Online v2.md` if Markdown conversion is available
  - otherwise `discoveries/fiction-corpus/exports/shattered-bonds-online/Shattered Bonds Online v2.txt`
- Observation artifact:
  - `corpus/fiction/observations/shattered-bonds-online.md`
- Mining status:
  - Pending version verify
- Evidence status:
  - Placeholder only; version reconciliation pending

### Fatal Vow Exception

- Canonical Drive document:
  - `https://docs.google.com/document/d/1NLMjLsSBRvIK8jYs-ttKhks3UuqdZTZstm98eC7zF18` (`v2`)
- Alternate exports:
  - `https://docs.google.com/document/d/1l5F1AAWLAO18R27VvH5wykdTSiAjgXKTZKg3akfRyTM` (original)
  - `https://drive.google.com/drive/folders/19t-nbM81NK5SknLqTIRigHlJNnGNk9Gf` (folder)
- Expected local export location:
  - `discoveries/fiction-corpus/exports/fatal-vow-exception/Fatal Vow Exception v2.md` if Markdown conversion is available
  - otherwise `discoveries/fiction-corpus/exports/fatal-vow-exception/Fatal Vow Exception v2.txt`
- Observation artifact:
  - `corpus/fiction/observations/fatal-vow-exception.md`
- Mining status:
  - Pending direct mining
- Evidence status:
  - Placeholder only; no direct book-local observations yet

### Veil of Liquid Stars

- Canonical Drive document:
  - `https://docs.google.com/document/d/1A4Ow--IuPRnrQ2hYOrW_hEGRK7KEU14py55qBprTWfM`
- Alternate exports:
  - `https://docs.google.com/document/d/12c7htN5UMG27Zc6cQlFE7MLFN4Rrm6ZzTt92j1Zw5E8` (`The Veil of Liquid Stars`)
- Expected local export location:
  - `discoveries/fiction-corpus/exports/veil-of-liquid-stars/Veil of Liquid Stars.md` if Markdown conversion is available
  - otherwise `discoveries/fiction-corpus/exports/veil-of-liquid-stars/Veil of Liquid Stars.txt`
- Observation artifact:
  - `corpus/fiction/observations/veil-of-liquid-stars.md`
- Mining status:
  - Mined / observation artifact present
- Evidence status:
  - Direct evidence present; not promoted

### Aegis of Victory

- Canonical Drive document:
  - `https://docs.google.com/document/d/1bIlXCINuMkXjVvRMUoR72xXT4_kOscteSBxVZXbpW58`
- Alternate exports:
  - `https://drive.google.com/file/d/1GCIaCRTRmsdZFFKpCduBbFuulFffWOwt` (TXT)
- Expected local export location:
  - `discoveries/fiction-corpus/exports/aegis-of-victory/Aegis of Victory.md` if Markdown conversion is available
  - otherwise `discoveries/fiction-corpus/exports/aegis-of-victory/Aegis of Victory.txt`
- Observation artifact:
  - `corpus/fiction/observations/aegis-of-victory.md`
- Mining status:
  - Pending direct mining
- Evidence status:
  - Placeholder only; no direct book-local observations yet

## Export Recommendation

Recommendation: yes, fiction manuscripts should also be exported, but not by `tools/refresh-drive-corpus.sh`.

Use a separate fiction export pass that reads `corpus/fiction/fiction-manifest.md`, resolves the canonical Google Doc entries there, and writes to a distinct local root such as `discoveries/fiction-corpus/exports/`.

Suggested layout:

- `discoveries/fiction-corpus/exports/<work>/<canonical-title>.md`
- fallback to `.txt`, `.docx`, or `.pdf` when Markdown conversion is unavailable
- keep versioned variants in sibling paths, not the same filename

Collision risks:

- repeated titles across different works
- multiple books under one work title, such as `Lighter Than Air`
- multiple revisions of one manuscript, such as `Shattered Bonds`
- alternate exports and support files with near-identical names

Provenance strategy:

- record the canonical Google Doc URL
- record the Drive file ID or folder ID when present
- keep one manifest row per exported artifact
- hash each local export
- preserve alternate versions instead of overwriting them
- keep source URLs and export format in the manifest so later agents can audit the bridge

## Retrieval Use

When searching for fiction, manuscripts, corpus, observations, or mining, read in this order:

1. `corpus/fiction/fiction-manifest.md`
2. `corpus/fiction/fiction-source-map.md`
3. `corpus/fiction/observations/README.md`
4. `corpus/fiction/fiction-observation-ledger.md`
5. `corpus/fiction/fiction-scene-index.md`
6. `skills/scene-compiler.md`

