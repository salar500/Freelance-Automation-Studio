# Development book

Status: P4 proposed standards baseline, 2026-10-11; READY_FOR_REVIEW only after checks. Owner conditionally approved P3 documentation, not technologies or ADRs. These language-neutral conventions are proposed for future authorized implementation; no source or tooling created. [Master policy](00-master-rulebook.md) owns permanent constraints and change/approval authority; this book owns coding, use-case, versioning, dependency and review conventions. [Code organization](05-code-organization-book.md), [testing](06-testing-book.md), [security](07-security-book.md) and [release](08-release-book.md) own their disciplines.

## Enforcement contract
Each DEV rule states scope/action, rationale, enforcement evidence and accountable owner. Future reviewers require the named evidence for applicable changed behavior; missing mandatory evidence blocks that change's gate, not unrelated low-risk work. Exceptions record rule, reason, scope/expiry, affected REQ/design/risks, alternative, approving owner and removal/review condition. Exceptions cannot silently waive permanent policy, adopt a PROPOSED ADR or change architecture. Language-specific addenda and commands follow approved technology plus P5 proof; no language, formatter or package manager mandated here.

## Coding conventions
| Rule | Scope / required action | Rationale | Verification | Owner |
| --- | --- | --- | --- | --- |
| DEV-01 Names | Descriptive domain/action names; units and UTC suffixes for numeric/time fields; stable public spelling; avoid obscure abbreviations except registered IDs | Predictable interpretation | Review public API/examples against glossary; later native-language formatter/naming addendum | Component lead |
| DEV-02 Files | One cohesive responsibility per file; module-private source stays under its owner; no generic dumping-ground utilities | Limit coupling | Ownership/import review per organization book | Architect |
| DEV-03 Functions | One observable purpose; extract unrelated branches/effects; no arbitrary line-count quota; explain unavoidable complex transformations | Reviewable behavior | Complexity review plus boundary/negative tests; document justified exceptions | Code reviewer |
| DEV-04 Types | Explicit bounded request/result/error types, no magic null/sentinel or unchecked dynamic payload; interfaces document pre/postconditions, ownership and units | Reject unexpected states | Contract/schema/invalid-value tests; static checks after stack approval | Contract owner |
| DEV-05 State | Immutable executed job/config/input and terminal attempt history; validation/review/approval/export remain separate; transitions use expected revision/lease | Avoid stale success | State/race cases from P3 protocol; changed-artifact approval denial | Domain/orchestration lead |
| DEV-06 Injection | Constructor/composition-supplied typed ports; pure domain free of drivers/UI/OS; no hidden singleton service locator or environment-dependent constructor effects | Isolated tests | Inject fake ports, test use cases without UI/files/network; inspect imports | Application lead |
| DEV-07 Resources | Scoped cleanup for handles/processes/temp leases; cleanup may not mask primary failure; bound loops/queues/allocations; never block UI on IO | Prevent leaks/exhaustion | Leak/fault/cancel tests and resource evidence; retain primary + cleanup diagnostics | Infrastructure lead |
| DEV-08 Cancellation | Propagate typed cancellation/deadline through every bounded work unit and IO operation; cancellation intent is not stopped/success | Safe interruption | P3 cancel/timeout/worker-tree tests; truthful partial/check NOT_RUN result | Worker lead |
| DEV-09 Validation | Validate syntax/types/limits and semantic prerequisites at trusted boundaries, not only UI; distinguish unsupported vs invalid | Prevent bypass | Negative/unauthorized tests through direct service/IPC entry, not button state | Security/module lead |
| DEV-10 Errors | Catch only where a typed decision/recovery can be made; top-level safety boundary maps unknown errors to INTERNAL_ERROR without swallowing; cleanup/audit retains failures | No false success | Fault injection + expected structured errors/log redaction; taxonomy below | Application lead |
| DEV-11 Comments | Explain rationale/invariants/security or fidelity constraints; public API documents inputs/outputs/errors/cancel/version and examples; avoid restating obvious code | Maintain durable intent | API/spec consistency review on changed interfaces | API owner |
| DEV-12 Determinism | Explicit encoding/locale/order/seed/time ports; same pinned inputs/config/profile produce comparable reconciled results; nondeterministic browser timing disclosed | Verifiable jobs | Repeated synthetic runs and independent expected counts; report environment | Module lead |
| DEV-13 Abstraction | Share proven common policy through public contracts; create abstractions only for demonstrated recurring needs; remove unused code/dependencies with impact checks | Avoid speculative complexity | Review callers/duplication/import graph and affected tests | Maintainer |
| DEV-14 Configuration | Parse versioned bounded structured data, reject unknown required schema; defaults explicit/safe; no executable template/credential fields | Safe reuse | Schema/fuzz/compatibility/migration tests, template diff invalidates plan | COM-Q owner |
| DEV-15 Logging | Use structured local events/redacted error references under security book; no raw exception/client-content dumps | Privacy and diagnosis | Secret-canary/log/diagnostic-bundle review | COM-O owner |
| DEV-16 Scope | Each change maps REQ/NFR and authorized design/profile; eleven P3 extensions stay conditional; no speculative feature code | Prevent scope drift | Change/trace report and owner scope disposition before implementation | Requirements lead |

## Application use-case contract
Each service accepts a typed validated request with correlation/job/version/expectedRevision/idempotency reference where applicable. Resolve current permissions and invariants, coordinate pure domain decisions with ports, establish COM-L transaction ownership, append required audit, commit before reporting durable success, then return bounded success/error/pending-effect result. Never hold a DB transaction while doing browser/filesystem work; prepared intents reconcile external effects. Domain owns invariant interfaces; application owns orchestration/use-case ports; infrastructure implements them; composition root wires adapters. P3's logical components/DAG remain authoritative, not forced one-project-per-component.

| Conceptual use case | Preconditions / effect | Independent testing seam |
| --- | --- | --- |
| CreateJob | Existing allowed client/project/module; create validated draft only | Fake repository; missing/invalid references and unchanged originals |
| ValidateJob | Pinned config/input/profile; invoke safe validators, retain truthful findings | Pure rules + isolated parser contract fixture |
| PrepareExecution | Compute immutable plan/effects/resource needs; no irreversible effects or implied consent | Fake clock/workspace/capability ports; plan diff |
| StartExecution | Fresh plan consent/scopes; single attempt/lease committed before dispatch | Fake supervisor/writer; duplicate/stale grant denial |
| CancelExecution | Current attempt/revision; signal stopping and reconcile actual disposition | Fake worker event order; completed vs validation cancellation |
| ReviewFinding | Current evidence, local reviewer label/time/rationale; observation never auto-defect | Fake evidence store; stale/unknown finding rejection |
| ApproveDeliverables | Eligible immutable selection/check/review evidence; human decision only | Fake hashes/review; stale/failed/missing evidence deny |
| ExportPackage | Current approval + local destination plan; verify writes/manifest before EXPORTED | Fake artifact/output ports; collision/full disk/tampering |
| RecoverInterruptedJob | Owned lease/process facts and prepared intents; retain prior failure/history | Fault matrix; no duplicate destructive replay |
| RestoreBackup | Explicit consent; staged compatible verified backup and space | Fake DB/files; corrupt/incompatible backup denies replacement |

Test pure service decisions without UI. Integration later proves real transactions/OS behavior; fakes do not establish confinement or durability. [P3 lifecycle](../specifications/P3-job-worker-protocol.md) and [persistence](../specifications/P3-persistence-artifacts.md) specify actual invariants.

## Error category reconciliation
P3 stable error codes remain authoritative. Proposed broad coding categories are tags, not a second incompatible wire taxonomy. Error instance: errorId, stable code/category/severity, safe description and affected scope, restricted diagnosticRef, job/version/attempt/correlation refs, timestampUtc, retry eligibility and recovery recommendation. Add a code only after contract/version/trace review.

| Coding tag | P3 category/code mapping / handling |
| --- | --- |
| BUSINESS_VALIDATION_ERROR | Plan/state/approval prerequisite rejection; INVALID_STATE or named validator cause; user correction, no retry of unchanged request |
| INPUT_ERROR | INPUT_INVALID, UNSUPPORTED_INPUT, INPUT_CORRUPT; supported corrected input/profile required |
| PERMISSION_ERROR | PERMISSION_DENIED, website authorization failure; renew exact scoped authorization, no auto-elevation |
| PROCESSING_ERROR | WORKER_START_FAILED, WORKER_CRASH or module failure; diagnostic-dependent new attempt |
| RESOURCE_ERROR | Storage/memory exhaustion, timeout; stop bounded work; resource correction before eligible retry |
| NETWORK_ERROR | Network failure; authorization/idempotency rechecked, not blanket retry |
| INTEGRITY_ERROR | Validation/artifact/hash or DB corruption; block affected approval, preserve/quarantine, no false PASSED |
| RECOVERY_ERROR | DB/restore/reconciliation/export recovery failure; keep originals/history and visible blocker |
| INTERNAL_ERROR | Unexpected implementation/protocol exception; map safe cause with restricted diagnostics; fail safely, never silently return success |

[Security coding](07-security-book.md) owns boundary/retry/log details; [P3 recovery](../specifications/P3-recovery-approval.md) owns proposed category semantics. Every mapping preserves cancellation/partial/validation outcomes separately.

## Configuration and interface versioning
| Object | Owner / compatibility standard | Verification |
| --- | --- | --- |
| App/environment settings | COM-Q; nonsecret local settings, precedence explicit default < local app < selected job; environment may not disable policy | Invalid/range/precedence/offline tests |
| Module/job config | Module schema predicate + Q; structured config schema/version, snapshot after execution; migration creates new version and diff | Roundtrip/old/new/unknown-required fields, no arbitrary code |
| Templates | Q; no inputs/secrets/grants/approval; module/version range, validated bounded import/export | TEST-0237 and existing template cases |
| Desktop/module package versions | Maintainer; candidate semantic versioning, API-breaking major, compatible minor/patch; supported matrix explicit, no automatic downgrade | Approved release tuple/compatibility evidence |
| IPC/module/report/export schemas | Contract owner; P3 major/minor negotiation, reject unsupported major, optional minor additions only when negotiated | Existing contracts + TEST-0229/0235/0236 |
| Database schema | COM-L monotonically increasing migration version, not application semver; backup/preflight/integrity/restore and rollback constraints | TEST-0232 and release migration gates |

Compatibility and migration evidence precede adoption; no silent deletion/default replacement for unknown config. Rollback to old binary may be impossible after data migration and must be disclosed. Manual/offline update standards belong release book.

## Dependency lifecycle
DEV-17 governs every runtime/build/test/native/browser/installer/transitive dependency. Scope: proposal through retirement; rationale: licensing, Windows support and reproducible supply chain. Owner: architecture/license/security leads plus owner adoption decision. Evidence: a dependency record and approved exact-tuple decision; unresolved mandatory item BLOCKS adoption.

| Stage | Required evidence / action |
| --- | --- |
| A PROPOSAL | Name/purpose, required REQ/capability, alternatives, exact candidate version/tag/hash, official source and owning component; existing equivalent assessed first |
| B EVALUATION | License/SPDX/text/rights/attribution/redistribution/modification/commercial-use obligations, bundled-runtime/third-party notices and transitive inventory; exact Windows/arch support/lifecycle/native prerequisites; maintainers/release history/vulnerability advisories/provenance/signatures/checksums; offline/packaging/size impact |
| C APPROVAL | ADR or recorded dependency decision with owner, exact approved scope/version tuple, risk/exception and prerequisites; phase documentary approval alone is insufficient |
| D IMPLEMENTATION | Authorized declarations and lockfiles where supported; frozen installs, official verified sources, record toolchain/OS/options; no TLS/signature/hash bypass, floating latest or imported project auto-install |
| E MAINTENANCE | Review advisories/support/license changes at each release and scheduled maintenance; update in reviewed scope, regenerate controlled lock/SBOM, affected contract/integration/Windows/offline tests; security-critical issues block applicable release |
| Retirement | Inventory affected consumers/stored formats, substitute/remove and migrate safely; preserve notices/history and compatibility evidence |

License source evidence is not legal clearance for an unpinned binary. Missing/ambiguous license or redistribution rights requires owner/license review, not invented legal conclusions. [P3 source register](../specifications/P3-technology-evaluation.md) is historical evidence with unresolved terms; no selection or fresh support claim here.

## Review, defects and controlled change
DEV-18 scope: every authorized implementation report; rationale: inspectable results; owner: implementer + reviewer; enforcement: review record covers REQ/NFR, scope/files, architecture/ADR and security/data impact, test commands/actual counts/evidence/environment, risks/limitations, Git state and acceptance/approval. Review verifies standards, independent observable tests, no shortcut dependencies, no stale approval or hidden networking. Architectural exceptions use reason/scope/risk/alternatives/required authorization/removal condition, update authoritative ADR/book and preserve history.

Change sequence: requested outcome -> existing requirements/owner approval -> architecture/security/data/consumer impact -> scoped acceptance plan -> authorized small implementation -> relevant verification -> actual results/trace updates -> applicable approval. Major architecture change needs explicit authorization and ADR disposition first. Pure refactoring must preserve public behavior and run affected contracts; no new abstraction or dependency without demonstrated need.

Defect records use a locally unique stable key such as DEF-<milestone>-<sequence>, allocated in the active report's defect list (local record convention, not a new REQ/TEST namespace). Include severity (impact), priority (work urgency), affected REQ/component, reproduction/preconditions/input, expected/actual, environment/evidence, root-cause state, fix reference, verification run and regression risk. Never close without actual successful applicable verification; duplicate/obsolete records retain history. Technical debt uses TD-<milestone>-<sequence> with description/impact/risk/owner/remediation/priority/affected components and review date. Minor noncritical debt need not block release; critical acceptance failure does.

## Git and milestone workflow
DEV-19 owner: task owner/reviewer; scope: repository mutations; rationale: preserve user work and reviewable history; enforcement: before/after status and reviewed file list. Branch proposals: milestone/MS-xxxx-purpose or fix/short-purpose under explicit branch authorization; no new branch created here. Commit proposals: docs(P4): descriptive outcome or fix(module): reason, with relevant IDs/body; no automatic commit. Dirty tree is expected now: preserve and identify existing work rather than demanding a reset. Use only authorized paths; no git add-all, destructive clean/reset, history rewrite, unapproved force push or unrelated conflict resolution. Resolve conflicts by comparing intended changes and owners, rerun affected checks; preserve both valid intents. PRs state concrete behavior, validation and unresolved risks; merge/protection/release tags require explicit authority. Proposed release tag v<version> references reviewed verified artifacts; no remote settings changed.

Controlled documentation checkpoint (not performed): record baseline/status and exact permitted paths; verify links/whitespace/trace, review diff including untracked contents and secret/client-data exclusion; obtain explicit owner permission for commit (and push separately); stage only reviewed docs, inspect staged diff, commit, then record commit/status. Uncommitted P0–P4 history remains RISK-0010; permission is not inferred from this procedure.

Each milestone report includes repository baseline, authorized scope/prerequisites, REQ/design refs, files, actual work, architecture/security review, commands/counts/evidence and failures/skips/unrun, acceptance, risks/limits, Git state, actual milestone status, human approval gate and exactly one saved next prompt/action. [AGENTS](../../AGENTS.md) and [execution state](09-execution-book.md) own operational handoff. No phase auto-advances.

## Tooling and local verification
DEV-20 owner: tooling/QA lead; rationale: reproducible quality without cloud runtime dependence; enforcement: approved tool record plus local check evidence. Future minimal tools cover formatter, lint/type/static analysis, import boundaries, unit/contract/integration runners, secrets/vulnerabilities/licenses, documentation links, result capture and build verification. Choose native ecosystem tools only after ADR/PoC evidence; no installed/finalized toolchain or executable CI here. Offline local essential checks must work from pinned available dependencies; optional GitHub Actions mirrors local checks, with synthetic inputs only and no product dependence on GitHub. Missing advisory access is BLOCKED/not fresh clearance, not a passing scan.

Local workflow stages: pre-change baseline/impact; changed-unit/contract/integration checks; risk-based E2E; explicitly authorized pre-commit/staged scope checks; PR consumer/security checks; integration full regression; release clean-build/exact Windows/install/offline gates. Future command catalog records working directory, tool/version/options/env variable names (no values), expected nonzero propagation, count/artifact and resource constraints. No pretend executable commands before stack selection. Tests and gates belong [testing book](06-testing-book.md).

## Acceptance and unresolved decisions
Every rule has owner/enforcement and trace references; layout, secure coding, test strategy and packaging boundaries agree with P3. P4 can become READY_FOR_REVIEW after documentary checks only. Language/toolchain, OS/laptop, eight ADRs, detailed requirement extensions, confinement, license/support and numeric budgets remain OPEN. [P4 coverage](../test-matrix/P4-standards-coverage.md) maps all existing requirements to standards; [P4 report](../milestone-reports/MS-0005-P4.md) owns actual evidence.
