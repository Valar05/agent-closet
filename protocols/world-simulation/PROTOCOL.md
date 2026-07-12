# Protocol

## Definition

An agentic simulation substrate is a durable, replayable, corrigible environment in which replaceable agents inherit a persistent world, act under pressure, produce consequences, and leave evidence that changes later judgment.

## State Transition

```text
Read state
-> identify knowns, unknowns, obligations, refusals, and consequence debt
-> select one pressure
-> let an agent act
-> introduce reality-grounded friction
-> record observation separately from interpretation
-> update world, character, relationship, and resource state
-> preserve unresolved contradiction
-> validate the transition
```

## Failed Transition

When intended state differs from observed state:

1. preserve the attempted transition;
2. state what actually occurred;
3. prohibit only the unsupported state claim;
4. preserve useful remaining actions;
5. select the cheapest discriminating probe;
6. define re-entry evidence;
7. replay the fixture after correction.

## Doctrine Promotion

```text
Simulation -> Observation -> Candidate doctrine -> Adversarial fixture
-> Replay -> Cross-worker test -> Promotion or rejection
```

Do not invent doctrine first and write a scene to prove it.

## Required Properties

### Durability

The world survives session and worker replacement.

### Consequence

Actions change later decisions.

### Provenance

Claims point to observations, commits, issues, traces, or source artifacts.

### Corrigibility

A correction preserves the failure and changes later behavior.

### Re-entry

Negative knowledge expires when the world supplies the required evidence.

### Antagonism

Contradiction, refusal, opacity, silence, and exit are not automatically assimilated.

### Portability

No single model is the house.

## Minimal Agent Packet

```yaml
world_state:
known_information:
unknown_information:
actor_state:
obligations:
refusals:
available_resources:
consequence_debt:
selected_doctrine:
forbidden_stale_premises:
requested_transition:
acceptance_evidence:
```

## Completion Rule

A simulation transition is complete only when:

- state changed or the failed transition is preserved;
- evidence is recorded;
- consequences are visible;
- memory is updated;
- unsupported claims remain quarantined;
- the next worker can reconstruct why.
