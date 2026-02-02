# Microsoft Purview — Audit baseline checks

Experience scope: Implemented and validated in a lab/sandbox tenant; production nuances documented separately.

## Purpose

Operational checklist for audit readiness and investigation support.

## Checks

### 1) Audit entry point and runbook are available

- **Where:** Microsoft Purview -> Audit  
- **Why:** audit is the primary timeline/evidence source  
- **Good:** runbook exists; admins know how to run scoped searches

### 2) Investigation-friendly search patterns are used

- **Where:** Microsoft Purview -> Audit (filters)  
- **Why:** broad searches create noise and are hard to validate  
- **Good:** narrow time windows; filter by user/activity where possible

### 3) Evidence capture is sanitized

- **Where:** 99-evidence/README.md  
- **Why:** avoid storing tenant identifiers and PII  
- **Good:** redaction/placeholder rules followed; evidence stored under 99-evidence/

### 4) Ticket output format is consistent

- **Where:** 07-operations-itil/incident-template.md  
- **Why:** repeatable investigations require consistent write-up  
- **Good:** scope, findings, evidence paths, and next actions recorded

### 5) Limitations are documented when audit data is incomplete

- **Where:** Ticket notes + runbook notes  
- **Why:** prevents false certainty  
- **Good:** explicit “inconclusive” outcomes with recommended next sources/steps

## Notes

Collect minimum necessary data for the purpose and follow privacy requirements.
