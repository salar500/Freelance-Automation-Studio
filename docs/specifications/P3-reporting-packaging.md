# P3 reporting and controlled delivery packaging

Status: PROPOSED formats/contracts, no renderer/installer adopted. COM-M owns common report schemas/rendering; COM-N owns local package/export; COM-J controls approval. [Artifact model](P3-persistence-artifacts.md), [review guards](P3-recovery-approval.md) and [P2 export UX](P2-screens.md#ux-s17--export-and-delivery-packaging) define compatible semantics. REQ-0017 through REQ-0023/0031/0041/0050/0059/0066/0067; NFR-0005/0012/0018/0022.

## Common client-report structure
All applicable sections carry explicit unavailable/not-applicable reasons instead of fabricated values: (1) report ID/version, (2) client/project reference, (3) job objective, (4) authorized execution scope, (5) input summary, (6) configuration summary, (7) safe execution environment, (8) operations performed, (9) results summary, (10) findings/exceptions, (11) validation evidence, (12) screenshots/supporting artifacts, (13) known limitations, (14) human review disposition, (15) approval metadata/reference, (16) final deliverable inventory. Report templates are structured data/render configuration, never arbitrary code. General logs exclude raw content; reviewed local reports may include approved selected client deliverables but never plaintext credentials or unrelated data.

## Proposed format capability matrix
P = proposed basic support profile; C = conditional fidelity/library feasibility and owner approval; dash = no intended direct rendering. No format is implemented. CSV/XLSX rows cannot represent all narrative/evidence semantics, so link manifest and limitations instead of claiming equivalent reports.
| Contract/output | HTML | PDF | CSV | XLSX | JSON | ZIP |
| --- | --- | --- | --- | --- | --- | --- |
| Execution/QA narrative | P passive encoded | C font/layout | P tabular summary only | C tabular summary | P structured | container only |
| Validation/change results | P | C | P check/row findings | C | P | container only |
| Finding/bug report | P | C | P issue index only | C issue index | P | evidence container |
| Review/approval record | P view | C | dash | dash | P sanitized record | container only |
| Artifact/package manifest | P view | dash | P inventory only | dash | P canonical structured | included manifest |
| Final deliverable package | dash | dash | dash | dash | manifest only | P container |

Passive HTML has encoded text, relative owned assets and no remote fonts/scripts/tracking; cannot execute untrusted website code. PDF pagination/embedded fonts/licensing/render engine unresolved; no perfect fidelity claim. ZIP entry paths/size/count limits and collision rules enforced; no extract-and-run instructions/scripts. JSON serialization and CSV formula safety validated under chosen format profiles.

## Versioned report data contracts
Every contract has schemaVersion major/minor, named ID, correlation, generatedAtUtc, sourceVersion and integrity algorithm/digest for referenced immutable content. Missing optional fields remain absent; required unavailable information has explicit error/unavailable state under schema, not guessed text. Required fields below are additional to this common header; ApprovalRecord/ReviewRecord are serialized domain records owned J, not grants invented by M.

### Contract — ExecutionReport
- Identifier: reportId; schema version: proposed 1.0.
- Required fields: jobId, jobVersionId, attemptId, module/operation versions, plan/config/input digest references, start/end, executionOutcome, per-item counts/dispositions, evidence refs, limitations; common header above.
- Optional fields: client/project display refs, environment safe summary, authorizedScopeRef, duration.
- Validation rules: Counts reconcile with operation profile; end required for terminal report; executionOutcome not check result/approval; bounded types/counts/strings and schema-major compatibility.
- Job/run linkage: explicit jobId/jobVersionId/attemptId; manifest associations must belong to the same scope.
- Artifact references: immutable artifact IDs/versions plus relative registered paths, size/hash; missing refs explicit.
- Integrity metadata: SHA-256/algorithm and source evidence/selection digests; final package digest in ExportRecord, not self-referential manifest.
- Error representation: errorId/code/category, affected scope, safe cause/recovery, evidence refs; check outcome distinct from execution outcome.

### Contract — ValidationReport
- Identifier: validationReportId; schema version: proposed 1.0.
- Required fields: job/version/attempt refs, artifact/version/hash refs, check IDs/versions, expected/observed safe values, explicit outcome, evidence refs; common header above.
- Optional fields: duration, warning confidence and profile limitations.
- Validation rules: Required check coverage explicit; zero checks NOT_RUN; unknown/failed checks cannot become PASSED; bounded types/counts/strings and schema-major compatibility.
- Job/run linkage: explicit jobId/jobVersionId/attemptId; manifest associations must belong to the same scope.
- Artifact references: immutable artifact IDs/versions plus relative registered paths, size/hash; missing refs explicit.
- Integrity metadata: SHA-256/algorithm and source evidence/selection digests; final package digest in ExportRecord, not self-referential manifest.
- Error representation: errorId/code/category, affected scope, safe cause/recovery, evidence refs; check outcome distinct from execution outcome.

### Contract — FindingReport
- Identifier: findingReportId; schema version: proposed 1.0.
- Required fields: job/version/attempt, findingId/rule, observation category, expected/observed safe context, evidence refs, unverified/confirmed/dismissed disposition; common header above.
- Optional fields: severity proposal, target/viewport time, reproduction steps and reviewer rationale.
- Validation rules: Confirmed defect requires HumanReview reference; environment/automation/inconclusive separated; no secret payload; bounded types/counts/strings and schema-major compatibility.
- Job/run linkage: explicit jobId/jobVersionId/attemptId; manifest associations must belong to the same scope.
- Artifact references: immutable artifact IDs/versions plus relative registered paths, size/hash; missing refs explicit.
- Integrity metadata: SHA-256/algorithm and source evidence/selection digests; final package digest in ExportRecord, not self-referential manifest.
- Error representation: errorId/code/category, affected scope, safe cause/recovery, evidence refs; check outcome distinct from execution outcome.

### Contract — ReviewRecord
- Identifier: reviewId; schema version: proposed 1.0.
- Required fields: job/version/attempt, scoped finding/manifest ref, reviewerLabel, timestamp, disposition, evidenceDigest; common header above.
- Optional fields: reason for ordinary confirm/dismiss; required rationale for warning acceptance.
- Validation rules: Valid explicit scope, current evidence; asserted local identity; no blanket failed-check waiver; bounded types/counts/strings and schema-major compatibility.
- Job/run linkage: explicit jobId/jobVersionId/attemptId; manifest associations must belong to the same scope.
- Artifact references: immutable artifact IDs/versions plus relative registered paths, size/hash; missing refs explicit.
- Integrity metadata: SHA-256/algorithm and source evidence/selection digests; final package digest in ExportRecord, not self-referential manifest.
- Error representation: errorId/code/category, affected scope, safe cause/recovery, evidence refs; check outcome distinct from execution outcome.

### Contract — ApprovalRecord
- Identifier: approvalId; schema version: proposed 1.0.
- Required fields: job/version/attempt, payloadManifestId/selectionDigest, each selected artifact/hash, validation/review evidenceDigest, reviewerLabel, timestamp, decision; common header above.
- Optional fields: invalidation/revocation event refs and rationale.
- Validation rules: Only J human use case; exact current finalized eligible selection; worker cannot write approval; bounded types/counts/strings and schema-major compatibility.
- Job/run linkage: explicit jobId/jobVersionId/attemptId; manifest associations must belong to the same scope.
- Artifact references: immutable artifact IDs/versions plus relative registered paths, size/hash; missing refs explicit.
- Integrity metadata: SHA-256/algorithm and source evidence/selection digests; final package digest in ExportRecord, not self-referential manifest.
- Error representation: errorId/code/category, affected scope, safe cause/recovery, evidence refs; check outcome distinct from execution outcome.

### Contract — ArtifactManifest
- Identifier: manifestId; schema version: proposed 1.0.
- Required fields: schemaVersion, job/version/attempt, artifact entries with ID/type/relativeLocation/size/hash/producer/validation/retention; common header above.
- Optional fields: source original reference (not raw client content), missing/incomplete flags and error refs.
- Validation rules: Safe paths, unique identity, declared hash algorithm, no finalized classification for incomplete/missing bytes; bounded types/counts/strings and schema-major compatibility.
- Job/run linkage: explicit jobId/jobVersionId/attemptId; manifest associations must belong to the same scope.
- Artifact references: immutable artifact IDs/versions plus relative registered paths, size/hash; missing refs explicit.
- Integrity metadata: SHA-256/algorithm and source evidence/selection digests; final package digest in ExportRecord, not self-referential manifest.
- Error representation: errorId/code/category, affected scope, safe cause/recovery, evidence refs; check outcome distinct from execution outcome.

### Contract — DeliveryPackageManifest
- Identifier: packageManifestId; schema version: proposed 1.0.
- Required fields: schemaVersion, payloadManifestId/selectionDigest, approvalId, job/version/attempt, package version, safe inventory paths/sizes/hashes, exclusions/limitations; common header above.
- Optional fields: reviewed supporting evidence/test-doc/config summaries, approval attestation reference, source profile refs.
- Validation rules: Only approved payload set, exclusion/redaction explicit, current hashes verified; packaging metadata cannot change approved payload; bounded types/counts/strings and schema-major compatibility.
- Job/run linkage: explicit jobId/jobVersionId/attemptId; manifest associations must belong to the same scope.
- Artifact references: immutable artifact IDs/versions plus relative registered paths, size/hash; missing refs explicit.
- Integrity metadata: SHA-256/algorithm and source evidence/selection digests; final package digest in ExportRecord, not self-referential manifest.
- Error representation: errorId/code/category, affected scope, safe cause/recovery, evidence refs; check outcome distinct from execution outcome.

## Result and integrity semantics
Report check outcomes: PASSED, FAILED, WARNING, INCONCLUSIVE, NOT_RUN. P2 PASS/FAIL presentation maps to PASSED/FAILED without changing meaning. BLOCKED/SKIPPED check is NOT_RUN with exact reason, not PASSED; execution FAILED/CANCELLED/INTERRUPTED/PARTIAL is separate context. Unverified observations remain unverified; human-confirmed findings carry review refs. Reports disclose expected failures/waivers if approved later, not silently passing them.

Avoid approval/hash cycles: approve an immutable payload manifest and content set (including any reviewed report versions); an approval attestation references that payload digest and decision, never its own final package hash. The final package inventory may include a separately generated sanitized attestation sidecar with its own hash and schema; it cannot rewrite an already approved report to insert new approval text. Package manifest excludes its own hash; ExportRecord stores final container/manifest digests after write. Any requested payload/report rewrite produces a new selection/review/approval. This permits real approval metadata without making checksum computation circular.

## Package procedure
1. Select exact finalized valid artifacts/evidence and inspect preview; show job partial/failure context, exclusions and limitations. Raw inputs, credentials, unrelated clients, logs/traces with unredacted secrets and unsigned/unreviewed scripts excluded by default.
2. J validates current required output checks/human reviews and records explicit approval for that payload selection and evidence digest. No module finalizes approval.
3. N prepares local export plan: user-chosen allowed local destination, package label/version (safe project/job/attempt IDs with optional sanitized display name), intended inventory and size; duplicate names require explicit deterministic rename mapping or block, never silent overwrite.
4. Recheck source hashes/current approval, hold/read stable handles or copy and verify against approved digests; reject TOCTOU changes. Stage package on destination volume where supported; verify inventory/size/hash and source selection again.
5. Verify final artifact/manifest and commit export record only after actual write success; partial files remain explicitly incomplete. A ZIP CRC is not the sole integrity proof; payload cryptographic hashes required.
6. Repackage unchanged payload with a new export occurrence/version and current approval; changed payload/selection needs new manifest/approval. Destination collision/deletion requires exact fresh consent; source originals/history unchanged.

No automatic email/cloud delivery, issue-tracker publication, freelance-platform automation or website deployment. EXPORTED means verified local output, not received by client. Test documents/synthetic config summaries may be supporting deliverables only when explicitly selected/reviewed; source credentials/raw client originals never swept into package.

## Acceptance prerequisites
Schema required-field/version/outcome tests; safe HTML/CSV/ZIP behavior; report-to-artifact referential integrity; unverified defect labeling; failed/not-run checks visible; approval attestation/hash-cycle prevention; modified source during export; duplicate filename and disk-full partial export. Existing TEST-0041 through TEST-0046, TEST-0099/0100, TEST-0131 through TEST-0134 and new architecture cases remain NOT_RUN.
