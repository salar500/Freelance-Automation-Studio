# P2 failure and recovery catalog

Status: PROPOSED UX; no fault injection performed. Common error layout: **What happened / What was affected / What can you do next** plus job/attempt/item reference, safe detail and linked field/evidence. Blocking errors persist in the view, announce accessibly and never disappear solely into a toast. Do not expose secrets or full client content in generic messages. [Screens](P2-screens.md) own detailed states; [workflow guards](P2-workflows.md) govern effects/approval; [UX book](../governance/02-ux-design-book.md) owns focus/announcement standards.

## UX-E01 — Invalid inputs
- What happened: A required field/rule is invalid.
- What was affected: The draft cannot be planned; valid fields are retained.
- What next: Use the linked error summary to correct the field and revalidate.
- Presentation / recovery: UX-S05 UX-S07; focus a linked error summary after user submission; asynchronous failures announce status without stealing focus. Safe Cancel/Back/View evidence remain available as appropriate. Retry is never an automatic permission grant.
- Related requirements: REQ-0008; conditional references via [coverage](../test-matrix/P2-ux-coverage.md).
- Acceptance: show this cause, impacted scope and permitted next action; preserve draft/original/history; keep affected delivery eligibility blocked until the defined guard is satisfied. TEST-0215 defines the corresponding future interaction case; NOT_RUN.

## UX-E02 — Unsupported formats
- What happened: The selected format or embedded feature is unsupported under the active profile.
- What was affected: That file/operation is not processed; source remains unchanged.
- What next: Choose a supported operation/file or leave draft pending capability assessment.
- Presentation / recovery: UX-S06 UX-S07; focus a linked error summary after user submission; asynchronous failures announce status without stealing focus. Safe Cancel/Back/View evidence remain available as appropriate. Retry is never an automatic permission grant.
- Related requirements: REQ-0032; conditional references via [coverage](../test-matrix/P2-ux-coverage.md).
- Acceptance: show this cause, impacted scope and permitted next action; preserve draft/original/history; keep affected delivery eligibility blocked until the defined guard is satisfied. TEST-0216 defines the corresponding future interaction case; NOT_RUN.

## UX-E03 — Missing files
- What happened: A selected input no longer exists or is unreadable.
- What was affected: Its plan fingerprint is stale; affected execution is blocked.
- What next: Locate a supported replacement or restore access, revalidate and reconfirm the plan.
- Presentation / recovery: UX-S07 UX-S09; focus a linked error summary after user submission; asynchronous failures announce status without stealing focus. Safe Cancel/Back/View evidence remain available as appropriate. Retry is never an automatic permission grant.
- Related requirements: REQ-0005 REQ-0009; conditional references via [coverage](../test-matrix/P2-ux-coverage.md).
- Acceptance: show this cause, impacted scope and permitted next action; preserve draft/original/history; keep affected delivery eligibility blocked until the defined guard is satisfied. TEST-0217 defines the corresponding future interaction case; NOT_RUN.

## UX-E04 — Corrupt documents
- What happened: Document parsing failed; no unsupported repair is silently attempted.
- What was affected: That item is failed; other items follow the explicit continue-on-error choice.
- What next: Replace the file or inspect safe diagnostic cause and rerun validation.
- Presentation / recovery: UX-S07 UX-S12; focus a linked error summary after user submission; asynchronous failures announce status without stealing focus. Safe Cancel/Back/View evidence remain available as appropriate. Retry is never an automatic permission grant.
- Related requirements: REQ-0051 REQ-0057; conditional references via [coverage](../test-matrix/P2-ux-coverage.md).
- Acceptance: show this cause, impacted scope and permitted next action; preserve draft/original/history; keep affected delivery eligibility blocked until the defined guard is satisfied. TEST-0218 defines the corresponding future interaction case; NOT_RUN.

## UX-E05 — Network unavailable
- What happened: The authorized live target cannot be reached, timed out or failed verified TLS.
- What was affected: Website steps are failed/blocked/not run; local workflows remain usable.
- What next: Check connectivity/target availability and start a linked retry with valid authorization; no TLS bypass.
- Presentation / recovery: UX-S09 UX-S10 UX-S14; focus a linked error summary after user submission; asynchronous failures announce status without stealing focus. Safe Cancel/Back/View evidence remain available as appropriate. Retry is never an automatic permission grant.
- Related requirements: REQ-0027 REQ-0043; conditional references via [coverage](../test-matrix/P2-ux-coverage.md).
- Acceptance: show this cause, impacted scope and permitted next action; preserve draft/original/history; keep affected delivery eligibility blocked until the defined guard is satisfied. TEST-0219 defines the corresponding future interaction case; NOT_RUN.

## UX-E06 — Unauthorized websites
- What happened: Host/path/action/redirect is missing authorization, out of scope or expired.
- What was affected: The prohibited request is not sent; affected step is blocked.
- What next: Obtain valid target permission or narrow the plan; editing permission needs revalidation.
- Presentation / recovery: UX-S09 UX-S14; focus a linked error summary after user submission; asynchronous failures announce status without stealing focus. Safe Cancel/Back/View evidence remain available as appropriate. Retry is never an automatic permission grant.
- Related requirements: REQ-0028 REQ-0042; conditional references via [coverage](../test-matrix/P2-ux-coverage.md).
- Acceptance: show this cause, impacted scope and permitted next action; preserve draft/original/history; keep affected delivery eligibility blocked until the defined guard is satisfied. TEST-0220 defines the corresponding future interaction case; NOT_RUN.

## UX-E07 — Processing cancellation
- What happened: Cancellation was requested; currently active work may be reaching a safe stopping point.
- What was affected: No new item starts; show cancellation requested until actual cancelled/partial outcome.
- What next: Inspect item dispositions; eligible new retry requires a fresh plan; do not approve incomplete outputs.
- Presentation / recovery: UX-S10 UX-S11; focus a linked error summary after user submission; asynchronous failures announce status without stealing focus. Safe Cancel/Back/View evidence remain available as appropriate. Retry is never an automatic permission grant.
- Related requirements: REQ-0013 REQ-0015; conditional references via [coverage](../test-matrix/P2-ux-coverage.md).
- Acceptance: show this cause, impacted scope and permitted next action; preserve draft/original/history; keep affected delivery eligibility blocked until the defined guard is satisfied. TEST-0221 defines the corresponding future interaction case; NOT_RUN.

## UX-E08 — Worker crashes
- What happened: The execution component stopped unexpectedly (no worker-process architecture is assumed).
- What was affected: Attempt status is failed/interrupted/unverifiable until evidence reconciliation; no success badge.
- What next: Inspect preserved evidence; use capability-supported recovery or linked safe retry.
- Presentation / recovery: UX-S10 UX-S20; focus a linked error summary after user submission; asynchronous failures announce status without stealing focus. Safe Cancel/Back/View evidence remain available as appropriate. Retry is never an automatic permission grant.
- Related requirements: REQ-0014 REQ-0016; conditional references via [coverage](../test-matrix/P2-ux-coverage.md).
- Acceptance: show this cause, impacted scope and permitted next action; preserve draft/original/history; keep affected delivery eligibility blocked until the defined guard is satisfied. TEST-0222 defines the corresponding future interaction case; NOT_RUN.

## UX-E09 — Interrupted jobs
- What happened: A prior run has no verified terminal outcome after restart.
- What was affected: Partial outputs and previous attempt stay visible and unapproved.
- What next: Inspect recovery options; resume only if supported and revalidated, otherwise new isolated retry.
- Presentation / recovery: UX-S01 UX-S11; focus a linked error summary after user submission; asynchronous failures announce status without stealing focus. Safe Cancel/Back/View evidence remain available as appropriate. Retry is never an automatic permission grant.
- Related requirements: REQ-0016; conditional references via [coverage](../test-matrix/P2-ux-coverage.md).
- Acceptance: show this cause, impacted scope and permitted next action; preserve draft/original/history; keep affected delivery eligibility blocked until the defined guard is satisfied. TEST-0223 defines the corresponding future interaction case; NOT_RUN.

## UX-E10 — Low storage
- What happened: Available local storage is insufficient or writing failed.
- What was affected: Affected output/evidence/package is not completed; original inputs remain intact.
- What next: Choose another local destination or explicitly manage selected generated records; never automatic cleanup.
- Presentation / recovery: UX-S09 UX-S18 UX-S17; focus a linked error summary after user submission; asynchronous failures announce status without stealing focus. Safe Cancel/Back/View evidence remain available as appropriate. Retry is never an automatic permission grant.
- Related requirements: NFR-0024 REQ-0026; conditional references via [coverage](../test-matrix/P2-ux-coverage.md).
- Acceptance: show this cause, impacted scope and permitted next action; preserve draft/original/history; keep affected delivery eligibility blocked until the defined guard is satisfied. TEST-0224 defines the corresponding future interaction case; NOT_RUN.

## UX-E11 — Export failures
- What happened: Package/report could not be fully written or verified.
- What was affected: List destination files actually written, incomplete items and unchanged source artifacts.
- What next: Choose another name/destination or retry after resolving access/space and current hash checks.
- Presentation / recovery: UX-S17; focus a linked error summary after user submission; asynchronous failures announce status without stealing focus. Safe Cancel/Back/View evidence remain available as appropriate. Retry is never an automatic permission grant.
- Related requirements: REQ-0023; conditional references via [coverage](../test-matrix/P2-ux-coverage.md).
- Acceptance: show this cause, impacted scope and permitted next action; preserve draft/original/history; keep affected delivery eligibility blocked until the defined guard is satisfied. TEST-0225 defines the corresponding future interaction case; NOT_RUN.

## UX-E12 — Partial completion
- What happened: Some items finished and some failed/cancelled/not run.
- What was affected: Whole job remains partial; successful items retain per-item validation/evidence.
- What next: Inspect failures; retry or propose only an independently valid explicitly reviewed subset, showing all exclusions.
- Presentation / recovery: UX-S10 UX-S12 UX-S16; focus a linked error summary after user submission; asynchronous failures announce status without stealing focus. Safe Cancel/Back/View evidence remain available as appropriate. Retry is never an automatic permission grant.
- Related requirements: REQ-0011 REQ-0018 REQ-0022; conditional references via [coverage](../test-matrix/P2-ux-coverage.md).
- Acceptance: show this cause, impacted scope and permitted next action; preserve draft/original/history; keep affected delivery eligibility blocked until the defined guard is satisfied. TEST-0226 defines the corresponding future interaction case; NOT_RUN.

## UX-E13 — Retry and recovery
- What happened: A failed/cancelled/interrupted job is being reconsidered.
- What was affected: New attempt/recovery choices show changed inputs and prior evidence; no inherited approval.
- What next: Revalidate inputs/rules/permissions and isolate new outputs; unsupported resume offers safe retry only.
- Presentation / recovery: UX-S11 UX-S09; focus a linked error summary after user submission; asynchronous failures announce status without stealing focus. Safe Cancel/Back/View evidence remain available as appropriate. Retry is never an automatic permission grant.
- Related requirements: REQ-0015 REQ-0016; conditional references via [coverage](../test-matrix/P2-ux-coverage.md).
- Acceptance: show this cause, impacted scope and permitted next action; preserve draft/original/history; keep affected delivery eligibility blocked until the defined guard is satisfied. TEST-0227 defines the corresponding future interaction case; NOT_RUN.

## UX-E14 — Stale approval or evidence
- What happened: Selected artifact/evidence changed or became unavailable since approval.
- What was affected: Affected approval is stale/unverifiable and delivery export is blocked.
- What next: Inspect differences, revalidate/review exact selection and obtain fresh final approval.
- Presentation / recovery: UX-S13 UX-S16 UX-S17; focus a linked error summary after user submission; asynchronous failures announce status without stealing focus. Safe Cancel/Back/View evidence remain available as appropriate. Retry is never an automatic permission grant.
- Related requirements: REQ-0020 REQ-0031 NFR-0018; conditional references via [coverage](../test-matrix/P2-ux-coverage.md).
- Acceptance: show this cause, impacted scope and permitted next action; preserve draft/original/history; keep affected delivery eligibility blocked until the defined guard is satisfied. TEST-0228 defines the corresponding future interaction case; NOT_RUN.

## Additional error boundaries
Settings save and history/diagnostics read failures are specified in UX-S11/19/20. Input/output collision and backup failures are covered by plan consent/module scope. If local evidence cannot be persisted, show unavailable evidence and prevent success/approval; a transient UI alert is not a durable job report. Screens retain available information while marking it stale instead of claiming current validation. Persistent diagnostic storage failure is a surfaced unrecoverable prerequisite until a valid local location exists.

## Catalog acceptance
All requested failure classes are present with truthful outcome, affected scope, keyboard-accessible next action and no automatic destructive/network/review effect. Specific error codes, filesystem/worker implementation and resumability remain P3/P5 matters.
