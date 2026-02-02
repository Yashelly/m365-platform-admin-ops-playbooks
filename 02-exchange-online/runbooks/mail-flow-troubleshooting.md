# Exchange Online — Mail flow troubleshooting (Message trace)

Experience scope: Implemented and validated in a lab/sandbox tenant; production nuances documented separately.

## What (What this covers)
Triage and resolution of mail delivery issues in Exchange Online:
- delayed delivery, NDR/bounces, missing emails
- inbound/outbound mail flow verification
- basic checks for rules, connectors, and security controls impact

## Why (Business / security rationale)
Mail flow incidents are high-impact. The goal is to:
- confirm whether Exchange accepted the message
- identify the failure point (sender -> transport -> recipient)
- restore delivery safely without weakening security controls

## Inputs to collect (from user / ticket)
- Sender address, recipient address
- Approximate time sent (with timezone)
- Subject (optional)
- NDR screenshot or error text (if any)
- Scope: single user / multiple users / external domains

## How (Steps)

### 1) Confirm scope and severity
- One user or multiple?
- Inbound / outbound / internal?
- Any recent changes (rules/connectors/security policies)?

Optional quick health check:
- **Microsoft 365 admin center** -> **Health** -> **Service health**

### 2) Run message trace
Go to: **Exchange admin center** -> **Mail flow** -> **Message trace**
- Search by sender/recipient and timeframe.
- Open the message details and capture:
  - status (Delivered / Failed / Pending / Filtered)
  - last event / final hop
  - any error codes or policy hits

Interpretation:
- **Delivered**: likely mailbox rules, junk, client filters, or quarantine release after delivery.
- **Failed**: capture failure details (reason, bounce type).
- **Pending/Delayed**: investigate throttling/connector path/size limits.

### 3) Check quarantine / mail security impact
Go to: **Microsoft Defender portal** -> **Email & collaboration** -> **Review** -> **Quarantine**
- Search by recipient, sender, subject.
- If found: capture quarantine reason and policy type (Anti-phish / Anti-spam / Safe Links / Safe Attachments).
- Release only according to policy/approval.

### 4) Check mail flow rules (systemic patterns)
Go to: **Exchange admin center** -> **Mail flow** -> **Rules**
- Look for rules affecting sender/recipient/domain.
- Check recently modified rules (if known).
- Validate conditions/actions (redirect, reject, add disclaimer, quarantine-like behavior).

### 5) Check connectors (if hybrid/3rd party routing exists)
Go to: **Exchange admin center** -> **Mail flow** -> **Connectors**
- Validate direction (Inbound/Outbound), TLS settings, smart host, restrictions.
- Confirm connector conditions match the intended traffic.

### 6) User/mailbox-level checks (single user cases)
- **Exchange admin center** -> **Recipients** -> **Mailboxes** -> select user
  - Verify mailbox exists, correct license, not soft-deleted.
  - Check **Mailbox delegation** if issue is “shared mailbox / access”.

User-side confirmation:
- Outlook rules, Focused Inbox, Junk Email folder
- Test in OWA (to isolate client-side caching)

### 7) Fix options (minimal-risk first)
Examples:
- False positive quarantine:
  - Release with approval; document reason; consider submitting false positive (org process).
- Misconfigured transport rule:
  - Create a **Change**; adjust rule; include rollback plan.
- Connector misrouting:
  - Create a **Change**; fix connector criteria; validate with test messages.

### 8) Validation (must-do)
- Send a controlled test message (internal + external if needed).
- Re-run **Message trace** and confirm “Delivered”.
- Confirm with the user (time received, client used).

## Validated example (lab)
See case study: `../cases/exo-tr-001-block-subject-marker.md`

## Evidence (sanitized)
- Transport rule overview: `../../99-evidence/exchange-online/2026-02-01_rule_block_subject_overview.png`
- Message trace (blocked): `../../99-evidence/exchange-online/2026-02-01_message-trace_blocked_details.png`
- Message trace (delivered after rollback): `../../99-evidence/exchange-online/2026-02-01_message-trace_delivered_details.png`

## Rollback / Safety notes
- Do not weaken security controls without approval.
- Any rule/connector change must have:
  - Change ticket
  - rollback steps
  - test plan

## Ticket notes (ITIL-friendly)
- Category: Messaging / Exchange Online / Mail flow
- Impact: users affected + business impact
- Timeline: detected -> triage -> fix -> validation
- Root cause: (if known)
- Resolution: actions + validation result
- Closure code: Resolved / Workaround / Duplicate / Not reproducible
