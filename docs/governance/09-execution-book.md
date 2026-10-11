# Execution book

Owns live milestone state, risk register, approvals and handoff. Durable policies and phase definitions live in [the master rulebook](00-master-rulebook.md).

## Status model
PROPOSED -> READY: prerequisites satisfied and explicit authorization recorded.
READY -> IN_PROGRESS: authorized work starts.
IN_PROGRESS -> BLOCKED: a prerequisite or unresolved gate-critical issue prevents progress.
BLOCKED -> READY: blocker resolved, prerequisites rechecked and authorization remains valid.
IN_PROGRESS -> READY_FOR_REVIEW: scoped deliverables and required checks complete with evidence.
READY_FOR_REVIEW -> IN_PROGRESS: reviewer requests scoped corrections under existing authorization.
READY_FOR_REVIEW -> BLOCKED: review identifies a prerequisite or gate-critical issue.
READY_FOR_REVIEW -> APPROVED: human approval recorded with identity/reference, date and evidence.
APPROVED -> COMPLETED: approval covers the deliverables and final record/handoff is reconciled; record closure evidence.
APPROVED -> IN_PROGRESS: approval withdrawn or changed scope explicitly authorized; preserve prior approval history.
COMPLETED is terminal; new changes use a new milestone/change record. Approval alone never starts the next phase. Rejected proposals remain PROPOSED with the rejection recorded; no implied authorization.

## Approval history and P1 initialization
2026-10-11, project owner: P0 approved in the user message headed “PHASE: P1 — REQUIREMENTS ENGINEERING / OWNER DECISION”, conditional on repository verification; P1 documentation-only work authorized. Verified original P0 evidence: 19 Markdown files, 51 valid local references, required books, 15 phase gates, 19 policies, 18 new documentation files, no tracked modifications and one current prompt. No condition failed.

MS-0001: READY_FOR_REVIEW -> APPROVED -> COMPLETED. Closure evidence: original P0 report plus the checkpoint/approval reconciliation in the P1 report. Historical P0 findings retained.
MS-0002: PROPOSED -> READY (P0 verified/closed; explicit P1 authorization) -> IN_PROGRESS. Scope: requirements catalog, traceability, review evidence and handoff only.

## P1 conditional approval and P2 initialization
2026-10-11, project owner, user message “PHASE P2 — UX AND INTERFACE DESIGN / OWNER AUTHORIZATION”: conditionally approves the P1 documentation baseline subject to repository verification and authorizes P2 documentation-only. Original P1 checkpoint reproduced all reported counts: 23 Markdown files, 608 links, 364 anchors, 67 REQ, 24 NFR, 91 matrix rows, 182 NOT_RUN cases, six risks, eight changed/four added documents and exact prompt archive. Verification condition satisfied.

MS-0002: READY_FOR_REVIEW -> APPROVED -> COMPLETED for documentation baseline/handoff only. This approval does not approve unresolved requirement details, targets, feasibility, architecture or implementation. All individual SRS entries retain PROPOSED status; O-01 through O-09 remain open. The four-category/core workflow scope is authorized for conditional UX exploration, not implementation or unconditional requirement acceptance. No requirement disposition is inferred.
MS-0003: PROPOSED -> READY (verified baseline and explicit P2 authorization) -> IN_PROGRESS. Scope: UX documentation, trace references, defined review cases and evidence only.

## P2 conditional approval and P3 initialization
2026-10-11, owner user message “PHASE: P3 — SYSTEM ARCHITECTURE AND DETAILED DESIGN”, Blocks 1–5 and final “ALL BLOCKS RECEIVED — BEGIN P3”: conditional P2 documentary approval, subject to verification; P3 documentation-only authorization. Re-executed the P2 checker before changes: 30 Markdown files, 1,284 local links, 920 anchors, 20 screens, 12 wizard steps, eight flows, four modules, 14 failure patterns, 91 requirement dispositions, 46 new cases, 228 NOT_RUN cases, original test definitions intact, eight previous changes/seven additions and preserved unrelated files. Condition satisfied.

MS-0003: READY_FOR_REVIEW -> APPROVED -> COMPLETED for documentation completeness only. Open requirements/UX decisions, architecture, technology adoption and runtime feasibility are not approved. MS-0004: PROPOSED -> READY -> IN_PROGRESS under explicit P3 authorization. Block 3 ends mid-networking section and Block 5 is duplicated in the received instruction; complete networking requirements in Blocks 2/4/5 still govern. No missing text invented.

## P3 conditional approval and P4 initialization
2026-10-11 UTC, project owner: P4 Block 1 conditionally approves P3 documentary completeness; latest reply “Yes do and continue developing” accepts the assistant's offered replacement of the five-block waiting instruction and execution of the saved P4 documentation-only prompt with received Blocks 1–4 incorporated. No Block 5 was received or invented. Blocks 2/3 end mid-section and Block 4 repeats and ends mid-sentence; substantive supplied content is retained in the consumed instruction archive. This authorization is not final ADR/language/framework/database/dependency/Windows/isolation approval, nor permission for implementation, installation, commit or deployment.

Before edits, reproduced P3 evidence: branch work, HEAD cef2f6c6a119d4a70b5b4ef5ac12cc18c52b56d4; 53 Markdown documents, 2,282 local links, 1,480 anchors, 19-component acyclic graph, four modules/73 capabilities, 33 entities, eight PROPOSED ADRs, 23 threats, 91 requirement mappings and 239 NOT_RUN cases; original 228 test definitions preserved. P3 checkpoint PASS. MS-0004 READY_FOR_REVIEW -> APPROVED -> COMPLETED for documentary scope only; original report retained with closure addendum. MS-0005 PROPOSED -> READY -> IN_PROGRESS under the explicit replacement authorization.

## P4 approval and controlled documentation checkpoint — 2026-10-11 UTC
Owner message “Approve P4 and execute the saved P5 prompt.” approved P4 documentary completeness. Reproduced P4 before assessment: 58 Markdown files, 2,942 links/1,805 anchors, 22 directory records, 19 component/33 entity maps, 91 requirements/239 NOT_RUN tests/eight PROPOSED ADRs, scope/archive/ID/preservation checks PASS. MS-0005 READY_FOR_REVIEW -> APPROVED -> COMPLETED for documentation only. No ADR or runtime/technology adoption implied.

Subsequent owner task “CONTROLLED DOCUMENTATION GIT CHECKPOINT” explicitly authorizes ONE documentation-only commit with title “docs: establish Freelance Automation Studio governance baseline”, pushed to a new documentation branch on origin, no main push/force/merge/application work. Approved P0–P4 documents and accurate P4 approval closure are in scope; newer P5-only assessment files remain uncommitted. Shared handoff files use this checkpoint view in Git while newer working-tree content is preserved. Git history/push report provide actual commit/persistence evidence; do not invent a self-referential commit hash in this document.

## Current milestone and checkpoint boundary
- MS-0005 / P4: COMPLETED in documentary scope after explicit owner approval and reproduced verification.
- MS-0006 / P5: BLOCKED at its previously assessed prerequisite checkpoint; no executable experiment initialized or run. Separate assessment files are outside this commit, and no P5 work is authorized by this checkpoint task.
- Pending technical decisions: all eight ADRs PROPOSED, target Windows facts/native access, named experimental tuple/support/license evidence and scope remain unresolved.
- Actual application results: all 239 planned cases NOT_RUN; no runtime/Windows/installer/benchmark/security/accessibility proof.
- Active task: one P0–P4 documentation Git checkpoint only, preserve unrelated/uncommitted work.
- Gate: no implementation, merge or further milestone begins automatically.

## Milestone register
MS-0001–MS-0005 COMPLETED (documentary scope/approval limits recorded); MS-0006 BLOCKED at prerequisite checkpoint, executable work not initialized; MS-0007–MS-0015 PROPOSED.

## Risk register
| ID | Risk / fact versus uncertainty | Impact | Mitigation / owner / review gate | Status |
| --- | --- | --- | --- | --- |
| RISK-0001 | Windows 10 exact target and tool support unverified; OS support lifecycle may limit viable distribution | Compatibility and maintainability | Project owner defines target in P1; architecture lead verifies support sources in P3 and actual Windows PoC in P5 | OPEN |
| RISK-0002 | Automation may corrupt outputs or misclassify uncertain results; no implementation tested | Client data loss / incorrect delivery | Module owners design separate outputs, review controls, validation and recovery; QA verifies each module gate | OPEN |
| RISK-0003 | Dependencies/licenses, website authorization and network/client-data boundaries unresolved | Legal, security or scope violations | Project owner plus architecture/security reviews in P1/P3; verify dependency obligations and target authorization before use | OPEN |
| RISK-0004 | Prompt handoffs may drift from approved scope or claim completion without evidence | Governance failure | Task owner follows AGENTS and status rules; reviewer checks evidence and approval at each gate | OPEN |
| RISK-0005 | Proposed performance/usability/resource budgets lack owner-confirmed workloads and measurements | Targets may be infeasible or unrepresentative | Owner reviews O-03 and NFR targets at P1 gate; architect/QA measure in P5/P12 | OPEN |
| RISK-0006 | Candidate formats/fidelity profiles and resume behavior not proven | Silent loss or unsupported expectations | Owner resolves O-02/O-09; architecture and QA assess in P3/P5 and module gates | OPEN |
| RISK-0007 | Worker restrictions and hostile parser confinement not proven | Unauthorized local access or code/resource effects | Security/OS lead verifies token/ACL/child/handle controls in P5/P12; unsupported capability disabled | OPEN |
| RISK-0008 | Browser traffic may bypass request-level authorization; native Win10 engine support unresolved | Unauthorized requests and privacy exposure | QA/security lead proves engine/OS support and complete traffic enforcement in P5 before live capability | OPEN |
| RISK-0009 | SQLite/file publication, migrations, interruption and restore may diverge | Lost history, incorrect artifact/approval or unrecoverable data | Persistence lead validates intents, integrity and backup/restore fault matrix in P5/P11 | OPEN |
| RISK-0010 | Entire governance/design baseline remains uncommitted/untracked | Loss of durable history or reviewable checkpoint | Owner authorizes a reviewed Git checkpoint before executable development; no commit/push now | OPEN |
| RISK-0011 | Block4 requested detailed extensions exceed existing detailed P1 capability decisions | Scope creep or unsupported product promises | Owner dispositions proposed profiles/new functional details before adoption; architecture traces related requirements only | OPEN |

Risk updates retain history: record assessed likelihood/severity in the responsible phase, mitigation evidence, residual risk and accepting authority before marking mitigated/accepted/closed. OPEN here does not imply a measured probability.

## Durable handoff
At each phase end: summarize actual work, link evidence, report failed/skipped/unrun checks, update this record and save exactly one next prompt. If blocked or incomplete, the prompt resolves that phase's blocker rather than advancing. Archive the previous prompt in `docs/prompts/completed/` only when it has been executed and reconciled; preserve its milestone/outcomes. The current-next file is the single authoritative recommendation. Prompt existence is never approval.

## Book acceptance
Current milestone and authorization are explicit, deliverables/results match evidence, risks have owners/gates, approval history is preserved, transitions are lawful, and exactly one current recommendation exists.

## P1 risk progress (2026-10-11)
RISK-0001: exact Windows target still O-01; no verification claim. RISK-0002: acceptance requirements/tests now specify input integrity, partial outcomes and review/recovery controls, but controls are not implemented. RISK-0003: synthetic-only website requests, authorization denial cases and dependency gates specified; licenses/target permissions remain unverified. RISK-0004: P0 conditional approval checked, IDs/links reviewed and the single handoff updated; continuing enforcement still required. RISK-0005/0006 added for unmeasured targets and feature-profile feasibility. All remain OPEN; no residual-risk acceptance invented.

## P2 handoff and risk progress (2026-10-11)
MS-0003: IN_PROGRESS -> READY_FOR_REVIEW after documentary checks. P2 not APPROVED/COMPLETED. Exactly one next action: review/approve the proposed P2 baseline and explicitly authorize the saved P3 prompt. No automatic architecture work.

RISK-0001/0005: Windows/measurement targets remain unresolved; design targets are proposals, not results. RISK-0002: approval invalidation, partial/cancelled artifacts, backup failure and recovery interactions documented but not implemented. RISK-0003: scoped synthetic-only website data and browser availability guards documented; dependencies/permissions remain unverified. RISK-0004: conditional approval limits, baseline hashes and preserved test definitions enforce documentary handoff. RISK-0006: format/fidelity/resume controls remain conditional on O-02/O-09. All six risks remain OPEN. UX-O01 through UX-O05 are local design questions in the UX book, not silently adopted requirements/ADRs.

## P3 probability/impact and remaining exposure assessment
Qualitative architecture judgments, not measured failure frequencies. Every probability remains UNKNOWN empirically; PLAUSIBLE names a reachable scenario, not a statistical estimate. Mitigation design is not closure evidence.
| Risk | Probability assessment | Impact assessment | Mitigation / remaining exposure | Owner | Verification stage | Status |
| --- | --- | --- | --- | --- | --- | --- |
| RISK-0001 | UNKNOWN; plausible target mismatch, support-source evidence exists | HIGH compatibility/support | Exact target/support matrix and P5 proof; laptop remains inaccessible from cloud | Owner/Windows lead | P3 adoption/P5/P13 | OPEN |
| RISK-0002 | UNKNOWN; plausible corruption/approval race | HIGH integrity/delivery | Separate snapshots/intents/hashes/consent; implementation and TOCTOU proof pending | Module/artifact/QA owners | P5/P7-P12 | OPEN |
| RISK-0003 | UNKNOWN; plausible data/license/credential exposure | HIGH privacy/legal | Source licenses/control review performed; exact package/transitives/key/backup protection unverified | Security/license lead | Adoption/P5/P12/P13 | OPEN |
| RISK-0004 | UNKNOWN; plausible governance drift | MEDIUM/HIGH scope/evidence | Conditional status/IDs/single handoff and documentation checks; future enforcement still needed | Task owner/reviewer | Each gate | OPEN |
| RISK-0005 | UNKNOWN; plausible proposed budget mismatch | MEDIUM/HIGH responsiveness/resources | Bounded profiles and streaming proposal; workloads/measurements not approved | Owner/performance QA | P5/P12 | OPEN |
| RISK-0006 | UNKNOWN; plausible fidelity/profile gaps | HIGH data correctness | Explicit unsupported/exact/best-effort/content profiles; formats/fonts/formulas/resume not proven | Owner/module leads | P5/module gates | OPEN |
| RISK-0007 | UNKNOWN; hostile input makes boundary attack plausible | HIGH local compromise | Restricted grants/OS controls proposed; same-user workers not verified sandbox | Security/OS lead | P5/P12 | OPEN |
| RISK-0008 | UNKNOWN; browser scope escape plausible | HIGH authorization/privacy | Fail-closed policy/traffic proof planned; supported Win10 engine and enforcement unknown | QA/security lead | P5/P8/P12 | OPEN |
| RISK-0009 | UNKNOWN; interruptions/corruption plausible | HIGH recovery/history | Prepared intents, one writer and verified backup/restore; power-loss/rename/journal evidence pending | Persistence lead | P5/P11 | OPEN |
| RISK-0010 | Observed uncommitted baseline; loss probability UNKNOWN | HIGH persistence/review history | Reviewed Git checkpoint recommended before executable development; explicit permission absent | Owner | Before P5/executable work | OPEN |
| RISK-0011 | Observed conditional new design capabilities; drift probability UNKNOWN | MEDIUM/HIGH scope/promises | Eleven capability extensions explicitly marked, no SRS changes; owner dispositions pending | Owner/requirements lead | Before implementation | OPEN |

## P3 handoff and actual verification (2026-10-11)
MS-0004 IN_PROGRESS -> READY_FOR_REVIEW after documentary acceptance and final preservation/link/identifier/contract/DAG review. Owner P3 approval remains pending; no ADR adopted and no risk closed. Source investigation: 48 attempts, 33 fetched, 15 unavailable; exact pinned dependency/license and Windows support clearance remains pending. Terminal establishes Linux cloud host only, not owner laptop compatibility. Mermaid rendering SKIPPED; all application/Windows/browser/performance/security/installer tests NOT_RUN. Two drafting/check issues (missing persistence output write and checker capability-row pattern) were corrected before final PASS; no outstanding check failure.

Exactly one next action: review and explicitly approve the conditional P3 documentary baseline and authorize the [saved P4 documentation prompt](../prompts/current-next-prompt.md). P4/P5 have not begun. RISK-0010 retains the need for a separately authorized reviewed Git checkpoint before executable development; no commit requested or performed here. Full [milestone report](../milestone-reports/MS-0004-P3.md) contains 25 check outcomes and 26 independent acceptance dispositions.

## P4 handoff and risk progress — 2026-10-11
MS-0005 IN_PROGRESS -> READY_FOR_REVIEW after documentary checks and semantic standards/boundary/trace review. P4 approval pending; eight ADRs PROPOSED, individual requirements/extensions/numeric targets unresolved. Exactly one next action: review/approve P4 documentary scope and authorize the [saved P5 prerequisite-check/PoC prompt](../prompts/current-next-prompt.md). P5 executable scope still requires applicable target/version/license/experimental authorization; no P5 begun.

All eleven project risks remain OPEN with existing probability/impact/owner/stage. RISK-0001/0003: exact Windows and dependency license/support tuple unverified, no new source-refresh or native proof. RISK-0002/0006/0009: review/integrity/fidelity/recovery standards documented, runtime effectiveness pending. RISK-0004: rule owners/trace/scope/prompt archive/actual outcomes checked, future enforcement unproven. RISK-0005: benchmark methodology and safe limits proposed, no measurements. RISK-0007/0008: handle/confinement/all-browser-traffic controls and future methods explicit, actual enforcement unresolved. RISK-0010: P0–P4 remain untracked/uncommitted; reviewed checkpoint procedure defined, no commit authorization/action. RISK-0011: extensions mapped as conditional only, no requirement changes.

Application/Windows/browser/security/accessibility/performance/build/installer/migration/restore checks NOT_RUN; optional network/source refresh SKIPPED because no technology adopted, P3 source evidence preserved as historical. Documentary failures none. Full checklist/evidence/limitations in [P4 report](../milestone-reports/MS-0005-P4.md). P4 is not APPROVED/COMPLETED and no product-readiness claim made.
