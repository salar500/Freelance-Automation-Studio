# P2 module-specific UX

Status: PROPOSED interactions, conditional on unresolved P1 format/capability profiles. Shared plan/progress/approval/export screens are reused. No engine, browser, document library or frontend chosen. [Screens](P2-screens.md) own common states; [workflows](P2-workflows.md) own approval guards. Category TEST-0211 through TEST-0214 are defined in [coverage](../test-matrix/P2-ux-coverage.md).

## UX-M01 — Spreadsheet and CSV
REQ-0033 through REQ-0041; REQ-0005/0008/0018/0023; NFR-0012/0019. Input list previews sheets/ranges or CSV delimiter/encoding/header; ambiguous interpretation blocks Next and preserves original selection. Supported format badges are conditional on O-02, not promises.

Configuration tabs: Data preview, Columns, Cleaning, Transform, Validation, Output. Mapping table has source name/type, output name/order, include switch and validation rule. Cleaning rules are independently selected (trim, missing values, exact duplicate removal), with key columns and explicit keep policy. Typed filters/sort show locale/type conversions and stable ties. Combine/join preview reports unmatched/duplicate keys and potential expansion; never silently truncates. Proposed counts distinguish original, selected, rejected and changed rows; no configured validation means no rules evaluated.

Before/after comparison labels sample versus full results and row/column references; sample preview is not proof that all data validated. Sensitive cell details remain local and absent from general logs. Export config shows proposed CSV encoding/XLSX preservation profile, formulas/leading zeros/date implications, output destination and unsupported-feature warnings. User corrects ambiguity/rule conflict then regenerates plan; failed output checks block approval. Keyboard supports mapping-row navigation, labeled reorder actions as alternatives to drag/drop and expandable full cell text.

```text
[Input files / sheet / range / CSV interpretation]
[Data preview] [Columns] [Cleaning] [Transform] [Validation] [Output]
Source column | Output name | Order | Rules | Inline error
[Before sample] [After sample] [Estimated changes / warnings]
[Save draft] [Preview confirmed effects]
```

## UX-M02 — Website QA/regression
REQ-0042 through REQ-0050; REQ-0028/0030/0019/0021; NFR-0023. Target form records base URL, host/path/action allowlist, permission evidence, expiry and request budget. Entering a URL never starts browsing. Missing/expired permissions disable live Start with exact recovery instructions. Redirect/asset exclusions are shown as BLOCKED with reasons, not silently ignored or fetched.

Configuration tabs: Scope, Environment, Scenarios, Baseline, Evidence. Environment shows capability-driven browser choice as UX-O01 (supported engines/versions pending owner/P3/P5), viewport profiles and user-agent/emulation limitations. No implicit browser download/install. Unavailable engine is labeled unavailable; selecting a different engine does not claim cross-browser coverage. Viewport rows have width/height and a label; changing them invalidates associated comparison context. Test scenarios list exact assertions/steps, synthetic form data and whether state changes are permitted. Reviewed baseline version, tolerance and ignored regions explicit; replacing it needs human review.

Monitoring presents pages/steps tested/not run, status, safe timing and authorized scope. Screenshot comparison pairs baseline/current with textual finding summary; unstable regions are uncertain. Triage separates deterministic observed assertion failure from suspected defect and human-confirmed defect; network/TLS failures are environment findings. Bug-report preview has expected/observed, context, evidence and reviewer disposition. QA summary export includes executed/blocked/not-run coverage and limitations; unreviewed observations stay labeled provisional. Synthetic test data only; no local client-file upload or target-authorization bypass. Keyboard alternatives select viewports/scenarios and switch screenshots without relying on drag/hover.

```text
[Target declaration / authorization / permitted actions / expiry]
[Scope] [Environment: conditional browser + viewport] [Scenarios] [Baseline]
Page/step | Observed result | Evidence | Human disposition
[Inspect screenshot comparison] [Review findings] [Local QA report]
```

## UX-M03 — PDF/documents
REQ-0051 through REQ-0059; REQ-0005/0018/0019/0023; NFR-0012. Import list shows candidate format, page/section count and protected/corrupt/no-text-layer warnings. Operation selector displays only assessed supported capabilities: split, merge, reorder/rotate, extract text or declared template substitution; O-02 remains unresolved. No OCR assumed, and no unauthorized decryption.

Page/section picker supplies keyboard-accessible numbered range entry plus thumbnail/text listing; ordering has Move up/down controls. Output configuration previews source-to-output page/field mapping, filenames, count/order and required placeholder resolution. Overlaps/duplicates are explicitly shown; invalid ranges or missing required fields block planning. Processing preview explains fidelity limits, scanned pages, signature validity changes and unsupported embedded content. Output validation uses declared count/order/content properties; before/after mapping supports human fidelity review. Unsupported layout cannot be silently labeled preserved. Export uses common approval/hash gates. Preview loading/decoder errors do not erase the job or claim corruption without evidence.

```text
[Document list / supported operation / warnings]
[Pages or sections / explicit order / placeholder fields]
[Output names + page/field mapping] [Fidelity limitations]
[Validate selection] [Preview plan] -> [Results / Review / Export]
```

## UX-M04 — Maintenance/templates
REQ-0060 through REQ-0067; REQ-0010/0018/0020; NFR-0004/0012. Import a local source workspace and licensed local template; show excluded metadata/secrets and resolved scope before selection. File tree includes selected/unselected/blocked paths; labels identify traversal/link escape rejection. No implicit script execution, package fetch or deployment.

Operation config uses exact text/asset mappings and template placeholders. Change preview is a file-level manifest with original fingerprint, proposed operation and output-copy destination. Side-by-side/text diff marks added/removed/replaced content with labels as well as colors; binary assets show metadata/evidence rather than fictitious text differences. Ambiguous matches invalidate the affected edit. Local link checks distinguish checked local references from external references not checked; authorized live checks are a separate QA job.

Rollback is shown only for an explicitly offered/approved in-place operation after a verified backup; default is separate output copy. Backup unavailable disables in-place Start; rollback shows affected files/new changes and fresh consent, then per-file outcomes. Final review names changed files, validation findings, backup availability and whether anything remains uncertain. Approved local package says Not deployed. Keyboard scope selection and diff navigation work without pointer-only file-tree dragging. In-place capability remains conditional, not a P2 architectural choice.

```text
[Source workspace / allowed files / licensed template]
[Operations] [File change manifest] [Before/after diff]
[Local validation] [Backup status; guarded rollback if eligible]
[Preview approved file selection] [Export locally: Not deployed]
```

## Module acceptance
For each category, walk import/configure/plan/process/validate/review/export and its format/network/scope/fidelity failure. Verify shared workflow consistency and that unsupported choices remain disabled with explanations. No user, accessibility or application test has run.
