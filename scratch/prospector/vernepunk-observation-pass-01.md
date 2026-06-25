# Vernepunk Observation Pass 01

Scope: mine `Valar05/vernepunk` as a discovery / expedition simulation space and keep the evidence separate from inference.

Core thesis to test: **the player does not collect treasure; the player reduces uncertainty.**

## Repo Surface Map

- `README.md` frames Vernepunk as "Jules Verne expedition fiction as crew simulation" and states the design north star: "The machine is analog. The memory is human. The truth arrives late."
- `REPO_DOCTRINE.md` defines the core pillars: analog machines, expedition awareness, company continuity, journal memory, and procedure over magic.
- `CORPUS_MANIFEST.md` defines the corpus layers and the WWVD judgment layer, and explicitly splits Verne from Wells while keeping both in scope.
- `docs/doctrine/*.md` contains the reusable rules for core doctrine, machine simulation, expedition awareness, journal voice, WWVD, and ingestion discoveries.
- `corpus/distillations/**/*.md` contains source-backed cards and a simulation primitive registry.
- `ml/prompts/*.md` contains retrieval and WWVD prompt contracts that require evidence, doctrine, inference, and missing-evidence labeling.
- `game/README.md`, `game/simulation.mjs`, and `game/main.mjs` show the first playable slice.
- `corpus/sources/verne/manifest.json` and `corpus/sources/wells/manifest.json` list the current source sets and metadata.

## Evidence Ledger

### Verne lane evidence

- `docs/doctrine/vernepunk-core.md` says Vernepunk starts with a machine question, not a style question.
- `docs/doctrine/analog-machine-simulation.md` requires purpose, crew stations, procedures, instruments, resources, stressors, failure modes, repair actions, and consequences.
- `docs/doctrine/expedition-awareness.md` says the player knows only what the company observes, measures, reports, misreads, and later corrects.
- `docs/doctrine/company-journal-voice.md` says the journal records belief, action, cost, correction, and one human detail worth remembering.
- `docs/doctrine/wwvd-runtime-protocol.md` says Verne-dominant questions are about exploration, invention, engineering, optimism, procedure, and capability.
- `corpus/distillations/verne/verne_initial_cards.md` includes ballast control, water crisis after route error, sound-based observation after a mistake, company survival through infrastructure, improvised recon, deadline pressure, and machine identity.
- `corpus/distillations/simulation_primitives.md` includes `procedural_competence`, `report_latency`, `machine_identity`, `resource_pressure`, `infrastructure_building`, `delayed_correction`, and `crew_continuity`.
- `game/simulation.mjs` currently models a land engine hearing a vibration under the ice, with procedures that change machine and crew state, reports with confidence labels, and a journal that stores a correction.

### Wells lane evidence

- `docs/doctrine/wwvd-runtime-protocol.md` says Wells-dominant questions are about consequences, unintended effects, social disruption, power imbalance, fear, and collapse.
- `corpus/distillations/wells/wells_initial_cards.md` includes future class split, machine proof, vivisection dread, beast-folk coercive law, unseen agency, invisibility isolation, ignorance gap, first-contact shock, future control, cavorite flight, alien lunar society, and scale change.
- `corpus/distillations/wells/high_confidence_cards.md` keeps the same pattern set and emphasizes delayed recognition, asymmetry, coercive doctrine, social paranoia, and institutional capture.
- `corpus/distillations/simulation_primitives.md` includes `capability_shock`, `ignorance_gap`, `classification_failure`, `hidden_actor`, `social_paranoia`, `identity_decay`, `class_split`, `first_contact`, `scale_shift`, `experimental_spillover`, and `institutional_capture`.
- `corpus/sources/wells/manifest.json` shows the source set is focused on `The Time Machine`, `The Island of Doctor Moreau`, `The Invisible Man`, `The War of the Worlds`, `The Sleeper Awakes`, `The First Men in the Moon`, and `The Food of the Gods and How It Came to Earth`.

## Correlated Patterns

### Verne pattern lane

1. Travel is constrained labor, not free movement.
2. Machine operation is procedural and expensive.
3. Reports are delayed, partial, and confidence-weighted.
4. Observation often comes from crew hearing, touching, or instrument reading before visual confirmation.
5. Survival is infrastructure, not a hero pose.
6. Vehicle identity matters because the machine is a social object as well as a tool.
7. Failure produces information before catastrophe.

### Wells pattern lane

1. First contact is a classification problem before it is a combat problem.
2. Hidden actors and hidden systems create social paranoia.
3. The public often learns too late.
4. Power shifts the social order as much as the immediate scene.
5. Institutions capture value during delay.
6. Scale changes the rules of labor and authority.
7. Scientific control can be morally and socially corrosive.

### Shared patterns

1. Knowledge is mediated, never direct.
2. Delay changes outcomes.
3. The wrong belief can still be useful until correction arrives.
4. Machine systems and social systems fail together.
5. Curiosity is productive only when bounded by procedure.
6. The interesting state is not "resolved" but "less uncertain."

## Story / World Hooks

- A buried machine, buried city, or buried route can be discovered only through listening, venting, sounding, and later correction.
- A crew-company can be forced to keep moving while its reports disagree.
- An expedition can find a machine that is proof of an idea before it is a transport system.
- A hidden power can be real without being fully named yet.
- A route can become a social event: who gets the truth, who gets the rumor, and who is still acting on the old map.

## Existing Mechanics

- Procedures: `halt`, `vent`, `dispatch`, `reduce`, `ignore`.
- Machine state: `boilerPressure`, `vibrationLevel`, `movementState`, `fuelState`, `machineStatus`.
- Crew state: morale, fear, and fatigue for commander, engineer, and sounding crew.
- Awareness state: multiple reports with source, perspective, text, and confidence label.
- Journal state: a memory entry with observed, believed, action taken, later learned, cost, and confidence.
- Outcome state: a resolved procedure plus a truth reveal.
- Hidden truth: the cause exists before the company understands it.

## Decision Points

- The source repo already treats uncertainty as the main resource, so the simulation layer should keep that as the primary currency.
- The Verne/Wells split is already documented and should stay explicit in the destination repo.
- The current playable slice is a single-situation simulation, not a general campaign engine.
- The next simulation layer should expand the model around route, crew, machine, report, and journal state, not around loot.

## Power / Technology / Machine Taxonomy

- Power source: steam, ballast, gas, fuel, heat, gravity, or pressure.
- Transmission: valves, runners, screws, cables, horns, and human relay.
- Sensing: gauges, sounding, vibration, crew hearing, watch phrases, rumor, and delayed reports.
- Control: procedures, stations, sequence, timing, and maintenance rituals.
- Enclosure: hull, boiler, cave, cabin, pressure shell, or habitat.
- Failure: leak, tremor, drift, heat, delay, false reading, fatigue, and loss of trust.
- Social machine: company discipline, report chain, and journal memory.

## Expedition / Discovery / Experiment Loop

### Expedition loop

Observe -> choose route -> commit crew -> manage machine -> update map -> record journal.

### Discovery loop

Notice anomaly -> classify source -> reduce uncertainty -> confirm or correct -> update shared understanding.

### Experiment loop

Set procedure -> change one variable -> observe response -> compare report to truth -> store correction.

## Crew / Company State

- Roster and role coverage.
- Fatigue, fear, morale, injuries, and replacements.
- Trust, grudges, and jokes as living continuity.
- Source reliability by crew member.
- Who hears first, who reports first, and who can be believed under pressure.

## Machine State

- Pressure, heat, fuel, vibration, movement mode, and maintenance backlog.
- Hidden operating modes and misleading gauges.
- Crew station assignments and repair actions.
- Cost of ignoring warnings.

## Route / Map State

- Surveyed versus unsurveyed terrain.
- Confidence by route segment.
- Drift, dead ends, hazards, and repair points.
- A map that changes because the company learned more, not because the world changed.

## Journal / Report Layer

- Source of report.
- What was observed.
- What was believed at the time.
- What action was taken.
- What it cost.
- What was later corrected.
- One human detail to keep memory anchored.

## Pressure Clocks

- Boiler pressure.
- Fuel or resource depletion.
- Crew fatigue.
- Report delay.
- Route uncertainty.
- Social suspicion.
- Machine confidence or gauge confidence.

## Failure Modes

- Mistaking vibration for background noise.
- Acting on a false certainty.
- Running the machine too hot.
- Treating a report as fact before correction.
- Letting fear or rumor outrun the instrument.
- Losing crew continuity through fatigue, injury, or panic.
- Turning a machine problem into a social problem.

## Agent Operating Contract

- Read doctrine before implementation.
- Separate evidence from inference.
- Preserve Verne and Wells as distinct lanes.
- Do not promote a doctrine candidate without repeated evidence.
- Model uncertainty as a resource that can be reduced, not eliminated.
- Keep the journal as memory, not flavor text.
- Prefer procedure over generic action labels.

## Runnable Prompt

```md
You are mining Vernepunk as a discovery / expedition simulation space.

Use only the provided repo evidence. Separate:
1. Evidence
2. Pattern
3. Inference
4. Simulation mechanics
5. Doctrine candidates

Rules:
- Keep Verne and Wells separate.
- Treat Verne as expedition logistics, machine wonder, and procedure.
- Treat Wells as consequence, speculation, and social dread.
- The blend is curiosity under constraint.
- The player does not collect treasure; the player reduces uncertainty.
- Do not promote doctrine unless repeated evidence supports it.
- Do not use omniscient knowledge; preserve report delay and confidence.

Output:
- repo surface map
- story/world hooks
- Verne pattern lane
- Wells pattern lane
- shared patterns
- existing mechanics
- decision points
- power/technology/machine taxonomy
- expedition loop
- discovery loop
- experiment loop
- crew/company state
- machine state
- route/map state
- journal/report layer
- pressure clocks
- failure modes
- agent operating contract
- runnable prompt
- doctrine candidates marked unpromoted
```

## Doctrine Candidates Not Promoted

- `uncertainty is the core currency` - supported, but keep as thesis language until the simulation layer proves it across more than one scenario.
- `reports should be confidence-weighted` - strongly supported and already present, but still treat as a working doctrine candidate until more scenarios use it.
- `machine state and social state co-fail` - supported by current prototype and cards, but not yet broad enough to become a universal doctrine.
- `route correction is more important than route speed` - supported by Verne cards, but should remain candidate until more route-heavy cases are mined.
- `experiment = procedure + observation + correction` - supported by the retrieval layer, but keep as reusable judgment rather than hard doctrine until the simulation surface repeats it.
