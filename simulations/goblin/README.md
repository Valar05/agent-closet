# Goblin Simulation Space

Goblin is the first real Simulation Space.

A simulation space is a durable behavior substrate. It is not lore. It is not a biography store. It is not a setting bible. It is a queryable model for generating consistent behavior from reusable rules.

A good simulation space lets an agent ask:

- What kind of entity is this?
- How does it interpret commands?
- What mistakes does it reliably make?
- What names, dialogue, reactions, and actions fit this substrate?
- How does changing traits change the output?

## Why Goblin First

Goblin is the proof artifact because goblins are useful wrongness.

A goblin can be funny, dangerous, literal, overconfident, cowardly, loyal, greedy, mechanically useful, or catastrophically helpful. That makes Goblin a strong first test of whether a simulation space can generate consistent behavior instead of generic flavor.

Goblin is infrastructure for:

- Goblin Chess
- Goblinball
- NPC generation
- dialogue generation
- commentary generation
- command interpretation
- competent misunderstanding

## What This Space Generates

This space supports generation of:

- goblin names
- interpretations
- mistakes
- dialogue
- command responses
- behavior tendencies
- role variants
- likely collateral damage

It does not require goblin history, species lore, family trees, kingdoms, or canon biographies.

## How To Query It

Use a query shaped like this:

```text
Generate a [trait mix] goblin for [role/context].
```

Examples:

```text
Generate a smart but cowardly goblin.
Generate a goblin knight.
Generate a goblin who misunderstands "protect."
Generate a goblin sports commentator.
How would this goblin interpret "protect wizard"?
```

To answer, read:

1. `traits.md` for trait behavior.
2. `behavior-model.md` for trait combination logic.
3. `command-interpretation.md` for command response examples.
4. `names.md` for naming.
5. `dialogue-patterns.md` for speech.
6. `content-queries.md` for supported query forms.
7. `examples.md` for evidence patterns.

## Core Rule

The simulation space succeeds if this works:

```text
Query
↓
Consistent Goblin
```

No chat history. No external context. No lore dependency.
