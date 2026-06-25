# Scene Compiler Runtime Dogfood Pass

Status: executed
Runtime: `skills/scene-compiler-runtime.md`
Harness: `skills/scene-compiler-tests.md`
Doctrine source: `corpus/fiction/candidate-writing-doctrines.md`
Pressure source: `skills/world-pressure-engine.md`

## Minimal Scenario

A damaged shelter is losing heat while a storm approaches. The protagonist is exhausted. A frightened companion is inside the shelter. Repair materials are limited.

## 1. Initial Runtime State

### World State

- Location: a half-collapsed shelter at the edge of open ground.
- Active facts: wind is rising; one wall is leaking heat; tools are present but scattered.
- Available resources: tarp, rope, a small hammer, salvage boards, one blanket, one lamp.
- Institutional status: none active.
- Unresolved promises: the shelter still has to survive the night.
- Scene history: the shelter was already weakened before the storm notice.
- World changes that must persist: the shelter is damaged and the storm is still coming.

### Character State

- Protagonist: exhausted, cold, competent enough to patch structures but not enough to waste motion.
- Capabilities: can repair, brace, and improvise; low energy.
- Current role: the only person likely to make the shelter survivable.
- What they know: the shelter will fail if they do nothing.
- What they owe: safety for the companion and the shelter.
- What they refuse: panic and decorative heroics.

### Relationship State

- Companion trusts the protagonist enough to stay, but is frightened and looking for reassurance.
- Dependence: the companion cannot repair the shelter alone.
- Repair evidence: none yet in this scene, only the opportunity to earn it.

### Pressure State

- Category: physical + logistical.
- Urgency: immediate, because heat loss will become exposure before the storm peaks.
- Consequence debt: the shelter's damage has already reduced safety; delay makes the loss worse.
- Why now: the temperature is dropping and the wind is increasing.
- Who must decide: the exhausted protagonist.
- What gets worse if ignored: hypothermia, collapse, and companion panic.

### Unresolved Promises

- Keep the shelter warm enough to survive the night.
- Keep the frightened companion from spiraling.
- Preserve the shelter as a usable refuge, not a dramatic ruin.

## 2. Pressure Selection

Selected pressure: the shelter's heat leak must be repaired before the storm takes the room.

Why this pressure is inevitable:

- The weather is already changing.
- Heat loss is ongoing.
- Exhaustion makes delay more dangerous, not less.
- The shelter cannot self-repair.

Why it beats alternatives:

- Relational pressure is secondary; the companion's fear matters, but it is driven by the shelter failure.
- Institutional pressure is absent.
- Informational pressure is already known; the problem is not uncertainty but action.
- Moral pressure exists, but it is expressed through the repair decision.

## 3. Doctrine Selection

Selected doctrine: `Make Repair the Dramatic Act`

Why this is the smallest sufficient doctrine set:

- The scene's core problem is functional failure, not relationship repair or power progression.
- Repair alone can force a visible, testable scene.
- The doctrine's pass condition is straightforward: the decisive action must be repair, calibration, feeding, shielding, or stabilization.

Support doctrine: none.

## 4. Scene Generation

### Scene Draft

Wind pushed through the split seam above the bedroll, thin and cold enough to make the lamp tremble.

The companion had wrapped both arms around the blanket and was trying not to look at the hole in the wall.

The protagonist knelt beside the broken brace, checked the board by touch, and found the grain split farther than it looked.

“Give me the tarp,” they said.

The companion handed it over with shaking hands.

The protagonist did not try to comfort them with promises. They threaded rope through the tarp, lashed it to the surviving studs, and used the hammer to drive a salvage board against the seam until the wall stopped breathing with the wind.

The cold did not vanish. It thinned.

The lamp steadied.

The companion stopped hugging the blanket long enough to hold the board in place while the protagonist tied the last knot.

When the final brace went in, the shelter changed from a wound into a patch.

Not safe. Usable.

The protagonist sat back on their heels, breathing hard, and finally took the blanket for themselves long enough to share it properly.

## 5. Harness Validation

### Doctrine: Make Repair the Dramatic Act

Pass/fail: Pass

Observable evidence:

- The decisive action is repairing and stabilizing the shelter.
- The scene focuses on tarp, rope, board, hammer, and brace work.
- The repair changes the state of the shelter from leaking to usable.

Missing behavior:

- None required for the selected doctrine.

## 6. Repair Pass

No repair pass required.

The first draft already satisfied the selected doctrine and produced a real state change.

## 7. Acceptance

Accepted.

### State Delta

- Shelter: from leaking heat to patched and usable.
- Protagonist: from exhausted but idle to exhausted but effective.
- Companion: from frightened and passive to frightened but participating.
- Relationship: from dependence without proof to shared maintenance.
- World state: the shelter remains damaged, but it now persists through the storm.

### Next Pressure

- The patched wall may hold, but the storm will test the repair.
- The companion has seen the protagonist's competence under strain and may now expect leadership for the rest of the night.
- Exhaustion remains, so rest or food becomes the next meaningful transition.

### Remaining Consequence Debt

- The shelter is still damaged and will need later repair.
- The protagonist is still exhausted.
- The companion's fear has not disappeared; it has only been routed into action.

## 8. Final Assessment

### What felt mechanical?

- Pressure selection was the most mechanical part in a good way: the damage-to-weather-to-exhaustion chain made the next pressure obvious.
- Doctrine selection was straightforward because the scene was a pure repair problem.

### What information was missing?

- Nothing critical for this minimal case.
- If the scene had needed a more complex institutional or relational choice, I would have wanted a more explicit world-state ledger.

### Which runtime step created the most leverage?

- Pressure selection.
- Choosing the leak-before-storm pressure made every later decision converge on one visible action.

### Which step needs redesign?

- Doctrine combination policy.
- The runtime is clear for single-doctrine scenes, but more complex scenes may need a better rule for when to pair a secondary doctrine without overfitting the scene.

### Which parts could become executable software instead of documentation?

- The runtime state object.
- Pressure selection scoring.
- Doctrine selection by observable pass condition.
- Harness validation and retry tracking.
- Acceptance gating based on state delta and explicit next pressure.
