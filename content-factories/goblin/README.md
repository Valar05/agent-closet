# Goblin Content Factory

Status: Active

Purpose: reusable goblin generation rules.

This folder is a queryable factory. A future agent should be able to answer `Generate a goblin` using only these files.

## What Makes A Goblin Feel Like A Goblin

A goblin is not defined by lore. A goblin is defined by behavior under instruction.

Goblin behavior emerges when an agent combines:

- partial understanding
- strong self-interest
- high reactivity
- concrete interpretation
- opportunistic problem solving
- survival logic
- status hunger
- noisy feedback
- willingness to treat bad ideas as available tools

The goblin feeling appears when the answer is useful and wrong at the same time. The goblin often understands the immediate task, misses the implied constraint, and produces a result that technically connects to the command while creating new cleanup work.

The reliable pattern is:

```text
Command
-> literal or biased interpretation
-> action with self-protection, loot, status, panic, curiosity, or force attached
-> outcome that is legible, funny, dangerous, or accidentally useful
```

## Factory Files

Read in this order for generation:

1. `attributes.md` - trait sliders and low/medium/high behavior.
2. `names.md` - procedural names, titles, nicknames, and examples.
3. `behavior-model.md` - how traits become interpretations and actions.
4. `command-interpretation.md` - command examples for common goblin profiles.
5. `dialogue-patterns.md` - speech templates by function.
6. `content-queries.md` - supported query interface.
7. `examples.md` - proof outputs.

## Minimum Output For A Generated Goblin

Every generated goblin should include:

- name
- role or use case
- trait levels
- dominant decision pattern
- likely command interpretations
- likely mistakes
- dialogue samples

## Non-Goals

Do not add species history, kingdoms, canon biography, UI, game rules, AI architecture, or simulation categories here.

The factory is the artifact.
