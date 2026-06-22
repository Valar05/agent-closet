# Artifact-Mined Judgment

## Core Doctrine

The strongest agent opportunity is not generic chatbot Q&A.

It is extracting repeated decisions, recurring workarounds, hidden process debt, and tribal knowledge from operational artifacts.

Reality leaves fossils.

Artifacts reveal how work actually happens.

## What Counts as an Artifact

Useful artifacts include:

- Git commits
- Pull requests
- Merge request comments
- Issue tickets
- Jira/GitLab histories
- Support cases
- Emails
- Meeting notes
- Calendar patterns
- Docs
- Error logs
- Deployment records
- Test failures
- Repeated manual checklists

The artifact does not need to be pretty.

Ugly artifacts are often better because they still have the dirt on them.

## The Strategic Claim

The future is not AI answering questions.

The future is AI reading the evidence trail of how work actually happens, extracting institutional judgment, and turning it into governed workflows.

## Why Artifacts Beat Interviews

People describe what they think they do.

Artifacts reveal what they repeatedly did under pressure.

A coworker may not know they have invented a workaround. But the ticket trail knows. The merge requests know. The comments know. The same pasted explanation appearing five times knows.

## Mining Loop

```text
Artifact Corpus
↓
Repeated Behavior
↓
Friction Cluster
↓
Decision Pattern
↓
Doctrine Candidate
↓
Crucible Evaluation
↓
Promoted Judgment
↓
Workflow, Automation, or Agent Instruction
```

## What to Look For

### Repeated Workarounds

Signs that people are routing around a broken process.

### Repeated Explanations

Signs that documentation or interface design is failing.

### Repeated Approvals

Signs that decision authority is concentrated or that a flywheel already exists.

### Repeated Test Failures

Signs that test harnesses are missing, brittle, or misunderstood.

### Repeated Manual Steps

Automation candidates.

### Repeated Confusion

Doctrine or onboarding candidates.

### Repeated Silence

Possible fear, ambiguity, ownership gap, or missing escalation path.

## Relationship to Prospector

Prospector mines artifacts for ore.

It asks:

- Is there hidden value here?
- What keeps repeating?
- What pain point is visible without asking anyone?
- What doctrine is trying to be born?

## Relationship to Quartermaster

Quartermaster preserves promoted judgment.

It asks:

- Is this worth storing?
- Where should it live?
- How should it be indexed?
- What future agent should inherit this?

## Relationship to Foreman

Foreman turns mined judgment into working artifacts.

It asks:

- What is the smallest useful version?
- What are the acceptance criteria?
- What test proves this solved the problem?

## Risks

### Hallucinated Causality

Do not infer motives from artifacts without evidence.

Say "the artifact suggests" when making an inference.

### Access Control

Artifacts may contain private, regulated, or sensitive information. Preserve security boundaries.

### Governance Debt

Mining may reveal process problems before leadership is ready to fix them.

### Over-Automation

Not every repeated behavior should be automated. Some repeated behavior is judgment under constraint.

### Data Quality

Messy artifacts can mislead. Cross-check across sources when possible.

## Testable Product Slice

A minimal implementation should:

1. Ingest one repository or ticket corpus.
2. Find repeated workaround clusters.
3. Produce an evidence-linked pain-point report.
4. Propose doctrine or workflow fixes.
5. Track whether future tickets decrease.

## Acceptance Test

Artifact-Mined Judgment is working when it produces a useful insight without needing to interrupt the humans doing the work.

The system reads the fossils, identifies the pressure pattern, and returns with ore.

## One-Line Version

Do not ask the tribe what it knows until you have read the cave walls.
