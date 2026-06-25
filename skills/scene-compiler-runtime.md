# Scene Compiler Runtime

Status: active runtime seed
Role: run the Scene Compiler loop over world state, pressure, doctrine, generation, validation, repair, and acceptance

## Purpose

The Scene Compiler Runtime is the execution layer that uses:

- `skills/world-pressure-engine.md` to choose the next pressure
- `skills/scene-compiler.md` to shape the scene-generation loop
- `skills/scene-compiler-tests.md` to validate whether the output behaves like the selected doctrine

It exists so the compiler stops being a static prompt library and starts behaving like a loop that can select, generate, test, repair, and accept scenes.

This is not new doctrine.
This is not manuscript mining.
This is not prose imitation.

## Runtime Contract

The runtime maintains the current fiction state as a set of explicit layers.

### World State

What is true in the story world right now.

Track:

- location
- active facts
- available resources
- institutional status
- unresolved promises
- scene history
- world changes that must persist

### Character State

What changed about the relevant character or characters.

Track:

- goals
- wounds or fatigue
- capabilities
- current role
- what they now know
- what they now owe
- what they refuse

### Pressure State

What is forcing action now.

Track:

- pressure category
- urgency
- consequence debt
- why now
- who must decide
- what gets worse if ignored

### Relationship State

What changed between characters.

Track:

- trust
- dependence
- resentment
- care
- rupture
- obligation
- repair evidence

### Doctrine Selection

Which candidate doctrine(s) the runtime is using for the current scene.

Track:

- doctrine name
- reason for selection
- whether it is the primary doctrine or a support doctrine
- what observable behavior the doctrine should force

### Scene Draft

The current generated scene under test.

Track:

- scene input
- draft text or scene plan
- expected state delta
- harness result
- repair notes

## Compiler Loop

```text
Story state
-> Pressure selection
-> Doctrine selection
-> Scene generation
-> Run test harness
-> Repair failures
-> Accept scene
```

### 1. Inspect Current State

Begin with the live state, not with a blank prompt.

Ask:

- what is true
- what changed last
- what pressure is inevitable
- what promise is unresolved
- what needs to move next

### 2. Select Pressure

Use `skills/world-pressure-engine.md` to choose the pressure that best fits the current world state.

Selection rule:

- prefer the pressure with the highest inevitability and cost clarity
- prefer the pressure that exposes the most system through the smallest concrete action
- avoid pressure shopping

### 3. Select Doctrine

Choose the smallest doctrine set that can force the scene into observable behavior.

Doctrine selection rules:

- prefer one primary doctrine
- add a second doctrine only when the scene cannot satisfy the pressure with one
- select based on observable output, not thematic resemblance
- prefer doctrines whose pass condition can be tested directly

Default mapping:

- routing and responsibility -> `Route Responsibility Through a Person`
- maintenance, repair, feeding, stabilization -> `Make Repair the Dramatic Act`
- artifact, interface, ritual, machine learning -> `Teach Systems by Contact`
- recovery, meals, rest -> `Use Food and Rest as Plot Transitions`
- care through shared use -> `Let Relationships Start as Utility`
- upgrade, training, new verbs -> `Progress by Expanding Choice Space`
- persistent consequences -> `Keep Consequences in the World`
- comfort temptation -> `Make Comfort Suspicious`
- institutions and authority -> `Write Institutions as Coherent and Harmful`
- recognition and rescue -> `Make Recognition Matter`

### 4. Generate Scene

Write the scene so the selected doctrine can be observed.

The scene must:

- begin from concrete pressure
- force a visible decision or action
- change at least one world-state layer
- create a new pressure at the end

### 5. Run Test Harness

Check the scene against `skills/scene-compiler-tests.md`.

Required checks:

- scene input matches the active pressure
- doctrine application is visible
- generated scene behavior satisfies the doctrine
- pass/fail test is satisfied

If the scene fails, keep the failure concrete.

### 6. Repair Failures

Repair by changing the scene, not by redefining the doctrine.

Repair order:

1. fix missing pressure
2. fix missing observable action
3. fix missing state change
4. fix missing consequence
5. fix missing next pressure

Bounded retry policy:

- retry a bounded number of times
- stop when the scene still fails the same way
- record the failure type instead of laundering it into acceptance

### 7. Accept Scene

Accept only when:

- the selected doctrine test passes
- the scene produces a real state transition
- the next pressure is explicit
- the scene is not dependent on vibe or prose imitation

## Runtime Data Shape

Minimal runtime payload:

```text
runtime_state:
  world_state
  character_state
  pressure_state
  relationship_state
  unresolved_promises
  selected_doctrines
  scene_draft
  harness_result
  repair_notes
```

Recommended output shape:

```text
accepted_scene:
  scene_text_or_plan
  state_delta
  next_pressure
  doctrine_checks
  unresolved_debt
```

## Failure Modes

### Pressure drift

The runtime picks a scene because it seems interesting, not because it is forced by state.

Fix:

- re-run pressure selection from the current world state
- require consequence debt or inevitability as the trigger

### Doctrine drift

The runtime picks a doctrine because it sounds right, not because it can be observed.

Fix:

- require an observable pass condition
- prefer the smallest doctrine set

### Harness laundering

The scene fails, but the failure is edited away by explanation.

Fix:

- keep failure concrete
- repair the scene or reject it

### Static prompt relapse

The runtime becomes a prose recipe instead of a loop.

Fix:

- preserve explicit state
- preserve validation
- preserve repair
- preserve acceptance rules

## Acceptance Criteria

This runtime works when it can:

- maintain explicit story state
- choose the next pressure from that state
- select one or more doctrines that can be tested
- generate a scene that changes state
- run the scene test harness
- repair failed scenes without changing doctrine
- accept only scenes that pass observable tests

## Related Assets

- `skills/scene-compiler.md`
- `skills/world-pressure-engine.md`
- `skills/scene-compiler-tests.md`
- `corpus/fiction/candidate-writing-doctrines.md`
- `corpus/fiction/fiction-observation-ledger.md`
