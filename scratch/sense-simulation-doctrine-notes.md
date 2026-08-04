# Sense Simulation Doctrine Notes

Status: strong scratch ore
Date: 2026-07-03
Owner: Quartermaster
Primary downstream case: Pose Lab screenshot review

Related:

- [Sense Simulation Skill Candidate](sense-simulation-skill-candidate.md)
- [Ore Worth Promoting](ore-worth-promoting.md)
- [Perspective Coding Doctrine Notes](perspective-coding-doctrine-notes.md)
- [Pose Lab Cloud Visual Truth Self-Service Ore](pose-lab-cloud-visual-truth-self-service-ore.md)
- [Sense Synthesis](../shared/sense-synthesis.md)
- [Recursive Sense Synthesis](../shared/recursive-sense-synthesis.md)
- [Visual Truth Authority](../shared/doctrine/visual-truth-authority.md)
- [Perspective-Guided Command](../shared/doctrine/perspective-guided-command.md)
- [Perspective Routing Doctrine](../shared/perspective-routing.md)

## Purpose

Preserve Sense Simulation as experience evaluation.

This note is not a promotion to canon. It operationalizes the scratch candidate for visual review work, especially Pose Lab weapon/FK screenshots where transform metrics can be green while the screenshot still reads wrong.

The doctrine does not replace metrics. It demotes metrics to support evidence. Human-visible truth judges the experience; metrics explain why that truth succeeded or failed.

## Truth Layer Model

Never collapse these layers:

1. Physical Truth: repo state, transforms, FK/IK, sockets, matrices, tests, metrics.
2. Visual Truth: what is actually visible in the screenshot, render, video, or runtime view.
3. Perceptual Truth: what the viewer's brain believes is happening after seeing the artifact.
4. Behavioral Truth: what the user or player will trust, do, ignore, or reject because of that perception.

Primary question:

> What would a human believe after seeing this for one second?

Only after answering that should the evaluator ask which metrics explain the belief.

## Pose Lab Screenshot Evaluation Mode

For Pose Lab weapon and FK review, simulate perception before reading transform data.

Primary question:

> Does the viewer believe the weapon is held by the character?

Required subquestions:

- Who visually owns the weapon?
- Does the hand own it?
- Does the forearm own it?
- Does the world own it?
- Does the camera own it?
- Does it float, orbit, slide, lag, or pivot around an impossible point?
- Does the wrist appear to drive it?
- Can the eye identify the intended grip point?
- Does the blade project naturally from the fist?
- Does the pose read as intentional or broken?

## Perceptual Vocabulary

Use experience language in visual reports:

- held
- pinned
- floating
- orbiting
- sliding
- lagging
- world-attached
- camera-attached
- wrist-broken
- wrong-owner
- disconnected
- plausible
- confident grip
- weak grip
- impossible anatomy
- visual no-op
- metric-green / human-red

This vocabulary is not decorative. It names the perceptual failure that metrics must explain.

## Metric-vs-Screenshot Conflict Rule

If Physical Truth is green but Visual Truth is red, the build is red.

If metrics are green but the screenshot looks wrong, metrics are proxy evidence, not acceptance evidence.

If an offline gate reports `hilt pinned` while the screenshot reads `wrong-owner` or `floating`, the correct result is split truth:

- Physical Truth: green or partially green.
- Visual Truth: red.
- Perceptual Truth: red.
- Behavioral Truth: user cannot trust the fix.

The next action is to explain the split, repair the gate, or identify the coordinate-frame/runtime mismatch. It is not to tune offsets until a metric passes.

## Example Application: Pose Lab Weapon/FK Evaluation

Current human observation to preserve:

- The T-pose screenshot is visually correct for T-pose/reference pose.
- Other screenshots show lack of FK hierarchy and/or incorrect orientation.
- The failure is not merely numeric; it is perceptual ownership failure.
- The weapon does not convincingly read as owned by the hand or arm.
- A correct evaluator flags this as red even if transform metrics pass.

Reusable rule:

> A weapon is not accepted because a socket, marker, or transform is correct. It is accepted only when the screenshot makes the viewer believe the character owns the weapon through the hand/arm relationship.

For Pose Lab, a green report must say what the viewer believes, not only where the socket is.

## Acceptance Criteria

Sense Simulation is working in screenshot review when:

- the report starts with expected experience and observed experience,
- the visible artifact is inspected before metrics are cited,
- the expected relationship and actual relationship are both named,
- Physical, Visual, Perceptual, and Behavioral Truth are not collapsed,
- metrics are used as explanation after the visual read,
- a metric-green / human-red artifact remains red,
- the final verdict uses perceptual vocabulary, not only transform vocabulary.

## Promotion Gate

Keep this in scratch until repeated use proves the grammar across domains.

Promotion needs evidence from more than Pose Lab, such as:

- UX screenshot review where correct layout still creates hesitation or confusion,
- accessibility review where visual or interaction design fails a specific user reality,
- game-feel review where timing/animation reads wrong despite valid state,
- Drink Simulation or perceptual composition logs where predicted experience beats ingredient identity.

Quartermaster gate:

- preserve source custody, scratch boundary, links, and evidence quality.

Prospector gate:

- prove this predicts human perception better than implementation-first reasoning.

Foreman gate:

- require an executable acceptance rubric before using it to block or pass a build.

Gasket gate:

- reject any report that uses metrics to excuse a visibly wrong experience.

Wallfly gate:

- keep retrieval terms and cross-links discoverable.

She-Raw gate:

- keep the evaluator able to ask, "what does this actually feel like?"

Holocron gate:

- teach future agents to judge screenshots as human experience, not metric diagrams.

## Pose Lab Visual QA Sense Simulation Contract

Do not edit Pose Lab from Agent Closet unless explicitly instructed.

Downstream handoff for Pose Lab agents:

- Screenshot truth beats metric-only claims.
- Every visual fix must include human-visible acceptance criteria.
- Transform deltas are diagnostic, not proof.
- A fix is not accepted until the screenshot reads correctly.
- If browser/runtime truth disagrees with offline metrics, report split truth instead of claiming success.
- For weapon/FK work, ask first whether the viewer believes the hand owns the weapon.

## Retrieval Keywords

sense simulation, experience evaluation, perceptual truth, behavioral truth, human-visible truth, screenshot evaluation, Pose Lab screenshot review, FK visual ownership, weapon held by hand, metric-green human-red, perceptual composition, visual truth authority, sense synthesis
