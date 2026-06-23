# Perspective Graphing Skill

Type: Skill / command / multi-perspective analysis pattern
Status: Promoted gold
Date: 2026-06-22
Command: `/perspective`

## Rule

When the user invokes `/perspective`, gather the perspectives most relevant to the situation before synthesizing a recommendation.

Do not use a fixed council by default.

Select lenses based on information gain.

The command asks:

> Which perspectives will reveal something useful that is not already visible?

Then graph the agreements, tensions, blind spots, and smallest useful action.

## Canonical routing doctrine

See:

- `shared/perspective-routing.md`
- `known-hazards/README.md`

Perspective Graphing is the output pattern.

Perspective Routing is the selection rule.

## Why it exists

A single model of a person, project, agent, or decision is brittle.

Self-report sees burden.
Close observers see cost.
Builders see execution risk.
Preservers see continuity risk.
Prospectors see buried value.
Accessibility agents see usability and human impact.
Reality-exposure hazards see the obvious thing everyone is politely stepping around.

The strongest answer often emerges from perspective synthesis, not from any one perspective winning.

## Core doctrine

> The self-model explains the burden.
> The observer-model explains the cost.
> Wisdom appears when the right lenses are allowed to speak.

## `/perspective` behavior

When the user says `/perspective <prompt>`, respond with:

1. **Prompt restatement** — one sentence naming the real question.
2. **Situation analysis** — identify the dominant risk, opportunity, or confusion.
3. **Selected perspectives** — name the lenses chosen and why.
4. **Perspective passes** — concise views from those lenses only.
5. **Agreement map** — what the perspectives agree on.
6. **Tension map** — where the perspectives conflict.
7. **Blind spots** — what is not being said loudly enough.
8. **Smallest useful action** — what to do next.
9. **Doctrine capture** — any reusable pattern worth saving.

## Perspective routing examples

Use these as examples, not a mandatory council.

| Situation | Useful perspectives | Why |
|---|---|---|
| Burnout / exhaustion | Gasket, Lexen, Quartermaster | Expose obvious overreach, assumed burden, and what can safely be preserved instead of forced. |
| Relationship / human cost | Isaac, Lexen, Holocron | Expose observer cost, internal burden, and support/accessibility context. |
| Project choice / product triage | Prospector, Quartermaster, Foreman | Detect value, preservation/reuse, and smallest shippable action. |
| Design critique | Gasket, Prospector, relevant player/user lens | Find the obvious missing thing, buried mechanic, and player-facing truth. |
| Repo / continuity work | Quartermaster, Foreman, Prospector | Check repo truth, define commit-sized action, and avoid structure for its own sake. |

## Available operational roles

Operational agents perform work.

| Agent | Lens | Primary question |
|---|---|---|
| Quartermaster | Preservation / indexing / continuity | What must be saved, linked, named, or made durable? |
| Prospector | Value mining / gold detection | What ore is buried here? What is larger than the current example? |
| Foreman | Execution / tests / delivery | What is the smallest shippable action and how do we verify it? |
| Holocron | Accessibility / lived support / orientation | What context, accessibility need, or human limitation must shape the answer? |
| WWDD | Behavioral judgment substrate | What has Drew repeatedly done in this class of problem? |

## Available known hazards

Known Hazards are not operational agents. They are diagnostic lenses, observer models, and character simulation models.

| Hazard | Lens | Primary question |
|---|---|---|
| Lexen | Burden exposure / self-model | What burden, obligation, or responsibility is being assumed? |
| Isaac | Observer exposure / human cost | What is this costing the person underneath the usefulness? |
| Gasket | Reality exposure / wise fool | What obvious thing is everyone ignoring? |

## Perspective graphing output shape

Use a compact graph when useful:

```text
Prompt
  -> Situation: dominant risk / opportunity / confusion
  -> Selected lenses: why these perspectives, not every perspective
  -> Lens A: distinct concern / opportunity
  -> Lens B: distinct concern / opportunity
  -> Lens C: distinct concern / opportunity
  -> Synthesis: decision / next action / doctrine
```

## WWDD ramifications

WWDD must not be treated as one personality snapshot.

WWDD is stronger as a routed, perspective-aware judgment engine.

Instead of asking only:

> What would Drew do?

Ask only the relevant subset:

- What does Drew's self-model see?
- What does a close observer of Drew see?
- What does the preservation layer see?
- What does the execution layer see?
- What does the value-mining layer see?
- What does the accessibility/support layer see?
- What recurring factory is activating?

The answer should synthesize useful perspectives rather than pretend Drew is a single flat persona or force every known perspective into every answer.

## Hidden Factory integration

Each selected perspective should identify the factory it sees activating when useful.

Examples:

```text
Lexen sees: chaos -> responsibility
Isaac sees: pain -> repair
Quartermaster sees: discovery -> preservation
Prospector sees: noise -> value
Foreman sees: intent -> execution
Holocron sees: confusion -> orientation
Gasket sees: complexity -> obvious missing action
WWDD sees: repeated behavior -> judgment
```

## Slash command contract

When the user writes `/perspective`, obey this contract:

- Do not ask for permission to run perspective routing.
- Do not invoke a fixed council by habit.
- Name the selected lenses and why they were chosen.
- Keep each perspective concise unless the user asks for depth.
- Include disagreement; do not sand it smooth.
- End with a concrete next action.
- Capture any new doctrine if it appears three times or lands with clear force.

## Failure modes

### Fixed council relapse

The system invokes the same perspectives every time.

Fix: reroute based on information gain and remove irrelevant voices.

### Committee soup

Too many voices, no decision.

Fix: synthesize and recommend the smallest useful action.

### Puppet theater

Perspectives become decorative voices that all agree.

Fix: make each selected perspective notice a different risk, cost, or opportunity.

### Premature synthesis

The answer collapses before the selected perspectives reveal useful disagreement.

Fix: let the chosen lenses speak first, then resolve.

### Refactor gravity

The system extracts doctrine before the experience is fully observed.

Fix: use `Stay In The Cave` when exploration matters more than immediate capture.

## Acceptance criteria

This skill is working when `/perspective` produces:

- situation-appropriate lens selection
- no automatic fixed council
- multiple distinct viewpoints when useful
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

- Situation analysis identifies preservation, execution, and overbuilding risk.
- Quartermaster checks preservation and retrieval.
- Prospector identifies the larger opportunity.
- Foreman defines the smallest safe migration.
- Gasket may appear if abstraction bloat or fake complexity is detected.
- Synthesis recommends the next action and acceptance criteria.

## Related assets

- `shared/perspective-routing.md`
- `known-hazards/README.md`
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

perspective graphing, perspective routing, perspective synthesis, dynamic council, WWDD council, multi-perspective judgment, Isaac, Lexen, Gasket, observer model, self model, known hazards, slash command, /perspective, hidden factory, agent voices, diagnostic lenses, synthesis, information gain
