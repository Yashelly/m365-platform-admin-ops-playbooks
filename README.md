# Microsoft 365 Platform Administration — Operations Playbooks (Portfolio)

This repository documents operations-first administration of Microsoft 365 services:
**Exchange Online**, **Microsoft Teams**, **SharePoint Online/OneDrive**, **Microsoft Purview**, and **Microsoft Defender for Office 365**.

Focus: incident/request/change handling, governance, secure configuration baselines, and repeatable runbooks.

## What you’ll find here
- Service runbooks (triage -> investigation -> fix -> validation -> rollback)
- Practical baselines and checks (what to verify, where, and why)
- Security & compliance workflows (Purview + mail security)
- ITIL-aligned operational templates (incident/change/request)
- Automation snippets (PowerShell / Microsoft Graph where applicable)
- Sanitized evidence and exports where available

## Repository navigation
- `02-exchange-online/` — mail flow, mailbox permissions, runbooks
- `03-microsoft-teams/` — policies, troubleshooting, governance
- `04-sharepoint-onedrive/` — permissions/sharing, external sharing review, sync issues
- `05-security-compliance-purview/` — retention/DLP/labels/audit
- `06-defender-for-office-365/` — configurations & incident response playbooks
- `07-operations-itil/` — incident/change/request templates & reporting
- `09-automation/` — scripts and guidelines
- `99-evidence/` — sanitized evidence rules and placeholders

## Evidence & Sanitization
Evidence is stored in `/99-evidence` and sanitized (no tenant IDs, user PII, domains, device names).
See: `/99-evidence/README.md`.

## Related work
- Intune baseline: https://github.com/Yashelly/intune-modern-workplace
- Automation repo: https://github.com/Yashelly/intune-endpoint-automation-powershell

## Notes
Where a feature is intentionally left not configured, it is documented explicitly to avoid unnecessary disruption and align with enterprise baseline best practices.
