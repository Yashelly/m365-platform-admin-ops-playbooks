# Exchange Online — Baseline checks

Experience scope: Implemented and validated in a lab/sandbox tenant; production nuances documented separately.

## Purpose

Lightweight operational checklist for Exchange Online to support day-2 administration and incident prevention.

## Checks

### 1) Mail flow visibility (trace ready)

- **Where:** Exchange admin center -> Mail flow -> Message trace  
- **Why:** fastest way to confirm acceptance/delivery status  
- **Good:** trace available; admins know standard trace window and filters

### 2) Quarantine review process exists

- **Where:** Microsoft Defender portal -> Email & collaboration -> Review -> Quarantine  
- **Why:** false positives and phishing triage depend on quarantine visibility  
- **Good:** documented process for release + approvals; no “blind releases”

### 3) Transport rules change discipline

- **Where:** Exchange admin center -> Mail flow -> Rules  
- **Why:** rules can break mail flow org-wide  
- **Good:** changes go via Change ticket; rollback steps documented

### 4) Connectors inventory (if present)

- **Where:** Exchange admin center -> Mail flow -> Connectors  
- **Why:** misrouting/TLS issues cause widespread delivery failures  
- **Good:** connectors are minimal, justified, documented; routing logic understood

### 5) Accepted domains / default domain sanity

- **Where:** Microsoft 365 admin center -> Settings -> Domains  
- **Why:** wrong domain config leads to NDRs and auth issues  
- **Good:** only required domains; default domain is correct

### 6) Mailbox permissions governance

- **Where:** Exchange admin center -> Recipients -> Mailboxes -> Mailbox delegation  
- **Why:** over-permissioning is a common security risk  
- **Good:** least privilege; permissions reviewed periodically; changes tracked

### 7) Forwarding controls awareness

- **Where:** Exchange admin center -> Recipients -> Mailboxes -> Mail flow settings (forwarding)  
- **Why:** forwarding is frequently abused during account compromise  
- **Good:** forwarding is controlled; exceptions are approved and time-bounded

### 8) Audit availability for investigations

- **Where:** Microsoft Purview -> Audit  
- **Why:** investigations require evidence of actions  
- **Good:** audit searches used for incident timelines; evidence sanitized

## Notes

Where a feature is intentionally left not configured, it is documented explicitly to avoid unnecessary disruption and align with enterprise baseline best practices.
