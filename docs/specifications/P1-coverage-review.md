# P1 coverage and consistency review

Document review only, 2026-10-11. No product tests executed. [SRS](../governance/01-requirements-book.md) owns requirements; [matrix](../test-matrix/P1-requirements-matrix.md) owns defined tests. This document records coverage mapping and review rationale, not duplicate policy.

## Requested functional areas
| Area | Requirement IDs |
| --- | --- |
| Desktop navigation | REQ-0001 |
| Clients and projects | REQ-0002, REQ-0003 |
| Job creation/configuration, import, module selection, templates | REQ-0004 through REQ-0007 |
| Validation and execution planning | REQ-0008, REQ-0009, REQ-0032 |
| Automated processing and progress | REQ-0011, REQ-0012, REQ-0029 |
| Cancellation, errors, recovery and retry | REQ-0013 through REQ-0016 |
| Evidence and output validation | REQ-0017, REQ-0018 |
| Human review and approval workflow | REQ-0010, REQ-0019, REQ-0020, REQ-0031 |
| Reports, packaging, export and history | REQ-0021 through REQ-0024 |
| Settings and local data management | REQ-0025, REQ-0026 |
| Offline/network authorization and privacy | REQ-0027, REQ-0028, REQ-0030 |
| Spreadsheet/CSV | REQ-0033 through REQ-0041 (9) |
| Website QA/regression | REQ-0042 through REQ-0050 (9) |
| PDF/documents | REQ-0051 through REQ-0059 (9) |
| Maintenance/templates | REQ-0060 through REQ-0067 (8) |

Shared core requirements apply to each module; category entries do not redefine approvals, retries or history.

## Requested quality areas
Performance NFR-0001/0002; reliability 0003; security 0004/0023; privacy 0005; offline 0006; usability 0007; accessibility 0008; maintainability 0009; modularity 0010; recoverability 0011; integrity 0012; resources 0013/0024; Windows 0014; installation/upgrades 0015/0016; testability 0017; auditability 0018. Additional explicit policy assurance: determinism 0019, licenses/dependencies 0020, no runtime AI 0021, safe recovery logging 0022. All numbers here have NFR prefix and resolve to the SRS.

## Permanent-constraint assurance mapping
This maps the owner's 18 original constraints without copying policy statements.
| Owner constraint | Requirement / governance assurance |
| --- | --- |
| 1 | AGENTS workflow and GOV-03; NFR-0021 runtime boundary |
| 2 | NFR-0021 |
| 3 | NFR-0020, NFR-0015 |
| 4 | NFR-0015, GOV-02 |
| 5 | REQ-0027, NFR-0006 |
| 6 | NFR-0015, NFR-0006 |
| 7 | REQ-0030, NFR-0005 |
| 8 | NFR-0020 |
| 9 | NFR-0014; O-01 |
| 10 | NFR-0004, NFR-0009, NFR-0010, NFR-0017 |
| 11 | NFR-0019; module transformation requirements |
| 12 | REQ-0010, REQ-0019, REQ-0020 |
| 13 | REQ-0017, REQ-0018, NFR-0018 |
| 14 | NFR-0012, REQ-0065 |
| 15 | REQ-0014 through REQ-0017, NFR-0011, NFR-0022 |
| 16 | REQ-0067 and GOV-15 exclusions; unauthorized-target tests |
| 17 | REQ-0028, REQ-0042, NFR-0023 |
| 18 | NFR-0010, NFR-0013, GOV-08/09; P3 adoption gate |

## Governance policy coverage
| Policy IDs | Product or process evidence |
| --- | --- |
| GOV-01 | Four-category SRS scope and this functional map |
| GOV-02 | NFR-0006/0015; REQ-0027 |
| GOV-03 | NFR-0021 |
| GOV-04 | REQ-0030; NFR-0005 |
| GOV-05 | NFR-0012; REQ-0010/0065 |
| GOV-06 | REQ-0017/0018; NFR-0019 |
| GOV-07 | REQ-0010/0019/0020/0031 |
| GOV-08 | NFR-0010; final boundaries pending P3 |
| GOV-09 | NFR-0020; adoption evidence pending P3/P5 |
| GOV-10 | NFR-0009; language-specific checks pending P4 |
| GOV-11 | REQ-0014/0016; NFR-0022 |
| GOV-12 | NFR-0017 and 182 defined acceptance cases |
| GOV-13 | P1 baseline hashes and Git scope verification |
| GOV-14 | Single SRS catalog and linked matrix; verified references |
| GOV-15 | REQ-0028/0060/0067; NFR-0004/0023 |
| GOV-16 | NFR-0015/0016; release approval still governed by release book |
| GOV-17 | NFR-0001/0002/0013/0024, provisional WP-1 |
| GOV-18 | NFR-0014 and unresolved O-01 |
| GOV-19 | Proposed requirements state, P0 approval reconciliation and preserved history |

## Duplicate and contradiction review
No duplicate IDs or identical catalog statements. Related requirements have distinct observable responsibilities: plan confirmation is not destructive consent; processing success is not output validation or delivery approval; failure retry creates a new attempt while recovery first discovers interruption; website findings do not establish desktop accessibility. Shared workflow governs modules rather than being replicated.

Local-only privacy permits requests only for authorized website testing with synthetic data; it does not permit client-file upload. Export/packaging is a local operation, not automatic delivery. Ordinary-job original preservation is distinct from separately confirmed in-place maintenance with verified backup. Determinism is normalized local content, not identical timestamp metadata or time-varying live websites. XLSX/PDF/DOCX proposals do not promise unsupported fidelity, OCR, signature preservation or macro execution. Automated website accessibility checks are not whole-site conformance certification.

Atomicity review treats one independently reviewable capability/property per requirement. Its success, rejection and boundary assertions belong to that capability rather than becoming competing duplicate requirements. Composite workflows are assembled from these requirements. Detailed feature profiles and feasibility remain O-01 through O-09, explicitly pending review/architecture; no requirement is claimed implemented or verified.

## Coverage outcome
91/91 requirements have metadata, observable nominal/adverse criteria and matrix rows; 182/182 tests have defined procedures/expected behavior and NOT_RUN status. All requested scenario classes are represented. Design, implementation and product acceptance evidence are explicitly pending. Documentary coverage is complete for review; runtime and feasibility coverage is not yet executed.
