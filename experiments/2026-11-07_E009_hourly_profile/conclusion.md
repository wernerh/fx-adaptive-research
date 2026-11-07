# E009 Conclusion (2026-11-07)

## Decision: **CANDIDATES** (pre-registered rule, applied exactly): Wed_ny_18 and Thu_ny_18, both long (+1.33 / +1.24 pips per hour)
This is an **exploratory** scan. Nothing here is a SIGNAL or a lead. Per the pre-registered follow-up rule, both candidate
cells become **val-only, 1-trial** signal tests in the observed (long) direction with the B1 rule: backlog items **B9** and **B10**.

## What we learned
- Across 192 cells, almost every hour has a mean drift well under 1 pip; time-of-day drift in EUR/USD mid is small.
- The one strong regularity is the **NY 18:00-19:00 hour** (first full hour after the 17:00 roll): EUR/USD mid rises on average
  on every weekday (+0.43 to +1.33 pips), up-share ~0.59, t p 3e-7 for the pooled hour. Only Wed/Thu clear the 1-pip bar.
- **Calendar labels:** not a London-fix, ECB-fix or NY 10:00 release effect. It is **rollover-adjacent**: spreads are widest at
  17:00-18:00 NY and normalise during this hour, so a mid drift could partly be a quote/spread-normalisation artifact of a single
  venue rather than a tradable move. Wed-trading-date's 18:00 hour (Tuesday evening NY) is not the triple-swap night, so the
  Wed/Thu split is not an obvious swap effect. Treat the weekday split as likely noise around a pooled ~0.9-pip effect.
- **Costs are the main risk:** a ~1.3-pip gross move in a thin hour must beat the bid/ask spread at that hour (SPEC 4). Any
  later lead check must use actual bid/ask, and x1.5 costs.
- NOTE cells (negative drift 07:00 NY / 11:00 UTC, Mon 08-09 NY positive, Wed 04 NY negative) spawn nothing, by rule.

## Next
- B9 (Wed_ny_18 long, val only, 1 trial) and B10 (Thu_ny_18 long, val only, 1 trial) added to the backlog as `ready`, marked dev-derived.
- Top `ready` item remains B4 (ECB fix) unless re-ranked with a reason.
