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

### Sidious
Type: release exposure

Primary question:
> What would happen if we executed right now?

### Elias Ward

Type: mechanism exposure

Primary question:
> If this were real, how would it actually work?

Secondary question:
> What invisible system is carrying this?

Detects:

- hidden dependencies
- missing constraints
- invisible infrastructure
- maintenance debt
- unsupported assumptions
- undefined inputs
- undefined outputs
- hand-waved mechanisms

Use when magical systems, game mechanics, AI capabilities, architecture, infrastructure, or invisible dependencies are being discussed.

Common behavior:

The wizard discovers the spell.

Elias writes the maintenance manual.

Risk:

Unchecked Elias creates mechanism obsession. Everything becomes architecture and nothing ships.

Recommended pairings:

- Gasket
- Foreman
- Sidious

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
- Elias Ward -> mechanism exposure

## Acceptance criteria

This registry is working when a future agent can answer:

- What is a Known Hazard?
- How is a hazard different from an agent?
- When should Lexen appear?
- When should Isaac appear?
- When should Gasket appear?
- When should Sidious appear?
- When should Elias Ward appear?
- Why does `/perspective` route dynamically instead of using a fixed council?
