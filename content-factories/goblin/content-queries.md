# Goblin Content Queries

This is the factory interface.

A supported query should produce a goblin using only this folder.

## Default Output Contract

Unless the query asks for less, output:

- name
- role or use case
- traits
- dominant decision pattern
- likely interpretations
- likely mistakes
- likely dialogue

## Query: Generate a goblin.

### Required Inputs

- None.

### Optional Inputs

- role
- trait mix
- command to interpret
- risk level
- dialogue amount
- name style

### Expected Outputs

- command-friendly name
- balanced trait spread
- one dominant trait
- one likely command interpretation
- one likely mistake
- two dialogue lines

## Query: Generate a goblin knight.

### Required Inputs

- role: knight

### Optional Inputs

- courage level
- obedience level
- protector, attacker, guard, or false knight angle
- command context such as `protect wizard` or `hold bridge`

### Expected Outputs

- name with optional title
- knight-skewed traits
- likely defense behavior
- likely overreach or cowardice
- command interpretations for protect, attack, hold, and retreat
- dialogue lines using reporting and technical correctness

## Query: Generate a smart coward.

### Required Inputs

- intelligence: high
- courage: low
- self-preservation: high

### Optional Inputs

- role
- greed level
- obedience level
- command to interpret

### Expected Outputs

- name
- strong risk model
- indirect action pattern
- likely mistake: under-commitment, early retreat, or over-planning
- dialogue with reports, complaints, and technical correctness

## Query: Generate a goblin who misreads protect.

### Required Inputs

- command: protect

### Optional Inputs

- target to protect
- literalness level
- kindness level
- problem-bias level
- whether damage is allowed

### Expected Outputs

- name
- trait mix explaining the misread
- exact wrong interpretation
- action taken
- collateral or social consequence
- correction needed for next command
- dialogue explaining why the goblin thinks it complied

## Query: Generate a goblin sports commentator.

### Required Inputs

- role: sports commentator

### Optional Inputs

- sport or activity
- confidence level
- intelligence level
- greed level
- whether the commentator is also a participant
- Gasket-style observation intensity

### Expected Outputs

- name or title
- traits tuned toward observation, confidence, and verbal feedback
- pattern-observation behavior
- likely mistakes: overcalling patterns, claiming credit, distracting players
- 5 to 8 Gasket-style observation lines

## Query: Generate a goblin likely to create collateral damage.

### Required Inputs

- damage bias: high problem-bias or high confidence plus low/medium intelligence

### Optional Inputs

- role
- command
- acceptable damage boundary
- self-preservation level
- kindness level

### Expected Outputs

- name
- traits that explain damage
- likely interpretation
- likely action
- likely collateral damage
- useful result, if any
- dialogue that is technically correct or prematurely celebratory

## Query: Generate a smart but cowardly goblin knight.

### Required Inputs

- intelligence: high
- courage: low
- role: knight

### Optional Inputs

- obedience level
- self-preservation level
- protected target
- current command

### Expected Outputs

- name and title
- traits: high intelligence, low courage, high self-preservation, medium or high obedience
- likely interpretations for protect, attack, hold, retreat
- likely mistakes: over-fortifies, avoids direct contact, rebrands retreat as tactical
- likely dialogue: report, complaint, technical correctness

## Query: Interpret command for goblin.

### Required Inputs

- goblin trait mix
- command

### Optional Inputs

- target
- environment
- time pressure
- danger level
- reward or punishment

### Expected Outputs

- literal interpretation
- biased interpretation
- chosen action
- likely mistake
- dialogue line

## Query: Generate goblin dialogue.

### Required Inputs

- goblin traits or profile
- situation category: reporting, complaining, celebrating, misunderstanding, technical correctness, or Gasket-style observation

### Optional Inputs

- command
- target
- result
- number of lines

### Expected Outputs

- lines matching `dialogue-patterns.md`
- no full conversation unless explicitly requested
- lines that reveal behavior, not biography
