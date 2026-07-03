# Pose Lab Cloud Visual Truth Self-Service Ore

Status: scratch ore, not canon.

## Knowledge Capture

- Visual truth work must have one repo-owned front door. If the agent is repeatedly asking for different approvals (`git add`, `git commit`, `git push`, `gh workflow run`, artifact download, browser wake), the workflow itself is under-tooled.
- For Pose Lab Meshy saber work, the correct front door is `node tools/pose_lab_cloud_visual_truth_self_service.mjs --commit-message "..." --push --wait --download --inspect`.
- The tool should stage tracked edits with `git add -u` and require explicit `--include path` for new files, so generated Firebase artifacts are not swept into commits.
- Hosted visual truth still requires human/agent image inspection. Automation may collect, validate, and wake the exact Ready URL, but it does not replace looking at `tpose.png`, `ready.png`, and `ready_visual_follow.png`.
- Cloud failures must preserve artifacts. A failed Firebase run with screenshots or JSON is useful evidence; a tool crash that prevents artifact writing is a workflow bug.

## Friction Audit

- Missing script behavior: the self-service tool existed but did not own commit creation, so the agent fell back to ad hoc approval-triggering commands.
- Missing workflow discipline: manual `gh workflow run` bypassed the documented PR-triggered self-service path.
- Missing test coverage: static contracts checked dispatch avoidance and artifact inspection, but not the all-in-one commit/push path.
- Missing documentation emphasis: docs named the self-service tool but did not make the one-command commit/push/wait/download/inspect path the normal agent loop.

## Build Next

- Promote this pattern if it repeats: expensive/approval-heavy workflows should expose one narrow project-native command with explicit safety rails, then doctrine should tell agents to use that command instead of composing shell fragments.
