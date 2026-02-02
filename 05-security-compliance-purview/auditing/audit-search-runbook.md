# Microsoft Purview — Audit search runbook (incident + governance)

Experience scope: Implemented and validated in a lab/sandbox tenant; production nuances documented separately.

## What (What this covers)

Operational workflow for running audit searches to support:

- incident response (who did what, when, where)
- governance reviews (sharing changes, admin actions, mailbox access)
- evidence collection for tickets and post-incident analysis

## Why (Business / security rationale)

Audit is a primary source of truth for investigation and accountability. The goal is to:

- establish a reliable timeline of actions
- identify actors and impacted resources
- provide evidence for incident/change tickets
- improve controls and prevent recurrence

## When to use audit (decision guide)

Use **incident** mode when:

- suspicious email activity, mailbox access, or forwarding rules are reported
- unusual file sharing or downloads are suspected
- admin changes may have caused an outage or security exposure

Use **governance** mode when:

- periodic review of sharing behavior is required
- verifying compliance with policy (retention, DLP, access control)
- validating a change (confirming actions took place)

## Inputs to collect (from ticket)

- Time window (start/end) with timezone
- User(s) or admin(s) involved (UPN or placeholder IDs)
- Workload: Exchange / SharePoint / OneDrive / Teams / Entra admin actions
- Suspected activity type (e.g., external sharing, mailbox rule change)
- Target object (file/site/mailbox) if known

## How (Steps)

### 1) Open audit search

Go to: **Microsoft Purview** -> **Audit**

- Choose an appropriate time range (narrow is better for signal).
- Select users (if known) or leave empty for broad query in short window.

### 2) Choose the right search approach

Approach A: Known user + short time window

- Filter by user and narrow time range.
- Add activity filters if available.

Approach B: Unknown user + known activity or target

- Filter by activities first (e.g., sharing-related events).
- Narrow by time window and workload.

Approach C: Admin change validation

- Filter by admin users and admin activities.
- Confirm change timeline matches ticket.

### 3) Apply filters (recommended minimum)

- Time range (start/end)
- User(s) (if known)
- Activities (based on scenario)
- Workload (if needed)

Example scenarios and typical activity focus:

- External sharing investigation: sharing link creation, permissions changes, guest access changes
- Mailbox compromise: mailbox rule creation/changes, forwarding configuration changes, sign-in related audit (if available)
- Admin actions: policy changes, configuration changes, role assignments (depends on licensing/log sources)

Note: Exact activity names vary; select the closest matching activities available in your tenant.

### 4) Run the search and review results

- Inspect events for:
  - timestamp (with timezone awareness)
  - actor (user/admin)
  - action/activity name
  - target resource (file/mailbox/site) if included
  - client/app/IP (if available and allowed to store in evidence)

### 5) Export / capture evidence (sanitized)

Capture either:

- export file (preferred) OR
- screenshots of filters + top results + event details

Sanitization rules:

- remove/blur tenant identifiers and PII (UPNs, domains, object IDs)
- use placeholders in any copied text (user1@contoso.com)

## Output (what to write in the ticket)

Include:

- Search scope: time range + filters used
- Findings summary:
  - key events (who/what/when)
  - impacted resources
  - confidence assessment (clear / likely / inconclusive)
- Evidence references:
  - path(s) under `99-evidence/` (sanitized)
- Recommended next actions:
  - containment/escalation if suspicious
  - change request if a control adjustment is needed

## Validation / closure

- For incident cases:
  - confirm investigation question is answered (actor identified or ruled out)
  - document whether escalation is required (SOC/security)
- For governance cases:
  - confirm baseline alignment or document deviations
  - create Change ticket if remediation is needed

## Safety / privacy notes

- Collect the minimum necessary audit data for the ticket purpose.
- Do not store sensitive identifiers in the repo evidence.
- Follow your org’s retention and privacy requirements.
- If audit data is incomplete/unavailable, document limitations and alternative sources.

## Validated example (0.2 target)

Planned case study: `05-security-compliance-purview/auditing/cases/pur-aud-001-onedrive-file-activity.md`

## Evidence (sanitized)

Planned evidence filenames (replace with real captures):

- `99-evidence/purview/2026-02-01_audit_filters.png`
- `99-evidence/purview/2026-02-01_audit_results.png`
- `99-evidence/purview/2026-02-01_audit_record_details.png`
- (optional) `99-evidence/purview/2026-02-01_audit_export.csv`
