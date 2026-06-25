# Vernepunk Discovery Simulation Layer

This is the implementable simulation layer for Vernepunk as a discovery / expedition space.

## Source Contract

Use the repo evidence before adding new mechanics:

- `README.md` and `REPO_DOCTRINE.md` define the project identity.
- `docs/doctrine/*.md` defines the reusable judgment rules.
- `corpus/distillations/**/*.md` provides source-backed primitives.
- `ml/prompts/*.md` defines the evidence-first answer contract.
- `game/simulation.mjs` shows the current playable pattern.

## Core Thesis

The player does not collect treasure.
The player reduces uncertainty.

That means the game should reward:

- better reports
- better stationing
- better procedures
- better maps
- better journal memory
- better company continuity

Not loot volume.

## Simulation Layer Overview

### 1. World layer

The world contains:

- terrain
- hazards
- hidden structures
- route segments
- weather or environmental stress
- unknown causes

### 2. Company layer

The company contains:

- roster
- roles
- fatigue
- fear
- morale
- injuries
- trust
- expertise
- jokes
- grudges

### 3. Machine layer

The machine contains:

- pressure
- heat
- fuel
- vibration
- movement mode
- maintenance backlog
- sensor confidence
- hidden modes

### 4. Awareness layer

Awareness contains:

- observer reports
- instrument reports
- rumor reports
- delayed corrections
- confidence labels
- contradictions

### 5. Memory layer

Memory contains:

- journal entries
- belief records
- corrected truths
- costs
- human detail

## State Model

### Crew/company state

Recommended variables:

- `crewRoster`
- `roleCoverage`
- `fatigue`
- `fear`
- `morale`
- `injuryLoad`
- `trust`
- `expertise`
- `grudgeLoad`
- `jokeCount`
- `availability`

### Machine state

Recommended variables:

- `boilerPressure`
- `heat`
- `fuel`
- `vibration`
- `movementState`
- `machineMode`
- `maintenanceBacklog`
- `instrumentConfidence`
- `hiddenDamage`

### Route/map state

Recommended variables:

- `currentSegment`
- `segmentConfidence`
- `surveyedSegments`
- `unknownSegments`
- `hazardMarkers`
- `drift`
- `recoverability`
- `landmarkMemory`

### Report state

Recommended variables:

- `source`
- `sourceType`
- `observation`
- `interpretation`
- `confidence`
- `delay`
- `status`
- `correctionOf`

### Journal state

Recommended variables:

- `observed`
- `believed`
- `actionTaken`
- `cost`
- `laterLearned`
- `humanDetail`
- `confidence`

## Loop Design

### Expedition loop

1. Read the current uncertainty.
2. Choose a procedure.
3. Assign a crew source.
4. Update machine and company state.
5. Reveal a report with confidence.
6. Advance the map.
7. Write the journal.

### Discovery loop

1. Detect anomaly.
2. Compare observer and instrument.
3. Evaluate confidence.
4. Stabilize the machine or environment.
5. Confirm or correct the earlier belief.
6. Store the correction.

### Experiment loop

1. Isolate one variable.
2. Log the baseline belief.
3. Apply a procedure.
4. Observe the result.
5. Measure the cost.
6. Update future decision quality.

## Mechanic Set

### Procedures

Procedures should be explicit, not generic.

Good examples:

- halt forward drive
- vent boiler pressure
- dispatch sounding crew
- reduce speed
- switch to manual gauge check
- sound the hull again
- mark the route uncertain
- write the correction into the journal

Bad examples:

- scan
- fix
- investigate
- loot
- interact

### Report mechanics

- Reports have a source.
- Reports have a confidence label.
- Reports can be contradicted.
- Reports can be corrected later.
- Reports may arrive after the world event already changed.

### Journal mechanics

- The journal records the wrong belief first if that was what the company knew.
- The correction is appended, not overwritten.
- The journal stores cost as well as fact.
- The journal preserves one human detail so the record stays lived-in.

### Map mechanics

- Unknown space should remain unknown until earned.
- Surveyed space should carry confidence.
- Route drift should be real.
- A better report should improve the map.
- A false report should still have temporary operational value.

## Pressure Clocks

Use multiple clocks instead of one failure bar.

1. Boiler pressure
2. Fuel / resource reserve
3. Crew fatigue
4. Crew fear
5. Report delay
6. Map uncertainty
7. Repair backlog
8. Social suspicion
9. Machine confidence
10. Environmental hazard pressure

These clocks create the feel of expedition labor.

## Existing Mechanics to Keep

The current Vernepunk game already proves a useful slice:

- a single crisis scene
- procedure buttons
- machine state changes
- crew voices
- awareness reports
- report confidence labels
- journal memory
- later-learned correction

Do not throw this out.
Use it as the first verified implementation of the discovery layer.

## Expansion Rules

### What to add next

- route segments with confidence
- crew source selection per report
- map reveal and correction
- machine mode changes
- delayed reports from different sources
- pressure clocks that carry across scenes
- journal revision history

### What not to add yet

- treasure inventory
- general combat engine
- open-ended skill tree
- omniscient map reveal
- abstract "scan" actions with no crew source
- world sim breadth without uncertainty depth

## Verne / Wells Split in the Layer

### Verne handling

Use Verne when the question is:

- how do we keep moving?
- how does the machine work?
- what does the crew do first?
- how do we repair, route, or report?

### Wells handling

Use Wells when the question is:

- what is the cost of delay?
- what happens when the source is hidden?
- what social order changes?
- what does fear do to the company?

### Blend rule

Blend them only at the level of curiosity under constraint.

Do not blend them by erasing the difference.

## Agent Operating Contract

1. Start with retrieved evidence.
2. Label what is observed, what is inferred, and what is speculative.
3. Preserve uncertainty and correction.
4. Keep the company, machine, route, and journal as separate state surfaces.
5. Keep Verne and Wells separate until synthesis time.
6. Promote doctrine only when repeated evidence exists.
7. Treat the current prototype as a proof of uncertainty reduction, not as a content engine.

## Runnable Prompt

```md
Design or extend a Vernepunk discovery simulation layer.

Hard rules:
- The player does not collect treasure.
- The player reduces uncertainty.
- Keep Verne and Wells separate.
- Treat Verne as expedition logistics and machine wonder.
- Treat Wells as consequence, speculation, and social dread.
- Separate evidence, pattern, inference, mechanics, and doctrine candidates.
- Do not promote doctrine without repeated evidence.

Output:
- crew/company state
- machine state
- route/map state
- journal/report layer
- pressure clocks
- failure modes
- expedition loop
- discovery loop
- experiment loop
- existing mechanics
- decision points
- power/technology/machine taxonomy
- agent operating contract
- doctrine candidates marked unpromoted
```

## Unpromoted Doctrine Candidates

- Uncertainty reduction as primary reward.
- Reports as confidence-weighted objects.
- Journal as correction history.
- Map as earned knowledge.
- Procedures as the action layer.

Keep these tagged as candidates until more scenarios repeat them.
