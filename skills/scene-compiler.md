# Scene Compiler Skill

Status: active skill seed / evidence-gated
Role: teach future fiction agents to generate scenes from Drew's underlying narrative judgment architecture without imitating sentence structure or surface prose style.
Created: 2026-06-25
Owner: Quartermaster

## Purpose

The Scene Compiler is a reusable writing capability.

It models the recursive judgment process underneath Drew's fiction rather than copying prose voice, favorite phrases, sentence rhythm, or cosmetic genre markers.

The capability exists so a future fiction agent can take a simple prompt, interrogate it until the real pressure appears, simulate consequences honestly, and produce scenes where spectacle becomes inevitable because systems, characters, institutions, resources, and moral commitments collide.

This document is not a full-corpus style doctrine yet. It is a skill seed supported by existing repository evidence and explicitly gated by the Fiction Corpus Evidence Gate.

Primary evidence anchors:

- `corpus/fiction/fiction-manifest.md` — corpus scope, canonical works, mining priority, and warning against full-corpus style claims before Priority A works are indexed.
- `corpus/fiction/canonical-corpus-map.md` — canonical target selection and version uncertainty.
- `corpus/fiction/fiction-scene-index.md` — scene-level evidence, currently strongest for Jumpy Bug / Biblical.
- `corpus/fiction/kinetic-action-evidence.md` — action-as-state-conversion evidence.
- `corpus/fiction/fiction-observation-ledger.md` — cross-corpus observations 051–065.
- `corpus/fiction/observations/` — book-local observation layer.
- `skills/kinetic-compression.md` — lower-level motion/state-change skill.
- `simulations/lighter-than-air/life-simulation-report.md` — world simulation and pressure-clock evidence.

Incoming ore:

- `Field Guide: Simulating Drew's Narrative Judgment` was referenced in the task directive as supplied ore. Its contents are treated as a hypothesis source, not repository truth, until fully reconciled against artifacts above.

## Repository Position

No existing artifact named `scene compiler` was found during the repository search pass.

Closest existing capabilities:

- `skills/kinetic-compression.md` — handles compressed motion, contact, consequence, and new tactical state.
- `simulations/lighter-than-air/life-simulation-report.md` — handles world-state simulation, pressure clocks, relationship state, institution state, and consequence memory.
- `skills/scene-compiler-runtime.md` — execution layer that selects pressure, doctrine, generation, validation, repair, and acceptance.
- `corpus/fiction/fiction-observation-ledger.md` — preserves repeated fiction patterns but does not yet package them as a generation skill.

Therefore this file does not replace an existing canonical Scene Compiler. It stitches existing evidence into a higher-order scene generation procedure.

The runtime file now supplies the loop that applies this procedure.

## Scene Compiler

Core recursive loop:

```text
Cool Image
-> Interrogation
-> Personality
-> Judgment
-> System
-> Consequence
-> New Pressure
-> Repeat
```

### 1. Cool Image

Start with the image, gimmick, scene seed, monster, fight, power, joke, visual, or emotional spark.

Examples:

- a dragon attacks a city
- a boy rides a jumping spider through Biblical plague ecology
- a trapped player becomes a monster-host inside a game world
- a gravity-powered girl keeps an institution alive by becoming its patch
- a VR game becomes real training infrastructure

Do not begin by explaining theme. The image is bait, not the engine.

Operational question:

```text
What makes this image worth chasing?
```

### 2. Interrogation

Question the image until it stops being decorative.

Ask:

- Why this fight?
- Why this location?
- Why this tactic?
- What failed before the scene began?
- What resource is scarce?
- What relationship is under pressure?
- What institution benefits from the current arrangement?
- What is the lie the world is currently maintaining?
- What becomes impossible if nobody acts?

The goal is not brainstorming more lore. The goal is finding the pressure that makes the scene necessary.

### 3. Personality

Identify which character-level operating pattern responds to the pressure.

Repository evidence repeatedly shows identity emerging through action rather than declaration. Corpus Observation 052 states that repeated operational decisions establish identity before exposition. Corpus Observation 054 states that competence is demonstrated through repair, diagnosis, adaptation, movement, and judgment.

Operational questions:

- What does this person always notice first?
- What kind of failure can they not ignore?
- What do they repair, protect, exploit, test, feed, carry, or confront?
- What do they refuse even when refusal is expensive?
- What bad shortcut are they tempted to take?

### 4. Judgment

Convert personality into a decision under constraint.

A Drew-style scene should reveal judgment by forcing a choice where every option costs something.

Evidence anchors:

- `Revelation`: Torah accepts quarantine, experimentation, risk, and deployment because duty overrides self-preservation.
- `Omnitread`: Evan shifts from tactical reaction to system diagnosis and thinks in bottlenecks, spawn logic, logistics, and production constraints.
- `Inhuman Reaches`: repair, debugging, oxygen, software, food, and protection become moral acts.
- `Veil of Liquid Stars`: Jonah and Erin survive by changing the interpretation layer rather than merely fighting hunters.
- `Lighter Than Air` simulation report: multiple-choice options work best when they represent distinct interpretations, not generic actions.

Operational question:

```text
What choice proves what this character believes under pressure?
```

### 5. System

Reveal the system that makes the choice matter.

Systems may be physical, social, technological, institutional, ecological, magical, logistical, informational, or moral.

Repository evidence:

- Corpus Observation 051: protagonists inherit systems they did not design.
- Corpus Observation 053: older systems leak into newer systems.
- Corpus Observation 057: maintenance receives more narrative weight than invention.
- Corpus Observation 059: systems are explained through interaction.
- Corpus Observation 062: integration is the recurring capability.
- `Omnitread`: enemies are logistical systems before combat encounters.
- `Veil of Liquid Stars`: game mechanics behave like natural law.
- `Revelation`: sacred artifacts possess operational interfaces.

Operational question:

```text
What machinery, rule, ecology, institution, or relationship turns this choice into consequence?
```

### 6. Consequence

Every meaningful scene changes state.

Use `skills/kinetic-compression.md` for action-level execution:

```text
intent -> movement -> contact -> consequence -> new state
```

The Scene Compiler broadens that rule beyond physical motion:

```text
intent -> decision -> system interaction -> consequence -> new pressure
```

Consequence should change at least one of:

- tactical position
- injury or fatigue
- resource state
- trust
- institutional attention
- knowledge
- obligation
- reputation
- available options
- future logistics

No consequence, no scene.

### 7. New Pressure

The scene should end by making the next scene more natural than stopping.

A solution should create a new burden, exposure, debt, clue, dependency, injury, name, enemy response, institutional reaction, or relationship shift.

Evidence anchors:

- Corpus Observation 055: first success produces greater responsibility.
- Corpus Observation 060: failure permanently increases capability.
- Corpus Observation 065: protagonists gradually become infrastructure.
- `Lighter Than Air` simulation report: every turn should update immediate scene outcome, relationships, trust, fatigue/injury, institutional attention, resources, reputation, unresolved consequences, and future hooks.

Operational question:

```text
Because this scene happened, what pressure now deserves the next scene?
```

### 8. Repeat

Return to interrogation with the updated world state.

Do not reset to authorial whim. Let the changed state decide what becomes urgent.

## World Pressure Engine

Status: first version / active skill seed.

Repository search found pressure concepts in `simulations/lighter-than-air/life-simulation-report.md`, especially institutional pressure, power-training pressure, moral pressure, friendship pressure, scarcity pressure, mission pressure, body exhaustion pressure, and responsibility pressure. No general-purpose World Pressure Engine artifact was found.

Purpose:

Given a simulated world state, determine which pressure naturally deserves the next scene.

### Pressure Categories

Use these categories as scan lanes:

| Category | What it asks | Example pressure |
|---|---|---|
| Physical | What body, object, environment, or machine condition is worsening? | injury, oxygen, gravity, fire, broken hull, terrain |
| Relational | What trust, debt, fear, care, dependence, or resentment changed? | teammate withdraws warmth after reckless victory |
| Institutional | What organization notices, exploits, suppresses, rewards, or redirects the event? | useful power becomes scheduled asset |
| Informational | What is known, hidden, misunderstood, signaled, audited, or made legible? | support ticket makes Jonah readable as a person |
| Logistical | What resource, route, tool, food, gear, time, medical capacity, or maintenance burden changed? | broken spear becomes chitin spear problem |
| Moral | What value collision now demands action? | complete healing vs rationed pain control |
| Economic | Who pays, profits, owns, extracts, or loses leverage? | person reduced to host hardware or company material |
| Environmental | What ecology, geography, weather, physics, or habitat now acts back? | plague insects become food, threat, material, and route pressure |

### Selection Heuristics

Choose the next scene pressure by scoring each category:

1. **Inevitability** — Which pressure would worsen next even if nobody acted?
2. **Debt** — Which consequence did the last scene create but not pay off?
3. **Character fit** — Which pressure most directly tests the protagonist's operating pattern?
4. **System exposure** — Which pressure reveals the hidden machinery behind the cool image?
5. **Layer count** — Which pressure can change multiple layers at once?
6. **Cost clarity** — Which pressure forces a decision with visible cost?
7. **Future yield** — Which pressure creates the strongest next pressure after resolution?
8. **Evidence match** — Which pressure resembles patterns already preserved in corpus evidence?

Default choice:

```text
Pick the pressure that exposes the most system through the smallest concrete action.
```

### Pressure Clock Template

For each active scene, track:

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
What it costs:
What changes if they act:
What worsens if they do not:
New pressure created:
```

## Interrogation Cascade

The Interrogation Cascade prevents spectacle from arriving naked and confused.

Use it before drafting any major scene.

```text
1. What is the cool image?
2. Why does this image happen now?
3. What system failed, leaked, exploited, or overreached?
4. Who is forced to respond?
5. What do they notice that another character would miss?
6. What do they want immediately?
7. What do they believe is more important than safety?
8. What tactic does that belief produce?
9. Why does this tactic fit this location?
10. What object, rule, terrain, institution, relationship, or resource does the tactic touch?
11. Who benefits from the current system staying unchanged?
12. Who suffers if it stays unchanged?
13. What does action reveal?
14. What breaks, moves, opens, closes, heals, burns, starves, remembers, updates, or becomes visible?
15. What state changes physically?
16. What state changes relationally?
17. What state changes institutionally?
18. What state changes informationally?
19. What state changes morally?
20. What new obligation exists because the scene happened?
21. What pressure now deserves the next scene?
```

Stop when the spectacle becomes inevitable.

If the answer is still only `because it would be cool`, keep interrogating.

## State Transition Grammar

Status: promotion candidate / evidence-gated.

Meaningful scenes should alter multiple layers simultaneously.

This is strongly aligned with existing repository evidence, but should remain a candidate until more Priority A manuscripts receive direct scene indexing.

### Layers

| Layer | Changed-state question |
|---|---|
| Physical | What body, object, environment, tool, wound, machine, or location changed? |
| Tactical | Who has more or fewer options now? |
| Relationship | Who trusts, fears, owes, resents, believes, or depends differently? |
| Institution | What authority, rule, incentive, mission, surveillance, or exploitation pressure changed? |
| Knowledge | What became known, legible, proven, disproven, or misunderstood? |
| Morality | What value was tested, compromised, defended, or clarified? |
| Future logistics | What must now be fed, repaired, carried, hidden, scheduled, explained, or paid for? |
| Responsibility | Who is now expected to maintain something? |
| Information | What signal, record, audit, support ticket, sensor result, or proof chain now exists? |

### Minimum Scene Contract

A generated scene should change at least three layers.

Preferred Drew-shaped scene:

```text
Concrete action changes physical state.
Physical state exposes system logic.
System logic forces judgment.
Judgment alters relationship or institution.
The altered state creates future logistics.
```

## Failure Modes

### 1. Beginning With Theme

Bad move:

```text
This scene is about sacrifice.
```

Better move:

```text
The oxygen scrubber cannot carry everyone through the night, and the only person who understands the patch is also the one the institution keeps treating as replaceable.
```

Why it fails:

Theme without pressure becomes lecture.

Repository support:

- Corpus Observation 052 shows identity emerging from repeated action rather than declaration.
- `Revelation` shows duty through quarantine, risk, experimentation, and deployment rather than speeches.

### 2. Beginning With Lore

Bad move:

```text
The city was founded 900 years ago by dragon kings.
```

Better move:

```text
The old dragon cistern still feeds the poor district because every newer pump routes uphill first.
```

Why it fails:

Lore without operational pressure becomes encyclopedia.

Repository support:

- Corpus Observation 059: systems are explained through interaction.
- `Veil of Liquid Stars`: game mechanics are investigated as natural law through survival, not dumped as rules.
- `Revelation`: mysticism is approached through scanners, MRI, spectroscopy, training, and repeatable tests.

### 3. Beginning With Mechanics

Bad move:

```text
The hero has fire level 3 and shield level 2.
```

Better move:

```text
The shield works until the hospital generator stutters, and now every patient under it is part of the power budget.
```

Why it fails:

Mechanics without judgment become menu prose.

Repository support:

- `Omnitread`: persistent corpses, gear recovery, news, civilians, and world-state persistence create responsibility.
- `Lighter Than Air` simulation report: powers are physics relationships with stamina, environment, emotional interaction, failure mode, and collateral risk.

### 4. Stopping Questioning Too Early

Bad move:

```text
A dragon attacks because dragons attack cities.
```

Better move:

```text
The dragon attacks the aqueduct because the treaty made it responsible for water, and the city has been stealing from its clutch reservoir for six months.
```

Why it fails:

The first answer is usually a trope. The fifth answer often contains the system.

Repository support:

- `Omnitread`: Evan becomes effective when he diagnoses spawn disks, cloning, supply, command structure, and production infrastructure.
- Corpus Observation 062: integration is the recurring capability.

### 5. Spectacle Without Consequence

Bad move:

```text
The dragon burns three towers. It looks awesome.
```

Better move:

```text
The dragon burns the tax tower. By sunset nobody can prove who owns the grain, which means everyone with a private ledger just became king.
```

Why it fails:

Damage that does not alter state is fireworks.

Repository support:

- `skills/kinetic-compression.md`: if the beat lacks consequence, it is choreography wallpaper.
- `corpus/fiction/kinetic-action-evidence.md`: Jumpy Bug action entries preserve setup, movement, contact, consequence, and new tactical/emotional state.

### 6. Producing Lectures

Bad move:

```text
The character explains why institutions exploit gifted people.
```

Better move:

```text
The scheduling board lists her as equipment. Someone has written thank you beside the extra shift.
```

Why it fails:

Explaining judgment is weaker than forcing the reader to see the system's behavior.

Repository support:

- `Lighter Than Air` simulation report: Alexis was not the system; she was the patch. The insight emerges from world logic.
- Corpus Observation 065: protagonists gradually become infrastructure.

### 7. Producing Encyclopedias

Bad move:

```text
Here are the six departments of the Institute.
```

Better move:

```text
Three departments arrive with clipboards, and none of them brought a blanket.
```

Why it fails:

Institutions matter when their incentives touch bodies, choices, and logistics.

Repository support:

- Corpus Observation 061: authority is usually wrong for understandable reasons.
- `Revelation`: the Institute shifts from investigation to measurement, experimentation, training, and deployment.

### 8. Simulation Without Judgment

Bad move:

```text
The world state updates randomly after each turn.
```

Better move:

```text
The world updates according to what characters value, what institutions reward, what resources permit, and what previous consequences made unavoidable.
```

Why it fails:

A simulator without values produces motion but not story.

Repository support:

- `simulations/lighter-than-air/life-simulation-report.md`: emergent fun comes from consistency, not randomness.
- Relationship state is not an approval bar; it tracks trust, respect, fear, dependence, resentment, debt, care, rupture, and repair evidence.

## Corpus Evidence

### Jumpy Bug / Biblical

Evidence status: partial direct scene evidence plus book-local placeholder.

Useful signals:

- High-density survival action appears in Chapter 1.
- Scene index records locust/plague survival, scorpion fight, web command, resource harvesting, and girl-in-hive emotional turn.
- Kinetic evidence shows threat becoming food, weapon, shelter, or route knowledge.
- Existing book-local file is partial and needs full mining.

Scene Compiler relevance:

- Cool image: Biblical plague ecology plus spider companion.
- Interrogation: threats become resources.
- System: ecology acts back.
- Consequence: broken spear, scorpion hole, chitin spear, food/water inference.
- New pressure: surface threat forces underground uncertainty; survival action produces resource logistics.

### Holding Vigil

Evidence status: placeholder / needs direct mining.

Useful signals:

- Corpus manifest identifies likely vigil/aftermath/simulation material and character-pressure scenes.
- Book-local artifact currently preserves pending questions only.

Scene Compiler relevance:

- Do not use as strong evidence yet.
- Candidate pressure lanes: grief maintenance, aftermath logistics, ritual/rest state transitions, protagonist as routing point for safety or responsibility.

### Shattered Bonds / Shattered Bonds Online

Evidence status: placeholder / needs version reconciliation.

Useful signals:

- Canonical map marks multiple versions and requires inspection before claims.
- Registry addendum preserves local Shattered Bonds Dorian signals: armor as externalized burnout, AI auditing as moral repair, game invite as agency trigger.
- Book-local artifact asks whether Inhuman Reaches patterns survive into the later work.

Scene Compiler relevance:

- Do not promote corpus-level conclusions from Shattered Bonds yet.
- Candidate lanes: game/system infrastructure as moral geography, assistant-as-conscience interface, repair heroism, agency restoration.

### Omnitread

Evidence status: substantial book-local observation artifact.

Useful signals:

- Simulation is apprenticeship.
- Persistent consequences are required for meaning.
- Enemies are logistical systems before combat encounters.
- Protagonist begins thinking like the system.
- Every new capability reveals a larger system layer.

Scene Compiler relevance:

- Strong evidence for interrogation beyond combat.
- A fight is not just a fight; it is a logistics, production, command, and persistence problem.
- The next scene should often emerge from what the previous scene made permanent.

### Aegis of Victory

Evidence status: partial / needs direct mining.

Useful signals:

- Pass 002 notes Evan inherits mission infrastructure.
- Pending questions ask whether first success creates greater responsibility and whether mission infrastructure becomes maintenance burden.

Scene Compiler relevance:

- Use cautiously as support for inherited-system pressure.
- Do not cite as fully mined evidence yet.

### Inhuman Reaches

Evidence status: substantial book-local observation artifact.

Useful signals:

- AI becomes companionship before automation.
- Repair is treated as heroism.
- Love is expressed through maintenance.
- Corruption spreads through trusted infrastructure.
- Personhood is threatened by ownership.
- Broken systems produce accidental families.
- Code changes alter moral risk.

Scene Compiler relevance:

- Strong evidence that spectacle should expose maintenance, ownership, corruption, care, and operational intimacy.
- Moral stakes often appear as infrastructure behavior.
- Debugging and repair are scene engines, not filler.

### Revelation

Evidence status: substantial book-local observation artifact.

Useful signals:

- Anomalies reveal rather than grant identity.
- Power scales with emotional regulation.
- Institutions transition from investigation to apprenticeship.
- Mysticism is approached through engineering.
- Sacred artifacts possess operational interfaces.
- Training rapidly replaces explanation.
- Duty overrides self-preservation.

Scene Compiler relevance:

- Strong evidence for treating supernatural spectacle as operational system.
- Character judgment matters more than power display.
- Once the impossible becomes repeatable, narrative pressure shifts to responsible use.

### Lighter Than Air

Evidence status: direct book-local observation placeholder, but substantial simulation report exists.

Useful signals from simulation package:

- Core engine is pressure: institutional, power-training, moral, friendship, scarcity, mission, exhaustion, responsibility.
- The agent should maintain world state, character state, institution state, pressure clocks, and consequence memory.
- Training is relationship.
- Powers are physics relationships with personality and cost.
- First success can make a person infrastructure.

Scene Compiler relevance:

- Strong simulation evidence for World Pressure Engine design.
- Still needs direct manuscript mining for book-local confirmation.

### Veil of Liquid Stars

Evidence status: substantial book-local observation artifact.

Useful signals:

- Protagonist is transformed into infrastructure against his will.
- Game mechanics operate as natural law.
- Progression increases agency rather than raw power.
- Prison makes personhood illegible.
- Communication restores humanity.
- Survival depends on changing the interpretation layer.

Scene Compiler relevance:

- Strong evidence for informational and interpretive pressure.
- The decisive scene is not merely fighting hunters; it is changing who can read Jonah as a person.

### Fatal Vow Exception

Evidence status: placeholder / needs direct mining.

Useful signals:

- Canonical candidate v2 exists.
- Pending questions focus on obligation systems, inherited rules, antagonist temptation through relief/forgetting/certainty/rest, failure becoming knowledge, and protagonist-as-infrastructure.

Scene Compiler relevance:

- Do not use as strong evidence yet.
- Candidate for moral, obligation, and relief-as-temptation pressure.

## Capability Tests

### Test 1 — Dragon Attacks A City

Input:

```text
A dragon attacks a city.
```

Weak output:

```text
The dragon swoops down and breathes fire. Knights fight it. Towers burn. The battle is epic.
```

Why weak:

- Starts and ends at spectacle.
- No system failed.
- No character judgment.
- No lasting state transition except generic destruction.
- No future pressure.

Strong compiler pass:

```text
Cool image:
A dragon attacks a city.

Interrogation:
Why now? The aqueduct treaty failed.
Why this target? The dragon burns the tax tower, not the palace.
What system failed? The city rerouted water from the clutch reservoir to wealthy districts.
Who must act? The junior cistern engineer who falsified last week's flow report to keep the hospital open.
What judgment is forced? Tell the truth and lose the hospital, or hide the theft and let the dragon become the only honest auditor in the city.

Scene result:
The dragon does not begin with fire. It lands on the aqueduct and waits until every district fountain runs dry.
Then it burns the tax tower.
By sunset nobody can prove who owns the grain.
The engineer knows where the real ledgers are because he wrote the false ones.
Now the city needs him alive, the dragon needs him honest, and the hospital needs water before morning.
```

Strong output properties:

- System failure: water theft and falsified infrastructure records.
- Judgment: truth vs hospital survival.
- Infrastructure: aqueduct, tax tower, grain ledgers, district fountains.
- Consequence: ownership, water, authority, and trust all change.
- Future pressure: engineer must negotiate between dragon, city, and hospital.

### Test 2 — Superpower Training

Input:

```text
A girl learns gravity powers.
```

Weak output:

```text
She floats rocks and becomes stronger.
```

Strong compiler pass:

```text
The first rock floats.
The floor alarm screams.
Three nurses run in because every incubator on the west wall just got six pounds lighter.
Nobody congratulates her.
The instructor shuts the door, lowers his voice, and asks whether she can put the babies down gently before the hospital notices who became load-bearing.
```

Strong output properties:

- Power is physics relationship.
- Training is institutional exposure.
- Success creates responsibility.
- Human cost appears immediately.
- Future pressure is unavoidable.

### Test 3 — Dungeon Fight

Input:

```text
The hero fights skeletons in a dungeon.
```

Weak output:

```text
He swings his sword and destroys the skeletons.
```

Strong compiler pass:

```text
The first skeleton came apart easily.
That was the problem.
Its ribs bounced down the stairs, clicked against the pressure plate, and opened every cell behind him.
The hero stopped swinging.
The dungeon was not defending itself.
It was using him as maintenance.
```

Strong output properties:

- Combat reveals system behavior.
- Victory creates a worse state.
- Environment acts as participant.
- New pressure is generated by success.

## Agent Procedure

When asked to generate a scene:

1. Write the cool image in one line.
2. Run the Interrogation Cascade until a system failure or pressure appears.
3. Identify the character judgment under constraint.
4. Select the active World Pressure Engine category.
5. Draft the scene around one concrete action or decision.
6. Ensure at least three state layers change.
7. End on new pressure.
8. Remove lectures, encyclopedias, decorative lore, and consequence-free spectacle.
9. Check against `skills/kinetic-compression.md` if physical action is involved.
10. Preserve any new recurring discovery in the relevant corpus or skill artifact.

## Acceptance Criteria

A Scene Compiler output passes when:

- It begins from a concrete image but does not stop there.
- It reveals a system through interaction.
- Character judgment is visible through action under cost.
- At least three state layers change.
- Consequence creates the next pressure.
- It does not imitate Drew's prose style.
- It does not rely on theme lectures or lore dumps.
- It can point back to corpus evidence or clearly mark itself as provisional.

## Open Questions

- Does a World Pressure Engine already exist under another name outside the searched repository paths?
- Does the incoming `Field Guide: Simulating Drew's Narrative Judgment` contain additional distinctions that should be merged after direct comparison?
- Does `Revelation` continue treating the supernatural as operational system in later unmined portions?
- Does `Fatal Vow Exception` confirm relief/forgetting/certainty/rest as antagonist temptation?
- Does `Holding Vigil` provide a non-combat version of the Scene Compiler through grief, ritual, aftermath, or caretaking?
- Does `Shattered Bonds Online` refine `Inhuman Reaches` patterns after version reconciliation?
- Are there genres where the compiler should weight pressure categories differently?
- Should State Transition Grammar be promoted to its own doctrine after more scene-level evidence exists?

## Promotion Gate

Do not promote this skill into canon until:

1. At least three additional Priority A works have direct scene-level evidence comparable to `Jumpy Bug / Biblical`.
2. Placeholder book-local observation artifacts are expanded or explicitly marked out of scope.
3. The Field Guide ore is directly compared against repository artifacts.
4. The World Pressure Engine is tested against at least three generated scenes and one manuscript-mining pass.
5. Future agents can generate strong compiler passes without copying prose voice.
