# Requirements book — Software Requirements Specification

Version: P1 proposed baseline, 2026-10-11. Requirement status: PROPOSED throughout; none is approved or measured. P0 governance is approved. This book owns WHAT the product does, not final technology choices. [Permanent policies](00-master-rulebook.md), [test outcome rules](06-testing-book.md) and [security assessment process](07-security-book.md) remain authoritative in their books.

## Sources and requirement interpretation
S1: owner P1 instruction (functional areas, four categories, measurable quality and documentation-only scope). S2: owner permanent constraints, mapped to GOV policies in the master rulebook. S3: candidate workflows/targets derived during P1; explicitly proposals, not business facts. Each entry cites S1/S2 and labels derivation; exact feature behaviors, formats and numbers are S3 until approved.

MUST = proposed release-blocking acceptance; SHOULD = proposed useful capability eligible for explicit owner deferral. These priorities do not authorize implementation. All entries are feasible only pending P3 assessment/P5 evidence. Numeric budgets are proposed, not measurements. An owner's approval of P1 must identify deferred capabilities/targets and unresolved conditions; silence cannot finalize an open choice.

Each entry contains description, rationale, source, priority, status, acceptance criteria, risk and trace references. Its TEST links resolve through the matrix. Design is pending P2/P3, implementation pending P6-P10, executable evidence pending implementation/Windows gates, and requirement approval pending P1 review. These pending links apply to every entry; they are not missing or completed artifacts.

## Scope, users and representative jobs
Proposed personas: operator (freelancer configuring/running jobs), reviewer (human checking evidence and approving delivery, possibly the same person), and local administrator (managing installation/settings). They describe responsibilities, not mandatory accounts or an approved authentication design. Clients are metadata records, not externally authenticated users.

| Category | Representative proposed job | Candidate inputs -> outputs | Boundary |
| --- | --- | --- | --- |
| Spreadsheet/CSV | Clean a table, validate fields and export a reviewed result | UTF-8 CSV / non-macro XLSX -> CSV/XLSX plus findings | Locale, formulas and preservation profile explicit; no macro execution |
| Website QA | Check authorized routes/assertions against a reviewed baseline | Authorized URL scope + synthetic scenarios -> local report/screenshots | Network needed for live targets; no unauthorized writes or platform automation |
| PDF/documents | Split/merge PDFs or fill declared document placeholders | PDF/TXT/DOCX -> declared supported outputs plus evidence | Scanned content/OCR, complex layout and encryption require explicit support decisions |
| Maintenance/templates | Generate or update a local website copy and validate links | Licensed local templates/assets -> local reviewed workspace/package | No implicit deployment, remote tool download or execution of template scripts |

Primary flow: client/project -> draft job -> select module/inputs/template -> validate -> inspect/confirm plan -> process -> validate outputs -> review uncertainty -> delivery approval -> local package/export -> history. Failure/cancel/interruption yields a truthful incomplete outcome and recovery options, never automatic approval.

Conceptual outcomes: draft, validated/planned, running, cancellation requested, cancelled, failed, interrupted, processed awaiting validation/review, reviewed/rejected and delivery-approved. These are product requirements concepts, not an approved state-machine implementation. Partial item success is recorded separately from overall failure/cancellation. Job outcome and human delivery approval are distinct.

Out of scope: cloud backend/database, paid APIs, runtime AI, compulsory subscriptions/external sign-in, automatic client delivery, freelance-platform automation, uncontrolled crawling and implicit deployment. OCR, advanced office-format support, scheduling, third-party plugin marketplace and commercial-scale multi-user workflows are not silently included.

## Assumptions and open decisions
| Key | Proposal / unknown | Decision owner and gate | Consequence |
| --- | --- | --- | --- |
| O-01 | Exact Windows 10 edition/build/architecture and support-lifecycle expectations unknown; candidate x64 target only | Owner P1/P3; actual Windows proof P5/P13 | No compatibility claim or final tool choice |
| O-02 | Candidate formats CSV/XLSX/PDF/TXT/DOCX need approved feature/fidelity profiles; no real client samples supplied | Owner P1 review, architecture/QA P3/P5 | Unsupported features must fail/flag; formats remain proposed |
| O-03 | WP-1 candidate machine: Windows target from O-01, 4 logical cores, 8 GiB RAM, SSD, 100,000 x 20 CSV fields averaging <=32 characters; no measurements | Owner P1 target review; architect P3; QA P5/P12 | Performance/resource numbers provisional |
| O-04 | Module priorities and SHOULD capability deferrals unknown | Owner P1 review | All four categories remain in scope; no silent release exclusion |
| O-05 | Same operator may review; local identity is asserted, not independently verified | Owner P1/P2; security P3 | No separation-of-duties or authentication mechanism assumed |
| O-06 | Exact website authorization evidence, allowed synthetic data and request budgets unknown | Owner before each live target; security P3 | Unauthorized live jobs blocked, no credentials requested now |
| O-07 | Retention durations, backup encryption and sensitive-data handling profiles need owner decisions | Owner P1/P3 | Explicit local settings/consent; no invented retention period |
| O-08 | Packaging/export format and offline installer prerequisites not finalized | Owner/architecture P3; release P13 | Local manifest/export behavior specified without choosing libraries |
| O-09 | Resumability is operation-dependent; arbitrary checkpoint support not assumed | Architecture P3/PoC P5 | Safe retry required where resume is unsupported |

These are review decisions, not blockers to a proposed SRS. Unresolved mandatory format/target/workload choices prevent unconditional implementation/release acceptance. No feasibility, usability, performance, security or license outcome has been verified.

## Functional requirement catalog

## Core desktop and job workflow

### REQ-0001 — Navigation
- Description: From the main view, reach clients, projects, job creation, history and settings without losing a saved job; show active project and job identity.
- Business rationale: Make job work discoverable.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: From the main view, reach clients, projects, job creation, history and settings without losing a saved job; show active project and job identity.
- Negative/boundary acceptance: Switch views with an unsaved edit; offer save/discard/cancel and cancel retains the edit.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0001) -> TEST-0001, TEST-0002; design/implementation/executable evidence/approval pending as declared above.

### REQ-0002 — Client records
- Description: Create, edit and archive a local client using a display name and optional notes; archived clients remain linked to history.
- Business rationale: Organize local client work.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Create, edit and archive a local client using a display name and optional notes; archived clients remain linked to history.
- Negative/boundary acceptance: Reject a blank display name; archiving does not erase project files or job evidence.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0002) -> TEST-0003, TEST-0004; design/implementation/executable evidence/approval pending as declared above.

### REQ-0003 — Project records
- Description: Create a named project linked to a client and chosen local workspace; list only its jobs when selected.
- Business rationale: Separate client deliverables.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Create a named project linked to a client and chosen local workspace; list only its jobs when selected.
- Negative/boundary acceptance: Reject unavailable workspace before saving; changing projects does not move or overwrite files.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0003) -> TEST-0005, TEST-0006; design/implementation/executable evidence/approval pending as declared above.

### REQ-0004 — Job creation
- Description: Save a draft with unique job ID, project, module, input references and configuration; reopen with the same saved values.
- Business rationale: Identify repeatable work.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Save a draft with unique job ID, project, module, input references and configuration; reopen with the same saved values.
- Negative/boundary acceptance: Reject execution of an incomplete draft and list missing fields without deleting it.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0004) -> TEST-0007, TEST-0008; design/implementation/executable evidence/approval pending as declared above.

### REQ-0005 — File import
- Description: Select one or several supported local files; show path, size and format before processing; cancel import leaves the draft unchanged.
- Business rationale: Use local inputs safely.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Select one or several supported local files; show path, size and format before processing; cancel import leaves the draft unchanged.
- Negative/boundary acceptance: Missing, unreadable or unsupported files are rejected with per-file reasons and no input modification.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0005) -> TEST-0009, TEST-0010; design/implementation/executable evidence/approval pending as declared above.

### REQ-0006 — Module selection
- Description: List the four initial module categories and supported capabilities; choose one module per job and validate its configuration.
- Business rationale: Choose the relevant automation.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: List the four initial module categories and supported capabilities; choose one module per job and validate its configuration.
- Negative/boundary acceptance: An unavailable capability cannot execute and explains its limitation without silently selecting another module.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0006) -> TEST-0011, TEST-0012; design/implementation/executable evidence/approval pending as declared above.

### REQ-0007 — Reusable templates
- Description: Save named/versioned configuration templates without client file contents or credentials; creating a job from a template makes an independent draft.
- Business rationale: Reduce repeated configuration.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Save named/versioned configuration templates without client file contents or credentials; creating a job from a template makes an independent draft.
- Negative/boundary acceptance: Editing a template does not mutate prior jobs; invalid or obsolete options require explicit correction before use.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0007) -> TEST-0013, TEST-0014; design/implementation/executable evidence/approval pending as declared above.

### REQ-0008 — Input validation
- Description: Before planning, validate required fields, input accessibility, supported formats and option ranges; show each error with its field/file.
- Business rationale: Catch configuration errors early.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Before planning, validate required fields, input accessibility, supported formats and option ranges; show each error with its field/file.
- Negative/boundary acceptance: An invalid field or changed input stops planning; validation does not execute macros or modify inputs.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0008) -> TEST-0015, TEST-0016; design/implementation/executable evidence/approval pending as declared above.

### REQ-0009 — Execution plan
- Description: Before start, display inputs, operations, output paths, review requirements and whether network access is required; require confirmation of this plan.
- Business rationale: Expose intended effects.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Before start, display inputs, operations, output paths, review requirements and whether network access is required; require confirmation of this plan.
- Negative/boundary acceptance: A changed input/configuration after confirmation invalidates the plan and requires revalidation.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0009) -> TEST-0017, TEST-0018; design/implementation/executable evidence/approval pending as declared above.

### REQ-0010 — Destructive-action consent
- Description: For every proposed overwrite/delete or irreversible action, display exact target, effect and recovery availability; require a fresh explicit confirmation.
- Business rationale: Prevent accidental data loss.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: For every proposed overwrite/delete or irreversible action, display exact target, effect and recovery availability; require a fresh explicit confirmation.
- Negative/boundary acceptance: Reject/cancel yields no destructive effect; template or previous-job consent cannot approve a new action.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0010) -> TEST-0019, TEST-0020; design/implementation/executable evidence/approval pending as declared above.

### REQ-0011 — Processing
- Description: Run only the validated, confirmed plan and record actual start/end, outcome and processed-item counts under its job ID.
- Business rationale: Execute the confirmed work.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Run only the validated, confirmed plan and record actual start/end, outcome and processed-item counts under its job ID.
- Negative/boundary acceptance: Injected operation failure prevents success classification and does not trigger unplanned operations.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0011) -> TEST-0021, TEST-0022; design/implementation/executable evidence/approval pending as declared above.

### REQ-0012 — Progress
- Description: Show current job state, current operation, completed/total items when known and recent activity; unknown totals are labeled indeterminate.
- Business rationale: Keep the operator informed.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Show current job state, current operation, completed/total items when known and recent activity; unknown totals are labeled indeterminate.
- Negative/boundary acceptance: A stalled operation is not reported complete; estimates are labeled estimates rather than measured completion.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0012) -> TEST-0023, TEST-0024; design/implementation/executable evidence/approval pending as declared above.

### REQ-0013 — Cancellation
- Description: Accept cancellation during a running job; cease starting new items and classify output as cancelled/partial with item dispositions.
- Business rationale: Allow safe stopping.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Accept cancellation during a running job; cease starting new items and classify output as cancelled/partial with item dispositions.
- Negative/boundary acceptance: Cancel at start, mid-item and near completion; preserve originals and never present an incomplete output as approved delivery.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0013) -> TEST-0025, TEST-0026; design/implementation/executable evidence/approval pending as declared above.

### REQ-0014 — Failure reporting
- Description: Record a failed item/operation, safe cause, affected outputs and permitted next action; retain a failure report even when no output is produced.
- Business rationale: Make failures actionable.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Record a failed item/operation, safe cause, affected outputs and permitted next action; retain a failure report even when no output is produced.
- Negative/boundary acceptance: Unreadable output destination and malformed input both show an actionable failure without exposing credentials.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0014) -> TEST-0027, TEST-0028; design/implementation/executable evidence/approval pending as declared above.

### REQ-0015 — Retry
- Description: Allow a new linked attempt of a failed/cancelled job after revalidation; identify what will rerun and isolate its outputs.
- Business rationale: Avoid duplicate work.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Allow a new linked attempt of a failed/cancelled job after revalidation; identify what will rerun and isolate its outputs.
- Negative/boundary acceptance: Changed inputs invalidate reuse; retry must not overwrite an earlier successful output without new consent.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0015) -> TEST-0029, TEST-0030; design/implementation/executable evidence/approval pending as declared above.

### REQ-0016 — Interrupted-job recovery
- Description: After restart, identify interrupted jobs and offer inspection plus eligible resume or safe retry; retain prior evidence and classify unfinished outputs.
- Business rationale: Recover from incomplete runs.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: After restart, identify interrupted jobs and offer inspection plus eligible resume or safe retry; retain prior evidence and classify unfinished outputs.
- Negative/boundary acceptance: For a non-resumable operation, explain the limitation and offer safe retry; never mark the interrupted run successful.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0016) -> TEST-0031, TEST-0032; design/implementation/executable evidence/approval pending as declared above.

### REQ-0017 — Evidence capture
- Description: Every started run produces a local record with job/attempt ID, timestamps, module/tool versions, input hashes, normalized configuration, item outcomes, output hashes and warnings.
- Business rationale: Make each result verifiable.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Every started run produces a local record with job/attempt ID, timestamps, module/tool versions, input hashes, normalized configuration, item outcomes, output hashes and warnings.
- Negative/boundary acceptance: If durable evidence cannot be written, do not start or finalize as success; redact secrets and identify unavailable evidence.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0017) -> TEST-0033, TEST-0034; design/implementation/executable evidence/approval pending as declared above.

### REQ-0018 — Output validation
- Description: Apply declared module output checks; report pass/fail/uncertain per output and link them to the run evidence.
- Business rationale: Detect incorrect deliverables.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Apply declared module output checks; report pass/fail/uncertain per output and link them to the run evidence.
- Negative/boundary acceptance: An unreadable or mismatched output fails validation and cannot enter the approved package.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0018) -> TEST-0035, TEST-0036; design/implementation/executable evidence/approval pending as declared above.

### REQ-0019 — Human review
- Description: Present uncertain or failed validation findings with evidence and allow recorded accept/reject plus rationale by a locally identified reviewer.
- Business rationale: Handle uncertainty honestly.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Present uncertain or failed validation findings with evidence and allow recorded accept/reject plus rationale by a locally identified reviewer.
- Negative/boundary acceptance: No response is not approval; rejection retains evidence and excludes the output from approved packaging.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0019) -> TEST-0037, TEST-0038; design/implementation/executable evidence/approval pending as declared above.

### REQ-0020 — Delivery approval
- Description: Require explicit reviewer approval tied to exact output hashes and run ID before labeling a package ready for client delivery.
- Business rationale: Control final client delivery.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Require explicit reviewer approval tied to exact output hashes and run ID before labeling a package ready for client delivery.
- Negative/boundary acceptance: Changing any approved file invalidates approval; validation success alone is insufficient.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0020) -> TEST-0039, TEST-0040; design/implementation/executable evidence/approval pending as declared above.

### REQ-0021 — Reports
- Description: Generate a human-readable local report listing plan, item counts, outcomes, warnings, validation findings and approval state.
- Business rationale: Summarize the actual run.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Generate a human-readable local report listing plan, item counts, outcomes, warnings, validation findings and approval state.
- Negative/boundary acceptance: Partial/failed/cancelled runs remain distinguishable; report-generation failure is recorded rather than hidden as success.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0021) -> TEST-0041, TEST-0042; design/implementation/executable evidence/approval pending as declared above.

### REQ-0022 — Deliverable packaging
- Description: Create a local package containing only selected approved outputs and a manifest of paths/hashes; show contents for review.
- Business rationale: Prepare controlled handoff.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Create a local package containing only selected approved outputs and a manifest of paths/hashes; show contents for review.
- Negative/boundary acceptance: Exclude raw inputs, unrelated client files and credentials by default; a hash mismatch prevents ready-for-delivery status.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0022) -> TEST-0043, TEST-0044; design/implementation/executable evidence/approval pending as declared above.

### REQ-0023 — Export
- Description: Export selected reports/evidence/packages to a user-chosen local destination and preserve source records.
- Business rationale: Provide explicit local exports.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Export selected reports/evidence/packages to a user-chosen local destination and preserve source records.
- Negative/boundary acceptance: Cancel changes nothing; existing destination collision requires a new name or explicit overwrite consent.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0023) -> TEST-0045, TEST-0046; design/implementation/executable evidence/approval pending as declared above.

### REQ-0024 — History
- Description: Find local attempts by client/project/date/module/outcome and inspect their evidence and approval state.
- Business rationale: Audit past activity.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Find local attempts by client/project/date/module/outcome and inspect their evidence and approval state.
- Negative/boundary acceptance: Missing external files are shown as unavailable; historical records are not silently rewritten to imply success.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0024) -> TEST-0047, TEST-0048; design/implementation/executable evidence/approval pending as declared above.

### REQ-0025 — Settings
- Description: Persist local preferences for default output location and proposed job defaults; show effective values before execution.
- Business rationale: Keep preferences explicit.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Persist local preferences for default output location and proposed job defaults; show effective values before execution.
- Negative/boundary acceptance: Invalid settings are rejected; changing a preference does not alter completed jobs or already confirmed plans.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0025) -> TEST-0049, TEST-0050; design/implementation/executable evidence/approval pending as declared above.

### REQ-0026 — Local data management
- Description: List managed records/output storage and offer selective archive/delete with affected evidence references and consent.
- Business rationale: Control retention.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: List managed records/output storage and offer selective archive/delete with affected evidence references and consent.
- Negative/boundary acceptance: Never delete original input files through history cleanup; deletion lists affected records and handles locked files as partial failure.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0026) -> TEST-0051, TEST-0052; design/implementation/executable evidence/approval pending as declared above.

### REQ-0027 — Offline gating
- Description: Allow local-job planning/execution/review/export with no connectivity; network-dependent jobs explain target connectivity requirements before start.
- Business rationale: Separate local and website work.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Allow local-job planning/execution/review/export with no connectivity; network-dependent jobs explain target connectivity requirements before start.
- Negative/boundary acceptance: With network unavailable, a website job reports a specific connectivity failure while local jobs remain usable.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0027) -> TEST-0053, TEST-0054; design/implementation/executable evidence/approval pending as declared above.

### REQ-0028 — Target authorization
- Description: Before any live website request, require a local authorization record covering target hosts/paths, actions, expiry and permission evidence; attach it to the plan.
- Business rationale: Prevent unauthorized website actions.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Before any live website request, require a local authorization record covering target hosts/paths, actions, expiry and permission evidence; attach it to the plan.
- Negative/boundary acceptance: Missing/expired authorization, out-of-scope redirects and unauthorized hosts/actions are blocked before the prohibited request.
- Relevant risk: RISK-0003 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0028) -> TEST-0055, TEST-0056; design/implementation/executable evidence/approval pending as declared above.

### REQ-0029 — Job concurrency controls
- Description: Detect plans writing to the same target and prevent conflicting simultaneous writes; report the blocked job and conflict.
- Business rationale: Avoid conflicting jobs.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Detect plans writing to the same target and prevent conflicting simultaneous writes; report the blocked job and conflict.
- Negative/boundary acceptance: Two simultaneous attempts with colliding destinations cannot silently corrupt or overwrite each other's outputs.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0029) -> TEST-0057, TEST-0058; design/implementation/executable evidence/approval pending as declared above.

### REQ-0030 — Client-data locality
- Description: No job or diagnostic action uploads local client inputs, outputs, logs or reports; website tests use only explicitly authorized synthetic test data.
- Business rationale: Avoid automatic uploads.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: No job or diagnostic action uploads local client inputs, outputs, logs or reports; website tests use only explicitly authorized synthetic test data.
- Negative/boundary acceptance: Any local client file selected for a website request is blocked; only separately authorized synthetic test values may be sent. No cloud storage or telemetry is enabled.
- Relevant risk: RISK-0003 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0030) -> TEST-0059, TEST-0060; design/implementation/executable evidence/approval pending as declared above.

### REQ-0031 — Review audit
- Description: Store review/consent decisions with local reviewer label, timestamp, decision, rationale where required and exact artifact/plan reference.
- Business rationale: Record accountability.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Store review/consent decisions with local reviewer label, timestamp, decision, rationale where required and exact artifact/plan reference.
- Negative/boundary acceptance: An altered artifact is displayed as changed since approval; a local identity label is not represented as verified external authentication.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0031) -> TEST-0061, TEST-0062; design/implementation/executable evidence/approval pending as declared above.

### REQ-0032 — Supported capability disclosure
- Description: Show supported formats/features and limits for each operation before start; fail explicitly when a requested feature cannot be preserved.
- Business rationale: Avoid silent loss.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Show supported formats/features and limits for each operation before start; fail explicitly when a requested feature cannot be preserved.
- Negative/boundary acceptance: Unsupported embedded content or format is not silently dropped; conversion with stated losses requires human review.
- Relevant risk: RISK-0006 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0032) -> TEST-0063, TEST-0064; design/implementation/executable evidence/approval pending as declared above.

## Spreadsheet and CSV automation

### REQ-0033 — CSV interpretation
- Description: For CSV jobs, show delimiter, encoding, header choice and preview; permit explicit override and persist the chosen interpretation.
- Business rationale: Avoid ambiguous data imports.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: For CSV jobs, show delimiter, encoding, header choice and preview; permit explicit override and persist the chosen interpretation.
- Negative/boundary acceptance: Ambiguous encoding/delimiter or inconsistent field counts blocks processing until resolved; UTF-8 quoted multiline fields round-trip in the declared profile.
- Relevant risk: RISK-0006 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0033) -> TEST-0065, TEST-0066; design/implementation/executable evidence/approval pending as declared above.

### REQ-0034 — Spreadsheet selection
- Description: For proposed XLSX inputs, list sheets and allow explicit sheet/range/header selection with preview.
- Business rationale: Target the correct data.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: For proposed XLSX inputs, list sheets and allow explicit sheet/range/header selection with preview.
- Negative/boundary acceptance: Missing sheet/range and encrypted or unsupported workbook features fail safely; no macros are executed.
- Relevant risk: RISK-0006 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0034) -> TEST-0067, TEST-0068; design/implementation/executable evidence/approval pending as declared above.

### REQ-0035 — Data cleaning
- Description: Configure trim, empty-value handling and exact duplicate removal independently; report changed/removed counts and retain input order unless configured otherwise.
- Business rationale: Make transformations explicit.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Configure trim, empty-value handling and exact duplicate removal independently; report changed/removed counts and retain input order unless configured otherwise.
- Negative/boundary acceptance: Unselected columns remain unchanged; duplicates differing outside the configured key are retained according to the shown rule.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0035) -> TEST-0069, TEST-0070; design/implementation/executable evidence/approval pending as declared above.

### REQ-0036 — Filter and sort
- Description: Apply typed filter conditions and explicit sort keys/directions; record selected/excluded counts and stable tie behavior.
- Business rationale: Create consistent subsets.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Apply typed filter conditions and explicit sort keys/directions; record selected/excluded counts and stable tie behavior.
- Negative/boundary acceptance: Invalid numeric/date conversion produces a row-level finding; locale interpretation is explicit and never silently guessed.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0036) -> TEST-0071, TEST-0072; design/implementation/executable evidence/approval pending as declared above.

### REQ-0037 — Column mapping
- Description: Select, rename and reorder columns using a displayed mapping; preview the resulting schema.
- Business rationale: Reshape data predictably.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Select, rename and reorder columns using a displayed mapping; preview the resulting schema.
- Negative/boundary acceptance: Reject duplicate output names or missing source columns before execution.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0037) -> TEST-0073, TEST-0074; design/implementation/executable evidence/approval pending as declared above.

### REQ-0038 — Join and combine
- Description: Combine compatible tables or join on configured keys; report unmatched keys and duplicate-key policy before applying it.
- Business rationale: Merge without hidden loss.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: SHOULD; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Combine compatible tables or join on configured keys; report unmatched keys and duplicate-key policy before applying it.
- Negative/boundary acceptance: Conflicting schemas and many-to-many expansion exceeding the approved plan stop or require a revised plan, not silent truncation.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0038) -> TEST-0075, TEST-0076; design/implementation/executable evidence/approval pending as declared above.

### REQ-0039 — Rule-based validation
- Description: Evaluate required-value, type, allowed-value and uniqueness rules; emit row/column findings linked to the rule.
- Business rationale: Flag questionable data.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Evaluate required-value, type, allowed-value and uniqueness rules; emit row/column findings linked to the rule.
- Negative/boundary acceptance: Invalid rows are flagged rather than silently deleted; no configured rules is reported as no rules evaluated, not full validation.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0039) -> TEST-0077, TEST-0078; design/implementation/executable evidence/approval pending as declared above.

### REQ-0040 — Spreadsheet export
- Description: Produce proposed CSV/XLSX outputs with declared encoding/schema and validate row/column counts plus configured preservation properties.
- Business rationale: Preserve requested data semantics.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Produce proposed CSV/XLSX outputs with declared encoding/schema and validate row/column counts plus configured preservation properties.
- Negative/boundary acceptance: Formula text, leading zeros and date values are preserved under the declared profile or flagged unsupported before start; export failure never overwrites the source.
- Relevant risk: RISK-0006 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0040) -> TEST-0079, TEST-0080; design/implementation/executable evidence/approval pending as declared above.

### REQ-0041 — Spreadsheet change summary
- Description: Report original/output counts, changed cells/rows, rejected records and rule results with deterministic local evidence.
- Business rationale: Support review of transformations.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Report original/output counts, changed cells/rows, rejected records and rule results with deterministic local evidence.
- Negative/boundary acceptance: Sensitive cell values are omitted from general logs; any detailed client-data evidence remains local and explicitly included for review.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0041) -> TEST-0081, TEST-0082; design/implementation/executable evidence/approval pending as declared above.

## Website QA and regression testing

### REQ-0042 — Website test scope
- Description: Choose an authorized base target, permitted routes and request budget before a run; report the effective allowlist.
- Business rationale: Constrain browsing.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Choose an authorized base target, permitted routes and request budget before a run; report the effective allowlist.
- Negative/boundary acceptance: A redirect, link or asset outside approved target scope is blocked and reported unless separately authorized.
- Relevant risk: RISK-0003 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0042) -> TEST-0083, TEST-0084; design/implementation/executable evidence/approval pending as declared above.

### REQ-0043 — Availability and links
- Description: Check configured pages and permitted links for response status and navigation errors; list tested and untested URLs with reasons.
- Business rationale: Find deterministic web failures.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Check configured pages and permitted links for response status and navigation errors; list tested and untested URLs with reasons.
- Negative/boundary acceptance: Timeout/TLS failure is recorded distinctly from a broken link; never disable certificate verification to pass.
- Relevant risk: RISK-0003 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0043) -> TEST-0085, TEST-0086; design/implementation/executable evidence/approval pending as declared above.

### REQ-0044 — Content assertions
- Description: Evaluate explicit text, element-presence and attribute assertions on approved pages and report expected versus observed values.
- Business rationale: Verify configured page behavior.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Evaluate explicit text, element-presence and attribute assertions on approved pages and report expected versus observed values.
- Negative/boundary acceptance: A missing selector or ambiguous multiple match fails the relevant assertion; no assertions is labeled no assertions configured.
- Relevant risk: RISK-0003 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0044) -> TEST-0087, TEST-0088; design/implementation/executable evidence/approval pending as declared above.

### REQ-0045 — Interaction scenarios
- Description: Run explicitly configured navigation/form scenarios with approved synthetic test values; record steps and assertions.
- Business rationale: Test authorized user flows.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Run explicitly configured navigation/form scenarios with approved synthetic test values; record steps and assertions.
- Negative/boundary acceptance: A state-changing submission requires authorization for that action; absence of authorization blocks the step without posting data.
- Relevant risk: RISK-0003 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0045) -> TEST-0089, TEST-0090; design/implementation/executable evidence/approval pending as declared above.

### REQ-0046 — Regression baselines
- Description: Compare current findings to a reviewed versioned baseline and classify new, unchanged and resolved issues.
- Business rationale: Avoid false pass claims.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Compare current findings to a reviewed versioned baseline and classify new, unchanged and resolved issues.
- Negative/boundary acceptance: Missing/stale baseline yields no regression verdict; accepting a new baseline requires recorded human review.
- Relevant risk: RISK-0003 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0046) -> TEST-0091, TEST-0092; design/implementation/executable evidence/approval pending as declared above.

### REQ-0047 — Visual evidence
- Description: Capture local screenshots for configured viewports and compare against approved baselines using declared tolerance/ignored regions.
- Business rationale: Capture reviewable differences.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: SHOULD; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Capture local screenshots for configured viewports and compare against approved baselines using declared tolerance/ignored regions.
- Negative/boundary acceptance: Unstable regions or rendering differences are flagged uncertain; visual comparison cannot silently replace a baseline.
- Relevant risk: RISK-0003 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0047) -> TEST-0093, TEST-0094; design/implementation/executable evidence/approval pending as declared above.

### REQ-0048 — Viewport checks
- Description: Run configured pages at proposed desktop/mobile viewport sizes and record overflow and configured layout assertions.
- Business rationale: Find responsive problems.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: SHOULD; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Run configured pages at proposed desktop/mobile viewport sizes and record overflow and configured layout assertions.
- Negative/boundary acceptance: Unavailable viewport capability is reported as not run; viewport emulation is not claimed as testing on a real mobile device.
- Relevant risk: RISK-0003 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0048) -> TEST-0095, TEST-0096; design/implementation/executable evidence/approval pending as declared above.

### REQ-0049 — Basic accessibility checks
- Description: Evaluate declared automated checks such as accessible names, image alternatives and label associations; report rule ID and element evidence.
- Business rationale: Expose bounded accessibility findings.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: SHOULD; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Evaluate declared automated checks such as accessible names, image alternatives and label associations; report rule ID and element evidence.
- Negative/boundary acceptance: Report automated scope/limitations and never label the entire site accessibility-compliant from automated results alone.
- Relevant risk: RISK-0003 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0049) -> TEST-0097, TEST-0098; design/implementation/executable evidence/approval pending as declared above.

### REQ-0050 — Website results
- Description: Produce per-page/step PASS, FAIL, UNCERTAIN, BLOCKED or NOT_RUN results with timing, authorization reference and evidence.
- Business rationale: Separate environment from product failures.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Produce per-page/step PASS, FAIL, UNCERTAIN, BLOCKED or NOT_RUN results with timing, authorization reference and evidence.
- Negative/boundary acceptance: A network outage or blocked external asset cannot be converted into a passing website assertion; sensitive test data is redacted.
- Relevant risk: RISK-0003 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0050) -> TEST-0099, TEST-0100; design/implementation/executable evidence/approval pending as declared above.

## PDF and document automation

### REQ-0051 — Document import
- Description: For proposed PDF/TXT/DOCX profiles, identify page/section counts and declared support limitations before processing.
- Business rationale: Recognize supported documents.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: For proposed PDF/TXT/DOCX profiles, identify page/section counts and declared support limitations before processing.
- Negative/boundary acceptance: Corrupt/encrypted files fail with a safe explanation; restricted documents are not decrypted or modified without legitimate authorization and supported access.
- Relevant risk: RISK-0006 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0051) -> TEST-0101, TEST-0102; design/implementation/executable evidence/approval pending as declared above.

### REQ-0052 — PDF split
- Description: Split a PDF using explicit page ranges into separately named outputs; verify selected page counts and order.
- Business rationale: Create correctly scoped extracts.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Split a PDF using explicit page ranges into separately named outputs; verify selected page counts and order.
- Negative/boundary acceptance: Reject out-of-range/empty selections; overlapping ranges are shown in the plan rather than silently deduplicated.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0052) -> TEST-0103, TEST-0104; design/implementation/executable evidence/approval pending as declared above.

### REQ-0053 — PDF merge
- Description: Merge selected PDFs in a user-confirmed file/page order and validate combined page count.
- Business rationale: Combine in declared order.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Merge selected PDFs in a user-confirmed file/page order and validate combined page count.
- Negative/boundary acceptance: Incompatible/restricted input causes a failure or explicit exclusion review; missing pages cannot silently pass validation.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0053) -> TEST-0105, TEST-0106; design/implementation/executable evidence/approval pending as declared above.

### REQ-0054 — Page reorganization
- Description: Rotate/reorder or omit pages only as specified in the confirmed plan and report source-to-output page mapping.
- Business rationale: Apply exact page operations.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: SHOULD; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Rotate/reorder or omit pages only as specified in the confirmed plan and report source-to-output page mapping.
- Negative/boundary acceptance: Duplicate/invalid page references are rejected unless explicit duplication is intended; originals remain unchanged.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0054) -> TEST-0107, TEST-0108; design/implementation/executable evidence/approval pending as declared above.

### REQ-0055 — Text extraction
- Description: Extract available text to local outputs with page references and report pages without a usable text layer.
- Business rationale: Separate extracted text from guesses.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Extract available text to local outputs with page references and report pages without a usable text layer.
- Negative/boundary acceptance: Scanned/no-text pages are flagged, not reported as successfully transcribed; OCR is not assumed part of the initial baseline.
- Relevant risk: RISK-0006 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0055) -> TEST-0109, TEST-0110; design/implementation/executable evidence/approval pending as declared above.

### REQ-0056 — Template substitution
- Description: For approved text/document templates, replace declared placeholders from local supplied values and list resolved/unresolved fields.
- Business rationale: Generate explicit document content.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: For approved text/document templates, replace declared placeholders from local supplied values and list resolved/unresolved fields.
- Negative/boundary acceptance: Missing required fields block finalization; embedded scripts/macros are never executed.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0056) -> TEST-0111, TEST-0112; design/implementation/executable evidence/approval pending as declared above.

### REQ-0057 — Batch document jobs
- Description: Apply one confirmed operation to selected documents, generating distinct outputs and per-file outcomes.
- Business rationale: Process collections transparently.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Apply one confirmed operation to selected documents, generating distinct outputs and per-file outcomes.
- Negative/boundary acceptance: One corrupt file is recorded as failure; continue remaining files only under the shown continue-on-error option, with the overall run partial.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0057) -> TEST-0113, TEST-0114; design/implementation/executable evidence/approval pending as declared above.

### REQ-0058 — Document validation
- Description: Reopen generated documents and verify declared page/section count, order and required content properties.
- Business rationale: Detect output damage.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Reopen generated documents and verify declared page/section count, order and required content properties.
- Negative/boundary acceptance: Unsupported fidelity-sensitive content is flagged before start; extraction cannot claim preservation of visual layout.
- Relevant risk: RISK-0006 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0058) -> TEST-0115, TEST-0116; design/implementation/executable evidence/approval pending as declared above.

### REQ-0059 — Document review evidence
- Description: Provide before/after page/field mapping and a local reviewable result summary; require review of uncertain layout/content fidelity.
- Business rationale: Support fidelity review.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Provide before/after page/field mapping and a local reviewable result summary; require review of uncertain layout/content fidelity.
- Negative/boundary acceptance: A signed input is preserved and output explicitly marked as not preserving signature validity when modified; no claim of valid signatures without verification.
- Relevant risk: RISK-0006 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0059) -> TEST-0117, TEST-0118; design/implementation/executable evidence/approval pending as declared above.

## Website maintenance and template-based development

### REQ-0060 — Maintenance workspace
- Description: Select a local website workspace and explicit allowed files; display which files are within the authorized job scope.
- Business rationale: Limit source changes.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Select a local website workspace and explicit allowed files; display which files are within the authorized job scope.
- Negative/boundary acceptance: Reject paths escaping that workspace, including traversal and link-based escape; exclude version-control metadata and secrets.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0060) -> TEST-0119, TEST-0120; design/implementation/executable evidence/approval pending as declared above.

### REQ-0061 — Template project generation
- Description: Generate a local website from an approved, licensed template with declared placeholders into a new output location.
- Business rationale: Create local starter outputs.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Generate a local website from an approved, licensed template with declared placeholders into a new output location.
- Negative/boundary acceptance: An occupied destination requires consent or a different location; no remote package fetch or script execution occurs implicitly.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0061) -> TEST-0121, TEST-0122; design/implementation/executable evidence/approval pending as declared above.

### REQ-0062 — Maintenance change plan
- Description: Preview proposed content/asset/link/template edits as a file-level change set before applying them to a separate output copy.
- Business rationale: Review exact edits.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Preview proposed content/asset/link/template edits as a file-level change set before applying them to a separate output copy.
- Negative/boundary acceptance: Unknown files and unexpected source hashes invalidate the plan; no change outside the previewed set is permitted.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0062) -> TEST-0123, TEST-0124; design/implementation/executable evidence/approval pending as declared above.

### REQ-0063 — Content and asset updates
- Description: Replace only explicitly mapped text/assets in the output copy and report each affected file/location.
- Business rationale: Apply deterministic updates.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Replace only explicitly mapped text/assets in the output copy and report each affected file/location.
- Negative/boundary acceptance: Missing or ambiguous match blocks the affected edit rather than globally replacing unrelated content.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0063) -> TEST-0125, TEST-0126; design/implementation/executable evidence/approval pending as declared above.

### REQ-0064 — Local link checks
- Description: Validate selected relative links and referenced assets within the generated workspace and report unresolved references.
- Business rationale: Detect broken local references.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Validate selected relative links and referenced assets within the generated workspace and report unresolved references.
- Negative/boundary acceptance: External links are marked not checked unless a separately authorized website QA job is created; local validation remains offline.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0064) -> TEST-0127, TEST-0128; design/implementation/executable evidence/approval pending as declared above.

### REQ-0065 — Backup and rollback
- Description: If an explicitly approved in-place operation is offered, create and verify a recoverable local backup before writing; offer rollback with a displayed scope.
- Business rationale: Recover approved in-place edits.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: If an explicitly approved in-place operation is offered, create and verify a recoverable local backup before writing; offer rollback with a displayed scope.
- Negative/boundary acceptance: Backup failure prevents modification; rollback with changed destination files requires fresh consent and records partial failure.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0065) -> TEST-0129, TEST-0130; design/implementation/executable evidence/approval pending as declared above.

### REQ-0066 — Change review and packaging
- Description: Present the final changed-file manifest, validation findings and review state before packaging local website output.
- Business rationale: Deliver reviewed website artifacts.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Present the final changed-file manifest, validation findings and review state before packaging local website output.
- Negative/boundary acceptance: Unapproved changed files are excluded from approved delivery; a package cannot imply the website was deployed.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0066) -> TEST-0131, TEST-0132; design/implementation/executable evidence/approval pending as declared above.

### REQ-0067 — Deployment boundary
- Description: Maintenance jobs produce local artifacts only; display that deployment and platform automation are outside this baseline.
- Business rationale: Prevent unauthorized publishing.
- Source: S1; derived proposal (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Maintenance jobs produce local artifacts only; display that deployment and platform automation are outside this baseline.
- Negative/boundary acceptance: A template containing a publishing command or external automation cannot trigger it as part of generation or maintenance.
- Relevant risk: RISK-0003 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#req-0067) -> TEST-0133, TEST-0134; design/implementation/executable evidence/approval pending as declared above.

## Nonfunctional requirements

### NFR-0001 — Performance responsiveness
- Description: Proposed profile WP-1: p95 navigation/validation-feedback response <=500 ms while a local job runs, across 100 interactions; long validation shows progress within 1 s.
- Business rationale: Keep interactive work usable.
- Source: S1 + S2; derived proposed target (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Proposed profile WP-1: p95 navigation/validation-feedback response <=500 ms while a local job runs, across 100 interactions; long validation shows progress within 1 s.
- Negative/boundary acceptance: On a larger-than-profile workload show processing state, not a frozen interface; measurement must name hardware and dataset.
- Relevant risk: RISK-0005 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#nfr-0001) -> TEST-0135, TEST-0136; design/implementation/executable evidence/approval pending as declared above.

### NFR-0002 — Batch processing budget
- Description: Proposed WP-1 CSV workload: clean/filter/export 100,000 rows x 20 columns <=60 s over 5 runs with cold/warm conditions reported; report median and worst run.
- Business rationale: Bound routine CSV work.
- Source: S1 + S2; derived proposed target (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Proposed WP-1 CSV workload: clean/filter/export 100,000 rows x 20 columns <=60 s over 5 runs with cold/warm conditions reported; report median and worst run.
- Negative/boundary acceptance: Exceeding the budget is a failed target, not suppressed; no measurement exists in P1.
- Relevant risk: RISK-0005 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#nfr-0002) -> TEST-0137, TEST-0138; design/implementation/executable evidence/approval pending as declared above.

### NFR-0003 — Reliability
- Description: All injected read/write/parse/permission/network failures in the agreed fault suite produce a non-success disposition with retrievable evidence and zero silently dropped items.
- Business rationale: Prevent false success.
- Source: S1 + S2; derived proposed target (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: All injected read/write/parse/permission/network failures in the agreed fault suite produce a non-success disposition with retrievable evidence and zero silently dropped items.
- Negative/boundary acceptance: Disk-full or evidence failure cannot leave a run marked successful without valid durable evidence.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#nfr-0003) -> TEST-0139, TEST-0140; design/implementation/executable evidence/approval pending as declared above.

### NFR-0004 — Security input boundaries
- Description: 100% of traversal/link escape, embedded macro/script and unsafe template fixtures in the approved negative suite are rejected or safely inert.
- Business rationale: Treat input as untrusted.
- Source: S1 + S2; derived proposed target (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: 100% of traversal/link escape, embedded macro/script and unsafe template fixtures in the approved negative suite are rejected or safely inert.
- Negative/boundary acceptance: Malformed fixtures cannot execute code or write outside the confirmed workspace.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#nfr-0004) -> TEST-0141, TEST-0142; design/implementation/executable evidence/approval pending as declared above.

### NFR-0005 — Privacy
- Description: During local jobs and diagnostic/report flows, observed outbound connections carrying client content are zero; logs contain zero seeded secret values.
- Business rationale: Prove local handling.
- Source: S1 + S2; derived proposed target (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: During local jobs and diagnostic/report flows, observed outbound connections carrying client content are zero; logs contain zero seeded secret values.
- Negative/boundary acceptance: Seed a credential and confidential cell in test inputs; check general logs/packages for unintended disclosure.
- Relevant risk: RISK-0003 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#nfr-0005) -> TEST-0143, TEST-0144; design/implementation/executable evidence/approval pending as declared above.

### NFR-0006 — Offline operation
- Description: On a clean installed machine with network disabled and no external sign-in, all approved local core/spreadsheet/document/maintenance scenarios complete including review/export.
- Business rationale: Remove connectivity dependence.
- Source: S1 + S2; derived proposed target (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: On a clean installed machine with network disabled and no external sign-in, all approved local core/spreadsheet/document/maintenance scenarios complete including review/export.
- Negative/boundary acceptance: Website live checks report connectivity limitations without disabling local workflows.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#nfr-0006) -> TEST-0145, TEST-0146; design/implementation/executable evidence/approval pending as declared above.

### NFR-0007 — Usability
- Description: Proposed usability target: at least 4 of 5 representative operators complete create/configure/run/review/export scenario without assistance within 10 minutes after a short orientation.
- Business rationale: Reduce unnecessary operator effort.
- Source: S1 + S2; derived proposed target (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Proposed usability target: at least 4 of 5 representative operators complete create/configure/run/review/export scenario without assistance within 10 minutes after a short orientation.
- Negative/boundary acceptance: Record failures and required assistance; do not invent participant results or generalize from developer-only use.
- Relevant risk: RISK-0005 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#nfr-0007) -> TEST-0147, TEST-0148; design/implementation/executable evidence/approval pending as declared above.

### NFR-0008 — Accessibility
- Description: All essential desktop workflows are operable by keyboard with visible focus and meaningful control labels; test 100% of essential controls with a Windows screen reader.
- Business rationale: Support keyboard and assistive access.
- Source: S1 + S2; derived proposed target (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: All essential desktop workflows are operable by keyboard with visible focus and meaningful control labels; test 100% of essential controls with a Windows screen reader.
- Negative/boundary acceptance: Focus traps, inaccessible destructive confirmations or unlabeled essential controls fail the gate.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#nfr-0008) -> TEST-0149, TEST-0150; design/implementation/executable evidence/approval pending as declared above.

### NFR-0009 — Maintainability
- Description: Every production module/public interface has an owner, contract and linked requirement/tests; every scoped change passes the approved review and relevant quality checks.
- Business rationale: Make changes assessable.
- Source: S1 + S2; derived proposed target (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Every production module/public interface has an owner, contract and linked requirement/tests; every scoped change passes the approved review and relevant quality checks.
- Negative/boundary acceptance: A public change without updated contract/trace tests is rejected at review.
- Relevant risk: RISK-0004 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#nfr-0009) -> TEST-0151, TEST-0152; design/implementation/executable evidence/approval pending as declared above.

### NFR-0010 — Modularity
- Description: A representative new module can be registered through approved extension boundaries without editing unrelated module internals; existing module regression scenarios still pass.
- Business rationale: Support independent extension.
- Source: S1 + S2; derived proposed target (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: A representative new module can be registered through approved extension boundaries without editing unrelated module internals; existing module regression scenarios still pass.
- Negative/boundary acceptance: Removing/disabling one optional module does not prevent other module workflows from starting.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#nfr-0010) -> TEST-0153, TEST-0154; design/implementation/executable evidence/approval pending as declared above.

### NFR-0011 — Recoverability
- Description: In 100% of interruption points in the approved suite, restart identifies the incomplete attempt and offers truthful inspect/resume-or-retry choices with preserved originals.
- Business rationale: Retain interrupted job state.
- Source: S1 + S2; derived proposed target (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: In 100% of interruption points in the approved suite, restart identifies the incomplete attempt and offers truthful inspect/resume-or-retry choices with preserved originals.
- Negative/boundary acceptance: A crash during output write cannot produce approved-ready state; recovery limitations must be shown.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#nfr-0011) -> TEST-0155, TEST-0156; design/implementation/executable evidence/approval pending as declared above.

### NFR-0012 — Data integrity
- Description: SHA-256 hashes of original input files are identical before/after all ordinary successful, failed, cancelled and interrupted jobs in the integrity suite.
- Business rationale: Preserve originals.
- Source: S1 + S2; derived proposed target (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: SHA-256 hashes of original input files are identical before/after all ordinary successful, failed, cancelled and interrupted jobs in the integrity suite.
- Negative/boundary acceptance: Explicitly consented in-place changes are excluded from this ordinary-job comparison and require backup/rollback verification.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#nfr-0012) -> TEST-0157, TEST-0158; design/implementation/executable evidence/approval pending as declared above.

### NFR-0013 — Resource consumption
- Description: Proposed WP-1: peak application memory <=1 GiB on the CSV budget workload, idle CPU <=2% averaged over 60 s after settling; report processes and measurement method.
- Business rationale: Bound desktop footprint.
- Source: S1 + S2; derived proposed target (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Proposed WP-1: peak application memory <=1 GiB on the CSV budget workload, idle CPU <=2% averaged over 60 s after settling; report processes and measurement method.
- Negative/boundary acceptance: Exceeding available resources fails gracefully with evidence, not corrupted outputs or silent truncation.
- Relevant risk: RISK-0005 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#nfr-0013) -> TEST-0159, TEST-0160; design/implementation/executable evidence/approval pending as declared above.

### NFR-0014 — Windows compatibility
- Description: All release-critical scenarios and install/upgrade/uninstall checks pass on each owner-approved Windows 10 edition/build/architecture with standard-user job execution.
- Business rationale: Verify the intended platform.
- Source: S1 + S2; derived proposed target (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: All release-critical scenarios and install/upgrade/uninstall checks pass on each owner-approved Windows 10 edition/build/architecture with standard-user job execution.
- Negative/boundary acceptance: Linux checks or vendor statements alone cannot satisfy this requirement; exact target remains an open decision.
- Relevant risk: RISK-0001 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#nfr-0014) -> TEST-0161, TEST-0162; design/implementation/executable evidence/approval pending as declared above.

### NFR-0015 — Installation
- Description: Clean install and launch succeeds using documented free dependencies with no subscription, external sign-in, cloud service or AI runtime; bundled/downloaded prerequisites are disclosed.
- Business rationale: Deliver a standalone product.
- Source: S1 + S2; derived proposed target (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Clean install and launch succeeds using documented free dependencies with no subscription, external sign-in, cloud service or AI runtime; bundled/downloaded prerequisites are disclosed.
- Negative/boundary acceptance: Disconnected installed operation works; whether offline installation media is required remains a proposal for owner review.
- Relevant risk: RISK-0001 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#nfr-0015) -> TEST-0163, TEST-0164; design/implementation/executable evidence/approval pending as declared above.

### NFR-0016 — Upgrade preservation
- Description: Supported upgrade scenarios preserve client/project metadata, templates, history and approved outputs with pre/post verification and documented recovery.
- Business rationale: Protect existing local work.
- Source: S1 + S2; derived proposed target (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Supported upgrade scenarios preserve client/project metadata, templates, history and approved outputs with pre/post verification and documented recovery.
- Negative/boundary acceptance: Interrupted/failed upgrade either restores usable previous state or exposes an explicit recovery procedure; no silent deletion.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#nfr-0016) -> TEST-0165, TEST-0166; design/implementation/executable evidence/approval pending as declared above.

### NFR-0017 — Testability
- Description: Every approved REQ/NFR has defined tests/fixtures, declared environment, actual result and evidence at its implementation/release gate; zero-test runs cannot count as coverage.
- Business rationale: Make acceptance reproducible.
- Source: S1 + S2; derived proposed target (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Every approved REQ/NFR has defined tests/fixtures, declared environment, actual result and evidence at its implementation/release gate; zero-test runs cannot count as coverage.
- Negative/boundary acceptance: Unavailable tests are NOT_RUN/BLOCKED with reasons, never PASS.
- Relevant risk: RISK-0004 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#nfr-0017) -> TEST-0167, TEST-0168; design/implementation/executable evidence/approval pending as declared above.

### NFR-0018 — Auditability
- Description: 100% of run records and approvals link job/attempt, inputs/configuration, artifact hashes, outcome and reviewer/time; stale hashes invalidate approvals.
- Business rationale: Trace decisions and artifacts.
- Source: S1 + S2; derived proposed target (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: 100% of run records and approvals link job/attempt, inputs/configuration, artifact hashes, outcome and reviewer/time; stale hashes invalidate approvals.
- Negative/boundary acceptance: Missing/tampered evidence is detected as unverifiable; no claim of cryptographic identity or tamper-proof storage is assumed.
- Relevant risk: RISK-0004 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#nfr-0018) -> TEST-0169, TEST-0170; design/implementation/executable evidence/approval pending as declared above.

### NFR-0019 — Determinism
- Description: With identical input/configuration/tool versions, 3 repeated deterministic local runs have identical normalized data/content and validation findings; variable timestamps/IDs are documented exclusions.
- Business rationale: Support repeatable local outcomes.
- Source: S1 + S2; derived proposed target (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: With identical input/configuration/tool versions, 3 repeated deterministic local runs have identical normalized data/content and validation findings; variable timestamps/IDs are documented exclusions.
- Negative/boundary acceptance: Live website observations are time-dependent and record capture context; do not assert identical live content.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#nfr-0019) -> TEST-0171, TEST-0172; design/implementation/executable evidence/approval pending as declared above.

### NFR-0020 — Dependency and licensing compliance
- Description: Before adoption, 100% of runtime dependencies have provenance/version/license/obligations and Windows support assessment; all redistribution obligations are met.
- Business rationale: Keep product lawful and free to run.
- Source: S1 + S2; derived proposed target (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Before adoption, 100% of runtime dependencies have provenance/version/license/obligations and Windows support assessment; all redistribution obligations are met.
- Negative/boundary acceptance: Unknown/incompatible licenses block selection; proprietary required runtime or paid API fails policy compliance.
- Relevant risk: RISK-0001 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#nfr-0020) -> TEST-0173, TEST-0174; design/implementation/executable evidence/approval pending as declared above.

### NFR-0021 — No runtime AI
- Description: All release-critical workflows pass with AI services unavailable; dependency/source/network review finds zero required runtime AI integrations.
- Business rationale: Run independently of development AI.
- Source: S1 + S2; derived proposed target (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: All release-critical workflows pass with AI services unavailable; dependency/source/network review finds zero required runtime AI integrations.
- Negative/boundary acceptance: A missing development AI credential cannot prevent installation, launch or job execution.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#nfr-0021) -> TEST-0175, TEST-0176; design/implementation/executable evidence/approval pending as declared above.

### NFR-0022 — Safe recovery logs
- Description: Each failure/cancellation/interruption records safe cause and next action; seeded secrets appear zero times in logs, and configurable retention deletes only consented managed data.
- Business rationale: Enable diagnosis without exposure.
- Source: S1 + S2; derived proposed target (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Each failure/cancellation/interruption records safe cause and next action; seeded secrets appear zero times in logs, and configurable retention deletes only consented managed data.
- Negative/boundary acceptance: Log write failure is surfaced and does not cause unauthorized writes or input deletion.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#nfr-0022) -> TEST-0177, TEST-0178; design/implementation/executable evidence/approval pending as declared above.

### NFR-0023 — Authorization enforcement
- Description: 100% of unauthorized host/path/action/expiry/redirect test cases are blocked before the prohibited request; TLS verification remains enabled.
- Business rationale: Limit network effects.
- Source: S1 + S2; derived proposed target (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: 100% of unauthorized host/path/action/expiry/redirect test cases are blocked before the prohibited request; TLS verification remains enabled.
- Negative/boundary acceptance: Network-enabled modules cannot bypass authorization through assets, redirects or retries.
- Relevant risk: RISK-0003 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#nfr-0023) -> TEST-0179, TEST-0180; design/implementation/executable evidence/approval pending as declared above.

### NFR-0024 — Efficient disk management
- Description: Show planned/estimated output and backup storage before disk-intensive work; storage-shortage suite produces explicit failures without damaging originals; estimates are labeled.
- Business rationale: Avoid avoidable data exhaustion.
- Source: S1 + S2; derived proposed target (S3 details pending owner review).
- Priority: MUST; status: PROPOSED; feasibility: pending P3/P5.
- Acceptance criteria: Show planned/estimated output and backup storage before disk-intensive work; storage-shortage suite produces explicit failures without damaging originals; estimates are labeled.
- Negative/boundary acceptance: Cleanup never deletes client originals, unselected exports or unrelated files to regain space.
- Relevant risk: RISK-0002 (see [risk register](09-execution-book.md)).
- Traceability: [matrix row](../test-matrix/P1-requirements-matrix.md#nfr-0024) -> TEST-0181, TEST-0182; design/implementation/executable evidence/approval pending as declared above.

## Catalog acceptance and maintenance
Every requested functional area and quality category is represented, module boundaries are explicit, entries have observable normal and adverse acceptance and valid trace links, and proposed versus verified states are distinguished. Requirement changes retain IDs, record rationale and update linked tests; superseded entries retain replacement links. Equivalent behavior is centralized: shared workflow requirements govern every module, while module entries describe category-specific behavior. Approval and next-phase authorization remain separate gates.

[Execution state](09-execution-book.md) · [P1 report](../milestone-reports/MS-0002-P1.md) · [Trace matrix and defined tests](../test-matrix/P1-requirements-matrix.md)
