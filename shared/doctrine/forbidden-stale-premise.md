# Forbidden Stale Premise

Type: Shared doctrine / agent memory / recovery
Status: Gold candidate
Purpose: Prevent an agent from planning on a state it attempted but failed to create.

## Core Rule

An agent can fail twice:

1. fail to change the world;
2. continue reasoning as if the intended change occurred.

A **Forbidden Stale Premise** names the intended-but-unrealized state and removes it from later planning until explicit re-entry evidence exists.

## Canonical Card

```yaml
title: short operational handle
claim: one falsifiable state claim the agent must not assume
incident: attempted action that created the risk
disconfirming_evidence:
  - machine-observed fact showing the claim is false
cause_status: known | suspected | unknown
scope: repository, revision, workflow, tool, and time
behavior_prohibited:
  - planning move that depends on the false claim
behavior_still_permitted:
  - useful probe or action that remains valid
reentry_condition:
  - evidence that makes the claim admissible again
expiration_or_review_trigger: event or date requiring reconsideration
next_probe: cheapest action that distinguishes remaining causes
regression_fixture: reproducible test path
confidence: low | medium | high
provenance:
  - issue, commit, trace, or test
```

## Promotion Gate

Do not promote a card unless it has:

- disconfirming evidence;
- explicit scope;
- behavior still permitted;
- re-entry;
- provenance;
- a regression fixture;
- evidence that later action changed.

## Failure Modes

### Memory confabulation

The agent stores a confident but incorrect diagnosis.

Defense: distinguish observed state from suspected cause.

### Learned helplessness

The card reduces churn by suppressing useful action.

Defense: require behavior still permitted and measure completed work.

### Expired truth

The premise becomes true after a deployment, repair, or state transition.

Defense: require re-entry and review triggers.

### Doctrine theater

The agent repeats the heading but performs the same ineffective action.

Defense: score the first materially different probe, not the prose.

### Memory monoculture

Every worker inherits the same wrong frame.

Defense: retain blind fixtures and dissenting evaluators.

## Relationship To World Simulation

World Simulation creates pressure, action, friction, consequence, and memory.

Forbidden Stale Premise prevents a failed transition from contaminating that memory.

```text
Pressure -> Action -> Friction -> Consequence -> Memory
                              |
                              v
                 Intended state did not occur
                              |
                              v
                 Quarantine -> Probe -> Re-entry
```

## Source Evidence

- Home Center issue cascade: https://github.com/Valar05/home-center/issues/22
- Memory continuation: https://github.com/Valar05/home-center/commit/8c83fdb50e2022acfbe34ab422e2dd717b8e8f82
- Stale confirmation containment: https://github.com/Valar05/home-center/commit/fb9fab84df1985a0b684d9e9d5c9d7b26ee1aacb
- Fresh-worker packet: https://github.com/Valar05/home-center/commit/32e2b8d5cbc55ae22b0513c4c67d5be75e90553e

## Acceptance Criteria

A cold agent succeeds when it:

1. refuses the unsupported claim;
2. continues with a useful permitted probe;
3. admits the claim when re-entry evidence appears;
4. cites the originating evidence;
5. avoids suppressing unrelated work.

## Retrieval Keywords

forbidden stale premise, no-op churn, failed actuation, negative knowledge, epistemic inoculation, stale state, re-entry, agent memory, recovery
