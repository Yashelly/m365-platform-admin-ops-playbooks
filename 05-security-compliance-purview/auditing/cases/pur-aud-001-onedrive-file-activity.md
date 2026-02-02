# PUR-AUD-001 — Purview Audit validated example (OneDrive file activity)

Goal: demonstrate an operations-ready audit workflow with a clear question -> filters -> results -> record details.

Scope: lab/sandbox tenant only. Evidence must be sanitized.

## Scenario (lab-safe)

Trigger auditable events in OneDrive:

1) OneDrive -> create a file `audit-test.docx`
2) Share the file (internal recipient or share to self)
3) Open the file (generate access event)

Then validate in Purview:

- Microsoft Purview -> Audit
- Apply filters (time range, activities, workload)
- Open a record (Record details)
- Optional: Export (CSV)

## Expected outcome

- Audit results contain the generated OneDrive activities
- Record details clearly show actor + activity + timestamp (sanitized for repo)

## Evidence to capture (sanitized)

Minimum screenshots (0.2 target):

- `99-evidence/purview/2026-02-01_audit_filters.png`
- `99-evidence/purview/2026-02-01_audit_results.png`
- `99-evidence/purview/2026-02-01_audit_record_details.png`

Optional:

- `99-evidence/purview/2026-02-01_audit_export.csv`

Sanitize before commit:
- tenant domain, UPNs, object IDs, IP addresses, unique record IDs

## Links

- Runbook: `../audit-search-runbook.md`
- Evidence rules: `../../../../99-evidence/README.md`
