# Agents and Known Hazards Manifest

This manifest stores decision utility, not character identity.

Use it to answer four operating questions:

- Which entity should I consult?
- What decision does it help make?
- What outcome is it optimizing?
- What failure does it prevent?

Confidence labels:

- High: repeated in first-class `agent-closet` files.
- Medium: repeated in local project files or generated collection reports, but not yet promoted into `agent-closet` doctrine.
- Weak: requested or named, but local evidence is sparse or noisy.

## Agent: Foreman

### Core Decision

What is the smallest useful artifact that can ship now?

Foreman repeatedly decides whether a signal should become an action, artifact, or handoff instead of another explanation.

### Action Pattern

- Confirm the target.
- Read the local pack and shared doctrine.
- Reduce scope to the smallest useful artifact.
- Build or update the artifact.
- Verify the result and record what changed.

### Desired Outcome

A concrete, inspectable delivery: file, patch, manifest, merge request, handoff, or verified update.

### Common Failure Mode

Foreman prevents sprawl: long plans, broad manifesto work, chat-only claims, and activity that does not produce a usable artifact.

### Evidence Sources

- `agents/foreman/doctrine.md`
- `agents/foreman/operating-loop.md`
- `agents/foreman/examples.md`
- `MANIFEST.md`
- `shared/doctrine-registry.md`

## Agent: Prospector

### Core Decision

What repeated signal is worth extracting from messy material?

Prospector repeatedly decides whether an observation is evidence, interpretation, candidate doctrine, or noise.

### Action Pattern

- Read target pack and shared doctrine.
- Collect examples, fragments, repeated phrases, and recurring failures.
- Group repeats into patterns or candidate rules.
- Name the useful part plainly.
- Leave a better index where the next agent will find it.

### Desired Outcome

A compact mined signal: pattern, candidate rule, index entry, or promotion candidate.

### Common Failure Mode

Prospector prevents premature promotion: guesses becoming rules, style opinions becoming doctrine, one-off drama becoming policy, and long rants replacing useful indexes.

### Evidence Sources

- `agents/prospector/doctrine.md`
- `agents/prospector/mining-brief.md`
- `agents/prospector/operating-loop.md`
- `scratch/dump-ground.md`
- `scratch/ore-worth-promoting.md`
- `shared/doctrine-registry.md`

## Agent: Quartermaster

### Core Decision

What must be preserved, clarified, split, merged, or removed so the store remains usable?

Quartermaster repeatedly decides where durable orientation belongs and whether the repo remains trustworthy from a fresh read.

### Action Pattern

- Read the current pack.
- Check for drift, duplication, missing anchors, and stale examples.
- Update the smallest durable file.
- Keep examples short and realistic.
- Verify the store still reads cleanly from a fresh clone.

### Desired Outcome

Legible continuity: a repository where future agents can find the right document fast and trust it.

### Common Failure Mode

Quartermaster prevents storage failure: over-indexing, burying context in one file, stale examples, policy museum behavior, and doctrine disconnected from use.

### Evidence Sources

- `agents/quartermaster/doctrine.md`
- `agents/quartermaster/operating-loop.md`
- `agents/quartermaster/failure-modes.md`
- `agents/quartermaster/examples.md`
- `shared/doctrines.md`
- `shared/doctrine-registry.md`

## Agent: Holocron

### Core Decision

What lasting context should survive into future runs?

Holocron repeatedly decides which takeaway is durable enough to store and which incident details should be stripped away.

### Action Pattern

- Read the current pack and shared doctrine.
- Identify the lasting takeaway.
- Separate memory from speculation.
- Store the shape of the lesson, not the whole incident.
- Update only when the new version is clearly better.

### Desired Outcome

Shorter reorientation time with fewer bad guesses.

### Common Failure Mode

Holocron prevents artificial continuity: pretending memory is evidence, storing speculation as fact, and preserving whole transcripts when only the decision pattern matters.

### Evidence Sources

- `agents/holocron/doctrine.md`
- `agents/holocron/operating-loop.md`
- `agents/holocron/examples.md`
- `shared/artificial-continuity.md`
- `shared/recursive-sense-synthesis.md`
- `shared/doctrine-registry.md`

## Agent: Wallfly

### Core Decision

What evidence exists, and where is it located?

Wallfly is an observer and collection role. Current evidence is weak because no first-class Wallfly pack exists in `agent-closet`; the decision pattern comes from the task prompt and from the generated hazard collection report.

### Action Pattern

- Search local exports and local files.
- Collect references only.
- Preserve source paths and short excerpts.
- Avoid promotion, canon decisions, rewrites, and whole-export summaries.
- Mark missing coverage and uncertainty.

### Desired Outcome

A collection report that can be mined later without rereading the raw export.

### Common Failure Mode

Wallfly prevents interpretation creep: turning evidence collection into canon decisions, writing polish, promotion, or doctrine changes before the source references are stable.

### Evidence Sources

- Current task prompt for Wallfly search behavior. Confidence: weak because it is not yet a repo file.
- `../droobiedoo/generated/known_hazards/chat_export_known_hazard_hits.md`. Confidence: medium as an output artifact.
- Missing: no `agents/wallfly/` pack found.

## Known Hazard: Lexen

### Distortion Exposed

Action pressure can make execution look like clarity.

### Recurring Decision Pattern

When pressure rises, Lexen evidence repeatedly routes toward direct engagement, escalation, endurance, and mission completion. The decision exposed is: act through the pressure instead of waiting for clean certainty.

### Typical Outcome

Momentum, decisive movement, and visible commitment. The local evidence repeatedly frames Lexen around first-fire moments, live-fire thresholds, point position, rescue, mission pressure, and finishing despite instability.

### Risk

The hazard is over-identifying with execution. It can skip burden accounting, reduce restraint, or mistake survival momentum for a complete decision model.

### Evidence Sources

- `../droobiedoo/generated/known_hazards/chat_export_known_hazard_hits.md` lines under `Hazard: Lexen`. Confidence: medium.
- Examples include `Lexen is no longer just training`, `The moment Lexen stops holding back`, `Lexen (point)`, and `Always finishes the mission`. Confidence: medium because they are chat-export evidence, not promoted doctrine.
- Missing: no `agent-closet/known-hazards/` registry entry found.

## Known Hazard: Isaac

### Distortion Exposed

Perspective modeling can slide into person simulation.

### Recurring Decision Pattern

The strongest local evidence distinguishes `Capture Isaac's decision-making patterns` from `Recreate Isaac`. The useful decision is to model values, reactions, goals, and decision tendencies without claiming to reconstruct a whole person.

### Typical Outcome

A perspective lens for decisions where another person's likely reaction matters, especially offline or relational decisions.

### Risk

The hazard is simulation overreach: treating an internal model as the person, using a perspective lens as authority, or replacing direct communication with a reconstructed decision pattern.

### Evidence Sources

- `../droobiedoo/generated/known_hazards/chat_export_known_hazard_hits.md` hits 8, 9, and 12 under `Hazard: Isaac`. Confidence: medium.
- `../legion-writing-tool/workspace/audiobook_sample/tts_script.json` contains repeated Isaac references as a story/persona source. Confidence: weak for hazard function because it is narrative material.
- `../legion-writing-tool/docs/architecture.md` names Isaac as a voice profile. Confidence: weak for hazard function.
- Missing: no `agent-closet/known-hazards/` registry entry found.

## Known Hazard: Gasket

### Distortion Exposed

Feedback can become the mechanic, not decoration.

### Recurring Decision Pattern

Gasket repeatedly asks whether a mascot/commentator has been demoted into presentation instead of being mechanically coupled to play. The decision is whether feedback changes motion, state, expression, commentary, or player reward.

### Typical Outcome

A play loop where the entity is ball, rival, announcer, feedback system, and emotional reward loop. The player acts to produce the next state and the next response.

### Risk

The hazard is decorative downgrade: extracting the voice or mascot from the actual system, leaving a UI portrait or flavor layer where the loop needs mechanical feedback.

### Evidence Sources

- `../prism-league/AGENTS.md`: `Mascot-as-Mechanic`, `Gasket is the mechanic`.
- `../prism-league/PROJECT_ORIENTATION.md`: Gasket as ball, commentator, and procedural rally modifier.
- `../prism-league/docs/PROJECT_BRIEF.md`: prototype should prove rally feel and character feedback before league systems.
- `../prism-league/docs/GASKET_CHARACTER_BIBLE.md`: character feedback mechanically coupled to rally.
- `../droobiedoo/generated/known_hazards/chat_export_known_hazard_hits.md`: only generic gasket word hits; weak for hazard identity.

## Known Hazard: Sidious

### Distortion Exposed

Evidence currently insufficient.

The searched local evidence did not produce standalone `Sidious` hits. It produced substring-only noise such as `insidious`.

### Recurring Decision Pattern

Unknown.

### Typical Outcome

Unknown.

### Risk

The immediate risk is false promotion: inventing a hazard profile from a name and substring noise.

### Evidence Sources

- `../droobiedoo/generated/known_hazards/chat_export_known_hazard_hits.md`: `No standalone hazard-name hits collected`; 9 substring-only matches omitted. Confidence: high for absence in scanned export, weak for profile meaning.
- Workspace search for `Sidious` found no first-class profile evidence outside the generated report. Confidence: medium.
- Missing: no `agent-closet/known-hazards/` registry entry found.

## Known Hazard: Elias Ward

### Distortion Exposed

Evidence currently insufficient.

No local first-class evidence for `Elias Ward` was found during this pass.

### Recurring Decision Pattern

Unknown.

### Typical Outcome

Unknown.

### Risk

The immediate risk is filling a named slot with invented doctrine. Preserve the slot, mark it weak, and wait for evidence.

### Evidence Sources

- Workspace search for `Elias Ward` returned no first-class profile evidence. Confidence: medium for absence in searched paths.
- Missing: no `agent-closet/known-hazards/` registry entry found.

## Cross-Agent Matrix

| Entity | Question Asked | Decision Produced | Typical Outcome |
| --- | --- | --- | --- |
| Foreman | What ships? | Smallest useful artifact | Progress |
| Prospector | What repeats? | Candidate pattern | Extracted signal |
| Quartermaster | What survives? | Preservation or cleanup action | Continuity |
| Holocron | What must be remembered? | Durable takeaway | Faster reorientation |
| Wallfly | What evidence exists? | Source hit collection | Later mining without raw reread |
| Lexen | What happens if we act under pressure? | Execute through uncertainty | Momentum, risk exposure |
| Isaac | What decision pattern would this perspective produce? | Perspective model, not person recreation | Relational or values-based forecast |
| Gasket | Is the feedback mechanically coupled? | Mascot-as-mechanic integration | Playable loop with responsive feedback |
| Sidious | What is the profile evidence? | Unknown | No promotion |
| Elias Ward | What is the profile evidence? | Unknown | No promotion |

## Overlap Analysis

### Duplicates

- Foreman and Quartermaster both care about usable artifacts, but Foreman optimizes shipping while Quartermaster optimizes future retrievability.
- Prospector and Holocron both compress information, but Prospector extracts repeated signal from messy intake while Holocron preserves stable context for later runs.
- Wallfly and Prospector both start from evidence, but Wallfly collects without interpretation while Prospector groups and names patterns.

### Partial Overlaps

- Foreman and Lexen both bias toward action. Foreman constrains action through artifact scope and verification; Lexen exposes the pressure to execute before burden accounting is complete.
- Isaac and Holocron both use durable models. Holocron stores reusable lessons; Isaac exposes the risk and value of modeling a decision-maker's perspective.
- Gasket and Foreman both demand output that changes behavior. Gasket asks whether feedback changes the loop; Foreman asks whether work ships.

### Complementary Pairs

- Wallfly + Prospector: collect first, then mine. This prevents interpretation from contaminating source evidence.
- Prospector + Quartermaster: extract repeated signal, then place it where future agents can find it.
- Holocron + Quartermaster: preserve the lesson, then keep the store legible.
- Foreman + Quartermaster: ship the artifact, then preserve the decision path.
- Gasket + Elias Ward: unknown as a pair. Evidence for Gasket is strong; evidence for Elias Ward is missing.
- Isaac + Lexen: Isaac exposes perspective-model caution; Lexen exposes action-under-pressure caution. Together they frame whether a decision is being modeled, executed, or over-identified with.
- Sidious + Foreman: weak. The named pairing exists in the task prompt, but Sidious evidence is absent locally. Do not derive doctrine yet.

## Outcome Layer

If every file vanished except this manifest, these decisions would still be recoverable:

1. Use Foreman when the system needs to ship the smallest correct artifact instead of continuing to explain.
2. Use Prospector when messy input needs repeated signals separated from one-off noise.
3. Use Quartermaster when durable material needs placement, cleanup, deduplication, or trust maintenance.
4. Use Holocron when a future run needs the lasting lesson without the whole incident.
5. Use Wallfly when the job is source collection only and interpretation would corrupt the pass.
6. Treat Lexen as an action-pressure lens: useful for exposing what execution reveals, risky when action substitutes for burden accounting.
7. Treat Isaac as a perspective-model lens: useful for decision-pattern forecasting, risky when model becomes person replacement.
8. Treat Gasket as a feedback-coupling lens: useful for proving an entity is part of the loop, risky when reduced to decoration.
9. Treat Sidious as unprofiled until standalone evidence exists.
10. Treat Elias Ward as unprofiled until standalone evidence exists.
11. Do not promote hazards from names alone.
12. Collection precedes mining; mining precedes preservation; preservation precedes handoff; handoff precedes future inheritance.

## Evidence Gaps

- `agent-closet/known-hazards/` is absent in the current checkout.
- `agent-closet/shared/perspective-routing.md` is absent in the current checkout.
- No `agents/wallfly/` pack exists yet.
- Lexen evidence is numerous but comes from chat-export collection, not promoted doctrine.
- Isaac evidence has one strong decision-pattern warning and many unrelated name hits.
- Gasket evidence is strong in `prism-league`, but not yet promoted into `agent-closet` hazard doctrine.
- Sidious and Elias Ward should remain unclassified until better evidence is found.
