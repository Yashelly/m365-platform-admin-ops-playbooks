# SharePoint Online / OneDrive — Baseline checks

Experience scope: Implemented and validated in a lab/sandbox tenant; production nuances documented separately.

## Purpose

Operational checklist for permissions, sharing, and governance to reduce data leakage risk.

## Checks

### 1) Tenant sharing baseline is documented

- **Where:** SharePoint admin center -> Policies -> Sharing  
- **Why:** tenant settings set the security ceiling  
- **Good:** baseline defined; OneDrive sharing aligned; deviations require Change

### 2) Default link type and link expiration posture known

- **Where:** SharePoint admin center -> Policies -> Sharing  
- **Why:** “Anyone links” are a common leakage vector  
- **Good:** defaults are intentional; expiration strategy documented where applicable

### 3) Site-level deviations are reviewable

- **Where:** SharePoint admin center -> Sites -> Active sites -> select site  
- **Why:** permissive sites are the main governance gap  
- **Good:** periodic review exists; outliers documented with business owner

### 4) Guest/external access review process exists

- **Where:** Microsoft 365 admin center / Entra (as applicable) + SharePoint admin center  
- **Why:** stale guests accumulate risk  
- **Good:** review cadence defined; removals/changes tracked

### 5) Audit usage for sharing investigations

- **Where:** Microsoft Purview -> Audit  
- **Why:** incident response requires who/what/when  
- **Good:** audit runbook used; evidence sanitized and referenced in ticket

### 6) “Tighten sharing” change discipline

- **Where:** Repo -> 04-sharepoint-onedrive/runbooks/ + 07-operations-itil/  
- **Why:** tightening can break business workflows  
- **Good:** Change ticket includes owner approval, rollback plan, and validation scenario

## Notes

Evidence must be sanitized (no tenant identifiers, no PII).
