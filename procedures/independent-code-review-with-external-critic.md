# Independent Code Review With External Critic

Type: Procedure / review workflow
Status: Gold
Owner: Quartermaster
Date: 2026-07-02
Related:
- `shared/doctrine/perspective-guided-command.md`
- `shared/doctrine/encoded-judgment-doctrine.md`
- `/storage/emulated/0/Documents/GodotProjects/thunder-brainstorm/README.md`
- `/storage/emulated/0/Documents/GodotProjects/.codex/skills/claude-pr-code-review/SKILL.md`

## Purpose

Use an external critic for code review when the implementation may have been written by Codex/OpenAI, when the change is risky, or when independent judgment matters more than author intent.

The review driver is not the author model defending its own work. The author model may explain intent or implement fixes, but review should come from a model with no stake in the patch when available.

## Rule

Claude is the preferred external critic for automated PR review.

Do not build broad source packets for PR review. The critic should read the repository and pull request through read-only tools. If the repo or PR cannot be read, treat that as a capability failure instead of substituting pasted context.

Quartermaster remains responsible for repository truth, evidence, verification, preservation, and final synthesis.

## Responsibility Split

| Responsibility | Owner |
|---|---|
| Independent critique | Claude external critic |
| Repo and PR access tools | Thunder Brainstorm |
| Local verification and synthesis | Quartermaster / Codex |
| Implementation fixes after review | Foreman / Codex, only when requested |

## Operating Loop

1. Identify the target PR as `OWNER/REPO#NUMBER` or a GitHub pull request URL.
2. Invoke the workspace skill `claude-pr-code-review`.
3. Run Thunder Brainstorm's PR review driver from `/storage/emulated/0/Documents/GodotProjects/thunder-brainstorm`.
4. Keep review posting disabled by default.
5. Let Claude inspect the PR through read-only GitHub tools.
6. Verify every finding against repository evidence and changed diff lines before reporting or posting.
7. Return one coherent review response with findings first.
8. Preserve review artifacts under Thunder Brainstorm for later audit.

## Posting Rule

Inline GitHub comments require explicit permission and the runner's `--post` flag.

Only verified findings mapped to changed diff lines should become inline comments. Report-only findings may be summarized, but they are not postable line comments.

## Artifact Rule

Thunder Brainstorm owns run artifacts, including the mission, tool transcript, read log, raw critic output, verified findings, GitHub payload, and review report.

Agent Closet owns this portable procedure and the responsibility model. It should not duplicate Thunder's runner internals.

## Failure Handling

If `gh`, GitHub auth, PR permissions, Anthropic access, or repo read tools fail, report the exact blocker.

Do not replace failed repo access with anonymous assistant speculation.

## Acceptance Criteria

This procedure is working when:

- the critic can read the PR/repo through tools
- findings cite concrete repository evidence
- changed-line findings are mechanically verified before posting
- posting is dry-run by default
- review artifacts are saved for audit
- Quartermaster synthesizes one final response instead of forwarding raw critic output

## Retrieval Keywords

code review, Claude critic, external critic, pull request review, PR review, Thunder Brainstorm, no source packet, read-only repo tools, verified findings, changed diff lines, dry-run review
