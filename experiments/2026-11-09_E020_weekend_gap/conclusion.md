# E020 Conclusion (2026-11-09, R038)

## Decision: **NONE on dev** (pre-registered rule `weekend_gap.decide_b17`, applied exactly). **No lead.**
Rule: SIGNAL if mean > 1.0 pip AND block-bootstrap CI lower > 0 AND one-sided t p < 0.05; WEAK if mean > 0 and
(CI lower > 0 or p < 0.05); else NONE.
- Mean -1.574 pips (not > 0), CI (-12.699, 7.03) includes 0, one-sided t p 0.6267 -> **NONE**.
- Per the methodology, B17 is closed for this definition; no re-test with other thresholds, windows or horizons on dev.
- Cost check also negative: SPEC 4 net -2.108, costs x1.5 -2.374 pips per event.

## Reading the result (cautions, no new numbers)
- The published weekend-overreaction reversal (Dao, McGroarty & Urquhart 2016) did not appear in 2015-2020 EUR/USD at the 1-pip bar;
  the median event lost 7.4 pips and the hit rate was 0.378.
- Descriptively, large gaps extended in the first 3 h after the Sunday open and the Tue/Fri exits were more negative still; this
  hints at continuation, not reversal. It is a post-hoc observation on dev and is **not** evidence; any continuation test needs its own
  pre-registration on fresh data (val) and counts as a new trial.
- As the power note said, SE ~4.9 pips means only a large effect could pass; NONE does not rule out a small reversal.

## Next
B17 closed (recorded in knowledge/rejected_hypotheses.md). Next `ready` backlog item: B18 (next-session reversal after a large daily move, dev).
