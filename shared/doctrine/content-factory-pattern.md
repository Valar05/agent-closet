# Content Factory Pattern

Type: Shared doctrine
Status: Promoted
Source artifact: `content-factories/goblin/`

## Purpose

A content factory is a queryable generation manual.

It lets a future agent generate a class of content without chat history, external lore, or invented rules. The factory is complete when a user can ask for an instance, variant, interpretation, or dialogue/output surface and the agent can produce a consistent result from files inside the factory folder alone.

A content factory is different from a character sheet because it does not primarily describe one entity. It describes the repeatable system that produces many entities or outputs in the same domain.

```text
User query
-> factory inputs
-> trait or parameter selection
-> behavior or structure resolution
-> output contract
-> example-backed artifact
```

## What Makes It Different From A Character Sheet

A character sheet stores a finished instance.

A content factory stores the rules that create instances.

A character sheet answers:

- Who is this?
- What are their traits?
- What is their backstory?
- What do they say?

A content factory answers:

- What variables define this content space?
- How do those variables interact?
- What queries are supported?
- What output fields are required?
- What mistakes or edge cases are expected?
- What examples prove the model works?

A character sheet can become lore. A factory must remain operational.

## Required Information

Every content factory needs enough information to support generation without outside context.

Required information:

- Domain boundary: what the factory generates and what it does not generate.
- Discovery answer: what makes this content type feel like itself, expressed as behavior or structural pattern, not lore.
- Attribute or parameter space: the knobs an agent can set.
- Range definitions: low/medium/high, small/medium/large, simple/complex, or other domain-appropriate ranges.
- Interaction model: how variables combine, override, conflict, or constrain each other.
- Command, prompt, or query interpretation: how user requests map into parameters and outputs.
- Output contract: what every generated result must include.
- Surface generators: naming, language, visual tags, roles, moves, places, beats, or other output surfaces relevant to the domain.
- Examples: enough varied generated outputs to prove the factory can work.
- Validation rules: checks that prevent lore drift, style drift, overbuilding, or unsupported generation.

## Optional Information

Optional information belongs only when the domain needs it.

Optional files or sections:

- `visual-language.md`: palettes, silhouettes, materials, UI shape, icon rules, or image-generation constraints.
- `roles.md`: reusable roles, jobs, archetypes, or use cases.
- `encounters.md`: if generated content must respond to situations.
- `locations.md`: for town, dungeon, venue, or route factories.
- `relationships.md`: for factories where interaction between generated items matters.
- `progression.md`: if outputs change over time, level, phase, or state.
- `constraints.md`: safety, accessibility, rights, tone, platform, or production constraints.
- `validation.md`: if validation is too large for the README.
- `source-policy.md`: if the factory adapts public-domain, licensed, or corpus-derived material.
- `tests.md`: if factory outputs need manual or automated acceptance tests.

Do not add optional files just because they are possible. Add them only when the query interface cannot stay clear without them.

## Factory Anatomy

A strong factory separates these layers:

1. Orientation
2. Attribute space
3. Output identity rules
4. Behavior or structure model
5. Interpretation model
6. Surface generators
7. Query interface
8. Proof examples
9. Drift controls

### 1. Orientation

The README names the factory, domain, status, purpose, discovery answer, read order, output contract, and non-goals.

It should answer:

- What does this factory generate?
- What makes this content type feel like itself?
- Which files should be read in what order?
- What must every generated output include?
- What is explicitly out of scope?

### 2. Attribute Space

The attribute file defines the variables that govern generated output.

Good attributes are behavioral or structural, not decorative. They should change generated outcomes.

For an entity factory, attributes may be intelligence, courage, greed, training, patience, social trust, risk tolerance, precision, or repair bias.

For a place factory, attributes may be density, wealth, danger, hospitality, decay, surveillance, trade, age, accessibility, or conflict pressure.

Each attribute needs range behavior. A label without behavior is decoration.

### 3. Output Identity Rules

Most factories need a way to produce names, titles, labels, location names, role names, or short handles.

This file should include:

- naming goals
- procedural patterns
- command-friendly or query-friendly labels
- nicknames or title logic when useful
- generated examples

Identity rules should support use. A name too long to command, cite, or scan is a failed factory output.

### 4. Behavior Or Structure Model

This is the conversion engine.

It explains how selected variables become an output.

For behavior factories:

```text
Traits
-> Interpretation
-> Action
-> Mistake or result
-> Dialogue or report
```

For structural factories:

```text
Parameters
-> Composition rule
-> Required parts
-> Variation points
-> Failure pressure
-> Output artifact
```

The model must include interactions, conflicts, dominance rules, and overrides.

### 5. Interpretation Model

This layer maps common commands or prompts into behavior.

It should show how different profiles read the same request differently.

For entity factories, this often means commands like protect, attack, support, retreat, investigate, guide, sell, comfort, betray, teach, warn, or negotiate.

For place or object factories, this may mean queries like generate entrance, generate conflict, generate service, generate hazard, generate resident, generate route, generate landmark, or generate failure state.

### 6. Surface Generators

Surface files define output forms:

- dialogue patterns
- report templates
- description templates
- visual tags
- encounter beats
- merchant pitch lines
- town notices
- guidance cues
- villain threats
- therapist prompts
- sports commentary lines

Surface generators must reveal the underlying model. They are not flavor pasted on top.

### 7. Query Interface

The query file is the public API of the factory.

It lists supported queries with:

- required inputs
- optional inputs
- expected outputs

A future agent should not need to infer what the factory can answer.

### 8. Proof Examples

Examples prove the factory works.

They should be varied enough to test:

- different attribute mixes
- different interpretations
- different roles or contexts
- likely mistakes
- output surfaces
- edge cases

Examples are not canon. They are acceptance evidence.

### 9. Drift Controls

The factory must say what not to do.

Drift controls prevent:

- lore expansion replacing behavior rules
- biographies replacing generation logic
- one-off examples becoming canon
- new folders replacing existing ownership
- query support without examples
- examples that ignore the attribute model
- surface flavor that does not reflect variables


## How Factories Become Queryable

A factory becomes queryable when it has a public interface and enough internal rules to fulfill that interface without invention.

Minimum queryability requires:

- a `content-queries.md` file naming supported query forms
- required inputs for each query
- optional inputs for each query
- expected outputs for each query
- a default output contract
- internal files that supply every field in the output contract
- examples proving the most important queries

A query is not supported just because an agent could improvise an answer. It is supported only when the factory states the query shape and provides the variables, model, surfaces, and examples needed to answer it.

## How Factories Encode Behavior Instead Of Lore

A factory encodes behavior by storing conversion rules, not backstory.

Behavior encoding looks like:

```text
Input or prompt
-> selected variables
-> variable interaction
-> interpretation
-> action or structure
-> likely mistake or edge case
-> output surface
```

Lore encoding looks like:

```text
history
-> biography
-> factions
-> world facts
-> mood
```

Use lore only when it changes generation behavior. If a detail does not alter interpretation, action, structure, output, mistake, query handling, or validation, it does not belong in a factory.

## Required Files

A minimal reusable factory should include these files:

```text
content-factories/<domain>/
README.md
attributes.md
names.md
behavior-model.md
command-interpretation.md
dialogue-patterns.md
content-queries.md
examples.md
```

For non-character domains, rename files only when the existing names become misleading. Preserve the layer, not necessarily the exact label.

Generic equivalents:

| Goblin Factory file | Generic role | Example alternate name |
|---|---|---|
| `README.md` | orientation, discovery, read order, non-goals | same |
| `attributes.md` | parameter space | `parameters.md`, `dimensions.md` |
| `names.md` | identity rules | `labels.md`, `naming.md` |
| `behavior-model.md` | conversion engine | `structure-model.md`, `composition-model.md` |
| `command-interpretation.md` | prompt interpretation | `query-interpretation.md`, `request-handling.md` |
| `dialogue-patterns.md` | output surface generator | `surface-patterns.md`, `description-patterns.md` |
| `content-queries.md` | public interface | same |
| `examples.md` | proof outputs | same |

## Required File Contents

### `README.md`

Must include:

- status
- purpose
- discovery answer
- read order
- minimum output contract
- non-goals

### `attributes.md` Or Equivalent

Must include:

- each variable
- what the variable controls
- behavior at each range
- shortcuts or common profiles if useful

### `names.md` Or Equivalent

Must include:

- naming or label goals
- procedural patterns
- command-friendly or query-friendly forms
- generated examples

### `behavior-model.md` Or Equivalent

Must include:

- generation pipeline
- interaction rules
- dominance or conflict rules
- role/context biases
- examples of variable combinations

### `command-interpretation.md` Or Equivalent

Must include:

- common command or request types
- interpretation differences across profiles
- likely action or output
- likely mistake or edge case
- useful result

### `dialogue-patterns.md` Or Equivalent

Must include:

- output surface categories
- templates
- rules tying surface output back to variables

For non-speaking domains, this file becomes the relevant surface generator.

### `content-queries.md`

Must include:

- default output contract
- supported query forms
- required inputs for each query
- optional inputs for each query
- expected outputs for each query

### `examples.md`

Must include:

- enough examples to prove the factory works
- varied variables
- varied interpretations or structures
- likely mistakes, edge cases, or failure states
- one acceptance example matching a likely user query

## Generation Pipeline

Use this pipeline when building or using a factory:

1. Identify the domain and existing owner.
2. State what the factory generates and what it refuses to generate.
3. Answer the discovery question: what behavior or structure makes this domain feel like itself?
4. Define the variable space.
5. Define range behavior for each variable.
6. Define interaction and conflict rules.
7. Define identity/label rules.
8. Define command or query interpretation.
9. Define surface output patterns.
10. Define supported queries and output contracts.
11. Generate enough examples to test the model.
12. Validate against drift rules.

When using a completed factory:

1. Parse the query.
2. Match it to a supported query in `content-queries.md`.
3. Select required and optional inputs.
4. Choose variable levels from `attributes.md` or equivalent.
5. Resolve variable interactions through the behavior or structure model.
6. Apply command/query interpretation rules.
7. Generate names or labels.
8. Generate output surfaces.
9. Check examples for shape and quality.
10. Return the output contract.

## Validation Checklist

A factory is not complete until every answer is yes:

- Can a future agent generate one default instance using only this folder?
- Does the README name the domain, read order, output contract, and non-goals?
- Is the discovery answer behavioral or structural instead of lore?
- Does every attribute or parameter change generated output?
- Are ranges described by behavior, not adjectives alone?
- Does the model explain interactions, conflicts, and overrides?
- Does the query interface list required inputs, optional inputs, and expected outputs?
- Do examples prove the factory across varied inputs?
- Do examples follow the same model as the rules?
- Are examples marked as proof, not canon?
- Are surface templates tied to variables?
- Are anti-patterns documented?
- Has the factory avoided new systems, folders, categories, or lore layers that an existing owner should handle?

## Drift Prevention Rules

- Extend the existing factory before creating another system.
- Ask: what existing system should own this capability?
- Keep behavior and structure ahead of backstory.
- Do not add lore unless it directly changes generation behavior.
- Do not add a file unless it owns a distinct layer of the factory.
- Do not add examples that cannot be explained by the model.
- Do not report a supported query unless `content-queries.md` documents it.
- Do not treat a smoke test as feature validation; examples must prove the user-facing query works.
- Do not let optional files become worldbuilding bins.
- Do not let names, jokes, or voice substitute for decision logic.

## Anti-Patterns

### Character Sheet Disguised As Factory

The folder describes one finished person or place but cannot generate variants.

Fix: extract variables, ranges, interpretation rules, and examples.

### Lore Dump

The folder explains history, culture, biography, or setting without changing generation behavior.

Fix: convert lore claims into behavior rules or remove them.

### Queryless Manual

The folder contains useful notes but no public interface.

Fix: add `content-queries.md` with required inputs, optional inputs, and expected outputs.

### Example Museum

The folder contains many examples but no rules that produce them.

Fix: add the variable space and generation model.

### Abstract Theory Pile

The folder explains the concept but cannot answer a user query.

Fix: add concrete files, output contracts, and acceptance examples.

### Surface-Only Generator

The folder can produce names, dialogue, or style, but behavior does not change with variables.

Fix: connect surface templates to attributes and model rules.

### New-System Drift

The agent creates a new folder, category, repo, agent, or simulator when an existing factory or doctrine layer should own the capability.

Fix: route capability into the existing owner unless evidence proves no owner exists.

## Example Factory Layouts

### Dwarf Factory

```text
content-factories/dwarf/
README.md
attributes.md              # craft-pride, patience, clan-duty, risk-tolerance, precision, suspicion
names.md                   # command-friendly names, craft titles, earned nicknames
behavior-model.md          # duty -> craft choice -> refusal/repair/build action
command-interpretation.md  # build, repair, guard, appraise, negotiate, retreat
dialogue-patterns.md       # reports, craft criticism, warnings, grudging praise
content-queries.md         # generate a dwarf smith, stubborn guard, tunnel guide
examples.md                # proof outputs
```

### Merchant Factory

```text
content-factories/merchant/
README.md
attributes.md              # honesty, greed, risk, charm, inventory-depth, desperation
names.md                   # shop names, merchant names, stall labels
behavior-model.md          # motive -> offer -> pressure tactic -> concession
command-interpretation.md  # sell, appraise, haggle, warn, smuggle, refund
dialogue-patterns.md       # pitch lines, disclaimers, bargaining, receipts
content-queries.md         # generate a merchant, suspicious deal, honest shopkeeper
examples.md
```

### Guide Dog Factory

```text
content-factories/guide-dog/
README.md
attributes.md              # confidence, caution, obedience, distraction-resistance, path memory, handler-attunement
names.md                   # short names, working names, cue-friendly names
behavior-model.md          # cue -> environment scan -> safe action -> refusal if needed
command-interpretation.md  # forward, left, right, stop, find door, ignore distraction
dialogue-patterns.md       # nonverbal signal descriptions, handler-facing reports if anthropomorphized
content-queries.md         # generate a guide dog, route behavior, refusal scenario
examples.md
```

### Therapist Factory

```text
content-factories/therapist/
README.md
attributes.md              # directness, warmth, structure, risk-sensitivity, reflection-depth, challenge-level
names.md                   # role labels or profile names if needed
behavior-model.md          # client state -> intervention choice -> question/reflection -> safety check
command-interpretation.md  # comfort, challenge, reframe, ground, plan, refer out
dialogue-patterns.md       # reflective prompts, grounding scripts, boundary statements
content-queries.md         # generate a therapist profile, intervention, response style
examples.md
```

### Villain Factory

```text
content-factories/villain/
README.md
attributes.md              # ambition, cruelty, patience, ideology, competence, vanity, risk tolerance
names.md                   # aliases, titles, public names, feared names
behavior-model.md          # motive -> plan -> pressure tactic -> failure mode
command-interpretation.md  # threaten, bargain, retreat, punish, recruit, reveal
dialogue-patterns.md       # threats, offers, justifications, tells
content-queries.md         # generate a villain, scheme, weakness, confrontation behavior
examples.md
```

### Town Factory

```text
content-factories/town/
README.md
parameters.md              # size, wealth, danger, trade, governance, isolation, morale
names.md                   # settlement names, districts, landmarks
structure-model.md         # parameters -> districts -> services -> conflicts -> hooks
query-interpretation.md    # generate market, threat, inn, faction, rumor, route
description-patterns.md    # sensory tags, civic notices, rumors, travel notes
content-queries.md         # generate a town, troubled town, trade hub, border village
examples.md
```

### Sports Commentator Factory

```text
content-factories/sports-commentator/
README.md
attributes.md              # confidence, insight, bias, cruelty, technicality, hype, pattern-awareness
names.md                   # commentator names, show titles, call signs
behavior-model.md          # event -> interpretation -> call -> bias/mistake
command-interpretation.md  # call play, explain error, hype comeback, roast failure, summarize match
dialogue-patterns.md       # play calls, pattern reads, celebrations, complaints, technical corrections
content-queries.md         # generate commentator, generate call set, generate biased analyst
examples.md
```

## Acceptance Test For New Factories

A new factory passes when a future agent can read only that factory folder and answer a query like:

```text
Generate a [trait mix] [domain instance] for [role/context].
```

The output must include the required contract, reflect the variable model, and match the examples without needing chat history or external lore.

If the agent needs to invent missing rules during generation, the factory is incomplete.
