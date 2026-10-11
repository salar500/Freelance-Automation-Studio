# Architecture book

Status: P3 PROPOSED documentary baseline, 2026-10-11. Owner conditionally approved P2 documentary completeness only. No technology/architecture ADR adopted, unresolved requirement finalized or runtime feasibility verified. [Master policies](00-master-rulebook.md) and [requirements](01-requirements-book.md) remain authoritative; architecture details below are proposals that require gate approval and evidence before implementation.

## Architectural direction
Evaluate a local modular monolith with shared application/domain services and isolated risky-operation workers. UI issues typed use-case commands, never arbitrary OS commands. Single application persistence owner, controlled local artifact workspaces, immutable versions/attempts and explicit review/approval/export dimensions support recovery and traceability. Alternative all-in-process design has lower overhead with weaker fault containment; services/distributed brokers/cloud backend conflict with initial scope and add unnecessary dependencies. Choice remains ADR-0001 PROPOSED, not proven performance/security.

## Controlled sections A through X
Each section has detailed ownership in the linked specification; this book owns overall rationale and decision register. Do not create competing governance books or copy permanent policies into every specification. Conditional support/missing evidence is not silently called an implemented capability.
| Section | Scope | Authoritative detailed reference |
| --- | --- | --- |
| A | Architecture principles and alternatives | [Architecture principles and alternatives](../specifications/P3-system-components.md) |
| B | System context and component boundaries | [System context and component boundaries](../specifications/P3-system-components.md) |
| C | Layers and dependency direction | [Layers and dependency direction](../specifications/P3-system-components.md) |
| D | Shared services | [Shared services](../specifications/P3-system-components.md) |
| E | Module contracts | [Module contracts](../specifications/P3-module-contracts.md) |
| F | Job orchestration and lifecycle | [Job orchestration and lifecycle](../specifications/P3-job-worker-protocol.md) |
| G | Worker lifecycle and communication | [Worker lifecycle and communication](../specifications/P3-job-worker-protocol.md) |
| H | Local database and persistence | [Local database and persistence](../specifications/P3-persistence-artifacts.md) |
| I | Filesystem and artifacts | [Filesystem and artifacts](../specifications/P3-persistence-artifacts.md) |
| J | Security and trust boundaries | [Security and trust boundaries](../specifications/P3-security-offline-network.md) |
| K | Privacy and offline execution | [Privacy and offline execution](../specifications/P3-security-offline-network.md) |
| L | Authorized website networking | [Authorized website networking](../specifications/P3-security-offline-network.md) |
| M | Technology/dependency evaluation | [Technology/dependency evaluation](../specifications/P3-technology-evaluation.md) |
| N | Windows compatibility | [Windows compatibility](../specifications/P3-windows-compatibility.md) |
| O | Spreadsheet module | [Spreadsheet module](../specifications/P3-module-designs.md) |
| P | Website QA module | [Website QA module](../specifications/P3-module-designs.md) |
| Q | PDF/documents module | [PDF/documents module](../specifications/P3-module-designs.md) |
| R | Website maintenance module | [Website maintenance module](../specifications/P3-module-designs.md) |
| S | Reporting and packaging | [Reporting and packaging](../specifications/P3-reporting-packaging.md) |
| T | Errors/cancellation/recovery | [Errors/cancellation/recovery](../specifications/P3-recovery-approval.md) |
| U | Human review and approval | [Human review and approval](../specifications/P3-recovery-approval.md) |
| V | Proposed ADRs | [Proposed ADRs](../adr/README.md) |
| W | Requirement/UX traceability | [Requirement/UX traceability](../test-matrix/P3-architecture-coverage.md) |
| X | Verification/risk assessment | [Verification/risk assessment](../specifications/P3-quality-verification.md) |

## Open architecture decisions
| Key | OPEN question / limitation | Owner and gate |
| --- | --- | --- |
| ARCH-O01 | Exact target Windows edition/build/architecture cannot be obtained from cloud terminal; current .NET/Playwright support cannot be assumed | Owner target facts; P3 adoption review/P5 actual Windows proof |
| ARCH-O02 | Exact runtime/library/provider/browser/installer release tags, transitive licenses and redistribution terms not fully pinned | Architecture/license lead before technology approval |
| ARCH-O03 | Hard worker file/network confinement with standard-user permissions unverified; process/Job Objects not sandbox proof | Security/OS lead, P5/P12 |
| ARCH-O04 | All browser traffic paths/redirect/DNS/TLS enforcement and supported Win10 browser alternative unresolved | QA/security lead, P5 before live capability |
| ARCH-O05 | SQLite mode/durability, cross-store intent/rename/flush/backup recovery performance unmeasured | Persistence lead, P5/P11 |
| ARCH-O06 | Block4 extensions (fuzzy duplicates/split/discovery/console/trace/conversion/impact/preview) need detailed requirements/profile disposition | Owner requirement change gate; module P5/P7-P10 |
| ARCH-O07 | Local reviewer identity, partial-valid-subset delivery and backup/retention/encryption recovery policy still conditional | Owner/security/UX, before affected implementation |
| ARCH-O08 | Fidelity/formula/font/OCR and supported framework profiles not universally known | Owner/module lead, P5 format proof |
| ARCH-O09 | Proposed resource/frame/heartbeat/cancel/storage limits need representative workload and actual target | Owner/QA, P5/P12 |
| ARCH-O10 | All documentation remains uncommitted; reviewed Git checkpoint needed before executable development, explicitly authorized separately | Owner, before P5 executable work; no commit authorized now |

SRS O-01 through O-09 and UX-O01 through UX-O05 remain unchanged at their authoritative homes. These architecture questions identify additional evidence/disposition needs; they do not replace or settle the earlier registers. Source-host 403/404 limits are documented in the technology evidence register. License/support investigation is performed; binary/transitive/adoption clearance and local tests remain pending.

## ADR inventory
- [ADR-0001 — Modular monolith with isolated execution adapters](../adr/ADR-0001-modular-platform.md): PROPOSED.
- [ADR-0002 — Conditional desktop stack candidate](../adr/ADR-0002-desktop-stack.md): PROPOSED.
- [ADR-0003 — SQLite candidate and single durable writer](../adr/ADR-0003-local-persistence.md): PROPOSED.
- [ADR-0004 — Versioned local IPC and bounded workers](../adr/ADR-0004-worker-boundaries.md): PROPOSED.
- [ADR-0005 — Recoverable database/filesystem publication](../adr/ADR-0005-artifact-finalization.md): PROPOSED.
- [ADR-0006 — Conditional supported browser automation and strict scope](../adr/ADR-0006-authorized-browser.md): PROPOSED.
- [ADR-0007 — Explicit format, formula and fidelity profiles](../adr/ADR-0007-document-profiles.md): PROPOSED.
- [ADR-0008 — Approval-bound manifests and local package attestation](../adr/ADR-0008-approval-package-scope.md): PROPOSED.

## Book acceptance and gate
All A-X areas have complete conditional specifications, acyclic component boundaries, standardized module/protocol/entity/report contracts, explicit state/approval separation, recoverable artifact/DB design, threat/permission/offline/network controls, supported-vs-unknown evidence and future verification. All 91 REQ/NFR IDs have architectural dispositions and preserved downstream pending status. Actual results and A-Z acceptance are in [P3 report](../milestone-reports/MS-0004-P3.md); [execution](09-execution-book.md) owns milestone state. Documentary READY_FOR_REVIEW does not approve any ADR, production readiness or feasibility. P4/P5 may not start automatically.
