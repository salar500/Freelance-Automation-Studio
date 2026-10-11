# P2 screen specifications

Status: PROPOSED UX only; conditional P1 documentation approval does not approve unresolved requirements. Screen IDs are local UX references, not new REQ/ADR identifiers. Related REQ/NFR links are conditional design traceability, not a declaration that individual requirements are approved. See [UX book](../governance/02-ux-design-book.md) for design/accessibility standards and [workflows](P2-workflows.md) for guards.

## Navigation and shared shell
Six top-level areas: Dashboard; Clients & projects (two tabs); Jobs (history, draft/resume, contextual workspace); Templates; Settings & storage (two tabs); Help. One New job action is available globally with selected project prefilled. Contextual workspace tabs: Setup, Plan, Progress, Results, Review, Findings, Preview, Approval, Export. Show only relevant tabs, preserve deep links and explain unavailable prerequisites. The wizard is a guided entry to these same views, not a second disconnected configuration system. Review queue is available from Dashboard/Jobs; it is not a seventh required top-level section.

Every screen uses the same header (client/project/job/attempt where applicable), left navigation, main content and status/footer. Detail/action panels remain contextual. Resizing collapses secondary panels with an accessible disclosure, not hidden essential actions. Screens listed below are all specified; logical screens can share a route/tab without losing their independent acceptance criteria.

Shared keyboard contract K: Tab/Shift+Tab follow visible reading order; Enter/Space activate focused controls; arrow keys navigate single composite lists/tabs; Esc closes a cancellable modal and restores invoker focus, never discards unsaved edits silently. Accessible names include purpose/context; status changes announced without moving focus. Read-only viewing never starts jobs or network requests. The per-screen row supplements K. Actual screen-reader/keyboard usability remains NOT_RUN.

## UX-S01 — Dashboard
- Purpose: Orient the operator to local work and pending review.
- User entry points: Launch; Home navigation.
- Layout structure: shared header/navigation; main dashboard work area; contextual detail panel; persistent primary/secondary action row with status.
- UI components: Recent projects, active jobs, review queue, New job action, local/offline indicator.
- User actions: Open project, resume draft, inspect running job, open review queue.
- Required inputs: Existing local project/job summaries; no input required to inspect.
- Validation: Show missing records as unavailable, not successful.
- Default state: read/view or editable draft only; no destructive action, job start, approval or request selected/triggered automatically. Existing project context is prefilled where applicable.
- Empty state: No jobs yet: Create client/project or New job.
- Loading state: label “Loading dashboard”; retain prior context but mark stale values; block actions requiring fresh data; allow safe navigation. Job monitoring uses actual progress, never a generic completed indicator.
- Success state: show confirmed result of the named action with record/attempt/artifact identity; saving/viewing success does not imply processing success, validation success or delivery approval.
- Failure state: Local summary unreadable: affected cards unavailable, safe cause shown.
- Warning state: Interrupted jobs and pending reviews shown separately from successful results.
- Recovery actions: Open history/diagnostics or retry reading summaries; never auto-resume.
- Keyboard accessibility: K applies; name all dashboard controls; error-summary links move to the affected field; tables expose headers and selected-item context; dialogs return focus to their invoker.
- Related requirements: REQ-0001, REQ-0012, REQ-0016, REQ-0024, REQ-0027, NFR-0001. Exact SRS entries remain proposed; [coverage matrix](../test-matrix/P2-ux-coverage.md) provides links/status.
- Acceptance criteria: walk the stated entry -> inputs -> action -> visible outcome; verify required-field rejection, the stated empty/loading/failure/warning paths, accessible action order and recoverability without losing unrelated draft/history. No action may bypass the [review/approval guards](P2-workflows.md#review-and-approval-model).
- Defined review case: TEST-0183 in [UX review register](../test-matrix/P2-ux-coverage.md); no application verification claimed.

Text wireframe (logical regions, not pixel implementation):
```text
[Context: Client / Project / Job / Attempt] [Local/network status]
[Navigation] | Dashboard: Recent projects
             | Selected item / fields / evidence / inline findings
             | [Safe secondary actions] [Guarded primary action]
[Actual state / affected items / next available action]
```

## UX-S02 — Client Management
- Purpose: Organize local client records.
- User entry points: Clients & projects navigation; wizard client picker.
- Layout structure: shared header/navigation; main client management work area; contextual detail panel; persistent primary/secondary action row with status.
- UI components: Client list/search, details pane, name/notes form, archive dialog.
- User actions: Create/edit/archive client; open its projects.
- Required inputs: Display name required; notes optional.
- Validation: Trim whitespace for blank-name rejection; expose identity separately from name.
- Default state: read/view or editable draft only; no destructive action, job start, approval or request selected/triggered automatically. Existing project context is prefilled where applicable.
- Empty state: No clients: Add client; blank optional notes allowed.
- Loading state: label “Loading client management”; retain prior context but mark stale values; block actions requiring fresh data; allow safe navigation. Job monitoring uses actual progress, never a generic completed indicator.
- Success state: show confirmed result of the named action with record/attempt/artifact identity; saving/viewing success does not imply processing success, validation success or delivery approval.
- Failure state: Save failure retains edits and identifies affected record.
- Warning state: Archive affects visibility, not history or original files.
- Recovery actions: Retry save or cancel/discard; archived references remain inspectable.
- Keyboard accessibility: K applies; name all client management controls; error-summary links move to the affected field; tables expose headers and selected-item context; dialogs return focus to their invoker.
- Related requirements: REQ-0002, REQ-0001, NFR-0005. Exact SRS entries remain proposed; [coverage matrix](../test-matrix/P2-ux-coverage.md) provides links/status.
- Acceptance criteria: walk the stated entry -> inputs -> action -> visible outcome; verify required-field rejection, the stated empty/loading/failure/warning paths, accessible action order and recoverability without losing unrelated draft/history. No action may bypass the [review/approval guards](P2-workflows.md#review-and-approval-model).
- Defined review case: TEST-0184 in [UX review register](../test-matrix/P2-ux-coverage.md); no application verification claimed.

Text wireframe (logical regions, not pixel implementation):
```text
[Context: Client / Project / Job / Attempt] [Local/network status]
[Navigation] | Client Management: Client list/search
             | Selected item / fields / evidence / inline findings
             | [Safe secondary actions] [Guarded primary action]
[Actual state / affected items / next available action]
```

## UX-S03 — Project Management
- Purpose: Separate client workspaces and jobs.
- User entry points: Clients & projects Projects tab; client detail; wizard picker.
- Layout structure: shared header/navigation; main project management work area; contextual detail panel; persistent primary/secondary action row with status.
- UI components: Project list, client reference, workspace picker, project jobs.
- User actions: Create/edit project; inspect workspace; open jobs.
- Required inputs: Client, project name, local workspace.
- Validation: Reject missing client/name or unavailable path before saving.
- Default state: read/view or editable draft only; no destructive action, job start, approval or request selected/triggered automatically. Existing project context is prefilled where applicable.
- Empty state: No projects: Create project with client context retained.
- Loading state: label “Loading project management”; retain prior context but mark stale values; block actions requiring fresh data; allow safe navigation. Job monitoring uses actual progress, never a generic completed indicator.
- Success state: show confirmed result of the named action with record/attempt/artifact identity; saving/viewing success does not imply processing success, validation success or delivery approval.
- Failure state: Workspace missing: keep project record and show job-input availability.
- Warning state: Changing workspace changes future defaults, not old job references.
- Recovery actions: Choose valid path or retry access; no implicit moving of files.
- Keyboard accessibility: K applies; name all project management controls; error-summary links move to the affected field; tables expose headers and selected-item context; dialogs return focus to their invoker.
- Related requirements: REQ-0003, REQ-0024, REQ-0001. Exact SRS entries remain proposed; [coverage matrix](../test-matrix/P2-ux-coverage.md) provides links/status.
- Acceptance criteria: walk the stated entry -> inputs -> action -> visible outcome; verify required-field rejection, the stated empty/loading/failure/warning paths, accessible action order and recoverability without losing unrelated draft/history. No action may bypass the [review/approval guards](P2-workflows.md#review-and-approval-model).
- Defined review case: TEST-0185 in [UX review register](../test-matrix/P2-ux-coverage.md); no application verification claimed.

Text wireframe (logical regions, not pixel implementation):
```text
[Context: Client / Project / Job / Attempt] [Local/network status]
[Navigation] | Project Management: Project list
             | Selected item / fields / evidence / inline findings
             | [Safe secondary actions] [Guarded primary action]
[Actual state / affected items / next available action]
```

## UX-S04 — New Job Wizard
- Purpose: Guide a complete job without redundant entry.
- User entry points: Global New job; dashboard/project contextual action.
- Layout structure: shared header/navigation; main new job wizard work area; contextual detail panel; persistent primary/secondary action row with status.
- UI components: Twelve-step progress map, draft summary, Back/Next/Save draft/Exit.
- User actions: Select client/project, move through setup, save/resume draft.
- Required inputs: Client/project and subsequent step-specific fields.
- Validation: Next validates current step; Start requires all validation and consent.
- Default state: read/view or editable draft only; no destructive action, job start, approval or request selected/triggered automatically. Existing project context is prefilled where applicable.
- Empty state: New draft with project prefilled when contextual.
- Loading state: label “Loading new job wizard”; retain prior context but mark stale values; block actions requiring fresh data; allow safe navigation. Job monitoring uses actual progress, never a generic completed indicator.
- Success state: show confirmed result of the named action with record/attempt/artifact identity; saving/viewing success does not imply processing success, validation success or delivery approval.
- Failure state: Invalid/missing step input: inline errors plus linked summary.
- Warning state: Exit with unsaved changes offers Save/Discard/Cancel.
- Recovery actions: Return to offending step preserving entered values.
- Keyboard accessibility: K applies; name all new job wizard controls; error-summary links move to the affected field; tables expose headers and selected-item context; dialogs return focus to their invoker.
- Related requirements: REQ-0004, REQ-0009, REQ-0001, REQ-0025, NFR-0007. Exact SRS entries remain proposed; [coverage matrix](../test-matrix/P2-ux-coverage.md) provides links/status.
- Acceptance criteria: walk the stated entry -> inputs -> action -> visible outcome; verify required-field rejection, the stated empty/loading/failure/warning paths, accessible action order and recoverability without losing unrelated draft/history. No action may bypass the [review/approval guards](P2-workflows.md#review-and-approval-model).
- Defined review case: TEST-0186 in [UX review register](../test-matrix/P2-ux-coverage.md); no application verification claimed.

Text wireframe (logical regions, not pixel implementation):
```text
[Context: Client / Project / Job / Attempt] [Local/network status]
[Navigation] | New Job Wizard: Twelve-step progress map
             | Selected item / fields / evidence / inline findings
             | [Safe secondary actions] [Guarded primary action]
[Actual state / affected items / next available action]
```

## UX-S05 — Job Configuration
- Purpose: Configure declared module rules and outputs.
- User entry points: Wizard Configure; draft detail Edit configuration.
- Layout structure: shared header/navigation; main job configuration work area; contextual detail panel; persistent primary/secondary action row with status.
- UI components: Module-specific form, preview, output path, continue-on-error choice, effective defaults.
- User actions: Edit rules, preview, reset a field, inspect proposed defaults.
- Required inputs: Module options and output destination; module schema details in module spec.
- Validation: Reject incompatible fields, missing rule inputs and colliding paths before plan.
- Default state: read/view or editable draft only; no destructive action, job start, approval or request selected/triggered automatically. Existing project context is prefilled where applicable.
- Empty state: No configuration: show required options, no guessed destructive operation.
- Loading state: label “Loading job configuration”; retain prior context but mark stale values; block actions requiring fresh data; allow safe navigation. Job monitoring uses actual progress, never a generic completed indicator.
- Success state: show confirmed result of the named action with record/attempt/artifact identity; saving/viewing success does not imply processing success, validation success or delivery approval.
- Failure state: Preview/config validation failure identifies exact option and preserves draft.
- Warning state: Unsupported capability or template change requires explicit correction.
- Recovery actions: Correct rule/path or select supported capability; regenerate plan.
- Keyboard accessibility: K applies; name all job configuration controls; error-summary links move to the affected field; tables expose headers and selected-item context; dialogs return focus to their invoker.
- Related requirements: REQ-0008, REQ-0009, REQ-0025, REQ-0029, REQ-0032. Exact SRS entries remain proposed; [coverage matrix](../test-matrix/P2-ux-coverage.md) provides links/status.
- Acceptance criteria: walk the stated entry -> inputs -> action -> visible outcome; verify required-field rejection, the stated empty/loading/failure/warning paths, accessible action order and recoverability without losing unrelated draft/history. No action may bypass the [review/approval guards](P2-workflows.md#review-and-approval-model).
- Defined review case: TEST-0187 in [UX review register](../test-matrix/P2-ux-coverage.md); no application verification claimed.

Text wireframe (logical regions, not pixel implementation):
```text
[Context: Client / Project / Job / Attempt] [Local/network status]
[Navigation] | Job Configuration: Module-specific form
             | Selected item / fields / evidence / inline findings
             | [Safe secondary actions] [Guarded primary action]
[Actual state / affected items / next available action]
```

## UX-S06 — Automation Module Selection
- Purpose: Choose one of four initial categories.
- User entry points: Wizard Select category; draft module change.
- Layout structure: shared header/navigation; main automation module selection work area; contextual detail panel; persistent primary/secondary action row with status.
- UI components: Four labeled category cards, capabilities/limits, local/network labels.
- User actions: Select module; inspect capability limitations.
- Required inputs: One category and supported operation.
- Validation: Unavailable operation cannot be selected for execution.
- Default state: read/view or editable draft only; no destructive action, job start, approval or request selected/triggered automatically. Existing project context is prefilled where applicable.
- Empty state: No category selected; Next disabled with reason.
- Loading state: label “Loading automation module selection”; retain prior context but mark stale values; block actions requiring fresh data; allow safe navigation. Job monitoring uses actual progress, never a generic completed indicator.
- Success state: show confirmed result of the named action with record/attempt/artifact identity; saving/viewing success does not imply processing success, validation success or delivery approval.
- Failure state: Capability list unreadable: selection unavailable rather than guessed.
- Warning state: Module change may invalidate inputs/rules; confirm before applying.
- Recovery actions: Keep old module or revalidate retained draft fields.
- Keyboard accessibility: K applies; name all automation module selection controls; error-summary links move to the affected field; tables expose headers and selected-item context; dialogs return focus to their invoker.
- Related requirements: REQ-0006, REQ-0032, NFR-0010, REQ-0027. Exact SRS entries remain proposed; [coverage matrix](../test-matrix/P2-ux-coverage.md) provides links/status.
- Acceptance criteria: walk the stated entry -> inputs -> action -> visible outcome; verify required-field rejection, the stated empty/loading/failure/warning paths, accessible action order and recoverability without losing unrelated draft/history. No action may bypass the [review/approval guards](P2-workflows.md#review-and-approval-model).
- Defined review case: TEST-0188 in [UX review register](../test-matrix/P2-ux-coverage.md); no application verification claimed.

Text wireframe (logical regions, not pixel implementation):
```text
[Context: Client / Project / Job / Attempt] [Local/network status]
[Navigation] | Automation Module Selection: Four labeled category cards
             | Selected item / fields / evidence / inline findings
             | [Safe secondary actions] [Guarded primary action]
[Actual state / affected items / next available action]
```

## UX-S07 — Input File Management
- Purpose: Inspect selected local files or declared website targets.
- User entry points: Wizard Inputs; config input link.
- Layout structure: shared header/navigation; main input file management work area; contextual detail panel; persistent primary/secondary action row with status.
- UI components: File list with path/size/format/status, preview, Add/Remove, website target/scope form.
- User actions: Choose files/folder within scope; remove reference; preview; enter target without requesting it.
- Required inputs: Supported file references or authorized target declaration.
- Validation: Detect missing/unreadable/unsupported files and preview ambiguity; no macro/script execution.
- Default state: read/view or editable draft only; no destructive action, job start, approval or request selected/triggered automatically. Existing project context is prefilled where applicable.
- Empty state: No inputs: explain module-specific required type.
- Loading state: label “Loading input file management”; retain prior context but mark stale values; block actions requiring fresh data; allow safe navigation. Job monitoring uses actual progress, never a generic completed indicator.
- Success state: show confirmed result of the named action with record/attempt/artifact identity; saving/viewing success does not imply processing success, validation success or delivery approval.
- Failure state: Corrupt input/preview failure identifies file and safe reason.
- Warning state: Preview may be limited; local client files cannot become website request data.
- Recovery actions: Replace reference, choose explicit parser options or return to module choice.
- Keyboard accessibility: K applies; name all input file management controls; error-summary links move to the affected field; tables expose headers and selected-item context; dialogs return focus to their invoker.
- Related requirements: REQ-0005, REQ-0008, REQ-0028, REQ-0030, REQ-0032, NFR-0004. Exact SRS entries remain proposed; [coverage matrix](../test-matrix/P2-ux-coverage.md) provides links/status.
- Acceptance criteria: walk the stated entry -> inputs -> action -> visible outcome; verify required-field rejection, the stated empty/loading/failure/warning paths, accessible action order and recoverability without losing unrelated draft/history. No action may bypass the [review/approval guards](P2-workflows.md#review-and-approval-model).
- Defined review case: TEST-0189 in [UX review register](../test-matrix/P2-ux-coverage.md); no application verification claimed.

Text wireframe (logical regions, not pixel implementation):
```text
[Context: Client / Project / Job / Attempt] [Local/network status]
[Navigation] | Input File Management: File list with path/size/format/status
             | Selected item / fields / evidence / inline findings
             | [Safe secondary actions] [Guarded primary action]
[Actual state / affected items / next available action]
```

## UX-S08 — Templates
- Purpose: Reuse configuration without inheriting permissions.
- User entry points: Templates navigation; wizard optional template step.
- Layout structure: shared header/navigation; main templates work area; contextual detail panel; persistent primary/secondary action row with status.
- UI components: Template list/version/module tags, config summary, apply-diff, save template form.
- User actions: Create/edit/version template; apply to independent draft; decline changes.
- Required inputs: Template name and nonsecret supported options.
- Validation: No client contents/credentials/consent stored; compatibility checked.
- Default state: read/view or editable draft only; no destructive action, job start, approval or request selected/triggered automatically. Existing project context is prefilled where applicable.
- Empty state: No templates: continue without template or save configuration.
- Loading state: label “Loading templates”; retain prior context but mark stale values; block actions requiring fresh data; allow safe navigation. Job monitoring uses actual progress, never a generic completed indicator.
- Success state: show confirmed result of the named action with record/attempt/artifact identity; saving/viewing success does not imply processing success, validation success or delivery approval.
- Failure state: Invalid/obsolete template options require correction before use.
- Warning state: Applying after configuration shows changed fields; never inherits old consent.
- Recovery actions: Cancel apply or fix incompatible fields and revalidate.
- Keyboard accessibility: K applies; name all templates controls; error-summary links move to the affected field; tables expose headers and selected-item context; dialogs return focus to their invoker.
- Related requirements: REQ-0007, REQ-0008, REQ-0009, REQ-0010. Exact SRS entries remain proposed; [coverage matrix](../test-matrix/P2-ux-coverage.md) provides links/status.
- Acceptance criteria: walk the stated entry -> inputs -> action -> visible outcome; verify required-field rejection, the stated empty/loading/failure/warning paths, accessible action order and recoverability without losing unrelated draft/history. No action may bypass the [review/approval guards](P2-workflows.md#review-and-approval-model).
- Defined review case: TEST-0190 in [UX review register](../test-matrix/P2-ux-coverage.md); no application verification claimed.

Text wireframe (logical regions, not pixel implementation):
```text
[Context: Client / Project / Job / Attempt] [Local/network status]
[Navigation] | Templates: Template list/version/module tags
             | Selected item / fields / evidence / inline findings
             | [Safe secondary actions] [Guarded primary action]
[Actual state / affected items / next available action]
```

## UX-S09 — Execution Plan and Authorization
- Purpose: Make effects and permissions explicit before execution.
- User entry points: Wizard Preview plan/Permissions; changed-plan prompt.
- Layout structure: shared header/navigation; main execution plan and authorization work area; contextual detail panel; persistent primary/secondary action row with status.
- UI components: Read-only plan, input fingerprints, effects/paths, storage estimate, network scope, authorization evidence, separate consent controls.
- User actions: Inspect plan; record website permission; confirm plan and each destructive operation; Start.
- Required inputs: Current inputs/config; host/path/actions/expiry/permission reference when network required.
- Validation: Changed plan/input invalidates confirmation; expired/missing/out-of-scope authorization blocks Start.
- Default state: read/view or editable draft only; no destructive action, job start, approval or request selected/triggered automatically. Existing project context is prefilled where applicable.
- Empty state: No valid plan: return to configuration; no automatic consent.
- Loading state: label “Loading execution plan and authorization”; retain prior context but mark stale values; block actions requiring fresh data; allow safe navigation. Job monitoring uses actual progress, never a generic completed indicator.
- Success state: show confirmed result of the named action with record/attempt/artifact identity; saving/viewing success does not imply processing success, validation success or delivery approval.
- Failure state: Plan/evidence/storage check failure blocks execution with exact cause.
- Warning state: Output overwrite and state-changing website requests prominently identified.
- Recovery actions: Edit paths/scope or replace expired authorization; do not bypass warnings.
- Keyboard accessibility: K applies; name all execution plan and authorization controls; error-summary links move to the affected field; tables expose headers and selected-item context; dialogs return focus to their invoker.
- Related requirements: REQ-0009, REQ-0010, REQ-0028, REQ-0017, NFR-0023, NFR-0024. Exact SRS entries remain proposed; [coverage matrix](../test-matrix/P2-ux-coverage.md) provides links/status.
- Acceptance criteria: walk the stated entry -> inputs -> action -> visible outcome; verify required-field rejection, the stated empty/loading/failure/warning paths, accessible action order and recoverability without losing unrelated draft/history. No action may bypass the [review/approval guards](P2-workflows.md#review-and-approval-model).
- Defined review case: TEST-0191 in [UX review register](../test-matrix/P2-ux-coverage.md); no application verification claimed.

Text wireframe (logical regions, not pixel implementation):
```text
[Context: Client / Project / Job / Attempt] [Local/network status]
[Navigation] | Execution Plan and Authorization: Read-only plan
             | Selected item / fields / evidence / inline findings
             | [Safe secondary actions] [Guarded primary action]
[Actual state / affected items / next available action]
```

## UX-S10 — Job Progress and Monitoring
- Purpose: Show truthful processing and cancellation.
- User entry points: Confirmed Start; dashboard running job; history active attempt.
- Layout structure: shared header/navigation; main job progress and monitoring work area; contextual detail panel; persistent primary/secondary action row with status.
- UI components: Job/attempt header, phase/item counts, determinate/indeterminate progress, recent safe activity, Cancel.
- User actions: Inspect current operation; request cancellation; open per-item evidence.
- Required inputs: Confirmed plan and unique attempt ID.
- Validation: Cannot start invalid plan; estimates labeled; no percent if total unknown.
- Default state: read/view or editable draft only; no destructive action, job start, approval or request selected/triggered automatically. Existing project context is prefilled where applicable.
- Empty state: No active attempt: show saved plan and appropriate next action.
- Loading state: label “Loading job progress and monitoring”; retain prior context but mark stale values; block actions requiring fresh data; allow safe navigation. Job monitoring uses actual progress, never a generic completed indicator.
- Success state: show confirmed result of the named action with record/attempt/artifact identity; saving/viewing success does not imply processing success, validation success or delivery approval.
- Failure state: Crash/failure shows affected items and evidence status, not a completed badge.
- Warning state: Cancellation requested is not cancelled; partial outputs not delivery-approved.
- Recovery actions: Inspect outcome; eligible resume or linked retry after revalidation.
- Keyboard accessibility: K applies; name all job progress and monitoring controls; error-summary links move to the affected field; tables expose headers and selected-item context; dialogs return focus to their invoker.
- Related requirements: REQ-0011, REQ-0012, REQ-0013, REQ-0014, REQ-0015, REQ-0016, REQ-0017. Exact SRS entries remain proposed; [coverage matrix](../test-matrix/P2-ux-coverage.md) provides links/status.
- Acceptance criteria: walk the stated entry -> inputs -> action -> visible outcome; verify required-field rejection, the stated empty/loading/failure/warning paths, accessible action order and recoverability without losing unrelated draft/history. No action may bypass the [review/approval guards](P2-workflows.md#review-and-approval-model).
- Defined review case: TEST-0192 in [UX review register](../test-matrix/P2-ux-coverage.md); no application verification claimed.

Text wireframe (logical regions, not pixel implementation):
```text
[Context: Client / Project / Job / Attempt] [Local/network status]
[Navigation] | Job Progress and Monitoring: Job/attempt header
             | Selected item / fields / evidence / inline findings
             | [Safe secondary actions] [Guarded primary action]
[Actual state / affected items / next available action]
```

## UX-S11 — Job History
- Purpose: Find previous attempts and review evidence.
- User entry points: Jobs navigation History; project jobs; dashboard recent item.
- Layout structure: shared header/navigation; main job history work area; contextual detail panel; persistent primary/secondary action row with status.
- UI components: Filterable attempt table, linked retries, outcome/validation/review columns, evidence detail.
- User actions: Filter/open attempt; inspect outputs; create linked retry.
- Required inputs: Optional project/date/module/outcome filters.
- Validation: Keep processing and approval state distinct; missing external files marked unavailable.
- Default state: read/view or editable draft only; no destructive action, job start, approval or request selected/triggered automatically. Existing project context is prefilled where applicable.
- Empty state: No matching attempts: clear filters; no jobs: create job.
- Loading state: label “Loading job history”; retain prior context but mark stale values; block actions requiring fresh data; allow safe navigation. Job monitoring uses actual progress, never a generic completed indicator.
- Success state: show confirmed result of the named action with record/attempt/artifact identity; saving/viewing success does not imply processing success, validation success or delivery approval.
- Failure state: History/evidence unreadable: unavailable state with affected attempt.
- Warning state: Old approval may be stale; archived client/project labels retained.
- Recovery actions: Reconnect missing local reference, inspect diagnostics or retry without altering history.
- Keyboard accessibility: K applies; name all job history controls; error-summary links move to the affected field; tables expose headers and selected-item context; dialogs return focus to their invoker.
- Related requirements: REQ-0024, REQ-0015, REQ-0016, REQ-0017, REQ-0031. Exact SRS entries remain proposed; [coverage matrix](../test-matrix/P2-ux-coverage.md) provides links/status.
- Acceptance criteria: walk the stated entry -> inputs -> action -> visible outcome; verify required-field rejection, the stated empty/loading/failure/warning paths, accessible action order and recoverability without losing unrelated draft/history. No action may bypass the [review/approval guards](P2-workflows.md#review-and-approval-model).
- Defined review case: TEST-0193 in [UX review register](../test-matrix/P2-ux-coverage.md); no application verification claimed.

Text wireframe (logical regions, not pixel implementation):
```text
[Context: Client / Project / Job / Attempt] [Local/network status]
[Navigation] | Job History: Filterable attempt table
             | Selected item / fields / evidence / inline findings
             | [Safe secondary actions] [Guarded primary action]
[Actual state / affected items / next available action]
```

## UX-S12 — Validation Results
- Purpose: Explain output checks separately from processing.
- User entry points: Job finished; job detail Results; review prerequisite.
- Layout structure: shared header/navigation; main validation results work area; contextual detail panel; persistent primary/secondary action row with status.
- UI components: Per-output checks, counts, expected/observed details, PASS/WARNING/FAIL/NOT_RUN filters.
- User actions: Inspect evidence; send warnings to review; choose valid subset.
- Required inputs: Current output fingerprints and declared checks.
- Validation: Missing/stale checks block approval; zero checks says No checks evaluated.
- Default state: read/view or editable draft only; no destructive action, job start, approval or request selected/triggered automatically. Existing project context is prefilled where applicable.
- Empty state: No outputs/checks: say why, never all passed.
- Loading state: label “Loading validation results”; retain prior context but mark stale values; block actions requiring fresh data; allow safe navigation. Job monitoring uses actual progress, never a generic completed indicator.
- Success state: show confirmed result of the named action with record/attempt/artifact identity; saving/viewing success does not imply processing success, validation success or delivery approval.
- Failure state: Failed validation exposes affected output and prohibits its approved inclusion.
- Warning state: Warning/uncertain findings require human review.
- Recovery actions: Correct/rerun validation or review eligible uncertainty; failed check remains failed.
- Keyboard accessibility: K applies; name all validation results controls; error-summary links move to the affected field; tables expose headers and selected-item context; dialogs return focus to their invoker.
- Related requirements: REQ-0018, REQ-0039, REQ-0041, REQ-0058, NFR-0003. Exact SRS entries remain proposed; [coverage matrix](../test-matrix/P2-ux-coverage.md) provides links/status.
- Acceptance criteria: walk the stated entry -> inputs -> action -> visible outcome; verify required-field rejection, the stated empty/loading/failure/warning paths, accessible action order and recoverability without losing unrelated draft/history. No action may bypass the [review/approval guards](P2-workflows.md#review-and-approval-model).
- Defined review case: TEST-0194 in [UX review register](../test-matrix/P2-ux-coverage.md); no application verification claimed.

Text wireframe (logical regions, not pixel implementation):
```text
[Context: Client / Project / Job / Attempt] [Local/network status]
[Navigation] | Validation Results: Per-output checks
             | Selected item / fields / evidence / inline findings
             | [Safe secondary actions] [Guarded primary action]
[Actual state / affected items / next available action]
```

## UX-S13 — Exception Review Center
- Purpose: Triage uncertainty and required human decisions.
- User entry points: Review queue; validation warnings; job Review tab.
- Layout structure: shared header/navigation; main exception review center work area; contextual detail panel; persistent primary/secondary action row with status.
- UI components: Finding list, evidence comparison, reviewer label, accept/reject/rationale controls, unresolved count.
- User actions: Review uncertainty; reject; approve eligible warning with rationale; defer.
- Required inputs: Local reviewer label; decision; rationale for warning disposition.
- Validation: No automatic acceptance; stale/missing evidence blocks decision; known invalid output cannot be waived into PASS.
- Default state: read/view or editable draft only; no destructive action, job start, approval or request selected/triggered automatically. Existing project context is prefilled where applicable.
- Empty state: No review items: show actual validation summary, still require delivery approval.
- Loading state: label “Loading exception review center”; retain prior context but mark stale values; block actions requiring fresh data; allow safe navigation. Job monitoring uses actual progress, never a generic completed indicator.
- Success state: show confirmed result of the named action with record/attempt/artifact identity; saving/viewing success does not imply processing success, validation success or delivery approval.
- Failure state: Evidence unreadable: keep unresolved and block affected output.
- Warning state: Suspected website issues not verified defects; local identity is asserted.
- Recovery actions: Inspect/recreate evidence, reject or rerun job; no blanket approval of hidden items.
- Keyboard accessibility: K applies; name all exception review center controls; error-summary links move to the affected field; tables expose headers and selected-item context; dialogs return focus to their invoker.
- Related requirements: REQ-0019, REQ-0031, REQ-0018, REQ-0047, REQ-0059, NFR-0018. Exact SRS entries remain proposed; [coverage matrix](../test-matrix/P2-ux-coverage.md) provides links/status.
- Acceptance criteria: walk the stated entry -> inputs -> action -> visible outcome; verify required-field rejection, the stated empty/loading/failure/warning paths, accessible action order and recoverability without losing unrelated draft/history. No action may bypass the [review/approval guards](P2-workflows.md#review-and-approval-model).
- Defined review case: TEST-0195 in [UX review register](../test-matrix/P2-ux-coverage.md); no application verification claimed.

Text wireframe (logical regions, not pixel implementation):
```text
[Context: Client / Project / Job / Attempt] [Local/network status]
[Navigation] | Exception Review Center: Finding list
             | Selected item / fields / evidence / inline findings
             | [Safe secondary actions] [Guarded primary action]
[Actual state / affected items / next available action]
```

## UX-S14 — Findings and Bug Reports
- Purpose: Turn evidence into human-reviewed issue reports.
- User entry points: Website results; review finding; job Findings tab.
- Layout structure: shared header/navigation; main findings and bug reports work area; contextual detail panel; persistent primary/secondary action row with status.
- UI components: Observed vs expected, screenshot/step evidence, severity proposal, suspected/confirmed/disputed status, report preview.
- User actions: Filter/group findings; human confirm/dispute; edit report; local export.
- Required inputs: Finding ID, observed behavior, target/viewport/time/evidence; reviewer decision.
- Validation: Missing evidence prevents verified-defect label; severity is proposed until reviewed.
- Default state: read/view or editable draft only; no destructive action, job start, approval or request selected/triggered automatically. Existing project context is prefilled where applicable.
- Empty state: No findings: show tested/not-run coverage rather than claim defect-free site.
- Loading state: label “Loading findings and bug reports”; retain prior context but mark stale values; block actions requiring fresh data; allow safe navigation. Job monitoring uses actual progress, never a generic completed indicator.
- Success state: show confirmed result of the named action with record/attempt/artifact identity; saving/viewing success does not imply processing success, validation success or delivery approval.
- Failure state: Report/evidence generation failure retains finding and cause.
- Warning state: Automated assertion failure is an observation, not automatically a verified defect.
- Recovery actions: Restore evidence, rerun authorized scenario or export clearly labeled provisional report.
- Keyboard accessibility: K applies; name all findings and bug reports controls; error-summary links move to the affected field; tables expose headers and selected-item context; dialogs return focus to their invoker.
- Related requirements: REQ-0043, REQ-0044, REQ-0049, REQ-0050, REQ-0021, REQ-0019. Exact SRS entries remain proposed; [coverage matrix](../test-matrix/P2-ux-coverage.md) provides links/status.
- Acceptance criteria: walk the stated entry -> inputs -> action -> visible outcome; verify required-field rejection, the stated empty/loading/failure/warning paths, accessible action order and recoverability without losing unrelated draft/history. No action may bypass the [review/approval guards](P2-workflows.md#review-and-approval-model).
- Defined review case: TEST-0196 in [UX review register](../test-matrix/P2-ux-coverage.md); no application verification claimed.

Text wireframe (logical regions, not pixel implementation):
```text
[Context: Client / Project / Job / Attempt] [Local/network status]
[Navigation] | Findings and Bug Reports: Observed vs expected
             | Selected item / fields / evidence / inline findings
             | [Safe secondary actions] [Guarded primary action]
[Actual state / affected items / next available action]
```

## UX-S15 — Deliverable Preview
- Purpose: Inspect exactly the proposed client artifacts.
- User entry points: Job Preview; validation/review continuation.
- Layout structure: shared header/navigation; main deliverable preview work area; contextual detail panel; persistent primary/secondary action row with status.
- UI components: Output list with hashes, before/after comparison, page/data/diff preview, package inclusion controls.
- User actions: Inspect output; include/exclude eligible artifact; open local supported preview.
- Required inputs: Selected outputs and current validation/review evidence.
- Validation: Missing/changed/invalid artifacts ineligible; declared unsupported preview states visible.
- Default state: read/view or editable draft only; no destructive action, job start, approval or request selected/triggered automatically. Existing project context is prefilled where applicable.
- Empty state: No eligible outputs: return to results; no silent empty delivery package.
- Loading state: label “Loading deliverable preview”; retain prior context but mark stale values; block actions requiring fresh data; allow safe navigation. Job monitoring uses actual progress, never a generic completed indicator.
- Success state: show confirmed result of the named action with record/attempt/artifact identity; saving/viewing success does not imply processing success, validation success or delivery approval.
- Failure state: Preview failure affects preview, not hidden approval; output marked not fully reviewed.
- Warning state: Fidelity/formula/signature differences require explicit review.
- Recovery actions: Choose valid subset, repair/rerun or obtain supported review evidence.
- Keyboard accessibility: K applies; name all deliverable preview controls; error-summary links move to the affected field; tables expose headers and selected-item context; dialogs return focus to their invoker.
- Related requirements: REQ-0018, REQ-0022, REQ-0041, REQ-0059, REQ-0066. Exact SRS entries remain proposed; [coverage matrix](../test-matrix/P2-ux-coverage.md) provides links/status.
- Acceptance criteria: walk the stated entry -> inputs -> action -> visible outcome; verify required-field rejection, the stated empty/loading/failure/warning paths, accessible action order and recoverability without losing unrelated draft/history. No action may bypass the [review/approval guards](P2-workflows.md#review-and-approval-model).
- Defined review case: TEST-0197 in [UX review register](../test-matrix/P2-ux-coverage.md); no application verification claimed.

Text wireframe (logical regions, not pixel implementation):
```text
[Context: Client / Project / Job / Attempt] [Local/network status]
[Navigation] | Deliverable Preview: Output list with hashes
             | Selected item / fields / evidence / inline findings
             | [Safe secondary actions] [Guarded primary action]
[Actual state / affected items / next available action]
```

## UX-S16 — Final Approval
- Purpose: Record human approval of exact deliverables.
- User entry points: Preview Continue to approval; job Approval tab.
- Layout structure: shared header/navigation; main final approval work area; contextual detail panel; persistent primary/secondary action row with status.
- UI components: Selected manifest/hashes, job outcome, validation/review summary, reviewer label, Approve/Reject.
- User actions: Review exact artifacts; explicitly approve or reject for delivery.
- Required inputs: Reviewer label; current eligible manifest and completed required review.
- Validation: Any changed artifact/config evidence invalidates relevant approval; failed/unreviewed output blocks approval.
- Default state: read/view or editable draft only; no destructive action, job start, approval or request selected/triggered automatically. Existing project context is prefilled where applicable.
- Empty state: Nothing selected/eligible: approval unavailable with reason.
- Loading state: label “Loading final approval”; retain prior context but mark stale values; block actions requiring fresh data; allow safe navigation. Job monitoring uses actual progress, never a generic completed indicator.
- Success state: show confirmed result of the named action with record/attempt/artifact identity; saving/viewing success does not imply processing success, validation success or delivery approval.
- Failure state: Unable to record durable approval: remains unapproved.
- Warning state: Processing completion or validation PASS never means human-approved.
- Recovery actions: Repair evidence, review unresolved items or create a revised selection requiring fresh approval.
- Keyboard accessibility: K applies; name all final approval controls; error-summary links move to the affected field; tables expose headers and selected-item context; dialogs return focus to their invoker.
- Related requirements: REQ-0020, REQ-0031, REQ-0019, REQ-0022, NFR-0018. Exact SRS entries remain proposed; [coverage matrix](../test-matrix/P2-ux-coverage.md) provides links/status.
- Acceptance criteria: walk the stated entry -> inputs -> action -> visible outcome; verify required-field rejection, the stated empty/loading/failure/warning paths, accessible action order and recoverability without losing unrelated draft/history. No action may bypass the [review/approval guards](P2-workflows.md#review-and-approval-model).
- Defined review case: TEST-0198 in [UX review register](../test-matrix/P2-ux-coverage.md); no application verification claimed.

Text wireframe (logical regions, not pixel implementation):
```text
[Context: Client / Project / Job / Attempt] [Local/network status]
[Navigation] | Final Approval: Selected manifest/hashes
             | Selected item / fields / evidence / inline findings
             | [Safe secondary actions] [Guarded primary action]
[Actual state / affected items / next available action]
```

## UX-S17 — Export and Delivery Packaging
- Purpose: Create an approved local package without delivering it automatically.
- User entry points: Approved selection; job Export tab; report export action.
- Layout structure: shared header/navigation; main export and delivery packaging work area; contextual detail panel; persistent primary/secondary action row with status.
- UI components: Package manifest preview, local destination picker, collision check, progress and final hash summary.
- User actions: Build approved package; export local report; retry failed export.
- Required inputs: Explicit local destination and approved output selection for delivery package.
- Validation: Recheck approval/artifact hashes; unsafe/colliding/unwritable paths block or need fresh consent.
- Default state: read/view or editable draft only; no destructive action, job start, approval or request selected/triggered automatically. Existing project context is prefilled where applicable.
- Empty state: No approved package: go to final approval; diagnostic report export remains clearly non-delivery.
- Loading state: label “Loading export and delivery packaging”; retain prior context but mark stale values; block actions requiring fresh data; allow safe navigation. Job monitoring uses actual progress, never a generic completed indicator.
- Success state: show confirmed result of the named action with record/attempt/artifact identity; saving/viewing success does not imply processing success, validation success or delivery approval.
- Failure state: Export failure shows files written/unfinished and retains approved source artifacts.
- Warning state: Local export does not mean sent, published or deployed; provisional reports cannot carry ready-for-delivery badge.
- Recovery actions: Select another destination/name or retry; clean only explicitly consented partial export.
- Keyboard accessibility: K applies; name all export and delivery packaging controls; error-summary links move to the affected field; tables expose headers and selected-item context; dialogs return focus to their invoker.
- Related requirements: REQ-0022, REQ-0023, REQ-0021, REQ-0067, NFR-0012. Exact SRS entries remain proposed; [coverage matrix](../test-matrix/P2-ux-coverage.md) provides links/status.
- Acceptance criteria: walk the stated entry -> inputs -> action -> visible outcome; verify required-field rejection, the stated empty/loading/failure/warning paths, accessible action order and recoverability without losing unrelated draft/history. No action may bypass the [review/approval guards](P2-workflows.md#review-and-approval-model).
- Defined review case: TEST-0199 in [UX review register](../test-matrix/P2-ux-coverage.md); no application verification claimed.

Text wireframe (logical regions, not pixel implementation):
```text
[Context: Client / Project / Job / Attempt] [Local/network status]
[Navigation] | Export and Delivery Packaging: Package manifest preview
             | Selected item / fields / evidence / inline findings
             | [Safe secondary actions] [Guarded primary action]
[Actual state / affected items / next available action]
```

## UX-S18 — Local Storage Management
- Purpose: Manage local retained data without destroying originals.
- User entry points: Settings & storage Storage tab; low-storage prompt.
- Layout structure: shared header/navigation; main local storage management work area; contextual detail panel; persistent primary/secondary action row with status.
- UI components: Managed storage summary, selectable records/generated outputs, deletion preview, affected references.
- User actions: Inspect space; archive/delete selected managed records with consent; preserve inputs.
- Required inputs: Explicit selected managed items and consent.
- Validation: Never include originals/unrelated exports; locked files produce per-item outcomes.
- Default state: read/view or editable draft only; no destructive action, job start, approval or request selected/triggered automatically. Existing project context is prefilled where applicable.
- Empty state: No managed records: show storage locations and no destructive action.
- Loading state: label “Loading local storage management”; retain prior context but mark stale values; block actions requiring fresh data; allow safe navigation. Job monitoring uses actual progress, never a generic completed indicator.
- Success state: show confirmed result of the named action with record/attempt/artifact identity; saving/viewing success does not imply processing success, validation success or delivery approval.
- Failure state: Partial deletion/locked file identifies retained items; no false full cleanup.
- Warning state: Deleting evidence affects future verification/approval; warn before consent.
- Recovery actions: Retry selected locked items later; no automatic cleanup to gain space.
- Keyboard accessibility: K applies; name all local storage management controls; error-summary links move to the affected field; tables expose headers and selected-item context; dialogs return focus to their invoker.
- Related requirements: REQ-0026, REQ-0010, NFR-0024, NFR-0022. Exact SRS entries remain proposed; [coverage matrix](../test-matrix/P2-ux-coverage.md) provides links/status.
- Acceptance criteria: walk the stated entry -> inputs -> action -> visible outcome; verify required-field rejection, the stated empty/loading/failure/warning paths, accessible action order and recoverability without losing unrelated draft/history. No action may bypass the [review/approval guards](P2-workflows.md#review-and-approval-model).
- Defined review case: TEST-0200 in [UX review register](../test-matrix/P2-ux-coverage.md); no application verification claimed.

Text wireframe (logical regions, not pixel implementation):
```text
[Context: Client / Project / Job / Attempt] [Local/network status]
[Navigation] | Local Storage Management: Managed storage summary
             | Selected item / fields / evidence / inline findings
             | [Safe secondary actions] [Guarded primary action]
[Actual state / affected items / next available action]
```

## UX-S19 — Application Settings
- Purpose: Expose local defaults and accessibility preferences.
- User entry points: Settings & storage Settings tab.
- Layout structure: shared header/navigation; main application settings work area; contextual detail panel; persistent primary/secondary action row with status.
- UI components: Output defaults, effective module defaults, theme/text options, capability/status information.
- User actions: Edit/save/reset proposed defaults; inspect effective settings.
- Required inputs: Valid local paths and supported preferences.
- Validation: Invalid settings rejected; prior completed jobs and confirmed plans unchanged.
- Default state: read/view or editable draft only; no destructive action, job start, approval or request selected/triggered automatically. Existing project context is prefilled where applicable.
- Empty state: First launch: safe local defaults, no external sign-in.
- Loading state: label “Loading application settings”; retain prior context but mark stale values; block actions requiring fresh data; allow safe navigation. Job monitoring uses actual progress, never a generic completed indicator.
- Success state: show confirmed result of the named action with record/attempt/artifact identity; saving/viewing success does not imply processing success, validation success or delivery approval.
- Failure state: Settings save failure retains edits and effective prior values.
- Warning state: Preference is not a permission grant; target performance/theme choices proposed.
- Recovery actions: Correct/retry or cancel; restore previous valid defaults.
- Keyboard accessibility: K applies; name all application settings controls; error-summary links move to the affected field; tables expose headers and selected-item context; dialogs return focus to their invoker.
- Related requirements: REQ-0025, REQ-0009, NFR-0006, NFR-0008. Exact SRS entries remain proposed; [coverage matrix](../test-matrix/P2-ux-coverage.md) provides links/status.
- Acceptance criteria: walk the stated entry -> inputs -> action -> visible outcome; verify required-field rejection, the stated empty/loading/failure/warning paths, accessible action order and recoverability without losing unrelated draft/history. No action may bypass the [review/approval guards](P2-workflows.md#review-and-approval-model).
- Defined review case: TEST-0201 in [UX review register](../test-matrix/P2-ux-coverage.md); no application verification claimed.

Text wireframe (logical regions, not pixel implementation):
```text
[Context: Client / Project / Job / Attempt] [Local/network status]
[Navigation] | Application Settings: Output defaults
             | Selected item / fields / evidence / inline findings
             | [Safe secondary actions] [Guarded primary action]
[Actual state / affected items / next available action]
```

## UX-S20 — Help and Diagnostics
- Purpose: Explain usage and local failures safely.
- User entry points: Help navigation; contextual error Help.
- Layout structure: shared header/navigation; main help and diagnostics work area; contextual detail panel; persistent primary/secondary action row with status.
- UI components: Offline help/search, versions/capabilities, safe diagnostics preview, local save dialog.
- User actions: Read local help; inspect safe diagnostics; explicitly save local diagnostic report.
- Required inputs: Optional topic/job ID; chosen local diagnostic destination.
- Validation: No upload/telemetry; redact seeded secrets; missing evidence explained.
- Default state: read/view or editable draft only; no destructive action, job start, approval or request selected/triggered automatically. Existing project context is prefilled where applicable.
- Empty state: No diagnostic events: display versions/help, not invented healthy tests.
- Loading state: label “Loading help and diagnostics”; retain prior context but mark stale values; block actions requiring fresh data; allow safe navigation. Job monitoring uses actual progress, never a generic completed indicator.
- Success state: show confirmed result of the named action with record/attempt/artifact identity; saving/viewing success does not imply processing success, validation success or delivery approval.
- Failure state: Diagnostic write failure names destination and affected report.
- Warning state: Local logs may reference client paths; preview before exporting; no compatibility certification.
- Recovery actions: Choose another local destination or inspect available logs; no remote support submission.
- Keyboard accessibility: K applies; name all help and diagnostics controls; error-summary links move to the affected field; tables expose headers and selected-item context; dialogs return focus to their invoker.
- Related requirements: REQ-0014, REQ-0021, REQ-0032, NFR-0005, NFR-0022, NFR-0014. Exact SRS entries remain proposed; [coverage matrix](../test-matrix/P2-ux-coverage.md) provides links/status.
- Acceptance criteria: walk the stated entry -> inputs -> action -> visible outcome; verify required-field rejection, the stated empty/loading/failure/warning paths, accessible action order and recoverability without losing unrelated draft/history. No action may bypass the [review/approval guards](P2-workflows.md#review-and-approval-model).
- Defined review case: TEST-0202 in [UX review register](../test-matrix/P2-ux-coverage.md); no application verification claimed.

Text wireframe (logical regions, not pixel implementation):
```text
[Context: Client / Project / Job / Attempt] [Local/network status]
[Navigation] | Help and Diagnostics: Offline help/search
             | Selected item / fields / evidence / inline findings
             | [Safe secondary actions] [Guarded primary action]
[Actual state / affected items / next available action]
```
