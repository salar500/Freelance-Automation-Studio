# MS-0004 consumed five-block P3 instruction archive

Source: owner user message “PROJECT: FREELANCE AUTOMATION STUDIO / PHASE: P3 — SYSTEM ARCHITECTURE AND DETAILED DESIGN”, 2026-10-11, final command “ALL BLOCKS RECEIVED — BEGIN P3”. This is a normalized substantive archive of all received blocks, not a byte-for-byte transcript or current recommendation. Repeated Block5 text is consolidated; Block3 stopped mid-section8 (“The application may need network access”) and its missing continuation is not invented. Complete overlapping network/technology/Windows requirements from Blocks2/4/5 remain binding. Lists/field requirements and gates below preserve substantive scope. Documentary execution is reported in MS-0004; archive placement is not milestone/ADR approval or proof of unrun work.

## Multi-block control
Wait for all five blocks; acknowledge each briefly; no execution/modification/installation/implementation before Block5 explicitly says ALL BLOCKS RECEIVED — BEGIN P3. Retain earlier blocks; treat them as one task, never silently omit/override. All five arrived together in the final message with that command. Repository checkpoint and P2 verification must happen first; fail means stop, one P2 recovery action and no P2 completion/P3 execution.

## Block1 — Context, authorization and checkpoint
Roles: Principal Software Architect, Windows Desktop Architect, Security Architect, QA Automation Architect, Dependency/Licensing Specialist and Enterprise Technical Lead. Product: enterprise standalone Windows desktop automation platform, four independently testable modules: spreadsheet/CSV, website QA/regression, PDF/documents, website maintenance/template development.

Permanent constraints: no runtime ChatGPT/Codex/external AI, paid APIs, cloud backend/database or mandatory online authentication; offline local tasks and local client storage; secure auditable execution, human final approval, reliable error/recovery, modular professional UX; actual Windows10 compatibility proof; suitable free/open-source dependencies; no unauthorized website/Fiverr automation.

Owner conditionally approves P2 reported documentation completeness subject to repository verification and authorizes P3 documentation only. No unresolved requirement finalization, final technology adoption, application/prototype development, installation, commits/push/merge/deployment.

Read AGENTS; master/requirements/UX/architecture/testing/security/execution books; P1 matrix; P2 coverage/screens/workflows/module UX/failure-recovery/report. Inspect branch/HEAD/status/all uncommitted files, existing architecture/ADRs and identifiers, requirement/test registers, risks/decisions and milestone status. Use existing checkout, no worktree/new branch/reset/discard/unrelated rewrite/delete. Verify P2 actual deliverables before conditional approval reconciliation and P3 IN_PROGRESS.

## Block2 — Architecture, contracts, execution and evidence
Priorities in order: correctness, reliability, security, client privacy, maintainability, testability, recoverability, modularity, performance, minimal cost. Evaluate preferred modular monolith plus isolated workers, explain alternatives/tradeoffs; no microservices/cloud/distributed DB/external broker/unnecessary dependencies; no unverified final architecture.

Components A-S: Desktop Presentation; Application Services; Domain/Business Rules; Job Orchestration; Local Queue; Worker Supervisor; Module Registry; Input Validation; Output Validation; Human Review/Approval; Artifact/File Management; Local DB/Persistence; Reports; Packaging; Audit/Diagnostics; Error/Recovery; Config/Templates; Backup/Restore; Security/Permissions. Each: responsibility, inputs, outputs, public interfaces, owned data, dependencies, failure scenarios, security boundary, REQ/NFR links. Document direct layer communication and acyclic direction; UI cannot execute arbitrary OS commands.

Standard module contract for A-D: ID/version, operations, input/output specs, configuration schema, input validation, planning, permissions, resource requirements, progress, cancellation, timeout, error classification, retry eligibility, recovery, evidence, verification and cleanup. Future extensions must not alter unrelated internals/private data; no executable module code.

Workers: creation/init, IPC, assignment/progress/deadline/cancel/health/heartbeat, unexpected exit/resources/cleanup/retry/recovery/finalization. Version protocol; request/response/progress/error/cancel-ack/completion-ack messages, correlation IDs, validation/protocol errors. No unrestricted file/network rights by default; explain that process isolation is not verified sandbox.

Durable job lifecycle evaluate DRAFT, READY, PREFLIGHT, BLOCKED, QUEUED, RUNNING, VALIDATING, REVIEW_REQUIRED, REVISION_REQUIRED, APPROVED, READY_FOR_EXPORT, EXPORTED, FAILED, CANCELLED, INTERRUPTED. Define owner, allowed/rejected transitions, preconditions/validation/audit/persistence/retry/cancel/restart/incomplete/partial/versioned rerun. Separate execution outcome, validation outcome, human disposition, final approval and export completion; successful processing never automatic approval.

Artifacts: original/generated/intermediate/screenshots/logs/validation/bug reports/packages. Metadata: artifact/job/attempt/type/location/time/size/checksum/source/validation/retention. Preserve originals, safe temp writes/atomic finalization where supported, interruption/partial treatment, content change detection, relevant approval invalidation.

Review distinguishes automated/unverified/confirmed/dismissed findings, validation warning/failure, approved deliverable; owner/local identity/time/evidence/scope/invalidation/history/re-review. Modules cannot grant delivery approval; preserve audit history.

Templates: saved processing/module rules, mapping/output/validation/report preferences/limits; identity/schema/validation/import-export/compatibility/migration/defaults; structured data, no embedded executable code.

Errors: invalid input, unsupported file, permission, corruption, DB, worker start/crash, timeout/cancel, storage/memory/resource, network/website authorization, validation/export. Each classification, user cause, diagnostic info, retry/recovery/cleanup/audit; transient vs permanent, no silent discard.

Eight Mermaid diagrams: logical architecture, component dependencies, module execution, worker communication, job lifecycle, artifacts, review/approval, error/recovery. Names/relations consistent and requirements referenced. Acceptance: distinct responsibilities/dependencies/consistent module contract/complete worker lifecycle/unambiguous states/execution-approval split/provenance/original protection/recovery/extensions/trace to requirements+risks; unsupported assumptions OPEN, no runtime feasibility claim.

## Block3 — Database, storage, security, privacy and offline
Evaluate SQLite candidate only. Entities: Clients, Projects, Jobs, JobVersions, Attempts, Modules, ModuleVersions, Configurations, Templates, Input/Intermediate/Generated Artifacts, Findings, ValidationResults, HumanReviews, Approvals, AuditEvents, Errors, Recovery, Settings, Backups. Each purpose/PK/attributes/relationships/FKs/constraints/indexes/lifecycle/owner/retention/REQ; normalize, justify denormalization, ERD; no migrations/executable DB.

Transactions/concurrency/schema/migrations/rollback/constraints/integrity/shutdown/interrupted writes/corruption/backup/restore specified. SQLite/file stores not atomic together: evaluate temp -> validate -> hash -> prepare metadata -> atomic rename where supported -> final metadata -> restart reconciliation; not automatic approved design.

Storage areas: config, DB, client projects, immutable input snapshots, temp, evidence, outputs, approved deliverables, logs, backups. Directory owner/names/path validation/permissions/isolation/space/file limits/cleanup/integrity/retention/safe deletion/backup-restore. Never silently modify original; no client files in source repo/fixtures.

Threat model assets/boundaries/actors/surfaces/scenarios/likelihood/impact/mitigations/residual risks/verification. Threats: malicious files, traversal, symlinks/junctions, command execution, formula injection, macros, malformed documents, zip bombs, oversized inputs, resource exhaustion, secrets/logs, unauthorized files, unsafe temp, hostile websites, unauthorized networking, redirects, DB corruption, crashes, escalation, unapproved destruction, output changes, exposed backups, supply chain. Separate prevent/detect/recover; not full-sandbox claim.

Controls A-O: input validation, workspace isolation, worker rights, file rights, restricted commands, network grants, credential protection, safe logging, integrity, module trust/version, backup protection, destructive consent, final approval, dependency verification, secure update/install. Assign desktop/orchestration/supervisor/module/OS/human ownership, least privilege, limitations/unverified protections.

Privacy: no AI upload/inference, cloud DB, required sign-in/subscription/telemetry/analytics/external processing/hidden sync. Client files local; define ownership/retention/deletion/export/log/redaction/backup/diagnostics/privacy tests. Evaluate Windows-protected secret store if needed; never plaintext secrets/examples/logs/Git.

Offline behavior: startup, DB, spreadsheets/documents, local maintenance, history/templates/reports/packages/backup-restore/diagnostics; future tests, no AI connection/network licensing/cloud/hidden fallback. Section8 introduced authorized website network access then truncated; apply complete target-authorization instructions elsewhere without inventing continuation.

## Block4 — Modules, shared services, reports, trace and quality
Every module: responsibilities, inputs/outputs/operations/config, validation/stages/resources/security/failure/recovery/evidence/review/acceptance/trace. Shared platform owns common services, no incompatible duplicates.

A spreadsheet capabilities: import/format detection/encoding/workbook/sheets/columns/schema/mapping/normalization/exact duplicates/fuzzy candidates for review/missing values/filter/sort/merge/split/formula-safe/types/date-number/validation/comparison/export-reports. Stages IMPORT-INSPECT-VALIDATE-PLAN-TRANSFORM-VERIFY-REVIEW-EXPORT. Handle empty/missing/duplicate headers/mixed types/invalid dates/encoding/large/formula/unsupported/corrupt/row mismatch/ambiguous duplicates/partial. No uncertain auto-deletion; exact vs judgment; reconciliation/input-output counts/transforms/invalid/candidates/errors/hashes/time; streaming/chunks where needed; formulas/Excel fidelity pending, no universal lossless promise.

B QA capabilities: authorized target/scope/discovery/links/assets/console/network errors/smoke/regression/navigation/form/viewport/screenshots/traces/evidence/classification/review/comparison/bug report/summary. Stages AUTHORIZE-CONFIGURE-PREFLIGHT-DISCOVER-EXECUTE-COLLECT EVIDENCE-CLASSIFY-REVIEW-REPORT. Browser/viewport profiles/scenario versions/locators/stable waits/retry/timeouts/isolation/auth/evidence retention/cleanup/limits. Distinguish assertion fail, human-confirmed defect, environment, automation defect, inconclusive. Explicit scope/no unauthorized crawl/origin+redirect+request limits/no unapproved destruction/sensitive approval/no bypass. Windows/browser support conditional; emulation not physical device.

C documents: PDF inspect/merge/split/extract/reorder/rotate/metadata/text/supported conversion/DOCX templates/batch/report/validation/package. Stages IMPORT-INSPECT-VALIDATE-CONFIGURE-PROCESS-VERIFY-PREVIEW-EXPORT. Scanned/encrypted/protected/fonts/images/layout/unsupported/corrupt/conversion/large/partial. Digital text vs image vs local OCR, no OCR/reliability or perfect conversion assumption. EXACT_REQUIRED/BEST_EFFORT/CONTENT_ONLY proposed pending requirements/feasibility. Originals unchanged, operation-specific evidence.

D maintenance: source import/structure/inventory/broken refs/local links/assets/metadata/structured replacements/templates/config updates/comparison/diff/impact/static validation/passive local preview/package/rollback prep. Stages IMPORT-INSPECT-DEFINE SCOPE-PLAN-PREVIEW-APPLY TO WORKING COPY-VALIDATE-REVIEW-PACKAGE. Isolated copies; no imported scripts/dependencies/build/deploy. Static/CSS-JS/template/framework/server compatibility limits; unsupported explicit.

Shared: input/workspace/config/planning/progress/cancel/log/resources/artifacts/evidence/validation/review/reports/packages/history/backups, clear owners without module coupling.

Reports sections1-16: ID/client-project/objective/authorized scope/input/config/environment/operations/results/findings-validation-evidence/screenshots/limits/human disposition/approval/deliverable inventory. Formats HTML/PDF/CSV/XLSX/JSON/ZIP capability matrix; not all types every format, no unsupported fidelity.

Contracts ExecutionReport, ValidationReport, FindingReport, ReviewRecord, ApprovalRecord, ArtifactManifest, DeliveryPackageManifest: ID/schema/required+optional fields/validation/job-run/artifact refs/integrity/error. PASSED/FAILED/WARNING/INCONCLUSIVE/NOT_RUN distinct; unverified observations not confirmed defects.

Packaging: outputs/QA/confirmed reports/screenshots/evidence/test docs/config+validation summaries/manifest as reviewed selection. Safe names/path/inventory/checksum/collision/sensitive exclusion/preview/approval/version/repackage. Exact approved set; changed/replaced/removed artifacts invalidate relevant approval; no external delivery.

Trace business source -> REQ -> UX -> components -> contract -> pending implementation -> TEST -> evidence -> acceptance. Existing IDs, no duplicates; every major capability requirement/UX/component/test/risk/open-choice map, no completed implementation/test evidence.

Quality: reliability/isolation/retry/recovery/no silent corruption; security/least privilege/files/inputs/network/secrets; maintainability/boundaries/version/error/code/dependencies; testable pure/mocked/contracts/fixtures/integration; bounded resources/UI/concurrency/file processing/workloads; accessible keyboard/semantics/errors/focus/status; persistent/restart/temp/integrity-restore recovery. Numeric targets PROPOSED.

Gates A requirements coverage/scope/criteria; B contracts/consistency/security/recovery; C future unit/contract/module/invalid; D future end-to-end/isolation/integrity/recovery/approval; E future Windows/install/offline/security/performance/backup/deliverable. P3 only documentary checks executed.

Risk-based tests: changed then affected shared/module contracts/target integration/full regression at checkpoints; no expensive unjustified reruns; valid prior evidence reused, relevant material changes rerun; honest skips/blocks; actual Windows release proof; high-risk stronger checks.

Planned scenarios: A valid merge/invalid schema/duplicates/no loss/corrupt/large/cancel/reconcile; B authorized/unauthorized/redirect/link/fail/browser crash/network loss/evidence/human confirmation; C merge/corrupt/encrypted/unsupported/fidelity/partial/verify; D import/unsupported framework/unsafe scripts/controlled change/diff/validation fail/original/rollback; shared interrupt/restart/DB/disk/full/artifact change/stale approval/unauthorized/offline/export. Existing TEST reuse, new IDs only register-check, none executed.

Fixtures synthetic clients/generated spreadsheets/sample PDFs/local sites/controlled browser/corrupt/boundary; no confidential files/real credentials/personal data, reproducible generation plan. Designs/contracts/reports/approval/requirements/security/candidates/errors/tests/diagrams consistent; no duplicate policy or unsupported promises. Place module/shared/report/package/trace/quality/risk docs in existing hierarchy. Acceptance requires four boundaries/contracts/failure/security/review/report/package/trace/positive-negative-boundary-recovery and honest unrun evidence; remaining feasibility/business OPEN.

## Block5 — Execution, evidence, gates and handoff (duplicate consolidated)
Only inspection/P2 verify+reconcile/architecture/detail/technology/security/proposed ADR/trace/risk/document checks/report/next prompt. No code/prototypes/install/adoption/commit/push/merge/deploy/other repo/P4/P5. First checkpoint reads all relevant books/P1/P2 matrices/screens/workflows/architecture/ADRs/execution/report, branch/HEAD/status/uncommitted/all registers/open risks/owner decisions.

P2 reproduce inventory/20 screens/12 steps/8 flows/4 modules/14 failures/91 dispositions/46 new cases/original cases intact/all NOT_RUN/links/IDs/scope. Fail means no P3 or P2 completion, precise blocker/one P2 recovery/stop. Pass means dated referenced limited owner approval, P2 APPROVED then COMPLETED, P3 IN_PROGRESS. Limits: documentary completeness only, no technical/feasibility approval.

Required controlled sections A-X: principles/alternatives; context/components; layers/dependencies; shared services; module contracts; orchestration/states; worker lifecycle/protocol; DB/persistence; files/artifacts; security/trust; privacy/offline; authorized network; technology/dependencies; Windows; spreadsheet; QA; PDF/documents; maintenance; reports/packages; errors/cancel/recovery; review/approval; ADRs; trace; verification/risks. Document blocker/impact if any section incomplete, never omit.

Architecture book remains authoritative; detail specs under docs/specifications, ADRs under docs/adr. Each ADR ID/title/status/context/problem/requirements/alternatives/criteria/evidence/proposal/rationale/consequences/risks/prerequisites/owner approval; only PROPOSED/CONDITIONAL/BLOCKED as honest; unknown OS/version/license pending. No invented final architecture.

Windows safeguard: Tauri/Electron/Playwright/Chromium/Node/Python/Rust/WebView2/installers cannot be assumed to support owner machine. Separate verified source/conditional/unsupported/missing/local proof; exact laptop info needed, no install/Windows testing/compatibility claim. Plan P5.

Both P1/P2 matrices: preserve content/IDs, each applicable REQ/NFR architecture/component/contract/pending implementation/planned verification/risk-decision; runtime/release pending, no invented PASSED/evidence.

Risks assessed: hostile files, unsafe exec/files/traversal/crash/DB/data/resource/network/approval/export/log/licenses/Windows/offline. Each ID/description/probability/impact/mitigation/exposure/owner/stage/status; design does not close risk.

25 documentary checks: inventory; completeness; module contracts; dependency direction; lifecycle; DB relationships; worker protocol; security; originals; provenance; approval split; recovery; reports; four modules; REQ-design; UX compatibility; ADR uniqueness; REQ uniqueness; TEST consistency; references; heading/links; unsupported claims; license+support evidence; whitespace; Git scope. Actual PASS/FAIL/SKIPPED/BLOCKED/NOT_RUN; separate from application/PoC/Windows/Playwright/performance/security/installer tests, all those NOT_RUN. Never production-ready claim.

Independent A-Z acceptance: core description, component responsibility, dependencies, module interfaces, worker protocol, lifecycle, DB logical model, files, integrity, review, invalidation, report/export, recovery, security, offline, target authorization, alternatives, license investigation, Windows evidence vs proof, four modules, trace, UX consistency, proposed ADRs, decisions, checks, Git scope. Documentary pass permits READY_FOR_REVIEW only; no forced PASS missing evidence, no APPROVED/COMPLETED without human approval; unmet required scope BLOCKED precise cause.

Report docs/milestone-reports/MS-0004-P3.md: ID/objective/scope/start/P2 verification/changes/deliverables/coverage/decisions/ADRs/technology/licenses/Windows/security/privacy/recovery/checks/acceptance/open choices/risks/limits/finalstatus/approval. Execution book records approval/start/progress/deliverables/results/risks/gate/one next action.

Archive whole consumed task per existing convention, preserve substantive all five blocks, do not imply unexecuted work complete. Exactly one current next prompt: if READY_FOR_REVIEW P4 Development Standards and Code Organization gated explicit P3 approval and P4 authorization, documentation-only; conventions/layout/modules/names/dependencies/interface versions/errors/logs/tests/fixtures/config/security/review/gates/build-packaging/docs/Git/milestones. If BLOCKED targeted P3 recovery, not P4.

Next prompt complete/self-contained/copy-paste/repository-specific/one milestone, with role/context/checkpoint/approval/reads/scope/deliverables/constraints/verification/acceptance/finalreport/nextgate; save docs/prompts/current-next-prompt.md, no execute. Preserve Git history/uncommitted docs/no branch/worktree/discard/delete/commit/push/merge/deploy; uncommitted persistence risk and reviewed checkpoint recommended before executable work, separate permission.

Final exact response structure A baseline(branch/HEAD/start/uncommitted); B P2 evidence/approval/status; C updated/created/preserved; D components/contracts/workers/states/DB-artifacts/approval-recovery; E candidates/rejected/conditional/licenses/Windows; F boundaries/safeguards/data/offline/residual; G REQ/UX/tests/deferred; H doc checks/fail/skip/runtime NOT_RUN; I owner/architecture/compatibility/PoC choices; J A-Z checklist/status/approval; K one next step; L next prompt location/text or concise reference. Final stop: no P4/P5/software/install/commit/push/merge/deploy/ADR autoapprove/unrun PASS; await human review.
