# agri-scan-agent

## CI severity policy

### Enforced in CI today (current fail gate)
CI currently uses a **critical-only fail gate**:

- **Fail**: one or more `critical` findings are present.
- **Pass**: zero `critical` findings, even if `serious`, `moderate`, or `low` findings are present.

In other words, `critical` is the only severity that is CI-blocking today.

### Aspirational policy (not yet enforced)
Our target policy is stricter than the current baseline:

- Move to **fail on `serious` or higher** once the existing `serious` baseline is reduced to a sustainable level.
- Continue reporting `moderate` and `low` findings for visibility and triage, even when non-blocking.

## Roadmap for threshold escalation

Planned sequence for tightening CI gates:

1. Burn down current baseline `serious` issues.
2. Flip CI gate from `critical` to `serious` (fail on `serious` + `critical`).
3. Re-evaluate after stability period and decide whether additional tightening is practical.

## Test naming and severity-language consistency

Use severity terms in tests exactly as they appear in policy language:

- `critical` = blocking today.
- `serious` = non-blocking today, planned future blocker.
- `moderate` / `low` = non-blocking informational severities.

Recommended CI-oriented test names:

- `test_ci_fails_on_critical_findings`
- `test_ci_passes_with_serious_when_no_critical`
- `test_ci_passes_with_moderate_and_low_when_no_critical`

These names intentionally mirror the pass/fail wording above to avoid ambiguity.
