# P5 prerequisite decision package

Date: 2026-10-11 UTC. Status: DOCUMENTARY PROPOSAL; P5 BLOCKED. Owner authorization: latest “P5 PREREQUISITE DECISION PACKAGE”, documentation only. This task supersedes the previous reconciliation-only task boundary in AGENTS for these authorized documents; no permanent policy changes. [Prerequisite plan](P5-prerequisites-plan.md) owns blocker dispositions, [execution book](../governance/09-execution-book.md) owns milestone state, and [development](../governance/04-development-book.md), [testing](../governance/06-testing-book.md), [security](../governance/07-security-book.md) and [release](../governance/08-release-book.md) own durable standards. This specification consolidates task evidence and the approval proposal, not another rulebook.

## Repository and evidence boundary
Verified branch `docs/governance-baseline`, HEAD `15acfb58dfa9f9616b60b2c41c771953cbfc878c`; starting four modified shared files and five untracked P5 files match the owner inventory. No staged changes. P0–P4 documentary completion remains recorded, all eight ADRs PROPOSED, all 239 application acceptance definitions NOT_RUN. No executable experiment, dependency installation, installer/package download, build or Git mutation is authorized or performed. Fetches below retrieve documentation, source text and release/package metadata only, using normal TLS; a retrieved source hash is not a verified binary signature.

## Initial candidate comparison and recommendation — historical
Earlier conditional recommendation (superseded for the supplied Home target by the review below): **EXP-N1, .NET SDK 10.0.401; .NET/Windows Desktop runtime and WPF 10.0.12; C# supplied by that SDK; Microsoft.Data.Sqlite and Microsoft.Data.Sqlite.Core 10.0.12; SQLitePCLRaw bundle/core/provider/native packages proposed at 2.1.12**, with native SQLite engine/build and complete dependency closure still pending. Target proposal is native supported Windows x64; framework target net10.0-windows with WPF, separate net10.0 worker and harness. No production architecture adopted. Do not execute this partly specified tuple: the missing native engine, package closure, target and authorization are real gates, not optional details.

Why this candidate: follows the conditional preference in [ADR-0002](../adr/ADR-0002-desktop-stack.md), can prove native startup and portable self-contained packaging without a browser shell, uses core facilities for JSON, checksums, bounded pipes and ZIP, and allows one small SQLite provider rather than an ORM. An SDK includes development tooling; the final experimental package must not require the SDK on the target. This is an experiment permission proposal, not approval of any ADR or a mandate for production C#.

| Candidate / exact proposed root versions | Compatibility evidence and assumptions | Dependencies / licensing | Strengths | Limits and risks / required experiments |
| --- | --- | --- | --- | --- |
| EXP-N1 .NET SDK 10.0.401, runtime/WPF 10.0.12, Microsoft.Data.Sqlite/Core 10.0.12, SQLitePCLRaw 2.1.12 | Official release metadata gives these .NET versions; current supported-OS table lists specific Windows10 enterprise/IoT versions, not unknown Home/Pro. x64 laptop and applicable lifecycle support unverified | Runtime/WPF/provider MIT; wrappers Apache-2.0; native SQLite provenance/version, runtime-pack/SDK notices and closure pending | Native UI, shared worker/runtime, no webview or broker, good minimal vertical slice | WPF requires Windows; .NET absent in cloud. Must prove native/offline startup, worker supervision, artifacts/DB consistency, accessibility basics and packaging; unsupported owner target disqualifies this tuple |
| Python 3.13.16, PySide6 6.12.0, PyInstaller 6.22.3 | CPython exact tag and Windows source fetched; source explicitly ties support to Microsoft lifecycle. Qt exact Windows build support unavailable; wheel architecture pending | PSF/historical notices; PySide metadata LGPL/GPL options; Qt/module/shiboken licenses and freezer exception/closure pending; PySide Essentials/Addons 6.12.0, WebEngine/Pdf 6.12.0.140 appear in current metadata | Strong future document/data ecosystem, one language, native-widget candidate | Greater native wheel/freezer/license surface, unwanted WebEngine components in default dependency graph; prove supported OS, permitted module-only install, native widgets, cleanup, packaging and notices before use |
| Electron 44.7.0, Node development prerequisite minimum 22.12.0 from metadata (exact development Node pin NOT selected) | Pinned Electron README says Windows10+ x64/arm64; minimum-build/lifecycle and exact embedded engine support still pending | Electron MIT; embedded Chromium/Node/third-party notices; npm ranges require closure. Embedded engine source revisions recorded below; minimum Node constraint is not an approved patch | Cross-platform UI; documentary Windows10 statement broader than .NET table | Higher browser/update/size/resource surface; must prove OS/build, no hidden egress, IPC security, keyboard semantics, native persistence and clean portable package; not selected for this small experiment |
| Previously proposed EXP-L1 installed CPython 3.12.14 / reported SQLite 3.53.1, Linux only | Host inventory only; no laptop or desktop packaging proof | Installed license presence, binary/native origin incomplete | No new installation for a narrow core-contract experiment | Cannot answer native startup/Windows packaging objective; retain as historical unapproved alternative, not substitute for EXP-N1 |

No alternative is silently adopted. Tauri/Rust/WebView2 remain the historical P3 alternative, deferred here because evaluating an additional toolchain/browser-runtime tuple does not reduce the smallest useful experiment. Cloud/microservices/paid APIs are excluded by master policy. If the laptop is not a vendor-supported target for EXP-N1, stop that proposal and investigate a supported alternative; do not downgrade to obsolete software or change the OS target without owner decision.

Release metadata is a snapshot, not “latest” at future execution. Revalidate versions, lifecycle and advisories before approval/execution; any materially changed tuple needs recorded review. No vulnerability clearance has been obtained in this task.

## Dependency evidence register
Evidence states describe documentation, not adoption: VERIFIED_DOCUMENTATION = fetched official text supports the stated narrow fact; PENDING_VERIFICATION = needed fact missing; BLOCKED = unavailable required evidence or unsupported target prevents use; NOT_APPLICABLE = excluded from this experiment. All adoption states below are PROPOSED/BLOCKED; none APPROVED. DEV-17 governs clearance and REL standards govern distribution.

| Name / candidate version / purpose | Official source evidence | License / redistribution obligations investigated | Windows and runtime prerequisites | Security / outstanding verification | Documentation state / adoption |
| --- | --- | --- | --- | --- | --- |
| .NET SDK 10.0.401; build tools | dotnet release JSON in source register | Runtime source MIT is verified, but SDK includes additional tools/licenses; inventory exact SDK distribution notices | Supported build host and x64 target; WPF native execution Windows only | Official installer/archive provenance, checksum/signature, SDK third-party inventory, advisories and chosen build-host support | VERIFIED_DOCUMENTATION release; PENDING_VERIFICATION distribution / PROPOSED |
| .NET runtime + WindowsDesktop/WPF 10.0.12; shell/worker | Release JSON; pinned runtime and WPF licenses; OS table | MIT copyright/permission preservation; shipped runtime packs include third-party notices requiring inventory | Exact supported Windows edition/build/lifecycle; no mandatory WebView | Self-contained native assets, runtime signatures/hash, OS patch/accessibility/offline proof | VERIFIED_DOCUMENTATION versions/headline licenses; target PENDING_VERIFICATION / BLOCKED pending B02/B04 |
| Microsoft.Data.Sqlite/Core 10.0.12; local provider, no EF ORM | Pinned efcore projects/license/version/central pins | MIT; preserve notices; separate native/transitive licenses | net10 worker/application; SQLite native win-x64 loading must be proven | Bound SQL/transactions; verify published package metadata/signature/advisories and closure vs source project | VERIFIED_DOCUMENTATION source pins/license; binary PENDING_VERIFICATION / PROPOSED |
| SQLitePCLRaw.bundle_e_sqlite3/core/provider.e_sqlite3/lib.e_sqlite3 2.1.12; wrapper/native binding | efcore central pin and pinned bundle/core/native/fragment sources | Apache-2.0 wrapper/native package declaration; license and applicable NOTICE/modification notices, patent conditions; native embedded SQLite separately reviewed | Native nuspec declares win-x64 DLL asset built with v143; asset existence is not proof of target support or VC runtime prerequisites | Verify each published package, exact native engine/version/build/options, signature/hash, architecture, native prerequisites, advisories; source ranges may resolve other versions | VERIFIED_DOCUMENTATION source chain/headline license; closure PENDING_VERIFICATION / BLOCKED |
| System.Memory source dependency lower bound 4.5.3, actual resolved version UNALLOCATED | SQLitePCLRaw.core pinned project | License and actual selected package obligations not verified; do not pin an old minimum merely because source requests it | Framework-specific resolution may omit/unify or select a different maintained version | Resolve complete package graph from official metadata before installs; inspect advisories and any System.Buffers/Unsafe/framework assets | PENDING_VERIFICATION / BLOCKED until closure |
| Native SQLite engine exact version/build UNALLOCATED; embedded DB | Native package nuspec + historical P3 SQLite source evidence | Primary SQLite public-domain statement is historical; native package Apache wrapper declaration is not proof all bundled source/assets have same license | Exact win-x64 binary/build flags/CRT dependency unknown | Engine source provenance, release patch/security state and native notices missing; query SQLite runtime version only in later authorized experiment | PENDING_VERIFICATION / BLOCKED B04 |
| CPython 3.13.16; alternative runtime | Exact tag version/Windows/license sources | PSF2 and historical/third-party terms, retain notices and modification summaries as applicable | Windows lifecycle/architecture and binary availability verified only in later clearance | Installer/bundled SQLite/OpenSSL/native notices and advisories missing | VERIFIED_DOCUMENTATION source/version; distribution PENDING_VERIFICATION / NOT SELECTED |
| PySide6 6.12.0 and its exact metadata companions; alternative UI | Official PyPI metadata and historical Qt evidence | LGPL/GPL license options in metadata; actual selected modules, relinking/source/install information obligations require license review; commercial license not assumed | Python >=3.10,<3.16 metadata; exact Qt build/Windows lifecycle/wheel prerequisites missing | qt.io support retrieval blocked; version-tag license path absent; complete module graph/unneeded web components unresolved | PENDING_VERIFICATION, required Qt support BLOCKED / NOT SELECTED |
| PyInstaller 6.22.3; alternative packager | Official metadata and pinned COPYING | GPL-2.0-or-later with bootloader exception; hooks/utilities additional Apache/MIT conditions, preserve notices; exception not all dependency clearance | Python >=3.8,<3.16; native Windows build needed | Windows dependencies pefile/pywin32-ctypes/hooks/altgraph/setuptools/etc exact closure and binary provenance pending | VERIFIED_DOCUMENTATION headline terms; closure PENDING_VERIFICATION / NOT SELECTED |
| Electron 44.7.0; alternative desktop runtime | npm metadata; pinned README/license/DEPS | MIT plus Chromium/Node/third-party binary notices and assets | Windows10+ x64/arm64 statement; precise build/support/security unknown; npm Node >=22.12.0 development minimum | Exact Node development pin, embedded engine advisories, signatures/hash, npm closure, sandbox/offline behavior pending | VERIFIED_DOCUMENTATION narrow OS/license claim; closure PENDING_VERIFICATION / NOT SELECTED |
| Browser automation, PDF/XLSX/OCR libraries, installer framework, WebView2 | Historical P3 only | No new clearance attempted or inferred | Not required for synthetic CSV portable slice | Remain future lanes; adding any changes experiment tuple/scope | NOT_APPLICABLE to EXP-N1 / NOT ADOPTED |

The source-tested dependency chain is not a resolved SBOM. B04 remains OPEN because binary/native engine provenance, a maintained exact dependency closure, full notices and current advisories are missing. Source URLs/hashes below allow future reproduction even though fetched text stays outside the repository. Do not install to discover the graph under this authorization. A future documentary review may use official package metadata; an actual restore/install requires separately scoped approval after applicable clearance.

## Windows information collection guide
Run only on the target laptop in built-in **Windows PowerShell**, without elevation. These commands read selected properties and do not install, launch browsers, change registry/policy or contact a remote target. They have NOT_RUN here; syntax/platform execution remains unverified. Optional queries can be unavailable or denied: record UNKNOWN with the error category, do not bypass restrictions. Review output before sharing; omit computer/account names, product keys, serials, tokens, file paths and client data. Avoid systeminfo full dumps, Get-ComputerInfo full dumps, licensing detail commands and Win32_Product (which can trigger repairs).

First collect OS/hardware/storage:

```powershell
$fasOs = Get-CimInstance Win32_OperatingSystem
$fasSystem = Get-CimInstance Win32_ComputerSystem
$fasVersion = Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion'
[pscustomobject]@{
  WindowsEdition = $fasOs.Caption
  EditionID = $fasVersion.EditionID
  DisplayVersion = $fasVersion.DisplayVersion
  ReleaseId = $fasVersion.ReleaseId
  Build = $fasOs.BuildNumber
  UpdateBuildRevision = $fasVersion.UBR
  OSArchitecture = $fasOs.OSArchitecture
  SystemType = $fasSystem.SystemType
  InstalledRAMGiB = [math]::Round($fasSystem.TotalPhysicalMemory / 1GB, 2)
  AvailableRAMGiB = [math]::Round($fasOs.FreePhysicalMemory * 1KB / 1GB, 2)
} | Format-List
Get-CimInstance Win32_Processor | Select-Object Name, Architecture, NumberOfCores, NumberOfLogicalProcessors
Get-CimInstance Win32_LogicalDisk -Filter 'DriveType=3' |
  Select-Object DeviceID, FileSystem,
    @{Name='SizeGiB';Expression={[math]::Round($_.Size / 1GB,2)}},
    @{Name='FreeGiB';Expression={[math]::Round($_.FreeSpace / 1GB,2)}}
```

Then inspect runtime/WebView registrations without running installed programs:

```powershell
$fasInstalledKeys = @(
  'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*',
  'HKLM:\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*',
  'HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*'
)
Get-ItemProperty $fasInstalledKeys -ErrorAction SilentlyContinue |
  Where-Object { $_.DisplayName -match 'Microsoft .NET|Microsoft Windows Desktop Runtime|Microsoft ASP.NET|WebView2|Python|Node.js|Visual C\+\+' } |
  Select-Object DisplayName, DisplayVersion | Sort-Object DisplayName, DisplayVersion -Unique
$fasEdgeKeys = @(
  'HKLM:\SOFTWARE\Microsoft\EdgeUpdate\Clients\*',
  'HKLM:\SOFTWARE\WOW6432Node\Microsoft\EdgeUpdate\Clients\*',
  'HKCU:\SOFTWARE\Microsoft\EdgeUpdate\Clients\*'
)
Get-ItemProperty $fasEdgeKeys -ErrorAction SilentlyContinue |
  Where-Object { $_.name -match 'WebView2' } | Select-Object name, pv
```

Registration is a clue, not proof that a runtime works; portable/nonregistered runtimes can be missed. For browser versions inspect only known executables, never user profiles:

```powershell
$fasBrowserCandidates = @(
  @{Browser='Edge';Path="${env:ProgramFiles(x86)}\Microsoft\Edge\Application\msedge.exe"},
  @{Browser='Edge';Path="$env:ProgramFiles\Microsoft\Edge\Application\msedge.exe"},
  @{Browser='Chrome';Path="$env:ProgramFiles\Google\Chrome\Application\chrome.exe"},
  @{Browser='Chrome';Path="${env:ProgramFiles(x86)}\Google\Chrome\Application\chrome.exe"},
  @{Browser='Chrome';Path="$env:LOCALAPPDATA\Google\Chrome\Application\chrome.exe"},
  @{Browser='Firefox';Path="$env:ProgramFiles\Mozilla Firefox\firefox.exe"},
  @{Browser='Firefox';Path="${env:ProgramFiles(x86)}\Mozilla Firefox\firefox.exe"}
)
foreach ($fasBrowser in $fasBrowserCandidates) {
  if (Test-Path -LiteralPath $fasBrowser.Path -PathType Leaf) {
    [pscustomobject]@{ Browser=$fasBrowser.Browser; Version=(Get-Item -LiteralPath $fasBrowser.Path).VersionInfo.ProductVersion }
  }
}
Get-ExecutionPolicy -List
Get-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem' -Name LongPathsEnabled -ErrorAction SilentlyContinue |
  Select-Object LongPathsEnabled
if (Get-Command Get-MpComputerStatus -ErrorAction SilentlyContinue) {
  Get-MpComputerStatus | Select-Object AntivirusEnabled, RealTimeProtectionEnabled
}
```

If portable/custom browsers are missed, manually provide only version from About. Manually add: LTSC/IoT/ESU status if known (no licensing keys); whether you may install/run ordinary-user signed executables, create a disposable local folder and run a reviewed PoC; antivirus/AppLocker/WDAC restrictions; permitted offline observation method; display scale/accessibility tools if relevant. Do not disable antivirus, alter policy, grant admin access or purchase anything. ESU status is not safely established by the queries above and must remain UNKNOWN unless owner supplies appropriate nonsecret evidence.

| Collected property | Decision it informs |
| --- | --- |
| Exact edition/version/build/revision, LTSC/IoT/ESU lifecycle | Compare vendor OS support; stop unsupported tuple. Windows10 standard Home/Pro support ended 2025-10-14 per owner-supplied Microsoft lifecycle reference; direct page retrieval unavailable here. ESU does not automatically establish .NET/Qt/browser support |
| OS architecture/system type/CPU model/core count | win-x64 vs alternative architecture/native assets; instruction/runtime suitability and conservative worker count; proposal changes require review |
| Installed/available RAM and local drive space/filesystem | Build/portable/temp/backup headroom, workload bounds and on-volume finalization; no measured throughput inferred |
| Existing .NET/Python/VC registrations | Determine permitted setup scope and native prerequisites; installed software is neither support proof nor authorization to use it |
| Browser/WebView version | Later website QA/alternative-shell dependency assessment; EXP-N1 shell does not need a browser |
| Execution/install restrictions, protection and long-path policy | Native access route, safe folder/path tests, permissions/installer feasibility; never bypass policy |
| Offline observation permission and display/assistive tools | Native offline/startup and bounded accessibility proof method; no automatic setting changes |

Native route recommendation: owner-run reviewed bounded source/package on laptop, with sanitized run manifest/evidence returned; no remote laptop-access agent needed. Linux cloud may later build/run the core lane on a supported host after approved installation, but cannot execute WPF/native Windows packaging tests. Owner command execution permission is a separate decision from reading the laptop facts. Full P5 acceptance requires genuine native evidence, not screenshots of cloud results.

## Bounded experiment approval proposal — NOT EXECUTED
Proposal identifier EXP-N1 is local; it does not allocate or approve a TEST/REQ/ADR. Targets [P3 contracts](P3-module-contracts.md), [worker protocol](P3-job-worker-protocol.md), [persistence/artifacts](P3-persistence-artifacts.md), [recovery/approval](P3-recovery-approval.md) and [reporting](P3-reporting-packaging.md). Existing [P5 experiment matrix](../test-matrix/P5-planned-experiments.md) owns procedure-to-requirement/test references.

**Entrance gates:** supported sanitized laptop tuple and authorized native execution route; complete exact dependency/native engine/packaging notice/provenance/advisory evidence; explicit owner approval naming this final tuple, temporary-source scope, dependency installations and run commands. P0–P4 checkpoint remains satisfied. The tuple above is not yet fully resolvable, so this is a reviewable proposal, not an execution-ready install script. Any absent mandatory gate keeps P5 BLOCKED.

**Scope:** one minimal native screen (select synthetic fixture, start, progress, cancel, truthful result/recovery and explicit test approval/export controls), one trusted child CSV worker via inherited framed pipes, one application SQLite writer, one owned disposable local workspace and portable multi-file self-contained win-x64 publish. This is an isolated prototype, no production desktop foundation. Test an explicitly supported tiny UTF-8 comma-separated table profile; reject unsupported quoting/encoding/formula-like cells in this slice rather than promise general CSV/Excel support. Transformation is deterministic exact duplicate handling with explicit configured key; independent expected row table, no uncertain deletion. No client records, browsers, live targets, Office/PDF/OCR or imported code.

**Likely future source files (not created):** proofs/P5/native-slice/README.md, global.json (pin SDK), NuGet.Config (approved source mapping), DependencyEvidence.md, NativeSlice.sln; Contracts/Contracts.csproj and message schema types; Core/Core.csproj and job/artifact/recovery guards; Desktop/Desktop.csproj, App.xaml, MainWindow.xaml and shell code; Worker/Worker.csproj and entry; Harness/Harness.csproj and deterministic checks/fixture generator; project lockfiles and approved notices. This proposed proofs directory is a bounded P4-layout exception requiring approval, not an unannounced production-layout change. No production migration or implementation directories created now. The harness will use core assertions returning nonzero on failures, avoiding a new test-runner dependency for this limited slice.

**Dependencies to install later:** SDK 10.0.401 on approved build host; exact Microsoft.Data.Sqlite/Core 10.0.12 and SQLitePCLRaw closure after clearance; SDK runtime/WindowsDesktop reference/runtime packs 10.0.12 for self-contained publish. No EF Core ORM, CsvHelper, Node, Python, WebView/browser, package manager other than SDK/NuGet, installer framework or Windows system-setting change. Exact native SQLite engine and any extra resolved package version are TBD/BLOCKED, not implicit permission for unlisted dependencies. Owner need not choose these technical patch details: architect resolves documentary evidence first, then submits a complete tuple.

**Proposed commands only:** execute from proofs/P5/native-slice after approved source exists, vetted dependency graph and optional installation are separately authorized. Pin SDK with rollForward disabled and telemetry/first-use policy documented. Acquire SDK only from official release metadata URL; verify checksum/signature before running any reviewed installer, never pipe downloaded scripts into a shell. No installer command supplied before correct architecture and installation permission are known. A first restore creates reviewed lockfiles only under separately approved installation scope; later repeat restores use locked mode. A graph change stops the run.

```text
dotnet --version
dotnet restore NativeSlice.sln --configfile NuGet.Config -p:RestorePackagesWithLockFile=true
dotnet list NativeSlice.sln package --include-transitive
dotnet build NativeSlice.sln -c Release --no-restore
dotnet run --project Harness/Harness.csproj -c Release --no-build -- core
dotnet run --project Desktop/Desktop.csproj -c Release --no-build
dotnet publish Desktop/Desktop.csproj -c Release -r win-x64 --self-contained true -p:RuntimeFrameworkVersion=10.0.12 -p:PublishSingleFile=false -p:PublishTrimmed=false -o <owned-output>/desktop
dotnet publish Worker/Worker.csproj -c Release -r win-x64 --self-contained true -p:RuntimeFrameworkVersion=10.0.12 -p:PublishSingleFile=false -p:PublishTrimmed=false -o <owned-output>/worker
```

The harness CLI/project layout are specifications, not existing commands verified to work. Runtime-pack restore for publish needs an approved locked RID-specific dependency inventory; no silent download. Stage desktop/worker outputs with fixed trusted paths under one owned portable package, manifest/checksums/notices; target run command is the reviewed package NativeSlice.exe. Repeated build/run/publish after acquisition must use local cached approved dependencies with networking unavailable and --no-restore where applicable. Linux core-only build/run uses Core/Worker/Harness projects (exclude WPF), linux-x64 RID/runtime pack and host-support confirmation; it cannot stand in for the native lane or expand permission automatically.

**Network:** future dependency acquisition only official documented .NET distribution destinations and approved NuGet package endpoints; record exact hosts from release metadata/approved package source mapping before approval, TLS/signature/hash verification retained. No network requests during jobs. No client files, telemetry, AI, backend or external delivery. Future offline observation/disconnection on laptop requires owner permission; do not change firewall/settings in this task. Optional vulnerability metadata access is distinct from runtime egress and must be recorded, not a hidden fallback.

**Precautions and bounds (PROPOSED, not measured):** ordinary user, one owned worker, one job, one heavy suite at a time, <=1 MiB input/message, <=10,000 rows/20 columns, <=10 MiB generated data per run, 60-second run deadline, cancellation target <=5 seconds then bounded supervisor action against owned process only. Suggested initial headroom 8 GiB installed RAM and 5 GiB free storage for SDK/build/native-package evidence; these are conservative planning estimates, not minimum product requirements or download-size claims. Recheck vendor installation space and actual target available resources. Stop rather than exhaust memory/disk. Keep process isolation and actual sandboxing distinct: this synthetic experiment does not clear hostile-file confinement risk.

**Fixtures:** generated synthetic rows with literal ASCII/UTF-8 text; nominal, empty, one row, missing/duplicate header, duplicate key, malformed/oversized input. Hand-reviewed expected row counts/values separate from transform implementation. Test approval label is synthetic, not identity authentication. Disposable corrupt DB/artifact cases and worker crash/restart injection operate only on run-owned files/processes. No real client data/credentials. Large/hostile document fixtures and live-network tests excluded.

**Expected outputs:** local evidence manifest with runId/attempt/correlation/schema/toolchain/OS/architecture, source and fixture hashes, exact resolved dependency list/notices, commands/exit codes/timestamps/assertion counts, worker events, input/output row reconciliation/hash, SQLite integrity/FK/backup evidence, each fault-boundary reconciliation, approval invalidation/export manifest, UI observation, idle/peak memory/CPU/elapsed/cancel measurements and packaged offline native run evidence. Evidence is retained outside source under an owner-approved folder; never commit generated client-like artifacts automatically.

| Objective | Success evidence | Failure / stop criterion |
| --- | --- | --- |
| Desktop startup | Native ordinary-user shell opens on exact supported laptop; readable/focusable controls and truthful progress | Unsupported OS/runtime, crash, blocked execution, frozen UI or unavailable native route |
| Local worker IPC | Versioned bounded/correlated events; wrong version/stale attempt rejected | Accepted malformed message, unrestricted launch or missing termination evidence |
| Synthetic CSV | Independent expected values/counts, preserved input hash, unsupported profiles rejected | Silent loss, mutation, unsupported input accepted or uncertain automatic deletion |
| Local persistence | Single-writer FK/transaction/history invariants and integrity output | Lost/contradictory attempt/artifact/approval record or silent blank DB recovery |
| Artifact integrity | Stage/hash/intent/finalization readback plus tamper denial | Partial output eligible, stale hash accepted or DB/files assumed one atomic transaction |
| Progress/cancellation | Native progress and owned-worker stop, measured latency, cancelled not success | Unbounded wait, unrelated process termination or false complete state |
| Failure/recovery | Deliberate owned-worker termination and crash-boundary restart evidence, prior failures retained | Duplicate effects, original overwrite, missing evidence or stale approval inherited |
| Offline | Packaged local job completes with network unavailable; approved observer finds no unexpected egress | Missing runtime downloads/login/network fallback or unobserved offline condition |
| Resources | Actual representative tiny-run measurements with hardware and limits; proposed budgets assessed honestly | Resource bound exceeded or measurements absent; do not invent benchmark |
| Packaging feasibility | Portable multi-file package contains worker/native runtime/assets/notices, launches without SDK/network | Native library missing, wrong arch, unreviewed dependency/notice or SDK required |

Portable feasibility does not prove installer/upgrade/uninstall readiness. Installer tooling, all four module formats/browser support and full accessibility/security/scale/release tests remain future scoped lanes. Passing this slice alone cannot complete P5 or mark any of the 239 broader product cases PASSED.

**Rollback/recovery plan:** stop only owned verified processes, preserve local failure evidence and input hashes, quarantine inconsistent run outputs, restore only synthetic DB into a new owned folder. Review an ownership manifest before removing disposable generated files; no blanket recursive deletion. SDK uninstall or changes to shared caches require separate review because other software may use them. No repository reset/clean, client directory modification or external delivery. Source stays reviewable and uncommitted unless later explicitly authorized.

## Open decisions and evidence gates
Keys below are local P5 decisions, not new ADR/REQ identifiers. All remain OPEN; no one is asked to approve an unsupported production architecture.

| Key / blocker | Options / recommendation | Supporting evidence | Risk / consequence | Approval and next verification |
| --- | --- | --- | --- | --- |
| P5-D01 / B01 | Approve completed bounded EXP-N1 tuple after gates; defer; investigate supported alternative. Recommend conditional EXP-N1 investigation only now | Existing ADR-0002 preference and pinned .NET metadata/license research | Unknown target/native closure can disqualify; no final language adoption | Owner explicitly approves final tuple/source/install/run scope only AFTER D02/D04 facts; architect fills closure first |
| P5-D02 / B02 | Return sanitized read-only laptop facts; remain blocked. Recommend collection guide above | Cloud only accesses Linux, no target facts | Wrong edition/lifecycle/architecture makes current candidate unsuitable | Owner supplies selected facts and permitted restrictions; architect compares current vendor support, no Windows proof yet |
| P5-D03 / B02 | Owner-run reviewed native package; existing authorized Windows runner; defer. Recommend owner-run, no remote agent | No attached native environment; ordinary-user bounded run proposal | AV/policy/resource limits may prevent experiment; Linux cannot clear gate | Owner authorizes actual execution method separately; record exact native run evidence later |
| P5-D04 / B04 | Resolve published exact closure/native engine/notices/advisories; exclude affected dependency if evidence fails; defer. Recommend technical documentary verification first | Source graph and headline licenses fetched, binary graph and engine unverified | Supply-chain/license/support exposure; no silent obsolete pin or legal conclusion | Technical lead completes records, owner reviews adoption/experimental distribution terms; native assets tested only after execution approval |

Exactly one next recommended action: **run the read-only Windows collection guide on the target laptop and return sanitized results**. Current next prompt is a documentation-only target/evidence review gated on those facts; it must not start experiments. This avoids asking for executable approval of an unsupported/incomplete tuple.

## Documentary review and limits
PASS criteria for this package: alternatives compared, one bounded recommendation explicitly conditional, known exact pins cited, unresolved transitive/native versions openly blocked, laptop commands and decision dependencies documented, all ten experiment objectives/commands/fixtures/success/failure/rollback/resources/native separation described, requirement/test links preserved, risks/ADRs/statuses unchanged and authorized files only edited. Exact full dependency tuple/Windows/license clearance remain BLOCKED, not a forced documentary PASS. PowerShell, future restore/build/run/publish, product/PoC/native/offline/benchmark/security/accessibility/installer tests remain NOT_RUN. Mermaid rendering is not required by this task. Link/heading/identifier/scope check results are recorded in [MS-0006](../milestone-reports/MS-0006-P5.md).

## Official source snapshot register
Retrieved 2026-10-11 UTC. Moving branches/registry JSON are time-specific observations; pinned tags are identified in URLs. A tag/source fetch confirms text availability, not release signature or package provenance. Unavailable paths remain recorded, including successful later corrections; missing source does not imply the license does not exist. All fetched bytes retained only in /tmp during this task; hashes below and extracted facts above are durable evidence. Publisher endpoints may later change; repeat collection before adoption.

| Source key | URL | Retrieval result | SHA-256 of fetched text or access error |
| --- | --- | --- | --- |
| dotnet | https://raw.githubusercontent.com/dotnet/core/main/release-notes/10.0/releases.json | FETCHED | 449f2b4c8efe3079cada3c39226569122a77e423168b0503644140a4a61cc57d |
| os | https://raw.githubusercontent.com/dotnet/core/main/release-notes/10.0/supported-os.md | FETCHED | 168f8bf76fdcaad9a1083ce5a96329291c17ef4c51e850b99c83f6e0457963f7 |
| python | https://raw.githubusercontent.com/python/cpython/3.13/Include/patchlevel.h | FETCHED | bdb46c7a878ce946942b0cad519fe1249f232e8544572bddf2aa5134846cd7c8 |
| qt | https://raw.githubusercontent.com/qt/qtbase/dev/.cmake.conf | FETCHED | 18db6c76345c05117287531b4764957d18c4bceb9a6ac0808952b23b4570b02c |
| electron | https://raw.githubusercontent.com/electron/electron/main/package.json | FETCHED | 4cd849c601402f2d5fa787ce90e74945b2371912961b3e9303b6161860092641 |
| netlicense | https://raw.githubusercontent.com/dotnet/runtime/main/LICENSE.TXT | FETCHED | cfc21f5e8bd655ae997eec916138b707b1d290b83272c02a95c9f821b8c87310 |
| eflicense | https://raw.githubusercontent.com/dotnet/efcore/main/LICENSE.txt | FETCHED | ae48df11a335dc1a615f4f938b69cba73bcf4485c4f97af49b38efb0f216353b |
| efversion | https://raw.githubusercontent.com/dotnet/efcore/release/10.0/eng/Versions.props | FETCHED | ec64d71887ce7ac977923cb69e0a0f7d8e71b9319a9cbac29d2e8b05cf8322f2 |
| ef-tag | https://raw.githubusercontent.com/dotnet/efcore/v10.0.12/src/Microsoft.Data.Sqlite/Microsoft.Data.Sqlite.csproj | FETCHED | 00448ec2082b4c14414f0ceb565f7b6f529142afb58968279e6969c50869fa8b |
| ef-core | https://raw.githubusercontent.com/dotnet/efcore/v10.0.12/src/Microsoft.Data.Sqlite.Core/Microsoft.Data.Sqlite.Core.csproj | FETCHED | b58e8f7587a04c49ae53754041763dc05dbf152f9e93686add6de6866482edef |
| ef-pins | https://raw.githubusercontent.com/dotnet/efcore/v10.0.12/eng/Versions.props | FETCHED | a31b3e681cac5f1537ef29e7b81976b4f61533affd7c5857de3d19f469be7c6e |
| wpf-license | https://raw.githubusercontent.com/dotnet/wpf/v10.0.12/LICENSE.TXT | FETCHED | ae48df11a335dc1a615f4f938b69cba73bcf4485c4f97af49b38efb0f216353b |
| net-pinned-license | https://raw.githubusercontent.com/dotnet/runtime/v10.0.12/LICENSE.TXT | FETCHED | cfc21f5e8bd655ae997eec916138b707b1d290b83272c02a95c9f821b8c87310 |
| sqlite-license | https://raw.githubusercontent.com/ericsink/SQLitePCL.raw/v2.1.13/LICENSE.TXT | UNAVAILABLE | HTTP Error 404: Not Found |
| pyside | https://pypi.org/pypi/PySide6/json | FETCHED | 77f1014e142d19f00bcb3776897bfc94ba915c39e5b0ad69bd5384a95a2d35be |
| pyinstaller | https://pypi.org/pypi/pyinstaller/json | FETCHED | d89a305e68655755bd5428eb5d73533c114c0999abfa02712948b46f840f517c |
| electron-release | https://registry.npmjs.org/electron/latest | FETCHED | 93adc88948184477a81b352dfd9ab08e04cda88fb27652f83b3962b30fee4aec |
| python-tag | https://raw.githubusercontent.com/python/cpython/v3.13.16/Doc/using/windows.rst | FETCHED | 9e2a25eec1bbcf5a0ca2a36fe727136be2a90aefd8a7fab7126eb75781e4b4a9 |
| lifecycle | https://learn.microsoft.com/en-us/lifecycle/products/windows-10-home-and-pro | UNAVAILABLE | <urlopen error Tunnel connection failed: 403 Forbidden> |
| ef-packages | https://raw.githubusercontent.com/dotnet/efcore/v10.0.12/Directory.Packages.props | FETCHED | b4c7f55e2beafe9592c7e728c2948bbfe1e263f109edfbf7f6cb080ae522b4d7 |
| ef-license-pinned | https://raw.githubusercontent.com/dotnet/efcore/v10.0.12/LICENSE.txt | FETCHED | ae48df11a335dc1a615f4f938b69cba73bcf4485c4f97af49b38efb0f216353b |
| sqlitepcl | https://raw.githubusercontent.com/ericsink/SQLitePCL.raw/v2.1.12/LICENSE | UNAVAILABLE | HTTP Error 404: Not Found |
| sqlite-bundle | https://raw.githubusercontent.com/ericsink/SQLitePCL.raw/v2.1.12/src/SQLitePCLRaw.bundle_e_sqlite3/SQLitePCLRaw.bundle_e_sqlite3.csproj | FETCHED | 11ebe6c7a49146048ad3d1d7be21efceefd0098bf1db5bf793e33e25f6aabd6b |
| sqlite-native | https://raw.githubusercontent.com/ericsink/SQLitePCL.raw/v2.1.12/src/SQLitePCLRaw.lib.e_sqlite3/SQLitePCLRaw.lib.e_sqlite3.csproj | FETCHED | 12a00992e4ecef2f3142dc4604c3b74e5582448c4de196b8830b88122fd1428d |
| python-license | https://raw.githubusercontent.com/python/cpython/v3.13.16/LICENSE | FETCHED | 78b12c3a81360b357002334f0e70ea0e92eebf7a9b358805c03c48484945f3bb |
| qt-platform | https://doc.qt.io/qt-6/supported-platforms.html | UNAVAILABLE | <urlopen error Tunnel connection failed: 403 Forbidden> |
| pyside-license | https://raw.githubusercontent.com/qt/pyside-setup/v6.12.0/LICENSES/LGPL-3.0-only.txt | UNAVAILABLE | HTTP Error 404: Not Found |
| electron-license | https://raw.githubusercontent.com/electron/electron/v44.7.0/LICENSE | FETCHED | 5154e165bd6c2cc0cfbcd8916498c7abab0497923bafcd5cb07673fe8480087d |
| electron-support | https://raw.githubusercontent.com/electron/electron/v44.7.0/docs/tutorial/support.md | FETCHED | 717946b6e7055a2fce56fa00f777ff889ff9fce556b2c4d8f45b8daebd21bfe4 |
| sqlite-public | https://sqlite.org/copyright.html | UNAVAILABLE | <urlopen error Tunnel connection failed: 403 Forbidden> |
| sqlitepcl-license | https://raw.githubusercontent.com/ericsink/SQLitePCL.raw/v2.1.12/LICENSE.TXT | FETCHED | cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30 |
| sqlitepcl-pins | https://raw.githubusercontent.com/ericsink/SQLitePCL.raw/v2.1.12/Directory.Build.props | FETCHED | c07cf23d964042afed343427295934236d643dbdac54d46bb9e26c16a910f4c8 |
| sqlite-fragment | https://raw.githubusercontent.com/ericsink/SQLitePCL.raw/v2.1.12/src/msbuild_bundle_fragments/e_sqlite3_dllimport.xml | FETCHED | 0d01a86dde986a9012135a1385c0b27985435b0de77516bdb76eb3f2b2709a9b |
| electron-readme | https://raw.githubusercontent.com/electron/electron/v44.7.0/README.md | FETCHED | cb788749d3f0d3991e9c17b0cbcd9fd15a8c9bd73e45874d0a936fdbd9d3745b |
| electron-deps | https://raw.githubusercontent.com/electron/electron/v44.7.0/DEPS | FETCHED | 46608960fb52f7120de7d531e9b243f16e03ced0febf85b095a2d49264c6d846 |
| python-version | https://raw.githubusercontent.com/python/cpython/v3.13.16/Include/patchlevel.h | FETCHED | fe193cc6d1c016cf6baaf60c4e7d26a4fdb8eb85d5d4e9c883de5b2808cea4ca |
| pyinstaller-license | https://raw.githubusercontent.com/pyinstaller/pyinstaller/v6.22.3/COPYING.txt | FETCHED | 0598064c7d2718e38d7914a7d08343b2fa008e3bea9ebba2aa7a6ffa5900dd64 |
| sqlite-core | https://raw.githubusercontent.com/ericsink/SQLitePCL.raw/v2.1.12/src/SQLitePCLRaw.core/SQLitePCLRaw.core.csproj | FETCHED | ece27f493840294255c04d03f6b17e87b516e06ca190bfef211049651ede4d70 |
| sqlite-nuspec | https://raw.githubusercontent.com/ericsink/SQLitePCL.raw/v2.1.12/src/SQLitePCLRaw.lib.e_sqlite3/SQLitePCLRaw.lib.e_sqlite3.nuspec | FETCHED | 8a1a5c76dae4f148d66193d609a9af4c06855450fe204b81dc4d5414211641a3 |

Electron 44.7.0 pinned DEPS `chromium_version`: `152.0.7977.130`. This embedded source revision/version is not a separately approved installed Node/browser or advisory clearance.

Electron 44.7.0 pinned DEPS `node_version`: `v24.21.0`. This embedded source revision/version is not a separately approved installed Node/browser or advisory clearance.

## Target-informed review and current recommendation — 2026-10-11 Asia/Kolkata
Authorization: owner “do tht” accepts the offered supported-stack/dependency documentation review. No installation, package download, prototype, native experiment, ADR approval or Git mutation authorized. Only the six named P5 documentation paths updated. Prior proposals/source records retained as history.

### Sanitized owner-reported target facts
| Property | Evidence and disposition |
| --- | --- |
| OS | Owner PowerShell output: Windows10 Home Single Language, 10.0.19045/build19045, 64-bit; this maps to 22H2. Exact update revision still unknown, not needed to identify this vendor-support mismatch |
| Hardware | Intel Core i3-6006U 2.00GHz; 3.87GiB usable memory as reported; C: 61.81GiB free at collection. This is an owner-reported snapshot, not a cloud hardware observation |
| .NET | dotnet command not found on PATH; this does not prove no private/runtime-only installation exists |
| Browser | Owner identifies Chrome154.0.8037.98, 64-bit |
| WebView2 | Corrected multi-location registry query returned Microsoft Edge WebView2 Runtime154.0.4258.62; registration, not runtime proof |
| OS maintenance | Owner quotes Windows Update: device no longer receiving security updates, “Enrol now”. Evidence indicates ESU not enrolled; enrollment/OS maintenance not changed or purchased |
| Permissions | Personal laptop; owner states control and ability to install software. Installation restriction question answered; specific PoC execution/download authorization is still separate |

The unrelated Toolzenhub Git transcript is not copied into project evidence and is not this project's checkpoint. Native laptop information has now been supplied: do not ask the owner to repeat these facts. B02 fact-collection portion is satisfied; approved native-run route/support proof remains pending.

### Support comparison and corrected Python interpretation
- .NET10 official refreshed supported-OS table omits this Windows10 Home22H2 target and says OS versions out of publisher support are not tested/supported. EXP-N1 is not selected for this laptop. Do not assume ESU enrollment alone adds .NET vendor support, nor silently select an old .NET release.
- Python PEP11 states that bugfix releases retain the OS versions supported by the original feature release even after Microsoft support ends. PEP745 records Python3.14.0 released 2025-10-07, before the stated Windows10 Home/Pro EOS2025-10-14, and Python3.14.8 on 2026-10-01. Pinned 3.14.8 Windows documentation says Windows10 and newer. Together these establish documentary support for the runtime family on this OS, not native proof or continued Windows security updates. Earlier blanket Python lifecycle concern is refined by this more precise policy, not silently carried forward as disqualification.
- Qt6.12.0's pinned supported-platform include lists Windows10 1809 or later, x86_64; owner22H2 fits. The same table says Qt6.12 will be the last Qt version supporting Windows10. Future upgrades cannot be assumed compatible. Binary package/native prerequisites and individual module licenses must still be checked.
- Official PyPI metadata for PySide6-Essentials6.12.0 lists only shiboken6==6.12.0 as its package dependency and supplies cp310-abi3 win_amd64 artifacts. Both require Python>=3.10,<3.16, consistent with3.14.8. Use QtCore/QtGui/QtWidgets only; do not install the PySide6 meta-package/Addons/WebEngine/Pdf. This reduces dependency breadth, not a measured memory guarantee.
- Electron44.7.0's pinned README states Windows10+ x64/arm64. It remains a plausible documented alternative but adds Chromium/Node/security/update/packaging surface; not preferred for the current roughly4GiB vertical slice. Browser/website-QA support remains a separate future question; installed Chrome/WebView do not prove automation authorization or compatibility.

**Current ONE recommended candidate: EXP-Q1 — CPython3.14.8 x64 + PySide6-Essentials6.12.0/shiboken6 6.12.0, standard-library sqlite3/CSV/JSON/pipes/hash/ZIP, packaged experimentally with PyInstaller6.22.3.** This supersedes the .NET recommendation for the supplied laptop only; ADR-0002 remains PROPOSED and is not rewritten/adopted. It is a conditional experimental recommendation, not proven product compatibility, native sandboxing, performance, accessibility or release readiness. No unsupported runtime workaround or production technology decision made.

### Exact proposed installation inventory — NOT authorized or executed
| Item | Proposed pin | Role / evidence / remaining obligation |
| --- | --- | --- |
| CPython Windows x64 | 3.14.8 | Full ordinary CPython build, not free-threaded or embeddable-only; release page/index inaccessible so official installer URL/signature/hash/distribution notices need confirmation before acquisition. No Visual Studio compiler needed if selected verified wheels work |
| Bundled pip | 26.2.1 | Exact ensurepip source pin; actual installer contents and vendored notices still to verify; no automatic upgrade |
| PySide6-Essentials | 6.12.0 | Qt widgets/runtime; official x64 wheel metadata and LGPL/GPL options. Propose LGPL3 compliance basis subject to module/distribution review; retain notices, supply corresponding library source and appropriate relinking/replacement/installation information. No commercial subscription proposed |
| shiboken6 | 6.12.0 | Required binding runtime; x64 wheel metadata, no Requires-Dist dependencies; exact binding/native notices and license scope pending |
| PyInstaller | 6.22.3 | Windows build tool; GPL2-or-later bootloader exception verified in COPYING; runtime hooks carry additional Apache terms. Build on Windows, not cross-freeze from Linux |
| altgraph | 0.17.5 | Build dependency; metadata MIT label, exact source permission text fetched; preserve included notice and audit final distribution |
| packaging | 26.3 | Build dependency; metadata Apache2 OR BSD2, pinned selector/BSD text verified; choose permitted branch explicitly and retain notices |
| pefile | 2024.8.26 | Windows build dependency; pinned MIT license fetched; age alone is not advisory clearance or a reason to replace arbitrarily |
| pyinstaller-hooks-contrib | 2026.8 | Build dependency; pinned license distinguishes GPL standard hooks from Apache runtime hooks; no blanket inherited bootloader exception claim |
| pywin32-ctypes | 0.2.3 | Windows build dependency; corrected v0.2.3 BSD3 license fetched; retain conditions/disclaimer and no endorsement |
| setuptools | 84.0.0 | Required by freezer metadata; MIT source/license-expression; no test/doc/core extras selected. Vendored distribution notices still need review |
| Bundled SQLite | Source default3.50.4.0 (engine family3.50.4), actual binary UNKNOWN | CPython PCbuild/python.props exact-tag source default, not proof installer used default. Use sqlite3 stdlib, no separate SQLite installer/provider. Confirm native binary version, provenance/notices/advisories before clearance |
| Microsoft VC native runtime / Qt third-party assets | Exact distribution requirement UNKNOWN | Qt table lists compiler toolchain but does not prove which DLLs wheel ships/needs. Do not require MSVC Build Tools or guess a redistributable pin; missing assets/notices remain B04 |

Windows marker evaluation for Python3.14 omits macOS macholib and Python<3.10 importlib_metadata, and excludes optional PyInstaller/setuptools extras. Proposed nine-wheel graph is derived from official metadata; it is not an installed lockfile or verified binary SBOM. Hash inventory below pins the selected metadata-advertised artifacts. PyPI vulnerabilities arrays were empty for queried build dependencies at retrieval; this is a narrow registry observation, NOT a complete vulnerability scan or clearance of Python/Qt/native/vendored dependencies. Root support is documentary VERIFIED_DOCUMENTATION; full binary/redistribution clearance remains PENDING_VERIFICATION/BLOCKED.

### Revised small experiment proposal — EXP-Q1, NOT_RUN
Reuse the ten objectives and existing requirement/TEST mappings in the original proposal and P5 matrix; no new requirement or TEST ID. One minimal native Qt Widgets screen and one fixed trusted Python child worker, framed versioned/correlated inherited pipes, one application sqlite3 writer and recoverable local artifact intents. Worker never grants delivery approval. Synthetic explicit UTF8 CSV profile only, originals hashed/read-only, independent expected row table, no client files/AI/network/browser/document parsers or imported code.

Likely future files, not created: proofs/P5/qt-slice/README.md; requirements-win-py314.lock; desktop.py; worker.py; contracts.py; persistence.py; artifacts.py; verify.py; Desktop.spec; Worker.spec; third-party notices and evidence manifest. Proposed isolated proofs directory remains a review-required layout exception. SQLite schema is disposable experiment metadata, not a production migration or replacement of33-entity design.

Proposed future commands (illustrative pending complete artifact/installer clearance and explicit scope approval): create a venv with the verified exact Python executable; use that venv python to install only reviewed wheels with --no-index --only-binary=:all: --require-hashes from a reviewed local wheelhouse and lock; run verify.py and desktop.py; package desktop/worker as separate PyInstaller --onedir outputs, retaining independently replaceable Qt DLLs and license/source/relink instructions. Run portable native output without system Python/network. CLI script names/source do not exist now and no command is represented as tested. Never use pip install latest or allow source builds/hooks from unreviewed dependencies.

Resource settings PROPOSED: one job/worker, sequential suites, <=1MiB input and <=10,000 rows/20 columns;60-second deadline; cancellation target<=5s with bounded action only on the owned process. Start with the tiny nominal fixture and stop on memory pressure; no throughput/idle-memory claim for this3.87GiB machine. Desktop may later prove unacceptable; then document failure rather than force success. Owner free-space snapshot supplies useful planning headroom but not measured installation sizes. Close Chrome/other heavy apps only at owner's choice, never terminate unrelated processes.

Network needed later only for official verified dependency acquisition; all jobs and portable local startup offline, no subscription/AI/cloud. Local network observer/disconnection method needs scoped permission; never alter firewall/security settings by default. Ordinary-user package in an owned disposable directory, preserve failed evidence, no client folders/deployment, no secret data. Staged finalization/restart faults, stale-approval hash rejection and manifest verification retain P3 semantics. Multi-file portable proof is not installer/release approval or general hostile-file sandbox proof.

Success/failure criteria, independent row/hash/DB/event evidence, cancellation/recovery fault matrix, approved-export invariants and local rollback follow the original ten-objective proposal above. Apply them to EXP-Q1 toolchain; ignore .NET restore/publish commands, which remain historical unexecuted examples. Capture actual Python/Qt/SQLite/native versions, source/package hashes, resource measurements and disconnected native run evidence if later authorized. Fail for missing DLLs/notices, unexpected network, native crash, exceeded bounds, false success, wrong output, stale approval or unsafe cleanup. No full239-case PASSED inference from a limited PoC.

### Current decisions and blockers
P5-B01 OPEN: exact EXP-Q1 experimental source/install/run scope not approved. P5-B02 OPEN, narrowed: laptop facts and owner's install control recorded; a specifically authorized native test route, effective OS/runtime behavior and Windows maintenance risk disposition remain unverified. P5-B03 RESOLVED, same Git checkpoint. P5-B04 OPEN: official Python binary identification/signature/hash, actual SQLite/Qt/VC contents/prerequisites, full notices/LGPL implementation and advisory closure unavailable. P5 BLOCKED. All eight ADRs PROPOSED,91 requirements unchanged,239 cases NOT_RUN, P0–P4 documentary completion preserved.

Owner's Windows no-security-updates statement is a material residual OS risk, even when Python/Qt document compatibility. Do not claim the stack restores Windows security support, enroll in ESU, change OS or make any purchase. Future live/client-data use and release need the existing security/lifecycle gates; bounded synthetic experiment permission cannot approve a release.

Exactly one next action: review/authorize the saved **evidence-only distribution inspection** prompt. It requests permission solely to download the nine pinned wheels below into an owned temporary evidence folder and inspect hashes/ZIP metadata/licenses/import tables without installing or executing them. Python installer acquisition remains excluded until an official exact URL/hash/signature record is accessible. This concrete restricted scope addresses B04 without starting PoC work.

### New official source snapshots
Retrieved2026-10-11; these are task-time source/metadata observations. Binary packages/installers were NOT downloaded.
| Key | Official URL | Result | SHA256 or error |
| --- | --- | --- | --- |
| python-version | https://raw.githubusercontent.com/python/cpython/3.14/Include/patchlevel.h | FETCHED | 6b6b66fa882788f8cc8831da33ba012aca4ab56ecc9bde469874a12b04e9904b |
| python-policy | https://raw.githubusercontent.com/python/peps/main/peps/pep-0011.rst | FETCHED | a044079d28889ebf56bccbf17c4381a80b31317567895d3fe241a1593132aeb1 |
| qt-platform | https://raw.githubusercontent.com/qt/qtdoc/v6.12.0/doc/src/platforms/supported-platforms.qdoc | FETCHED | c11b0cdc17f0733c458f5c6360fdf47467d5147968304be96cdae12e157e35cc |
| net-os | https://raw.githubusercontent.com/dotnet/core/main/release-notes/10.0/supported-os.md | FETCHED | 168f8bf76fdcaad9a1083ce5a96329291c17ef4c51e850b99c83f6e0457963f7 |
| electron | https://raw.githubusercontent.com/electron/electron/v44.7.0/README.md | FETCHED | cb788749d3f0d3991e9c17b0cbcd9fd15a8c9bd73e45874d0a936fdbd9d3745b |
| pyinstaller | https://pypi.org/pypi/pyinstaller/6.22.3/json | FETCHED | f31cd317e95e6fd2490694eed5e34437968260789dc704745cd16cdde60de4a7 |
| qtessential | https://pypi.org/pypi/PySide6-Essentials/6.12.0/json | FETCHED | 831feab9b07c343224453cf4313d56bf10a2c9c6af1e44b8778ffd25547715e6 |
| shiboken | https://pypi.org/pypi/shiboken6/6.12.0/json | FETCHED | b578fd1f2ad26c001f2c6a69b10b11b4311661e9923fd5e8f2f5b16f37be3ea3 |
| qt-table | https://raw.githubusercontent.com/qt/qtdoc/v6.12.0/doc/src/platforms/supported-platforms.qdocinc | FETCHED | 0a2ee55ae4de5b7202b512ab0f899e473be6bfca60e5f1c694c0c4e9155deae3 |
| python-win | https://raw.githubusercontent.com/python/cpython/v3.14.8/Doc/using/windows.rst | FETCHED | ebd796a5391ee3e548a0e668a1da29c1d82d4665c463f45aa4711af18c6496a3 |
| python-build | https://raw.githubusercontent.com/python/cpython/v3.14.8/PCbuild/python.props | FETCHED | d925bc2b59c2bf3adb3b11eb9e8738f3b6e101981ba7d1564b293ae55dd9906c |
| python-license | https://raw.githubusercontent.com/python/cpython/v3.14.8/LICENSE | FETCHED | b0e25a78cffb43f4d92de8b61ccfa1f1f98ecbc22330b54b5251e7b6ba010231 |
| python-release | https://www.python.org/downloads/release/python-3148/ | UNAVAILABLE | <urlopen error Tunnel connection failed: 403 Forbidden> |
| qt-license | https://raw.githubusercontent.com/qt/qtbase/v6.12.0/LICENSES/LGPL-3.0-only.txt | FETCHED | da7eabb7bafdf7d3ae5e9f223aa5bdc1eece45ac569dc21b3b037520b4464768 |
| pyside-license | https://raw.githubusercontent.com/qt/pyside-setup/v6.12.0/LICENSES/LGPL-3.0-only.txt | UNAVAILABLE | HTTP Error 404: Not Found |
| freezer-license | https://raw.githubusercontent.com/pyinstaller/pyinstaller/v6.22.3/COPYING.txt | FETCHED | 0598064c7d2718e38d7914a7d08343b2fa008e3bea9ebba2aa7a6ffa5900dd64 |
| altgraph | https://pypi.org/pypi/altgraph/json | FETCHED | f96e87a37385278bc8e0510594943dd89e6590db99cf9e0a25b0dd9d5810bc90 |
| packaging | https://pypi.org/pypi/packaging/json | FETCHED | 9d7a2885e9e79296598f8c943e0a94c2468e21c800abd26ed13c633465a78835 |
| pefile | https://pypi.org/pypi/pefile/json | FETCHED | 812ac224ad72ce8b9424da448d0bfc6d4015313cf98e6551f774ce76f9b1f2d4 |
| pyinstaller-hooks-contrib | https://pypi.org/pypi/pyinstaller-hooks-contrib/json | FETCHED | afeda2882f2a47ffffd7b66909da3284dd8fe5efb613b0a6458ceb6a0a32168e |
| pywin32-ctypes | https://pypi.org/pypi/pywin32-ctypes/json | FETCHED | 1e640bb390084cfb6510b5f25308691ec80f953467e9dc2d40d1f2bf61808ce1 |
| setuptools | https://pypi.org/pypi/setuptools/json | FETCHED | b17d794d3d3176216e3aabb872735d5e2d7aa16f62b374694af32ee6287ca73f |
| python-schedule | https://raw.githubusercontent.com/python/peps/main/peps/pep-0745.rst | FETCHED | 13adc87eaf2673bb29e0ebf9490448d0738fca9be365f4dd15ae97924ef97671 |
| qt-modules | https://raw.githubusercontent.com/qt/pyside-setup/6.12/sources/pyside6/PySide6/__init__.py.in | UNAVAILABLE | HTTP Error 404: Not Found |
| python-index | https://www.python.org/ftp/python/index-windows.json | UNAVAILABLE | <urlopen error Tunnel connection failed: 403 Forbidden> |
| altgraph-license | https://raw.githubusercontent.com/ronaldoussoren/altgraph/v0.17.5/LICENSE | FETCHED | 6c194d6db0c64d45535d10c95142b9b0cda7b7dcc7f1ddee302b3d536f3dbe46 |
| packaging-license | https://raw.githubusercontent.com/pypa/packaging/26.3/LICENSE | FETCHED | cad1ef5bd340d73e074ba614d26f7deaca5c7940c3d8c34852e65c4909686c48 |
| pefile-license | https://raw.githubusercontent.com/erocarrera/pefile/v2024.8.26/LICENSE | FETCHED | b44409c067c6da52bfb54bb6624fb11a7b52157c3a13ae1400232f8196e86ad3 |
| hooks-license | https://raw.githubusercontent.com/pyinstaller/pyinstaller-hooks-contrib/v2026.8/LICENSE | FETCHED | 91d0baaff00773038e72c0a1fc9d5d2d38706b7a2b9c04f34296608f931b9cd0 |
| ctypes-license | https://raw.githubusercontent.com/enthought/pywin32-ctypes/0.2.3/LICENSE.txt | UNAVAILABLE | HTTP Error 404: Not Found |
| setuptools-license | https://raw.githubusercontent.com/pypa/setuptools/v84.0.0/LICENSE | FETCHED | 86da0f01aeae46348a3c3d465195dc1ceccde79f79e87769a64b8da04b2a4741 |
| pip-bundled | https://raw.githubusercontent.com/python/cpython/v3.14.8/Lib/ensurepip/__init__.py | FETCHED | 18bdd155b4cdf3d6d667a98f9ab7a21782e33600b92c4e73d641eaca80e9afa9 |
| qt-license-scope | https://raw.githubusercontent.com/qt/qtbase/v6.12.0/LICENSES/BSD-3-Clause.txt | FETCHED | 9f0490f18656c6f2435bd14f603ef0c96434d1825615363dce43abb42ed1dcce |
| pyside-license-cgit | https://code.qt.io/cgit/pyside/pyside-setup.git/plain/LICENSES/LGPL-3.0-only.txt?h=v6.12.0 | UNAVAILABLE | <urlopen error Tunnel connection failed: 403 Forbidden> |
| ctypes-license-corrected | https://raw.githubusercontent.com/enthought/pywin32-ctypes/v0.2.3/LICENSE.txt | FETCHED | cc03ae891a362c85d508a4e47af954314a2e4ccbd445140cb8dca7e2baee19f7 |
| packaging-bsd | https://raw.githubusercontent.com/pypa/packaging/26.3/LICENSE.BSD | FETCHED | b70e7e9b742f1cc6f948b34c16aa39ffece94196364bc88ff0d2180f0028fac5 |
| pip-license | https://raw.githubusercontent.com/pypa/pip/26.2.1/LICENSE.txt | FETCHED | 634300a669d49aeae65b12c6c48c924c51a4cdf3d1ff086dc3456dc8bcaa2104 |
| pyside-license-branch | https://raw.githubusercontent.com/qt/pyside-setup/6.12/LICENSES/LGPL-3.0-only.txt | UNAVAILABLE | HTTP Error 404: Not Found |

### Exact proposed wheel acquisition manifest — approval required
| Name / version | Filename | SHA256 from publisher metadata | Size bytes | Official artifact URL |
| --- | --- | --- | --- | --- |
| PySide6-Essentials 6.12.0 | pyside6_essentials-6.12.0-cp310-abi3-win_amd64.whl | c9a95102aa23c1f86516a30d5a9be37552d324eee7e567eb7508973f1218cb42 | 82153795 | https://files.pythonhosted.org/packages/03/61/9a7e32a37b224f68506785bfb0f288d516098ec71681782d72b695a6c95d/pyside6_essentials-6.12.0-cp310-abi3-win_amd64.whl |
| shiboken6 6.12.0 | shiboken6-6.12.0-cp310-abi3-win_amd64.whl | a1906cb8116869178c64b6bab52623bbc8b4ceed7b30bfc3c9aa0f6e67f6438e | 1265476 | https://files.pythonhosted.org/packages/2a/b6/bee97e7a2edeab72aafabb46ee5adc939790a638d107860b4cad7a20e407/shiboken6-6.12.0-cp310-abi3-win_amd64.whl |
| pyinstaller 6.22.3 | pyinstaller-6.22.3-py3-none-win_amd64.whl | 500bd58c7bf7e584a8435adccbd763a0b918d5c12b08d74ff50fd79b2915458b | 1454907 | https://files.pythonhosted.org/packages/24/83/c5422204772a27aef643280fdc887b7ef55679989096b21dceb1b9625fc4/pyinstaller-6.22.3-py3-none-win_amd64.whl |
| altgraph 0.17.5 | altgraph-0.17.5-py2.py3-none-any.whl | f3a22400bce1b0c701683820ac4f3b159cd301acab067c51c653e06961600597 | 21228 | https://files.pythonhosted.org/packages/a9/ba/000a1996d4308bc65120167c21241a3b205464a2e0b58deda26ae8ac21d1/altgraph-0.17.5-py2.py3-none-any.whl |
| packaging 26.3 | packaging-26.3-py3-none-any.whl | d7193f7c8e4e93f444fde0262bf90af30e16fa0ad0ad44cb553c87339b23cd1c | 129956 | https://files.pythonhosted.org/packages/63/34/ba1c580383c9eada3711951fef0795c80b829a078d72188184bcab9dd527/packaging-26.3-py3-none-any.whl |
| pefile 2024.8.26 | pefile-2024.8.26-py3-none-any.whl | 76f8b485dcd3b1bb8166f1128d395fa3d87af26360c2358fb75b80019b957c6f | 74766 | https://files.pythonhosted.org/packages/54/16/12b82f791c7f50ddec566873d5bdd245baa1491bac11d15ffb98aecc8f8b/pefile-2024.8.26-py3-none-any.whl |
| pyinstaller-hooks-contrib 2026.8 | pyinstaller_hooks_contrib-2026.8-py3-none-any.whl | 6d21d65323ea4467753afc21f52d7d0e69416ae8101dd88269bf273ad48db084 | 462145 | https://files.pythonhosted.org/packages/8f/f1/3eee0263b487e571aed9204257b45bc2a0b6fec34d0a1adade4d8d8a968c/pyinstaller_hooks_contrib-2026.8-py3-none-any.whl |
| pywin32-ctypes 0.2.3 | pywin32_ctypes-0.2.3-py3-none-any.whl | 8a1513379d709975552d202d942d9837758905c8d01eb82b8bcc30918929e7b8 | 30756 | https://files.pythonhosted.org/packages/de/3d/8161f7711c017e01ac9f008dfddd9410dff3674334c233bde66e7ba65bbf/pywin32_ctypes-0.2.3-py3-none-any.whl |
| setuptools 84.0.0 | setuptools-84.0.0-py3-none-any.whl | 51a52592b3b99e102b609654876bd65f19f999935166d1352678931132b0c670 | 818216 | https://files.pythonhosted.org/packages/95/9c/c510029fc6ef33a6275cd2c5d3cecd6613dfd6aa401d57c54f1c18852ccf/setuptools-84.0.0-py3-none-any.whl |

Total selected wheel download bytes from metadata: 86411245. This is compressed acquisition size only; no installed memory/disk or signature claim. Source URLs/metadata hashes retained; failed license paths and later corrections preserved.

## Approved wheel distribution inspection — 2026-10-11 Asia/Kolkata
Owner “ok do it now” explicitly authorizes the saved nine-wheel evidence-only inspection. Scope excludes install/import/build hooks/experiments and Python installer acquisition. Branch/HEAD/index/ten pending paths matched expected baseline. Used existing trusted host Python/packaging for static parsing; downloaded modules were never imported or executed. No setup draft or environment installation needed for this inspection workflow.

### Acquisition and bounded archive verification
Downloaded exactly nine approved files from their pinned files.pythonhosted.org HTTPS URLs into an owned /tmp evidence directory. No additional packages, installers or source archives downloaded; official text documentation retrievals separately recorded below. Every advertised byte size and full SHA256 matched the approved manifest; total86,411,245 bytes. HTTPS and hashes preserved; no bypass. External publisher hash verifies consistency with metadata, not independent package authorship or Authenticode.

All ZIPs checked before content reads:<=25,000 entries/package,<=2GiB expanded/package,<=300MiB/entry,<=2,000 compression ratio,depth<=32,no duplicate entry names,traversal/rooted/drive/ADS/backslash paths or symlink attributes. Archive entries were streamed, never extracted. Total expanded metadata size229,767,646 bytes; reading this count does not imply installation. Every root wheel RECORD hashed entry checked against declared hash/size (4,273 entries); no mismatches. Each RECORD's own intentionally blank self-hash is excluded. RECORD consistency is not malicious-content clearance.

A checker initially chose setuptools' nested vendored RECORD and stopped on relative paths; corrected it to each wheel's root .dist-info RECORD, reran all checks and found no package RECORD issue. No false publisher corruption claim retained; correction described for actual evidence accountability.

| Artifact | ZIP entries | Expanded bytes | Hashed root RECORD entries | Dependency closure | Content issues |
| --- | --- | --- | --- | --- | --- |
| PySide6-Essentials 6.12.0 | 2483 | 218973578 | 2482 | PASS for Windows x64 CPython3.14, no extras | none |
| shiboken6 6.12.0 | 73 | 3117427 | 72 | PASS for Windows x64 CPython3.14, no extras | none |
| pyinstaller 6.22.3 | 571 | 3179370 | 570 | PASS for Windows x64 CPython3.14, no extras | none |
| altgraph 0.17.5 | 13 | 63350 | 12 | PASS for Windows x64 CPython3.14, no extras | none |
| packaging 26.3 | 29 | 499179 | 28 | PASS for Windows x64 CPython3.14, no extras | none |
| pefile 2024.8.26 | 11 | 344116 | 10 | PASS for Windows x64 CPython3.14, no extras | none |
| pyinstaller-hooks-contrib 2026.8 | 720 | 738854 | 719 | PASS for Windows x64 CPython3.14, no extras | none |
| pywin32-ctypes 0.2.3 | 39 | 78143 | 38 | PASS for Windows x64 CPython3.14, no extras | none |
| setuptools 84.0.0 | 343 | 2773629 | 342 | PASS for Windows x64 CPython3.14, no extras | none |

Metadata Name/Version and wheel tags match selected artifacts; Requires-Python ranges accept3.14.8. Actual Windows-marker evaluation confirms PySide Essentials -> shiboken6 and PyInstaller -> altgraph,packaging,pefile,hooks-contrib,pywin32-ctypes,setuptools; hooks-contrib -> packaging. No omitted active declared dependency or pin-range conflict. Optional/macOS/older-Python dependencies excluded through explicit marker evaluation, not ignored. A closed declared Python graph is not a closed native/vendored dependency inventory.

### Actual packaged licenses and notices
| Artifact | Observed packaged evidence | Clearance disposition |
| --- | --- | --- |
| PySide6-Essentials6.12.0 | METADATA offers LGPL3/GPL2/GPL3; License-File and visible license-named file are LicenseRef-Qt-Commercial.txt, stating terms for holders of commercial Qt licenses | BLOCKED redistribution clearance: reconcile metadata/source/binary licensing, obtain exact library LGPL/GPL text/source/third-party notices and replacement/relink instructions; do NOT conclude paid license required or commercial-only from this alone |
| shiboken6 6.12.0 | Same declared license alternatives and commercial-reference-only visible license-file inventory | Same unresolved distribution/source licensing; standalone LGPL source text path retrieval unavailable, not evidence license absent upstream |
| PyInstaller6.22.3 | Packaged COPYING.txt with GPL2-or-later bootloader exception and Apache runtime-hook terms | Text confirmed; exception does not clear bundled libraries or all standard hooks |
| altgraph0.17.5 / pefile2024.8.26 | Packaged LICENSE texts present; MIT-like permission text / MIT respectively | Notices identifiable; include exact texts, do not infer security clearance |
| packaging26.3 | LICENSE selector, LICENSE.APACHE and LICENSE.BSD present | Select supported Apache2 or BSD2 basis and preserve corresponding notices |
| hooks-contrib2026.8 | Packaged LICENSE distinguishes GPL standard hooks and Apache runtime hooks | Preserve per-file distinction; no blanket freezer exception assertion |
| pywin32-ctypes0.2.3 | Packaged BSD3 LICENSE.txt present | Preserve attribution/disclaimer/no-endorsement obligations |
| setuptools84.0.0 | MIT root license plus17 visible license/notice paths, including vendored packaging26.0/importlib_metadata8.7.1/wheel0.46.3/tomli2.4.0 and other vendored libraries | Vendor inventory/individual notices remain separate from top-level MIT and Requires-Dist; no extras downloaded or vendored code executed |

Inspecting wheel contents does not approve redistribution or imply a legal opinion. Only selected QtCore/QtGui/QtWidgets use is proposed; the full Essentials archive includes QML/network/SQL/OpenGL/tools/plugins and PDF/WebEngine-related plugin names even though no PySide meta-package was selected. Earlier “avoid browser components” describes the planned active shell, not proof the wheel has no unrelated plugin artifacts. Future packaging must explicitly identify/exclude unused modules without breaking supported runtime/source/license obligations. No fonts/resources/system DLLs assumed freely redistributable.

### Static native dependency findings
A bounded PE-header/import-table parser inspected266 .dll/.pyd/.exe assets without running them. This verifies file structure/import names only; not loader resolution, signatures, DLL versions, exported API availability or effective sandboxing. Core Qt/binding/platform assets inspected are AMD64(machine0x8664); setuptools additionally ships nonselected x86/ARM launchers, not a target mismatch.

- Essentials packages242 native assets; shiboken12; PyInstaller4; setuptools8. Counts include unused plugins/tools, not expected application process count.
- Both Qt wheels contain msvcp140*.dll,vcruntime140.dll,vcruntime140_1.dll,concrt140.dll and related VC files. Presence resolves “unknown whether bundled” only; exact versions/source/signature/redistribution rights and loader precedence remain unverified. No separate VC installer purchase/download or Visual Studio build tools recommended.
- Qt6Core.dll imports **icuuc.dll**. No icuuc.dll is present in either inspected Qt wheel; Essentials includes resources/icudtl.dat, which is data and not the required DLL. Effective provider/version/license/OS availability is UNKNOWN; do not declare Windows supplies it or install an arbitrary ICU package. This is an exact native closure gap P5-C02.
- Core binding .pyd files import python3.dll and shiboken6.abi3.dll; the latter is supplied by the second wheel. Python distribution/provider still needs verification. Qt6Gui/Widgets import Qt6Core/Gui and VC plus system DirectX/UI libraries; qwindows.dll supplies the proposed native platform plugin. System API contracts and graphics/ordinary-user loading require actual native proof.
- Official Qt Windows deployment source says ICU/OpenSSL dependencies must be distributed when linked and distinguishes permitted redistributables from development/debug runtime files. This supports investigating actual imports; it does not prove the unidentified icuuc.dll can be bundled or fetched under this task.

| Selected asset | Non-system import examples requiring package/provider evidence | Status |
| --- | --- | --- |
| Qt6Core.dll | MSVCP140.dll/MSVCP140_1.dll,VCRUNTIME140/VCRUNTIME140_1,icuuc.dll | VC names present in wheels; ICU provider missing/UNKNOWN |
| Qt6Gui.dll / Qt6Widgets.dll | Qt6Core/Qt6Gui,MSVCP140 family,VCRUNTIME140 family | Internal names present; system/graphics/runtime verification NOT_RUN |
| QtCore/QtGui/QtWidgets.pyd / pyside6.abi3.dll | Qt libs,python3.dll,shiboken6.abi3.dll,VC | Package chain partly established; Python DLL identity/loading unverified |
| Shiboken.pyd / shiboken6.abi3.dll | python3.dll,VC | Python provider pending |
| plugins/platforms/qwindows.dll | Qt6Core/Gui,VC,Windows UI/DirectX/API-set libs | File present; native startup NOT_RUN |

Full raw inspection JSON and downloaded bytes remain outside source. Inspection JSON SHA256 recorded below; selected facts, source/hash manifest and licensed-file paths retained here. No package imported or signatures represented as verified.

### Remaining precise clearance gaps and status
| Local gap | Required evidence / next step | Blocker |
| --- | --- | --- |
| P5-C01 | Reconcile Qt/shiboken exact binary license alternatives with packaged commercial-reference inventory; official corresponding source/LGPL terms, module/third-party/VC notices and relinking/replacement plan | B04 OPEN |
| P5-C02 | Establish exact trusted provider/version/license for QtCore icuuc.dll and closed minimal native dependency inventory; no unapproved binary download | B04 OPEN |
| P5-C03 | Official Python3.14.8 x64 distribution identity/download URL/hash/signature/notices and actual stdlib SQLite/VC assets; release/index access unavailable, installer excluded | B04 OPEN |
| P5-C04 | Current official advisories and exact vendored/native/Qt/CPython asset provenance/security clearance; registry empty vulnerability arrays are insufficient | B04 OPEN |
| P5-C05 | Explicit complete experiment scope approval and genuine native loader/offline/resource/approval/recovery evidence | B01/B02 OPEN |

Owner “ok do it now” approves this evidence-only download task, NOT experiment execution, installation or production ADRs. Preserve P0–P4 documentary completion,B03 RESOLVED,P5 BLOCKED,eight ADRs PROPOSED,239 cases NOT_RUN. Target information need not be recollected. Windows no-security-update residual risk unchanged. EXP-Q1 remains conditional and is **not installation-cleared**. No pending risk closed merely by hash or source text inspection.

Exactly one next action: review/authorize the saved **targeted Qt/Python distribution-clearance recovery** prompt, scoped to official documentation/metadata and the already verified nine archives. It resolves these identified gaps or records that candidate change is necessary; no new binary acquisition/install/PoC silently authorized.

### Follow-up official source investigation
| Key | Official URL | Result | SHA256 or error |
| --- | --- | --- | --- |
| pyside-lgpl | https://raw.githubusercontent.com/qt/pyside-setup/6.12.0/LICENSES/LGPL-3.0-only.txt | UNAVAILABLE | HTTP Error 404: Not Found |
| pyside-readme | https://raw.githubusercontent.com/qt/pyside-setup/6.12.0/README.md | UNAVAILABLE | HTTP Error 404: Not Found |
| qt-security | https://raw.githubusercontent.com/qt/qtbase/v6.12.0/SECURITY.md | UNAVAILABLE | HTTP Error 404: Not Found |
| python-release-api | https://api.github.com/repos/python/cpython/releases/tags/v3.14.8 | UNAVAILABLE | <urlopen error Tunnel connection failed: 403 Forbidden> |
| python-security | https://raw.githubusercontent.com/python/cpython/v3.14.8/SECURITY.md | UNAVAILABLE | HTTP Error 404: Not Found |
| pyside-wheel-licenses | https://raw.githubusercontent.com/qt/pyside-setup/6.12.0/LICENSES/LicenseRef-Qt-Commercial.txt | UNAVAILABLE | HTTP Error 404: Not Found |
| qtpython-license-doc | https://doc.qt.io/qtforpython-6/licenses.html | UNAVAILABLE | <urlopen error Tunnel connection failed: 403 Forbidden> |
| qt-licensing | https://raw.githubusercontent.com/qt/qtdoc/v6.12.0/doc/src/legal/licensing.qdoc | UNAVAILABLE | HTTP Error 404: Not Found |
| qt-icu-doc | https://raw.githubusercontent.com/qt/qtdoc/v6.12.0/doc/src/platforms/windows.qdoc | FETCHED | d6b939a84efa17796bb32da572e971b2324329004c7aa312c09d297614b03b61 |
| pyside-license-main | https://raw.githubusercontent.com/qt/pyside-setup/dev/LICENSES/LGPL-3.0-only.txt | UNAVAILABLE | HTTP Error 404: Not Found |
| pyside-source-main | https://raw.githubusercontent.com/qt/pyside-setup/dev/README.md | UNAVAILABLE | HTTP Error 404: Not Found |

Static inspection record SHA256: `94daef5ab126c80e613d972d8c353b44976507d06d3a26711bc05012fcd64c63`; acquisition record SHA256: `23bf25f38e170300fdbf7aed8a40813c4a56f9567b2de7980e54fbbc6a3afedc`. No persistent setup/configuration saved because no install/startup is authorized or required for this evidence workflow.

## Dependency/distribution evidence recovery — 2026-10-11 Asia/Kolkata
Authority: owner “P5 DEPENDENCY AND DISTRIBUTION EVIDENCE RECOVERY”, documentary/static evidence only. Current prohibition on new binary downloads overrides the previous recovery prompt's conditional re-download fallback; existing nine archives are available and no download needed. Checked AGENTS, rulebooks, latest report/decision/handoff, unchanged docs/governance-baseline HEAD15acfb58dfa9f9616b60b2c41c771953cbfc878c,ten pending paths and empty index. Only six existing P5 docs updated, prior records preserved.

### Issue 1 — Qt/PySide licensing reconciliation
Corrected an earlier source-location mistake: Qt for Python's repository is **pyside/pyside-setup**, not qt/pyside-setup. Exact v6.12.0 README.pyside6.md explicitly says PySide6 is available under open-source LGPLv3/GPLv2/GPLv3 and commercial licensing, and recommends PyPI. Exact libpyside/pyside.h and libshiboken/shiboken.h declare LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only; inspected Qt qglobal.h/qwidget.h declare the same alternatives. Exact LGPL3 and GPL3 texts are now fetched from the proper repository. This corroborates the inspected METADATA; no blanket commercial-only or paid-subscription requirement established.

The actual wheels still have only LicenseRef-Qt-Commercial.txt in their visible license-text inventory. That is an incomplete distribution/compliance inventory for the proposed LGPL route, not evidence that metadata/source alternatives disappeared. wheel_artifacts/pyproject.toml.base declares the same LGPL/GPL text, while build_scripts/config.py loads it. No fetched build setting establishes why only the commercial reference was copied; do not invent a publisher bug/root cause or treat this textual reconciliation as proof every shipped asset is LGPL. P5-C01 **license-option interpretation RECONCILED**, full binary/module/third-party compliance still OPEN.

Proposed LGPL3 route obligations for a future combined distribution, not approved legal clearance:
1. Include the applicable LGPL3 and GPL3 texts, prominent library/use/copyright notices and individual third-party/VC notices; preserve modifications/attribution and selected license basis.
2. Offer/provide corresponding covered-library source and applicable build/relink/replacement materials using a GPL-compatible method; a vague link to moving upstream main is insufficient. Identify exact shipped library versions and matching source modifications.
3. Combined-work terms must permit modification for the user's own use and reverse engineering for debugging library modifications. Do not impose contradictory EULA restrictions.
4. Select an appropriate shared-library/relink mechanism and demonstrate operation with a modified compatible library or provide the alternate corresponding application-code/source path required by the license. PyInstaller onedir alone does not prove compliance or Qt replacement; runtime DLL loading and replacement must later be tested.
5. Provide installation information where license conditions apply; retain notices/source/materials for the covered distribution. System libraries are distinct from shipped redistributable binaries. A commercial alternative is not selected or paid for. GPL alternative would have broader combined-work distribution implications and must not be silently chosen.

License clauses are verified documentary facts; satisfaction for the actual planned package is pending. No production packaging source/installer or license notices written outside this authorized specification.

### Issue 2 — ICU interpretation corrected
The previous “absent wheel DLL => missing native dependency” concern was too broad. MicrosoftDocs/win32 official ICU page explicitly records **icuuc.dll and icuin.dll as Windows10 system DLLs introduced in1703**, with combined icu.dll added in1903. The page's API location/name list includes these system DLLs and the corresponding C functions. Owner target22H2/build19045 is later than both releases. The bare unversioned name is consistent with the documented Windows system library, unlike a separately packaged version-suffixed ICU build.

Static reinspection of the existing hash-verified Qt6Core.dll found20 imported ICU functions/data-symbol names; **all20 appear in Microsoft's documented ICU API list**, with no ordinal-only/undocumented ICU import found in that descriptor. No DLL was executed, downloaded or resolved by a Windows loader. Imported names:

`ucnv_open`, `ucnv_close`, `UCNV_FROM_U_CALLBACK_SUBSTITUTE`, `UCNV_TO_U_CALLBACK_SUBSTITUTE`, `ucnv_reset`, `ucnv_getMaxCharSize`, `ucnv_getName`, `ucnv_getToUCallBack`, `ucnv_getFromUCallBack`, `ucnv_setToUCallBack`, `ucnv_setFromUCallBack`, `ucnv_cbToUWriteUChars`, `ucnv_toUnicode`, `ucnv_cbFromUWriteUChars`, `ucnv_toUCountPending`, `ucnv_fromUCountPending`, `ucnv_getStandardName`, `ucnv_getAvailableName`, `ucnv_countAvailable`, `ucnv_fromUnicode`.

Disposition: a **documented OS-supplied dependency and an earlier incomplete interpretation**, not an established genuine missing dependency/distribution mismatch/packaging defect. It is appropriate not to duplicate an OS system DLL in the wheel when the target provides its documented API. icudtl.dat remains data, not a DLL replacement. No arbitrary ICU binary download, system-DLL redistribution or extra ICU installation recommended. P5-C02 documentary provider explanation RESOLVED; laptop file authenticity/presence/export/loader behavior remains NOT_RUN under B02/native verification and full B04 provenance boundaries. Do not claim every owner's Windows image is intact.

Future read-only laptop evidence (not run here): ordinary64-bit Windows PowerShell may inspect `%SystemRoot%\System32\icuuc.dll` and `icuin.dll` file/version metadata and Get-AuthenticodeSignature; if a catalog-signed system file reports no embedded signature, do not automatically label it unauthentic—catalog/Windows servicing verification is separate. No repairs or system changes authorized. Future native startup resolves actual loader/search-path/API behavior. This task does not ask owner to repeat hardware facts or fetch DLLs from third-party sites.

### Issue 3 — Python official provenance and exact distribution route
Pinned CPython3.14.8 Windows documentation identifies CPython-team distributions: Install Manager from python.org/Microsoft Store, official NuGet packages for build scenarios, and embeddable packages. It explicitly lists python for64-bit,pythonx86 for32-bit and pythonarm64 forARM64. The NuGet documentation is primary vendor evidence for the official build package route, not popularity-based inference. Install Manager may default to latest unless an exact runtime is requested; that does not meet our pinning requirement. No manager/runtime installed. Embeddable distributions have capability limitations and are not silently substituted.

Publisher package metadata retrieved over normal TLS from NuGet: package **python3.14.8**, authors Python Software Foundation, description64-bit build-scenario runtime, project python.org, CPython repository commit8e6e75d, license file tools\LICENSE.txt. CPython's exact Tools/nuget/python.nuspec and make_pkg.proj establish this package family/id/x64 layout route. Registration/catalog metadata gives a concrete new evidence-acquisition proposal below. Publisher-authors field alone is not a verified signer; hashes alone are not independent authenticity or legal clearance.

The previously sought python.org release/index page still cannot be retrieved from cloud (403); this does not mean Python distribution is unavailable. The exact official NuGet build route is now a viable **alternative distribution candidate**, not final adoption or approval of a replacement installed interpreter. Choosing it for EXP-Q1 would be an experimental distribution-tuple revision that the owner must approve after static/native evidence; it does not alter the desktop/framework ADR. No NuGet CLI or .NET SDK required merely to inspect a package archive.

Authenticity verification methods (planned, NOT_RUN): compare downloaded bytes to official catalog SHA512 and size before inspection; inspect package signature(s), signer/certificate chain/timestamp and verification evidence with trusted tooling where available; inspect native PE Authenticode/Windows-catalog identity as applicable. CPython Install Manager documentation describes signed JSON catalogs, requires_signature/root/publisher/EKU checks and hash-bound downloads; it does not establish that every NuGet package is author-signed or that the source project's SignOutput=false setting identifies the final publication signature. Do not bypass absent verification or require a guessed signer certificate.

License/native inventory: exact CPython LICENSE is PSF2 with retained copyright/agreement, modification summaries for derivative works, historical license texts and separately licensed incorporated software. Source PCbuild/python.props defaults:SQLite3.50.4.0,OpenSSL3.5.9,bzip2 1.0.8,xz5.2.5,libffi3.4.4,mpdecimal4.0.0,zlib1.3.1,zlib-ng2.2.4. These are source defaults, not proof the published package includes them unchanged. ensurepip source pin26.2.1 does not prove the NuGet layout includes pip; inspect actual layout before prescribing pip/venv/bootstrap. Check full native DLL/stdlib/tools/license inventory, vendored pip terms and VC rights per selected distribution. SQLite primary public-domain policy is not a blanket license for every bundled asset. Current advisories/binary signatures/actual SQLite version are unresolved; native imports/run tests remain NOT_RUN.

Windows support: pinned3.14.8 documentation says Windows10+, and previously retrieved PEP11/PEP745 establish feature-release OS support retained by maintenance releases. This does not restore Windows10 Home security updates or prove the laptop works. Exact distribution build/native prerequisite evidence and later native run still required.

### Architecture consistency — actual historical decision chain
1. ADR-0002/P3 **PROPOSED** says evaluate .NET10/WPF first only on an exact vendor-listed target and evaluate alternatives on target mismatch; Python/PySide is explicitly an alternative. No .NET decision was approved.
2. Initial P5 EXP-N1 follows that conditional preference, with SQLite provider/source/binary/target gaps.
3. Owner then supplied Home Single Language22H2/build19045. Refreshed .NET10 OS table does not list this Home22H2 configuration; no blanket Win10 or ESU support inferred.
4. Under owner-authorized alternative review, EXP-Q1 became the single conditional experiment recommendation because pinned Python/Qt sources document OS support and selected Qt Widgets avoids a full browser shell. No benchmark or4GiB capacity proof exists.
5. SQLite stays the proposed local persistence capability; Python uses stdlib sqlite3 rather than Microsoft.Data.Sqlite. There is no approved provider/language switch. Native worker/IPC/domain/artifact/review boundaries remain P3 contracts, not rewritten internals or implementation.

Neither stack adopted; all8 ADR files remain byte-identical PROPOSED. Documentary milestone approval does not approve a framework, dependency version, language, DB provider, distribution route, worker confinement or release. Future source/experiment approval is separate from production ADR adoption.

### Updated gap dispositions and single next action
| Gap | Actual progress | Remaining evidence |
| --- | --- | --- |
| P5-C01 licensing | Open-source alternatives and official LGPL/GPL source texts reconciled; earlier wrong source path corrected | Exact minimal native/module/VC/third-party notices and covered-library source/replacement/relink package compliance OPEN |
| P5-C02 ICU | Microsoft system-library provider +20/20 documented symbols; documentary ambiguity RESOLVED | Actual target system-file/load verification NOT_RUN; no extra ICU package proposed |
| P5-C03 Python | Official distribution sources/support/authenticity method verified; exact NuGet package identity/hash/size located | Actual package signatures/native/stdlib-SQLite/pip/notices inventory not inspected; binary acquisition not authorized here |
| P5-C04 provenance/advisories | Source defaults and interpretation limits explicit | Current full native/vendored advisory/signature/rights clearance OPEN |
| P5-C05 execution | Laptop facts/install control unchanged | Explicit complete experiment/native scope approval and real Windows evidence pending |

P5-B01/B02/B04 OPEN; B03 RESOLVED; P5 BLOCKED. P0–P4 documentary completion,91 requirements,239 NOT_RUN cases,8 PROPOSED ADRs preserved. No risk closed. Exactly one next action: **review/authorize evidence-only acquisition and static inspection of the one official python3.14.8 x64 NuGet package below**, with no installation or execution. This completes the missing binary inventory before proposing any experiment. No repeated Qt-wheel download or unspecified installer required.

### Concrete next artifact proposal — NOT downloaded
Official registration-derived URL: `https://api.nuget.org/v3-flatcontainer/python/3.14.8/python.3.14.8.nupkg`.

Expected filename: `python.3.14.8.nupkg`; expected compressed bytes: **15554015**.

Publisher catalog SHA512 (base64): `b9oz/C2qiLlE7FKAogz3dyiT38vFX3d9K2IqhooLZmcL3E9REJsgrg3eUXeTHLXRy50jgfHEoX1bx3u91Vjeaw==`.

Use owned /tmp evidence only,TLS and same trusted API host,no redirects to unrelated destinations,strict size/hash before archive reads. Inspect bounded ZIP paths/counts/expanded sizes,read native/license/stdlib/pip metadata and PE imports/signature structures statically; do not execute/unpack into an environment/install/import package modules. Signature parsing alone is not certificate-chain verification. No new tool installs; unavailable trusted verification is a BLOCKED result. Resolve missing Qt/VC notices from authoritative text and already inspected wheels within that task. No outside dependency acquisition or app code.

### Recovery source snapshots
Official source text/metadata only; retrieval hashes identify snapshots,not binary signatures. Earlier failed Qt paths and unsupported interpretations remain historical above.
| Key | URL | Result | SHA256 or access error |
| --- | --- | --- | --- |
| windows-icu | https://raw.githubusercontent.com/MicrosoftDocs/win32/docs/desktop-src/Intl/international-components-for-unicode--icu-.md | FETCHED | 84721795242f3b6d480a2a04581fcd99e7bec80ca3e4c88e10f77c193d034d74 |
| pyside-license | https://raw.githubusercontent.com/pyside/pyside-setup/v6.12.0/LICENSES/LGPL-3.0-only.txt | FETCHED | da7eabb7bafdf7d3ae5e9f223aa5bdc1eece45ac569dc21b3b037520b4464768 |
| pyside-readme | https://raw.githubusercontent.com/pyside/pyside-setup/v6.12.0/README.md | FETCHED | 94ba63b907235169b408b099606c91eaf5cd35ef1c71947a879c51dc239bb8c7 |
| pyside-pypi | https://raw.githubusercontent.com/pyside/pyside-setup/v6.12.0/setup.py | FETCHED | 17be28239e1a8139f83066832a97f2343fe76d6b16ed1dcb71086309f347d4f7 |
| python-release | https://www.python.org/downloads/release/python-3148/ | UNAVAILABLE | <urlopen error Tunnel connection failed: 403 Forbidden> |
| python-winget | https://raw.githubusercontent.com/microsoft/winget-pkgs/master/manifests/p/Python/Python/3/3.14.8/Python.Python.3.installer.yaml | UNAVAILABLE | HTTP Error 404: Not Found |
| python-windows | https://raw.githubusercontent.com/python/cpython/v3.14.8/Doc/using/windows.rst | FETCHED | ebd796a5391ee3e548a0e668a1da29c1d82d4665c463f45aa4711af18c6496a3 |
| qt-icu | https://raw.githubusercontent.com/qt/qtbase/v6.12.0/src/corelib/configure.cmake | FETCHED | 62e638897f2eb136baa337e0d24306f98835e5496244c124e7d2ede1631c15a0 |
| pyside-license-readme | https://raw.githubusercontent.com/pyside/pyside-setup/v6.12.0/README.pyside6.md | FETCHED | 29dce932c304c6a63e142a560db161d4cdd93b0806a8a6ef3eef0233e5ccbef6 |
| shiboken-license-readme | https://raw.githubusercontent.com/pyside/pyside-setup/v6.12.0/README.shiboken6.md | FETCHED | 104061725327e98dd75f951d28e257c5edd04e16d90e81b73f4ff445ca24b7eb |
| pyside-header | https://raw.githubusercontent.com/pyside/pyside-setup/v6.12.0/sources/pyside6/libpyside/pyside.h | FETCHED | d01b36b37492b773096576076e31e2c18e57ad197e00848b3c4a49446f02778a |
| pyside-config | https://raw.githubusercontent.com/pyside/pyside-setup/v6.12.0/build_scripts/config.py | FETCHED | 1c78987e0d5105200933816958f3bf58fb622d9b315b54a9c1d7de0ca11e9724 |
| pyside-gpl | https://raw.githubusercontent.com/pyside/pyside-setup/v6.12.0/LICENSES/GPL-3.0-only.txt | FETCHED | 8ceb4b9ee5adedde47b31e975c1d90c73ad27b6b165a1dcd80c7c545eb65b903 |
| qt-header | https://raw.githubusercontent.com/qt/qtbase/v6.12.0/src/corelib/global/qglobal.h | FETCHED | 701afb76d34526593d7bd128219f2db5abccd029cdba7b9e115305c3cd558aac |
| python-build | https://raw.githubusercontent.com/python/cpython/v3.14.8/PCbuild/python.props | FETCHED | d925bc2b59c2bf3adb3b11eb9e8738f3b6e101981ba7d1564b293ae55dd9906c |
| python-license | https://raw.githubusercontent.com/python/cpython/v3.14.8/LICENSE | FETCHED | b0e25a78cffb43f4d92de8b61ccfa1f1f98ecbc22330b54b5251e7b6ba010231 |
| python-manager | https://raw.githubusercontent.com/python/pymanager/main/README.md | FETCHED | fb16208b2442d21e47177f73d986df9496c8bb59075b4753613dcdbfa72a0d75 |
| python-nuget-metadata | https://api.nuget.org/v3-flatcontainer/python/3.14.8/python.nuspec | FETCHED | ea8a8c44ca7b1e9e4b38a51a430083e98a7f3134d11fa25e10086b7cdf5acda2 |
| pyside-pyproject | https://raw.githubusercontent.com/pyside/pyside-setup/v6.12.0/pyproject.toml | UNAVAILABLE | HTTP Error 404: Not Found |
| shiboken-header | https://raw.githubusercontent.com/pyside/pyside-setup/v6.12.0/sources/shiboken6/libshiboken/shiboken.h | FETCHED | d89447d3839b2179d3839f994965110f0889d95425c71540bc352e0836714c74 |
| python-nuget-hash | https://api.nuget.org/v3-flatcontainer/python/3.14.8/python.3.14.8.nupkg.sha512 | UNAVAILABLE | HTTP Error 404: Not Found |
| python-nuget-build | https://raw.githubusercontent.com/python/cpython/v3.14.8/Tools/nuget/make_pkg.proj | FETCHED | 76fd1a57f3307688f7c2820fe07f3c5e7190bd9d18766eb34c6993cd7a90df8f |
| python-nuget-native | https://raw.githubusercontent.com/python/cpython/v3.14.8/Tools/nuget/python.nuspec | FETCHED | a29fd1e339a960763c199d41ce90d5b2786af9bd2e7cc7f919d64f50d8ae1d4d |
| qt-widgets-header | https://raw.githubusercontent.com/qt/qtbase/v6.12.0/src/widgets/kernel/qwidget.h | FETCHED | edfcaf4c202ac8c28fb21d2445a7334eefb569af15d82326316c1f156be01dda |
| python-pip-license | https://raw.githubusercontent.com/python/cpython/v3.14.8/Lib/ensurepip/__init__.py | FETCHED | 18bdd155b4cdf3d6d667a98f9ab7a21782e33600b92c4e73d641eaca80e9afa9 |
| python-registration | https://api.nuget.org/v3/registration5-semver1/python/3.14.8.json | FETCHED | 635c0ddb5f0c286778f0ec50c72974ca6c4357f603ae8c74f9ebe84b3c558dc1 |
| python-catalog | https://api.nuget.org/v3/catalog0/data/2026.09.30.20.00.00/python.3.14.8.json | FETCHED | 4e7c4ce3407b34eb602f8d00e3dd13724ab6ab595ac7266609b28bed5998c2e5 |
| pyside-init | https://raw.githubusercontent.com/pyside/pyside-setup/v6.12.0/build_scripts/__init__.py | FETCHED | 8b68996a8d650eb0f6a981b5b7c304e871bb9fd528ef90552d717a82418e9409 |
| pyside-wheel-project | https://raw.githubusercontent.com/pyside/pyside-setup/v6.12.0/wheel_artifacts/pyproject.toml.base | FETCHED | 405f32998a375b1e70b2095c0fd1435bf5eab342d387d5a35ad754bb5babed5f |
| python-layout | https://raw.githubusercontent.com/python/cpython/v3.14.8/PC/layout/__main__.py | FETCHED | 4475a03d1cda6dc0ae1c83c8941cc92cf33d0fcdea198a8e9d566f212a49fd6c |

ICU static-symbol evidence JSON SHA256: `d0b48c7e5bcbfbec80b96610c7988498297b0046298c598ff8cd0eb132302994`. No new binary downloaded, code imported from archives, installation or runtime experiment.

## Official Python static-inspection preflight — 2026-10-11 UTC
Authorization: owner approved one official Python3.14.8 x64 package static inspection, but explicitly required the exact publisher SHA-256 and size to be established before download. Latest user instructions take precedence over the saved SHA-512 proposal. Starting branch docs/governance-baseline, HEAD15acfb58dfa9f9616b60b2c41c771953cbfc878c, ten pending documentation paths and empty index match the checkpoint. Existing work preserved.

### Identity and digest gate
Official registration, catalog and nuspec fetched again over verified TLS establish python3.14.8, Python Software Foundation author metadata, x64 build-scenario description, source commit8e6e75d and license path tools\LICENSE.txt. Exact URL: https://api.nuget.org/v3-flatcontainer/python/3.14.8/python.3.14.8.nupkg ; expected size15,554,015 bytes. A HEAD request only (no binary response body read) returned HTTP200 and matching Content-Length. Catalog packageHashAlgorithm is SHA512, not SHA256; the HEAD x-ms-meta-sha512 agrees with the catalog:

`b9oz/C2qiLlE7FKAogz3dyiT38vFX3d9K2IqhooLZmcL3E9REJsgrg3eUXeTHLXRy50jgfHEoX1bx3u91Vjeaw==`

The inspected authoritative registration/catalog/nuspec and HEAD headers do not establish a publisher SHA-256 for these exact bytes. Content-MD5 and ETag are not SHA-256. A SHA-512 cannot be converted into the corresponding SHA-256. A locally calculated SHA-256 after acquisition would be an observation, not a pre-download publisher expectation. This is an algorithm/authorization prerequisite mismatch, not evidence of a corrupt or unsafe package. No claim that no publisher SHA-256 exists anywhere.

### Actual outcomes
Identity/declared size/SHA-512 metadata cross-check PASS (documentary only). Required pre-download publisher SHA-256 gate BLOCKED. Binary download, actual size/hash checks, archive inspection, native imports/signatures, bundled license/notices and redistribution clearance NOT_RUN. No binary downloaded, installed, extracted or executed. NuGet catalog packageEntries are publisher-declared inventory, not a verified inspection of archive bytes. Authors/source links do not prove cryptographic authorship. Prior Python/Qt/.NET findings remain historical and conditional; no stack or ADR approved.

P5 BLOCKED; B01/B02/B04 OPEN, B03 RESOLVED. The SHA-256 preflight gap belongs to B04; no new blocker identifier allocated. P0–P4 documentary completion, eight PROPOSED ADRs and all239 application cases NOT_RUN preserved. No application development, experiments, additional binary acquisition or Git mutation.

Exactly one recommended next action: approve a revised digest gate using the official NuGet SHA-512 and size before static inspection, with local SHA-256 recorded afterward as observed evidence only. The saved current prompt requests this exact narrow change; it does not execute automatically or approve technology adoption/installation/PoC.

### Refreshed official text sources
| Source | URL | Result | Snapshot SHA256 |
| --- | --- | --- | --- |
| registration | https://api.nuget.org/v3/registration5-semver1/python/3.14.8.json | FETCHED | 635c0ddb5f0c286778f0ec50c72974ca6c4357f603ae8c74f9ebe84b3c558dc1 |
| catalog | https://api.nuget.org/v3/catalog0/data/2026.09.30.20.00.00/python.3.14.8.json | FETCHED | 4e7c4ce3407b34eb602f8d00e3dd13724ab6ab595ac7266609b28bed5998c2e5 |
| nuspec | https://api.nuget.org/v3-flatcontainer/python/3.14.8/python.nuspec | FETCHED | ea8a8c44ca7b1e9e4b38a51a430083e98a7f3134d11fa25e10086b7cdf5acda2 |
| nuget-catalog-doc | https://raw.githubusercontent.com/NuGet/docs.microsoft.com-nuget/main/docs/api/catalog-resource.md | FETCHED | 3667ddc6b2a2ce9e864865b65c7ea24df8f59acd957e5c1b821e947f1a427fc7 |

### Superseded saved prompt — historical proposal, not executed
The following saved SHA-512 proposal was approved subject to the latest SHA-256 prerequisite, which prevented download. It is retained as historical instructions, not execution evidence.

```text
# P5 exact Python distribution inspection — approval gated

PROJECT: Freelance Automation Studio. ROLE: Windows runtime/dependency/license security reviewer.
MODE: evidence-only acquisition and static inspection; no installation or executable experiment.

OWNER GATE: Owner must explicitly authorize downloading ONE official x64 Python3.14.8 NuGet artifact specified below. Current recovery prohibited new binaries; approval of this prompt is not PoC or technology/ADR adoption approval. Do not download before authorization.

CHECKPOINT: Read AGENTS/master/architecture/development/testing/security/release/execution books,P5 decision/prerequisite/matrix/MS-0006 report and8 PROPOSED ADRs. Verify docs/governance-baseline HEAD15acfb58dfa9f9616b60b2c41c771953cbfc878c,ten pending paths/empty index and preserve existing work.

CONTEXT: Owner target Windows10 Home22H2/build19045 x64,i3-6006U,3.87GiB RAM,61.81GiB C:free;Chrome/WebView versions/control recorded. Do not recollect facts. .NET10 target mismatch prompted conditional Python3.14.8/Qt6.12/PyInstaller6.22.3 alternative under PROPOSED ADR-0002;no final adoption. Existing9 wheels hash/RECORD verified. Correct PySide upstream establishes LGPL/GPL alternatives;full compliance pending. Microsoft establishes icuuc.dll as Windows OS library since1703 and all20 Qt ICU imports documented;no third-party ICU package needed by documentary evidence,native proof still NOT_RUN.

EXACT NEW ARTIFACT:
URL: https://api.nuget.org/v3-flatcontainer/python/3.14.8/python.3.14.8.nupkg
Filename: python.3.14.8.nupkg
Expected compressed size: 15554015 bytes
Publisher SHA512 base64: b9oz/C2qiLlE7FKAogz3dyiT38vFX3d9K2IqhooLZmcL3E9REJsgrg3eUXeTHLXRy50jgfHEoX1bx3u91Vjeaw==
Official registration: https://api.nuget.org/v3/registration5-semver1/python/3.14.8.json

SCOPE: Revalidate official text metadata,then download only this exact package to owned /tmp evidence with TLS/host/size bounds and full SHA512 comparison. Hash/size mismatch stops use;do not replace expectation to make it pass. Do not install NuGet/.NET or fetch another runtime/dependency/installer.

STATIC INSPECTION: Bounded ZIP listing/path/entry/decompression checks before streamed reads,prefer no extraction. Inspect root nuspec,licenses,tools/runtime/stdlib/ensurepip/pip/native assets,PE imports/version/signature structures using existing trusted tools. Verify actual Python architecture/version,SQLite/OpenSSL/VC/native inventory and per-asset notices where statically demonstrable. Do not import downloaded modules or run executables/build hooks. Signature structure or hash alone is not certificate-chain/authorship proof;use trusted verification only where already available,otherwise BLOCKED. Source project SignOutput=false does not prove final package unsigned.

ADDITIONAL DOCUMENTARY WORK: Complete minimal Qt widget/shiboken/VC/library notices/source/replacement plan from already verified archives/official text;no new Qt/ICU binary. Review official current advisory evidence,not just empty registry vulnerability lists. Assess whether this vendor-documented build distribution contains required venv/pip/freezer capabilities;do not silently switch the experimental distribution tuple.

DELIVERABLES: Update only6 P5 docs:decision package,prerequisite plan,experiment matrix,MS-0006 report,execution book,current-next-prompt. Record hashes/source/signature/native/licensing findings,unavailable evidence,proposed exact distribution tuple and owner scope gate. Keep binary evidence outside repository.

RESTRICTIONS: No installation,package imports/scripts,source/prototype/fixture code,native/PoC/browser/offline/benchmark/security tests,system/Windows changes,credentials/client data,ADR approval,stage/commit/push/merge/reset/clean,deployment or P6. No binary outside the one approved artifact.

VERIFICATION: Documentary links/anchors/formatting/identifiers/status/scope/protected hashes;actual artifact checks vs pending native/runtime evidence. Preserve P0–P4 documentary completion,B03 RESOLVED,8 ADRs PROPOSED,239 tests NOT_RUN. Keep P5 BLOCKED while mandatory explicit complete-scope/native/provenance/license evidence missing;source facts alone never approve release.

FINAL: Baseline/files,acquisition/static results,exact native/license/authenticity gaps,architecture consistency,blockers/test/ADR states,documentation results,exactly ONE next action. Save ONE complete gated next prompt for bounded experiment approval only if actual evidence supports it;otherwise precise recovery. Do not execute next prompt. Stop for owner review.
```

## Approved Python SHA-512 static inspection — 2026-10-11 UTC
Owner authorization: P5 PYTHON PACKAGE STATIC INSPECTION WITH OFFICIAL SHA-512 VERIFICATION explicitly supersedes prior publisher SHA-256 precondition for this one artifact only. No installation/experiment/adoption/ADR/Git authority inferred. Baseline branch docs/governance-baseline HEAD15acfb58dfa9f9616b60b2c41c771953cbfc878c,ten pending documentation paths,empty index. No unrelated work overwritten.

### Acquisition and integrity
Official CPython3.14.8 Windows documentation links the x64 NuGet python family. Fresh official NuGet registration/catalog confirm python3.14.8,x64 description,PSF author metadata,source reference8e6e75d,license tools\LICENSE.txt. URL: https://api.nuget.org/v3-flatcontainer/python/3.14.8/python.3.14.8.nupkg . Expected and actual bytes:15,554,015. Independently refreshed catalog packageHashAlgorithm SHA512 and HTTP HEAD x-ms-meta-sha512/Content-Length agree; full streamed download matches both before archive reads. Verified TLS/trusted-host redirects/strict transfer-size bounds; exactly one new binary package downloaded outside repository to `/tmp/p5-python-evidence-dsau35lk/python.3.14.8.nupkg`. No extraction/installation/downloaded code execution/import.

Official and matching actual SHA512 base64:
`b9oz/C2qiLlE7FKAogz3dyiT38vFX3d9K2IqhooLZmcL3E9REJsgrg3eUXeTHLXRy50jgfHEoX1bx3u91Vjeaw==`

**Locally computed SHA256**, not a publisher expectation:
`ce85f674d9a63029f709cbff7a3da1c6bc5bfcfaefdd9999f98fa0290470c454`

### Static results and limitations
Archive safety checks/CRC reads PASS:1,382 entries,41,662,246 expanded bytes; bounded entry count/single-file/ratio/total/depth,no unsafe paths,symlinks,encrypted entries or case-colliding names found. All1,379 catalog-listed entries match archive names/sizes;three additional ZIP package infrastructure entries (`_rels/.rels`, `[Content_Types].xml`, `package/services/metadata/core-properties/nuget.psmdcp`) recorded,not interpreted as unexplained executables. Catalog list comparison is not independent per-file signed-hash validation.

41 PE native assets inspected statically:37AMD64,2x86,2ARM64. Four non-AMD64 assets are pip/distlib launcher variants,not the core interpreter architecture. Core Python EXE/DLLs are AMD64;python314.dll contains3.14.8 string,Windows fixed version3.14.8150.1013 (different encoding,not silently called semantic-version mismatch).35PEs have embedded certificate tables;6pip/distlib launchers do not. No claim unsigned launchers are automatically malicious. Inventory includes libcrypto-3.dll/libssl-3.dll fixed3.5.9.0,sqlite3.dll fixed3.50.4.0/string3.50.4,libffi-8.dll,libtommath.dll,python3.dll/python314.dll,vcruntime140.dll/vcruntime140_1.dll fixed14.51.36247.0. Versions are static resources/strings,not runtime execution measurements. Remaining imports are Windows API-set/system DLL names; actual target resolution/search-path/delay-load/plugin/ABI behavior NOT_RUN. Static import names alone do not prove complete runtime closure.

Pip26.2.1 METADATA/MIT plus22declared license-file references all located;venv10entries,ensurepip4entries,pip450entries present. Availability is static presence,not demonstrated bootstrap/freezer functionality. No hidden dependency acquisition or pip command executed.

NuGet `.signature.p7s` and Windows `tools/DLLs/python.cat` present. OpenSSL CMS parsing shows NuGet.org Repository by Microsoft certificate;CMS mathematical check and chain-to-existing-host-trust check with purpose any PASS. Initial legacy PKCS7 parser failed on NuGet CMS encoding,corrected to CMS parser; native Authenticode structure required PKCS7 parser instead. Parser mismatches were tooling format differences,not package verification defects. A diagnostic noverify CMS check did not constitute trust verification; later host-chain check used existing trust store. **These checks are not full NuGet package-signature verification**: signed ZIP hash reconstruction,NuGet repository signature policy/trusted-signer identity/EKU/timestamp/revocation not fully verified. Embedded native certificates in inspected Python314/SQLite show Python Software Foundation subject;certificate presence/subject parsing does not verify native file Authenticode digests,chain,timestamp/revocation/catalog coverage. Actual native authenticity remains pending,not passed. Signed NuGet content includes a SHA256 hash for the NuGet signing representation;it is not the full final-package SHA256 and is not substituted for the local artifact hash.

### Licensing/redistribution
43license/notice-like text assets inventoried and hashed,including35,407-byte tools/LICENSE.txt,PSF/historical agreements,Windows Microsoft Distributable Code additional conditions,bzip2/libffi/Zstandard/Apache2 text and pip/vendor notices. Python agreement requires retaining notices/license and brief changes summary for derivative modifications. Additional Windows conditions require applicable Microsoft redistribution restrictions and protective downstream terms,forbid altering notices,misleading Microsoft trademarks,unsupported-platform distribution and malicious/deceptive/unlawful programs. This is direct shipped-license evidence,not assumed blanket open-source clearance.

Pip MIT retains copyright/license;vendored Apache/BSD/MIT/MPL-style obligations must be mapped per selected asset rather than covered by Python's license alone. Main LICENSE includes Apache2 text,but exact native-component/copyright/NOTICE mapping remains incomplete;absence of a component name from that text is not proof its terms are absent or violated. Exact VC14.51 redistribution rights/source build agreement,OpenSSL/SQLite/libtommath/other linked components and Qt LGPL covered-library source/replaceability/notices still need consolidated distribution evidence. Full license/advisory/redistribution clearance BLOCKED;no legal guarantee or adoption approval claimed. Preserve license materials when making a future minimal runtime proposal;do not remove pip/vendor assets without documented requirements and later verification.

### Current milestone and one next action
Python artifact identity/size/SHA512/archive/native/pip/license inventory PASS for stated static scope. Prior SHA256-specific preflight stop is historical and now superseded by explicit owner authorization. P5-B04 remains OPEN for full native signature/advisory/license/redistribution closure;B01complete experiment scope approval/B02approved native route and real proof OPEN;B03RESOLVED;P5BLOCKED. Eight ADRs PROPOSED,91requirements/239application cases NOT_RUN preserved. No experimental/runtime/Windows/offline/browser/performance/security test claimed. No risk closed.

Exactly one recommended next action: authorize the saved documentation-only distribution-clearance and native-verification approval package;it resolves remaining evidence mappings and defines concrete trusted verification/Windows scope for review without executing anything. No repeated package download,installation or new owner hardware questionnaire.

### Exact native import inventory
| Asset | Machine | Fixed version | Embedded certificate bytes | Imports / delayed imports |
| --- | --- | --- | --- | --- |
| tools/DLLs/_asyncio.pyd | 0x8664 | 3.14.8150.1013 | 14048 | KERNEL32.dll, VCRUNTIME140.dll, api-ms-win-crt-runtime-l1-1-0.dll, python314.dll |
| tools/DLLs/_bz2.pyd | 0x8664 | 3.14.8150.1013 | 14048 | KERNEL32.dll, VCRUNTIME140.dll, api-ms-win-crt-heap-l1-1-0.dll, api-ms-win-crt-runtime-l1-1-0.dll, api-ms-win-crt-stdio-l1-1-0.dll, python314.dll |
| tools/DLLs/_ctypes.pyd | 0x8664 | 3.14.8150.1013 | 14048 | KERNEL32.dll, OLEAUT32.dll, VCRUNTIME140.dll, api-ms-win-crt-runtime-l1-1-0.dll, api-ms-win-crt-stdio-l1-1-0.dll, api-ms-win-crt-string-l1-1-0.dll, libffi-8.dll, ole32.dll, python314.dll |
| tools/DLLs/_decimal.pyd | 0x8664 | 3.14.8150.1013 | 14048 | KERNEL32.dll, VCRUNTIME140.dll, api-ms-win-crt-convert-l1-1-0.dll, api-ms-win-crt-heap-l1-1-0.dll, api-ms-win-crt-locale-l1-1-0.dll, api-ms-win-crt-math-l1-1-0.dll, api-ms-win-crt-runtime-l1-1-0.dll, api-ms-win-crt-stdio-l1-1-0.dll, api-ms-win-crt-string-l1-1-0.dll, python314.dll |
| tools/DLLs/_elementtree.pyd | 0x8664 | 3.14.8150.1013 | 14048 | KERNEL32.dll, VCRUNTIME140.dll, api-ms-win-crt-runtime-l1-1-0.dll, api-ms-win-crt-string-l1-1-0.dll, python314.dll |
| tools/DLLs/_hashlib.pyd | 0x8664 | 3.14.8150.1013 | 14048 | KERNEL32.dll, VCRUNTIME140.dll, api-ms-win-crt-runtime-l1-1-0.dll, api-ms-win-crt-string-l1-1-0.dll, libcrypto-3.dll, python314.dll |
| tools/DLLs/_lzma.pyd | 0x8664 | 3.14.8150.1013 | 14048 | KERNEL32.dll, VCRUNTIME140.dll, api-ms-win-crt-heap-l1-1-0.dll, api-ms-win-crt-runtime-l1-1-0.dll, python314.dll |
| tools/DLLs/_multiprocessing.pyd | 0x8664 | 3.14.8150.1013 | 14048 | KERNEL32.dll, VCRUNTIME140.dll, WS2_32.dll, api-ms-win-crt-runtime-l1-1-0.dll, python314.dll |
| tools/DLLs/_overlapped.pyd | 0x8664 | 3.14.8150.1013 | 14048 | KERNEL32.dll, VCRUNTIME140.dll, WS2_32.dll, api-ms-win-crt-runtime-l1-1-0.dll, api-ms-win-crt-string-l1-1-0.dll, python314.dll |
| tools/DLLs/_queue.pyd | 0x8664 | 3.14.8150.1013 | 14048 | KERNEL32.dll, VCRUNTIME140.dll, api-ms-win-crt-runtime-l1-1-0.dll, python314.dll |
| tools/DLLs/_remote_debugging.pyd | 0x8664 | 3.14.8150.1013 | 14048 | KERNEL32.dll, VCRUNTIME140.dll, api-ms-win-crt-runtime-l1-1-0.dll, api-ms-win-crt-string-l1-1-0.dll, python314.dll |
| tools/DLLs/_socket.pyd | 0x8664 | 3.14.8150.1013 | 14048 | IPHLPAPI.DLL, KERNEL32.dll, RPCRT4.dll, VCRUNTIME140.dll, WS2_32.dll, api-ms-win-crt-runtime-l1-1-0.dll, api-ms-win-crt-stdio-l1-1-0.dll, api-ms-win-crt-string-l1-1-0.dll, python314.dll |
| tools/DLLs/_sqlite3.pyd | 0x8664 | 3.14.8150.1013 | 14048 | KERNEL32.dll, VCRUNTIME140.dll, api-ms-win-crt-runtime-l1-1-0.dll, api-ms-win-crt-string-l1-1-0.dll, python314.dll, sqlite3.dll |
| tools/DLLs/_ssl.pyd | 0x8664 | 3.14.8150.1013 | 14048 | CRYPT32.dll, KERNEL32.dll, VCRUNTIME140.dll, WS2_32.dll, api-ms-win-crt-runtime-l1-1-0.dll, api-ms-win-crt-stdio-l1-1-0.dll, api-ms-win-crt-string-l1-1-0.dll, libcrypto-3.dll, libssl-3.dll, python314.dll |
| tools/DLLs/_uuid.pyd | 0x8664 | 3.14.8150.1013 | 14048 | KERNEL32.dll, RPCRT4.dll, VCRUNTIME140.dll, api-ms-win-crt-runtime-l1-1-0.dll, python314.dll |
| tools/DLLs/_wmi.pyd | 0x8664 | 3.14.8150.1013 | 14048 | KERNEL32.dll, OLEAUT32.dll, PROPSYS.dll, VCRUNTIME140.dll, VCRUNTIME140_1.dll, api-ms-win-crt-heap-l1-1-0.dll, api-ms-win-crt-runtime-l1-1-0.dll, api-ms-win-crt-string-l1-1-0.dll, python314.dll, ole32.dll |
| tools/DLLs/_zoneinfo.pyd | 0x8664 | 3.14.8150.1013 | 14048 | KERNEL32.dll, VCRUNTIME140.dll, api-ms-win-crt-runtime-l1-1-0.dll, python314.dll |
| tools/DLLs/_zstd.pyd | 0x8664 | 3.14.8150.1013 | 14048 | KERNEL32.dll, VCRUNTIME140.dll, api-ms-win-crt-heap-l1-1-0.dll, api-ms-win-crt-runtime-l1-1-0.dll, api-ms-win-crt-stdio-l1-1-0.dll, api-ms-win-crt-time-l1-1-0.dll, python314.dll |
| tools/DLLs/libcrypto-3.dll | 0x8664 | 3.5.9.0 | 14072 | ADVAPI32.dll, CRYPT32.dll, KERNEL32.dll, USER32.dll, VCRUNTIME140.dll, WS2_32.dll, api-ms-win-crt-convert-l1-1-0.dll, api-ms-win-crt-environment-l1-1-0.dll, api-ms-win-crt-filesystem-l1-1-0.dll, api-ms-win-crt-heap-l1-1-0.dll, api-ms-win-crt-runtime-l1-1-0.dll, api-ms-win-crt-stdio-l1-1-0.dll, api-ms-win-crt-string-l1-1-0.dll, api-ms-win-crt-time-l1-1-0.dll, api-ms-win-crt-utility-l1-1-0.dll |
| tools/DLLs/libffi-8.dll | 0x8664 | not located | 12048 | KERNEL32.dll, VCRUNTIME140.dll, api-ms-win-crt-runtime-l1-1-0.dll |
| tools/DLLs/libssl-3.dll | 0x8664 | 3.5.9.0 | 14072 | KERNEL32.dll, VCRUNTIME140.dll, WS2_32.dll, api-ms-win-crt-convert-l1-1-0.dll, api-ms-win-crt-environment-l1-1-0.dll, api-ms-win-crt-filesystem-l1-1-0.dll, api-ms-win-crt-heap-l1-1-0.dll, api-ms-win-crt-runtime-l1-1-0.dll, api-ms-win-crt-string-l1-1-0.dll, api-ms-win-crt-time-l1-1-0.dll, api-ms-win-crt-utility-l1-1-0.dll, libcrypto-3.dll |
| tools/DLLs/libtommath.dll | 0x8664 | not located | 14048 | ADVAPI32.dll, KERNEL32.dll, api-ms-win-crt-environment-l1-1-0.dll, api-ms-win-crt-heap-l1-1-0.dll, api-ms-win-crt-private-l1-1-0.dll, api-ms-win-crt-runtime-l1-1-0.dll, api-ms-win-crt-stdio-l1-1-0.dll, api-ms-win-crt-string-l1-1-0.dll, api-ms-win-crt-time-l1-1-0.dll |
| tools/DLLs/pyexpat.pyd | 0x8664 | 3.14.8150.1013 | 14048 | KERNEL32.dll, VCRUNTIME140.dll, api-ms-win-crt-convert-l1-1-0.dll, api-ms-win-crt-environment-l1-1-0.dll, api-ms-win-crt-heap-l1-1-0.dll, api-ms-win-crt-runtime-l1-1-0.dll, api-ms-win-crt-stdio-l1-1-0.dll, api-ms-win-crt-string-l1-1-0.dll, python314.dll |
| tools/DLLs/select.pyd | 0x8664 | 3.14.8150.1013 | 14048 | KERNEL32.dll, VCRUNTIME140.dll, WS2_32.dll, api-ms-win-crt-runtime-l1-1-0.dll, python314.dll |
| tools/DLLs/sqlite3.dll | 0x8664 | 3.50.4.0 | 14048 | KERNEL32.dll, VCRUNTIME140.dll, api-ms-win-crt-heap-l1-1-0.dll, api-ms-win-crt-math-l1-1-0.dll, api-ms-win-crt-runtime-l1-1-0.dll, api-ms-win-crt-string-l1-1-0.dll, api-ms-win-crt-time-l1-1-0.dll, api-ms-win-crt-utility-l1-1-0.dll |
| tools/DLLs/unicodedata.pyd | 0x8664 | 3.14.8150.1013 | 14048 | KERNEL32.dll, VCRUNTIME140.dll, api-ms-win-crt-runtime-l1-1-0.dll, api-ms-win-crt-stdio-l1-1-0.dll, api-ms-win-crt-string-l1-1-0.dll, python314.dll |
| tools/DLLs/winsound.pyd | 0x8664 | 3.14.8150.1013 | 14048 | KERNEL32.dll, USER32.dll, VCRUNTIME140.dll, WINMM.dll, api-ms-win-crt-runtime-l1-1-0.dll, python314.dll |
| tools/Lib/site-packages/pip/_vendor/distlib/t32.exe | 0x14c | 1.1.0.14 | 0 | KERNEL32.dll, SHLWAPI.dll |
| tools/Lib/site-packages/pip/_vendor/distlib/t64-arm.exe | 0xaa64 | 1.1.0.14 | 0 | KERNEL32.dll, SHLWAPI.dll |
| tools/Lib/site-packages/pip/_vendor/distlib/t64.exe | 0x8664 | 1.1.0.14 | 0 | KERNEL32.dll, SHLWAPI.dll |
| tools/Lib/site-packages/pip/_vendor/distlib/w32.exe | 0x14c | 1.1.0.14 | 0 | KERNEL32.dll, SHLWAPI.dll, USER32.dll |
| tools/Lib/site-packages/pip/_vendor/distlib/w64-arm.exe | 0xaa64 | 1.1.0.14 | 0 | KERNEL32.dll, SHLWAPI.dll, USER32.dll |
| tools/Lib/site-packages/pip/_vendor/distlib/w64.exe | 0x8664 | 1.1.0.14 | 0 | KERNEL32.dll, SHLWAPI.dll, USER32.dll |
| tools/Lib/venv/scripts/nt/venvlauncher.exe | 0x8664 | 3.14.8150.1013 | 14048 | KERNEL32.dll, api-ms-win-core-path-l1-1-0.dll |
| tools/Lib/venv/scripts/nt/venvwlauncher.exe | 0x8664 | 3.14.8150.1013 | 14048 | KERNEL32.dll, USER32.dll, api-ms-win-core-path-l1-1-0.dll |
| tools/python.exe | 0x8664 | 3.14.8150.1013 | 14048 | KERNEL32.dll, VCRUNTIME140.dll, api-ms-win-crt-heap-l1-1-0.dll, api-ms-win-crt-locale-l1-1-0.dll, api-ms-win-crt-math-l1-1-0.dll, api-ms-win-crt-runtime-l1-1-0.dll, api-ms-win-crt-stdio-l1-1-0.dll, python314.dll |
| tools/python3.dll | 0x8664 | 3.14.8150.1013 | 14048 |  |
| tools/python314.dll | 0x8664 | 3.14.8150.1013 | 14048 | ADVAPI32.dll, KERNEL32.dll, VCRUNTIME140.dll, VERSION.dll, WS2_32.dll, api-ms-win-core-path-l1-1-0.dll, api-ms-win-crt-conio-l1-1-0.dll, api-ms-win-crt-convert-l1-1-0.dll, api-ms-win-crt-environment-l1-1-0.dll, api-ms-win-crt-filesystem-l1-1-0.dll, api-ms-win-crt-heap-l1-1-0.dll, api-ms-win-crt-locale-l1-1-0.dll, api-ms-win-crt-math-l1-1-0.dll, api-ms-win-crt-process-l1-1-0.dll, api-ms-win-crt-runtime-l1-1-0.dll, api-ms-win-crt-stdio-l1-1-0.dll, api-ms-win-crt-string-l1-1-0.dll, api-ms-win-crt-time-l1-1-0.dll, bcrypt.dll |
| tools/pythonw.exe | 0x8664 | 3.14.8150.1013 | 14048 | KERNEL32.dll, VCRUNTIME140.dll, api-ms-win-crt-heap-l1-1-0.dll, api-ms-win-crt-locale-l1-1-0.dll, api-ms-win-crt-math-l1-1-0.dll, api-ms-win-crt-runtime-l1-1-0.dll, api-ms-win-crt-stdio-l1-1-0.dll, python314.dll |
| tools/vcruntime140.dll | 0x8664 | 14.51.36247.0 | 20408 | KERNEL32.dll, api-ms-win-crt-convert-l1-1-0.dll, api-ms-win-crt-heap-l1-1-0.dll, api-ms-win-crt-runtime-l1-1-0.dll, api-ms-win-crt-stdio-l1-1-0.dll, api-ms-win-crt-string-l1-1-0.dll |
| tools/vcruntime140_1.dll | 0x8664 | 14.51.36247.0 | 20416 | KERNEL32.dll, VCRUNTIME140.dll, api-ms-win-crt-heap-l1-1-0.dll, api-ms-win-crt-runtime-l1-1-0.dll, api-ms-win-crt-string-l1-1-0.dll |

### Packaged license inventory
| Path | Raw-file SHA256 |
| --- | --- |
| tools/LICENSE.txt | 935cf13e19f8c31b497d20b05d73623431a226b230c3599bc30fa3348979bc68 |
| tools/Lib/site-packages/pip-26.2.1.dist-info/licenses/AUTHORS.txt | 4eb1fb1705e2def898e81bcba19c3aac80620d27ba3569d6a6df7b4629d1b5c2 |
| tools/Lib/site-packages/pip-26.2.1.dist-info/licenses/LICENSE.txt | 634300a669d49aeae65b12c6c48c924c51a4cdf3d1ff086dc3456dc8bcaa2104 |
| tools/Lib/site-packages/pip-26.2.1.dist-info/licenses/src/pip/_vendor/cachecontrol/LICENSE.txt | 86eeee87be2a43f3ff1f56496f451f69243926f025fedbb033666c304c4c161b |
| tools/Lib/site-packages/pip-26.2.1.dist-info/licenses/src/pip/_vendor/certifi/LICENSE | e93716da6b9c0d5a4a1df60fe695b370f0695603d21f6f83f053e42cfc10caf7 |
| tools/Lib/site-packages/pip-26.2.1.dist-info/licenses/src/pip/_vendor/distlib/LICENSE.txt | 808e10c8a6ab8deb149ff9b3fb19f447a808094606d712a9ca57fead3552599d |
| tools/Lib/site-packages/pip-26.2.1.dist-info/licenses/src/pip/_vendor/distro/LICENSE | cb5e8e7e5f4a3988e1063c142c60dc2df75605f4c46515e776e3aca6df976e14 |
| tools/Lib/site-packages/pip-26.2.1.dist-info/licenses/src/pip/_vendor/idna/LICENSE.md | 1a9a4f0e3d479a27240ddd59a9137a66ab4a0f9dfdc8ca6188cc0bfd85187f04 |
| tools/Lib/site-packages/pip-26.2.1.dist-info/licenses/src/pip/_vendor/msgpack/COPYING | 492dedba85da5872f78e6091bcd1fea474d660d35acb4dee964b8aab3f007427 |
| tools/Lib/site-packages/pip-26.2.1.dist-info/licenses/src/pip/_vendor/packaging/LICENSE | cad1ef5bd340d73e074ba614d26f7deaca5c7940c3d8c34852e65c4909686c48 |
| tools/Lib/site-packages/pip-26.2.1.dist-info/licenses/src/pip/_vendor/packaging/LICENSE.APACHE | 0d542e0c8804e39aa7f37eb00da5a762149dc682d7829451287e11b938e94594 |
| tools/Lib/site-packages/pip-26.2.1.dist-info/licenses/src/pip/_vendor/packaging/LICENSE.BSD | b70e7e9b742f1cc6f948b34c16aa39ffece94196364bc88ff0d2180f0028fac5 |
| tools/Lib/site-packages/pip-26.2.1.dist-info/licenses/src/pip/_vendor/pkg_resources/LICENSE | 86da0f01aeae46348a3c3d465195dc1ceccde79f79e87769a64b8da04b2a4741 |
| tools/Lib/site-packages/pip-26.2.1.dist-info/licenses/src/pip/_vendor/platformdirs/LICENSE | 29e0fd62e929850e86eb28c3fdccf0cefdf4fa94879011cffb3d0d4bed6d4db6 |
| tools/Lib/site-packages/pip-26.2.1.dist-info/licenses/src/pip/_vendor/pygments/LICENSE | a9d66f1d526df02e29dce73436d34e56e8632f46c275bbdffc70569e882f9f17 |
| tools/Lib/site-packages/pip-26.2.1.dist-info/licenses/src/pip/_vendor/pyproject_hooks/LICENSE | 1b22b049b5267d6dfc23a67bf4a84d8ec04b9fdfb1a51d360e42b4342c8b4154 |
| tools/Lib/site-packages/pip-26.2.1.dist-info/licenses/src/pip/_vendor/requests/LICENSE | 09e8a9bcec8067104652c168685ab0931e7868f9c8284b66f5ae6edae5f1130b |
| tools/Lib/site-packages/pip-26.2.1.dist-info/licenses/src/pip/_vendor/resolvelib/LICENSE | f388fd38cad13112c1dc0f669bbe80e7f84541edbafb72f3030d2ca7642c3c9d |
| tools/Lib/site-packages/pip-26.2.1.dist-info/licenses/src/pip/_vendor/rich/LICENSE | deed7c17a4318158190a3ea239cc879a5a50271cebb98ae7025f48fbe58dca15 |
| tools/Lib/site-packages/pip-26.2.1.dist-info/licenses/src/pip/_vendor/tomli/LICENSE | b80816b0d530b8accb4c2211783790984a6e3b61922c2b5ee92f3372ab2742fe |
| tools/Lib/site-packages/pip-26.2.1.dist-info/licenses/src/pip/_vendor/tomli_w/LICENSE | b80816b0d530b8accb4c2211783790984a6e3b61922c2b5ee92f3372ab2742fe |
| tools/Lib/site-packages/pip-26.2.1.dist-info/licenses/src/pip/_vendor/truststore/LICENSE | 33be7b7e8fa4fd19b1760e1a8ed8a668bdab852c91b692dd41424bcb725a9fca |
| tools/Lib/site-packages/pip-26.2.1.dist-info/licenses/src/pip/_vendor/urllib3/LICENSE.txt | 130e3a64d5fdd5d096a752694634a7d9df284469de86e5732100268041e3d686 |
| tools/Lib/site-packages/pip/_vendor/cachecontrol/LICENSE.txt | 86eeee87be2a43f3ff1f56496f451f69243926f025fedbb033666c304c4c161b |
| tools/Lib/site-packages/pip/_vendor/certifi/LICENSE | e93716da6b9c0d5a4a1df60fe695b370f0695603d21f6f83f053e42cfc10caf7 |
| tools/Lib/site-packages/pip/_vendor/distlib/LICENSE.txt | 808e10c8a6ab8deb149ff9b3fb19f447a808094606d712a9ca57fead3552599d |
| tools/Lib/site-packages/pip/_vendor/distro/LICENSE | cb5e8e7e5f4a3988e1063c142c60dc2df75605f4c46515e776e3aca6df976e14 |
| tools/Lib/site-packages/pip/_vendor/idna/LICENSE.md | 1a9a4f0e3d479a27240ddd59a9137a66ab4a0f9dfdc8ca6188cc0bfd85187f04 |
| tools/Lib/site-packages/pip/_vendor/msgpack/COPYING | 492dedba85da5872f78e6091bcd1fea474d660d35acb4dee964b8aab3f007427 |
| tools/Lib/site-packages/pip/_vendor/packaging/LICENSE | cad1ef5bd340d73e074ba614d26f7deaca5c7940c3d8c34852e65c4909686c48 |
| tools/Lib/site-packages/pip/_vendor/packaging/LICENSE.APACHE | 0d542e0c8804e39aa7f37eb00da5a762149dc682d7829451287e11b938e94594 |
| tools/Lib/site-packages/pip/_vendor/packaging/LICENSE.BSD | b70e7e9b742f1cc6f948b34c16aa39ffece94196364bc88ff0d2180f0028fac5 |
| tools/Lib/site-packages/pip/_vendor/pkg_resources/LICENSE | 86da0f01aeae46348a3c3d465195dc1ceccde79f79e87769a64b8da04b2a4741 |
| tools/Lib/site-packages/pip/_vendor/platformdirs/LICENSE | 29e0fd62e929850e86eb28c3fdccf0cefdf4fa94879011cffb3d0d4bed6d4db6 |
| tools/Lib/site-packages/pip/_vendor/pygments/LICENSE | a9d66f1d526df02e29dce73436d34e56e8632f46c275bbdffc70569e882f9f17 |
| tools/Lib/site-packages/pip/_vendor/pyproject_hooks/LICENSE | 1b22b049b5267d6dfc23a67bf4a84d8ec04b9fdfb1a51d360e42b4342c8b4154 |
| tools/Lib/site-packages/pip/_vendor/requests/LICENSE | 09e8a9bcec8067104652c168685ab0931e7868f9c8284b66f5ae6edae5f1130b |
| tools/Lib/site-packages/pip/_vendor/resolvelib/LICENSE | f388fd38cad13112c1dc0f669bbe80e7f84541edbafb72f3030d2ca7642c3c9d |
| tools/Lib/site-packages/pip/_vendor/rich/LICENSE | deed7c17a4318158190a3ea239cc879a5a50271cebb98ae7025f48fbe58dca15 |
| tools/Lib/site-packages/pip/_vendor/tomli/LICENSE | b80816b0d530b8accb4c2211783790984a6e3b61922c2b5ee92f3372ab2742fe |
| tools/Lib/site-packages/pip/_vendor/tomli_w/LICENSE | b80816b0d530b8accb4c2211783790984a6e3b61922c2b5ee92f3372ab2742fe |
| tools/Lib/site-packages/pip/_vendor/truststore/LICENSE | 33be7b7e8fa4fd19b1760e1a8ed8a668bdab852c91b692dd41424bcb725a9fca |
| tools/Lib/site-packages/pip/_vendor/urllib3/LICENSE.txt | 130e3a64d5fdd5d096a752694634a7d9df284469de86e5732100268041e3d686 |

Static inspection result JSON snapshot SHA256: `27c97cb392b9d145fe36d9438b058bbe75316fbdcc70f5cfd21d1b7655d13880`. Full1,382entry inventory and entry hashes retained outside repository at /tmp/p5-python-approved-inspection.json;cloud temporary storage is not a durable artifact archive. A future authorized evidence checkpoint should preserve manifests/checksums without committing runtime binaries.

### Consumed SHA-512 inspection prompt — scope executed, P5 not completed
```text
# P5 official Python package inspection — revised digest approval gate

PROJECT: Freelance Automation Studio
ROLE: Windows runtime, dependency provenance and redistribution reviewer.
MODE: one-package evidence-only acquisition and static inspection; no installation or executable experiment.

APPROVAL PREREQUISITE: Owner must explicitly approve replacing the unavailable pre-download publisher SHA-256 requirement with verification against the official NuGet SHA-512 plus exact size. Calculate SHA-256 locally afterward for evidence identity only; never call it a publisher hash. If this change is not approved, stop before download. Approval does not approve architecture ADRs, production adoption, native experiments or installation.

CHECKPOINT: Read AGENTS.md; master, architecture, development, testing, security, release and execution books; P5 decision package, prerequisites plan, planned experiment matrix, MS-0006-P5 report and all eight proposed ADRs. Verify branch docs/governance-baseline, HEAD15acfb58dfa9f9616b60b2c41c771953cbfc878c, ten pending documentation paths and empty index. Preserve existing files and historical evidence; stop on unexpected unsafe discrepancies.

EXACT ARTIFACT (one binary only):
URL: https://api.nuget.org/v3-flatcontainer/python/3.14.8/python.3.14.8.nupkg
Filename: python.3.14.8.nupkg
Expected bytes: 15554015
Official SHA512 base64: b9oz/C2qiLlE7FKAogz3dyiT38vFX3d9K2IqhooLZmcL3E9REJsgrg3eUXeTHLXRy50jgfHEoX1bx3u91Vjeaw==
Official registration: https://api.nuget.org/v3/registration5-semver1/python/3.14.8.json
Official catalog: https://api.nuget.org/v3/catalog0/data/2026.09.30.20.00.00/python.3.14.8.json

PRE-DOWNLOAD: Re-fetch official text metadata over verified TLS and confirm package identity, x64 description, exact URL, size and SHA512 algorithm/value against this proposal. Stop on discrepancy; never change expected values to make a check pass. Latest preflight downloaded no binary because only SHA512 was published in inspected sources.

AUTHORIZED AFTER EXPLICIT DIGEST APPROVAL: Download exactly this package into owned /tmp evidence, with bounded transfer, verified TLS and trusted host/redirect controls. Compare full bytes to official size/SHA512 before archive reads. Record computed SHA256 as locally observed. No other binary/tool/dependency download.

STATIC INSPECTION: Use existing trusted tools only. Check bounded ZIP count/expanded sizes/ratios/path traversal/case collisions/symlinks before streamed reads, preferably without extraction. Inspect nuspec, actual license/notices, stdlib/venv/ensurepip/pip assets, native DLL/PE architecture/import/version/signature structures and bundled SQLite/OpenSSL/VC components. Distinguish signature presence from trusted chain/signer verification; unavailable verification stays BLOCKED. Do not import archive code, execute binaries/build hooks or install packages. Publisher inventory is not actual archive evidence until verified. Evaluate redistribution obligations without asserting unsupported legal clearance.

CONTEXT: Existing nine Qt/freezer wheels are hash/RECORD verified. Qt open-source alternatives reconciled, complete redistribution clearance pending. ICU OS-provider documentation corrected earlier wheel-absence concern; native target loading remains NOT_RUN. Python/Qt is a conditional alternative after .NET10 target support mismatch, not final adoption. Laptop facts already recorded; do not recollect them. Preserve all eight ADRs PROPOSED.

DOCUMENTATION SCOPE: Update only P5 decision package, prerequisites plan, planned experiment matrix, MS-0006-P5 report, execution book and current-next-prompt.md. Keep binary evidence outside repository. Preserve historical prompts/findings. Record actual results, remaining provenance/license/native/advisory gaps and blockers.

RESTRICTIONS: No installation, downloaded code execution/import, runtime/Qt/Windows/PoC experiments, application/fixture code, additional binary downloads, native tests, benchmarks, ADR approval, Git staging/commit/push/merge/reset/clean, deployment or P6.

VERIFICATION/ACCEPTANCE: Actual archive/hash/static results must be evidenced and limitations explicit. Verify documentation inventory/links/anchors/identifiers/statuses/whitespace/protected baseline hashes/Git scope. P0–P4 documentary completion preserved; B03 RESOLVED; B01/B02/B04 remain OPEN where mandatory evidence/approval absent; P5 BLOCKED until its actual prerequisites are met; all239 application tests remain NOT_RUN. Do not conflate static evidence with Windows compatibility or authenticity proof.

FINAL REPORT: A package identity/source; B download/hash verification; C static findings; D license/provenance; E uncertainties; F documentation checks; G blocker statuses; H exactly ONE next recommended action. Save one complete approval-gated next prompt addressing remaining blockers; do not execute it automatically. Stop for owner review.
```

## Consolidated distribution clearance and native verification plan — 2026-10-11 UTC
Authorization: owner P5 DISTRIBUTION CLEARANCE AND NATIVE VERIFICATION PLAN, documentation/static existing-evidence only. Branch docs/governance-baseline / HEAD15acfb58dfa9f9616b60b2c41c771953cbfc878c; ten pending paths,empty index. No installation,new binary,downloaded software execution,prototype,Windows configuration,ADR or Git change authorized. New observations below supplement,not replace,historical records.

### Already verified; do not repeat research
Fresh local integrity recheck PASS for the existing Python package (full official SHA512/size) and all nine wheel files (previously verified SHA256/size). Previous bounded ZIP/CRC/RECORD/native import inventories remain relevant because artifact bytes did not change. Reuse Python1,382entries/41native assets/43license text assets,Qt242native assets/shiboken12 and freezer/tool inventories,20/20Microsoft-documented ICU imports,Python3.14.8/SQLite3.50.4/OpenSSL3.5.9/VC14.51.36247 static observations. Full hashes/asset paths are in preceding inspection sections. No new artifact acquisition or package import. Static results are not evidence of runtime behavior.

### Component-to-license clearance register
States below apply to evidence,not stack approval. VERIFIED_DOCUMENTATION means identified official text/declaration; PENDING_VERIFICATION means exact binary/build/obligation fulfillment still missing.
| Component / proposed role | Existing packaged evidence and authoritative source | Applicable obligations / remaining condition | Evidence status |
| --- | --- | --- | --- |
| CPython3.14.8 x64 runtime | tools/LICENSE.txt PSF/historical agreements;official CPython pinned LICENSE/Windows docs;NuGet hash and PSF source reference | Retain agreement/copyright;modified derivative summary where applicable. Native PSF certificates parsed,not full Authenticode verified;separate included-component terms | VERIFIED_DOCUMENTATION;native identity PENDING_VERIFICATION |
| SQLite3.50.4 runtime DLL | tools/DLLs/sqlite3.dll resources/string;official sqlite/sqlite version-3.50.4 LICENSE.md explicitly public-domain RDBMS/amalgamation,with non-public-domain build-tool exceptions | No copyright-license notice requirement invented for public-domain core;retain documented origin/version. Source-only auxiliary licenses do not automatically apply to runtime DLL. Actual build options/extensions/compiler runtime still map separately | Core license VERIFIED_DOCUMENTATION;binary provenance PENDING_VERIFICATION |
| OpenSSL3.5.9 DLLs | libcrypto-3.dll/libssl-3.dll;official openssl-3.5.9 LICENSE.txt Apache2;Python consolidated LICENSE includes Apache2 text | Retain Apache2 license/relevant copyright/attributions;mark modified files;preserve applicable NOTICE if upstream includes one. Requested root NOTICE404 does not prove no NOTICE obligations elsewhere;resolve exact build attribution | License VERIFIED_DOCUMENTATION;notice/native/advisory mapping PENDING_VERIFICATION |
| Microsoft VC DLLs | Python vcruntime140/vcruntime140_1 14.51.36247;Qt MSVCP140/MSVCP140_1/MSVCP140_2/VCRUNTIME assets;Python Windows additional conditions | Microsoft official redistributing-visual-cpp-files limits distribution to applicable licensed VS users/software terms/REDIST list. Python's shipped conditions explicitly address onward distribution but do not justify unrelated Qt/toolchain rights. Need exact applicable compiler/runtime EULA/REDIST and downstream protective terms;do not infer purchase requirement or free entitlement from marketing/version number | BLOCKED for complete redistribution mapping |
| PySide6/shiboken6 6.12 | Wheel METADATA alternatives,commercial-reference file;official pyside-setup v6.12 headers,README,LGPL3/GPL source | LGPL route candidate,not selected legal conclusion. Include LGPL3/GPL3 texts and notices;covered-library corresponding source including modifications/build scripts;preserve user modification/debugging rights and effective replacement/relink path as applicable. Commercial or GPL alternatives must be evaluated separately | Alternatives VERIFIED_DOCUMENTATION;fulfillment PENDING_VERIFICATION |
| QtCore/Gui/Widgets/qwindows | Exact wheel asset/import inventory;qtbase v6.12 headers/third-party attribution records | Identify exact compiled features/linked sources/plugin licensing,not entire wheel treated as uniformly LGPL. Shared DLLs alone do not prove LGPL4d1 replacement works;frozen loader/signed package restrictions require later proof. No blanket obligation to publish unrelated application source inferred under LGPL | PENDING_VERIFICATION |
| Qt third-party font/regex/image/compression | Qt v6.12 source qt_attribution.json and associated LICENSE files fetched for zlib,FreeType,HarfBuzz,PCRE2,libpng,libjpeg | Source declares zlib1.3.2 Zlib;FreeType2.14.3 FTL OR GPL2;HarfBuzz14.5.0 MIT;PCRE2 10.48 BSD3 with binary-like exception plusSLJIT;libpng1.6.58 Libpng AND libpng2;libjpeg-turbo3.2.0 IJG AND BSD3. Preserve exact notices/exceptions;FTL choice requires attribution per text. These source versions/optional configure paths are not proof of wheel build contents | Source terms VERIFIED_DOCUMENTATION;exact binary mapping PENDING_VERIFICATION |
| Python compression/parser/math components | Combined LICENSE bzip2/libffi/Zstandard/Apache2;CPython source defaults and modules;libffi-8/libtommath DLL inventory | Retain applicable bzip2 notice/nonmisrepresentation,MIT/BSD notices and disclaimers;map Expat/xz/zlib/mpdecimal and static-linked assets using exact binary/source-build evidence. libtommath v1.3.0 license fetched as reference only:actual bundled version not yet identified,no version substituted | PENDING_VERIFICATION |
| Pip26.2.1/vendor build support | MIT METADATA,22declared license files all present,43aggregate license-like paths | Maintain selected vendor MIT/BSD/Apache/MPL-style notices and scope-specific obligations;Python license cannot cover all. Include build environment inventory even if omitted from future client runtime;no deletion now | Text inventory VERIFIED_DOCUMENTATION;selected distribution subset PENDING_VERIFICATION |
| PyInstaller6.22.3/bootloader build support | Wheel COPYING and official tagged COPYING:GPL2-or-later with bootloader exception;hooks separate license | Preserve applicable tool notices,do not infer frozen application must be GPL solely from using bootloader exception. Exception scope/modifications/redistributed build-tool portions reviewed separately;one-directory is proposed for inspectable library replacement,not legal proof | VERIFIED_DOCUMENTATION;future packaging compliance pending |
| altgraph/pefile/pywin32-ctypes/packaging/setuptools/hooks | Previously verified exact wheel license/vendor inventory | Map LGPL/GPL exceptions to the correct hooks/code portion;MIT/BSD/Apache dual-license choices and setuptools vendors separately. Build-only role remains in manifest;do not bundle tool trees by default or claim removed assets | Existing text inventory verified;final role/obligations pending |
| Windows ICU/API-set/UCRT/system files | Microsoft ICU source and20API import matches;Windows system names in Python/Qt import tables | OS-supplied dependency,not arbitrary extra DLL acquisition. Actual servicing/version/catalog/loader checks on laptop needed;do not copy system DLLs into product | Documentary provider verified;native proof NOT_RUN |

### Practical LGPL candidate compliance plan
Propose minimal Qt Widgets shared-library lane,not approval. Keep covered Qt/PySide/shiboken DLLs and notices identifiable in one-directory layout;provide covered-library corresponding source or an applicable valid LGPL/GPL source conveyance method with exact version/modification/build correspondence. Merely linking a moving repository URL is not automatically sufficient. Identify LGPL section4 obligations for combined works,license copies/prominent notices,reverse engineering for debugging modified library,installation information if required,shared-library compatibility/replacement versus relinkable application object-code alternative. Do not put blanket no-reverse-engineering terms over covered rights. EULA/installer/signature policy must not prevent lawful replacement. Future replace-a-covered-library test verifies packaging mechanics,not a legal conclusion. Any GPL-only/noncompatible module/plugin must be excluded by approved feature profile or separately authorized license solution;no commercial license bought/selected here. Production redistribution acceptance remains separate from private feasibility approval.

### Qt plugin/transitive plan
Leading minimal profile: PySide bindings for QtCore/QtGui/QtWidgets,shiboken,Qt6Core/Gui/Widgets/platforms/qwindows and only explicitly required style/font/image resources. File-level exact manifest still pending;no bundle built. Recorded qwindows imports include UIAutomationCore,D3D9,COM/WinRT/MSVC/system DLLs;Gui adds DWrite/D3D11/D3D12/DXGI and MSVCP140_2;Core ICU/MSVCP140_1. This requires actual laptop loader/graphics/accessibility proof. Source attribution files describe optional bundled vs system dependencies;native imports miss statically linked code.

Exclude by proposal,not actual removal: designer tools,qmltooling/debug plugins,Qt Quick/WebEngine/PDF/virtualkeyboard,SQL-driver plugins,TLS/network plugins and unused image codecs. Python stdlib SQLite avoids Qt qsqlite;local minimal startup needs no TLS backend. Wheel includes such plugins;its broad presence is not permission to load all. Audit PyInstaller hook inclusion,qt.conf,plugin search paths,QT_PLUGIN_PATH/PYTHONPATH/PATH,hidden imports and optional DLL loads. Prevent user/project directories becoming plugin/source loading roots;no untrusted imported client executable plugins. After separately authorized packaging,record loaded-module paths and hashes plus selected/excluded plugin inventory,then validate no ambient installation fills gaps. Shared VC runtime choices must reconcile version compatibility between Python and Qt,not overwrite one package's DLL with another untested file.

### Exact authenticity verification methods — planned, not run
| Question | Official method / proposed command | Acceptance and limits |
| --- | --- | --- |
| Full NuGet signed ZIP | Microsoft NuGet CLI `nuget verify -All <exact.nupkg> -Verbosity detailed -NonInteractive -ConfigFile <reviewed isolated config>` or compatible existing SDK `dotnet nuget verify <exact.nupkg> --all --verbosity detailed --configfile <reviewed config>` | Valid package digest/signature,repository vs author classification,chain/EKU/timestamp and approved repository identity/fingerprint from independent official certificate source;all warnings resolved. Official dotnet docs say --all currently supports signatures only;do not claim broader tests. No .NET adoption implied by verification tool |
| Trusted signer policy | NuGet trustedSigners repository serviceIndex and certificate SHA256 fingerprint from current official source | Never use example fingerprints/copied package certificate as its own trust root;no allowUntrustedRoot/trust-store edits/signature disable. Unknown or rotating certificate investigated and approval recorded |
| Native embedded signature | Windows Get-AuthenticodeSignature / trusted installed SignTool `verify /pa /all /v <file>` | Capture status,actual signer,chain/timestamp/revocation and exit/error output;authenticity evidence for exact hash,not just parsed subject. Generic OpenSSL purpose-any chain check is insufficient for Authenticode/NuGet policy |
| Explicit catalogue | Existing SignTool `verify /pa /v /c <python.cat> <file>` and `verify /pa /v <python.cat>`;system files `verify /a /pa /v <file>` | Signed catalog plus matching member hash,valid policy. No catdb registration necessary/authorized;unregistered catalog may require explicit /c. PowerShell uses catalog signature when both types exist;NotSigned alone not a conclusion about Windows catalog coverage |
| Expected unsigned launchers/Qt assets | Existing wheel SHA256+RECORD/source-origin evidence,exact vendor signature behavior and documented risk/trust disposition | No fabricated signature pass and no automatic malware conclusion. Decide if that asset's provenance is sufficient before executing;unsigned exceptions explicit,not disabling mandatory checks |
| Windows OS dependencies | Built-in file/version/hash/Get-AuthenticodeSignature for exact System32 DLLs;servicing provenance if catalog-only | No third-party DLL retrieval/repair. If system file identity uncertain,stop native execution and obtain OS servicing evidence under separate authorization |

These commands are documentary proposals. Tools are not installed/assumed available. Existing cloud openssl/objdump/static parsers can read structures;NuGet full verifier and Windows policy verification prerequisites remain pending. Root/revocation fetches may require explicitly approved network,possibly update caches;fully disconnected verification reports missing revocation as unknown,not pass. Neither disabling AV/security policy nor enrolling ESU is authorized.

### Security advisory register and current review limits
Review date2026-10-11UTC. Official CPython v3.14.8 NEWS fetched:security fixes include CVE-2026-19445 ssl/SNI callback and CVE-2026-15806 urllib credential scheme scoping;release notes also address TLS-hostname validation,archive decompression/filter issues and bundled Expat2.8.5 update. This verifies published fix descriptions,not binary behavior,or absence of later vulnerabilities. No exhaustive no-CVE claim. Official OpenSSL/SQLite/Qt live advisory pages inaccessible via cloud403;record BLOCKED current advisory clearance. Wrong guessed SECURITY/source paths404 preserved then corrected CPython policy path;not interpreted as no security policy. Official policy directs PSRT/GitHub advisories.

| Surface / observed or conditional version | Required official review / applicability evidence | Current state |
| --- | --- | --- |
| CPython3.14.8 | PSRT/current GitHub advisories + later release notes;match affected ranges and enabled modules;fixed-release metadata vs vendor patch evidence | Release-fix documentation verified;complete current applicability OPEN |
| OpenSSL3.5.9 | OpenSSL official vulnerability/advisory index;3.5branch affected/fixed ranges and configuration;Python SSL and optional Qt TLS reviewed separately | Live primary page403;OPEN |
| SQLite3.50.4 | Official security/change logs,reported bugs vs exploitable exposure;compile options/extensions and untrusted DB input threat | Primary page403;OPEN |
| Qt6.12/PySide/shiboken + codecs/fonts | Qt security announcements/patch releases,source revision/SBOM linked versions/feature flags;reachable image/font/parsing/network code | Primary security page403,exact binary transitive versions pending;OPEN |
| VC14.51/Windows build19045 | Microsoft MSRC product/runtime bulletin and current Windows servicing/ESU conditions;never map DLL version alone to entitlement or patched OS | Exact maintenance/build revision missing;OPEN |
| pip/freezer/hooks/vendors | Official project/GitHub advisories,root and vendored ranges,build-vs-runtime reachability;malicious package supply chain and extraction behavior | All exact root pins known;full vendor versions/current advisory closure OPEN |

Future review records advisory ID/source/date,affected/fixed version,our version/hash/configuration,exposure,severity,mitigation/required update,owner disposition and next recheck. Missing review remains UNKNOWN. Do not close from an empty package-registry vulnerability array. A source-default component version is not an actual binary version. Unsupported OS security status remains separate from upstream runtime compatibility. No exploit/penetration test run.

### Static cloud versus physical Windows evidence
Cloud completed:hash preservation,archive/RECORD/native/import/text/licensing inventories,official verification procedure and source attribution analysis. Can further inspect verified binary strings/headers/complete selected source-license map without installation or executing artifacts. Cannot prove Windows loader/plugin/graphics/ACL/process recovery/resource/offline/installer behavior or Windows Authenticode policy from Linux. No redundant re-download planned.

Physical laptop target facts already supplied:Windows10HomeSingleLanguage22H2/build19045x64,i3-6006U,3.87GiB usable RAM,61.81GiB C free,Chrome/WebView versions,owner installation control. Do not recollect these. Exact servicing revision/security-support state and actual DLL/tool availability are remaining evidence,not a new hardware questionnaire. Python pinned docs sayWindows10+,Qt6.12 source targetWindows10>=1809x64;native VC/graphics/runtime target prerequisites still pending. Home EOS/owner no-security-updates notice does not prove native incompatibility and compatible runtimes do not cure OS security exposure. .NET10 mismatch remains conditional alternative rationale,not production decision.

### Proposed native evidence stages and approval bounds
Stage W0,next proposed task: owner read-only laptop verification readiness using built-in PowerShell. Inspect ICU system file signatures/versions and presence of NuGet/SDK/SignTool only;do not run tool versions or download/install them. Inspect approved exact package's local hash only if already available. If assets absent,record evidence-transfer prerequisite rather than re-download. This confirms available path,not runtime feasibility. No framework/runtime execution,code,unpack/system repair.

Stage W1,separate later explicit scope:transfer existing verified archives by an approved local method,compare hashes,stream only bounded approved data members to owned evidence directory,run trusted pre-existing signature verifiers. File extraction and certificate/revocation network/caches must be explicitly covered;no registration/trust-store edits. Native content is not executed. If tool unavailable,stop verification and propose precise separately approved tool acquisition,not production .NET adoption.

Stage W2,separate later explicit experimental scope after experiment-use provenance/license/advisory clearance:one Qt Widgets shell/one isolated worker/synthetic CSV/std-librarySQLite/artifact hashes/progress/cancel/interruption recovery/offline/measurement/portable packaging. One heavy process at a time,proposed memory/time/disk budgets from prerequisite plan;no client data/authorized live website/browser module/installer/OS changes. Actual startup/loaded DLL origins,plugin closure/graphics/accessibility,DB/artifact consistency,cancel/recovery and absent-network behavior recorded with command/environment/time/output/hash evidence. Build/fixture/experiments are NOT authorized by this plan. Resource targets remain PROPOSED.

Rollback for W0: no file/system modification intended;retain sanitized outputs. W1 owned evidence files only,retain failure evidence,never clean unrelated directories. W2 rollback disposal only approved owned experimental outputs;originals/backups/evidence preserved;terminate only identified owned processes. All failures pause affected scope;no repeated destructive retry or assumption of full worker sandbox.

### Installation approval assessment
**Current evidence does not support unconditional installation or executable experiment approval.** W0 readiness can be separately authorized now because it reads existing OS evidence and runs no downloaded software. It does not require production redistribution fulfillment. W1 trust verification may proceed only within explicit scope/tool prerequisites. Private W2 feasibility gate needs scoped provenance/license/advisory disposition and exact owner experiment approval,not final production architecture adoption. Full client distribution additionally requires final shipped manifest/notices/source/replaceability/release compliance evidence;do not unnecessarily treat a future production package as already built or approved.

### Objective blocker closing criteria
| Blocker | Closure evidence and approval | Current disposition |
| --- | --- | --- |
| B01 experimental scope/version tuple | Owner explicitly approves ONE complete bounded EXP-Q1(or alternative) tuple including NuGet distribution role,exact root/tool/runtime/native versions/hashes,files/commands/download/install limits,offline/native objectives,resource bounds,security/success/failure/rollback. Separate runtime framework/DB production ADR adoption. Approval of documentary plan/static download is insufficient | OPEN |
| B02 target/native route | Target facts retained;owner authorizes usable native route;required tool/artifact access established;actual approved target startup/module/worker/SQLite/artifact/cancel/recovery/offline/resource/packaging feasibility evidence passes or explicit blocking limitation disposition. W0/W1 success alone does not close runtime-proof condition | OPEN |
| B03 reviewed Git checkpoint | Existing docs/governance-baseline SHA15acfb58dfa9f9616b60b2c41c771953cbfc878c preserves approved P0–P4;no new checkpoint permission inferred | RESOLVED unchanged |
| B04 scope-appropriate distribution/provenance | Every selected experimental asset has exact identity/hash/source/native dependency/signature-or-approved-provenance evidence;applicable license/VC agreement/source/notices/Qt obligations identified with feasible experimental use;current advisories and target-support assessment disposed by responsible owner,none silently unknown. Before client redistribution additionally demonstrate selected packaged notice/source/replacement fulfillment and shipped manifest. Missing mandatory evidence blocks respective scope,not automatically closed by planning | OPEN |

P5 remains BLOCKED,8ADRsPROPOSED,all239application testsNOT_RUN,91requirements andP0–P4 documentary completion unchanged. Do not close project risks merely by documenting controls. Exactly one recommended next action: authorize saved W0 read-only Windows verification-readiness checkpoint. It addresses actual native access/tool/OS dependency uncertainty without repeating existing binary research or permitting installation/PoC.

### Clearance official source snapshots
| Key | Official URL | Result | SHA256 or access error |
| --- | --- | --- | --- |
| nuget-verify | https://raw.githubusercontent.com/NuGet/docs.microsoft.com-nuget/main/docs/reference/cli-reference/cli-ref-verify.md | FETCHED | 362b5f1d4d58df9052157aa8c3cd9ae66219f521b86e04c4c683c8591c4e5e3e |
| dotnet-verify | https://raw.githubusercontent.com/dotnet/docs/main/docs/core/tools/dotnet-nuget-verify.md | FETCHED | ad11690a80f78049d9c1ca5294fc2e3c0b4e1a417834e249ebe024beedc067de |
| nuget-signspec | https://raw.githubusercontent.com/NuGet/Home/dev/designs/PackageSignatures.md | UNAVAILABLE | HTTP Error 404: Not Found |
| signtool | https://raw.githubusercontent.com/MicrosoftDocs/win32/docs/desktop-src/SecCrypto/signtool.md | FETCHED | 17bee547ba6e87838cfd5a0f3c5f529e72e99869d7113e92f9b734e4d0a43171 |
| authenticode | https://raw.githubusercontent.com/MicrosoftDocs/PowerShell-Docs/main/reference/7.5/Microsoft.PowerShell.Security/Get-AuthenticodeSignature.md | FETCHED | 13dfc42c600a5e2c13a29086a8bd9a8aa9c7c4b318261c8deccbd9484115f9dd |
| openssl-license | https://raw.githubusercontent.com/openssl/openssl/openssl-3.5.9/LICENSE.txt | FETCHED | 7d5450cb2d142651b8afa315b5f238efc805dad827d91ba367d8516bc9d49e7a |
| openssl-notice | https://raw.githubusercontent.com/openssl/openssl/openssl-3.5.9/NOTICE | UNAVAILABLE | HTTP Error 404: Not Found |
| openssl-advisories | https://openssl-library.org/news/vulnerabilities/index.html | UNAVAILABLE | <urlopen error Tunnel connection failed: 403 Forbidden> |
| sqlite-copyright | https://www.sqlite.org/copyright.html | UNAVAILABLE | <urlopen error Tunnel connection failed: 403 Forbidden> |
| sqlite-security | https://www.sqlite.org/security.html | UNAVAILABLE | <urlopen error Tunnel connection failed: 403 Forbidden> |
| vc-redist | https://raw.githubusercontent.com/MicrosoftDocs/cpp-docs/main/docs/windows/redistributing-visual-cpp-files.md | FETCHED | 13a6c4e7c41971dc1a5e5856aa4ed5d606d3fd54b3c971f4ae758203e7b3b39e |
| vc-license | https://visualstudio.microsoft.com/license-terms/vs2026-cruntime/ | UNAVAILABLE | <urlopen error Tunnel connection failed: 403 Forbidden> |
| qt-security | https://www.qt.io/blog/tag/security | UNAVAILABLE | <urlopen error Tunnel connection failed: 403 Forbidden> |
| python-security | https://raw.githubusercontent.com/python/cpython/v3.14.8/SECURITY.md | UNAVAILABLE | HTTP Error 404: Not Found |
| qtbase-thirdparty | https://api.github.com/repos/qt/qtbase/git/trees/v6.12.0?recursive=1 | UNAVAILABLE | <urlopen error Tunnel connection failed: 403 Forbidden> |
| qtimage-thirdparty | https://api.github.com/repos/qt/qtimageformats/git/trees/v6.12.0?recursive=1 | UNAVAILABLE | <urlopen error Tunnel connection failed: 403 Forbidden> |
| libtommath-license | https://raw.githubusercontent.com/libtom/libtommath/v1.3.0/LICENSE | FETCHED | 2fa64b163659f41965c9815882a8296d3d03ff546b76153e11445f9bdecf955a |
| pyinstaller-license | https://raw.githubusercontent.com/pyinstaller/pyinstaller/v6.22.3/COPYING.txt | FETCHED | 0598064c7d2718e38d7914a7d08343b2fa008e3bea9ebba2aa7a6ffa5900dd64 |
| python-news | https://raw.githubusercontent.com/python/cpython/v3.14.8/Misc/NEWS.d/3.14.8.rst | FETCHED | 39c47ab66955ae683f26f9a6d227e1f1977f1913ea58fe9a898fe4d906c70f5a |
| python-security-policy | https://raw.githubusercontent.com/python/cpython/main/.github/SECURITY.md | FETCHED | 5267143fb08ba1efd2d2555f0c6c1b7b67db82c4736b49e7e38bef0d67b1cc82 |
| sqlite-readme | https://raw.githubusercontent.com/sqlite/sqlite/version-3.50.4/README.md | FETCHED | 5aad961283581e5f1196d5b560c96b0b5aa111092233015dd89f05c101fc5a83 |
| sqlite-license | https://raw.githubusercontent.com/sqlite/sqlite/version-3.50.4/LICENSE.md | FETCHED | a7a58d6022c090c528e3167026167b3141d682efc6a3c188b473ba59f1788fc7 |
| qt-zlib | https://raw.githubusercontent.com/qt/qtbase/v6.12.0/src/3rdparty/zlib/qt_attribution.json | FETCHED | 0346805e9c4048316dbc7c58d560a20c12482ea0218de264282212e9619b6d64 |
| qt-freetype | https://raw.githubusercontent.com/qt/qtbase/v6.12.0/src/3rdparty/freetype/qt_attribution.json | FETCHED | 628b68bf60eb3bc1616342bc3545b63be2392e78bbebbc4c19f49675dd2ac8a7 |
| qt-harfbuzz | https://raw.githubusercontent.com/qt/qtbase/v6.12.0/src/3rdparty/harfbuzz-ng/qt_attribution.json | FETCHED | b869a7f186e4cfc00cc979e7c4ffd369d823f7a0a94b951a6aedb9b3278c8419 |
| qt-pcre | https://raw.githubusercontent.com/qt/qtbase/v6.12.0/src/3rdparty/pcre2/qt_attribution.json | FETCHED | c65e311b057e3ecb8ee9aeddd681add5aa4484485e265d3a6a8e7967abc19948 |
| qt-libpng | https://raw.githubusercontent.com/qt/qtbase/v6.12.0/src/3rdparty/libpng/qt_attribution.json | FETCHED | a43ff8e146c949f7cd14e00bd681f4957e27def06ecafec55ccc7231c451d3fa |
| qt-libjpeg | https://raw.githubusercontent.com/qt/qtbase/v6.12.0/src/3rdparty/libjpeg/qt_attribution.json | FETCHED | ed7cb7abdd9124f664acd26cf552ba821c8cf236c4cd34a6737f202215bd41bc |
| openssl-web | https://raw.githubusercontent.com/openssl/web/master/data/vulnerabilities.xml | UNAVAILABLE | HTTP Error 404: Not Found |
| qt-ft-license | https://raw.githubusercontent.com/qt/qtbase/v6.12.0/src/3rdparty/freetype/LICENSE.txt | FETCHED | bf543cdda11864477b8d2ca2aa9afc2aaa8f9133461b4d962ed6ec73646256a1 |
| qt-hb-license | https://raw.githubusercontent.com/qt/qtbase/v6.12.0/src/3rdparty/harfbuzz-ng/COPYING | FETCHED | ba8f810f2455c2f08e2d56bb49b72f37fcf68f1f4fade38977cfd7372050ad64 |
| qt-pcre-license | https://raw.githubusercontent.com/qt/qtbase/v6.12.0/src/3rdparty/pcre2/LICENCE.md | FETCHED | 197d8a73ffee0d6b09adba2f9c677b5f5aede24edf89258a68e48248d010d811 |
| qt-zlib-license | https://raw.githubusercontent.com/qt/qtbase/v6.12.0/src/3rdparty/zlib/LICENSE | FETCHED | d7e3139972874dc8abdbbfce27ec1e6f942b28279dd7d27453630a8b4610e080 |
| qt-png-license | https://raw.githubusercontent.com/qt/qtbase/v6.12.0/src/3rdparty/libpng/LICENSE | FETCHED | bdb0a645ea18c60507d0368379b1ac5474b92255fcc2d115e07486a7672ba526 |
| qt-jpeg-license | https://raw.githubusercontent.com/qt/qtbase/v6.12.0/src/3rdparty/libjpeg/LICENSE | FETCHED | ba6bceebcba0fdd35488477c2cca8c4632ce82c74dbfbc87d886ce6fc4433579 |
| nuget-signed | https://raw.githubusercontent.com/dotnet/docs/main/docs/core/tools/nuget-signed-package-verification.md | FETCHED | 7a757b87ba68f9ee9a124414eccd7bae01576f2a52dbf3bd7ea4181124368e9a |
| nuget-trust | https://raw.githubusercontent.com/NuGet/docs.microsoft.com-nuget/main/docs/reference/nuget-config-file.md | FETCHED | c4730088c48f40a23f8467e149efe99b97df95adc9398661f720aaa88ad59712 |

### Consumed distribution-clearance prompt — documentary scope only
```text
# P5 distribution clearance and native-verification approval package

PROJECT: Freelance Automation Studio
ROLE: Dependency/licensing reviewer, Windows security architect and QA lead.
MODE: DOCUMENTATION-ONLY. Requires explicit owner authorization of this next task. Do not execute automatically.

CONTEXT: One official Python3.14.8 x64 NuGet package verified at15,554,015bytes against official SHA512. Local SHA256 ce85f674d9a63029f709cbff7a3da1c6bc5bfcfaefdd9999f98fa0290470c454. Static archive/native/license inventory recorded;no installation or execution. Nine Qt/freezer wheels already verified. NuGet CMS/host-chain checks are partial evidence,not full NuGet ZIP-policy or native Authenticode verification. P5BLOCKED,B01/B02/B04OPEN,B03RESOLVED,eightADRsPROPOSED,239testsNOT_RUN.

CHECKPOINT: Read AGENTS;master,architecture,development,testing,security,release/execution books;P5 decision package/prerequisites/experiment matrix/MS-0006 report;all eight ADRs and current prompt. Verify docs/governance-baseline HEAD15acfb58dfa9f9616b60b2c41c771953cbfc878c,ten pending documentation paths and empty index. Preserve historical and unrelated work. Stop if evidence artifacts are missing or hash-invalid;do not redownload binaries automatically.

OBJECTIVE: Prepare the concrete remaining distribution/provenance clearance and native-verification scope needed before a bounded P5 experiment can be proposed. No final technology adoption or silent tuple change.

DELIVERABLES:
1. Map the exact minimal Python/Qt/freezer runtime assets to authoritative license/notices/copyright/source/replacement obligations. Distinguish build-only pip/freezer/vendor tools from proposed shipped files;do not remove files. Investigate VC14.51 Microsoft Distributable Code rights and downstream terms,OpenSSL3.5.9/SQLite3.50.4/libffi/libtommath/compression/parser/vendor obligations,Qt LGPL source/replaceability and PyInstaller exceptions. Use official text only and existing verified archives. Unknown applicable terms remain adoption blockers.
2. Review authoritative current advisories for exact observed versions;record dates/applicability/unknown patch status without claiming empty vulnerability results prove safety.
3. Define full NuGet signature/trusted repository policy/package-hash validation and native Authenticode/catalog/chain/timestamp/revocation verification methods. Existing tools may perform further static inspection only;do not install tools or change trust stores. Distinguish certificate subjects from verified publisher identity.
4. Prepare ONE bounded owner approval package for the next native verification step,including exact existing artifacts/tool prerequisites,read-only versus executable actions,files/commands,network destinations,permissions,resource bounds,evidence,stop/failure/rollback conditions. Hardware facts already recorded;do not request them again. If prerequisites are missing,offer a precise evidence-recovery gate rather than prematurely authorizing PoC. Linux evidence cannot prove the Windows10 Home22H2 laptop works. Preserve OS security-maintenance risk.

AUTHORIZED FILES: Update existing P5 decision package,prerequisites plan,planned experiment matrix,MS-0006 report,execution book,current-next-prompt only. Keep original history,requirements/ADRs/test evidence intact. No new implementation directories.

RESTRICTIONS: No new binaries/installers/packages or inspection-tool downloads,no installation,no downloaded code execution/import,no Python/Qt/native/PoC experiments,no application/prototype code,no Windows/system/trust-store changes,no ADR approval,no Git stage/commit/push/merge/reset/clean,deployment or P6. Official text/metadata retrieval and static inspection using already available trusted tools permitted.

CHECKS: Exact scope/protected hashes,links/anchors/formatting,identifier and blocker/ADR/test states;actual documentation/static results and missing evidence separately. Keep P5BLOCKED,B01/B02/B04OPEN unless their specific conditions genuinely met,B03RESOLVED,eightADRsPROPOSED,all239application testsNOT_RUN. Never treat documentation as native compatibility or complete license/security proof.

FINAL: Baseline/files;asset/obligation/advisory map;signature evidence gaps;precise proposed native-verification approval package;documentation check results;blocker states;exactly ONE next recommended action. Save exactly ONE complete approval-gated next prompt addressing actual remaining prerequisites;do not execute it. Stop for owner review.
```

## Authorized W0 preparation checkpoint — 2026-10-12 UTC
Owner authorizes the saved read-only Windows verification-readiness prompt and documentation scope;authorization persists and is not requested again. Actual environment reports Linux. No owner laptop connection or new Windows results supplied;native W0 commands remain NOT_RUN awaiting owner-side evidence. Branch docs/governance-baseline / HEAD15acfb58dfa9f9616b60b2c41c771953cbfc878c,ten pending documentation paths,empty index match expected checkpoint. Prior work/history preserved.

Candidate reconciliation: ADR-0002 remains PROPOSED;initial .NET10/WPF preference was conditional on vendor-listed exact target,not adoption. Later supplied Windows10Home22H2 target was absent from reviewed.NET10 support table;Python3.14.8/PySide6.12/PyInstaller6.22.3 investigation is an explicit alternative,not an approved language/framework/provider switch. Existing stdlib SQLite observations do not approve production DB selection. Neither candidate approved;no ADR/history rewritten.

Prepared one copyable PowerShell block for existing verifier PATH availability and eight Windows system-DLL metadata/hash/Authenticode observations. Tools are discovered,not invoked. Sysnative handles32-bit-shell redirection on64-bitOS;Format-List avoids hash/signature truncation;per-file error/missing states sanitized and preserved. FoundOnPATH=false means no PATH-resolved command,not proof no tool is installed. Commands create no files/install/repair/configuration or package transfer/unpack;signature trust evaluation may use Windows network/cache services and is not a full offline revocation proof. No administrator or specific repository directory required;running built-in read-only commands from Toolzenhub does not modify that repository. No personal paths/accounts/identifiers requested.

Native system-file/hash/signature/tool results currently unavailable. NotSigned/UnknownError does not prove a system DLL is malicious or absent from catalog coverage;future catalogue/servicing check may be required. This block does not inspect/run Python/Qt or validate the NuGet package. Optional local package hash check deferred because owner has supplied no specific existing file location;no personal-directory search/download/transfer assumed.

P5BLOCKED;B01/B02/B04OPEN,B03RESOLVED,eightADRsPROPOSED,all239application testsNOT_RUN;91requirements/P0–P4 documentary completion preserved. W0 prepared,not completed;B02 approved-guidance subcondition progressed but required actual route/proof unmet. Exactly one next action:run the supplied block in Windows PowerShell on the laptop and return its output for evidence review. Saved next prompt reviews those outputs only;no installation/W1/W2/P6 or approval of candidate architecture.

### Authorized owner-side W0 commands — NOT_RUN here
```powershell
# Run in Windows PowerShell on your laptop; no administrator needed.
'=== VERIFICATION TOOLS (NOT EXECUTED) ==='
$toolResults = foreach ($tool in @('dotnet', 'nuget', 'signtool')) {
    $found = Get-Command -Name $tool -CommandType Application -ErrorAction SilentlyContinue
    [pscustomobject]@{ Tool = $tool; FoundOnPATH = [bool]$found }
}
$toolResults | Format-Table -AutoSize

# Sysnative avoids reading 32-bit DLLs from a 32-bit PowerShell process.
$systemFolder = 'System32'
if ([Environment]::Is64BitOperatingSystem -and -not [Environment]::Is64BitProcess) {
    $systemFolder = 'Sysnative'
}
$systemPath = Join-Path $env:SystemRoot $systemFolder
'=== SYSTEM DLL EVIDENCE ==='
foreach ($dll in @('icuuc.dll', 'icuin.dll', 'ucrtbase.dll', 'dwrite.dll',
                   'd3d11.dll', 'd3d12.dll', 'dxgi.dll', 'UIAutomationCore.dll')) {
    $dllPath = Join-Path $systemPath $dll
    try {
        if (-not (Test-Path -LiteralPath $dllPath -PathType Leaf)) {
            [pscustomobject]@{ File = $dll; Result = 'MISSING' } | Format-List
            continue
        }
        $file = Get-Item -LiteralPath $dllPath -ErrorAction Stop
        $hash = Get-FileHash -LiteralPath $dllPath -Algorithm SHA256 -ErrorAction Stop
        $signature = Get-AuthenticodeSignature -LiteralPath $dllPath -ErrorAction Stop
        [pscustomobject]@{
            File = $dll
            Version = $file.VersionInfo.FileVersion
            Bytes = $file.Length
            SHA256 = $hash.Hash
            SignatureStatus = [string]$signature.Status
            Signer = $signature.SignerCertificate.Subject
        } | Format-List
    } catch {
        [pscustomobject]@{
            File = $dll
            Result = 'CHECK_ERROR'
            ErrorType = $_.Exception.GetType().Name
        } | Format-List
    }
}
```

### Consumed W0 prompt — preparation authorized, laptop evidence pending
```text
# P5 W0 — owner-side read-only Windows verification readiness

PROJECT: Freelance Automation Studio
ROLE: Windows security/dependency verification and QA lead.
MODE: READ-ONLY LAPTOP CHECK + DOCUMENTATION. Requires explicit owner authorization before execution. Do not start automatically.

CONTEXT: P5BLOCKED;B01/B02/B04OPEN,B03RESOLVED. Existing official Python3.14.8 x64 NuGet artifact size15,554,015bytes/SHA512 verified;local SHA256 ce85f674d9a63029f709cbff7a3da1c6bc5bfcfaefdd9999f98fa0290470c454. Nine Qt/freezer wheels already verified. Full NuGet/Authenticode trust,VC/Qt redistribution and current advisory closure remain pending. P5 decision package contains component evidence map,official methods and W0/W1/W2 staged plan. No stack adopted;8ADRsPROPOSED;all239application testsNOT_RUN.

REPOSITORY CHECKPOINT: Read AGENTS/master/architecture/development/testing/security/release/execution books,P5 decision package/prerequisite plan/experiment matrix/MS-0006 report,current prompt. Verify docs/governance-baseline HEAD15acfb58dfa9f9616b60b2c41c771953cbfc878c,ten pending documentation paths and empty index. Preserve existing/historical/unrelated work. Do not repeat verified downloads/ZIP inspections or create worktrees.

OWNER TARGET: Already supplied Windows10HomeSingleLanguage22H2/build19045x64,i3-6006U,3.87GiBusableRAM,61.81GiBCfree,personal installation control/browser/WebView facts. Do not request these again. Cloud Linux is not laptop access.

SCOPE W0 ONLY:
1. On the owner's physical laptop,inspect availability of existing trusted verification tools without running them;inspect ICU/UCRT/graphics/accessibility system files using built-in PowerShell metadata/hash/Authenticode queries. No repair/trust-store/catalog registration or system setting changes.
2. If exact package already exists locally and owner supplies its specific path,read its size/SHA512/SHA256 only;do not transfer,download,unpack or execute any package automatically. Absence is a transfer prerequisite,not permission to fetch a replacement.
3. Record sanitized actual outputs and verification route availability. Tool presence is not proof it is trusted/compatible;do not invoke discovered executables until separately reviewed/authorized. Missing tool is a precise prerequisite;do not install it.

READ-ONLY OWNER COMMANDS (documentation until explicitly authorized and run on Windows):
```powershell
'Trusted verification tool availability (no tool execution)'
foreach ($name in @('dotnet','nuget','signtool')) {
    $cmd = Get-Command -Name $name -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1
    [pscustomobject]@{ Tool = $name; Found = [bool]$cmd }
}
'System DLL evidence'
foreach ($name in @('icuuc.dll','icuin.dll','ucrtbase.dll','dwrite.dll','d3d11.dll','d3d12.dll','dxgi.dll','UIAutomationCore.dll')) {
    $path = Join-Path (Join-Path $env:SystemRoot 'System32') $name
    if (Test-Path -LiteralPath $path -PathType Leaf) {
        $file = Get-Item -LiteralPath $path
        $sig = Get-AuthenticodeSignature -LiteralPath $path
        [pscustomobject]@{
            File = $name
            Version = $file.VersionInfo.FileVersion
            Size = $file.Length
            SHA256 = (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash
            SignatureStatus = [string]$sig.Status
            Signer = $sig.SignerCertificate.Subject
        }
    } else {
        [pscustomobject]@{ File = $name; Status = 'MISSING' }
    }
}
```
Do not output secrets,serial numbers,product keys,account names or full personal paths. Commands may use Windows trust services/caches for signature evaluation;record offline/revocation limitations. They execute existing built-in PowerShell operations only,not the downloaded Python/Qt package. If no native connection exists,provide this exact guide to the owner and await actual output;never simulate it. Do not recollect hardware.

OPTIONAL EXACT LOCAL PACKAGE: Only after owner identifies an existing local file,read Get-Item length and Get-FileHash SHA512/SHA256;compare to official SHA512 from recorded evidence (PowerShell returns hex,official hash is base64—convert the digest representation correctly). Local SHA256 above identifies exact bytes. Do not infer trust from filename or hash alone. Do not invent or search arbitrary personal paths.

EVIDENCE CLASSIFICATION: Valid signature status is evidence for this file/policy/environment,not package execution or complete release clearance. NotSigned/UnknownError/revocation unavailable for a system file may need catalogue/servicing verification;do not label malware automatically. Full NuGet signed ZIP/trusted repository certificate verification,explicit Python catalogue membership and native PE policy tests remain W1. Worker/startup/SQLite/cancellation/recovery/offline/resources/packaging remain W2 and NOT_RUN. W0 does not close B02 native runtime-proof condition.

DOCUMENTATION DELIVERABLES: Update only existing P5 decision package,prerequisites plan,experiment matrix,MS-0006 report,execution book,current-next-prompt. Record which commands actually ran,outputs/environment/missing evidence,tool-route availability,system-dependency disposition and exact W1 prerequisite. Preserve histories;no new requirement/ADR/TEST IDs without register check.

RESTRICTIONS: No new binary/software downloads,installation,unpack/transfer of packages,execution of downloaded binaries/scripts/hooks,verification-tool execution,Python/Qt/PoC/native experiments,application code,Windows configuration/repair/trust changes,ADR approval,Git staging/commit/push/merge/reset/clean,deployment or P6. Official text retrieval remains allowed for interpretation;do not turn this into repeated broad research.

ACCEPTANCE: Actual owner-side W0 outputs or honestly recorded missing-native-access BLOCKED result;no fabricated PASS. Clearly establish available tool/artifact/system-file route and unresolved conditions. Check links/anchors/identifiers/status/scope/protected hashes/whitespace;all8ADRsPROPOSED,239testsNOT_RUN;P5BLOCKED,B03RESOLVED,B01/B02/B04OPEN unless their specific full criteria independently met. Do not grant installation approval.

FINAL: Repository baseline,owner-side checks actually run,tool/system/package evidence,trust limitations,remaining W1 prerequisites,documentation check results,blocker states and exactly ONE next recommended action. Save one complete approval-gated next prompt addressing the actual prerequisite;do not execute it. Stop for owner review.
```

## Authorized portable-core implementation — 2026-10-12 UTC
Owner correction P5 EXECUTION MODE AND START CODING explicitly authorizes source/fixtures/standard-library execution/tests in cloud. This supersedes W0/read-only restrictions for this bounded core task only. No Windows DLL inventory,PowerShell check,Qt/.NET installation or further prerequisite package was required or performed before development. Current host CPython3.12.14 / sqlite3 runtime3.53.1 / Linux used;the downloaded Python3.14.8/Qt artifacts were NOT installed or executed. Neither production candidate or ADR adopted.

Starting repository docs/governance-baseline HEAD15acfb58dfa9f9616b60b2c41c771953cbfc878c,ten existing pending documentation paths/empty index. All unrelated uncommitted docs/archives preserved. New source isolated under experiments/p5_portable_core;runtime DB/input snapshots/outputs remain outside repository. Compact four-table prototype intentionally co-locates application/persistence/CSV adapter responsibilities;not a production layout or implementation of the33-entity architecture. This temporary experimental scope exception is owner-authorized and must not be silently promoted into P6.

### Executed deliverables
Runnable entry `python -m experiments.p5_portable_core`;Engine SQLite jobs/attempts/artifacts/events;create/run/process/show/cancel/verify/recover commands;synthetic fixture;UTF8/CSV header/row/size validation;exact first-occurrence duplicate removal;original-preserving hashed snapshot;unique staged output and exclusive publication;input/output SHA256;JSON progress;durable cooperative cancellation;structured errors;explicit retry history;restart reconciliation with quarantined uncertain artifacts. OS locks serialize execution/recovery and release after actual process exit. Processing/validation/review remain distinct;successful output is never delivery-approved.

### Actual executed evidence
Command:
`PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s experiments/p5_portable_core/tests -v`

Final run:29tests,29PASS,0FAIL,0SKIPPED,exit0,0.991s.26CoreTests+3CLIIntegrationTests. Initial26 and intermediate28passing runs are historical;added cross-process cancellation/single-command CLI/collision assertions and completion-report boundary refinement justify final rerun. Tests use synthetic temporary data and real subprocess CLI;actual worker process terminates with exit17,lock releases,recovery records INTERRUPTED,explicit retry succeeds. Other tests cover malformed/header/UTF8/boundary input,quoted unicode/multiline,original preservation,snapshot/output tampering,storage failure,deterministic checksums,DB integrity and no-output-overwrite. No assertions removed to pass;terminal reporting callback cannot retroactively relabel committed execution.

Executed sample:
`PYTHONDONTWRITEBYTECODE=1 python -m experiments.p5_portable_core --workspace /tmp/fas-p5-executed-demo process experiments/p5_portable_core/fixtures/duplicates.csv`

Result exit0:job `908a8bd44b2c42a6b4687b1fe23067a2`,5input records,3output records,2exact duplicates removed;stateREVIEW_REQUIRED,processingSUCCEEDED,validationPASSED,reviewPENDING,delivery_approved=false. Original fixture checksum matches saved input hash. Output path `/tmp/fas-p5-executed-demo/jobs/908a8bd44b2c42a6b4687b1fe23067a2/attempts/c3f6f41abc6447739d6f18423b5658d7/output.csv`;SHA256 `e564c77254e2d216b76bafa363bdf7cd9fac160e829bce417a7351c907e91ab6`;output contents:

```csv
id,name
1,Ada
2,Lin
3,Sam
```

Actual CLI verify command on that job returned exit0,artifacts_verified1,delivery_approvedfalse. SQLite constraints/PRAGMA integrity_check and foreign_key_check exercised in automated tests. Test duration is execution evidence,not a performance benchmark. Live /tmp output/logs are ephemeral;hash/results recorded here do not imply durable binary checkpoint.

### Authorization, milestone and limitations
Portable-core subtask READY_FOR_REVIEW with actual source/tests/demo evidence;not human-approved or complete P5. P5 remains BLOCKED for remaining overall/native/distribution scope. B01 bounded portable-core authorization SATISFIED by this message;earlier Python3.14.8/Qt EXP-Q1 tuple remains OPEN/unapproved. B02WindowsGUI/native/installer proof OPEN;B04provenance/license/current-advisory clearance for distributed/native candidate OPEN;B03RESOLVED unchanged. All8ADRsPROPOSED. Existing239full-product acceptance definitions retain NOT_RUN;29executed prototype tests are distinct partial evidence,not acceptance of those larger product cases. No requirement scope changed/no new TESTidentifier allocated;qualified unittest names and existing requirement references below supply experimental traceability.

Limits:trusted local workspace,hard-link filesystem required;same-user attack/symlink race confinement not proven. Dedup set bounded by experimental32MiB/100krow limits,not measured capacity;progress persistence per row may be slow. CSV formula values preserved literally,not safe client spreadsheet export. Partial snapshot creation may leave unregistered evidence;DB/storage failure can prevent failure-state persistence. File fsync/process crash tests do not prove physical power-loss/directory durability. Windows msvcrt branch,GUI/installer/full approval/export modules NOT_RUN. No Qt/.NET install,network dependency/new package download,Git stage/commit/push/merge or P6.

Exactly one next action:review the runnable portable-core result and approve a bounded P5 crash-consistency follow-up if acceptable. Saved next prompt stays within P5 core and cannot require Windows inventories as a prerequisite or silently adopt production architecture.

## P5 portable-core crash consistency — executed 2026-10-12 UTC
Owner authorizes implementation/automated testing of existing portable core,not a renewed prerequisite review. Before edits read AGENTS/saved prompt/relevant P5 report/source,verified branch docs/governance-baseline HEAD15acfb58dfa9f9616b60b2c41c771953cbfc878c,eleven pending Git paths and preserved existing uncommitted documentation/source. Baseline focused suite29PASS,0FAIL,exit0. Existing Python3.12.14/sqlite3.53.1/Linux;no downloads/installation/Qt/.NET.

### A — Source changes
Engine records staging/final paths before writes and migrates prototype schema1to2 additively;unsupported versions reject. POSIX directory fsync complements existing staged-file fsync/exclusive hard-link publication. Terminal outcome/job state/artifact eligibility commit atomically in SQLite,including final cancellation check. Attempts already terminal cannot be relabeled failed because an acknowledgement/reporting operation failed. DB/filesystem are still separate commit domains.

Recovery records actual staging/final presence,hash,size and integrity states in durable JSON;partial bytes from interruptions/failed/cancelled writes become QUARANTINED evidence. Completed verified output missing/tampered/unreadable loses eligibility,validation fails,job becomes REVISION_REQUIRED. Interrupted attempts become INTERRUPTED without inferred success/approval. Repeated recovery is idempotent for reconciled attempts/artifacts/events. Recovery storage/path errors are structured;CLIexit3 indicates reconciliation found issues requiring review. No cleanup/removal of uncertain evidence or overwriting existing outputs.

Modified:experiments/p5_portable_core/core.py,__main__.py,README.md. Added:tests/test_crash_consistency.py. Original29test source/fixtures/init files preserved byte-for-byte;no production33entityschema/GUI/architecture adoption.

### B/C/D — Added tests, exact commands and actual results
New21unittest methods preserve original29unchanged. Seven subprocess checkpoints use os._exit(23),not sleeps:attempt_started,row_written,staging_written,artifact_prepared,output_published,before_terminal_commit,terminal_committed. Additional tests:write/fsync/disk and terminalDB failures;recovery rollback/error;missing/tampered/unreadable artifacts;unsafe managed paths;three finalization cancellation subcases;post-commit lost-response guard;schema1migration/unknown-version rejection;CLIreview-exit status;repeat recovery and original hashes.

Commands actually executed:
```bash
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s experiments/p5_portable_core/tests -v
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s experiments/p5_portable_core/tests -p test_crash_consistency.py -v
```
First command baseline29PASS;first implementation45PASS;targeted new21PASS after additions;final complete suite50PASS(29original+21new),0FAIL,0SKIPPED,exit0,1.383s. No tests removed or bypassed;test duration not a benchmark. Error/termination cases are expected asserted behavior,not skipped or hidden failures. Syntax review with Pythonast PASS. Windows/GUI/installer/physicalpowerloss testsNOT_RUN.

### E — Separate real recovery evidence
An inline trusted Python demo created a synthetic job and invoked this child process body with workspace/job arguments:
```python
import os, sys
from experiments.p5_portable_core.core import Engine
hook = lambda point, context: os._exit(23) if point == 'output_published' else None
Engine(sys.argv[1], fault_hook=hook).run(sys.argv[2])
```
Parent used subprocess.run(...,timeout=10),asserted exit23,called engine.recover(),inspected job,and called recover()again. Artifact evidence directory:`/tmp/fas-p5-crash-demo-1ouixuv5`;job:`8c14cbb480ca4e4fa09b3a21652f7b8a`. First recovery interrupted_attempts1;second0,invalidated0,partial_evidence0,no additional change. JobINTERRUPTED,artifactQUARANTINED,staging/finalMATCH,size26bytes,sha256`e564c77254e2d216b76bafa363bdf7cd9fac160e829bce417a7351c907e91ab6`. Original fixture before/after sha256`14b1157b0d5e754704c328a91b187f4ca00427166c4598617f40ce07e169031d`;delivery_approvedfalse. Matched bytes are evidence,not sufficient proof to promote an interrupted attempt. JSON/demofiles remain outside repo at /tmp/fas-p5-crash-demo-result.json;ephemeral cloud data,not a durable Gitcheckpoint.

### F/G/H — Limits, Git and next action
Process failure and simulated write/DB/fsync failures verified;actual devicepowerloss/Windowsflush/locking branch/storage hardware durability not proven. Trusted local workspace/hard-link filesystem required;same-user TOCTOU/sandbox,unregistered snapshot creation and corruptDBrepair still outside this bounded task. Quarantined artifacts are never automatically reinstated;manual review/correction or explicit retry is needed. Older attempts with unrecorded paths may have incomplete evidence. No liveclientdata/AI/externalAPI dependency.

Source crash-consistency subtask READY_FOR_REVIEW only. OverallP5BLOCKED,B02WindowsGUI/native/installer proofOPEN,B04distribution/provenance/licensingOPEN,B03RESOLVED;B01thisboundedcore permission satisfied,earlierQt/native tuple still unapproved. EightADRsPROPOSED;239original product acceptance definitionsNOT_RUN are separate from50actuallyexecutedprototype tests. No P6,Gitstage/commit/push/merge/reset/clean or production approval. CurrentGitbaseline unchanged,elevenpendingpaths;existingchanges preserved.

Exactly one next recommended action:review this crash-consistent executable baseline and approve saved bounded P5 workload/resource verification. No Windows prerequisite inventory is required for that cloud-core follow-up;it must not imply final product performance or native compatibility.

### Consumed crash-consistency prompt — executed scope, overall P5 still blocked
```text
# P5 portable-core crash-consistency follow-up — approval gated

PROJECT: Freelance Automation Studio
ROLE: Senior Python reliability engineer and QA architect.
MODE: Bounded P5 experimental source/tests. Begin only after owner explicitly approves this follow-up;do not execute automatically. No Windows inventory/precondition required for cloud core development.

CONTEXT: Owner2026-10-12 authorized portable stdlib prototype. Existing CPython3.12.14/Linux/sqlite3.53.1 used,no installation. experiments/p5_portable_core implements SQLite jobs/attempts/events/artifacts,CSV validation/exact dedup/snapshots/checksums/progress/cancel/recovery/CLI;29tests passed,real5-to3CSVdemo verified. Portable core READY_FOR_REVIEW;overallP5BLOCKED,B02/B04OPEN,B03RESOLVED. B01portable scope satisfied,Qt/native tuple unapproved.8ADRsPROPOSED;239original product acceptance casesNOT_RUN. Both native candidates remain proposals.

CHECKPOINT: Read AGENTS/master/development/code-organization/testing/security/execution books,current prompt,P5report/matrix/decision package,and prototype README/source/tests. Verify docs/governance-baseline HEAD15acfb58dfa9f9616b60b2c41c771953cbfc878c;preserve all dirty docs/experiments. Inspect actual status rather than assuming a clean checkout. No commits/pushes/merges/reset/clean.

BOUNDED OBJECTIVE: Strengthen remaining publication crash consistency in the existing portable experiment. Cover actual process interruption after publication but before terminal DB commit;verify uncertain outputs remain quarantined and prior attempts/evidence intact. Test cancellation races at finalization and failure to persist terminal storage state. Inspect schema-version mismatch handling and unregistered snapshot evidence;implement only small necessary core fixes. Do not introduce GUI,installer,additional modules,deployment,third-party libraries or production33-entity schema.

DELIVERABLES: Modify existing experiments/p5_portable_core source/tests/README and related existing P5 evidence as necessary. Use synthetic fixtures/temp workspaces. Add meaningful behavior/fault tests rather than mirrored implementation assertions. Record exact commands/environment/counts/results/output hashes;preserve original input and old attempt data. Update AGENTS/current execution boundary only if authorization/state changes require it.

CHECKS: Run targeted new cases and existing portable suite once after changes;realCLIregression and SQLite/artifact consistency as risk warrants. Documentationlinks/identifiers/protected scope/gitdiff check. Original239 product acceptance cases remainNOT_RUN unless their actual complete procedures are run;new prototype evidence is explicitly scoped. Do not assert Windows locking/GUI/installer/offline-egress/performance/security proof from Linux tests.

RESTRICTIONS: No software downloads/installations,Qt/.NET/native experiments,realclientdata,productionADRapproval,Gitstage/commit/push/merge/reset/clean,deployment orP6. Only existing Pythonstandardlibrary and approved prototype code execution. Preserve unrelated work;cleanup only owned disposable test workspaces.

ACCEPTANCE: Crash/cancel/storage faults produce accurate durable state or explicit unresolved interruption,never false success/delivery approval;input/output integrity and attempt history preserved;actual relevant tests pass or blockers honestly recorded. OverallP5remainsBLOCKED until remaining native/distribution gate genuinely satisfied;core completion does not closeB02/B04.

FINAL: Baseline/files/codechanges;actual executable command/demo;test results;fault/recovery evidence;remaining limits/risks;milestone/ADR/blocker states;exactlyONE next action. SaveONE complete gated next prompt;do not execute it. Stop for owner review.
```
