# AI Substrate Contract

Status: active interface contract
Role: define the AI-facing transformation layer that turns explicit story state into validated state transitions

## Purpose

This contract treats the agent as the transformation substrate and the docs as the decision layer.

The goal is not a human-facing writing app.
The goal is an AI-facing simulation and what-if engine that can:

- read structured story state
- select pressure and doctrine
- generate candidate scene transitions
- validate the result against testable doctrine
- repair failures
- emit the next machine-readable state

This is a glue layer, not doctrine.
It exists so orchestrated agents can become the thing they are simulating.

## Contract Roles

### Transformation Substrate

The agent runtime that accepts state, applies policy, and emits a new state.

### Decision Layer

The repository docs that tell the substrate how to choose pressure, doctrine, validation, and acceptance.

Primary sources:

- `skills/scene-compiler-runtime.md`
- `skills/world-pressure-engine.md`
- `skills/scene-compiler.md`
- `skills/scene-compiler-tests.md`

### Trace Layer

The machine-readable record of what state existed, what was selected, what changed, and what remains unresolved.

## Machine-Readable State Contract

The substrate should accept and emit explicit state objects.

### Input State

```yaml
simulation_id: string
branch_id: string
parent_branch_id: string | null
world_state:
  location: string
  active_facts: [string]
  available_resources: [string]
  institutional_status: string
  unresolved_promises: [string]
  scene_history: [string]
character_state:
  goals: [string]
  wounds_or_fatigue: [string]
  capabilities: [string]
  current_role: string
  knowledge: [string]
  obligations: [string]
  refusals: [string]
relationship_state:
  trust: [string]
  dependence: [string]
  resentment: [string]
  care: [string]
  rupture: [string]
  obligation: [string]
pressure_state:
  category: string
  urgency: string
  consequence_debt: [string]
  why_now: string
  who_must_decide: string
selected_doctrines: [string]
unresolved_promises: [string]
```

### Output State

```yaml
accepted: boolean
selected_pressure:
  category: string
  why_now: string
  why_this_pressure_was_chosen: string
selected_doctrines: [string]
scene_draft:
  scene_text_or_plan: string
  observable_behaviors: [string]
validation:
  per_doctrine:
    - doctrine: string
      pass_fail: string
      observable_evidence: [string]
      missing_behavior: [string]
state_delta:
  world_state: [string]
  character_state: [string]
  relationship_state: [string]
  pressure_state: [string]
next_pressure: [string]
remaining_consequence_debt: [string]
repair_notes: [string]
```

## Branch / What-If Protocol

The substrate should support alternate branches from the same starting state.

### Branch Contract

Each branch must carry:

- `simulation_id`
- `branch_id`
- `parent_branch_id`
- `selected_pressure`
- `selected_doctrines`
- `candidate_scene`
- `validation_result`
- `accepted` / `rejected`
- `state_delta`
- `remaining_consequence_debt`

### Branch Flow

```text
Input state
-> Pressure selection
-> Doctrine selection
-> Scene generation
-> Harness validation
-> Repair or reject
-> Accepted transition
-> New branch state
```

### What-If Rule

If two candidate branches start from the same state, the engine should preserve both traces until one is accepted or explicitly discarded.

Branches are compared by:

- observable state change
- test pass rate
- remaining consequence debt
- next-pressure clarity
- doctrine economy

## Simulation Trace Format

The trace is the resumption and audit layer.

### Trace Record

```yaml
trace_id: string
simulation_id: string
branch_id: string
parent_branch_id: string | null
timestamp: string
input_state: object
selected_pressure: object
selected_doctrines: [string]
candidate_scene: object
validation_result: object
repairs: [string]
accepted: boolean
state_delta: object
next_pressure: object
remaining_consequence_debt: [string]
notes: [string]
```

### Trace Rules

- Keep the trace machine-readable.
- Preserve rejected alternatives.
- Preserve why a branch failed.
- Preserve what changed.
- Preserve what still matters next.
- Do not collapse the trace into prose-only output.

## AI Runtime Behavior

The substrate should behave like this:

1. Load explicit state.
2. Choose the next pressure from changed state.
3. Choose the smallest doctrine set that can force observable behavior.
4. Generate a candidate scene or detailed scene plan.
5. Validate each doctrine independently.
6. Repair the scene if a selected doctrine fails.
7. Accept only if the state transition is real and the tests pass.
8. Emit the new trace and next state.

## What This Is Not

- not a prose editor
- not a human writing coach
- not a static prompt library
- not a lore dump
- not a new doctrine source
- not a replacement for `skills/scene-compiler-runtime.md`

## Acceptance Criteria

This contract is working when an AI system can:

- ingest a structured state payload
- select pressure and doctrine without human intervention
- emit a candidate branch
- validate it against the harness
- repair or reject it
- preserve a trace for resumption
- compare branches from the same origin state
- continue simulation without losing consequence memory

## Related Assets

- `skills/scene-compiler-runtime.md`
- `skills/world-pressure-engine.md`
- `skills/scene-compiler.md`
- `skills/scene-compiler-tests.md`
- `shared/theory/simulation-as-learning-infrastructure.md`
- `simulations/goblin/README.md`
- `simulations/lighter-than-air/life-simulation-report.md`
