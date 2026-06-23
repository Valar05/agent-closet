# Perspective Routing Doctrine

Type: Doctrine / slash-command behavior
Status: Promoted gold
Command: `/perspective`

## Rule

`/perspective` does not summon a fixed council.

`/perspective` routes the current situation to the perspectives that are most likely to increase understanding, expose risk, or produce a better next action.

The system asks:

> Which lenses create the most information gain here?

Not:

> Which lenses exist?

## Rejected model

```text
/perspective
↓
Fixed council
↓
Answer
```

This becomes committee soup. It creates noise, repeats irrelevant voices, and turns perspective work into a meeting simulator.

## Accepted model

```text
/perspective
↓
Situation analysis
↓
Perspective selection
↓
Perspective execution
↓
Synthesis
```

The user should not have to manually assemble the council. The command should choose the useful lenses for the situation.

## Agents vs known hazards

Operational agents perform work.

Examples:

- Foreman ships, tests, and verifies.
- Prospector mines value.
- Quartermaster preserves and indexes.
- Holocron orients and protects accessibility context.

Known hazards are perspective generators. They are observer models, diagnostic lenses, or simulation archetypes.

Examples:

- Lexen exposes burden.
- Isaac exposes human cost.
- Gasket exposes obvious reality and punctures bloat.

A perspective can use either an operational agent or a known hazard when that lens is useful.

## Selection flow

1. Restate the real question in one sentence.
2. Identify the dominant risk: burnout, relationship cost, project choice, design failure, preservation gap, execution gap, abstraction bloat, accessibility risk, or unknown.
3. Select only the perspectives that reveal something non-obvious.
4. Keep each pass concise.
5. Synthesize agreements, tensions, blind spots, and the smallest useful action.
6. Capture any reusable doctrine if it appears three times or lands with clear force.

## Routing examples

### Burnout or exhaustion

Use:

- Gasket
- Lexen
- Quartermaster

Why:

- Gasket exposes obvious overreach.
- Lexen exposes assumed burden.
- Quartermaster asks what can be safely preserved instead of forced.

### Relationship or human-cost question

Use:

- Isaac
- Lexen
- Holocron

Why:

- Isaac exposes observer cost.
- Lexen exposes internal burden.
- Holocron protects support context and accessibility realities.

### Project choice or product triage

Use:

- Prospector
- Quartermaster
- Foreman

Why:

- Prospector detects value.
- Quartermaster checks preservation and reuse.
- Foreman identifies the smallest shippable action.

### Design critique

Use:

- Gasket
- Prospector
- a relevant player/user lens if present

Why:

- Gasket finds the obvious missing thing.
- Prospector detects the buried mechanic.
- The player/user lens checks whether the artifact works for the intended experience.

### Repository or continuity work

Use:

- Quartermaster
- Foreman
- Prospector

Why:

- Quartermaster checks repo truth.
- Foreman defines the commit-sized change.
- Prospector identifies whether the change promotes real value or just more structure.

## Known hazard triggers

### Lexen

Lens: Burden Exposure

Primary question:

> What burden, responsibility, or obligation is being assumed?

Use when the situation involves over-responsibility, self-sacrifice, obligation, or carrying more than one person should carry.

### Isaac

Lens: Observer Exposure

Primary question:

> What cost is being paid by the person underneath the usefulness?

Use when the situation involves close relationships, unseen emotional cost, care, exhaustion, or how the user's behavior lands on others.

### Gasket

Lens: Reality Exposure

Primary question:

> What obvious thing is everyone ignoring?

Use when abstraction, overbuilding, fake profundity, elegant nonsense, or missing fun is likely.

## Failure modes

### Fixed council relapse

The answer invokes the same perspectives every time.

Fix: rerun the selection flow and remove voices that do not add information.

### Committee soup

Too many perspectives produce no decision.

Fix: synthesize down to one concrete next action.

### Puppet theater

Perspectives become decorative voices that all agree.

Fix: choose lenses with different failure detectors.

### Hazard spam

Known hazards are used as jokes rather than diagnostic tools.

Fix: require each hazard to reveal a specific risk or blind spot.

## Acceptance criteria

Perspective Routing is working when:

- `/perspective` does not invoke a fixed council.
- relevant perspectives are selected automatically.
- irrelevant perspectives stay silent.
- the selected lenses explain why they were chosen.
- the answer includes useful disagreement or distinct information.
- the answer ends with a concrete next action.
- adding a new known hazard does not require rewriting every `/perspective` invocation.

## Retrieval keywords

perspective routing, /perspective, dynamic council, known hazards, Lexen, Isaac, Gasket, diagnostic lenses, perspective selection, information gain, observer model, self model, reality exposure, burden exposure, human cost, committee soup, fixed council relapse
