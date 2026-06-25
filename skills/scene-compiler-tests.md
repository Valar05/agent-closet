# Scene Compiler Test Harness

Status: active test harness / doctrine-to-scene validation
Role: turn fiction doctrines into executable scene tests
Source basis: `corpus/fiction/candidate-writing-doctrines.md`, `skills/scene-compiler.md`, and the fiction corpus observation layer

## Purpose

This file does not add new doctrine.

It turns the existing candidate doctrines into scene-level capability tests so future scene generation can be judged on behavior, not vibe.

Test rule:

```text
Doctrine -> Scene input -> Required pressure -> Doctrine applied -> Generated scene behavior -> Pass/fail test
```

## 1. Route Responsibility Through a Person

Scene input:
A group is stalled because no one will take responsibility for the next move.

Required pressure:
The delay must threaten safety, timing, or access to a needed resource.

Doctrine applied:
The protagonist becomes the routing point for judgment, coordination, or triage.

Generated scene behavior:
Other characters begin deferring to the protagonist because they have already proven reliable under pressure. The scene should show the protagonist absorbing the burden of choice, not merely standing in the center of attention.

Pass/fail test:
- Pass: the scene's decisive action is the protagonist routing work, safety, or information.
- Fail: the scene treats the protagonist as important without making them structurally necessary.

## 2. Make Repair the Dramatic Act

Scene input:
A damaged shelter, tool, body, or machine is losing function.

Required pressure:
The damage must create an immediate cost if not repaired now.

Doctrine applied:
Repair, feeding, calibration, stabilization, or debugging becomes the decisive action.

Generated scene behavior:
The scene should focus on fixing, patching, or maintaining the thing that keeps people alive. If violence appears, it should support the repair rather than replace it.

Pass/fail test:
- Pass: the decisive beat is repair or maintenance, and the repair changes the state of the scene.
- Fail: the scene treats maintenance as background texture or replaces it with combat/exposition.

## 3. Teach Systems by Contact

Scene input:
A character encounters a new artifact, interface, ritual, or machine under pressure.

Required pressure:
The character must act before they fully understand the system.

Doctrine applied:
The scene teaches the system through use, failure, or interaction before explanation.

Generated scene behavior:
The character touches, tests, wears, breaks, or tries the system. The rules become legible because of what happens, not because a manual appears.

Pass/fail test:
- Pass: the character learns the rule by using the system and the consequence clarifies behavior.
- Fail: the scene explains the system first and uses it second.

## 4. Use Food and Rest as Plot Transitions

Scene input:
The characters have just survived danger, strain, or institutional pressure.

Required pressure:
The body must be visibly changed by the last scene and need recovery.

Doctrine applied:
Meals, drink, sleep, or deliberate rest close one pressure state and open another.

Generated scene behavior:
The scene should mark recovery as a real state change. Food or rest should not just decorate the setting; it should end one mode of action and begin a new one.

Pass/fail test:
- Pass: eating, drinking, or sleeping changes readiness, trust, or available options.
- Fail: food or rest is used only for atmosphere or filler.

## 5. Let Relationships Start as Utility

Scene input:
Two or more characters need each other to get through the current problem.

Required pressure:
The characters cannot safely solve the problem alone.

Doctrine applied:
The relationship begins as shared function and grows into care through repetition.

Generated scene behavior:
The first bond is practical. The scene should show cooperation, support, or rescue first, then let trust or affection emerge as a consequence of repeated usefulness.

Pass/fail test:
- Pass: the relationship is first established through work, rescue, or shared survival, and only later reads as affection.
- Fail: the relationship is declared emotionally without any shared labor.

## 6. Progress by Expanding Choice Space

Scene input:
A character receives a new power, tool, training result, or upgrade.

Required pressure:
The character must choose among multiple viable responses.

Doctrine applied:
Progression increases decision space rather than merely raw output.

Generated scene behavior:
The new capability should add verbs, routes, or coordination options. The scene should feel more open, not just more lethal.

Pass/fail test:
- Pass: the upgrade changes what the character can choose to do.
- Fail: the upgrade only increases numbers, damage, or spectacle.

## 7. Keep Consequences in the World

Scene input:
A failure, defeat, death, or broken system has already occurred.

Required pressure:
The scene must continue in the same world state rather than reset cleanly.

Doctrine applied:
Consequences remain as knowledge, scars, or altered state.

Generated scene behavior:
The world should remember. The scene should acknowledge prior damage and use it as part of the current problem.

Pass/fail test:
- Pass: failure leaves a durable effect that changes later choices.
- Fail: the scene erases the cost or resets consequence away.

## 8. Make Comfort Suspicious

Scene input:
A character is offered luxury, relief, oblivion, or rest while under strain.

Required pressure:
The offer must compete with agency or memory.

Doctrine applied:
Comfort is treated as a force with costs.

Generated scene behavior:
The scene should make comfort morally or operationally ambiguous. It may heal, but it must also threaten to soften resistance, dull memory, or hide coercion.

Pass/fail test:
- Pass: comfort restores something while also risking something important.
- Fail: comfort is free, purely decorative, or automatically good.

## 9. Write Institutions as Coherent and Harmful

Scene input:
An authority, organization, or formal system responds to the protagonist.

Required pressure:
The institution must have a defensible goal that still conflicts with the character's needs.

Doctrine applied:
Authority is rational and still damaging.

Generated scene behavior:
The scene should show coherent optimization creating harm. The institution should not be stupid; it should be misaligned.

Pass/fail test:
- Pass: the institution is understandable and the damage comes from the mismatch.
- Fail: the institution exists only as a cartoon villain.

## 10. Make Recognition Matter

Scene input:
A character is isolated, illegible, hidden, or reduced to a signal.

Required pressure:
Someone else must notice, believe, or answer them.

Doctrine applied:
Witnessing, naming, communication, or belief becomes rescue infrastructure.

Generated scene behavior:
The scene should turn recognition into an action that changes the character's options. Being seen should matter as much as a weapon, a tool, or a door.

Pass/fail test:
- Pass: recognition changes the scene state and restores agency or connection.
- Fail: recognition is emotional decoration with no operational effect.

## Harness Use

To test a scene draft, answer the following for each doctrine:

1. Does the scene input force the relevant pressure?
2. Does the doctrine produce a visible scene behavior?
3. Does the pass condition describe an action the reader can verify?
4. Does the fail condition catch the common fake version of the scene?

If the answer to any of those is no, the scene is not yet Scene Compiler ready.
