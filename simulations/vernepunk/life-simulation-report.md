# Vernepunk Life Simulation Report

Status: evidence-backed simulation synthesis for the living expedition layer.

## Evidence First

### Source-backed signals

- `REPO_DOCTRINE.md` says Vernepunk is about crews operating analog machines under uncertainty.
- `docs/doctrine/analog-machine-simulation.md` demands physical principle, crew stations, resources, stressors, failure modes, and repair actions.
- `docs/doctrine/expedition-awareness.md` says the player knows the world only through observer-sourced and confidence-weighted awareness.
- `docs/doctrine/company-journal-voice.md` says the journal records what the company believed, what happened, what was corrected later, and one human detail worth remembering.
- `corpus/distillations/verne/verne_initial_cards.md` repeatedly shows route error, ballast management, improvised sensing, machine identity, deadline pressure, and company survival.
- `corpus/distillations/wells/high_confidence_cards.md` shows the Wells side of the same space: delayed recognition, hidden actors, social paranoia, institutional capture, and scale change.
- `game/simulation.mjs` already implements a living slice with crew morale/fear/fatigue, machine pressure/vibration/fuel/movement, awareness reports, and a journal that stores a correction.

## Living Simulation Thesis

The life simulation is not about movement alone. It is about a company staying coherent while uncertainty is reduced in stages.

The active unit is not a hero.
It is a company with:

- a roster
- a machine
- a route
- a report chain
- a memory engine
- a pressure budget

The player succeeds by keeping those systems legible under strain.

## Verne Lane

Verne provides the operational shape.

- Ballast and altitude are labor.
- Steam, pressure, and vibration are decision surfaces.
- Reports are delayed and confidence-weighted.
- Crew labor is specific and station-based.
- Survival comes from infrastructure and procedure.
- Discovery is usually earned by changing the machine state enough to hear the truth.

### Evidence examples

- `five_weeks_ballast_guidance` and `five_weeks_ballast_and_anchor` show route control through ballast discipline.
- `journey_wrong_turn_water_crisis` shows navigation mistakes becoming survival pressure.
- `journey_subterranean_observation_chain` shows sound and contact as awareness sources after error.
- `twenty_thousand_watch_phrase` shows low-information watch language as useful state.
- `twenty_thousand_secret_machine` shows machine identity as a meaningful social object.
- `mysterious_island_company_survival` shows that survival is a build-up of heat, shelter, and labor.
- `around_world_wager_clock` and `around_world_service_and_logistics` show route timing and crew pairing as the real machine.

## Wells Lane

Wells provides the consequence shape.

- Knowledge can arrive too late.
- Hidden sources can continue to act.
- Social systems can reorganize around fear or ignorance.
- Scientific power can become morally unstable.
- Scale changes the rules of labor and authority.

### Evidence examples

- `war_worlds_ignorance_gap` shows catastrophe before public recognition.
- `war_worlds_first_contact_shock` shows capability shock and hesitation.
- `invisible_man_unseen_agency` shows hidden agency with low classification certainty.
- `invisible_man_isolation_cost` shows concealment as social damage.
- `sleeper_future_control` shows delay turning into institutional capture.
- `food_of_the_gods_scale_change` and `food_of_the_gods_public_spread` show diffusion and scale change as systemic events.

## Shared Pattern

Verne and Wells agree on one useful operational truth:

> the interesting state is not certainty; it is managed uncertainty.

Verne answers:

- How do we keep the machine alive?
- How do we move?
- How do we report honestly?

Wells answers:

- What happens when the report is late?
- What happens when the source is hidden?
- What happens when the system spreads beyond control?

The combined simulation is curiosity under constraint.

## Life Simulation Model

### Crew/company state

Track the company as a living organism:

- roster
- roles
- fatigue
- fear
- morale
- injuries
- expertise
- grudges
- jokes
- trust
- replacement status
- who can still act on the next watch

### Machine state

Track the machine as a pressure system:

- pressure
- heat
- fuel
- vibration
- movement mode
- maintenance backlog
- sensor confidence
- hidden operating mode
- crew station load

### Route/map state

Track the route as an uncertainty graph:

- surveyed segments
- unsurveyed segments
- confidence by segment
- hazards
- dead ends
- drift
- recoverability
- known landmarks

### Report state

Track reports as objects, not text blobs:

- source
- source type
- observed fact
- interpretation
- confidence
- delay
- contradiction status
- corrected status

### Journal state

Track journal entries as memory with revision:

- observed
- believed
- acted
- cost
- later learned
- human detail
- confidence after correction

## Pressure Clocks

The living simulation should advance multiple clocks at once.

1. Boiler pressure clock
2. Fuel / resource clock
3. Fatigue clock
4. Fear / morale clock
5. Report delay clock
6. Map confidence clock
7. Weather or terrain clock
8. Social suspicion clock
9. Repair backlog clock
10. Institutional attention clock

These clocks are more important than a generic enemy HP bar.

## Expedition Loop

1. Choose a route or next move.
2. Assign crew to a station or role.
3. Spend resources to keep the machine in a survivable state.
4. Receive partial reports.
5. Compare report to machine behavior.
6. Correct the route or procedure.
7. Write the journal entry.
8. Carry the cost into the next scene.

## Discovery Loop

1. Notice an anomaly.
2. Identify the observer or instrument source.
3. Rate confidence.
4. Apply a procedure that changes visibility or machine state.
5. See what the anomaly becomes after correction.
6. Update the map and the journal.

Discovery is not loot collection.
Discovery is uncertainty reduction.

## Experiment Loop

1. Pick one variable to change.
2. Record the current belief.
3. Execute a procedure.
4. Observe the new state.
5. Compare result to expectation.
6. Store the correction.

This is the playable form of WWVD retrieval logic.

## Machine and Crew Interlock

The machine should not be able to run without crew judgment.

Crew work changes:

- pressure
- vibration
- confidence
- morale
- fatigue
- report quality

Machine stress changes:

- crew stress
- uncertainty
- route confidence
- future options

This makes the machine and the company a single living system rather than two separate UI panels.

## Failure Modes

### Mechanical

- overheating
- pressure spike
- false gauge calm
- resource exhaustion
- repair backlog
- mode confusion

### Cognitive

- acting on a weak report as if it were certain
- overtrusting a single source
- losing the correction chain
- confusing suspicion with evidence
- failing to update the map after new information

### Social

- fear spread
- trust erosion
- blame drift
- crew exhaustion
- role overload
- rumor outrunning the journal

### Structural

- route drift becomes irrecoverable
- the company becomes too tired to exploit new knowledge
- the machine survives but the crew does not stay coherent
- the world reorganizes while the company is still uncertain

## Design Implications

- Use specific procedures instead of generic "fix" or "scan" actions.
- Put confidence on every report.
- Let the journal keep the wrong belief before the correction.
- Make source type matter: crew, instrument, rumor, and later correction are not the same thing.
- Reward stabilizing the machine because it buys better truth, not because it increases score.
- Keep Wells-style consequence in the background so discovery has a bill.

## Agent Operating Contract

- Evidence first.
- Infer only after source review.
- Keep Verne and Wells separate in the analysis.
- Do not collapse uncertainty into omniscience.
- Keep the company alive as a continuity object.
- Keep the machine legible as a pressure system.
- Keep the journal as revision history.
- Do not promote a doctrine candidate unless the same pattern repeats in multiple sources.

## Runnable Prompt

```md
Mine the Vernepunk repo as a living expedition simulation.

Requirements:
- Separate evidence, patterns, mechanics, and doctrine candidates.
- Keep Verne and Wells in separate lanes.
- Treat Verne as expedition logistics and machine wonder.
- Treat Wells as consequence, speculation, and social dread.
- Verify the thesis that the player reduces uncertainty rather than collecting treasure.
- Base all claims on repo files, corpus cards, and doctrine docs.
- Mark any doctrine candidate that is not yet repeated as unpromoted.

Required output sections:
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
```

## Unpromoted Doctrine Candidates

- Uncertainty reduction is the primary reward.
- Reports should always carry source and confidence.
- Machine state and social state should co-evolve.
- The journal should preserve correction history.
- Discovery should be a procedure, not a menu action.

These are strongly supported, but they should stay tagged as candidates until another simulation layer or scenario repeats them.
