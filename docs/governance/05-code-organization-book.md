# Code organization book

Status: P4 proposed logical layout, 2026-10-11. No implementation directories, source files, manifests, migrations or CI created. This book owns source/test ownership and directory boundaries; [development conventions](04-development-book.md) own coding/version/dependency/review; [P3 components](../specifications/P3-system-components.md) and [33-entity schema](../specifications/P3-persistence-artifacts.md) remain the unchanged design baseline. Layout is conditional on ADR-0001 and exact stack adoption; directory is not equivalent to separate executable/project/package.

## Proposed tree and tradeoffs
The owner's starting tree is refined to provide explicit infrastructure adapters and a composition root: without these, generic native/shared folders could absorb DB/process/file/security ownership. Keep a single desktop entry point; ui/native split is optional for an approved hybrid stack, not a mandate to mix languages. For WPF or Qt, map both concerns into coherent native projects without inventing a second frontend. Database schema/migrations directory holds provider adapters' versioned assets, not domain decisions or live DB. Modules remain independently owned adapters with shared platform services. Avoid microservices and one-project-per-component overhead; final physical project boundaries follow chosen language and measured build complexity.

```text
Freelance-Automation-Studio/
  AGENTS.md, README.md
  docs/{governance,specifications,adr,milestone-reports,test-matrix,prompts}
  apps/desktop/{ui,native,composition}        # ui/native split conditional
  packages/{domain,application,contracts,validation,reporting}
  infrastructure/{persistence,artifacts,processes,network,security,diagnostics,backup}
  workers/{spreadsheet,website-qa,documents,website-maintenance}
  database/{schemas,migrations}              # assets only, no live data
  tests/{unit,contract,integration,end-to-end,security,recovery,performance,packaging}
  tooling/{scripts,quality-gates,fixtures}
  packaging/windows/
  configuration/                            # safe examples/schema only
```

ORG-01 scope: all future source ownership; rationale: one clear semantic owner per change; owner: architect/component reviewer; evidence: every file maps to a directory below and a P3 component, imports satisfy the unchanged DAG, and related tests/specs are identified. Add a directory only for demonstrated responsibility with approval; never create generic utils/common as an unrestricted dependency hub. No live client workspace, DB, secrets, reports or generated binaries in the repository. Runtime user data is externally managed under P3 workspace rules; future generated build artifacts require explicit ignore/cleanup ownership.

## Directory ownership records

### Directory — docs/
- Purpose: Governance/design/evidence records.
- Owning architectural layer: Documentation leads.
- Allowed source types: Markdown and explicitly reviewed synthetic diagrams.
- Forbidden dependencies: Executable/runtime client data or duplicate rulebooks.
- Permitted imports: Relative authoritative references, no code imports.
- Public interface expectations: Stable headings/IDs and proposal/approval states.
- Relevant testing location: Document links/trace/scope review.
- Relevant documentation: [governance/00-master-rulebook.md](../governance/00-master-rulebook.md).
- Change approval requirements: Scoped milestone permission + code-owner review; boundary/public schema/provider change needs impact/ADR and explicit owner authorization before adoption.

### Directory — apps/desktop/ui/
- Purpose: P2 views, focus and typed user intent.
- Owning architectural layer: COM-A Presentation.
- Allowed source types: Approved UI-language resources/views and view-model adapters.
- Forbidden dependencies: DB/worker/OS/network/module-private calls.
- Permitted imports: Application public use-case ports and immutable view contracts.
- Public interface expectations: Accessible commands/read-model events, no shell strings.
- Relevant testing location: tests/unit and tests/end-to-end.
- Relevant documentation: [specifications/P2-screens.md](../specifications/P2-screens.md).
- Change approval requirements: Scoped milestone permission + code-owner review; boundary/public schema/provider change needs impact/ADR and explicit owner authorization before adoption.

### Directory — apps/desktop/native/
- Purpose: Conditional platform shell bridge, not catch-all business logic.
- Owning architectural layer: Presentation adapter only; infrastructure remains separate.
- Allowed source types: Approved framework shell bindings/resources.
- Forbidden dependencies: Domain orchestration or raw UI commands to arbitrary OS.
- Permitted imports: Application public APIs, minimal approved shell adapter ports.
- Public interface expectations: Validated shell capability binding; no unbounded invoke.
- Relevant testing location: tests/contract and tests/integration.
- Relevant documentation: [specifications/P3-system-components.md](../specifications/P3-system-components.md).
- Change approval requirements: Scoped milestone permission + code-owner review; boundary/public schema/provider change needs impact/ADR and explicit owner authorization before adoption.

### Directory — apps/desktop/composition/
- Purpose: Wire installed trusted adapters and startup/shutdown.
- Owning architectural layer: Application composition root.
- Allowed source types: Entry-point/service registration of approved stack.
- Forbidden dependencies: Business policies or arbitrary runtime plugin loading.
- Permitted imports: Public application/domain/contracts/infrastructure APIs only.
- Public interface expectations: Construct dependencies with no reverse import from composed packages.
- Relevant testing location: tests/integration and tests/packaging.
- Relevant documentation: [specifications/P3-system-components.md](../specifications/P3-system-components.md).
- Change approval requirements: Scoped milestone permission + code-owner review; boundary/public schema/provider change needs impact/ADR and explicit owner authorization before adoption.

### Directory — packages/domain/
- Purpose: Pure entities/invariants/state decisions.
- Owning architectural layer: COM-C Domain.
- Allowed source types: Language-neutral-to-policy domain types/value objects/inner ports.
- Forbidden dependencies: UI/DB drivers/OS/network/worker packages or serialization framework.
- Permitted imports: Pure standard-library primitives only; no inward import from contracts needed.
- Public interface expectations: Explicit domain invariants/results; inner-owned ports.
- Relevant testing location: tests/unit.
- Relevant documentation: [specifications/P3-persistence-artifacts.md](../specifications/P3-persistence-artifacts.md).
- Change approval requirements: Scoped milestone permission + code-owner review; boundary/public schema/provider change needs impact/ADR and explicit owner authorization before adoption.

### Directory — packages/application/
- Purpose: Use cases/orchestration, queue/review/config/registry policy.
- Owning architectural layer: COM-B/D/E/G/J/P/Q plus service policies.
- Allowed source types: Requests/results/services and owned outbound port contracts.
- Forbidden dependencies: UI framework or direct module-private/provider-specific imports.
- Permitted imports: Domain/public wire contracts, injected infrastructure ports.
- Public interface expectations: Typed use cases, immutable projections, revision/lease guards.
- Relevant testing location: tests/unit, tests/contract and tests/integration.
- Relevant documentation: [governance/04-development-book.md](../governance/04-development-book.md).
- Change approval requirements: Scoped milestone permission + code-owner review; boundary/public schema/provider change needs impact/ADR and explicit owner authorization before adoption.

### Directory — packages/contracts/
- Purpose: Versioned external module/IPC/report DTO schemas.
- Owning architectural layer: Public transport boundaries.
- Allowed source types: Bounded pure DTO/schema/version definitions.
- Forbidden dependencies: Domain business policy, infrastructure, executable deserialization types.
- Permitted imports: Pure standard-library primitives; DTO/domain mapping at application edge.
- Public interface expectations: Negotiated major/minor messages, stable errors/progress/cancel.
- Relevant testing location: tests/contract.
- Relevant documentation: [specifications/P3-module-contracts.md](../specifications/P3-module-contracts.md).
- Change approval requirements: Scoped milestone permission + code-owner review; boundary/public schema/provider change needs impact/ADR and explicit owner authorization before adoption.

### Directory — packages/validation/
- Purpose: Shared H/I policy and result semantics.
- Owning architectural layer: COM-H/I services.
- Allowed source types: Shared validators/invocation ports/result types.
- Forbidden dependencies: Module-private parsers or duplicate domain invariants.
- Permitted imports: Domain/public contracts/registry and artifact ports as permitted by P3.
- Public interface expectations: Input/output validation ports; module predicates supplied through contract.
- Relevant testing location: tests/unit, tests/contract and tests/integration.
- Relevant documentation: [specifications/P3-module-contracts.md](../specifications/P3-module-contracts.md).
- Change approval requirements: Scoped milestone permission + code-owner review; boundary/public schema/provider change needs impact/ADR and explicit owner authorization before adoption.

### Directory — packages/reporting/
- Purpose: Common report/package planning and schema policy.
- Owning architectural layer: COM-M/N; approval remains COM-J.
- Allowed source types: Report projections/format capability/payload manifests.
- Forbidden dependencies: Independent final approval authority or module-private import.
- Permitted imports: Domain/contracts/current approval/artifact/persistence ports under P3 DAG.
- Public interface expectations: Seven report contracts, passive formats and immutable selection.
- Relevant testing location: tests/contract, tests/integration and tests/end-to-end.
- Relevant documentation: [specifications/P3-reporting-packaging.md](../specifications/P3-reporting-packaging.md).
- Change approval requirements: Scoped milestone permission + code-owner review; boundary/public schema/provider change needs impact/ADR and explicit owner authorization before adoption.

### Directory — infrastructure/persistence/
- Purpose: Only COM-L adapter performs DB writes.
- Owning architectural layer: COM-L.
- Allowed source types: Approved DB provider/repository/transaction adapters.
- Forbidden dependencies: UI/worker modules or ownership of business acceptance.
- Permitted imports: Domain/application-owned persistence ports; provider assets.
- Public interface expectations: Single serialized writer/read snapshots with explicit transaction/audit.
- Relevant testing location: tests/integration and tests/recovery.
- Relevant documentation: [specifications/P3-persistence-artifacts.md](../specifications/P3-persistence-artifacts.md).
- Change approval requirements: Scoped milestone permission + code-owner review; boundary/public schema/provider change needs impact/ADR and explicit owner authorization before adoption.

### Directory — infrastructure/artifacts/
- Purpose: Managed files/publication/intents.
- Owning architectural layer: COM-K.
- Allowed source types: Filesystem/handle/hash/staging adapters.
- Forbidden dependencies: Arbitrary path authority, approval grants or original modification.
- Permitted imports: Inner artifact ports and L/O/S contracts under DAG.
- Public interface expectations: Leased owned path/artifact handles, recoverable finalization.
- Relevant testing location: tests/security, tests/recovery and tests/integration.
- Relevant documentation: [specifications/P3-persistence-artifacts.md](../specifications/P3-persistence-artifacts.md).
- Change approval requirements: Scoped milestone permission + code-owner review; boundary/public schema/provider change needs impact/ADR and explicit owner authorization before adoption.

### Directory — infrastructure/processes/
- Purpose: Worker launch/IPC/health/cancel/resource enforcement.
- Owning architectural layer: COM-F.
- Allowed source types: OS process/IPC adapters and trusted manifests.
- Forbidden dependencies: Imported executable/scripts or another attempt process control.
- Permitted imports: Supervisor port plus G/K/O/S contracts under DAG.
- Public interface expectations: Validated versioned protocol, owned-tree token, bounded grant.
- Relevant testing location: tests/contract, tests/security and tests/recovery.
- Relevant documentation: [specifications/P3-job-worker-protocol.md](../specifications/P3-job-worker-protocol.md).
- Change approval requirements: Scoped milestone permission + code-owner review; boundary/public schema/provider change needs impact/ADR and explicit owner authorization before adoption.

### Directory — infrastructure/network/
- Purpose: Approved network policy implementation adapter.
- Owning architectural layer: COM-S policy / MOD-B browser adapter.
- Allowed source types: Exact approved driver/traffic-control implementation.
- Forbidden dependencies: Hidden network fallback or unauthorized hosts/actions.
- Permitted imports: Scoped network ports/contracts, no desktop intent bypass.
- Public interface expectations: Request-level and effective egress enforcement; fail closed.
- Relevant testing location: tests/security and tests/integration.
- Relevant documentation: [specifications/P3-security-offline-network.md](../specifications/P3-security-offline-network.md).
- Change approval requirements: Scoped milestone permission + code-owner review; boundary/public schema/provider change needs impact/ADR and explicit owner authorization before adoption.

### Directory — infrastructure/security/
- Purpose: OS permissions/credential protection adapters.
- Owning architectural layer: COM-S.
- Allowed source types: Candidate token/ACL/secret-store adapters after proof.
- Forbidden dependencies: UI-only authorization or plaintext secret config.
- Permitted imports: Application permission ports/domain scope plus L under DAG.
- Public interface expectations: Expiring scoped grants/opaque secret references.
- Relevant testing location: tests/security.
- Relevant documentation: [governance/07-security-book.md](../governance/07-security-book.md).
- Change approval requirements: Scoped milestone permission + code-owner review; boundary/public schema/provider change needs impact/ADR and explicit owner authorization before adoption.

### Directory — infrastructure/diagnostics/
- Purpose: Local redacted audit/diagnostic sinks.
- Owning architectural layer: COM-O.
- Allowed source types: Structured logging adapters/rotation.
- Forbidden dependencies: Client raw content, secrets or upload services.
- Permitted imports: Audit/diagnostic ports, L under DAG.
- Public interface expectations: Safe event/error refs and retention/export review.
- Relevant testing location: tests/unit, tests/security and tests/integration.
- Relevant documentation: [governance/07-security-book.md](../governance/07-security-book.md).
- Change approval requirements: Scoped milestone permission + code-owner review; boundary/public schema/provider change needs impact/ADR and explicit owner authorization before adoption.

### Directory — infrastructure/backup/
- Purpose: Consistent local backup/restore adapter.
- Owning architectural layer: COM-R.
- Allowed source types: DB snapshot/files/manifest restore implementation.
- Forbidden dependencies: Cloud sync or overwrite of unmanaged originals.
- Permitted imports: R ports plus C/K/L/O/S under P3 DAG.
- Public interface expectations: Validated backup image/manifest and recoverable staged restore.
- Relevant testing location: tests/recovery and tests/packaging.
- Relevant documentation: [specifications/P3-persistence-artifacts.md](../specifications/P3-persistence-artifacts.md).
- Change approval requirements: Scoped milestone permission + code-owner review; boundary/public schema/provider change needs impact/ADR and explicit owner authorization before adoption.

### Directory — workers/<module>/
- Purpose: Private operations for exactly one of four modules.
- Owning architectural layer: MOD-A/B/C/D.
- Allowed source types: Eight internal areas below plus approved parser/driver adapters.
- Forbidden dependencies: Application DB/approval API/cross-module private import.
- Permitted imports: Public contracts and narrow worker infrastructure capability ports only.
- Public interface expectations: Common P3 descriptor/validation/plan/run/result contract.
- Relevant testing location: tests/unit, tests/contract and module integrations.
- Relevant documentation: [specifications/P3-module-designs.md](../specifications/P3-module-designs.md).
- Change approval requirements: Scoped milestone permission + code-owner review; boundary/public schema/provider change needs impact/ADR and explicit owner authorization before adoption.

### Directory — database/{schemas,migrations}/
- Purpose: Versioned provider schema/migration assets.
- Owning architectural layer: COM-L.
- Allowed source types: Approved migration/schema assets only in future.
- Forbidden dependencies: Live DB/client rows/secrets/domain business code.
- Permitted imports: Consumed by trusted persistence adapter only.
- Public interface expectations: Schema version/migration journal + backup verification.
- Relevant testing location: tests/integration and tests/recovery.
- Relevant documentation: [specifications/P3-persistence-artifacts.md](../specifications/P3-persistence-artifacts.md).
- Change approval requirements: Scoped milestone permission + code-owner review; boundary/public schema/provider change needs impact/ADR and explicit owner authorization before adoption.

### Directory — tests/<level>/
- Purpose: Behavior and contract verification.
- Owning architectural layer: QA / component owner.
- Allowed source types: Approved runner cases/harnesses; levels in testing book.
- Forbidden dependencies: Production imports of tests or confidential fixtures.
- Permitted imports: Public APIs primarily; private-unit seam only documented and no cross-module shortcut.
- Public interface expectations: Existing TEST IDs, fresh actual run evidence.
- Relevant testing location: Relevant level plus shared contract checks.
- Relevant documentation: [governance/06-testing-book.md](../governance/06-testing-book.md).
- Change approval requirements: Scoped milestone permission + code-owner review; boundary/public schema/provider change needs impact/ADR and explicit owner authorization before adoption.

### Directory — tooling/{scripts,quality-gates,fixtures}/
- Purpose: Local developer checks and reproducible synthetic fixtures.
- Owning architectural layer: Tooling/QA owner.
- Allowed source types: Future approved nonruntime scripts and fixture manifests.
- Forbidden dependencies: Mandatory cloud runtime or untrusted client build scripts.
- Permitted imports: Approved tool interfaces, public schemas; no product dependence.
- Public interface expectations: Local count/result/exit-status and safe cleanup contract.
- Relevant testing location: Tool smoke/integration under explicit later authorization.
- Relevant documentation: [specifications/P4-testing-verification.md](../specifications/P4-testing-verification.md).
- Change approval requirements: Scoped milestone permission + code-owner review; boundary/public schema/provider change needs impact/ADR and explicit owner authorization before adoption.

### Directory — packaging/windows/
- Purpose: Installer/portable manifests and notices.
- Owning architectural layer: Release lead.
- Allowed source types: Future approved packaging assets.
- Forbidden dependencies: Client DB/data/secrets or compile-only release claim.
- Permitted imports: Reviewed build outputs and dependency/notice inventory.
- Public interface expectations: Versioned installer/artifact/hash/release manifest.
- Relevant testing location: tests/packaging and system release.
- Relevant documentation: [governance/08-release-book.md](../governance/08-release-book.md).
- Change approval requirements: Scoped milestone permission + code-owner review; boundary/public schema/provider change needs impact/ADR and explicit owner authorization before adoption.

### Directory — configuration/
- Purpose: Versioned schemas and nonsecret examples.
- Owning architectural layer: COM-Q / module config owners.
- Allowed source types: Synthetic defaults/schema/sample settings.
- Forbidden dependencies: Credentials, browser sessions, grants/approvals or executable expressions.
- Permitted imports: Public schema/spec refs only.
- Public interface expectations: Bounded safe defaults, compatibility and migration policy.
- Relevant testing location: tests/contract and tests/security.
- Relevant documentation: [governance/04-development-book.md](../governance/04-development-book.md).
- Change approval requirements: Scoped milestone permission + code-owner review; boundary/public schema/provider change needs impact/ADR and explicit owner authorization before adoption.

## Boundary and interface enforcement
ORG-02 scope: every import/reference/runtime capability; rationale: prevent architectural shortcuts; owner: architect/security reviewer; evidence: static import graph and public-interface contract tests plus direct-entry security tests. Pure inner layers own their invariants/ports; infrastructure implements them, presentation calls application only. P3 component dependencies remain the authoritative acyclic graph; this layout changes no edge. Wire schemas in contracts use primitive payloads, mapped to domain types at the edge; domain does not depend on wire infrastructure. Composition may depend on public adapters to instantiate them, but no component imports composition or uses it as a service locator. Reporting/security/orchestration policies are application services, their OS/DB libraries remain infrastructure. OS commands only through trusted fixed supervisor/adapter contracts; no unrestricted filesystem or network API shared with UI/modules.

No cross-module private imports, direct worker DB write, UI-to-DB/worker shortcut or infrastructure-specific domain rule. Source-level checks complement runtime capability tests; passing graph checks is not hard sandbox proof. Boundary exceptions require reason/scope/risk/alternative/owner approval/removal or review date; record in development book change record and ADR when architectural, never silently change P3.

## Component directory map
Each P3 component is represented once; grouping changes no P3 edge/ownership. Logical policies and infrastructure implementations use ports rather than reverse package imports.

| Component | Proposed directory responsibility | Public boundary |
| --- | --- | --- |
| COM-A Desktop Presentation | apps/desktop/ui/ | [Unchanged P3 interface and DAG](../specifications/P3-system-components.md#com-a--desktop-presentation) |
| COM-B Application Services | packages/application/ | [Unchanged P3 interface and DAG](../specifications/P3-system-components.md#com-b--application-services) |
| COM-C Domain and Business Rules | packages/domain/ | [Unchanged P3 interface and DAG](../specifications/P3-system-components.md#com-c--domain-and-business-rules) |
| COM-D Job Orchestration | packages/application/ | [Unchanged P3 interface and DAG](../specifications/P3-system-components.md#com-d--job-orchestration) |
| COM-E Local Job Queue | packages/application/ | [Unchanged P3 interface and DAG](../specifications/P3-system-components.md#com-e--local-job-queue) |
| COM-F Worker Process Supervisor | infrastructure/processes/ | [Unchanged P3 interface and DAG](../specifications/P3-system-components.md#com-f--worker-process-supervisor) |
| COM-G Automation Module Registry | packages/application/ | [Unchanged P3 interface and DAG](../specifications/P3-system-components.md#com-g--automation-module-registry) |
| COM-H Input Validation | packages/validation/ | [Unchanged P3 interface and DAG](../specifications/P3-system-components.md#com-h--input-validation) |
| COM-I Output Validation | packages/validation/ | [Unchanged P3 interface and DAG](../specifications/P3-system-components.md#com-i--output-validation) |
| COM-J Human Review and Approval | packages/application/ | [Unchanged P3 interface and DAG](../specifications/P3-system-components.md#com-j--human-review-and-approval) |
| COM-K Artifact and File Management | infrastructure/artifacts/ | [Unchanged P3 interface and DAG](../specifications/P3-system-components.md#com-k--artifact-and-file-management) |
| COM-L Local Persistence | infrastructure/persistence/ | [Unchanged P3 interface and DAG](../specifications/P3-system-components.md#com-l--local-persistence) |
| COM-M Report Generation | packages/reporting/ | [Unchanged P3 interface and DAG](../specifications/P3-system-components.md#com-m--report-generation) |
| COM-N Delivery Packaging | packages/reporting/ | [Unchanged P3 interface and DAG](../specifications/P3-system-components.md#com-n--delivery-packaging) |
| COM-O Audit and Diagnostics | infrastructure/diagnostics/ | [Unchanged P3 interface and DAG](../specifications/P3-system-components.md#com-o--audit-and-diagnostics) |
| COM-P Error and Recovery | packages/application/ | [Unchanged P3 interface and DAG](../specifications/P3-system-components.md#com-p--error-and-recovery) |
| COM-Q Configuration and Templates | packages/application/ and configuration/ | [Unchanged P3 interface and DAG](../specifications/P3-system-components.md#com-q--configuration-and-templates) |
| COM-R Local Backup and Restore | infrastructure/backup/ | [Unchanged P3 interface and DAG](../specifications/P3-system-components.md#com-r--local-backup-and-restore) |
| COM-S Security and Permissions | packages/application/ policy + infrastructure/security/ and network/ adapters | [Unchanged P3 interface and DAG](../specifications/P3-system-components.md#com-s--security-and-permissions) |

## Domain entity ownership mapping
ORG-03 scope: P3's existing 33 entities; rationale: preserve normalized identity/provenance; owner: domain/persistence leads; enforcement: table covers every schema entity exactly once, while COM-L persists all records. Folder grouping is not a new table, migration or reduced model. Fourteen user-named aggregates (Client, Project, Job, JobVersion, ExecutionAttempt, AutomationModule, ModuleConfiguration, Artifact, Finding, ValidationResult, Review, Approval, AuditEvent, RecoveryRecord) map to their plural P3 entities; ModuleConfiguration means JobConfigurations, not an invented additional table. Subtypes/associations remain preserved. No entity scope change authorized.

| P3 entity | Proposed domain concern | Semantic owner | Source reference |
| --- | --- | --- | --- |
| Clients | packages/domain/clients-projects (pure model); provider mapping remains infrastructure | COM-B semantic owner; COM-L persists and enforces constraints. | [P3 entity](../specifications/P3-persistence-artifacts.md#entity--clients) |
| Projects | packages/domain/clients-projects (pure model); provider mapping remains infrastructure | COM-B semantic owner; COM-L persists and enforces constraints. | [P3 entity](../specifications/P3-persistence-artifacts.md#entity--projects) |
| Jobs | packages/domain/jobs (pure model); provider mapping remains infrastructure | COM-D semantic owner; COM-L persists and enforces constraints. | [P3 entity](../specifications/P3-persistence-artifacts.md#entity--jobs) |
| JobVersions | packages/domain/jobs (pure model); provider mapping remains infrastructure | COM-D semantic owner; COM-L persists and enforces constraints. | [P3 entity](../specifications/P3-persistence-artifacts.md#entity--jobversions) |
| ExecutionAttempts | packages/domain/jobs (pure model); provider mapping remains infrastructure | COM-D semantic owner; COM-L persists and enforces constraints. | [P3 entity](../specifications/P3-persistence-artifacts.md#entity--executionattempts) |
| AutomationModules | packages/domain/configuration (pure model); provider mapping remains infrastructure | COM-G semantic owner; COM-L persists and enforces constraints. | [P3 entity](../specifications/P3-persistence-artifacts.md#entity--automationmodules) |
| ModuleVersions | packages/domain/configuration (pure model); provider mapping remains infrastructure | COM-G semantic owner; COM-L persists and enforces constraints. | [P3 entity](../specifications/P3-persistence-artifacts.md#entity--moduleversions) |
| JobConfigurations | packages/domain/jobs (pure model); provider mapping remains infrastructure | COM-Q semantic owner; COM-L persists and enforces constraints. | [P3 entity](../specifications/P3-persistence-artifacts.md#entity--jobconfigurations) |
| ReusableTemplates | packages/domain/configuration (pure model); provider mapping remains infrastructure | COM-Q semantic owner; COM-L persists and enforces constraints. | [P3 entity](../specifications/P3-persistence-artifacts.md#entity--reusabletemplates) |
| InputArtifacts | packages/domain/artifacts (pure model); provider mapping remains infrastructure | COM-K semantic owner; COM-L persists and enforces constraints. | [P3 entity](../specifications/P3-persistence-artifacts.md#entity--inputartifacts) |
| IntermediateArtifacts | packages/domain/artifacts (pure model); provider mapping remains infrastructure | COM-K semantic owner; COM-L persists and enforces constraints. | [P3 entity](../specifications/P3-persistence-artifacts.md#entity--intermediateartifacts) |
| GeneratedArtifacts | packages/domain/artifacts (pure model); provider mapping remains infrastructure | COM-K semantic owner; COM-L persists and enforces constraints. | [P3 entity](../specifications/P3-persistence-artifacts.md#entity--generatedartifacts) |
| Findings | packages/domain/review (pure model); provider mapping remains infrastructure | COM-I semantic owner; COM-L persists and enforces constraints. | [P3 entity](../specifications/P3-persistence-artifacts.md#entity--findings) |
| ValidationResults | packages/domain/review (pure model); provider mapping remains infrastructure | COM-I semantic owner; COM-L persists and enforces constraints. | [P3 entity](../specifications/P3-persistence-artifacts.md#entity--validationresults) |
| HumanReviews | packages/domain/review (pure model); provider mapping remains infrastructure | COM-J semantic owner; COM-L persists and enforces constraints. | [P3 entity](../specifications/P3-persistence-artifacts.md#entity--humanreviews) |
| ApprovalRecords | packages/domain/review (pure model); provider mapping remains infrastructure | COM-J semantic owner; COM-L persists and enforces constraints. | [P3 entity](../specifications/P3-persistence-artifacts.md#entity--approvalrecords) |
| AuditEvents | packages/domain/history (pure model); provider mapping remains infrastructure | COM-O semantic owner; COM-L persists and enforces constraints. | [P3 entity](../specifications/P3-persistence-artifacts.md#entity--auditevents) |
| ErrorRecords | packages/domain/history (pure model); provider mapping remains infrastructure | COM-O semantic owner; COM-L persists and enforces constraints. | [P3 entity](../specifications/P3-persistence-artifacts.md#entity--errorrecords) |
| RecoveryRecords | packages/domain/history (pure model); provider mapping remains infrastructure | COM-P semantic owner; COM-L persists and enforces constraints. | [P3 entity](../specifications/P3-persistence-artifacts.md#entity--recoveryrecords) |
| ApplicationSettings | packages/domain/configuration (pure model); provider mapping remains infrastructure | COM-Q semantic owner; COM-L persists and enforces constraints. | [P3 entity](../specifications/P3-persistence-artifacts.md#entity--applicationsettings) |
| LocalBackupRecords | packages/domain/history (pure model); provider mapping remains infrastructure | COM-R semantic owner; COM-L persists and enforces constraints. | [P3 entity](../specifications/P3-persistence-artifacts.md#entity--localbackuprecords) |
| Artifacts | packages/domain/artifacts (pure model); provider mapping remains infrastructure | COM-K semantic owner; COM-L persists and enforces constraints. | [P3 entity](../specifications/P3-persistence-artifacts.md#entity--artifacts) |
| ArtifactRoles | packages/domain/artifacts (pure model); provider mapping remains infrastructure | COM-K semantic owner; COM-L persists and enforces constraints. | [P3 entity](../specifications/P3-persistence-artifacts.md#entity--artifactroles) |
| FinalizationIntents | packages/domain/artifacts (pure model); provider mapping remains infrastructure | COM-K semantic owner; COM-L persists and enforces constraints. | [P3 entity](../specifications/P3-persistence-artifacts.md#entity--finalizationintents) |
| QueueLeases | packages/domain/jobs (pure model); provider mapping remains infrastructure | COM-E semantic owner; COM-L persists and enforces constraints. | [P3 entity](../specifications/P3-persistence-artifacts.md#entity--queueleases) |
| AuthorizationRecords | packages/domain/security (pure model); provider mapping remains infrastructure | COM-S semantic owner; COM-L persists and enforces constraints. | [P3 entity](../specifications/P3-persistence-artifacts.md#entity--authorizationrecords) |
| DestructiveConsents | packages/domain/security (pure model); provider mapping remains infrastructure | COM-S semantic owner; COM-L persists and enforces constraints. | [P3 entity](../specifications/P3-persistence-artifacts.md#entity--destructiveconsents) |
| DeliveryManifests | packages/domain/artifacts (pure model); provider mapping remains infrastructure | COM-N semantic owner; COM-L persists and enforces constraints. | [P3 entity](../specifications/P3-persistence-artifacts.md#entity--deliverymanifests) |
| DeliveryManifestItems | packages/domain/artifacts (pure model); provider mapping remains infrastructure | COM-N semantic owner; COM-L persists and enforces constraints. | [P3 entity](../specifications/P3-persistence-artifacts.md#entity--deliverymanifestitems) |
| ExportRecords | packages/domain/artifacts (pure model); provider mapping remains infrastructure | COM-N semantic owner; COM-L persists and enforces constraints. | [P3 entity](../specifications/P3-persistence-artifacts.md#entity--exportrecords) |
| ExecutionPlans | packages/domain/jobs (pure model); provider mapping remains infrastructure | COM-D semantic owner; COM-L persistence. | [P3 entity](../specifications/P3-persistence-artifacts.md#entity--executionplans) |
| PlanAuthorizations | packages/domain/jobs (pure model); provider mapping remains infrastructure | COM-S semantic owner; COM-L persistence. | [P3 entity](../specifications/P3-persistence-artifacts.md#entity--planauthorizations) |
| PlanConsents | packages/domain/jobs (pure model); provider mapping remains infrastructure | COM-S semantic owner; COM-L persistence. | [P3 entity](../specifications/P3-persistence-artifacts.md#entity--planconsents) |

Any later model suggestion must identify the existing entity/design, rationale, affected REQ/NFR, migration and compatibility/data-retention impact, tests/fault/recovery impact and explicit approval; do not edit the schema to fit a convenient framework. DB-driven fields do not dictate domain coupling.

## Four module ownership and internal separation
ORG-04 owner: module/contract lead; scope: workers/spreadsheet (MOD-A), website-qa (MOD-B), documents (MOD-C), website-maintenance (MOD-D); rationale: independent extension; verification: each module has public adapter plus seven private responsibilities, consistent versioned P3 contract tests, no private imports. Proposed internal areas for every module: adapter (descriptor/public contract), configuration (schema predicates), planning (no execution effects), processing (private algorithms/parsers), validation (output assertions), evidence (typed factual results), errors (map P3 codes), recovery (owned cleanup/checkpoint/cancel). These may be small files/namespaces, not eight needless libraries.

Shared snapshots/config/queue/cancel/progress/artifact/result semantics/review/reports/packaging/backup are platform services, never copied per module. Module algorithms use scoped readonly inputs/staging handles/network grants, publish prepared results and never grant delivery approval. Tests live by level with a module subdirectory and shared contract fixtures; future extension registers a descriptor and isolated implementation through public contracts without editing unrelated module internals. Eleven P3 scope extensions remain pending. [Module contract](../specifications/P3-module-contracts.md) is authoritative; no new incompatible interface.

## Test/data/build separation and acceptance
ORG-05 owner: QA/release lead; scope: fixtures/generated outputs/user data; rationale: privacy and reproducibility; evidence: fixture manifest/license/size/expected-output review, no confidential content, owned ignored run directory cleanup and packaging inventory. Test-generated DB/files/browser profiles run outside source under owned disposable workspace, never runtime client data folders. Packaging consumes reviewed build outputs, not test files/live DB. Fixture policy belongs [testing](06-testing-book.md), program/user-data separation belongs [release](08-release-book.md).

Acceptance: tree evaluated against P3 layers/workers/contracts, all directory records have nine required fields, all 33 entities/19 components retain ownership, modules independently evolve, import direction/exception review testable, conditional framework/native split explicit, no scaffolding created. Final physical project/package layout awaits approved stack/P5 measurements; no new language choice or architecture ADR here. [Coverage](../test-matrix/P4-standards-coverage.md) and [P4 report](../milestone-reports/MS-0005-P4.md) own trace/check evidence.
