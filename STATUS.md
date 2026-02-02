# STATUS

Evidence maturity board for this portfolio repository.

Legend:
- **Planned**: documented intent only, no hands-on artifacts yet
- **Partial**: documentation/runbook exists, evidence capture pending or incomplete
- **Captured**: sanitized evidence artifacts are available and referenced

Lifecycle: Planned -> Partial -> Captured

## Current maturity

| Area | Artifact | Type | Status | Evidence / reference |
| --- | --- | --- | --- | --- |
| Repo | START-HERE navigation page | Entry point | Captured | `START-HERE.md` |
| Repo | Baseline manifest | Inventory | Captured | `baseline-manifest.yml` |
| Repo | Consistency checker + CI | Quality gate | Captured | `tools/check_repo_consistency.py`, `.github/workflows/repo-quality.yml` |
| Overview | Scope | Documentation | Captured | `00-overview/scope.md` |
| Overview | Operating model | Documentation | Captured | `00-overview/operating-model.md` |
| Overview | Environments | Documentation | Captured | `00-overview/environments.md` |
| Overview | Navigation map | Documentation | Captured | `00-overview/navigation.md` |
| Operations (ITIL) | Incident template | Template | Captured | `07-operations-itil/incident-template.md` |
| Operations (ITIL) | Change template | Template | Captured | `07-operations-itil/change-template.md` |
| Operations (ITIL) | Service request template | Template | Captured | `07-operations-itil/service-request-template.md` |
| Evidence | Evidence rules and sanitization | Documentation | Captured | `99-evidence/README.md` |
| Exchange Online | Mail flow troubleshooting (Message trace) | Runbook | Captured | `02-exchange-online/runbooks/mail-flow-troubleshooting.md` (validated example: `02-exchange-online/cases/exo-tr-001-block-subject-marker.md`) |
| Exchange Online | Transport rule blocks subject marker `[LAB-BLOCK]` | Case study | Captured | `02-exchange-online/cases/exo-tr-001-block-subject-marker.md`, `99-evidence/exchange-online/2026-02-01_*` |
| Exchange Online | Operational baseline checks | Checks | Captured | `02-exchange-online/configuration/checks.md` |
| Microsoft Teams | Policy not applying (user-level) | Runbook | Partial | `03-microsoft-teams/runbooks/policy-not-applying.md` |
| Microsoft Teams | Operational baseline checks | Checks | Captured | `03-microsoft-teams/governance/checks.md` |
| SharePoint/OneDrive | External sharing review (governance) | Runbook | Partial | `04-sharepoint-onedrive/runbooks/external-sharing-review.md` |
| SharePoint/OneDrive | Operational baseline checks | Checks | Captured | `04-sharepoint-onedrive/governance/checks.md` |
| Defender for Office 365 | Anti-phish triage (phishing / false positive) | Runbook | Partial | `06-defender-for-office-365/runbooks/anti-phish-triage.md` |
| Defender for Office 365 | DEF-POL-001 Anti-phish policy review (fallback) | Case study | Planned | `06-defender-for-office-365/cases/def-pol-001-anti-phish-policy-review.md` |
| Defender for Office 365 | Operational baseline checks | Checks | Captured | `06-defender-for-office-365/configurations/checks.md` |
| Purview | Audit search runbook (incident + governance) | Runbook | Partial | `05-security-compliance-purview/auditing/audit-search-runbook.md` |
| Purview | PUR-AUD-001 OneDrive file activity audit example | Case study | Planned | `05-security-compliance-purview/auditing/cases/pur-aud-001-onedrive-file-activity.md` |
| Purview | Audit baseline checks | Checks | Captured | `05-security-compliance-purview/auditing/checks.md` |

## Evidence capture backlog (0.2 target)

| Area | Evidence item | Status | Target folder |
| --- | --- | --- | --- |
| Defender for Office 365 | Quarantine item details (reason + action) | Planned | `99-evidence/defender-o365/` |
| Defender for Office 365 | Explorer results (filters + actions) | Planned | `99-evidence/defender-o365/` |
| Purview | Audit search (filters + results) screenshot/export | Planned | `99-evidence/purview/` |

Notes:
- Evidence must be sanitized: no tenant IDs, no real domains, no UPNs, no object IDs.
- Use placeholders like `contoso.com`, `user1`, `tenantA`.