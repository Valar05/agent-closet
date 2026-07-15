# Prompt Hydraulics

Status: Silver / active skill seed
Date: 2026-07-15
Owner: Quartermaster
Primary consumer: Timmy or any cold-start worker that must turn a compact prompt into state-changing work
Related skills: `skills/world-pressure-engine.md`, `skills/scene-compiler-runtime.md`, `skills/kinetic-compression.md`

## Purpose

Prompt Hydraulics turns a prompt from a description of desired content into pressure applied to persistent actors, systems, or tools.

The prompt supplies pressure. Existing state supplies geometry. Constraints route the pressure. An actuator converts it into visible work. The accepted output records what changed.

This is a composition layer over existing skills, not a replacement for them:

- World Pressure Engine selects pressure that is inevitable, timely, and costly to ignore.
- Scene Compiler Runtime preserves state and runs generation, validation, repair, and acceptance.
- Kinetic Compression makes each beat convert intent into changed state.
- Prompt Hydraulics seals those parts into one pressure-routing model.

## Core Definition

> Prompt Hydraulics applies semantic pressure to persistent state and routes it through honest constraints until visible consequence performs work.

A shallow metaphor describes resemblance. An operational metaphor transfers rules that constrain decisions and predict failure.

## Hydraulic Model

| Hydraulic element | Prompt or simulation element | Required behavior |
|---|---|---|
| Fluid | semantic pressure | carries urgency, contradiction, obligation, scarcity, or consequence |
| Pump | prompt / initiating condition | introduces pressure from a named source |
| Pipe geometry | established character, agent, world, or system state | determines which responses are possible without breaking identity |
| Valve | timing, permission, decision, or routing rule | controls when and where pressure moves |
| Accumulator | unresolved promise, consequence debt, memory, or status quo | stores pressure for later release |
| Relief valve | refusal, safety boundary, scope stop, or graceful degradation | releases unsafe pressure without pretending the task succeeded |
| Leak | exposition, prompt bloat, arbitrary coincidence, or discarded consequence | consumes pressure without useful state change |
| Cavitation | missing evidence or fabricated state | creates noisy motion while the system loses causal contact |
| Actuator | smallest visible event that changes state | converts semantic pressure into observable work |
| Gauge | acceptance check | shows whether pressure produced the intended state delta |
| Return line | continuity update | carries changed state into the next run |

## Governing Rules

1. Pressure must come from somewhere.
2. Pressure does not disappear merely because the output stops mentioning it.
3. Constraints determine the path; they are not decoration.
4. Small, well-placed inputs can move large semantic loads.
5. Valves control timing and routing, not the existence of consequence.
6. Leaks reduce useful work.
7. A system may return to its visible resting position while retaining changed state, wear, debt, knowledge, or stored pressure.
8. Every run needs an actuator: one concrete event that proves the system moved.
9. Every run needs a gauge: an observable acceptance condition.
10. Every accepted run updates continuity. A reset that erases earned consequence is a failed return line.

## Cold-Load Input Contract

A worker may run Prompt Hydraulics from this minimum packet:

```yaml
prompt_hydraulics:
  desired_outcome: what must become true
  current_state: facts that already constrain the run
  persistent_actors:
    - actor: name or responsibility
      geometry: goals, habits, limits, obligations, refusal boundaries
  pressure:
    source: what introduces it
    why_now: why action cannot wait
    cost_if_ignored: what worsens
  time_model: continuous | bounded_slice | asynchronous
  actuator_candidate: smallest visible event that could prove movement
  acceptance_gauge: observable pass condition
  safety_relief: stop, refuse, or degrade conditions
  continuity_target: state that must survive into the next run
```

If `current_state`, `pressure.source`, or `acceptance_gauge` is missing, stop and request or retrieve the missing truth. Do not fill the system with fabricated fluid.

## Runtime Procedure

### 1. Load the vessel

Read the current artifacts, state, and actor contracts. Do not infer geometry from a role label alone.

### 2. Select one pressure source

Choose the pressure with the clearest inevitability, cost, and ability to expose the system through a small event. Do not pressure-shop.

### 3. Seal the system

Name the state and consequences that cannot be silently discarded. Remove prompt instructions that prescribe surface output without constraining cause.

### 4. Map the geometry

For each persistent actor or component, record:

- what it wants
- what it resists
- what it can do
- what it cannot honestly do
- what pressure makes it reveal

Different actors must route the same pressure differently. If all respond alike, geometry has collapsed.

### 5. Set the valves

Choose the timing, permissions, information flow, and decision points. In a continuous time model, do not reset between beats.

### 6. Run consequence forward

Use the smallest event that forces the next event. Preserve the bind until every affected actor, relationship, or system changes grip.

### 7. Fire the actuator

Make one concrete object, decision, message, record, tool result, or bodily action carry the largest hidden relationship. The actuator is not a symbol added afterward; it is where pressure becomes work.

### 8. Read the gauge

Ask:

- What is now true that was not true before?
- Which actor or system paid the cost?
- Did the visible event satisfy the acceptance condition?
- What pressure remains stored?
- What becomes inevitable next?

### 9. Update the return line

Emit the state delta and next pressure. Do not return only prose or a success claim.

## Output Contract

```yaml
prompt_hydraulics_result:
  work_product: scene, decision, artifact, or tool result
  actuator: concrete event that performed work
  state_delta:
    world_or_system: changed facts
    actors: changed knowledge, options, authority, trust, debt, or condition
  acceptance_gauge:
    condition: expected observable result
    verdict: pass | fail | partial
    evidence: what proves the verdict
  stored_pressure: unresolved consequence debt
  next_pressure: what the new state makes likely or necessary
  relief_events: refusals, stops, or graceful degradations used
```

## Delegated Speech Valve

Prehumous, posthumous, future, historical, or otherwise delegated speech can move information across a boundary without moving a body across it.

Use it as controlled process, not authenticity theater.

The output must distinguish:

- source evidence or established character geometry
- inferred wording
- uncertainty or contradiction
- who controls the record
- what action the delegated speech is allowed to influence

For a real person, never present generated wording as a verified quotation. The valve may route preserved judgment; it may not counterfeit custody.

## Information-Only Time Machine

An information-only time machine changes everything while transporting nothing physical.

Runtime rule:

```text
future or alternate information
-> present actor receives pressure
-> actor makes a constrained choice
-> physical history changes
-> later state creates, contradicts, or refuses the originating information
```

The machine works only when information changes action and the resulting state persists. A prophecy with no decision cost is atmosphere, not hydraulics.

## Proof Run: Continuous Bikini Bottom Slice

Source context: 2026-07-15 chat exercise combining a continuous real-time crisis model, Bikini Bottom as persistent character geometry, future delegated speech, and kinetic compression.

Pressure source:

- an unplugged order printer emits future instructions
- statements arrive before their speakers produce them
- a lunch rush prevents stopping the system

Geometry:

- SpongeBob converts pressure into action
- Squidward converts it into reluctant responsibility
- Sandy diagnoses and routes it
- Krabs tries to monetize it
- Plankton mistakes access for control
- Patrick accidentally completes the circuit

Valves:

- real-time timestamps
- no reset between beats
- information can cross time; matter cannot
- the order cannot be served before a fixed second

Actuator:

- one pickle lands on Order 47 at the deadline

Gauge result:

- the restaurant visibly returns to lunch service
- causal history, knowledge, and responsibility have changed
- the same status quo now contains a completed loop and stored consequence

Why it passed:

The prompt did not outline the episode. It pressurized established actors. Each routed the same pressure differently, and a tiny physical displacement proved total system movement.

## Timmy Consumption Prompt

Use this bootstrap without importing the originating chat:

```text
Owner: Timmy.
Responsibility: convert the requested outcome into state-changing work using Prompt Hydraulics.

Read:
- skills/prompt-hydraulics.md
- skills/world-pressure-engine.md
- skills/scene-compiler-runtime.md
- skills/kinetic-compression.md

Load current state before generating.
Name one pressure source, persistent actor geometry, timing valves, one actuator, one acceptance gauge, and one relief boundary.
Run consequence forward without resetting earned state.
Return the work product plus state delta, gauge verdict, stored pressure, and next pressure.
Stop rather than fabricate missing state or evidence.
```

## Failure Modes

### Metaphor cosplay

Hydraulic words decorate an ordinary prompt.

Fix: require the input contract, actuator, gauge, and state delta.

### Pressure leak

Characters explain the pressure instead of acting under it.

Fix: replace exposition with a constrained decision or concrete event.

### Geometry collapse

Every actor behaves like the prompt author.

Fix: restate each actor's wants, resistance, capabilities, and refusal boundary.

### Railroading

The prompt prescribes every event, leaving no work for actor geometry.

Fix: prescribe outcome, pressure, and constraints; let the system determine the path.

### Actuator theater

A symbolic object appears but changes no state.

Fix: require the object or event to alter options, authority, knowledge, trust, resources, or the next pressure.

### Reset laundering

The surface returns to normal and the output claims nothing changed.

Fix: record retained knowledge, debt, wear, obligation, or consequence in the return line.

### Cavitation

The run invents evidence, state, or authority to keep moving.

Fix: stop, retrieve truth, or use the named relief path.

### Competence commercial

Actors perform impressively but relationship, judgment, and authority remain inert.

Fix: require collision -> relationship exposed -> judgment transferred -> irreversible state.

## Acceptance Tests

Prompt Hydraulics passes a run only when:

- the pressure source and why-now are explicit
- current state constrains the output
- persistent actors route pressure differently
- no essential consequence disappears between beats
- one concrete actuator performs visible work
- the gauge cites observable evidence
- a state delta survives the run
- stored pressure or the next pressure is named
- safety or authority boundaries remain available as relief valves

## Promotion Condition

Promote from Silver to Gold after three readback-verifiable runs in distinct domains:

1. narrative or simulation
2. agent orchestration or prompt compilation
3. tool-backed implementation or operational workflow

At least one run must fail safely through a relief valve, and at least one cold-start worker must execute the Timmy Consumption Prompt without access to the originating chat.
