# SharePoint Online / OneDrive — External sharing review (governance)

Experience scope: Implemented and validated in a lab/sandbox tenant; production nuances documented separately.

## What (What this covers)
Review and hardening workflow for external sharing:
- tenant-level SharePoint/OneDrive sharing settings
- site-level sharing settings
- link types (Anyone / New and existing guests / Specific people)
- audit-driven investigation and remediation recommendations

## Why (Business / security rationale)
External sharing is a common data leakage vector. The goal is to:
- ensure sharing aligns with business requirements and policy
- reduce anonymous links where possible
- increase visibility via auditing and consistent governance

## Inputs to collect
- Business requirement (who needs to share with whom)
- Scope: tenant-wide vs specific site vs specific users
- Is this routine governance or incident-driven?

## How (Steps)

### 1) Check tenant-level sharing settings
Go to: **SharePoint admin center** -> **Policies** -> **Sharing**
- Review SharePoint sharing level and OneDrive sharing level.
- Review default link type and link expiration (if configured).

### 2) Identify sites that deviate from baseline (site-level)
Go to: **SharePoint admin center** -> **Sites** -> **Active sites**
- Select a site -> open **Policies** / **Sharing** (site panel options may vary by portal)
- Compare site sharing to tenant baseline.
- Flag outliers (more permissive than baseline).

### 3) Review external access patterns (high-level)
Depending on what’s available in your tenant:
- Review guest/external users and sharing posture.
- Focus on unknown or stale external access patterns.

### 4) Review “Anyone links” risk (if applicable)
If “Anyone links” are allowed:
- Confirm expiration policy is set (if required by org policy).
- Confirm usage is justified by business case.
If not justified:
- Recommend moving to “Specific people” links or controlled guest access.

### 5) Audit (incident-driven or periodic review)
Go to: **Microsoft Purview** -> **Audit**
- Search for sharing-related activities (link created, file shared externally).
- Correlate with site/user/timeframe and document findings.

### 6) Remediation options (least disruptive first)
- Align site sharing settings to baseline (requires **Change**).
- Set safer default link type (requires **Change**, may affect workflows).
- Enable/adjust link expiration where supported (requires **Change**).
- Remove stale guests / review external access (process-driven, document approvals).

### 7) Validation (must-do)
- Test the required sharing scenario using a controlled external account (if allowed).
- Confirm business workflow still works after tightening controls.

## Evidence (sanitized)
- Tenant sharing settings screenshot
- Site-level sharing screenshot (for the reviewed site)
- Audit query screenshot/export (if used)

## Rollback / Safety notes
- Tightening sharing may break partner workflows; document business owner approval.
- Use Change process for tenant/site policy changes and keep a rollback plan.

## Ticket notes (ITIL-friendly)
- Category: Collaboration / SharePoint Online / External sharing
- Outcome: baseline alignment + validated business scenario
