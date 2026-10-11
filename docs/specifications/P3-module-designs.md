# P3 detailed four-module architecture

Status: PROPOSED profiles, not implemented/supported product promises. All modules use the [common contract](P3-module-contracts.md) and [platform components](P3-system-components.md). Each capability below maps to an existing requirement as support or a related requirement only where marked EXTENSION. Block 4 explicitly requests design exploration for new fuzzy duplicates/splitting/discovery/trace/conversion/impact/preview details; these are not silently promoted into approved functional requirements. SRS unchanged; [architecture decision register](../governance/03-architecture-book.md#open-architecture-decisions) records scope/feasibility gates.

Common platform owns snapshots/config/queue/progress/cancel/errors/artifacts/evidence/validation-result semantics/review/reports/packaging/history/backups. A module owns only its parser/transform/test predicates and declares stage/capability profile. Worker publishes prepared result; platform verifies and grants human decisions. No module reaches another module's private data or client DB.

## MOD-A — Spreadsheet and CSV
- Responsibilities: category-specific inspect/plan/transform/assert/verify adapters, with common lifecycle supplied by platform.
- Inputs: Readonly CSV/XLSX snapshot set, explicit header/sheet/range/locale/encoding, column mappings/rules and operation profile.
- Outputs: Prepared CSV/XLSX data plus change/invalid/duplicate/reconciliation evidence; supported feature profile only.
- Configuration schema: versioned structured encoding, delimiter, header mode, sheets/ranges, columns/types, cleaning rules/key policy, filters/sort/join/split predicates, allowed formula profile, output schema and limits; no embedded code/secrets/permissions.
- Validation: H input/profile validation and I operation-specific verification; declared unsupported/uncertain profiles block automatic acceptance.
- Execution stages: IMPORT -> INSPECT -> VALIDATE -> PLAN -> TRANSFORM -> VERIFY -> REVIEW -> EXPORT. These are module progress phases, not replacement durable attempt states.
- Resource limits: max input/expanded bytes/rows/columns/cells, memory/chunk bytes, join-expansion factor, deadline and output reserve; values pending O-03/P5.
- Security boundaries: No macros/external formula links/external workbook resources evaluated. Candidate parsers may not stream all XLSX features; whole-workbook memory requires reject/bounded fallback, not silent truncation. Formula-safe handling separates literal text from explicitly preserved formula and human review; no formula evaluator adopted.
- Failure handling: Empty input yields truthful zero records/declared header policy; missing/duplicate headers, mixed types, invalid dates and encoding ambiguity reject or yield named row-level findings under explicit profile. Corrupt/unsupported workbook features block the affected operation; no lossless-all-Excel promise. Unexpected row count or ambiguous fuzzy candidate never auto-deletes rows.
- Recovery: Immutable snapshot/plan enables deterministic new attempt; verified chunk checkpoints only if record boundary/ordering/profile state is proven, otherwise safe retry. Partial rows remain non-deliverable until reconciliation.
- Evidence: Input/output/selected/rejected/changed counts, schema mapping, invalid rows, duplicate candidates, rule IDs, before/after content comparison, module/config/duration/hash refs; detailed cells local-only.
- Human review / acceptance: Output counts/types/order/key/cardinality match declared operation; hashes and original preservation verified. Judgment-dependent/fuzzy candidates need human review; deterministic exact matches have explicit key/keep policy.
- Requirement / UX traceability: REQ-0033 through REQ-0041; UX-M01 / UX-S05/07/12/15/17; risks RISK-0002 RISK-0005 RISK-0006; all applicable details conditional. Existing TEST references derived per requirement and category cases TEST-0211 through TEST-0214; [P3 trace/test register](../test-matrix/P3-architecture-coverage.md).

### Capability/profile matrix
| Capability | Candidate behavior / limit | Supporting or related REQ | Scope status / future verification |
| --- | --- | --- | --- |
| File import | Shared K snapshots; inspect CSV/workbook metadata | REQ-0033 | Conditional existing capability detail; TEST-0065/TEST-0066 |
| Format detection | Declared/profile detection, ambiguity not guess | REQ-0033 | Conditional existing capability detail; TEST-0065/TEST-0066 |
| CSV encoding handling | Explicit encoding and delimiter, invalid bytes fail | REQ-0033 | Conditional existing capability detail; TEST-0065/TEST-0066 |
| Excel workbook inspection | Supported sheet/features inspection | REQ-0034 | Conditional existing capability detail; TEST-0067/TEST-0068 |
| Worksheet selection | Explicit sheet/range/header selection | REQ-0034 | Conditional existing capability detail; TEST-0067/TEST-0068 |
| Column identification | Stable header/column references, duplicate names surfaced | REQ-0037 | Conditional existing capability detail; TEST-0073/TEST-0074 |
| Schema validation | Types/required/header rules and per-field findings | REQ-0039 | Conditional existing capability detail; TEST-0077/TEST-0078 |
| Column mapping | Select/rename/order with duplicate-name rejection | REQ-0037 | Conditional existing capability detail; TEST-0073/TEST-0074 |
| Data normalization | Configured trim/empty-value rules only | REQ-0035 | Conditional existing capability detail; TEST-0069/TEST-0070 |
| Exact duplicate detection | Configured exact key policy; report preserved/removed counts | REQ-0035 | Conditional existing capability detail; TEST-0069/TEST-0070 |
| Configurable fuzzy duplicate review | Candidate similarity/threshold/evidence only; no uncertain auto-delete | REQ-0019 | EXTENSION: related requirement only, owner requirement/profile disposition + new scoped tests pending; not enabled by P3 |
| Missing-value detection | Named missing-value rules and row references | REQ-0039 | Conditional existing capability detail; TEST-0077/TEST-0078 |
| Data filtering | Typed configured conditions, conversion ambiguity surfaced | REQ-0036 | Conditional existing capability detail; TEST-0071/TEST-0072 |
| Sorting | Explicit keys/directions/stable ties | REQ-0036 | Conditional existing capability detail; TEST-0071/TEST-0072 |
| Dataset merging | Append/join cardinality and unmatched-key reconciliation | REQ-0038 | Conditional existing capability detail; TEST-0075/TEST-0076 |
| Dataset splitting | Candidate configured partitions with total-row conservation | REQ-0037 | EXTENSION: related requirement only, owner requirement/profile disposition + new scoped tests pending; not enabled by P3 |
| Formula-safe handling | Typed literal vs explicit formula, external links blocked/flagged | REQ-0040 | Conditional existing capability detail; TEST-0079/TEST-0080 |
| Data type conversion | Declared locale/types with invalid-value findings | REQ-0036 | Conditional existing capability detail; TEST-0071/TEST-0072 |
| Date and number normalization | Explicit locale/time/type rules, no hidden business inference | REQ-0036 | Conditional existing capability detail; TEST-0071/TEST-0072 |
| Data validation | Per-rule results, no zero-rule PASS | REQ-0039 | Conditional existing capability detail; TEST-0077/TEST-0078 |
| Before/after comparison | Counts/content evidence with sample/full distinction | REQ-0041 | Conditional existing capability detail; TEST-0081/TEST-0082 |
| Export/report generation | K stages data; M renders evidence, N gates final package | REQ-0040 | Conditional existing capability detail; TEST-0079/TEST-0080 |

Unsupported: any undeclared operation/format/fidelity, hard-limit overflow, unauthorized effects or unverified runtime dependency. Registry advertises only adopted/verified profiles later, never every research capability in this table.

## MOD-B — Website QA and regression
- Responsibilities: category-specific inspect/plan/transform/assert/verify adapters, with common lifecycle supplied by platform.
- Inputs: Approved target/action/expiry and synthetic scenarios, browser/viewport/version profile, reviewed baseline, evidence/retention preferences.
- Outputs: Prepared screenshots/traces/findings/QA summary; observed result and human classification separate.
- Configuration schema: versioned structured allowed origins/paths/methods/actions, request/page/depth/byte limits, explicit discovery strategy, stable locators/waits, scenario/version, engine/viewport/baseline, retry/deadlines; no embedded code/secrets/permissions.
- Validation: H input/profile validation and I operation-specific verification; declared unsupported/uncertain profiles block automatic acceptance.
- Execution stages: AUTHORIZE -> CONFIGURE -> PREFLIGHT -> DISCOVER -> EXECUTE -> COLLECT EVIDENCE -> CLASSIFY -> REVIEW -> REPORT. These are module progress phases, not replacement durable attempt states.
- Resource limits: bounded requests/pages/navigation time/concurrency/browser memory/evidence bytes; operation and heartbeat deadlines; concrete targets pending O-03/O-06/UX-O01.
- Security boundaries: Fresh owned browser profile per attempt; least-privilege optional authorized test-account session; no local client files, inherited normal browsing cookies, downloads/scripts outside approved scenario or insecure TLS. Service workers/WebRTC/background requests and redirects require proven enforcement. Browser support on Windows10 remains adoption blocker for current Playwright candidate.
- Failure handling: Classify AUTOMATED_ASSERTION_FAILURE, CONFIRMED_SOFTWARE_DEFECT (human only), ENVIRONMENT_FAILURE, AUTOMATION_DEFECT and INCONCLUSIVE distinctly. Network loss/TLS/locator ambiguity not automatically website bug; missing baseline gives no regression verdict. Lost nonidempotent response is inconclusive, never auto-post retry.
- Recovery: Close only owned browser tree/profiles; retain safe captured evidence. New retry rechecks target permission and version/baseline; transient idempotent observations can retry under bounded approved policy, final result shows all attempts rather than hiding flakiness.
- Evidence: Scope/permission snapshot, scenario/locator/browser/viewport/time, checked/blocked/not-run pages, assertion expected/observed, screenshots/network/console/trace safe refs, classification and human disposition.
- Human review / acceptance: Every request stays within proven grant; screenshots/trace refs present or NOT_RUN; no verified defect without human confirmation. Real-device support not inferred from viewport emulation.
- Requirement / UX traceability: REQ-0042 through REQ-0050; UX-M02 / UX-S09/10/13/14/17; risks RISK-0001 RISK-0003 RISK-0008; all applicable details conditional. Existing TEST references derived per requirement and category cases TEST-0211 through TEST-0214; [P3 trace/test register](../test-matrix/P3-architecture-coverage.md).

### Capability/profile matrix
| Capability | Candidate behavior / limit | Supporting or related REQ | Scope status / future verification |
| --- | --- | --- | --- |
| Authorized target configuration | Explicit origin/path/action permission before request | REQ-0042 | Conditional existing capability detail; TEST-0083/TEST-0084 |
| Testing scope management | Limits/expiry/assets/redirect grant, fail closed | REQ-0042 | Conditional existing capability detail; TEST-0083/TEST-0084 |
| Page discovery | Bounded configured discovery, no unrestricted crawl | REQ-0042 | EXTENSION: related requirement only, owner requirement/profile disposition + new scoped tests pending; not enabled by P3 |
| Internal link validation | Authorized link status and scope findings | REQ-0043 | Conditional existing capability detail; TEST-0085/TEST-0086 |
| Asset loading checks | Allowed assets only; untested/blocked explicitly | REQ-0043 | EXTENSION: related requirement only, owner requirement/profile disposition + new scoped tests pending; not enabled by P3 |
| Browser console monitoring | Safe log observations, not automatic defects | REQ-0050 | EXTENSION: related requirement only, owner requirement/profile disposition + new scoped tests pending; not enabled by P3 |
| Network failure recording | Request disposition and safe error context | REQ-0050 | Conditional existing capability detail; TEST-0099/TEST-0100 |
| Smoke-test execution | Declared assertions not assumed business rules | REQ-0044 | Conditional existing capability detail; TEST-0087/TEST-0088 |
| Regression scenarios | Versioned scenarios and reviewed baseline | REQ-0046 | Conditional existing capability detail; TEST-0091/TEST-0092 |
| Navigation testing | Authorized configured steps/assertions | REQ-0045 | Conditional existing capability detail; TEST-0089/TEST-0090 |
| Form validation testing | Synthetic values; sensitive/state change separately authorized | REQ-0045 | Conditional existing capability detail; TEST-0089/TEST-0090 |
| Responsive viewport checks | Declared viewport geometry and emulation limits | REQ-0048 | Conditional existing capability detail; TEST-0095/TEST-0096 |
| Screenshot capture | Captured context and local evidence digest | REQ-0047 | Conditional existing capability detail; TEST-0093/TEST-0094 |
| Trace collection | Candidate redacted local trace, secret-aware retention | REQ-0050 | EXTENSION: related requirement only, owner requirement/profile disposition + new scoped tests pending; not enabled by P3 |
| Evidence association | Stable attempt/step/artifact references | REQ-0050 | Conditional existing capability detail; TEST-0099/TEST-0100 |
| Failure classification | Environment/automation/inconclusive separate from defect | REQ-0050 | Conditional existing capability detail; TEST-0099/TEST-0100 |
| Finding review | J records human confirm/dismiss/defer | REQ-0019 | Conditional existing capability detail; TEST-0037/TEST-0038 |
| Regression comparison | New/unchanged/resolved plus reviewed baseline version | REQ-0046 | Conditional existing capability detail; TEST-0091/TEST-0092 |
| Bug report preparation | M report observation/evidence/review status | REQ-0050 | Conditional existing capability detail; TEST-0099/TEST-0100 |
| QA execution summary | Coverage/timing/limits/NOT_RUN visible | REQ-0050 | Conditional existing capability detail; TEST-0099/TEST-0100 |

Unsupported: any undeclared operation/format/fidelity, hard-limit overflow, unauthorized effects or unverified runtime dependency. Registry advertises only adopted/verified profiles later, never every research capability in this table.

## MOD-C — PDF and document automation
- Responsibilities: category-specific inspect/plan/transform/assert/verify adapters, with common lifecycle supplied by platform.
- Inputs: Readonly supported PDF/TXT/DOCX snapshots, explicit pages/sections/order, template field map and fidelity profile.
- Outputs: Prepared document/text outputs plus source-output page/field mapping and validation/fidelity evidence.
- Configuration schema: versioned structured operation, page ranges/order/rotation, placeholders, required field values, output names, candidate fidelity EXACT_REQUIRED/BEST_EFFORT/CONTENT_ONLY, batch continue policy and limits; no embedded code/secrets/permissions.
- Validation: H input/profile validation and I operation-specific verification; declared unsupported/uncertain profiles block automatic acceptance.
- Execution stages: IMPORT -> INSPECT -> VALIDATE -> CONFIGURE -> PROCESS -> VERIFY -> PREVIEW -> EXPORT. These are module progress phases, not replacement durable attempt states.
- Resource limits: input/expanded bytes/pages/images/fonts/template fields, memory/time, staging/output reserve; bounds pending format/workload evidence.
- Security boundaries: No macro/script execution, unauthorized decryption or external conversion/OCR API. Protected input legitimate access must be explicitly supported; credentials not logged. Font licensing/resources and native parsers assessed before use.
- Failure handling: Scanned/no-text-layer pages are not transcribed success; encrypted/protected/corrupt/unsupported input yields typed limitation. Missing fonts/images/complex layout require fidelity findings. Conversion or signature validity never promised perfect. Partial batch keeps per-item status under configured continue policy.
- Recovery: Preserve originals, outputs staged separately; retry from snapshots, resume only independently verified document boundary/checkpoint; invalid output stays ineligible.
- Evidence: Input/output page/section counts/order, extracted text coverage, placeholder resolution, metadata/signature/fidelity warnings, output readability/hash/operation duration; preview evidence tied to current bytes.
- Human review / acceptance: EXACT_REQUIRED rejects unsupported exact-fidelity properties; BEST_EFFORT exposes limitations and requires review; CONTENT_ONLY checks declared content not visual layout. Profiles are proposed concepts awaiting requirements/feasibility approval. Local OCR is research-only extension, not assumed available or reliable.
- Requirement / UX traceability: REQ-0051 through REQ-0059; UX-M03 / UX-S05/07/12/13/15/17; risks RISK-0002 RISK-0006; all applicable details conditional. Existing TEST references derived per requirement and category cases TEST-0211 through TEST-0214; [P3 trace/test register](../test-matrix/P3-architecture-coverage.md).

### Capability/profile matrix
| Capability | Candidate behavior / limit | Supporting or related REQ | Scope status / future verification |
| --- | --- | --- | --- |
| PDF inspection | Format/page/protection/unsupported-feature metadata | REQ-0051 | Conditional existing capability detail; TEST-0101/TEST-0102 |
| PDF merging | Confirmed order and total page count | REQ-0053 | Conditional existing capability detail; TEST-0105/TEST-0106 |
| PDF splitting | Explicit ranges and distinct outputs | REQ-0052 | Conditional existing capability detail; TEST-0103/TEST-0104 |
| Page extraction | Selected page conservation/order | REQ-0052 | Conditional existing capability detail; TEST-0103/TEST-0104 |
| Page reordering | Explicit permutation/duplication policy | REQ-0054 | Conditional existing capability detail; TEST-0107/TEST-0108 |
| Page rotation | Declared page rotations, inspect output | REQ-0054 | Conditional existing capability detail; TEST-0107/TEST-0108 |
| Metadata inspection | Candidate safe metadata/signature context | REQ-0051 | EXTENSION: related requirement only, owner requirement/profile disposition + new scoped tests pending; not enabled by P3 |
| Text extraction | Digital text only with coverage findings | REQ-0055 | Conditional existing capability detail; TEST-0109/TEST-0110 |
| Supported document conversion | Conditional exact/best-effort/content profile; no universal conversion | REQ-0058 | EXTENSION: related requirement only, owner requirement/profile disposition + new scoped tests pending; not enabled by P3 |
| DOCX template population | Declared placeholders, no macro execution | REQ-0056 | Conditional existing capability detail; TEST-0111/TEST-0112 |
| Batch document generation | Independent per-item outputs/status | REQ-0057 | Conditional existing capability detail; TEST-0113/TEST-0114 |
| Report formatting | M common report renderer, not duplicate engine | REQ-0059 | Conditional existing capability detail; TEST-0117/TEST-0118 |
| Document validation | Reopen/count/order/content profile checks | REQ-0058 | Conditional existing capability detail; TEST-0115/TEST-0116 |
| Output packaging | N/J common approved manifest only | REQ-0022 | Conditional existing capability detail; TEST-0043/TEST-0044 |

Unsupported: any undeclared operation/format/fidelity, hard-limit overflow, unauthorized effects or unverified runtime dependency. Registry advertises only adopted/verified profiles later, never every research capability in this table.

## MOD-D — Website maintenance/template development
- Responsibilities: category-specific inspect/plan/transform/assert/verify adapters, with common lifecycle supplied by platform.
- Inputs: Readonly source workspace snapshot, licensed local template, explicit allowed file manifest and structured update mapping.
- Outputs: Isolated changed working copy, diff/change impact/validation evidence and eligible local project package.
- Configuration schema: versioned structured scope/file patterns and exclusions, exact mappings/placeholders, output copy root, supported project profile, validation/report choices, candidate backup/rollback mode; no embedded code/secrets/permissions.
- Validation: H input/profile validation and I operation-specific verification; declared unsupported/uncertain profiles block automatic acceptance.
- Execution stages: IMPORT -> INSPECT -> DEFINE SCOPE -> PLAN -> PREVIEW -> APPLY TO WORKING COPY -> VALIDATE -> REVIEW -> PACKAGE. These are module progress phases, not replacement durable attempt states.
- Resource limits: file/count/expanded byte/depth/text size, operation deadline/disk reserve; bounds pending O-03 and framework profile.
- Security boundaries: Reject traversal/junction escape, source .git/secrets/unknown executables; no arbitrary scripts/dependency installation/build commands/imported code or deployment. Preview must be passive/network-inert, not execute client JavaScript/server runtime.
- Failure handling: Unsupported framework/server-side structures yield no unsafe modification. Missing/ambiguous replacement stops affected edit; unknown source fingerprint invalidates plan; binary assets have metadata/diff limits rather than fictitious text diff.
- Recovery: Default working copy discarded/retained under registered policy; original unchanged. Conditional explicitly approved in-place mode needs verified backup first; rollback rechecks changed target and fresh destructive consent, then per-file outcome.
- Evidence: Input inventory/fingerprints, selected/excluded paths, exact edit manifest, before/after source diff, local link/asset/static findings, backup/rollback refs, current hashes and Not deployed label.
- Human review / acceptance: Static HTML/CSS/JS text/template files are candidate supported profiles for deterministic edits only; framework-generated/server-side execution/conversion unsupported unless separately approved. External references not live-tested unless separately authorized QA job.
- Requirement / UX traceability: REQ-0060 through REQ-0067; UX-M04 / UX-S05/07/09/12/15/17; risks RISK-0002 RISK-0003 RISK-0006; all applicable details conditional. Existing TEST references derived per requirement and category cases TEST-0211 through TEST-0214; [P3 trace/test register](../test-matrix/P3-architecture-coverage.md).

### Capability/profile matrix
| Capability | Candidate behavior / limit | Supporting or related REQ | Scope status / future verification |
| --- | --- | --- | --- |
| Source project import | K readonly snapshot and safe scoped paths | REQ-0060 | Conditional existing capability detail; TEST-0119/TEST-0120 |
| Project structure inspection | Candidate profile detection without running project code | REQ-0060 | Conditional existing capability detail; TEST-0119/TEST-0120 |
| File inventory | Selected/excluded/blocked manifest with hashes | REQ-0060 | Conditional existing capability detail; TEST-0119/TEST-0120 |
| Broken reference detection | Declared local reference graph | REQ-0064 | Conditional existing capability detail; TEST-0127/TEST-0128 |
| Local link validation | Resolve permitted local links only | REQ-0064 | Conditional existing capability detail; TEST-0127/TEST-0128 |
| Asset validation | Candidate existence/profile validation | REQ-0064 | Conditional existing capability detail; TEST-0127/TEST-0128 |
| Metadata inspection | Candidate declared metadata fields, no inferred SEO promise | REQ-0063 | EXTENSION: related requirement only, owner requirement/profile disposition + new scoped tests pending; not enabled by P3 |
| Structured content replacement | Exact typed mapping, ambiguous match blocked | REQ-0063 | Conditional existing capability detail; TEST-0125/TEST-0126 |
| Template-based page generation | Licensed local template/placeholders | REQ-0061 | Conditional existing capability detail; TEST-0121/TEST-0122 |
| Configuration-driven updates | Schema-bounded deterministic changes | REQ-0063 | Conditional existing capability detail; TEST-0125/TEST-0126 |
| Before/after comparison | Current source/working-copy diff | REQ-0062 | Conditional existing capability detail; TEST-0123/TEST-0124 |
| Source diff generation | Text delta and binary metadata limitations | REQ-0062 | Conditional existing capability detail; TEST-0123/TEST-0124 |
| Change impact analysis | Candidate bounded reference impact, not universal correctness proof | REQ-0062 | EXTENSION: related requirement only, owner requirement/profile disposition + new scoped tests pending; not enabled by P3 |
| Static validation | Declared syntax/reference predicates only | REQ-0064 | Conditional existing capability detail; TEST-0127/TEST-0128 |
| Local preview | Passive text/image preview; untrusted code/network disabled | REQ-0066 | EXTENSION: related requirement only, owner requirement/profile disposition + new scoped tests pending; not enabled by P3 |
| Exportable project package | N common approval-bound local package | REQ-0066 | Conditional existing capability detail; TEST-0131/TEST-0132 |
| Rollback preparation | Conditional verified backups and exact fresh consent | REQ-0065 | Conditional existing capability detail; TEST-0129/TEST-0130 |

Unsupported: any undeclared operation/format/fidelity, hard-limit overflow, unauthorized effects or unverified runtime dependency. Registry advertises only adopted/verified profiles later, never every research capability in this table.

## Future acceptance scenarios (all NOT_RUN)
| Module | Positive | Negative / boundary | Integrity / recovery |
| --- | --- | --- | --- |
| A | Valid configured merge/clean/export | Invalid schema, exact duplicates, corrupt files, encoding/type/date ambiguity; unapproved fuzzy candidates only flagged | Row reconciliation, original hashes, large workload, chunk boundary/cancel/retry; TEST-0065 through TEST-0082 and TEST-0211 |
| B | Authorized URL/assertions/screenshots | Unauthorized URL/redirect, broken link/assertion, ambiguous locator, network/TLS loss | Browser crash/cleanup, local evidence integrity, human defect confirmation; TEST-0083 through TEST-0100 and TEST-0212 |
| C | Valid PDF merge/split/template | Corrupt/encrypted/unsupported/scanned input, missing fonts/layout warning | Partial batch/count/order/content verification and preservation; TEST-0101 through TEST-0118 and TEST-0213 |
| D | Valid source import and controlled change | Unsupported framework, unsafe project scripts/traversal, ambiguous update/validation failure | Diff review, original preservation, verified backup/rollback; TEST-0119 through TEST-0134 and TEST-0214 |
| Shared | Approved offline plan/run/review/export | Unauthorized operation, protocol/DB/storage/evidence failure | Restart/interrupted write, changed artifact/stale approval and export verification; original core/NFR cases plus new P3 cases |

## Large structured-data strategy and fidelity limits
A proposes streaming/chunk processing for CSV transformations with bounded memory. Joins/sorts need bounded spill-to-disk or explicit workload rejection; spill files registered/isolated/space checked and output order/reconciliation defined. XLSX cell/object models may require materialization; do not claim streaming support from CSV results. Exact duplicate detection is deterministic under declared keys; fuzzy similarity is judgment-dependent and creates candidates only. Numeric/date normalization may be deterministic after explicit interpretation but never invents business corrections. Formula-safe output must retain semantic distinction and warn if sanitization changes intended formulas; EXCEL evaluation/fidelity stays O-02/P5, not a lossless promise.

B locators prefer explicit stable identifiers/roles where supported, with versioned fallback and cardinality checks; no arbitrary time sleeps as correctness evidence. Stable waits are declared load/element/state/assertion conditions with deadlines; unavailable elements fail or become inconclusive according to scenario, not guessed pass. Scenario versions, browser/viewport/baseline version and retry history in every run prevent incompatible regression comparisons. Authentication is optional target-specific test-session handling under S; synthetic values only.

C distinguishes digital text extraction, image content inspection and local OCR-dependent extraction; only explicitly assessed local OCR could be a future extension. EXACT_REQUIRED must list exact properties proved; BEST_EFFORT reports deviations for human review; CONTENT_ONLY makes no layout claim. M handles common reports; document processing does not duplicate rendering/report policy.

D compatibility profile: static HTML/CSS/JS source files as deterministic content, local templates as data; framework-generated outputs may be inspected but not rebuilt or universally refactored; server-side applications are not executed. Passive preview avoids importing an app runtime. No auto installs/build scripts/deployment. External tests are separate authorized B jobs.
