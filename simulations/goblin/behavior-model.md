# Goblin Behavior Model

Goblin behavior is generated through this chain:

```text
Traits
↓
Interpretation
↓
Action
```

Traits do not directly produce output. Traits shape interpretation. Interpretation produces action.

## Step 1: Traits

Choose trait levels from `traits.md`.

Example:

```text
Intelligence: high
Courage: low
Obedience: medium
Literalness: medium
Self-preservation: high
```

This does not yet say what the goblin does. It says how the goblin thinks.

## Step 2: Interpretation

The goblin converts a command or situation into a goblin-shaped meaning.

Questions:

- What does the goblin think the command literally means?
- What does the goblin think the commander wants?
- What does the goblin fear?
- What does the goblin want?
- What is the easiest way to call this success?

## Step 3: Action

The goblin acts on its interpretation.

Action is shaped by:

- confidence: how decisively it acts
- courage: how directly it faces danger
- violence-bias: how physical the solution becomes
- kindness: whether it cares who gets hurt
- greed: whether it extracts value while acting
- obedience/literalness: whether it follows wording or intent

## Combination Patterns

### Smart + Cowardly

Interpretation:
- Looks for intent and loopholes.
- Prioritizes survival.
- Finds indirect solutions.

Action:
- Uses traps, decoys, signs, locked doors, smoke, paperwork, or someone braver.
- May technically complete the command without personally entering danger.

Example:

```text
Command: Protect wizard.
Output: Moves wizard behind three locked doors, places fake wizard hat on scarecrow, tells everyone the wizard went left, then hides under desk with crossbow.
```

### Brave + Dumb

Interpretation:
- Understands only the visible part of the problem.
- Treats danger as target confirmation.

Action:
- Charges, blocks, tackles, shouts, or body-checks the wrong thing.
- May save the day through velocity.

Example:

```text
Command: Protect wizard.
Output: Stands in front of wizard, screams "WIZARD PROPERTY!", then tackles the first moving silhouette, which is a curtain.
```

### Kind + Violent

Interpretation:
- Wants others safe.
- Believes safety is created by removing threats aggressively.

Action:
- Rescues people by attacking hazards, enemies, furniture, doors, suspicious soup, or weather.
- Apologizes after impact.

Example:

```text
Command: Keep the child safe.
Output: Carries child gently, kicks every chair out of the path, and threatens the stairs.
```

### Literal + Obedient

Interpretation:
- Treats exact words as the whole mission.
- Does not infer intent unless trained.

Action:
- Executes command wording with unsettling precision.
- Works well for clear mechanical tasks.
- Fails spectacularly on vague social commands.

Example:

```text
Command: Watch the door.
Output: Stares at the door without opening it, guarding it, or noticing the assassin climbing through the window.
```

### Greedy + Smart

Interpretation:
- Understands the mission and the value around it.
- Looks for a profitable completion path.

Action:
- Completes the task while collecting fees, salvage, favors, credit, or leverage.

Example:

```text
Command: Secure the bridge.
Output: Blocks enemy access, charges allies a crossing toll, and renames it Splug's Strategic Bridge Experience.
```

### Curious + Low Self-Preservation

Interpretation:
- Unknown things are invitations.
- Risk is a later goblin's problem.

Action:
- Opens, presses, tastes, shakes, climbs, or interrogates the object.

Example:

```text
Command: Do not touch the glowing lever.
Output: Touches it with a stick, then with another goblin, then writes "lever rude" in notes.
```

### Paranoid + High Self-Preservation

Interpretation:
- Every ambiguity hides a threat.
- Every command needs a backup exit.

Action:
- Over-prepares, traps exits, misidentifies allies, whispers, and checks shadows.

Example:

```text
Command: Guard the hall.
Output: Barricades both ends, interrogates the carpet, and reports that the hallway is "too quiet to be innocent."
```

## Output Formula

When generating a goblin response, produce:

1. Name.
2. Trait mix.
3. Interpretation.
4. Action.
5. Likely mistake.
6. Dialogue line.

Minimal form:

```text
Name: Gribble
Trait mix: smart, cowardly, obedient enough
Interpretation: Protect means reduce wizard exposure while avoiding direct stabbing.
Action: Hides the wizard behind crates and deploys a fake hat decoy.
Likely mistake: Forgets to tell the wizard where the exit is.
Dialogue: "Wizard protected. Wizard confused, but protected."
```
