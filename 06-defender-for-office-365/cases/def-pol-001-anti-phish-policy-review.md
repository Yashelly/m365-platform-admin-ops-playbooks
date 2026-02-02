# DEF-POL-001 — Defender for Office 365 validated example (Anti-phish policy review)

Goal: show an operations signal in Defender for Office 365 even when Quarantine is empty.

This case documents a safe, review-friendly baseline check:
- policy exists
- scope/assignments are clear
- key settings are documented

Scope: lab/sandbox tenant only. Evidence must be sanitized.

## Scenario options

### Option A (preferred if available): Quarantine triage

- Microsoft Defender portal -> Email & collaboration -> Review -> Quarantine
- Capture: item list + item details (reason, action, policy)

### Option B (fallback): Anti-phish policy review

- Microsoft Defender portal -> Email & collaboration -> Policies & rules -> Threat policies -> Anti-phishing
- Capture:
  - policy overview
  - key settings
  - scope/assignments

## Expected outcome

- Reviewer can see either:
  - a quarantine item with a clear reason/action, OR
  - a policy baseline with clear scope and settings

## Evidence to capture (sanitized)

If Option A (quarantine):

- `99-evidence/defender-o365/2026-02-01_quarantine_list.png`
- `99-evidence/defender-o365/2026-02-01_quarantine_item_details.png`

If Option B (policy review):

- `99-evidence/defender-o365/2026-02-01_anti-phish_policy_overview.png`
- `99-evidence/defender-o365/2026-02-01_anti-phish_policy_settings.png`
- `99-evidence/defender-o365/2026-02-01_anti-phish_policy_assignments.png`

Sanitize before commit:
- tenant domain, UPNs, object IDs, IP addresses, message-id, unique policy IDs

## Links

- Runbook: `../runbooks/anti-phish-triage.md`
- Evidence rules: `../../99-evidence/README.md`
