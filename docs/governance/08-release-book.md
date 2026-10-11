# Release book

Status: P4 proposed build/packaging/update standards; implementation and release approval remain future P13/P14 work.

## Purpose
Owns release packaging, distribution checklist, release approval and maintenance policy.

## Inputs and planned scope
Prepare Windows target matrix, dependency/license inventory, build provenance, installer/upgrade/uninstall and rollback evidence, release notes and support limitations after approved hardening.

## Records and working rules
Record exact tool/dependency/OS versions, test evidence, known issues, risk dispositions and human release approval. Distribution/signing choices and Windows 10 support feasibility remain unverified. No release action is authorized by P0.

## Acceptance criteria
Release only with approved acceptance evidence, resolved blockers or approved noncritical exceptions, verified packaging/offline behavior and explicit human release authorization. Maintenance changes repeat relevant impact and regression gates.

## References
[Master policy and phase gates](00-master-rulebook.md) · [Execution state](09-execution-book.md) · [Trace matrix](../test-matrix/README.md)

## P4 build and packaging standards
This book owns REL engineering conventions; permanent release policy remains in the master. Owner: release lead with QA/security/license owners. Scope: future authorized builds/installers/manual updates. Rationale: reproducible reviewed artifacts and preservation of local client data. Each rule needs the stated evidence; no actual build or installer executed here.

| Rule | Required future standard / evidence | Gate |
| --- | --- | --- |
| REL-01 Build provenance | Exact toolchain/OS/architecture/options, pinned approved dependencies/frozen locks, source revision/dirty scope, input hashes, offline prerequisite inventory, build logs/status and artifact ID/hash/manifest/SBOM/notices | Clean-environment build verification; configuration reproducibility is not byte-identical proof |
| REL-02 Determinism | Record variable timestamps/paths/signing/compression/font effects; verify repeated clean builds before byte-for-byte hash claim; measured differences documented | No invented reproducibility claim from pinned config alone |
| REL-03 Packaging profiles | Installer vs portable choice conditional on ADR/P5; separate program files/user LocalAppData-like managed workspace; bundling must include verified freely redistributable runtime/native/browser/document/font resources for chosen stack | No hidden runtime downloads/sign-in/subscription; unsupported profile explicitly blocked |
| REL-04 Worker runtime matrix | Python lane: pinned interpreter/native wheels/freezer licenses; Node lane: runtime/driver/browser versions and notices; .NET lane: approved runtime/self-contained dependencies; Rust/Tauri lane: approved native/WebView terms; not a mandate to use all lanes | Verify exact approved lane on target Windows; no product dependency on Codex/AI |
| REL-05 Installer safety | Minimal documented privileges, approved user-selectable path, validated filesystem locations; initialization cannot overwrite existing DB/workspace; recoverable install journal/rollback; Start-menu/uninstall ownership explicit | Install failure/standard-user/permission/space/AV tests |
| REL-06 Offline readiness | Local processing/startup/history/templates/reports/export/backup after installation without internet/AI/cloud/auth/telemetry/license service; website QA separately requires authorized target access | Actual packaged disconnected/egress-observed tests, no hidden fallback |
| REL-07 Upgrade | Preflight current schema/runtime/OS/space, compatible backup, stop dispatch/owned workers, bounded verified migrations, commit schema version last; local manual update remains possible | Upgrade/failed migration/recovery/old-data integrity tests |
| REL-08 Rollback | State exact data-format compatibility and known impossibility of old binary reading new schema; use validated compatible backup restore where necessary; notify user, retain release notes | No assumed reversible migration or silent data loss |
| REL-09 Uninstall | Remove owned program files only by default; preserve jobs/client inputs/outputs/evidence/backups; valuable managed user-data deletion separate exact consent after backup/export option | No broad recursive delete/unrelated directory purge; uninstall/reinstall/data preservation evidence |
| REL-10 Runtime update trust | Manual/offline signed or provenance/hash-verified packages, dependency/notice inventory and exact approvals; signing/distribution mechanism pending evidence, no mandatory paid service/cloud updater | Mismatched/tampered/unsupported update rejects; no signature bypass |
| REL-11 Release dossier | Approved scope, implementation trace, relevant passing actual tests/counts, Windows/install/offline/security/license/dependency/accessibility/performance/recovery/data integrity, documentation/known issues and explicit owner release authorization | Compilation alone insufficient; mandatory missing evidence or critical failure BLOCKED |

## Windows target and lifecycle gate
REL-12 owner Windows/release lead; rationale supported/security-maintainable distribution; evidence exact edition/version/build/CPU architecture/RAM/disk/display/accessibility/WebView/browser/native/runtime/installer privileges/ACL/antivirus profile plus vendor statements and actual native tests. [P3 Windows classification](../specifications/P3-windows-compatibility.md) is historical documentary evidence only. Cloud Linux cannot prove laptop compatibility. Windows 10 support lifecycle/ESU/LTSC maintenance implications and upstream runtime/browser support must be confirmed for the exact target; don't adopt unsupported old runtime merely to meet timeline. Unknown owner laptop facts/support/license clearance remain release/adoption blockers. No final runtime/installer framework selected here.

## Local disaster recovery and operational material
REL-13 owner backup/release lead; scope database/workspace/artifacts/config/templates/migration/export recovery; rationale prevent loss; evidence consistent DB snapshot + verified artifact/config/template manifest/schema/module versions/checksums and tested restore under space/key/permission failures. Backup destination/retention/ACL/encryption/key-loss policy must be explicitly selected. A backup on the same physical disk does not protect against disk failure: use a separately controlled local device/destination; no cloud dependency. Application crash/failed upgrade/corrupt DB/missing files/interrupted export/accidental deletion all require documented repair-or-restore paths; no promise to recover missing data without an intact backup. Original external sources not overwritten.

REL-14 owner documentation/support lead; scope released user/support material; rationale align promises with shipped capabilities; enforcement actual build/profile review. Release version must have installation/getting-started/four module/error-reference/troubleshooting/backup-restore/offline/supported-format/limitations/release-notes/local-diagnostics guides. Describe measured supported operations, licensing/OS boundaries and known issues, not unimplemented P3/P4 proposals. Troubleshooting explains happened/affected/next and safe local evidence export; never requests client secrets or automatic uploads.

## Version and release acceptance
App/module version, IPC/config/template/report/export schema and DB migration versions follow [development compatibility rules](04-development-book.md). Release manifest records the exact compatibility tuple and input/output inventory. Mandatory gates BLOCKED for missing evidence; noncritical exceptions require the governance-authorized human risk disposition with scope/expiry, never a false test pass. No release tagging/build/signing/distribution in P4. Actual future assurance belongs testing and P13 report.
