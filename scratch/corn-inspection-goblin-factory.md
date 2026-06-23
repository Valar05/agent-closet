# Corn Inspection: Goblin Factory

Artifact inspected: `038dfa1 Complete goblin content factory`

## 60-Second Answer

This commit turned `content-factories/goblin/` from a stub into a queryable generation manual.

Before the commit, the folder could only say that a goblin factory should exist. It had a purpose line, a TODO list, and an unfinished attribute stub.

After the commit, an agent can generate goblins on demand with:

- names and titles
- trait levels
- dominant decision patterns
- command interpretations
- likely mistakes
- dialogue lines
- proof examples

The corn is real: the folder now supports concrete queries such as `Generate a goblin`, `Generate a goblin knight`, `Generate a smart coward`, `Generate a goblin who misreads protect`, `Generate a goblin sports commentator`, `Generate a goblin likely to create collateral damage`, `Generate a smart but cowardly goblin knight`, `Interpret command for goblin`, and `Generate goblin dialogue`.

## Capability Gain

### What changed from before

Before `038dfa1`, the folder contained:

- `README.md`: name, active status, and purpose only.
- `TODO.md`: a list saying the folder still needed attribute, name, behavior, command, dialogue, and example rules.
- `attributes.md`: one sentence plus `TODO: expand the slider list with ranges and interaction notes.`

After `038dfa1`, the folder contains a working set of generation files:

- `README.md`: discovery answer, read order, minimum output contract, and non-goals.
- `attributes.md`: ten behavior sliders with low/medium/high behavior.
- `names.md`: naming rules, title rules, command-friendly names, 50 generated names, and 20 title examples.
- `behavior-model.md`: trait-to-interpretation-to-action pipeline, dominance rules, conflict examples, and role biases.
- `command-interpretation.md`: command interpretation tables for protect, attack, hold, scout, support, retreat, and investigate across five goblin profiles.
- `dialogue-patterns.md`: speech templates for reporting, complaining, celebrating, misunderstanding, technical correctness, and Gasket-style observations.
- `content-queries.md`: supported query forms with required inputs, optional inputs, and expected outputs.
- `examples.md`: 20 generated goblins plus an acceptance example.

### What an agent can do now

An agent can now answer user requests that require generated goblin content without chat history or external lore.

New capabilities:

- Generate a default goblin.
- Generate role-specific goblins such as a knight, scout, sports commentator, or damage-prone helper.
- Generate named goblins with command-friendly names and titles.
- Assign trait levels and explain how those traits alter behavior.
- Predict how a goblin interprets commands.
- Predict likely mistakes.
- Produce short dialogue lines that reflect the trait model.
- Use examples as proof of output shape.

## Exact Queries Now Answerable

From `content-queries.md`, the exact supported query families are:

1. `Generate a goblin.`
2. `Generate a goblin knight.`
3. `Generate a smart coward.`
4. `Generate a goblin who misreads protect.`
5. `Generate a goblin sports commentator.`
6. `Generate a goblin likely to create collateral damage.`
7. `Generate a smart but cowardly goblin knight.`
8. `Interpret command for goblin.`
9. `Generate goblin dialogue.`

Each query has required inputs, optional inputs, and expected outputs documented in the folder.

## Outputs Now Generatable

The commit makes these output types available:

- Command-friendly names.
- Nicknames and titles.
- Trait blocks using intelligence, courage, kindness, greed, obedience, curiosity, literalness, self-preservation, confidence, and problem-bias.
- Profile shortcuts such as smart coward, brave fool, kind literalist, greedy opportunist, paranoid goblin, collateral damage goblin, and sports commentator goblin.
- Dominant decision pattern.
- Likely command interpretation.
- Likely action.
- Likely mistake.
- Useful result.
- Dialogue lines by category.
- Complete generated goblin examples.

The default generated goblin contract is:

- name
- role or use case
- traits
- dominant decision pattern
- likely interpretations
- likely mistakes
- likely dialogue

## Behavior That Became More Consistent

The strongest consistency gain is command interpretation.

Before the commit, a future agent would have to invent how goblins read commands. After the commit, the folder gives repeated mappings:

- traits -> interpretation -> action -> mistake/result -> dialogue
- high literalness changes abstract commands into physical actions
- high greed redirects commands toward profit
- high self-preservation redirects commands toward safety
- high courage redirects commands toward contact
- high curiosity redirects commands toward testing
- high confidence locks in first interpretations
- high kindness redirects commands toward visible rescue
- high problem-bias redirects ambiguity toward force, theft, traps, shouting, testing, or destruction

Command behavior is now consistent across seven verbs:

- protect
- attack
- hold
- scout
- support
- retreat
- investigate

The examples also make consistency checkable: each generated goblin includes traits, likely interpretations, likely mistakes, and likely dialogue.

## Decorative Material

Low-decorative, useful material:

- Names are not merely flavor because they are command-friendly and support generated output.
- Dialogue is not merely flavor because templates reveal interpretation, mistake, or trait bias.
- Titles are not merely flavor when they encode repeated behavior or role.

Actually decorative or near-decorative material:

- Some individual example names are interchangeable once they satisfy command-friendly naming.
- Some dialogue lines are illustrative rather than structurally necessary.
- The Gasket-style observation category is useful for sports-commentator queries but decorative for ordinary goblin generation.

No large lore block appears in the commit. That is a positive signal: most content is operational rather than decorative.

## Reusable Components

Reusable inside future goblin generation:

- Attribute slider format.
- Attribute shortcut profiles.
- Trait interaction steps.
- Dominance rules.
- Command interpretation tables.
- Command modifiers.
- Dialogue template categories.
- Default output contract.
- Query contract format: required inputs, optional inputs, expected outputs.
- Example format.

Reusable outside goblin generation:

- Queryable folder shape.
- Behavior-first discovery answer.
- Range-based attribute model.
- Conversion pipeline from variables to interpretation to output.
- Acceptance example pattern.
- Separation between examples and canon.

## Evidence of Broader Pattern

The commit shows that a content factory becomes useful when it contains these layers:

1. Orientation: what the factory generates and refuses.
2. Attribute space: variables with behavior ranges.
3. Identity rules: names, titles, labels, or handles.
4. Behavior model: how variables interact.
5. Interpretation model: how commands or queries are read.
6. Surface templates: dialogue or other output forms.
7. Query interface: supported prompts and output contracts.
8. Proof examples: generated outputs that demonstrate the factory.

This is larger than goblins. The same skeleton could support another content domain because it describes generation mechanics instead of goblin lore.

## Accidental Complexity

Possible accidental complexity in the commit:

- `TODO.md` remains as a status file after completion. It is harmless, but it is no longer part of the generation path.
- The folder has both role biases in `behavior-model.md` and role-specific queries in `content-queries.md`; this is useful now but could duplicate if expanded carelessly.
- The sports-commentator/Gasket-style material is a specialized branch inside a general goblin factory. It is justified by requested queries, but it is not core to every goblin.
- `examples.md` is large compared with the rule files. The examples prove capability, but future readers should treat them as evidence patterns, not canon.

## Open Questions

- Is the factory intended to be used only for text generation, or should later agents treat it as source for game data too?
- Should command verbs beyond protect, attack, hold, scout, support, retreat, and investigate be added only when a real query requires them?
- Should non-speaking goblin outputs use `dialogue-patterns.md` as behavior evidence, or should they omit dialogue when the query does not ask for speech?
- Should Gasket-style observations remain a goblin-specific branch or move only if another factory needs sports-commentator behavior?

## Promotion Candidates

These are observed reusable pieces, not improvement proposals:

- Query contract shape: required inputs, optional inputs, expected outputs.
- Minimum output contract: name, role/use case, traits, decision pattern, interpretations, mistakes, dialogue.
- Behavior-first discovery answer: define the content type by what it does under pressure, not by lore.
- Conversion pipeline: traits -> interpretation -> action -> mistake/result -> dialogue.
- Examples as proof, not canon.
- Drift rule: if a future agent needs chat history or external lore, the factory is incomplete.

## Verdict

There is corn in the bucket.

The commit created actual capability. It did not only add prose. The decisive evidence is that an agent can now answer concrete generation queries from `content-factories/goblin/` alone and can produce structured outputs that were impossible from the previous stub files.
