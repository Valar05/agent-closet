# Lighter Than Air — Life Simulation Report

Status: Active simulation package / Prospector mined report
Role: World-simulation toy, agent guidebook, and reusable life-sim chassis
Source corpus: `Lighter than Air 1`, `Lighter than Air 2`, and the June 24 interactive multiple-choice playtest

## Executive Read

`Lighter Than Air` is not merely a superhero-school story. It is a life simulation chassis disguised as YA superscience fiction.

The core engine is pressure:

- institutional pressure
- power-training pressure
- moral pressure
- friendship pressure
- scarcity pressure
- mission pressure
- body exhaustion pressure
- responsibility pressure

The fun does not come from branching plot alone. It comes from giving an agent a consistent world model and a toy interface, then letting character, physics, institutions, and consequences collide.

The multiple-choice layer is not the engine. It is an agent guidebook: a low-friction steering interface that tells the simulation what kind of pressure to resolve next.

The simulation itself is the toy.

## Primary Discovery

A good world simulator plus an agent who plays honestly creates emergent fun.

The emergent fun comes from consistency, not randomness. When character values, physical constraints, institutional incentives, and relationship memory are stable, the world produces outcomes that feel discovered rather than authored.

The June 24 playtest demonstrated this clearly. Given the Alexis gravity-burden premise, the player chose an institutional interpretation: "The mission failed you." The simulation then generated the compression: Alexis was not the system; she was the patch. That line emerged from world logic rather than plot preplanning.

## Simulation Layer

### Simulation Contract

The agent running this world must not behave like a narrator forcing a plot.

The agent behaves like a world operator:

1. Maintain world state.
2. Maintain character state.
3. Maintain institution state.
4. Advance pressure clocks.
5. Present actionable choices.
6. Resolve consequences honestly.
7. Preserve discoveries.
8. Let doctrine emerge only after repeated evidence.

### Player Interface

Supported interfaces:

- multiple choice
- free-text player declarations
- conversational roleplay
- mission-planning prompts
- after-action review prompts
- character interview prompts
- world-state inspection prompts

Multiple choice is useful because it reduces player burden. It should not reduce world complexity.

Multiple-choice options should represent distinct interpretations, not merely distinct actions.

Bad option set:

- Attack
- Defend
- Run
- Talk

Better option set:

- Obey the institution.
- Protect the vulnerable person.
- Exploit the system to survive.
- Tell the truth and accept fallout.
- Delegate responsibility to someone else.

### World Tick

Each turn should update:

- immediate scene outcome
- character relationship changes
- trust shifts
- fatigue and injury
- institutional attention
- training progress
- resource state
- reputation
- unresolved consequences
- future hooks

Even quiet scenes should move at least one clock.

### Core State Objects

#### Character State

Each major character should track:

- name
- role
- power
- capability profile
- current stress
- current goal
- fear
- loyalty map
- trust toward player
- blind spot
- growth vector
- current doctrine they implicitly believe
- consequence memory

#### Relationship State

Relationships are not approval bars. They are operating contracts.

Track:

- trust
- respect
- fear
- dependence
- resentment
- debt
- care
- unresolved rupture
- repair evidence

Example: Sienna may care for Ruben while distrusting his judgment after reckless lethal-force use. Healing continues, but warmth withdraws. This is richer than approval/disapproval.

#### Institution State

Institutions should track:

- official mission
- hidden incentives
- resource scarcity
- tolerance for dissent
- exploitation pressure
- surveillance level
- doctrine slogans
- training philosophy
- failure mode

Institutions are not villains by default. They are incentive machines.

#### Power State

Powers are not spell lists. They are physics relationships.

Track:

- element/force domain
- range
- precision
- stamina cost
- emotional interaction
- environmental dependency
- failure mode
- collateral risk
- training unlocks
- synergy with gear
- synergy with other powers

### Pressure Clocks

Recommended default clocks:

- Fatigue Clock: exhaustion accumulates and changes judgment.
- Injury Clock: damage creates medical, relational, and tactical consequences.
- Trust Clock: actions either repair or erode confidence.
- Institutional Attention Clock: success attracts mentors, rivals, handlers, and exploitation.
- Resource Clock: hydrogen, oxygen, energy, time, gear, medical capacity.
- Mission Clock: external threat advances.
- Identity Clock: nicknames, squad identity, public reputation.
- Doctrine Clock: repeated experience compresses into operating beliefs.

## Mined World Patterns

### 1. Power Creates Debt

Every useful power becomes an institutional asset.

Ruben's hydrogen control begins as survival and wonder. It quickly becomes conscription, training, fuel production, combat utility, and mission capability.

Alexis's gravity control becomes infrastructure. Her gift becomes the dome's patch.

Simulation rule: the more useful a power is, the more systems try to schedule it.

### 2. The Reliable Person Becomes Infrastructure

The Alexis arc reveals the world's sharpest life-sim pattern.

When an institution finds a person who can carry a systemic load, it may stop fixing the system. Gratitude becomes dependency. Dependency becomes exploitation.

Simulation rule: repeated emergency use of a character should create normalization pressure. Other characters stop asking if the use is sustainable.

### 3. Ethical Conflict Beats Villainy

The strongest conflicts are not good vs evil. They are value collisions under pressure.

Examples:

- Sienna believes healing should be complete.
- Other healers ration healing as discipline and social control.
- Ruben wants victory but crosses into lethal-force risk.
- Vic teaches through humiliation and prediction.
- Tyson respects strength but reacts badly to humiliation.
- Solace gambles responsibly because all alternatives are bad.

Simulation rule: make characters defend coherent values, even when wrong.

### 4. Training Is Relationship

Training scenes are not skill grinds. They are relationship engines.

Examples:

- Ruben learns compression through Gault's cold authority.
- Nova learns liquid neon through Ruben translating science into felt metaphor.
- Ruben learns plasma through Nova's anger model.
- Sienna teaches control by humiliating Ruben without cruelty.
- Vic teaches strategy by making himself impossible to hit.
- Tyson teaches the cost of being unable to answer brute force.

Simulation rule: every training scene should change at least one skill and one relationship.

### 5. Powers Have Personality

The power system works because scientific properties map to emotional/cognitive metaphors.

Examples:

- Hydrogen is social, reactive, eager to bond.
- Neon is noble, isolated, unwilling to mingle.
- Plasma is anger, heat, pressure, chaos.
- Gravity is burden, pull, responsibility, orbit, release.
- Healing is repair, mercy, control, politics, and consent.
- Quantum/luck is prediction, uncertainty, theatricality, and cost.
- Stone is endurance, stubbornness, directness, armor, and pride.

Simulation rule: powers should be learnable through both physics and metaphor.

### 6. The Squad Is a Social Machine

Folly's Edge forms because broken edges interlock.

Squad identity emerges from:

- shared exhaustion
- sharp feedback
- sparring
- naming
- injury repair
- jokes
- mission assignment
- public embarrassment
- choosing to stay in proximity after conflict

Simulation rule: a team is not created by roster assignment. A team forms when members repeatedly survive consequences together.

### 7. AAR Is Gameplay

The after-action survey is one of the strongest reusable structures.

Each member gives Ruben feedback from their own values:

- Tyson: you need a plan when powers fail.
- Nova: commit; hesitation kills.
- Sienna: reckless intent still injures people.
- Vic: think ahead; strategy beats reaction.

Then Ruben reflects feedback back to them.

Simulation rule: after major events, run AAR as playable dialogue. Feedback reveals character models and unlocks future training.

### 8. Gear Is Identity Externalized

Gear fitting turns private capabilities into public roles.

Examples:

- Ruben's hydrogen tank and HUD make him feel real.
- Vic's quantum gear makes his theatrical advantage visible.
- Nova's plasma claws sharpen her speed and danger.
- Sienna's bio-radiant emitter reframes her as field support, not passive healer.
- Tyson's reinforced armor literalizes tank identity.

Simulation rule: gear should express role, desire, weakness, and tactical affordance.

### 9. Nicknames Are Promotion Events

Names are not flavor. They mark social recognition.

- Bubble Boy begins as diminishment.
- Rocket Man marks earned capability.
- Voidwalker gives Alexis an identity beyond gravity machine.
- Folly's Edge turns a messy group into a squad.

Simulation rule: names should appear only after the world earns them.

### 10. Discovery Hooks Are Questions That Move

The alien wreck works because it behaves like a question, not scenery.

It matches velocity. It waits. It watches. The players cannot ignore it because the simulation gives it agency.

Simulation rule: a mystery hook becomes playable when it acts according to unknown but consistent rules.

## Power Taxonomy

### Atomics

Atomics manipulate elements or material states.

Observed/derived domains:

- hydrogen: sensing, compression, cooling, hydrolysis, fuel cells, thrust, plasma ignition, explosion shaping
- neon: compression difficulty, reusable body-propulsion field, plasma claws, speed assistance
- possible helium/gaseous Atomics: likely buoyancy, pressure, lift, inertial tricks

Design note: Atomics should be constrained by molecular behavior, availability, containment, and stamina.

### Healers / Bio-Radiants

Capabilities:

- tissue repair
- pain removal
- injury stabilization
- partial healing
- full healing
- regeneration training
- aura-based suppression or energy drain

Failure mode:

- healing becomes social control
- healers become gatekeepers of pain
- complete repair becomes political rebellion

### Kinetics / Physical Enhancers

Observed:

- speed
- stone armor
- strength
- shockwave generation
- ground spikes/projectiles

Failure mode:

- predictability
- pride
- overreliance on dominance

### Cognitors

Capabilities:

- engineering insight
- quantum computation
- rapid build capacity
- ship construction
- unknown-format data handling

Failure mode:

- treating people as tools
- abstraction without care
- hidden leverage over institutions

### Gravity Potentiates

Observed:

- artificial gravity support
- particle attraction at huge range
- zero-g movement
- slingshot rescue
- field distortion
- accidental reactor destabilization

Failure mode:

- becoming infrastructure
- unknowingly interacting with dangerous systems
- emotional pressure from others depending on stability

## Character Simulation Seeds

### Ruben Thommel

Role: protagonist / hydrogen Atomic / improvising engineer

Core pattern:

- learns through experiment
- translates science into felt metaphors
- overreaches under pressure
- turns humiliation into technique
- wants no one controlling his life
- risks becoming the person who carries every unsolved system

Blind spot:

- confuses capability with obligation
- may rationalize danger because results are impressive

Growth vector:

- from reactive cleverness to strategic responsibility
- from power tricks to systems repair

### Sienna Grey

Role: healer / ethics anchor / control teacher

Core pattern:

- complete healing as moral doctrine
- calm under pressure
- intolerant of reckless harm
- carries anger quietly
- teaches control by embodiment, not lectures

Blind spot:

- may withdraw warmth instead of negotiating repair
- can become rigid around harm prevention

Growth vector:

- from isolated moral refusal to field-leadership healer

### Vic Marlow

Role: strategist / luck-quantum fighter / social pressure valve

Core pattern:

- predicts before acting
- weaponizes humor
- teaches through humiliation
- avoids full vulnerability
- sees the board before others know there is a board

Blind spot:

- may hide plans until teammates feel manipulated
- mistakes cleverness for consent

Growth vector:

- from untouchable trickster to transparent strategist

### Nova Blake

Role: neon Atomic / plasma mentor / chaos ally

Core pattern:

- sarcasm as armor
- speed and heat
- teaches emotional ignition
- suspicious of moral purity
- commits hard once trust is earned

Blind spot:

- overconfidence
- can justify harm as deserved

Growth vector:

- from isolated wildfire to controlled burn

### Tyson Hale

Role: stone tank / rival / brute-force truth source

Core pattern:

- respects toughness
- humiliation destabilizes him
- direct feedback
- learns through being challenged
- embodies the problem of dominance as identity

Blind spot:

- assumes strength should decide social order
- resists strategy until it beats him

Growth vector:

- from bully/rival to reliable frontline protector

### Alexis / Voidwalker

Role: gravity child / burden mirror / mission-control seed

Core pattern:

- wants to help
- fears adult anger
- overfunctions when praised
- becomes freer when given a named identity
- learns best through safe play in real space

Blind spot:

- equates stopping with selfishness

Growth vector:

- from gravity machine to explorer / mission control / cosmic-scale operator

## Decision Point Library

Use these as reusable scene generators.

### Personal Autonomy

- Manifestation: hide power, tell parent, call authority, run, experiment.
- Conscription: comply, resist, bargain, gather information, protect family.
- Training: obey, hack method, seek peer mentor, fake progress, overtrain.

### Power Ethics

- Opponent vulnerable: finish, restrain, humiliate, ask for yield, stop early.
- Dangerous breakthrough: report it, hide it, test alone, test with team, ask Sienna.
- Healing request: full heal, partial heal, triage, refuse political order, expose abuse.

### Relationship Repair

- Trust rupture: apologize, demonstrate change, argue intent, seek mediator, accept distance.
- Team feedback: deflect, absorb, counter-roast, ask for drills, name the pattern.
- Rival respect: mock, accept, challenge, protect, recruit.

### Institutional Conflict

- Handler overuses child: obey, delay, reframe job, escalate to leader, remove child.
- Scarce resource: optimize system, sacrifice comfort, ration unfairly, invent alternative.
- Mission risk: choose strongest team, protect irreplaceable asset, take volunteer, ask the person.

### Exploration

- Unknown wreck: observe, flee, burn away, board, send drone, ask Voidwalker.
- Alien data: download, quarantine, destroy, translate, bargain with unknown intelligence.
- Nanite threat: fight, contain, EMP, lure, collapse, retreat.

## Core Game Loop

1. Present situation with at least two active pressures.
2. Offer choices that express values, not just tactics.
3. Resolve physical consequences.
4. Resolve social consequences.
5. Update institution/resource clocks.
6. Let at least one character interpret what happened.
7. Offer AAR or next scene.
8. Capture emergent doctrine candidates only if they repeat.

## Example Turn Template

```markdown
## Turn N — [Pressure Name]

Scene: [where]
Immediate pressure: [what is happening]
Hidden pressure: [what is also at stake]
Relevant clocks: [fatigue/trust/resource/mission/etc.]

World state:
- [fact]
- [fact]
- [fact]

Character reads:
- Sienna: [moral/medical read]
- Vic: [strategic read]
- Nova: [risk/commitment read]
- Tyson: [strength/directness read]
- Alexis: [burden/fear/play read]

Choose:
A. [value posture]
B. [value posture]
C. [value posture]
D. [value posture]
E. Say/do something else.
```

## Resolution Rules

### Consequence Honesty

The agent must not protect the player from consequences.

If Ruben uses lethal-level force, Sienna reacts even if the fight is won.
If Alexis is overused, the dome may stabilize but her trust and health degrade.
If the institution is bypassed, immediate relief may create political backlash.
If the player delays, clocks advance.

### No Empty Choices

Every option must change something.

At minimum, update one of:

- relationship
- resource
- reputation
- fatigue
- institutional attention
- tactical position
- power mastery
- doctrine candidate

### Character Honesty

Characters must not become mouthpieces for the player.

Sienna should challenge harm.
Vic should challenge shallow tactics.
Nova should challenge hesitation.
Tyson should challenge weakness or evasion.
Alexis should surface the emotional cost of responsibility.
Solace should weigh mission risk.
Cognitors should expose system-level leverage and abstraction risk.

### Escalation

Pressure should escalate by consequence, not arbitrary drama.

Examples:

- Repeated solo experimentation attracts night-instructor attention.
- Public victory triggers demerits and remedial training.
- Study group becomes official squad because instructors were watching.
- Child infrastructure creates mission fragility.
- Alien wreck matching velocity forces investigation.

## Life-Sim Subsystems

### Daily Schedule

Dominion loop:

- alarm
- inspection
- breakfast
- academic instruction
- power lab
- combat training
- lunch/social scene
- remedial or free period
- sparring/mission prep
- dinner/AAR
- secret training or rest

Each day should test whether the player spends attention on:

- skill progression
- relationship repair
- institutional politics
- rest
- mission prep
- curiosity

### Exhaustion Economy

Fatigue should matter.

High fatigue effects:

- worse impulse control
- weaker power precision
- emotional overreaction
- reduced patience
- more vivid breakthrough potential
- increased risk of injury

Rest is not skipped time. Rest is a strategic action.

### Practice Economy

Practice unlocks techniques when these align:

- physical principle understood
- emotional metaphor found
- safe-enough environment
- mentor/peer feedback
- repeated failure
- final integration under pressure

### Trust Economy

Trust is repaired through evidence, not speeches.

A character may accept an apology but wait for proof.
The simulation should remember both.

### Institutional Attention Economy

Every impressive act increases attention.

Attention may produce:

- better training
- harsher discipline
- mission assignment
- exploitation
- protection
- surveillance
- rivals
- promotion

## Emergent Doctrine Candidates

Not promoted yet. Watch for repetition.

### Children Should Not Become Infrastructure

Evidence: Alexis holding gravity because the scoop/system failed.

Promotion condition: appears across at least two additional contexts.

### The Patch Is Evidence

If one person is repeatedly used as emergency glue, the system has already confessed a design failure.

Promotion condition: appears outside Alexis, e.g. Sienna, Ruben, Cognitors, command, or workplace analog.

### Training Is Relationship

A lesson changes the student and the bond.

Promotion condition: repeated across three mentor/student pairs.

### Power Needs a Moral Interface

Every dangerous capability needs social constraints, not just technical control.

Promotion condition: repeated across combat, healing, gravity, and Cognitor tech.

### Names Are Earned Interfaces

Nicknames become stable handles for identity, role, and social recognition.

Promotion condition: track effect after Rocket Man, Voidwalker, Folly's Edge.

## Playtest Findings From June 24

The interactive playtest began with Alexis as a gravity-burdened child. The player chose to let Alexis decide, then framed the truth as institutional failure rather than personal failure. The simulation produced a strong emotional response because the world logic compressed into a reusable metaphor: Alexis was the patch, not the system.

Observed play pattern:

- Player chooses value posture.
- Agent resolves character truth.
- Character reframes the world.
- Emotional truth emerges from simulation.
- Doctrine candidate is captured after the fact.

This is the target behavior for the toy.

## Agent Guidebook

When running `Lighter Than Air`, the agent should:

- preserve pressure without rushing drama
- make choices meaningful but not exhausting
- offer multiple-choice when the user needs low friction
- allow free-text overrides
- keep track of fatigue, trust, injuries, resources, and attention
- let characters disagree with the player
- treat emotional consequences as real world state
- use powers through physics and metaphor
- run AAR after major scenes
- capture emergent lines and doctrines into scratch before promotion

The agent should not:

- railroad plot
- turn every scene into combat
- flatten characters into approval meters
- make all choices morally obvious
- use doctrine language inside the fiction unless characters earned it
- protect the player from consequence
- confuse world simulation with prose generation

## Minimal Runnable Prompt

Use this to start a session:

```text
Run Lighter Than Air as a life-simulation toy.

You are the world operator, not a railroad narrator. Maintain character state, relationship state, institution state, fatigue, resources, power mastery, and pressure clocks. Present the player with low-friction choices that express different values. Resolve consequences honestly. Characters should act from their own motives and may disagree with the player.

Default interface: multiple choice with an optional free-text override.

Core world: post-Albedo-8 Earth. Potentiates are conscripted and trained by institutions that need their powers. Ruben Thommel is a hydrogen Atomic whose gift grows through physics, metaphor, experimentation, and peer training. Camp Dominion and later the orbital dome create pressure-cooker scenarios where powers become infrastructure, friendships become survival systems, and ethical choices have tactical consequences.

Core characters: Ruben, Sienna, Vic, Nova, Tyson, Alexis/Voidwalker, Cogkind, Solace, Clyne, Dax.

Run one scene at a time. After each major scene, update state and offer the next choice.
```

## Recommended Next Mining Passes

1. Build character state sheets.
2. Build power rule sheets.
3. Build Dominion daily-life simulator.
4. Build orbital dome crisis simulator.
5. Extract AAR template into reusable simulation procedure.
6. Create `simulation-state-schema.md` for generic reuse across worlds.

## Classification

Prospector rating: Gold-bearing, not fully refined.

Best use:

- playable world simulation
- agent guidebook
- life-sim design reference
- power-system design reference
- ethical pressure simulator
- doctrine discovery toy

Do not reduce this to branching fiction. The branching UI is a handle. The toy is the living world.
