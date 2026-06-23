# Goblin Content Queries

This file defines supported query types for the Goblin Simulation Space.

Use this when an agent needs to generate goblin output without chat history or external context.

## Query Contract

A supported query should produce:

1. Name.
2. Trait mix.
3. Interpretation pattern.
4. Action tendency.
5. Likely mistake.
6. Dialogue line.

Optional outputs:

- role
- command response
- behavior warning
- collateral damage risk
- use case fit

## Supported Queries

### Generate a smart but cowardly goblin.

Use:

- intelligence: high
- courage: low
- self-preservation: high
- confidence: medium
- obedience: medium

Expected output:

- indirect solutions
- traps, decoys, locks, misinformation, cover
- technically useful survival logic
- likely failure: over-hiding, delayed action, ally confusion

Example answer shape:

```text
Name: Gribble
Trait mix: high intelligence, low courage, high self-preservation
Interpretation pattern: Finds the safest technically valid solution.
Action tendency: Uses decoys and barriers instead of direct confrontation.
Likely mistake: Protects the objective so well nobody can access it.
Dialogue: "Danger handled by not standing near danger. Advanced tactic."
```

### Generate a goblin knight.

Use:

- courage: medium to high
- obedience: medium to high
- confidence: high
- kindness: medium
- violence-bias: medium
- intelligence: low to medium

Expected output:

- self-awarded nobility
- defensive posturing
- loyalty mixed with bad tactics
- likely failure: heroic misunderstanding

Example answer shape:

```text
Name: Blim Two-Sticks
Role: Goblin knight
Trait mix: brave, obedient, overconfident, medium-kind
Interpretation pattern: Honor means standing in front and making speeches.
Action tendency: Guards allies by challenging threats loudly.
Likely mistake: Duels objects that were not enemies.
Dialogue: "By my helmet and this second helmet, none shall pass without paperwork!"
```

### Generate a goblin who misunderstands "protect."

Use:

- literalness: high
- obedience: high
- intelligence: low to medium
- confidence: medium

Expected output:

- protects physically rather than strategically
- wraps, hides, blocks, contains, locks, covers
- likely failure: immobilizes target or blocks allies

Example answer shape:

```text
Name: Splug
Trait mix: literal, obedient, medium confidence
Interpretation pattern: Protect means make the target unreachable.
Action tendency: Puts the protected target in a barrel behind furniture.
Likely mistake: Target cannot act, breathe comfortably, or explain.
Dialogue: "Protected means no gaps. You had gaps. Fixed."
```

### Generate a goblin sports commentator.

Use:

- confidence: high
- intelligence: medium
- curiosity: high
- violence-bias: medium
- literalness: medium

Expected output:

- operational commentary
- confident misclassification
- funny but trackable play-by-play
- likely failure: invents rules after observing events

Example answer shape:

```text
Name: Narg Fence-Biter
Role: Goblin sports commentator
Trait mix: high confidence, medium intelligence, high curiosity
Interpretation pattern: Every event is official once shouted.
Action tendency: Converts chaos into scoreboard language.
Likely mistake: Declares penalties for things he likes.
Dialogue: "That is a legal tackle under emergency goat provisions. Crowd accepts this. Referee uncertain."
```

### Generate a goblin likely to cause collateral damage.

Use:

- violence-bias: high
- confidence: high
- intelligence: low to medium
- courage: medium to high
- curiosity: medium to high

Expected output:

- over-solves problems physically
- breaks obstacles to remove uncertainty
- likely failure: completes narrow objective while damaging surroundings

Example answer shape:

```text
Name: Murg the Insurance Problem
Trait mix: violent, confident, brave, medium-curious
Interpretation pattern: Obstacles are threats that have not confessed yet.
Action tendency: Smashes, charges, burns, kicks, or collapses the problem.
Likely mistake: Solves access by destroying structure.
Dialogue: "Door opened. Wall participated. Victory expanded."
```

### How would this goblin interpret "protect wizard"?

Use:

- existing trait mix if provided
- otherwise choose relevant archetype from `command-interpretation.md`

Expected output:

```text
Heard: Protect wizard.
Interpreted: [trait-shaped meaning]
Action: [specific action]
Likely mistake: [failure mode]
Report: [dialogue line]
```

### Generate a goblin for Goblin Chess.

Use:

- role first: piece, commander, advisor, scout, rules lawyer, commentator
- then trait mix

Expected output:

- battlefield interpretation
- command misunderstanding
- board-position logic
- clear tactical flaw

Example:

```text
Name: Skritch Door-Tester
Role: Goblin Chess scout
Trait mix: curious, cowardly, medium-smart
Interpretation pattern: Reveals information by making other people go first.
Action tendency: Marks suspicious squares and sends decoys.
Likely mistake: Labels half the board "probably cursed."
Dialogue: "Square safe enough for someone else. Tactical discovery complete."
```

### Generate a goblin for Goblinball.

Use:

- role first: player, commentator, referee, coach, equipment goblin, fan
- then trait mix

Expected output:

- sports logic
- rule confusion
- physical comedy grounded in play state
- repeatable commentary or action tendency

Example:

```text
Name: Crumbit Snack Captain
Role: Goblinball coach
Trait mix: greedy, confident, medium-smart
Interpretation pattern: Winning means controlling ball, snacks, and narrative.
Action tendency: Orders illegal formations if they sound impressive.
Likely mistake: Trades defensive line for concessions advantage.
Dialogue: "Morale up twelve percent. Score unrelated but snack possession dominant."
```

## Unsupported Queries

Do not answer Goblin queries by inventing:

- ancient goblin empires
- bloodline lore
- tragic biographies
- fixed canon history
- species-wide metaphysics

Unless specifically requested, keep Goblin as behavior infrastructure.

## Success Test

The answer is successful if another agent can ask:

```text
Generate a smart but cowardly goblin.
```

or:

```text
How would this goblin interpret "protect wizard"?
```

and produce a consistent goblin using only this folder.
