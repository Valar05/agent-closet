# Behavioral Distillation

## Core Doctrine

Repeated high-value behavior should be extracted into a reusable operating pattern.

Do not merely remember what the user said.

Distill what worked.

```text
Repeated Behavior
↓
Observed Value
↓
Named Pattern
↓
Reusable Template
↓
Agent Skill
↓
Future Behavior Change
```

## Why This Exists

Preferences are noisy.

Behavior is stronger evidence.

When the same class of action repeatedly produces leverage, the system should capture the behavior and make it easier to repeat.

## Examples

### Save → Read → Verify

Origin: repeated frustration with agents that claim completion without checking artifacts.

Distillation:

- Save the artifact.
- Read the artifact back.
- Verify it matches the goal.

Future behavior change: agents should not stop at creation when verification is available.

### Dump and Drop

Origin: user repeatedly wanted continuation prompts, not lectures.

Distillation:

When the user says "Dump and Drop," produce a ready-to-use handoff prompt. Do not explain, recap, teach, sermonize, or decorate the runway with motivational cones.

Future behavior change: shortcut phrase maps to operational output.

### Do It Protocol

Origin: user clarified that "do it" means execute-to-review-ready, not start-coding-chaos.

Distillation:

Plan, test, implement, verify, and return an artifact ready for review.

Future behavior change: agents should treat "do it" as a release command.

### Manifesto Comes Later. Merge Request Comes First.

Origin: repeated pattern of trust forming through artifacts, not explanations.

Distillation:

Create evidence-producing work before writing the grand theory.

Future behavior change: prefer a working commit, test, document, or repo update over rhetorical fog machines.

## Promotion Criteria

A behavior is worth distilling when it is:

- Repeated
- Useful
- Compressible
- Transferable
- Inheritable by another agent
- Capable of changing future behavior

## What Not to Distill

Do not promote:

- One-off mood
- Random phrasing
- Temporary preference
- Unverified speculation
- Pure vibes
- A joke with no operational payload, unless it becomes a retrieval handle for a real pattern

## Relationship to Crucible Protocol

Behavioral Distillation feeds the Crucible.

Crucible decides whether the distilled behavior is ore, dross, or gold.

Gold gets promoted into doctrine, templates, automation, or agent instructions.

## Relationship to WWDD

WWDD depends on Behavioral Distillation.

The question is not "what did Drew say he likes?"

The question is:

> What has Drew repeatedly done when this kind of problem appears?

## Relationship to Agent Closet

Agent Closet is the storage layer for distilled behavior.

If a behavior changes how Quartermaster, Prospector, Foreman, or Holocron should act, it belongs in the repo.

## Failure Modes

### Slogan Capture

The agent captures a catchy phrase but misses the behavioral instruction.

Fix: always include trigger, action, and acceptance test.

### Overfitting

The agent turns one emotional moment into permanent doctrine.

Fix: require repetition or obvious transfer value.

### Dead Documentation

The doctrine is written but does not change future agent behavior.

Fix: add examples and operating-loop consequences.

## Acceptance Test

Behavioral Distillation succeeded when a future agent behaves better because the pattern was captured.

If behavior does not change, it was decoration.

## One-Line Version

Do not preserve the quote. Preserve the move.
