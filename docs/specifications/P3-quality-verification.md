# P3 quality attributes, gates and future verification

Status: proposed verification strategy, not runtime results. [Testing book](../governance/06-testing-book.md) owns result semantics; [requirements](../governance/01-requirements-book.md) own numeric NFR targets and WP-1. No benchmark or participant/Windows study executed. [Trace/test register](../test-matrix/P3-architecture-coverage.md) defines 11 new cases in addition to existing 228; all NOT_RUN. [P3 report](../milestone-reports/MS-0004-P3.md) owns actual documentary checks.

## Measurable architectural assurance
| Attribute | Acceptance measure / planned method | State |
| --- | --- | --- |
| Reliability | Zero silent dropped items/false success in declared fault suite; bounded retries, truthful phases and reconciled per-item counts | NOT_RUN; NFR-0003 |
| Security/privacy | Zero forbidden effects/requests in scope/path/macro/script/canary suite; prove effective least privilege and redaction | NOT_RUN; NFR-0004/0005/0023 |
| Maintainability/modularity | 100% component/interface ownership/version trace; no cycle in declared dependencies; representative extension leaves unrelated module internals unchanged | Documentation DAG checked in P3; executable extension NOT_RUN; NFR-0009/0010 |
| Testability | Every one of 91 REQ/NFR has defined planned tests and injectable typed boundaries; deterministic synthetic fixtures with explicit versions | Documentary mapping only; execution NOT_RUN; NFR-0017 |
| Performance/resources | Measure owner-dispositioned WP-1 response/CSV/memory/CPU budgets, bounded concurrency/frame/input/expanded bytes/deadlines | Numeric targets PROPOSED, not measured; NFR-0001/0002/0013/0024 |
| Accessibility | Essential keyboard/semantic status/focus/error flows, proposed contrast/scaling in P2, real Windows assistive-tool proof | Documentary alignment only; NOT_RUN; NFR-0008 |
| Recoverability/integrity | Original hashes unchanged; restart/backup/restore/publication interruptions reconcile 100% declared cases without false approval | NOT_RUN; NFR-0011/0012/0016/0018 |
| Offline/Windows/licensing | Offline local paths with no sign-in/AI/network license; exact supported OS and version/transitive obligations documented before adoption | Source investigation performed; runtime/licensing clearance pending; NFR-0006/0014/0015/0020/0021 |

## Gates A through E
| Gate | Required evidence | Phase / permitted executed scope |
| --- | --- | --- |
| A Requirements | Scope, clear acceptance, uniqueness/coverage, owner dispositions for unknowns/extensions | P1/P3 document review; no finalization of unresolved requirements |
| B Design | Contracts/DAG/entities/protocol/state/artifacts/security/recovery/UX/ADR/support evidence consistency | P3 document checks only; missing adoption facts explicit |
| C Module implementation | Unit, version/schema contract, module integration, malformed/boundary/fidelity/security tests with counts/results | Future P5/P7-P10; NOT_RUN |
| D System integration | End-to-end workflows, isolation, state races, data/approval boundaries, restart/backup/restore | Future P11/P12; NOT_RUN |
| E Release | Exact Windows/install/upgrade/offline/security/resources/backup and reviewed deliverable/license inventory | Future P13 explicit release approval; NOT_RUN |

## Risk-based execution strategy
When executable work is authorized: test changed component first, then affected shared contracts/dependencies, then module contract and targeted integration; full regression at major checkpoints. Reuse prior evidence only for identical relevant implementation/config/input/tool/OS versions and unexpired scope. Rerun materially changed/dependent cases; preserve old evidence as historical, not fresh proof. Avoid repeating expensive unchanged suites without risk justification. Report failed/expected-failed/skipped/blocked/unrun distinctly, with actual counts. High-risk destructive/network/path/fidelity/publication/approval operations receive stronger fault/adversarial tests than low-impact formatting. Real target Windows validation precedes release.

## Safe future fixtures
Synthetic clients/projects; generated deterministic CSV/XLSX with types/encodings/formula canaries; sample/generated PDF/DOCX with page/order/placeholder/scan-like content; licensed local HTML/CSS/JS fixtures; controlled authorized browser sites with redirects/resources/form state; deliberately corrupted, nested/high-ratio or boundary-size files under safe quotas. No confidential client originals, real personal information or actual credentials committed. Generation plan records seed/spec/version/hash/license and expected outcomes, but no executable generators created in P3. Local malicious-content fixtures remain confined and never run arbitrary imported scripts.

## Documentary verification inventory
Required inventory, complete component/module/protocol/entity/report fields, DAG, lifecycle/approval separation, normalized relationships, security boundaries, original/artifact integrity, recovery, all four modules, 91 requirement dispositions, preserved P2 UX/tests, unique ADR/REQ/TEST registers, local heading/link resolution, unsupported-claim review, license/support-source investigation, Markdown whitespace and Git/hash scope. Each result independently recorded in the milestone report; semantic review is not replaced by a file-count checker. Mermaid source is checked for referenced names/relationships but no renderer installed, so rendered layout/syntax proof remains NOT_RUN.
