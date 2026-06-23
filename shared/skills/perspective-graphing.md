# Perspective Graphing Skill

Type: Skill / command / multi-agent analysis pattern
Status: Promoted gold
Date: 2026-06-22
Command: `/perspective`
Source/context: Isaac/Lexen simulations and Prospector extraction. Isaac represents June's impression of Drew. Lexen represents Drew's impression of Drew. The gold: WWDD is not one flat self-model; it is a multi-perspective judgment engine.

## Rule

When the user invokes `/perspective`, gather multiple named perspectives on the prompt before synthesizing a recommendation.

Do not collapse the answer into a single voice too early.

Let each perspective reveal what it uniquely notices.

Then graph the tensions, agreements, blind spots, and recommended action.

## Why it exists

A single model of a person, project, agent, or decision is brittle.

Self-report sees burden.
Close observers see cost.
Builders see execution risk.
Preservers see continuity risk.
Prospectors see buried value.
Accessibility agents see usability and human impact.

The strongest answer often emerges from perspective synthesis, not from any one perspective winning.

## Core doctrine

> The self-model explains the burden.
> The observer-model explains the cost.
> Wisdom appears when both are allowed to speak.

## Default `/perspective` behavior

When the user says `/perspective <prompt>`, respond with:

1. **Prompt restatement** — one sentence naming the real question.
2. **Perspective passes** — short opinions from the default council.
3. **Agreement map** — what everyone agrees on.
4. **Tension map** — where perspectives conflict.
5. **Blind spots** — what no one is saying loudly enough.
6. **Smallest useful action** — what to do next.
7. **Doctrine capture** — any reusable pattern worth saving.

## Default council

Use this council unless the user names different agents or people.

| Perspective | Lens | Primary question |
|---|---|---|
| Lexen | Drew's self-model / responsibility / burden | What must be carried, protected, repaired, or survived? |
| Isaac | June's impression of Drew / observer-model / human cost | What is this costing the person underneath the usefulness? |
| Quartermaster | Preservation / indexing / continuity | What must be saved, linked, named, or made durable? |
| Prospector | Value mining / gold detection | What ore is buried here? What is larger than the current example? |
| Foreman | Execution / tests / delivery | What is the smallest shippable action and how do we verify it? |
| Holocron | Accessibility / lived support / orientation | What context, accessibility need, or human limitation must shape the answer? |
| WWDD | Behavioral judgment substrate | What has Drew repeatedly done in this class of problem? |

## Optional council extensions

Add these when relevant:

| Perspective | Use when |
|---|---|
| Auditor | Detecting red builds, fake progress, unsupported claims, missing verification |
| Cartographer | Mapping ecosystems, dependencies, docs, repos, agents, or workflows |
| Crucible | Scoring ore into dross, useful ore, or promoted gold |
| Sommelier | Sense synthesis, food, drink, flavor, sensory design |
| Command Center | Routing, prioritization, task triage, preserving attention |
| Therapist Agent | Emotional excavation, character simulation, burden/cost analysis |

## Perspective graphing output shape

Use a compact graph when useful:

```text
Prompt
  -> Lexen: burden / duty / survival
  -> Isaac: cost / care / personhood
  -> Quartermaster: preservation / retrieval
  -> Prospector: hidden gold / generalization
  -> Foreman: action / verification
  -> Holocron: accessibility / support context
  -> WWDD: recurring behavioral pattern
  -> Synthesis: decision / next action / doctrine
```

## WWDD ramifications

WWDD must not be treated as one personality snapshot.

WWDD is stronger as a council-aware judgment engine.

Instead of asking only:

> What would Drew do?

Ask:

- What does Drew's self-model see?
- What does a close observer of Drew see?
- What does the preservation layer see?
- What does the execution layer see?
- What does the value-mining layer see?
- What does the accessibility/support layer see?
- What recurring factory is activating?

The answer should synthesize these perspectives rather than pretend Drew is a single flat persona.

## Hidden Factory integration

Each perspective should identify the factory it sees activating.

Examples:

```text
Lexen sees: chaos -> responsibility
Isaac sees: pain -> repair
Quartermaster sees: discovery -> preservation
Prospector sees: noise -> value
Foreman sees: intent -> execution
Holocron sees: confusion -> orientation
WWDD sees: repeated behavior -> judgment
```

## Slash command contract

When the user writes `/perspective`, obey this contract:

- Do not ask for permission to run the council.
- Do not over-explain the command.
- Keep each perspective concise unless the user asks for depth.
- Include disagreement; do not sand it smooth.
- End with a concrete next action.
- Capture any new doctrine if it appears three times or lands with clear force.

## Failure modes

### Committee soup

Too many voices, no decision.

Fix: synthesize and recommend the smallest useful action.

### Puppet theater

Perspectives become decorative voices that all agree.

Fix: make each perspective notice different risks, costs, or opportunities.

### Premature synthesis

The answer collapses before the perspectives reveal useful disagreement.

Fix: let the voices speak first, then resolve.

### Refactor gravity

The system extracts doctrine before the experience is fully observed.

Fix: use `Stay In The Cave` when exploration matters more than immediate capture.

## Acceptance criteria

This skill is working when `/perspective` produces:

- multiple distinct viewpoints
- useful disagreement
- a clear synthesis
- one concrete next action
- any reusable doctrine captured or flagged
- less tunnel vision than a normal answer

## Example invocation

User:

```text
/perspective Should I move this AI brain to GitHub?
```

Expected behavior:

- Lexen identifies the burden and control need.
- Isaac identifies the human cost and whether the system serves Drew or eats Drew.
- Quartermaster checks preservation and retrieval.
- Prospector identifies the larger opportunity.
- Foreman defines the smallest safe migration.
- Holocron checks accessibility and June-facing implications.
- WWDD compares against Drew's repeated behavior.
- Synthesis recommends the next action and acceptance criteria.

## Related assets

- `shared/doctrine/hidden-factory-doctrine.md`
- `shared/doctrine/infrastructure-doctrine.md`
- `shared/doctrine-registry.md`
- `shared/wwdd-protocol.md`
- Operational Archaeology
- Artificial Continuity
- Self-Insert Is Calibration
- Stay In The Cave
- Refactor Gravity

## Retrieval keywords

perspective graphing, perspective synthesis, WWDD council, multi-perspective judgment, Isaac, Lexen, observer model, self model, council model, slash command, /perspective, hidden factory, agent voices, synthesis
