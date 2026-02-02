# Start here

This repository is an operations-first portfolio for Microsoft 365 administration.
Use this page as the single entry point.

## Quick navigation
- Exchange Online: `02-exchange-online/runbooks/`
- Microsoft Teams: `03-microsoft-teams/runbooks/`
- SharePoint Online / OneDrive: `04-sharepoint-onedrive/runbooks/`
- Purview: `05-security-compliance-purview/`
- Defender for Office 365: `06-defender-for-office-365/`
- ITIL templates: `07-operations-itil/`
- Evidence rules: `99-evidence/README.md`

## Featured captured scenario (validated)
- Exchange Online -> Transport rule blocks subject marker `[LAB-BLOCK]` (change -> validate -> rollback -> validate)  
  Case: `02-exchange-online/cases/exo-tr-001-block-subject-marker.md`  
  Evidence:  
  - `99-evidence/exchange-online/2026-02-01_rule_block_subject_overview.png`  
  - `99-evidence/exchange-online/2026-02-01_message-trace_blocked_details.png`  
  - `99-evidence/exchange-online/2026-02-01_message-trace_delivered_details.png`

## Runbook format
Each runbook follows:
**triage -> investigation -> fix -> validation -> rollback**  
Includes ITIL-friendly ticket notes (what to capture, how to close).

## Suggested reading order (fast)
1) Exchange: mail flow troubleshooting (message trace)
2) Teams: policy not applying (user-level)
3) SharePoint/OneDrive: external sharing review (governance)

## Related work
- Intune baseline: https://github.com/Yashelly/intune-modern-workplace
- Automation patterns: https://github.com/Yashelly/intune-endpoint-automation-powershell

## Planned next (0.2 target)
- Purview -> Audit search validated example
  Case: `05-security-compliance-purview/auditing/cases/pur-aud-001-onedrive-file-activity.md`
  Runbook: `05-security-compliance-purview/auditing/audit-search-runbook.md`

- Defender for Office 365 -> Anti-phish triage evidence (quarantine OR policy review)
  Case: `06-defender-for-office-365/cases/def-pol-001-anti-phish-policy-review.md`
  Runbook: `06-defender-for-office-365/runbooks/anti-phish-triage.md`
