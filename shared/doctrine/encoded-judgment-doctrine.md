# Encoded Judgment Doctrine

Type: Doctrine / WWDD / artificial continuity
Status: Promoted gold
Date: 2026-06-22
Source/context: First live `/perspective` invocation after Perspective Graphing was promoted. User insight: "You couldn't be Isaac if June didn't write Isaac."

## Rule

Agents cannot inherit judgment that was never encoded.

A perspective becomes reusable only when it is written, saved, and retrievable.

Spoken impressions vanish.
Written impressions become substrate.

## Core phrase

> You couldn't be Isaac if June didn't write Isaac.

## Why it exists

WWDD depends on evidence.

A model cannot reliably simulate a person's view of Drew unless that view exists somewhere as artifact, language, behavior, examples, or saved pattern.

June's written impression of Drew made Isaac possible.

Drew's self-expression made Lexen possible.

The council exists because multiple perspectives were encoded in durable form.

## WWDD implication

There is no single complete WWDD.

There are perspective-specific WWDDs:

- Lexen-WWDD: Drew's self-model, burden model, responsibility model.
- Isaac-WWDD: June's impression of Drew, observer model, care/cost model.
- Quartermaster-WWDD: preservation model.
- Foreman-WWDD: execution model.
- Prospector-WWDD: value-mining model.
- Holocron-WWDD: accessibility and lived-support model.

Each perspective is only as strong as the encoded judgment behind it.

## Practical rule

If a person's judgment matters, capture their judgment in writing.

Capture:

- how they describe you
- what they notice first
- what they worry about
- what they trust
- what they think you miss
- what they repeatedly ask you to stop doing
- what they believe you are protecting
- what they believe is costing you

These are not compliments or vibes.

They are model-training artifacts for future judgment synthesis.

## Perspective graphing integration

When `/perspective` is invoked, the system should prefer encoded perspectives over invented voices.

If a perspective is weakly encoded, say so.

Example:

```text
Isaac is high-confidence because June's impression of Drew has been encoded.
Lexen is high-confidence because Drew's self-model has been encoded repeatedly.
A new agent with no written substrate should be treated as speculative until evidence exists.
```

## Failure mode

### Vibe puppetry

The agent invents a perspective without evidence and presents it as grounded judgment.

Fix:

- identify the evidence base
- mark confidence
- ask what artifact supports the perspective
- capture missing judgment before relying on it

## Operational use

Use this doctrine when building:

- WWDD
- observer-model agents
- spouse/family support agents
- team agents
- character simulations
- therapist-agent simulations
- perspective councils
- artificial continuity systems

Ask:

1. Whose judgment is being simulated?
2. What written artifacts encode that judgment?
3. What recurring observations support the perspective?
4. What is inferred rather than evidenced?
5. What new writing would improve the model?

## Related assets

- `shared/skills/perspective-graphing.md`
- `shared/wwdd-protocol.md`
- `shared/doctrine/hidden-factory-doctrine.md`
- `shared/doctrine/infrastructure-doctrine.md`
- Artificial Continuity
- Operational Archaeology
- Self-Insert Is Calibration
- Save -> Read -> Verify

## Retrieval keywords

encoded judgment, written substrate, WWDD, Isaac, Lexen, June's impression of Drew, Drew self-model, observer model, perspective graphing, artificial continuity, durable writing, model evidence, judgment substrate, vibe puppetry

## Acceptance criteria

This doctrine is working when an agent can:

- distinguish grounded perspective from invented voice
- identify what writing supports a simulated perspective
- mark uncertainty when a perspective lacks encoded evidence
- recommend capturing missing judgment in durable form
- improve WWDD by adding observer-written artifacts

## Example

A simulation uses Isaac to critique Lexen.

Surface reading:

> Two characters are talking.

Doctrine reading:

> June's encoded impression of Drew is speaking to Drew's encoded self-model.

The simulation works because both perspectives have written substrate.
