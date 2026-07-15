# World Simulation Protocol

Status: Experimental public protocol
Canonical owner: Agent Closet

> Persistent worlds. Consequential agents. Memory that knows what did not happen.

This directory packages Agent Closet's existing simulation organs into a cold-agent transmission path. It does not replace Simulation Doctrine, Scene Compiler, World Pressure Engine, the AI Substrate Contract, or the promotion system.

## Five-Minute Orientation

Read:

1. [Simulation Doctrine](../../doctrines/SIMULATION_DOCTRINE.md)
2. [AI Substrate Contract](../../glue/ai-substrate-contract.md)
3. [World Pressure Engine](../../skills/world-pressure-engine.md)
4. [Simulation as Learning Infrastructure](../../shared/theory/simulation-as-learning-infrastructure.md)
5. [Forbidden Stale Premise](../../shared/doctrine/forbidden-stale-premise.md)
6. [Protocol](PROTOCOL.md)
7. [Validation](VALIDATION.md)

## Two Loops

```text
WORLD SIMULATION
Information -> Order -> Friction -> Adaptation -> Consequence -> Memory

FORBIDDEN STALE PREMISE
Failed actuation -> False assumed state -> Quarantine -> Next probe -> Re-entry
```

World Simulation makes a persistent world disagree with an agent.

Forbidden Stale Premise prevents the agent from remembering an attempted transition as completed reality.

## Public Use

A project adopts the protocol by adding:

- explicit world state;
- transition and consequence records;
- a memory or doctrine injection path;
- Forbidden Stale Premise cards;
- replay fixtures;
- a promotion and demotion rule.

Start with [the memory adapter](adapters/MEMORY.md) and [the example card](fixtures/stale-confirmation.yaml).

## Authority Boundary

- Agent Closet owns portable doctrine and promotion.
- Project repositories own implementation evidence.
- Drive and private conversation may supply governed source material.
- Raw private conversations do not belong in a public repository.
- A downstream mirror must point to Agent Closet commits instead of silently forking doctrine.

## Contribution Rule

Bring one repeated failure.

A useful contribution turns it into:

1. an incident record;
2. a falsifiable stale premise;
3. a replay fixture;
4. a re-entry case;
5. evidence that behavior changed;
6. a negative-transfer check.

If a strong raw-context baseline performs equally well, do not invent new doctrine.
