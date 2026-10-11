# Traceability and test matrix

This directory owns TEST-XXXX definitions and the requirement-to-evidence matrix. P0 allocated no functional requirements or application tests. P1 now defines 67 functional requirements, 24 nonfunctional requirements and 182 acceptance test cases in the [P1 matrix](P1-requirements-matrix.md); every application case is NOT_RUN. Documentation checks are recorded directly in the [P0 report](../milestone-reports/MS-0001-P0.md); do not invent passing application tests.

For each REQ/NFR row record: requirement link/status, design/specification/ADR link, implementation reference, TEST identifiers, expected outcome, latest run/environment/result, acceptance evidence and approving reference. Until the responsible phase executes, use `pending: <reason>` in unproduced fields. Each test case records prerequisites, procedure, inputs, expected result and linked risks. Multiple tests may cover one requirement and one test may cover several requirements, provided coverage is explicit.

Acceptance: unique IDs, no orphan approved requirements, no claims based on stale/unrun evidence, and failures/skips/blockers visible. [Testing book](../governance/06-testing-book.md) owns result semantics; [master rulebook](../governance/00-master-rulebook.md) owns ID and trace conventions.

P2 adds [conditional UX coverage and TEST-0183 through TEST-0228](P2-ux-coverage.md). Total defined cases: 228; all application/interaction outcomes NOT_RUN. P1 original cases retain their definitions and outcomes. Documentary check results live in the milestone reports.

P3 adds [architecture dispositions and TEST-0229 through TEST-0239](P3-architecture-coverage.md). All 91 requirement IDs trace conditionally through UX/design; total future cases 239, all NOT_RUN. Original 228 definitions/outcomes are preserved. Missing requirement profiles for Block4 extensions remain explicit; documentation validation is recorded separately.

[P4 standards coverage](P4-standards-coverage.md) adds 91 documentary engineering dispositions, no new requirement or TEST allocation. Existing P1/P2/P3 matrices remain unchanged and all 239 test definitions NOT_RUN.
