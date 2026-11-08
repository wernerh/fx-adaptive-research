# E010 Conclusion (2026-11-08)

## Decision: **WEAK** (pre-registered rule, applied exactly)
Rule per test: SIGNAL if mean signed > 1.0 pip AND block-bootstrap CI lower > 0 AND binomial p < 0.025;
WEAK if mean signed > 0 and (CI lower > 0 or p < 0.05); else NONE.
- `ecb_pre_all`: mean +0.76 pips (< 1.0), CI (0.124, 1.537) lower > 0, binom p 0.53 -> **WEAK**.
- `ecb_post_all`: mean +0.29 pips, CI includes 0, p 0.51 -> **NONE**.
Per the pre-registration, WEAK does **not** go to val. **B4v is not queued.** No lead.

## What we learned
- The ECB-fix version behaves like the London-fix version (E007): predicted signs, sub-pip size, no hit-rate edge.
- The pre-window mean is carried by magnitude, not frequency (hit rate 0.508): a few large USD-up moves in the hour before 14:15 CET.
  That hour is roughly 07:15-08:15 New York, which overlaps the E009 exploratory NOTE `ny_07` (-1.12 pips, i.e. USD up).
  Both are dev-only observations of the same clock region and must not be counted as independent support.
- Even if real, +0.76 pips is well below a round-trip cost, so it is not tradable on its own.
- The post window (contains 08:30 NY releases on most days) is the more volatile one (mean |ret| 14.0 vs 9.5 pips) and directionless.

## Next
B4 done. Next ready backlog item: B5 (Tokyo fix, E011).
