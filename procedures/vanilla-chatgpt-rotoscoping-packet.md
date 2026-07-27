# Vanilla ChatGPT Rotoscoping Packet

Type: Procedure / cold-start packet  
Status: Gold — reusable native-chat workflow  
Date: 2026-07-27  
Owner: Foreman  
Authority owner: Quartermaster  
Acceptance authority: Human reviewer  
Retrieval keywords: vanilla ChatGPT, rotoscoping, rotoscopy, video-to-animation, character swap, contact sheet, native image generation, no Home Center, Satan's Toes

> [!WARNING]
> **THIS PACKET IS NOT FOR WORKERS WITH HOME CENTER.**
>
> This is a human-operated fallback for an ordinary ChatGPT conversation using native file upload, image understanding, image generation, and data analysis.
>
> If the conversation has Home Center, Command Center, durable workers, or the installed `rotoscoping` skill, stop. Do not use this packet. Invoke the installed `rotoscoping` skill and its job-addressed production lane instead.
>
> Mixing the vanilla and Home Center paths creates split authority, duplicate generations, lost approvals, and output collisions. Pick one factory.

## Purpose

Turn an owned or authorized video—or an already ordered contact sheet—into a different character performing the same fixed-camera motion.

The source performance is immutable motion authority. The target reference is identity authority. Image generation may redraw appearance; it may not rewrite the action.

This packet deliberately avoids:

- Home Center and Command Center
- background workers or delegated agents
- MCP tools and cloud job queues
- GitHub, Drive publication, or repository mutation
- GLBs, rigs, Blender, and mandatory 3D character animation

Use 3D only when the result truly requires arbitrary camera changes, unseen body surfaces, exact spatial collision volumes, dynamic relighting, or structurally editable motion. Fixed-camera animation does not owe the skeleton bureaucracy rent.

## What vanilla ChatGPT must have

Before beginning, the conversation must be able to:

1. accept the source video or ordered contact sheet;
2. accept separate character reference images;
3. inspect images and video;
4. run native image generation or image editing;
5. use data analysis/code execution to extract frames, build and split sheets, and reconstruct a GIF or MP4;
6. return generated files for immediate download.

If a capability is missing, stop at that boundary and say exactly what external artifact the human must supply. Do not claim a hash, frame extraction, generated image, split frame set, or runtime preview that does not exist.

## The five authorities

Keep these separate throughout the run:

| Authority | Canonical evidence | Owns |
|---|---|---|
| Motion | Original uploaded video or approved ordered sheet | Pose order, camera, crop, contacts, screen direction, occlusion |
| Identity | Approved character references plus written identity lock | Anatomy, costume, equipment, materials, palette |
| Render | One generated whole-sheet candidate | The pixels produced by a specific generation |
| Timing | Source timestamps or an explicitly approved timing map | Holds, cadence, action duration, loop seam |
| Acceptance | Human watchdown plus mechanical checks | Whether the result actually works |

When authorities disagree, report the disagreement before changing anything. A beautiful generated pose does not outrank the source performance. A correct file count does not outrank a visibly wrong animation.

## Session survival rule

Vanilla conversations are not durable factories. At the end of every gate:

1. return the named artifacts as downloadable files;
2. return a short `CHECKPOINT.md` containing source identity, decisions, accepted files, rejected files, and the exact next gate;
3. tell the human to download the checkpoint before proceeding.

If the session later loses access to an artifact, ask for that named checkpoint artifact to be re-uploaded. Do not reconstruct approved state from conversational memory.

## Human intake card

The human supplies this with the uploads:

```text
I own or am authorized to transform this motion source: yes/no
Source: <video or ordered contact sheet filename>
Action boundary: <whole clip or start/end time>
Action: <plain-language progression>
Loop: yes/no
Planted contact or anchor: <foot, hand, hip, prop, or none>
Screen direction: <left/right/toward camera/away>
Camera and crop: <preserve full frame or one fixed crop>
Audio: preserve/remove/not present
Target character references: <filenames>
Identity invariants: <anatomy, appendages, costume, equipment, proportions>
Background: preserve / flat removable color / opaque replacement
Delivery: GIF / MP4 / ordered frames / sprite sheet
Resolution and playback target: <if known>
```

If ownership or authorization is `no` or unclear, do not begin the transformation.

## Gate 0 — Paste the bootstrap

Paste this into a new ordinary ChatGPT conversation:

```text
You are running a human-operated vanilla ChatGPT rotoscoping session with no Home Center.

THIS PROCEDURE IS SPECIFICALLY NOT FOR HOME CENTER WORKERS. Do not invoke or simulate Home Center, Command Center, MCP, cloud workers, GitHub, Drive publication, Blender, GLB, or a background job. Use only the native capabilities available inside this conversation: file upload, image/video understanding, image generation/editing, and data analysis.

Mission:
Transfer the exact fixed-camera performance in my owned or authorized source into a different visual identity.

Constitution:
- The source performance is motion authority.
- The approved character references are identity authority.
- Generate the whole contact sheet as one identity-transfer operation.
- Preserve camera, crop, scale, anchor, screen direction, pose order, occlusion order, contact points, and cadence.
- Do not add, remove, reorder, mirror, recenter, rescale, smooth, or invent frames.
- Keep labeled review evidence separate from the unlabeled image-generation input.
- Work one gate at a time. Do not proceed past a human approval gate.
- Return real downloadable artifacts at every gate. Descriptions of artifacts are not artifacts.
- Preserve rejected candidates and the reason for rejection.
- Mechanical checks cannot accept visual motion. I am the final acceptance authority.

First, perform only a capability check and request the Human Intake Card plus uploads. Do not generate anything yet.
```

Pass Gate 0 only when ChatGPT names the native capabilities it can actually use and requests the intake without pretending to have started.

## Gate 1 — Lock the source

Upload the source and completed Human Intake Card. Then paste:

```text
Perform source intake only. Do not generate the target character.

1. Inspect the uploaded source at normal speed.
2. Record filename, duration, displayed orientation, displayed dimensions, frame rate when available, audio presence, and the requested action boundary.
3. Compute SHA-256 for the exact uploaded source bytes if data analysis exposes them. If it cannot, record hash as unavailable; never invent one.
4. Apply one fixed crop only if I requested it. Never crop or recenter individual frames.
5. Describe the action progression, planted contacts, screen direction, camera, important occlusions, anticipation, extremes, contact, recoil, recovery, and loop seam.
6. Return `SOURCE-LOCK.md`.
7. Stop for my approval.
```

Reject Gate 1 when:

- the action boundary is vague;
- the displayed orientation is wrong;
- the crop changes between frames;
- ownership/authorization is missing;
- the assistant claims metadata it did not inspect.

## Gate 2 — Extract meaningful motion keys

After approving `SOURCE-LOCK.md`, paste:

```text
Extract a sparse key sequence that explains the approved action.

Use motion energy and action meaning, not equal time spacing. Preserve anticipation, extreme, plant/contact, recoil, recovery, and loop seam where present. Prefer 8–16 keys for a short action unless the motion proves it needs more or fewer.

Create and return:
- `motion-input.png`: the unlabeled contact sheet used for image generation;
- `motion-review.png`: the same cells with stable frame IDs and timestamps outside the image area;
- `sheet-map.json`: columns, rows, cell geometry, border/gutter, frame IDs, source times, and hold durations;
- `motion.json`: source identity, locks, ordered key list, hashes when available, and selection status `proposed`.

Use one fixed camera, crop, canvas, and subject scale. Do not label, draw arrows on, or annotate `motion-input.png`.

Then explain why each key survives and stop for my approval. Do not generate the target character.
```

Human review questions:

- Does the sheet still tell the whole action?
- Is the planted contact actually planted?
- Did anticipation, contact, recoil, or recovery disappear?
- Did screen direction or handedness flip?
- Is the first/last state correct for the intended boundary or loop?
- Are near-duplicate cells consuming space while a meaningful extreme is missing?

Revise the proposed key list until the human explicitly says it is approved. A changed key list is a new revision, not a silent overwrite.

## Gate 3 — Lock the target identity

Upload separate, approved character references. Do not place identity references inside the motion grid. Paste:

```text
Inspect the uploaded character references as identity authority.

Write and return `IDENTITY-LOCK.md` covering:
- anatomy and appendage count;
- proportions and silhouette;
- face, hair, skin, and distinguishing features;
- costume and equipment;
- palette and materials;
- handedness;
- details that must remain identical across every cell;
- details that may simplify at delivery resolution.

Identify any conflict between the target body and the source poses. Do not solve conflicts by changing motion. Stop for my approval before image generation.
```

## Gate 4 — Transfer identity across the whole sheet

After both motion and identity are approved, paste:

```text
Use native image generation/editing for one whole-sheet identity transfer.

Image roles:
- `motion-input.png` is motion authority.
- The separate approved character images are identity authority.

Redraw the subject in every motion cell as the approved target character.

Motion invariants:
- Preserve exactly the approved cell count and grid.
- Preserve camera, crop, canvas, scale, planted anchor, screen direction, pose order, silhouette changes, occlusion order, and contact points.
- Preserve the approved action progression.
- Do not add, remove, reorder, mirror, interpolate, recenter, rescale, or label frames.

Identity invariants:
- Keep one consistent character design, anatomy, appendage count, costume, equipment, palette, proportions, and materials across all cells.
- Obey `IDENTITY-LOCK.md`.

Background:
- Obey the approved background policy exactly.

Avoid:
grid changes, panel labels, text, watermark, camera drift, scale breathing, anchor crawl, limb-count drift, costume drift, melted anatomy, invented in-betweens, and per-cell compositions.

Return the original generated whole sheet as `candidate-001.png`, the exact generation instruction as `candidate-001.prompt.txt`, and a side-by-side review image comparing motion and render. Do not split or reconstruct yet. Stop for review.
```

Generate the whole sheet in one operation. Never regenerate every cell independently; that destroys shared identity, camera, and scale.

If the candidate fails, record the failure by frame and authority. Make one targeted correction. If that correction damages multiple good cells, reject it and regenerate the whole sheet from the same locked inputs. Preserve rejected candidates.

## Gate 5 — Split and reconstruct

After the whole sheet is approved, paste:

```text
Use data analysis to split the approved generated sheet deterministically from `sheet-map.json`.

Do not eyeball or hand-crop individual cells. If the generator added one outer border, measure and remove it once for the entire sheet.

Return:
- `candidate-001-frames.zip` with ordered, consistently named frames;
- `timing-map.json` preserving source timestamps/holds or the explicitly approved authored timing;
- the requested GIF or MP4 runtime preview;
- ordered frames and timing metadata as primary assets when the delivery target is a game;
- source audio only when the approved audio policy says preserve.

For a sprite sheet, build it from the accepted split frames—not directly from the generated sheet.

Stop for runtime watchdown. Do not declare acceptance.
```

For transparency, prefer a perfectly flat removable color not used by the subject. Inspect edges against black, white, and gray. Reject any matte cleanup that amputates hair, claws, feathers, weapons, smoke, or contact pixels.

## Gate 6 — Human runtime tribunal

The assistant may prepare evidence. It may not accept its own miracle.

Watch in this order:

1. source video at full speed;
2. approved source motion sheet;
3. source and generated sheets cell by cell;
4. generated frames as a rapid flip or onion skin;
5. reconstructed runtime at intended size and speed;
6. loop seam repeatedly, if applicable;
7. picture-only and audio-only, if source audio is retained.

Use this verdict table:

| Frame/time | Authority | Observed failure | Severity | Required repair |
|---|---|---|---|---|
| Example: k004 / 00:00.73 | motion | heel drifts while source remains planted | reject | restore heel anchor without recentering |

Probe for:

- pose laundering: prettier art replaced the actual pose;
- anchor crawl;
- scale breathing;
- per-cell camera forgery;
- identity or appendage mutation;
- unauthorized smoothing or invented in-betweens;
- missing anticipation, contact, recoil, recovery, or loop seam;
- mirroring or handedness reversal;
- false occlusion order;
- timing amnesia;
- matte erosion;
- codec alibis: correct dimensions and frame counts presented as visual proof.

The verdict must be one of:

- `accepted`
- `accepted-with-explicit-deviation`
- `revision-required`
- `rejected`

Silence is not approval. “Looks good” from the generating assistant is not approval. The human must watch the runtime and issue the verdict.

## Gate 7 — Release the packet

After human acceptance, paste:

```text
Assemble and return `rotoscope-release.zip`.

Include:
- original source identity and rights statement;
- `SOURCE-LOCK.md`;
- approved `motion.json`;
- `motion-input.png`;
- `motion-review.png`;
- `sheet-map.json`;
- character references and `IDENTITY-LOCK.md`;
- accepted generated whole sheet and exact prompt;
- ordered split frames;
- timing map;
- runtime GIF or MP4;
- mechanical audit or file-integrity notes;
- rejected candidates with rejection reasons;
- `VERDICT.md` containing the explicit human verdict and any accepted deviation;
- `CHECKPOINT.md` explaining how to resume in a new vanilla conversation.

Do not include claims about Home Center, workers, cloud publication, or repository state. This release proves only the artifacts produced and reviewed in this vanilla conversation.
```

## Accessibility requirements

- Give every sheet and runtime preview useful alt text.
- Use stable frame IDs in text; never rely on color alone.
- Describe each rejected frame in words as well as marking it visually.
- Return individual downloadable files before bundling so a screen-reader user is not trapped inside a ZIP.
- Keep controls and requested human replies short: `approve Gate 2`, `revise k004`, `reject candidate-001`.
- When visual evidence is inaccessible to the reviewer, obtain a trusted human visual verdict; generated descriptions are interpretation, not visual acceptance.

## Red-build stop conditions

Stop immediately when the conversation:

- tries to route the task to Home Center or a worker;
- introduces Blender, a rig, or a GLB without a stated 3D requirement;
- generates the character before source and identity locks are approved;
- redraws cells independently;
- feeds the labeled review sheet into image generation;
- loses, reorders, duplicates, mirrors, or invents a pose;
- replaces source timing with equal holds without approval;
- reports files that are not downloadable;
- claims acceptance from metadata, hashes, dimensions, or its own visual opinion;
- loses an approved artifact and tries to remember it instead of requesting re-upload.

## Final compression

The vanilla path is:

```text
Upload truth
-> lock the action
-> approve sparse keys
-> lock identity
-> redraw the whole sheet
-> split deterministically
-> restore timing
-> watch the runtime
-> preserve the packet
```

Perform truth once. Re-embody it endlessly.

The performance survives. The tollbooths do not.
