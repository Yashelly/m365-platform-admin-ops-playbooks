# Microsoft Teams — Policy not applying (user-level)

Experience scope: Implemented and validated in a lab/sandbox tenant; production nuances documented separately.

## What (What this covers)
Triage when a user claims Teams policy settings are not effective:
- meeting policy, messaging policy, app permission policy, app setup policy, calling policy
- direct vs group-based policy assignment
- propagation/caching issues

## Why (Business / security rationale)
Teams policies enforce governance and user experience standards. Misapplied policies can cause:
- uncontrolled external collaboration
- missing business-critical features
- inconsistent compliance across users

## Inputs to collect
- User UPN
- What exactly is not working (feature + expected behavior)
- When the policy was assigned/changed
- Scope: one user vs many users

## How (Steps)

### 1) Confirm expected policy and current assignments
Go to: **Teams admin center** -> **Users** -> select user -> **Policies**
- Capture current assignments (Meeting / Messaging / App permission / App setup / Calling).

### 2) Identify assignment method and precedence
- If **group assignment** is used: confirm user is in the assigned group.
- Check if there is a **direct assignment** overriding group assignment.

Tip:
- Prefer governance-consistent approach (usually group assignment), use direct assignment only as a temporary workaround.

### 3) Consider propagation and client caching
Ask the user to:
- sign out/in of Teams
- test in Teams web client (to isolate local client)
- wait for propagation if the change is very recent

### 4) Validate policy configuration itself
Go to: **Teams admin center** -> **Teams** / **Meetings** / **Messaging** -> **Policies**
- Open the relevant policy and verify the setting is correctly configured.
- If multiple users affected, check whether policy was recently modified.

### 5) Validate licensing (basic)
Ensure the user has a license that enables the required Teams functionality.

### 6) Fix options (minimal-risk)
- Reassign the correct policy (temporary direct assignment if needed) and document.
- Correct group membership / group policy assignment.
- If policy settings need change: create a **Change** ticket and modify with rollback plan.

### 7) Validation
- Confirm assignment in **Teams admin center** -> **Users** -> **Policies**
- Ask user to validate the exact feature (meeting option, chat feature, app availability).

## Evidence (sanitized)
- User policy assignment screenshot
- Policy settings screenshot
- Group assignment screenshot (if applicable)

## Rollback / Safety notes
- Avoid permanent direct assignments if governance expects group-based control.
- Any policy change should be tracked via Change with rollback steps.

## Ticket notes (ITIL-friendly)
- Category: Collaboration / Microsoft Teams / Policies
- Impact: user(s) affected
- Resolution: assignment method + validation result
