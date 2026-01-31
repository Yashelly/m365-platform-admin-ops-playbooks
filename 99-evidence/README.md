# Evidence rules

## Sanitization
- No PII (names, emails), no tenant IDs, no real domains, no IPs.
- Use placeholders: contoso.com, user1, tenantA.
- Blur/cover sensitive values.
- Prefer exports over screenshots where possible.

## Naming
99-evidence/<area>/<YYYY-MM-DD>_<topic>_<artifact>.png
99-evidence/<area>/<YYYY-MM-DD>_<topic>_<export>.json
