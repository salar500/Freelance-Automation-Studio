# Codex operating instructions

## Authority and scope
Read this file first, then [the master rulebook](docs/governance/00-master-rulebook.md), [execution state](docs/governance/09-execution-book.md), and books relevant to the task. The master rulebook owns durable product and development policies; this file owns the agent workflow. User instructions control the authorized task. If instructions conflict or approval is unclear, finish unaffected work and report the conflict before dependent changes.

Use the existing isolated checkout; do not create a worktree unless explicitly requested. Inspect Git status, branch, recent history, existing files and instructions before edits. Preserve unrelated, uncommitted and historical work. Never modify other repositories or delete unrelated files.

## Every task
1. Identify the active milestone, approval state, prerequisites and applicable acceptance criteria.
2. State intended files and changes; work only within the authorized milestone scope.
3. Read the authoritative books for each affected area; distinguish approved policy, proposals, assumptions and verified facts.
4. Execute relevant quality checks and report their actual outcomes, including failures, skips and blockers. Never remove tests or ignore failures to claim success.
5. Update authorized documentation, traceability, and milestone evidence. Do not mark incomplete work complete.
6. Update execution state according to its transition rules. Produce exactly one next recommended prompt in `docs/prompts/current-next-prompt.md`; if blocked, that prompt addresses the blocker.
7. Stop and await approval; do not execute the next prompt automatically.

Never silently change approved architecture or expand scope. Commit, push, merge, deployment, repository permission changes and destructive actions require explicit authorization; approval of a phase alone does not authorize them.

## Current boundary
P0–P4 documentary baselines are approved/completed within their recorded conditional scope. All eight ADRs, unresolved requirements and technical assumptions remain pending. Owner authorized one documentation-only Git commit and push to a new documentation branch, no main push/force/merge or application development. P5 prerequisite assessment previously identified blockers; its working documents remain outside this P0–P4 checkpoint and no executable PoC is authorized here. Read execution state; no automatic P5/P6 advancement.
