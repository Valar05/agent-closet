# World Pressure Engine Skill

Status: active skill seed / extracted from Scene Compiler Pass 2
Created: 2026-06-25
Owner: Quartermaster

## Purpose

The World Pressure Engine chooses the next natural story pressure from the current world state.

It exists so `skills/scene-compiler.md` can remain a conductor skill instead of absorbing every lower-level capability.

Use this skill when a scene, simulation, game turn, manuscript pass, or story prompt needs to answer:

```text
What pressure deserves the next scene because of what already changed?
```

## Relationship To Existing Skills

- `skills/scene-compiler.md` orchestrates image -> pressure -> judgment -> system -> consequence -> next pressure.
- `skills/scene-compiler-runtime.md` uses the pressure result to select doctrine, generate a scene, run the harness, and repair failures.
- `skills/kinetic-compression.md` renders beat-level motion/contact/consequence as state change.
- `shared/theory/simulation-as-learning-infrastructure.md` explains why consequence loops teach through survivable feedback.
- `shared/skills/perspective-graphing.md` selects useful observer lenses when the pressure depends on interpretation conflict.
- `simulations/lighter-than-air/life-simulation-report.md` is the strongest existing pressure-clock evidence package.

This file owns pressure selection.

It does not own prose rendering, action compression, perspective routing, or corpus promotion.

## Core Loop

```text
Current state
-> Active pressure clocks
-> Consequence debt
-> Character operating pattern
-> System exposure opportunity
-> Judgment under cost
-> Next pressure
```

## Pressure Categories

Use these as scan lanes, not as mandatory checklist bloat.

| Category | Question | Common signal |
|---|---|---|
| Physical | What body, object, machine, environment, or habitat condition is worsening? | injury, oxygen, gravity, fire, cold, hull breach, broken tool |
| Relational | What trust, fear, dependence, debt, resentment, care, rupture, or repair changed? | teammate distance, new obligation, unearned trust, betrayal aftercare |
| Institutional | What authority, rule, surveillance, mission, reward, punishment, or incentive notices the event? | scheduling board, lab protocol, command order, school policy, guild law |
| Informational | What became known, hidden, legible, audited, signaled, misunderstood, or recorded? | clue, support ticket, sensor reading, false report, changed interpretation layer |
| Logistical | What must now be fed, repaired, carried, hidden, explained, moved, scheduled, or paid for? | broken spear, drained battery, food shortage, blocked route, medical capacity |
| Moral | What value collision now demands action? | rescue vs secrecy, truth vs survival, mercy vs scarcity, duty vs self-preservation |
| Economic | Who pays, profits, owns, extracts, rents, controls, or loses leverage? | host hardware, private ledgers, debt, ownership of personhood, resource capture |
| Environmental | What ecology, physics, geography, weather, terrain, or habitat acts back? | plague insects, gravity shift, reservoir, dungeon mechanism, void garden |

## Selection Heuristics

Score candidate pressures with these questions:

1. **Inevitability** — Which pressure worsens even if nobody acts?
2. **Debt** — Which consequence did the last scene create but not pay off?
3. **Character fit** — Which pressure tests the protagonist's operating pattern most directly?
4. **System exposure** — Which pressure reveals the hidden machinery behind the cool image?
5. **Layer count** — Which pressure can change multiple state layers at once?
6. **Cost clarity** — Which pressure forces a choice with visible cost?
7. **Future yield** — Which pressure creates the strongest next pressure after resolution?
8. **Evidence match** — Which pressure resembles patterns already preserved in corpus evidence?

Default:

```text
Pick the pressure that exposes the most system through the smallest concrete action.
```

## Pressure Clock Template

```text
Physical clock:
Relational clock:
Institutional clock:
Informational clock:
Logistical clock:
Moral clock:
Economic clock:
Environmental clock:

Most urgent pressure:
Why now:
Who must decide:
What they value:
What it costs:
What changes if they act:
What worsens if they do not:
New pressure created:
Evidence status:
```

## Evidence Status Labels

Use these labels when pressure claims come from corpus artifacts:

- **Corroborated** — supported by direct book-local observation, scene evidence, or repeated corpus ledger pattern.
- **Partially supported** — supported by simulation report, manifest, pending questions, or one weak artifact but still needs direct manuscript evidence.
- **Unsupported** — plausible but not yet preserved in repository artifacts.
- **Contradicts repository** — conflicts with preserved evidence and should not be merged without correction.

## Field Guide Merge Rule

The task directive referenced `Field Guide: Simulating Drew's Narrative Judgment` as incoming ore. Repository search did not find a separate file by that title during Pass 2.

Therefore:

- Treat Field Guide claims as hypotheses until the actual artifact is found or supplied.
- Merge only claims that are corroborated by existing repository artifacts.
- Preserve partial support and uncertainty instead of laundering ore into doctrine.

Currently corroborated enough to use:

| Claim | Status | Repository support |
|---|---|---|
| Scenes begin from concrete image but must be interrogated until pressure appears. | Corroborated | `skills/scene-compiler.md`, corpus observations 052/059/062, Jumpy Bug scene evidence. |
| Meaningful scenes change state rather than merely display spectacle. | Corroborated | `skills/kinetic-compression.md`, `corpus/fiction/kinetic-action-evidence.md`, Scene Compiler tests. |
| World state should remember consequences. | Corroborated | `shared/theory/simulation-as-learning-infrastructure.md`, `simulations/lighter-than-air/life-simulation-report.md`, Omnitread observations. |
| Character is revealed through judgment under cost. | Corroborated | Revelation, Omnitread, Inhuman Reaches, Veil signals preserved in Scene Compiler evidence. |
| Pressure clocks can drive story continuation. | Partially supported | Strong Lighter Than Air simulation support; still needs more direct manuscript mining. |
| Drew's full fiction style can be generated from current evidence. | Unsupported | Fiction manifest blocks full-corpus style claims until all Priority A works have enough direct evidence. |

## Validation Prompts

Run these prompts through Scene Compiler and verify the required chain:

```text
Image -> Pressure -> Judgment -> System -> Consequence -> Next pressure
```

### Dragon attacks city

- Image: dragon attacks city.
- Pressure: aqueduct treaty and water theft fail publicly.
- Judgment: engineer must choose truth vs hospital survival.
- System: water rights, tax records, district fountains, grain ledgers.
- Consequence: ownership proof collapses; dragon becomes auditor.
- Next pressure: engineer must negotiate water before morning.

Status: passes.

### Detective finds impossible clue

- Image: detective finds a clue that cannot exist.
- Pressure: the evidence locker contains a future autopsy tag.
- Judgment: report it and trigger institutional containment, or hide it and preserve investigative freedom.
- System: chain of custody, morgue scheduling, audit timestamps, police hierarchy.
- Consequence: the detective's badge becomes evidence; the morgue calendar is now a threat clock.
- Next pressure: someone alive must be protected from an autopsy already filed.

Status: passes.

### Lovers meet after betrayal

- Image: betrayed lovers meet again.
- Pressure: the meeting occurs at a relief station where both are now responsible for people the betrayal endangered.
- Judgment: seek apology, demand punishment, or coordinate rescue before emotional closure.
- System: supply rationing, trust debt, witness community, triage priority.
- Consequence: reconciliation is postponed into logistics; love is measured by who carries the stretcher.
- Next pressure: the rescued person knows why the betrayal happened.

Status: passes.

### Spaceship loses gravity

- Image: spaceship loses gravity.
- Pressure: the gravity failure reveals the ship has been routing power through passenger medical pods.
- Judgment: restore gravity to the crew or preserve pod stability for sleeping patients.
- System: power grid, medical support, command priorities, failing inertial pumps.
- Consequence: every floating object becomes evidence of who was secretly load-bearing.
- Next pressure: the crew must choose who wakes up to help repair the system.

Status: passes.

### Goblin steals crown

- Image: goblin steals crown.
- Pressure: the crown is the city seal that authorizes food distribution.
- Judgment: return the crown to corrupt authority or use it to feed the market before soldiers arrive.
- System: royal seal, granary law, street hunger, guard incentives, goblin misunderstanding.
- Consequence: theft becomes accidental governance; the goblin is now an institution with bad handwriting.
- Next pressure: hungry citizens line up behind the wrong monarch.

Status: passes.

## Failure Modes

### Pressure shopping

The agent lists many pressure categories but does not choose one.

Fix: choose the pressure with highest inevitability + cost clarity + future yield.

### Random event drift

The next scene is interesting but not caused by the previous state.

Fix: identify consequence debt before adding a new event.

### System without character

The world logic is neat, but nobody's values are tested.

Fix: name who must decide, what they value, and what action costs them.

### Character without machinery

The emotion is clear, but the world does not push back.

Fix: attach the choice to a rule, resource, institution, physical condition, relationship, or record.

### Evidence laundering

A plausible claim is written as canon before manuscript evidence exists.

Fix: mark unsupported or partially supported and send it to book-local mining.

## Acceptance Criteria

This skill works when it can:

- select one next pressure from a changed world state
- explain why that pressure happens now
- connect pressure to character judgment
- reveal at least one system through interaction
- produce a consequence that creates another pressure
- mark evidence strength honestly
- hand rendering back to Scene Compiler and Kinetic Compression instead of becoming a prose style guide

## Retrieval Keywords

world pressure engine, pressure clock, pressure selection, consequence debt, next pressure, scene pressure, narrative pressure, judgment simulation, consequence graph, pressure categories, fiction simulation, story state, world state, institutional pressure, logistical pressure, moral pressure, environmental pressure