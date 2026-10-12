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

## Historical boundary — superseded for the portable-core experiment
P0–P4 documentary baselines are approved/completed within recorded limits and preserved on `docs/governance-baseline` at `15acfb58dfa9f9616b60b2c41c771953cbfc878c`. P5-B03 (P0–P4 documentation checkpoint) is RESOLVED; previous checkpoint permission was limited to the one completed documentation commit/push, not future Git operations. Current authorization covers reconciliation of the nine existing P5 documentation changes only. P5 remains BLOCKED: P5-B01 experimental scope/version approval, P5-B02 target Windows facts/native access and P5-B04 provenance/license evidence remain OPEN. No executable PoC, installation, tests, packages, ADR approval, commit/push/merge or P6 work authorized. Preserve historical handoffs and unrelated work; execution book owns current status.

## Current authorized boundary — 2026-10-12
The owner's P5 EXECUTION MODE AND START CODING correction authorizes actual experimental Python standard-library implementation/tests under experiments/p5_portable_core using the existing cloud Python. Do not require Windows inventories/read-only handoff completion before this portable core work. Preserve prior documentation and record genuine executable evidence. This is not production stack/ADR approval,Qt/.NET installation,Windows GUI/installer proof,Git action or P6 authorization. Core source/test scope is now reviewable;overall P5 remains BLOCKED with native/distribution B02/B04 OPEN and B03 RESOLVED. Execution book owns detailed current state and next gate. Follow the latest owner scope;never use the historical read-only boundary to block authorized core development.
