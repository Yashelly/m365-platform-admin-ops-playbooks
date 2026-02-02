# Microsoft Defender for Office 365 — Anti-phish triage (suspected phishing / false positive)

Experience scope: Implemented and validated in a lab/sandbox tenant; production nuances documented separately.

## What (What this covers)

Operational workflow to triage and respond to suspected phishing incidents or false positives in email protection, including:

- identify whether a message was delivered, blocked, or quarantined
- investigate email entities, detections, and policy impact
- take safe actions (release, allow/block, submission) with minimal risk
- document incident handling in ITIL-friendly format

## Why (Business / security rationale)

Phishing incidents are high impact. The goal is to:

- protect users and the tenant from credential theft and malware
- quickly restore legitimate mail flow when false positives occur
- avoid weakening security controls without proper approval

## Inputs to collect (from user / ticket)

- Reporter (user) UPN (or placeholder ID in lab)
- Sender address and display name
- Recipient(s)
- Approximate time received/sent (with timezone)
- Subject and message ID (if available)
- What happened: delivered, blocked, quarantined, user clicked a link, attachments opened
- Any screenshots (headers, warning banners, quarantine notice)

## Triage (first 5 minutes)

1) Determine severity

- One user or multiple users?
- Similar reports across the org?
- Any indicators of compromise: clicked link, entered credentials, opened attachment?

2) Containment guidance (if user engaged)

- If credentials were entered: follow org process (password reset, revoke sessions, MFA check).
- If attachment opened: follow org process (endpoint scan/isolation, report to SOC).

Note: This repo focuses on M365 email security ops; endpoint containment steps may be handled by endpoint/SOC runbooks.

## Investigation (where to look)

### 1) Locate the message / entity

Option A: Quarantine

- **Microsoft Defender portal** -> **Email & collaboration** -> **Review** -> **Quarantine**
- Search by recipient, sender, subject.
- Open item details and capture:
  - quarantine reason (Anti-phish / Anti-spam / Malware / Safe Attachments)
  - policy name (if shown)
  - detection details

Option B: Explorer (if available)

- **Microsoft Defender portal** -> **Email & collaboration** -> **Explorer**
- Filter by sender, recipient, subject, time range.
- Confirm action taken:
  - Delivered / Junked / Quarantined / Blocked / Replaced

Option C: Exchange message trace (cross-check delivery path)

- **Exchange admin center** -> **Mail flow** -> **Message trace**
- Confirm whether Exchange accepted and delivered the message, and note any policy-related events.

### 2) Validate phishing indicators (quick checks)

- Sender domain mismatch / lookalike domain
- Suspicious reply-to address
- Urgent language, credential request
- Link destination mismatch (hover/URL)
- Attachments: unexpected, macro-enabled, password-protected archives

### 3) Identify policy impact (why it was blocked/quarantined)

- In quarantine/explorer details, identify which control triggered:
  - Anti-phish policy
  - Anti-spam policy
  - Safe Links / Safe Attachments
  - Malware detection

Capture: policy name, action, and detection reason for ticket notes.

## Fix / Response actions (minimal-risk first)

### Scenario A: Confirmed phishing / malicious

1) Block and contain

- Use org process to block sender/domain as appropriate.
- If multiple recipients: identify impacted users via Explorer.
- If click is suspected: escalate to security/SOC workflow.

2) Remediation support (email-side)

- Ensure message is not released from quarantine.
- If delivered: follow org process to remove/contain messages (capabilities depend on licensing and tenant).

### Scenario B: Likely false positive (legitimate business email blocked)

1) Validate legitimacy

- Confirm sender is expected (known vendor/partner) and content matches expected business case.
- Confirm no obvious indicators of phishing.
- If uncertain: treat as suspicious and escalate.

2) Release from quarantine (with approval where required)

- **Microsoft Defender portal** -> **Email & collaboration** -> **Review** -> **Quarantine**
- Release message according to org policy (often “Release to inbox” + optional “Report false positive”).

3) Submit for analysis (recommended)

- Use built-in submission flow (if available) to improve detections:
  - submit as false positive / not phishing

4) Policy tuning (only with Change + approval)

- If recurring false positives: create a **Change**.
- Prefer narrow allow-listing (specific sender or domain) with justification.
- Avoid broad bypass rules that reduce security posture.

## Validation (must-do)

- Confirm message outcome in **Explorer** or **Message trace**:
  - released and delivered (if false positive)
  - blocked/quarantined for all targeted users (if phishing)
- Confirm with user:
  - email received (false positive) OR
  - no further suspicious emails received (phishing containment)
- Document validation result and timestamp.

## Validated example (0.2 target)

Planned case study: `06-defender-for-office-365/cases/def-pol-001-anti-phish-policy-review.md`

## Evidence (sanitized)

Planned evidence filenames (choose the available option):

Option A (quarantine):
- `99-evidence/defender-o365/2026-02-01_quarantine_list.png`
- `99-evidence/defender-o365/2026-02-01_quarantine_item_details.png`

Option B (policy review):
- `99-evidence/defender-o365/2026-02-01_anti-phish_policy_overview.png`
- `99-evidence/defender-o365/2026-02-01_anti-phish_policy_settings.png`
- `99-evidence/defender-o365/2026-02-01_anti-phish_policy_assignments.png`

## Rollback / Safety notes

- Do not disable Anti-phish / Safe Links / Safe Attachments to “make it work”.
- Avoid global allow rules; prefer scoped exceptions and time-bounded changes.
- Any policy tuning must go through Change management with rollback steps.

## Ticket notes (ITIL-friendly)

- Category: Security / Email security / Anti-phish
- Impact: number of users affected + business impact
- Urgency: user credentials risk? org-wide campaign?
- Timeline: report -> triage -> action -> validation
- Findings: indicators, detection reason, policy involved
- Actions taken: release/block/submission/escalation
- Validation: confirmed result in Explorer/Message trace + user confirmation
- Closure code: Resolved / Workaround / Escalated / False positive
