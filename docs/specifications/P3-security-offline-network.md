# P3 security, privacy, offline and authorized networking

Status: PROPOSED assessment; no penetration/isolation/privacy tests. [Security book](../governance/07-security-book.md) remains process authority and [master](../governance/00-master-rulebook.md) policy authority. TH references are local threat IDs, not replacement project RISK IDs. [Risk register](../governance/09-execution-book.md) owns status. COM-S evaluates permissions, but prevention requires actual OS/driver enforcement; process separation alone is not a complete sandbox.

## Assets, actors and trust boundaries
Assets: client originals/snapshots, config/templates, artifacts/evidence, local DB/history, authorizations/reviewer decisions, credentials, backups and delivery manifests. Actors: authorized operator/reviewer; accidental operator; malicious file/template/site supplier; local user/malware with filesystem access; compromised dependency/browser/parser. No external account or enterprise identity system presumed.

Boundaries: UI intent -> B/S domain guard; trusted app -> untrusted worker input/content; worker -> attempt-only storage; persistence -> file publication protocol; browser -> explicitly authorized website; review -> exact artifact/evidence approval; export/backup -> user-selected controlled local destination. Modules cannot cross private workspaces or obtain DB/approval access. Host OS/admin compromise is a residual risk, not prevented by hashes alone.

Likelihood convention: UNKNOWN empirically; qualitatively PLAUSIBLE where a supplied hostile file/content or interruption can reach the described boundary. This is an architecture judgment, not measured frequency. Impact HIGH for client integrity/privacy/scope breaches; severity needs owner risk appetite review. P/D/R below mean preventative/detective/recovery controls, all unverified proposals. All residual exposures remain OPEN.

## TH-01 — Malicious client-supplied files
- Likelihood: UNKNOWN measured; PLAUSIBLE architecture scenario.
- Impact: HIGH — Parser compromise, client-data access.
- Mitigations: P: bounded format inspection, trusted parsers in restricted workers; D: exit/resource/integrity monitoring; R: quarantine attempt.
- Residual risk: Same-user process compromise can exceed app-only controls; actual sandbox unverified; OPEN until verification/acceptance.
- Verification method: Synthetic malformed/parser exploit-style fixtures; verify capability confinement in P5/P12; planned only, NOT_RUN.
- Project risk: RISK-0007; owner security/architecture lead with component owner; P5/P12 and relevant module gate.

## TH-02 — Path traversal
- Likelihood: UNKNOWN measured; PLAUSIBLE architecture scenario.
- Impact: HIGH — Writes/reads beyond confirmed workspace.
- Mitigations: P: safe relative names and handle-based confinement; D: path audit; R: stop/quarantine.
- Residual risk: String canonicalization alone insufficient against races; OPEN until verification/acceptance.
- Verification method: Parent-relative/rooted/encoded traversal and reserved device names; planned only, NOT_RUN.
- Project risk: RISK-0002; owner security/architecture lead with component owner; P5/P12 and relevant module gate.

## TH-03 — Symbolic links and junctions
- Likelihood: UNKNOWN measured; PLAUSIBLE architecture scenario.
- Impact: HIGH — Workspace escape and original modification.
- Mitigations: P: reject reparse/escaped paths and verify handles; D: compare source/target identity; R: invalidate artifact.
- Residual risk: Filesystem race until Windows handle/ACL tests; OPEN until verification/acceptance.
- Verification method: Swap junction/reparse target between validation and open; planned only, NOT_RUN.
- Project risk: RISK-0007; owner security/architecture lead with component owner; P5/P12 and relevant module gate.

## TH-04 — Arbitrary command execution
- Likelihood: UNKNOWN measured; PLAUSIBLE architecture scenario.
- Impact: HIGH — Code execution with user privileges.
- Mitigations: P: typed allowlisted operations/fixed worker launch, no project/template scripts; D: process-tree observation.
- Residual risk: Imported active document/rendering feature may trigger hidden execution if parser unsafe; OPEN until verification/acceptance.
- Verification method: Template command payload, quote/metacharacter and untrusted build fixtures; planned only, NOT_RUN.
- Project risk: RISK-0007; owner security/architecture lead with component owner; P5/P12 and relevant module gate.

## TH-05 — Spreadsheet formula injection
- Likelihood: UNKNOWN measured; PLAUSIBLE architecture scenario.
- Impact: HIGH — Unexpected execution/exfiltration when client opens export.
- Mitigations: P: explicit cell type/formula-safe export profile, no implicit eval; D: leading formula/link findings; R: review or block export.
- Residual risk: Downstream spreadsheet application behavior cannot be guaranteed; OPEN until verification/acceptance.
- Verification method: Synthetic =,+,-,@ prefixes, DDE/external-link formulas and preservation/review cases; planned only, NOT_RUN.
- Project risk: RISK-0006; owner security/architecture lead with component owner; P5/P12 and relevant module gate.

## TH-06 — Embedded macros
- Likelihood: UNKNOWN measured; PLAUSIBLE architecture scenario.
- Impact: HIGH — Malicious office behavior.
- Mitigations: P: disallow macro execution and unsupported macro-enabled formats; D: capability inspection.
- Residual risk: Some container inspection may be incomplete until library validation; OPEN until verification/acceptance.
- Verification method: Macro-bearing container inert/rejected, no subprocess/network effects; planned only, NOT_RUN.
- Project risk: RISK-0007; owner security/architecture lead with component owner; P5/P12 and relevant module gate.

## TH-07 — Malformed documents
- Likelihood: UNKNOWN measured; PLAUSIBLE architecture scenario.
- Impact: HIGH — Crash, misleading content or unsafe parsing.
- Mitigations: P: size/depth/profile/parser restrictions; D: typed parse errors; R: preserve original, linked retry.
- Residual risk: Unsupported fidelity and parser CVEs remain; OPEN until verification/acceptance.
- Verification method: Corrupt PDF/DOCX inputs and unexpected embedded content; planned only, NOT_RUN.
- Project risk: RISK-0006; owner security/architecture lead with component owner; P5/P12 and relevant module gate.

## TH-08 — Zip bombs/decompression
- Likelihood: UNKNOWN measured; PLAUSIBLE architecture scenario.
- Impact: HIGH — Memory/disk exhaustion and file escape.
- Mitigations: P: bound compressed/expanded bytes/count/depth/ratio/time; D: streaming counters; R: terminate/quarantine.
- Residual risk: Library may expand before callback; reject unsafe libraries/profiles; OPEN until verification/acceptance.
- Verification method: Synthetic high-ratio/nested archive and zip-entry traversal fixtures; planned only, NOT_RUN.
- Project risk: RISK-0007; owner security/architecture lead with component owner; P5/P12 and relevant module gate.

## TH-09 — Oversized files
- Likelihood: UNKNOWN measured; PLAUSIBLE architecture scenario.
- Impact: HIGH — OOM or unbounded work.
- Mitigations: P: bounded input/profile preflight; D: measured resource limits; R: safe failure.
- Residual risk: Budgets lack representative data evidence; OPEN until verification/acceptance.
- Verification method: Boundary just below/at/over chosen limits, NOT_RUN; planned only, NOT_RUN.
- Project risk: RISK-0005; owner security/architecture lead with component owner; P5/P12 and relevant module gate.

## TH-10 — Resource exhaustion
- Likelihood: UNKNOWN measured; PLAUSIBLE architecture scenario.
- Impact: HIGH — UI loss, corrupt partial output.
- Mitigations: P: controlled queue/concurrency and OS job resource limits; D: memory/heartbeat/deadline; R: kill owned tree/reconcile.
- Residual risk: OS limits not a complete file/network sandbox; OPEN until verification/acceptance.
- Verification method: Large workload, runaway child and frozen worker; planned only, NOT_RUN.
- Project risk: RISK-0007; owner security/architecture lead with component owner; P5/P12 and relevant module gate.

## TH-11 — Secrets in logs
- Likelihood: UNKNOWN measured; PLAUSIBLE architecture scenario.
- Impact: HIGH — Credential/client data disclosure.
- Mitigations: P: typed safe events/redaction; D: seeded-secret scans; R: consented managed purge/invalidate leaked report.
- Residual risk: Redaction not proof against every unknown data shape; OPEN until verification/acceptance.
- Verification method: Synthetic canary values across logs/reports/browser traces; planned only, NOT_RUN.
- Project risk: RISK-0003; owner security/architecture lead with component owner; P5/P12 and relevant module gate.

## TH-12 — Unauthorized filesystem access
- Likelihood: UNKNOWN measured; PLAUSIBLE architecture scenario.
- Impact: HIGH — Other client/history/OS exposure.
- Mitigations: P: least privilege/restricted grants and isolated workspace; D: access observation; R: abort affected capability.
- Residual risk: Same-user unrestricted token defeats hard confinement; OPEN until verification/acceptance.
- Verification method: Worker attempt reading sibling/original/DB/backup paths; planned only, NOT_RUN.
- Project risk: RISK-0007; owner security/architecture lead with component owner; P5/P12 and relevant module gate.

## TH-13 — Unsafe temporary directories
- Likelihood: UNKNOWN measured; PLAUSIBLE architecture scenario.
- Impact: HIGH — Link/hijack/sensitive leftover exposure.
- Mitigations: P: random owned dirs/ACLs, no shared predictable paths; D: registered lease ownership; R: reconciled cleanup.
- Residual risk: Power loss may leave sensitive staged bytes; OPEN until verification/acceptance.
- Verification method: Precreated name/link, crash cleanup and retained evidence tests; planned only, NOT_RUN.
- Project risk: RISK-0002; owner security/architecture lead with component owner; P5/P12 and relevant module gate.

## TH-14 — Untrusted website content
- Likelihood: UNKNOWN measured; PLAUSIBLE architecture scenario.
- Impact: HIGH — Browser exploit, download or client-data exposure.
- Mitigations: P: fresh scoped browser, no local-file capability, downloads denied; D: network/process monitoring; R: close owned profile.
- Residual risk: Browser child network paths/isolation need proof; OPEN until verification/acceptance.
- Verification method: Controlled malicious fixture, download/file URL and external scheme cases; planned only, NOT_RUN.
- Project risk: RISK-0008; owner security/architecture lead with component owner; P5/P12 and relevant module gate.

## TH-15 — Unauthorized network connections
- Likelihood: UNKNOWN measured; PLAUSIBLE architecture scenario.
- Impact: HIGH — Privacy/scope breach.
- Mitigations: P: denied network by default, synthetic-only explicit grants; D: external request observation; R: fail closed capability.
- Residual risk: Browser intercept coverage is not an OS egress guarantee; OPEN until verification/acceptance.
- Verification method: Hidden analytics/DNS/WebRTC/socket/service-worker/browser traffic observation; planned only, NOT_RUN.
- Project risk: RISK-0008; owner security/architecture lead with component owner; P5/P12 and relevant module gate.

## TH-16 — Redirects outside scope
- Likelihood: UNKNOWN measured; PLAUSIBLE architecture scenario.
- Impact: HIGH — Unauthorized crawling/action.
- Mitigations: P: reauthorize each redirect/resource/method/host/path and resolved destination; D: denied-request audit.
- Residual risk: Routing gaps or DNS changes may escape unless enforced; OPEN until verification/acceptance.
- Verification method: Cross-origin redirect/asset/CNAME/private address changes; planned only, NOT_RUN.
- Project risk: RISK-0008; owner security/architecture lead with component owner; P5/P12 and relevant module gate.

## TH-17 — Local database corruption
- Likelihood: UNKNOWN measured; PLAUSIBLE architecture scenario.
- Impact: HIGH — Lost history/approval or false success.
- Mitigations: P: supported transactions/durability/constraints; D: integrity/FK checks; R: verified backup/staged restore.
- Residual risk: Filesystem/power loss/host malware beyond app guarantees; OPEN until verification/acceptance.
- Verification method: Interrupt DB writes/migration, corrupted backup and missing artifact; planned only, NOT_RUN.
- Project risk: RISK-0009; owner security/architecture lead with component owner; P5/P12 and relevant module gate.

## TH-18 — Worker crashes
- Likelihood: UNKNOWN measured; PLAUSIBLE architecture scenario.
- Impact: HIGH — Incomplete output mislabeled complete.
- Mitigations: P: supervisor/typed protocol; D: exit/heartbeat; R: attempt interruption and intent reconciliation.
- Residual risk: Some incomplete state cannot resume; OPEN until verification/acceptance.
- Verification method: Kill at every finalization/transition step; planned only, NOT_RUN.
- Project risk: RISK-0009; owner security/architecture lead with component owner; P5/P12 and relevant module gate.

## TH-19 — Privilege escalation
- Likelihood: UNKNOWN measured; PLAUSIBLE architecture scenario.
- Impact: HIGH — Broader OS permissions.
- Mitigations: P: ordinary jobs standard user, trusted binaries and least privilege; D: privilege/process review.
- Residual risk: OS/browser/parser flaws remain outside app-only control; OPEN until verification/acceptance.
- Verification method: Standard-user install/run and no unsolicited elevation; planned only, NOT_RUN.
- Project risk: RISK-0007; owner security/architecture lead with component owner; P5/P12 and relevant module gate.

## TH-20 — Unapproved destructive operations
- Likelihood: UNKNOWN measured; PLAUSIBLE architecture scenario.
- Impact: HIGH — Original/client data loss.
- Mitigations: P: separate output default, exact fresh consent and backup; D: action/target audit; R: verified rollback if supported.
- Residual risk: In-place recovery not always possible; unsupported operations disabled; OPEN until verification/acceptance.
- Verification method: Reject consent, changed target/plan and failed backup; planned only, NOT_RUN.
- Project risk: RISK-0002; owner security/architecture lead with component owner; P5/P12 and relevant module gate.

## TH-21 — Unauthorized output modification
- Likelihood: UNKNOWN measured; PLAUSIBLE architecture scenario.
- Impact: HIGH — Stale approval or substituted export.
- Mitigations: P: immutable managed publication/ACL; D: rehash manifest/evidence before approval/export; R: stale invalidation.
- Residual risk: Same-user attacker may alter DB and hashes; not tamper-proof; OPEN until verification/acceptance.
- Verification method: Modify/remove output after approval, during packaging and restore; planned only, NOT_RUN.
- Project risk: RISK-0002; owner security/architecture lead with component owner; P5/P12 and relevant module gate.

## TH-22 — Backup exposure
- Likelihood: UNKNOWN measured; PLAUSIBLE architecture scenario.
- Impact: HIGH — Sensitive files/keys leaked.
- Mitigations: P: scoped protected local backup, encryption option/key separation; D: manifest/access review; R: controlled revoke/delete.
- Residual risk: Key loss and other local users/malware need accepted threat model; OPEN until verification/acceptance.
- Verification method: Wrong user/key, copied backup, incomplete/invalid hash restore; planned only, NOT_RUN.
- Project risk: RISK-0003; owner security/architecture lead with component owner; P5/P12 and relevant module gate.

## TH-23 — Dependency/supply-chain compromise
- Likelihood: UNKNOWN measured; PLAUSIBLE architecture scenario.
- Impact: HIGH — Malicious or unlawfully redistributed component.
- Mitigations: P: pinned trusted sources/digests/licenses/transitives; D: inventory/advisory review; R: quarantine unsafe version.
- Residual risk: Unsigned/unreviewed components and browser binaries pending adoption; OPEN until verification/acceptance.
- Verification method: Verify package provenance/signatures/checksums and redistribution manifest in P5/P13; planned only, NOT_RUN.
- Project risk: RISK-0003; owner security/architecture lead with component owner; P5/P12 and relevant module gate.

## Control ownership matrix
| Control | Responsible boundary / proposed verification |
| --- | --- |
| A Input validation | H/module parser with S limits; typed schema, counts/encoding/fidelity boundaries; invalid/malicious fixtures |
| B Workspace isolation | K/F + OS ACL/token mechanisms; cross-attempt/sibling path denial incl. reparse races |
| C Worker permissions | F/S + OS; default no network, readonly scoped inputs, own staging only; verify effective token and child rights |
| D File/directory access | K/S + OS handles/ACLs; path grant, reserved names/collisions; TOCTOU tests |
| E Restricted commands | B/F/G; fixed trusted program/options, no shell/script import; injection/process observation |
| F Network authorization | S + QA adapter/OS enforcement; per-origin/path/method/action/expiry/resolution and redirect check; observed denied requests |
| G Credential protection | S + Windows native credential protection candidate; opaque references, no templates/logs; wrong-user/session protection tests |
| H Safe logging | O/report adapter; allowlisted safe fields/redaction; seeded secret and client-content scans |
| I Integrity | K/I/J/N; stream hash/reconciliation, independent validation, approval/export recheck; modified/missing file tests |
| J Module trust/version | G/F + installation provenance; pinned module digest/schema, no arbitrary plugin; wrong-package/version tests |
| K Backup protection | R/S/OS; consistent snapshot, ACL/encryption proposal, key loss/restore validation |
| L Destructive consent | B/S human intent, K actual target; current exact plan/target + backup where required; reject/change/race tests |
| M Final approval | J/C + explicit human review; durable exact manifest/evidence decision, no worker authority; bypass/stale tests |
| N Dependency verification | Architecture/release owners, trusted build source inventory; source licenses/transitives/signature/checksum review before use |
| O Secure install/update | Release owner + OS verification; local verified offline-capable media, backup/version checks; no automatic network updater or paid signing assumption |

## Local secrets and privacy
Only authorized QA scenarios may need target credentials (optional, not required to run app). Evaluate Windows Credential Manager/DPAPI-protected local store with user-scoped access and no plaintext copies in settings, templates, DB examples, diagnostics or repo. No OS credential-store test performed. A protected credential blob is not portable backup key recovery; export/migration of credentials requires separate legitimate owner handling and must not be implied by workspace restore. Browser traces/screenshots can expose synthetic/session values; minimize/redact, restrict local access and preview before report inclusion.

Client owns data; application manages only consented local copies/metadata. No background analytics, telemetry, synchronization, subscription checks, AI inference, cloud DB, external processing APIs or mandatory sign-in. Original client data never enters website requests; only explicitly authorized synthetic values. Deletion preview lists managed data, dependent evidence and stale-approval consequences; originals/unrelated exports excluded; retention periods remain O-07. Backup location cannot silently become cloud-synced storage. Diagnostic local export has safe-field preview and explicit target; no remote support upload. Logical deletion is not guaranteed physical secure erasure on SSD; requirement/OS threat review needed if secure erasure demanded.

## Offline behavior matrix
| Area | Required design behavior when network denied | Future proof |
| --- | --- | --- |
| Startup/UI/local DB | No external sign-in/license/AI call; local reads/writes only | Launch disconnected with blocked egress |
| Spreadsheet/document | Local parsers/assets, supported feature profiles only; no external formula/font/OCR API fallback | Offline complete jobs and evidence; external-link deny |
| Local maintenance | Local working copy, no auto npm/build/deploy/project script | Script/network traps remain inert |
| History/templates/reports | Local data/resources; no CDN/fonts/support fetch | Read/apply/render disconnected |
| Export/package | Explicit local target and manifest verification | Offline package hashes and review |
| Backup/restore | Local protected consistent snapshot/key handling | Disconnected restore integrity |
| Diagnostics/help | Bundled local help/redacted logs; no telemetry | Observe zero unintended requests |

REQUIRED tests NFR-0005/0006/0021 remain NOT_RUN. Optional live QA failure must not disable local workflows. Missing dependency/resource blocks that supported operation explicitly, never silently fetches it.

## Authorized website operations
Authorization record defines canonical scheme/host/port, allowed paths/methods/actions, scenario/synthetic data, request/page/depth/byte/time budgets, allowed redirects/assets, permission evidence and expiry/revocation. Exclude platform automation. Target editing/planning does not request URLs. Every actual navigation/resource/redirect/XHR/fetch/socket/download action needs policy coverage before effect; DNS resolution/host changes and loopback/private ranges fail closed unless exact controlled target authorization includes them. Host labels alone are insufficient; reject unsupported schemes/file URLs, credentials embedded in URLs and unauthorized DNS/redirect destinations.

Browser/network adapter must prevent service-worker/cache/background/preload/WebRTC/extension/proxy bypass and validate TLS; no insecure-certificate mode to pass checks. Authentication uses explicitly authorized least-privilege test account/session; no bypass/CAPTCHA circumvention; no secrets in output evidence. State-changing forms need action-specific authorization/consent; lost response may mean effect occurred and is not blindly retryable. Requests are bounded/idempotently retried only under current scope. Browser profiles are fresh per attempt, credentials/sessions cleaned under ownership; screenshot evidence labeled with capture context. No mobile-device claim from viewport emulation.

Critical OPEN: common request interception is not proof that all browser/child-process traffic is restricted. Candidate OS egress controls or a supported audited browser enforcement design must be demonstrated without introducing compulsory administrative privileges/network service. If strict scope cannot be enforced, live QA capability remains unavailable until an approved safe alternative exists. Do not weaken target authorization to adopt a convenient library. [Windows/P5 plan](P3-windows-compatibility.md) and [ADR-0006](../adr/ADR-0006-authorized-browser.md) retain this adoption prerequisite.
