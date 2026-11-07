# E006 Conclusion (2026-11-07)

## Decision: **NONE** (pre-registered rule)
No predictor was significant in dev after Bonferroni (all 1.0), and none had unadjusted p < 0.05 in val. Shortening the
outcome window to the first US hour, with or without the 08:30 release jump, did not reveal any signal hidden by E001's 4-hour window.

## Exploratory note (NOT a finding)
`lon_false_break_fade` on 08:00-09:00 was positive by > 1 pip in both blocks (about +1.4 to +1.6 pips/day), with hit rates of
51-54% on small samples. It is far from significant and was one of 14 trials. Recorded so a future experiment can
**pre-register** it with its own trial count; it must not be promoted on this evidence.

## Implications
- The core project hypothesis (Asian/London structure gives a US-session directional bias) has now failed twice:
  over 4 hours (E001) and over the first hour, before and after data (E006).
- S002/S003 stay deprioritised.
- The trial count is now 7 (E001) + 14 (E006) + 1 (E004) = 22 tests on dev data. Any later "discovery" on dev must be judged against that.
