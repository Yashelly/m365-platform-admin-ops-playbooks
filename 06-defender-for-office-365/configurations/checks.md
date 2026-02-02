# Microsoft Defender for Office 365 — Baseline checks

Experience scope: Implemented and validated in a lab/sandbox tenant; production nuances documented separately.

## Purpose

Operational checklist to keep email protection effective and investigations repeatable.

## Checks

### 1) Quarantine workflow exists and is enforced

- **Where:** Microsoft Defender portal -> Email & collaboration -> Review -> Quarantine  
- **Why:** releases without process weaken security  
- **Good:** release requires justification/approval; false positives submitted where possible

### 2) Anti-phish triage playbook is available

- **Where:** Repo -> 06-defender-for-office-365/runbooks/  
- **Why:** phishing tickets are repetitive and high-impact  
- **Good:** runbook used; incident notes capture detection reason and action taken

### 3) Explorer/Investigation capability is understood (if available)

- **Where:** Microsoft Defender portal -> Email & collaboration -> Explorer  
- **Why:** faster scoping across recipients and actions  
- **Good:** admins can filter by sender/recipient/time and interpret actions

### 4) “Do not weaken controls” guardrail is explicit

- **Where:** Ops policy + Change process  
- **Why:** disabling protection to “fix delivery” is high risk  
- **Good:** policy tuning only via Change; scoped, time-bounded exceptions

### 5) Evidence capture standards are followed

- **Where:** 99-evidence/README.md  
- **Why:** portfolio must be review-friendly and safe  
- **Good:** screenshots/exports sanitized; paths referenced in STATUS and tickets

## Notes

Any policy tuning must be treated as a Change: justification, rollback, and validation.
