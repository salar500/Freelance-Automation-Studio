# Master rulebook

Status: P0 governance baseline approved by the project owner on 2026-10-11 after repository verification. No technology or detailed design is approved by this document.

## Product and authority
Freelance Automation Studio is a standalone Windows desktop application that reduces repetitive freelance work. Initial categories are spreadsheet/CSV automation, website QA/regression, PDF/document automation, and website maintenance/template development. Future modules must be independently extendable. Detailed workflows and requirements belong to P1.

This book owns durable policy, lifecycle gates and traceability conventions. [AGENTS.md](../../AGENTS.md) owns Codex task operation; [execution](09-execution-book.md) owns live milestone state. Each other book owns its named discipline; reference policy here instead of duplicating it. Approved decisions are preserved in ADRs. A specific user authorization is required to change a permanent constraint; an ADR cannot silently override it.

## Enforceable policies
| Policy | Rule | Required evidence / gate |
| --- | --- | --- |
| GOV-01 Scope | Implement only approved requirements within the active phase and four initial categories. | Change list maps to authorized requirements and milestone. |
| GOV-02 Local first | No cloud backend/database, paid APIs, subscriptions or external authentication required to run the product. Local jobs must work without mandatory internet. | Architecture dependency review and offline local-job tests before release. |
| GOV-03 No runtime AI | Codex and other AI may assist development only. Completed software must run without ChatGPT, Codex, Claude, Gemini or external AI services. | Source/dependency/network review and functional tests with AI services unavailable. |
| GOV-04 Client privacy | Client inputs, derived data and reports remain local; no telemetry or uploads of client data. Website requests must be limited to authorized targets and necessary test data with explicit authorization. | Data-flow review, network observation and log/export inspection. |
| GOV-05 Original preservation | Preserve original files by default; write outputs separately. Overwrite, delete or irreversible modification needs explicit human confirmation and recovery planning. | Input hashes before/after ordinary jobs; confirmation and recovery tests for destructive paths. |
| GOV-06 Reliable automation | Prefer deterministic operations; every execution produces a verifiable result with job identity, inputs, operation/configuration, outcomes and evidence references. Never label uncertain output successful. | Reproducibility checks, failure cases and independently inspectable job reports. |
| GOV-07 Human verification | Uncertain results, destructive actions and final client delivery require recorded human review. No automatic client delivery without approval. | Review/confirmation flow tests including rejection and cancellation. |
| GOV-08 Modular design | Modules have documented boundaries and stable contracts; no unnecessary frameworks, microservices, network services or runtime dependencies. | Design review and representative module isolation tests. |
| GOV-09 Dependency selection | Use free/open-source technologies with licenses suitable for intended distribution/use. Verify maintained versions, provenance, license obligations and Windows 10 compatibility before selection. | Dependency assessment, license inventory and approved ADR; unresolved license/compatibility issues block adoption. |
| GOV-10 Coding quality | Follow approved development standards, review changes, keep code readable and validate inputs at boundaries. Do not suppress failures to pass checks. | Review, relevant static checks and tests defined in the development/testing books. |
| GOV-11 Error and recovery | Handle errors explicitly, log safely, distinguish partial failure, cancellation and success, and provide tested recovery for interrupted jobs. | Fault injection and recovery tests; logs exclude secrets and unnecessary client content. |
| GOV-12 Testing | Test throughout all phases using risk-based checks. Maintain requirement/design/test/evidence links. Report failed, skipped, blocked and unrun checks separately. | Current test matrix and execution evidence at every gate. |
| GOV-13 Version control | Preserve unrelated work and approved history. Commit/push/merge/deploy require explicit authorization. | Pre/post Git status and reviewed change scope; no automatic repository operations at gates. |
| GOV-14 Documentation | One authoritative home per policy; update affected books and traceability with approved changes; preserve rationale and history. | Link/consistency review and change impact record. |
| GOV-15 Security/access | Apply least privilege, safe path/file handling, explicit target authorization and appropriate access controls without mandatory external authentication. No unauthorized Fiverr or freelance-platform automation. | Threat review, negative authorization/path tests and target scope records. |
| GOV-16 Release | No release without approved acceptance evidence, resolved release blockers, installer checks and explicit release approval. | Release checklist, versioned evidence and approval record. |
| GOV-17 Performance | Measure representative workloads; set budgets in P1/P3 rather than inventing limits. Avoid unnecessary resource use. | Agreed budgets and measured results with environment/workload details. |
| GOV-18 Windows | Windows 10 is the initial target. Verify exact supported edition/build/architecture and tools before selection; Linux/cloud checks alone do not prove Windows support. | Authoritative support references plus actual Windows validation; unresolved target support blocks compatibility claims. |
| GOV-19 Change control | Proposed policy/scope/architecture changes record rationale, affected requirements/design/tests, risks and approval before adoption. | Reviewed change record and ADR for significant design changes; prior approved decision retained and marked superseded. |

## Authority map and book acceptance
| Book | Authoritative purpose | Acceptance for this P0 baseline |
| --- | --- | --- |
| [Requirements](01-requirements-book.md) | Requirement catalog, scope and acceptance definitions | ID/status/traceability rules and P1 work boundary defined. |
| [UX](02-ux-design-book.md) | User flows, interaction design and human-review experience | P2 inputs, outputs and review criteria defined without finalized UI. |
| [Architecture](03-architecture-book.md) | Module contracts, data flows and technical decisions | P3 decision process and compatibility evidence needs defined. |
| [Development](04-development-book.md) | Implementation and review standards | P4 standards agenda and enforcement gates defined. |
| [Code organization](05-code-organization-book.md) | Source layout and ownership boundaries | P4 organization criteria defined without invented code layout. |
| [Testing](06-testing-book.md) | Test strategy, outcomes and evidence | Continuous checks, result vocabulary and traceability defined. |
| [Security](07-security-book.md) | Threats, controls and security validation | Assessment scope, authorization and privacy criteria defined. |
| [Release](08-release-book.md) | Packaging, distribution and maintenance approval | Windows release evidence and approval criteria defined. |
| [Execution](09-execution-book.md) | Current milestone, gate status and handoff | Status transitions, approval rules and actual P0 record present. |

## Traceability and identifiers
Use zero-padded, monotonically allocated four-digit identifiers; never reuse or renumber an assigned identifier. Separate namespaces: `REQ-XXXX` functional requirements, `NFR-XXXX` nonfunctional requirements, `ADR-XXXX` decisions, `RISK-XXXX` risks, `TEST-XXXX` tests and `MS-XXXX` milestones. P0-P14 are phase labels, not identifiers. Next numbers are derived from the authoritative register, never guessed from filenames. Concurrent edits must recheck uniqueness.

Requirements are allocated in the requirements book, ADRs in `docs/adr`, risks in the execution book, tests in `docs/test-matrix`, and milestones in the execution book. Check for equivalent entries before allocation; consolidate overlaps by reference and preserve retired identifiers with rationale. Conflicts block affected work pending review.

Trace chain: requirement -> design reference (specification section and/or ADR) -> implementation reference -> TEST identifier -> acceptance evidence (milestone report with command/run/environment/results) -> approval. Use `pending: <reason>` where a phase has not produced a link; never fabricate implementation or tests. Traceability review must find orphaned requirements, unsupported implementations, missing tests and stale evidence.

## Hybrid Agile / stage gates
Small iterative work is allowed within an authorized phase; advancement requires the gate. Each milestone records objective, prerequisites, scope, deliverables, acceptance criteria, required checks, risks, completion evidence, approval gate and one next recommended action. Testing is continuous, not deferred to P11.

| Phase / milestone | Objective and scope / deliverables | Prerequisites | Acceptance and required checks | Risks | Evidence / approval gate / next action |
| --- | --- | --- | --- | --- | --- |
| P0 / MS-0001 | Governance books, agent rules, registers and handoff | Repository inspection and user constraints | Documents complete, links valid, policies consistent, no feature changes | RISK-0004 | P0 report; human approval; authorize P1 |
| P1 / MS-0002 | Requirements and prioritized workflows, measurable acceptance, trace matrix | Approved P0 and P1 authorization | Scope, offline/network boundaries, failure/review cases and NFRs reviewed; ambiguity and duplication checks | RISK-0001, RISK-0003 | Requirement review report; human approval; authorize P2 |
| P2 / MS-0003 | UX flows, wireframes and review/recovery interactions | Approved P1 and P2 authorization | Requirements covered; usability/accessibility, error and review-flow checks | RISK-0002 | UX review evidence; human approval; authorize P3 |
| P3 / MS-0004 | Architecture, contracts, data flows, candidate assessment and ADRs | Approved P2 and P3 authorization | Trace coverage, threat review, licenses and Windows support assessment; unknowns explicit | RISK-0001, RISK-0003 | Architecture review/decision records; human approval; authorize P4 |
| P4 / MS-0005 | Development standards and code organization | Approved P3 and P4 authorization | Standards enforceable; boundaries and tooling checks specified | RISK-0004 | Standards review; human approval; authorize P5 |
| P5 / MS-0006 | Minimal technical PoC of approved high-risk choices | Approved P4 and P5 authorization | Representative feasibility, Windows and offline checks executed; failures diagnosed | RISK-0001, RISK-0003 | PoC measurements/test report; human approval; authorize P6 |
| P6 / MS-0007 | Desktop foundation, job lifecycle and module integration contracts | Approved P5 and P6 authorization | Startup, offline behavior, lifecycle, errors and recovery tests pass | RISK-0002 | Foundation build/test report; human approval; authorize P7 |
| P7 / MS-0008 | Spreadsheet/CSV module | Approved P6 and P7 authorization | Approved requirements; format, preservation, malformed input and determinism tests | RISK-0002 | Module trace/test report; human approval; authorize P8 |
| P8 / MS-0009 | Website QA/regression module | Approved P7 and P8 authorization | Authorized targets, scope controls, reproducible reports and failure tests | RISK-0003 | Module trace/test/authorization evidence; human approval; authorize P9 |
| P9 / MS-0010 | PDF/document module | Approved P8 and P9 authorization | Approved formats, fidelity, invalid input, preservation and review tests | RISK-0002 | Module trace/test report; human approval; authorize P10 |
| P10 / MS-0011 | Maintenance/template development module | Approved P9 and P10 authorization | Authorized change scope, preview/review, backup/recovery and regression checks | RISK-0002, RISK-0003 | Module trace/test report; human approval; authorize P11 |
| P11 / MS-0012 | Integration and comprehensive verification | Approved P10 and P11 authorization | End-to-end trace coverage, regression, offline, compatibility and recovery checks | RISK-0001, RISK-0002 | System test report; human approval; authorize P12 |
| P12 / MS-0013 | Security/performance/reliability hardening | Approved P11 and P12 authorization | Threat controls, agreed resource budgets and interruption/stress checks | RISK-0002, RISK-0003 | Hardening evidence and risk dispositions; human approval; authorize P13 |
| P13 / MS-0014 | Windows installer and release | Approved P12 and P13 authorization | Clean install/upgrade/uninstall, offline packaged jobs, license notices and release checks | RISK-0001, RISK-0003 | Release dossier; explicit human release approval; authorize P14 |
| P14 / MS-0015 | Maintenance and independently extendable future modules | Approved P13 and specific maintenance authorization | Change impact, regressions, migration/recovery and release checks per approved change | RISK-0004 | Maintenance report; human approval per change; propose next scoped maintenance task |

The execution book records current milestone statuses; this table defines gate expectations, not authorization or completed evidence. Concrete checks and budgets are refined in their responsible approved phases.

## Change record
P0 initial baseline prepared from the user's brief. No historical approved technical decisions exist. On approval record approver, date, authorized scope and evidence reference in execution state. Subsequent significant changes need an impact record and explicit decision; do not erase prior approval evidence.

P0 approval reconciled on 2026-10-11: owner decision in the P1 authorization message, conditional on repository verification; verification passed with the original 19-file/51-reference evidence. MS-0001 closed in the execution book. No permanent policy changed.
