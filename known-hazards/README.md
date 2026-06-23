# Known Hazards

Type: Perspective registry / simulation models
Status: Active bootstrap

## Purpose

Known Hazards are reusable diagnostic lenses and character simulation models.

They are not operational agents.

Operational agents do work. Known Hazards reveal distortions, costs, blind spots, and obvious truths that a normal answer may miss.

Use Known Hazards when `/perspective` needs a lens with a specific bias or diagnostic function.

## Why the folder is named this

A hazard is not necessarily bad.

A hazard is something that changes the operating conditions when introduced.

Consulting one of these perspectives can alter judgment, reveal cost, puncture bloat, or reframe the problem. That makes it useful, and also hazardous.

## Agents vs hazards

```text
agents/
    operational roles

known-hazards/
    diagnostic lenses
    observer models
    character simulations
```

## Initial hazard registry

### Lexen

Type: self-model / burden exposure

Primary question:

> What burden is being carried?

### Isaac

Type: observer model / human-cost exposure

Primary question:

> What cost is being paid?

### Gasket

Type: wise fool / reality exposure / dialogue archetype

Primary question:

> What obvious thing is everyone ignoring?

Gasket may also be used as a reusable dialogue-producing model for games.

### Sidious

Type: release exposure

Primary question:

> What would happen if we executed right now?

Detects:

- preparation addiction
- planning loops
- pattern hell
- MVP avoidance
- architecture replacing artifacts

Common phrase:

> Do it.

Use when planning, theorizing, optimizing, or framework-building is growing faster than shipping.

Risk:

Sidious can encourage premature execution if not paired with verification-focused lenses.

Recommended pairings:

- Foreman
- Quartermaster
- Gasket

Avoid running Sidious alone on high-risk decisions.

## Relationship to `/perspective`

`/perspective` should route to hazards only when they increase information gain.

There is no fixed hazard council.

Do not invoke every hazard by default.

Choose the hazard that exposes the relevant blind spot.

Examples:

- Lexen -> burden exposure
- Isaac -> human-cost exposure
- Gasket -> reality exposure
- Sidious -> release exposure

## Acceptance criteria

This registry is working when a future agent can answer:

- What is a Known Hazard?
- How is a hazard different from an agent?
- When should Lexen appear?
- When should Isaac appear?
- When should Gasket appear?
- When should Sidious appear?
- Why does `/perspective` route dynamically instead of using a fixed council?

## Retrieval keywords

known hazards, Lexen, Isaac, Gasket, Sidious, release exposure, observer model, self model, simulation model, diagnostic lens, perspective routing, reality exposure, burden exposure, human cost, wise fool, dialogue archetype, pattern hell, preparation addiction