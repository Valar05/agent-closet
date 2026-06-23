# Goblin Command Interpretation

This is the main factory file for turning commands into goblin behavior.

Use it after selecting traits from `attributes.md` and resolving dominance in `behavior-model.md`.

## Command Output Shape

For each command, produce:

- likely interpretation
- likely action
- likely mistake
- useful result
- dialogue pattern

## Profiles Used In Examples

- Smart coward: high intelligence, low courage, high self-preservation.
- Brave fool: low intelligence, high courage, low self-preservation.
- Kind literalist: high kindness, high literalness, medium obedience.
- Greedy opportunist: high greed, medium intelligence, low or medium obedience.
- Paranoid goblin: high self-preservation, medium intelligence, low confidence or high curiosity.

## Protect

| Profile | Interpretation | Action | Likely mistake | Useful result |
| --- | --- | --- | --- | --- |
| Smart coward | Reduce danger while staying alive. | Builds cover, redirects threats, uses alarms. | May protect from too far away. | Target survives with minimal direct risk. |
| Brave fool | Put body between target and danger. | Charges nearest threat or becomes shield. | Blocks target movement or spell lines. | Stops obvious attacks fast. |
| Kind literalist | Prevent any harm to named target. | Wraps, carries, hides, or restrains target. | Protects target from their own task. | Good emergency bodyguard if given exact boundaries. |
| Greedy opportunist | Target is valuable property. | Moves target to a secure place and negotiates fee. | Kidnaps the protected target for safekeeping. | Good at guarding assets. |
| Paranoid goblin | Everyone is a possible threat. | Creates perimeter, checks exits, over-reports movement. | Treats allies as suspicious. | Spots ambushes early. |

## Attack

| Profile | Interpretation | Action | Likely mistake | Useful result |
| --- | --- | --- | --- | --- |
| Smart coward | Damage enemy without exposure. | Uses traps, thrown objects, doors, or other fighters. | May delay until advantage is perfect. | Efficient low-risk pressure. |
| Brave fool | Run at enemy now. | Charges, bites, tackles, swings. | Attacks wrong target if pointed poorly. | Disrupts enemy quickly. |
| Kind literalist | Stop target from hurting others. | Disarms, trips, pins, or apologizes while hitting. | Pulls blows against dangerous target. | Good nonlethal control. |
| Greedy opportunist | Enemy owns loot and therefore is objective. | Attacks pockets, weapon hand, pack, trophy items. | Prioritizes loot over victory. | Can disarm or distract well. |
| Paranoid goblin | Strike before being struck. | Attacks suspicious motion or hidden angles. | Starts fights unnecessarily. | Hard to ambush. |

## Hold

| Profile | Interpretation | Action | Likely mistake | Useful result |
| --- | --- | --- | --- | --- |
| Smart coward | Maintain position without dying. | Fortifies, creates fallback lines, uses signals. | Calls withdrawal a flexible hold. | Strong defensive planning. |
| Brave fool | Do not move. | Plants feet, blocks path, grabs object. | Refuses to dodge hazards. | Physically reliable under simple orders. |
| Kind literalist | Hold the named thing. | Grips bridge, door, person, or banner. | Holds the object instead of controlling area. | Good if target is concrete. |
| Greedy opportunist | Control access. | Charges toll, sells passage, marks ownership. | Lets paying enemies through. | Creates chokepoint leverage. |
| Paranoid goblin | Hold until trap is proven absent. | Watches every angle, lays markers, blocks everyone. | Stops allies from passing. | Good at preventing surprise movement. |

## Scout

| Profile | Interpretation | Action | Likely mistake | Useful result |
| --- | --- | --- | --- | --- |
| Smart coward | Learn without being seen. | Uses distance, cover, counting, maps. | May return before seeing enough. | Good risk report. |
| Brave fool | Go ahead first. | Runs forward and triggers contact. | Becomes the alarm. | Finds danger immediately. |
| Kind literalist | Look ahead and report exactly. | Counts visible objects and beings. | Misses meaning behind details. | Accurate raw observations. |
| Greedy opportunist | Find safe path and valuables. | Scouts treasure, exits, weak locks. | Reports loot before enemies. | Useful asset discovery. |
| Paranoid goblin | Prove the path is dangerous. | Checks shadows, tracks, smells, ceiling, floor. | Over-reports harmless signs. | Good trap suspicion. |

## Support

| Profile | Interpretation | Action | Likely mistake | Useful result |
| --- | --- | --- | --- | --- |
| Smart coward | Help from safer position. | Carries supplies, reloads, signals, patches plans. | Avoids front-line support. | Reliable backline help. |
| Brave fool | Help by joining the biggest action. | Piles into fight, blocks, shouts. | Crowds allies. | Adds pressure and morale. |
| Kind literalist | Physically support whoever looks strained. | Holds people up, carries gear, props doors. | Props the wrong thing. | Good rescue assistance. |
| Greedy opportunist | Help where credit is visible. | Supports leader, witness, or reward source. | Ignores unglamorous tasks. | Useful when incentives are explicit. |
| Paranoid goblin | Prevent support from becoming trap. | Checks supplies, watches flanks, distrusts gifts. | Slows the team. | Finds sabotage. |

## Retreat

| Profile | Interpretation | Action | Likely mistake | Useful result |
| --- | --- | --- | --- | --- |
| Smart coward | Leave safely with information. | Covers tracks, uses smoke, counts survivors. | May retreat too early. | Best at surviving with useful data. |
| Brave fool | Move backward angrily. | Backs away while fighting. | Turns retreat into second attack. | Can delay pursuit. |
| Kind literalist | Bring everyone back. | Drags allies, pets, captives, and maybe furniture. | Overloads retreat with rescues. | High survivor recovery. |
| Greedy opportunist | Leave with valuables. | Grabs portable loot and exits. | Slows escape for loot. | Recovers useful objects. |
| Paranoid goblin | Execute preplanned escape. | Uses hidden route, decoys, false trail. | Leaves before order completes. | Strong ambush avoidance. |

## Investigate

| Profile | Interpretation | Action | Likely mistake | Useful result |
| --- | --- | --- | --- | --- |
| Smart coward | Learn cause without touching hazard. | Observes, tests with tools, asks witnesses. | May avoid the decisive test. | Good diagnosis. |
| Brave fool | Find out by direct contact. | Opens, shakes, kicks, presses, tastes. | Activates danger. | Fast information, if anyone survives. |
| Kind literalist | Examine exactly what was named. | Inspects target and reports visible state. | Ignores related context. | Clean narrow report. |
| Greedy opportunist | Determine value and owner. | Appraises, pockets samples, searches compartments. | Contaminates evidence. | Finds hidden assets. |
| Paranoid goblin | Identify how it will kill us. | Tests exits, fumes, symbols, tracks, hidden watchers. | Concludes too many threats. | Good threat model. |

## Command Modifiers

Add modifiers when user query includes them:

- `quietly`: reduces confidence display, not necessarily competence.
- `without damage`: lowers problem-bias action; if problem-bias remains high, the goblin uses traps, padding, or theft.
- `fast`: increases mistakes unless intelligence is high.
- `carefully`: increases self-preservation and observation.
- `for pay`: increases obedience for greedy goblins.
- `for friend`: increases kindness and courage.
- `do not touch`: blocks brave fool and curious action only if obedience is medium or high.

## Acceptance Test Pattern

Query:

```text
Generate a smart but cowardly goblin knight.
```

Expected response shape:

- Name from `names.md`.
- Traits: high intelligence, low courage, medium or high obedience, high self-preservation, role knight.
- Likely interpretations: protects by fortifying, attacks from cover, holds with fallback lines, retreats with map.
- Likely mistakes: under-commits, calls retreat tactical, overbuilds cover.
- Dialogue: report plus complaint plus technical correctness.
