# Microsoft Teams — Baseline checks

Experience scope: Implemented and validated in a lab/sandbox tenant; production nuances documented separately.

## Purpose

Operational checklist to keep Teams governance consistent and reduce “policy not applying” incidents.

## Checks

### 1) Policy assignment strategy is consistent

- **Where:** Teams admin center -> Users -> Policies  
- **Why:** mixed assignment models create confusion and drift  
- **Good:** group-based assignment preferred; direct assignment only as temporary workaround

### 2) Meeting policy baseline is defined

- **Where:** Teams admin center -> Meetings -> Meeting policies  
- **Why:** meetings are high-risk for compliance and user experience  
- **Good:** baseline policy exists; deviations are justified and tracked

### 3) Messaging policy baseline is defined

- **Where:** Teams admin center -> Messaging policies  
- **Why:** controls chat features, external comms, and governance  
- **Good:** baseline documented; exceptions reviewed periodically

### 4) External access / guest access posture known

- **Where:** Teams admin center -> Users -> External access / Guest access  
- **Why:** uncontrolled external collaboration increases risk  
- **Good:** settings align with business policy; changes go via Change

### 5) Apps governance is under control (high-level)

- **Where:** Teams admin center -> Teams apps -> Manage apps / Permission policies / Setup policies  
- **Why:** third-party apps can introduce compliance and security risk  
- **Good:** baseline approach documented; high-risk apps handled via approvals

### 6) Incident playbook is available for policy issues

- **Where:** Repo -> 03-microsoft-teams/runbooks/  
- **Why:** repeated tickets need repeatable triage steps  
- **Good:** runbook used; ticket notes capture assignment method + validation

## Notes

Keep policy changes review-friendly: Change ticket, rollback steps, and validation plan.
