# Drink Compiler Schema

Status: scratch schema candidate
Owner: Sommelier / Quartermaster
Date: 2026-07-03
Related:

- `drink-simulation-sense-synthesis-collation.md`
- `droobiedoo-chat-corpus-sense-synthesis-mining.md`
- `sense-synthesis-log-template.md`

## Purpose

Define the minimum structured shape for turning inventory, constraints, target perception, and feedback into a drink experiment.

## Candidate JSON Shape

```json
{
  "target_state": "preserved orange hydration drink",
  "mode": "Hydration",
  "constraints": {
    "volume": "40 oz",
    "calorie_target": "low",
    "caffeine": "none",
    "alcohol": "none",
    "safety_notes": ["electrolyte concentration should remain casual-sipping strength"]
  },
  "inventory": [
    {"item": "ice water", "jobs": ["dilution", "cold", "hydration"]},
    {"item": "Lite Salt", "jobs": ["minerality", "potassium", "savory edge"]},
    {"item": "orange bitters", "jobs": ["citrus peel aroma", "bitterness", "top note"]}
  ],
  "lever_map": {
    "aroma": ["orange bitters"],
    "salt_minerality": ["Lite Salt"],
    "dilution": ["ice water"],
    "bitterness": ["orange bitters"]
  },
  "prediction": {
    "first_impression": "cold salted citrus peel",
    "finish": "light bitter savory hydration",
    "failure_modes": ["seawater", "medicine", "ghost water", "flat"]
  },
  "build": {
    "formula": [],
    "process": [],
    "serving_state": "large cold vessel"
  },
  "feedback": {
    "observed_result": "",
    "prediction_mismatch": "",
    "next_adjustment": "",
    "reusable_rule_candidate": "",
    "confidence": "low"
  }
}
```

## Required Fields

- `target_state`
- `mode`
- `constraints.safety_notes`
- `inventory[].jobs`
- `lever_map`
- `prediction.failure_modes`
- `feedback.prediction_mismatch`
- `feedback.reusable_rule_candidate`

## Promotion Gate

Do not promote this schema until at least five experiments have been logged with prediction, observation, deviation, and next adjustment.
