# 2026-07-04 Sense Simulation + Drink Proof Ladder + Normandy Promotion

Status: promotion addendum
Date: 2026-07-04
Owner: Quartermaster

## Scope Reviewed

Drive evidence:

- `Discovery Promotion Report - 2026-07-04 - Sense Simulation + Drink Proof Ladder + Normandy Doctrine Cast`
- `Drink Simulation Ore Extraction Answers - 2026-07-03`
- `Normandy Campaign Simulation Artifacts - Sherman Crew Alpha/Whiskey/Tango/Delta`
- updated Drive cluster/index surfaces for Recipe Synthesis, AI Orchestration, Accessibility Engineering, Animation and Pose Systems, Game Development, Writing Systems, Project Archaeology, Home Center, and Daily Delta

GitHub evidence:

- `Valar05/agent-closet` commit `58ba381bc19154fe79859abda7b8b75c15dfa068`
- `scratch/sense-simulation-skill-candidate.md`
- `scratch/drink-simulation-sense-synthesis-collation.md`
- `scratch/drink-observation-ledger.md`
- `scratch/research-manifest-sense-synthesis.md`
- `discoveries/research-corpus/sense-synthesis/README.md`
- `discoveries/research-corpus/sense-synthesis/manifest.jsonl`
- `procedures/chat-export-corpus-mining.md`
- `tools/mine-chat-export.py`
- `Valar05/pose-lab` PR #4: `Add Meshy Ready Static falsification experiment`

## Promotion Records

### 1. Sense Simulation Truth Ladder

Observation:

Sense Simulation generalizes Visual Truth Authority into a broader review skill. It separates Physical Truth, Visual Truth, Perceptual Truth, and Behavioral Truth instead of treating implementation correctness as equivalent to human experience.

Why it matters:

Many project failures come from optimizing the wrong layer. A transform can be correct while the weapon still reads as floating. A UI can be technically functional while the user hesitates. A recipe can contain the intended ingredients while the experienced flavor misses the target.

Reusable rule:

Do not judge experience from implementation facts alone. Name the desired experience, inspect what reaches the senses, infer what the human will believe, then ask what behavior that belief causes.

Supporting evidence:

- `scratch/sense-simulation-skill-candidate.md` defines the Physical -> Visual -> Perceptual -> Behavioral truth ladder.
- The same file states that metrics explain but do not judge experience.
- It defines output fields for desired experience, observed experience, contradictions, dominant perception, supporting metrics, recommended changes, and confidence.

Confidence: medium-high as a scratch candidate. Do not canonize yet.

Owning cluster: AI Orchestration, with support from Accessibility Engineering and Animation and Pose Systems.

Promotion decision:

Promote as strong scratch ore and active review vocabulary. Hold canon until repeated evidence proves it changes implementation priorities across multiple domains.

### 2. Drink Simulation Proof Loop

Observation:

Drink Simulation moved from recipe brainstorming into proof-gated perceptual composition. The useful loop is target perception -> mode -> levers -> ingredient jobs -> predicted interactions -> build -> observation -> deviation -> reusable rule.

Why it matters:

This prevents recipe-table cosplay. A table of ingredients is not knowledge unless the prediction survives contact with taste and the deviation creates a reusable rule.

Reusable rules:

- The ingredient is not the flavor; the composition is the flavor.
- Recipes are implementations; sensory signatures are assets.
- Hydration Mode and Ritual Mode need different acceptance rubrics.
- Bitters are aromatic and structural modules, not just bitterness sources.
- Predict before tasting; preserve the mismatch.

Supporting evidence:

- `scratch/drink-simulation-sense-synthesis-collation.md` defines Drink Simulation as a fast feedback loop for perceptual composition.
- `scratch/drink-observation-ledger.md` pre-registers prediction-first experiments with observation and deviation fields deliberately left blank until tasted.
- `scratch/research-manifest-sense-synthesis.md` defines a proof ladder: internal corpus evidence, experiment logs, external mechanism support, then promotion only if future behavior changes.
- `discoveries/research-corpus/sense-synthesis/README.md` limits the corpus to metadata, short derivative notes, and rights-clear artifacts, not full-text dumps.
- Drive `Drink Simulation Ore Extraction Answers - 2026-07-03` adds concrete lever/failure evidence: carbonation as dryness/structure, water exposing overbuilt recipes, salt rounding bitterness, acid and sweetness morphing bitterness, and gentian requiring support to read tonic-adjacent.

Confidence: medium for Drink Simulation as a domain pack; low-medium for parent Perceptual Composition until repeated outside drinks.

Owning cluster: Recipe Synthesis / Home Center, with AI Orchestration and Project Archaeology support.

Promotion decision:

Activate Recipe Synthesis as the owning surface. Do not create a separate Drink Simulation cluster. Treat Drink Simulation as the first proof-gated domain pack under Recipe Synthesis / Perceptual Composition.

### 3. Research Corpus Boundary And Rights Gate

Observation:

The Sense Synthesis research corpus distinguishes source metadata, rights notes, safety domains, and local-copy policy before anyone starts dumping research or chat exports into the repo.

Why it matters:

The repo needs evidence without becoming a copyright landfill or a safety-advice laundering machine. Metadata and bounded derivative notes are enough until rights and safety are clear.

Reusable rules:

- External research supports or challenges a claim; it does not replace prediction/build/observation/deviation logs.
- Raw ChatGPT exports stay local-only.
- Safety-sensitive hydration, alcohol, fermentation, medical, supplement, nicotine, or inhalation material stays scratch until reviewed.
- Every source must map to a claim, lever, mode, rights note, and safety domain.

Supporting evidence:

- `discoveries/research-corpus/sense-synthesis/README.md` defines allowed and not-allowed contents plus schema and acceptance criteria.
- `discoveries/research-corpus/sense-synthesis/manifest.jsonl` records candidate sources with claim tags, lever tags, mode tags, rights notes, and safety domains.
- `procedures/chat-export-corpus-mining.md` defines the raw corpus rule and bounded derivative mining workflow.
- `tools/mine-chat-export.py` emits bounded derivative source indexes and safety tags instead of full raw conversations.

Confidence: high for corpus-boundary procedure; medium for the specific Sense Synthesis source set, because most sources are candidate metadata rather than fully cited doctrine.

Owning cluster: Project Archaeology, with AI Orchestration support.

Promotion decision:

Promote the boundary/routing rules. Keep scientific/culinary mechanism claims as support candidates until used in logged experiments.

### 4. One-Command Evidence Front Door

Observation:

Pose Lab cloud visual truth work exposed a recurring under-tooled path: agents were repeatedly asking for permission to stage, commit, push, trigger workflow, collect artifacts, open cloud review, and inspect screenshots.

Why it matters:

If evidence acquisition itself is approval-heavy shell-fragment roulette, visual tasks stall or churn. A repo-owned command can preserve safety while reducing friction.

Reusable rule:

Expensive or approval-heavy evidence workflows need a single repo-owned command with explicit safety rails. The command does not replace judgment; it gets the agent to the correct evidence surface.

Supporting evidence:

- Agent Closet `scratch/pose-lab-cloud-visual-truth-self-service-ore.md` records the ore.
- Pose Lab PR #4 gives the current concrete case: a hosted Meshy Ready Static falsification experiment.

Confidence: medium. Strong for Pose Lab, candidate for broader visual/build pipelines.

Owning cluster: Animation and Pose Systems, with Software Delivery and AI Orchestration support.

Promotion decision:

Keep as a candidate operational rule under Animation and Pose Systems. Promote only after another repo repeats the same evidence-front-door need.

### 5. Isolated Falsification Packet Boundary

Observation:

Pose Lab PR #4 isolated a directly authored Meshy Ready Static actor on a known visual-green baseline and bypassed retarget, IK correction, adaptive solve, blending, and generated clip machinery.

Why it matters:

The experiment proves the renderer, Meshy rig, and simple FK attachment can produce the desired class of result. That narrows the suspect to the existing Meshy Ready retarget pipeline without pretending the production path is repaired.

Reusable rule:

A visual-green isolated path can prove capability and narrow suspects, but it does not repair the production path by itself.

Supporting evidence:

- Pose Lab PR #4 title/body and hosted-review packet.
- July 4 Drive promotion report records PR #4 as falsification evidence, not production fix.

Confidence: high for the specific Pose Lab diagnosis; medium as reusable doctrine.

Owning cluster: Animation and Pose Systems.

Promotion decision:

Promote the packet boundary. Do not count PR #4 as production repair until the production Ready route is fixed and visually accepted.

### 6. Normandy Doctrine Cast / Moving Doctrine

Observation:

The Normandy Sherman cast creates companions as doctrine under motion rather than quest dispensers. Whiskey preserves machines, Tango preserves people, Delta preserves order, and Alpha decides what survives when those values collide.

Why it matters:

This gives both game design and writing a reusable companion-construction grammar. Characters become systems that create tactical pressure, social pressure, trust changes, and failure modes.

Reusable packet:

1. origin pressure
2. pre-war habit
3. tactical strength
4. tactical weakness
5. vice or distortion
6. social hook with player
7. battlefield failure mode
8. campaign use
9. what they preserve
10. what they misread
11. what makes them trust or resent the player

Supporting evidence:

- Drive `Normandy Campaign Simulation Artifacts - Sherman Crew Alpha/Whiskey/Tango/Delta` defines Alpha, Whiskey, Tango, Delta, the platoon social triangle, simulation hooks, and the campaign truth.

Confidence: medium-high for writing/game design pattern; needs runtime test before mechanics promotion.

Owning clusters: Game Development and Writing Systems.

Promotion decision:

Promote as a design/writing pattern. Keep project-local campaign details in the Normandy artifact until there is a live repo or game prototype.

## Source Of Truth Decisions

- `Valar05/agent-closet` is canonical for Sense Simulation, Drink Simulation scratch, research corpus metadata, chat-export derivative mining procedure, and promotion addenda.
- `Valar05/pose-lab` PR #4 is canonical for the Meshy Ready Static falsification packet.
- Drive remains canonical for the Normandy campaign cast and Drink Simulation ore answers.
- Drive promotion reports summarize and index; they do not replace GitHub implementation or scratch truth.
- Thunder Brainstorm should carry source references only, not mirrored doctrine bodies.

## Duplicate / Merge Decisions

- Do not create a top-level Perceptual Composition cluster yet. Evidence points there, but current proof is drink-centered.
- Do not create a separate Drink Simulation cluster. Route it through Recipe Synthesis / Sense Synthesis.
- Do not create a separate Sense Simulation cluster. Keep it as an AI Orchestration skill candidate until repeated cross-domain proof exists.
- Treat Home Center issue #16 as reinforcement of tool-loop failure-report doctrine, not a fresh doctrine family.
- Treat Pose Lab PR #4 as falsification evidence, not production acceptance.

## Archive / Demote Guidance

Archive or demote:

- recipe notes that name ingredients without target perception, lever job, prediction, observation, deviation, and reusable rule
- proof matrices treated as verdicts instead of gates
- raw chat exports copied into repo-facing doctrine
- research PDFs or full-text blobs without rights clarity
- isolated visual experiments described as production repair
- Home Center failure reports that expose planner sludge instead of failed step, cause, preserved successes, and next safe action

## Final Compression

```text
Implementation creates sensation.
Sensation creates perception.
Perception creates behavior.

Recipes are implementations.
Flavor is composed perception.

Companions are not quest givers.
They are moving doctrine under fire.
```
