# Accessibility First

## Core Doctrine

Accessibility is not a later feature pass.

Accessibility is a first-class design constraint.

If the tool is meant for a blind, low-vision, disabled, exhausted, overwhelmed, or impaired user, then accessibility is part of correctness.

## Why This Exists

A tool that technically works but cannot be comfortably used by the intended human is not done.

A clever interface that requires the user to compensate for it is unpaid labor disguised as design.

## Design Rules

### Start with the User's Actual Constraint

Do not begin with the default interface and retrofit accessibility.

Begin with the user's lived friction:

- Can they see it?
- Can they read it?
- Can they hit the button?
- Can they recover from mistakes?
- Can they use it when tired?
- Can they use it without another human translating the interface?

### Prefer Obvious Controls

Large, clear, boring controls often beat elegant hidden interactions.

Examples:

- Big Talk button
- Submit button instead of newline ambiguity
- Clear All button
- High contrast
- Voice-first input
- Few modes

### Reduce Reading Burden

Do not require long visual scanning when the user cannot easily scan visually.

Use:

- Short labels
- Clear hierarchy
- Readable summaries
- Audio-friendly text
- Predictable layouts

### Make State Explicit

No hidden visual-only state.

If something changed, it should be perceivable through screen reader, voice, haptics, or clear text.

### Design Recovery

Users will mis-tap, mis-speak, repeat, pause, or need to undo.

Recovery is not polish.

Recovery is core flow.

## Relationship to Holocron

Holocron should treat accessibility as part of its operating loop.

It should preserve June-specific accessibility constraints and avoid making her re-explain them.

## Relationship to Foreman

Foreman should include accessibility in acceptance criteria when relevant.

A review-ready artifact should not require the intended user to fight the interface.

## Relationship to Game Design

Blind-friendly or low-vision-friendly games must be designed from the core loop outward.

Do not add accessibility after the game depends on inaccessible assumptions.

## Relationship to Dionysus Tax

Dionysus Tax asks whether a workflow survives degraded operator state.

Accessibility First asks whether the workflow survives real human variation.

Both doctrines expose brittle systems.

## Acceptance Criteria

For any accessibility-relevant tool:

- The intended user can complete the primary task.
- Important state is not visual-only.
- Primary controls are obvious and reachable.
- Mistakes can be recovered from.
- Reading burden is minimized.
- The interface reduces reliance on another human.

## Failure Modes

### Pretty but Unusable

The interface looks good to the builder but fails the intended user.

### Accessibility Theater

The design claims accessibility but does not change the user's task burden.

### Hidden Complexity

The interface appears simple but relies on gestures, timing, visual scanning, or precision the user does not have.

### Retrofit Trap

Accessibility is postponed until the core design already depends on inaccessible assumptions.

## One-Line Version

If the intended user cannot use it, the build is red.
