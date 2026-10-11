# UX design book

Status: P2 PROPOSED design baseline, 2026-10-11; no interface implemented, evaluated with users or accessibility-tested. P1 documentation approval is conditional; unresolved SRS entries, numeric targets and technical choices remain unapproved. The owner authorized conditional UX exploration of the four-module/core workflow scope only.

## Authority and specification map
This book owns UX principles, proposed design system and UX decision register. [Screens](../specifications/P2-screens.md) own the 20 screen specifications; [workflows](../specifications/P2-workflows.md) own guided jobs and approval guards; [module UX](../specifications/P2-module-ux.md) owns module-specific controls; [failure/recovery](../specifications/P2-failure-recovery.md) owns error presentations. [UX coverage](../test-matrix/P2-ux-coverage.md) owns conditional design coverage/new TEST definitions. Requirements and permanent policy remain in their authoritative books; these documents do not replace or expand the SRS without explicit approval.

## Principles
Keep context visible, reuse saved nonsecret configuration and preserve drafts. Prefer explicit labels and relevant actions over unexplained icons or dense dashboards. Make risky effects visible before action. Show measured progress and evidence availability separately from human approval. Local workflows remain usable offline; live website connectivity/authorization is a scoped requirement, not a global application sign-in. Use the same setup/plan/run/review/export pattern in all modules. Professional appearance is expressed through consistent alignment, spacing, typography and status language, not branding claims.

## Proposed design system
All numeric visual targets below are proposals for P2 review, not approved NFR amendments or measured compliance. No final UI framework selected.

| Element | Proposed standard / acceptance review |
| --- | --- |
| Layout grid | 8 logical-unit base grid; 12-column main region with readable max text width; resizable navigation/details; collapse secondary panes before clipping essential controls. Candidate 1024x768 usable workspace is UX-O02, not an approved OS/display minimum. |
| Navigation | Six areas in the screen spec; contextual job tabs and breadcrumbs retain client/project/attempt; current location exposed visually and to assistive tools. |
| Typography | Candidate Windows system UI font (Segoe UI if available; system fallback), no redistributed font assumed; body 14 logical units, secondary 12, headings 18/24, line spacing >=1.4; no essential message only in tiny secondary text. |
| Light palette | Candidate background #F8FAFC, surface #FFFFFF, text #0F172A, secondary text #475569, accent #1D4ED8, danger #B91C1C, warning #92400E, success #166534. Tokens represent semantics, not module-specific colors. Contrast not verified yet. |
| Dark palette | Candidate background #0F172A, surface #1E293B, text #F8FAFC, secondary #CBD5E1, accent #93C5FD, danger #FCA5A5, warning #FCD34D, success #86EFAC. Theme preference local; proposed follow-system option. Contrast not verified yet. |
| Spacing | Scale 4/8/12/16/24/32 logical units; consistent field grouping, label-to-control and section gaps; dense tables do not shrink essential action targets. |
| Form fields | Persistent labels, required indicator in text, helper text and linked inline errors; units/ranges explicit; never use placeholder as sole label; validation retains entered values. |
| Buttons | One clear primary action per region, explicit verbs (Save draft, Confirm plan, Approve selected outputs, Export locally); secondary Cancel/Back; destructive action visually/textually distinct and never auto-selected. Candidate essential hit area >=40x40 logical units; keyboard equivalent for all. |
| Tables | Named headers, sortable indicator/direction, explicit selection count; filters show scope; accessible row/detail navigation; truncated paths have full-text expansion without hover-only dependence. |
| Cards | Summaries link to evidence/detail; no card color alone encodes status; counts specify denominator and freshness. |
| Dialogs | Modal only for risky consent or focused decisions; named title/context, safe initial focus, trap focus within modal while open and restore invoker on close. Esc cancels only when safe; Enter must not silently authorize destructive action. |
| Notifications | Inline durable errors for blockers, local job banners for persistent outcomes, transient noncritical confirmations only when redundant with retained state; no essential information solely in a disappearing toast. |
| Progress | Known total: determinate with completed/total and operation; unknown: labeled indeterminate. Cancellation requested/partial/interrupted shown explicitly. Avoid invented percentage or ETA. |
| Status indicators | Text plus icon; distinguish processing, validation, review and delivery eligibility. PASS is check result, not defect confirmation or delivery approval. |
| Empty states | Explain why empty, what input/filter is needed and one relevant next action; no sample client data that appears real. |
| Error messages | Three-part What happened / What was affected / What next; safe details and stable job/finding reference; avoid secrets/client cell content in general notifications. |
| Confirmation dialogs | Name exact targets, effect and recovery availability; show plan/artifact fingerprints by reference; require fresh affirmative choice; keep safe Cancel prominent. Never infer consent from template/default. |

## Accessibility contract (proposed, untested)
- Keyboard: every essential workflow has non-pointer access, logical tab order matching reading order, visible focus and no keyboard trap. Composite controls use documented arrow keys; nonmodal navigation does not trap focus.
- Focus: candidate outline >=2 logical units and >=3:1 adjacent contrast; never obscured by a sticky panel. Validation moves focus to an error summary on explicit submit, with links to fields; asynchronous updates do not steal focus.
- Names/roles/state: meaningful accessible names for icons, tables, tabs, fields and dialogs; required/invalid/selected/expanded states exposed; job state includes attempt context.
- Announcements: politely announce phase changes and summaries, not every progress tick; announce blocking error and linkable next action. Cancellation feedback remains available in the view.
- Contrast targets: normal text >=4.5:1, large text >=3:1, essential controls/focus >=3:1; no color-only status. Proposed design benchmarks, not a desktop accessibility certification.
- Scaling: essential text/content usable at proposed 200% text scaling and common 100/150/200% Windows display scaling; allow reflow/scroll without clipped approval/cancel actions. Exact minimum window size awaits UX-O02.
- Screen-reader expectations: title/context read on entry, headers associated with table cells, modal title/description announced, action outcomes available in text, full path/evidence summaries without image-only information. Screenshots/diffs need textual summary.
- Accessibility validation: future keyboard/screen-reader/high-contrast/scaling tests on approved Windows target, plus representative usability review. None has occurred in P2 documentation work.

## UX open decisions and conflicts
| Key | Unresolved / proposed item | Owner / gate | Handling now |
| --- | --- | --- | --- |
| UX-O01 | Browser choice requested in P2 but supported engines/versions are not in approved P1 capability detail | Owner requirements disposition and P3/P5 feasibility | Conditional capability selector only; no bundled browser or download decision |
| UX-O02 | Minimum window/display size, typography and scaling profile | Owner P2 review, UX/QA actual Windows evaluation later | Proposed targets; essential actions remain conceptually reachable |
| UX-O03 | Local reviewer identity and any separation-of-duties controls (SRS O-05) | Owner/security P3 | Asserted local label, not verified account or automatic authorization |
| UX-O04 | Diagnostic report/help and bug-report editorial affordances extend existing reporting/navigation purposes | Owner P2 scope review | Proposed local-only affordances; no support upload or new external issue tracker |
| UX-O05 | Template step follows configuration in requested 12-step sequence | Owner P2 review | Show apply-diff, retain current options unless accepted, revalidate and invalidate stale consent |

O-01 through O-09 remain in the requirements book. This UX does not settle formats, release priorities, budgets, storage/security mechanisms, license feasibility, packaging or resumability. Each related design remains conditional. Non-UX quality properties retain explicit downstream ownership in coverage; screenshots/wireframes cannot demonstrate runtime performance, security or Windows compatibility.

## P2 acceptance
All requested logical screens have defined fields/states, wireframes, keyboard behavior and conditional requirement references; guided/module and failure flows include safe guards; review distinguishes evidence uncertainty from confirmed defects; local/offline operation and accessible feedback are modeled; links/trace references and scope are checked. P2 can be READY_FOR_REVIEW after documentary checks only, not implemented, user-validated or accessibility-certified. [P2 report](../milestone-reports/MS-0003-P2.md) owns actual evidence; [execution state](09-execution-book.md) owns approval/status.
