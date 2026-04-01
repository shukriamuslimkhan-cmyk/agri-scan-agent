## CI severity policy

### Enforced in CI today
CI currently uses a **critical-only fail gate**:

- **Fail** when one or more `critical` findings are present.
- **Pass** when there are no `critical` findings, even if there are `serious`, `moderate`, or `low` findings.

### Aspirational policy
The goal is to eventually **fail on `serious` or higher** once the current baseline of `serious` issues is reduced to a sustainable level.

- `moderate` and `low` findings will remain non-blocking.

### Roadmap for threshold escalation
1. Burn down current `serious` issues.
2. Flip the CI gate to fail on `serious` + `critical`.
3. Re-evaluate the threshold after a stability period.

### Test naming and severity-language consistency
Use the exact severity terms in test names to avoid ambiguity between policy and implementation.

- `test_ci_fails_on_critical_findings`
- `test_ci_passes_with_serious_when_no_critical`
- `test_ci_passes_with_moderate_and_low_when_no_critical`
