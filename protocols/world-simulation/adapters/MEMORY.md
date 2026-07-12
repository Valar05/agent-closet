# World Simulation Memory Adapter

Copy the bounded sections needed by the current project into its agent memory file. Do not copy the entire Agent Closet corpus.

## World Contract

- Treat repository and provider evidence as world state.
- Separate attempted action from observed state.
- Record consequences that affect later decisions.
- Preserve unknowns and contradictions.
- Do not silently turn interpretation into canon.
- Do not treat local or simulated proof as production completion.

## Forbidden Stale Premise

For each active card, load:

```text
Claim:
Disconfirming evidence:
Scope:
Planning consequence:
Behavior still permitted:
Re-entry condition:
Next probe:
Provenance:
```

## Execution Rule

Before acting:

1. read the latest world state;
2. check active stale-premise cards;
3. reject plans that require an unsupported state;
4. retain useful permitted probes;
5. act;
6. verify;
7. update or retire cards from evidence.

## Completion Rule

Do not claim completion from:

- tool visibility;
- a generated plan;
- a local-only smoke;
- a simulated worker;
- a successful write request without read-back;
- a green check whose authoritative artifact is red.

Completion requires the evidence named by the task.

## Memory Safety

- An observed state is not a proven cause.
- A prohibition must have re-entry.
- A correction must preserve the incident.
- A private conversation is not a public fixture.
- A card that blocks unrelated work must be narrowed or demoted.
