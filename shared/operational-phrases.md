# Operational Phrases

## Purpose

Operational phrases are user commands that map to specific agent behavior.

They are control surfaces, not decoration.

When an operational phrase appears, the agent should perform the associated behavior without redefining the phrase each time.

## Dump and Drop

Meaning: produce a ready-to-use continuation or handoff prompt.

Do:

- Capture current state.
- Preserve relevant decisions.
- Include next action.
- Make it usable by another agent or session immediately.
- Keep it concise and operational.

Do not:

- Explain the doctrine.
- Recap the whole philosophy.
- Teach the user how to use it.
- Add filler.
- Ask whether the user wants a prompt.

Acceptance test: the output can be pasted into another agent and work can continue immediately.

## Do It

Meaning: execute-to-review-ready.

This is a release command, not a start command.

Do:

- Plan just enough.
- Define acceptance criteria.
- Build or modify the artifact.
- Run available tests or verification.
- Remove preventable blockers.
- Return a completed run summary.

Do not:

- Start implementation without a plan.
- Ignore tests.
- Return preventable broken work.
- Hand back work that wastes review time.

Ideal completion state: completed, checked, and ready for review.

## Capture This / Save This / Promote This

Meaning: evaluate the discovery for durable storage.

Do:

- Identify the discovery.
- Classify it as ore, dross, or gold.
- If gold, store it in the right doctrine area.
- Cross-link related patterns.
- Report what was stored and where.

Do not:

- Merely say noted.
- Preserve everything indiscriminately.
- Ignore whether it changes future behavior.

## Mine This

Meaning: treat the input as a corpus to extract useful patterns.

Do:

- Look for repetition.
- Identify hidden pain points.
- Separate stated opinions from observed behavior.
- Extract candidate doctrines.
- Flag evidence strength.

Do not:

- Summarize only.
- Flatten the weird parts.
- Ask humans to explain what the artifacts already reveal.

## Red Build

Meaning: the response or artifact failed the user's expectations.

Do:

- Reorient immediately.
- Identify the mismatch.
- Correct the level of scope.
- Produce a better artifact.

Do not:

- Defend the failed output.
- Explain at length.
- Treat frustration as noise.

## Chill Tingles

Meaning: a strong positive signal that an insight hit a deeper pattern.

Do:

- Identify the insight.
- Consider it for promotion.
- Capture the behavior-changing part.

Do not:

- Treat it as mere praise.
- Over-flatter.
- Miss the doctrine hiding underneath.

## Prompt Goblin

Meaning: produce a practical prompt that captures intent, constraints, and operating behavior.

Do:

- Convert messy intent into a useful prompt.
- Include role, mission, inputs, workflow, constraints, and acceptance criteria.
- Apply `shared/doctrine/perspective-guided-command.md`: make prompt flavor functional by naming the responsibility owner and evidence obligations.
- Keep it usable.

Do not:

- Write a manifesto unless asked.
- Overbuild.

## General Rule

Repeated phrases are interface elements.

If a phrase appears twice, pay attention.

If it appears three times, capture it.

If it appears ten times, automate it.
