# E022 Conclusion (2026-11-09, R043)

## Decision: **SIGNAL on dev** (pre-registered rule `vol_state_fix.decide_b19`, applied exactly). **Not a LEAD yet.**
Rule: SIGNAL if mean > 1.0 pip AND block-bootstrap CI lower > 0 AND one-sided t p < 0.05; WEAK if mean > 0 and
(CI lower > 0 or p < 0.05); else NONE.
- Mean +3.646 pips (> 1.0), CI (0.011, 7.751) lower > 0, one-sided t p 0.0133 (< 0.05) -> **SIGNAL**.
- Cost check positive (descriptive): SPEC 4 net +3.139, costs x1.5 +2.886 pips per event.
- LEAD definition (docs/AUTONOMOUS_PROTOCOL.md) needs a separate pre-registered val confirmation. Per the methodology, the next step is
  **B19v**: the identical rule on the val block as its own experiment (1 val trial). No notification.

## Reading the result (cautions, no new numbers)
- **Marginal:** the CI lower bound is 0.011 pips, just above 0; with ~236 registered trials across the project, one dev SIGNAL at
  p 0.013 is within what chance alone produces. Val is the real test.
- **Conditioning vs. unconditional drift:** the control (normal dates, +1.731) and all dates (+2.339, CI excludes 0) are also
  positive. The difference between high-vol and normal dates was not tested and is not established; part of the dev result may be an
  unconditional pre-fix / European-morning USD-up drift (also seen as WEAK in E010 and as the +1.776 European leg of E017 on val).
- **Uneven over time:** 2015 (+10.9) and 2016 (+5.7) carry much of the mean; 2018 was negative. Weekday splits are post-hoc and not
  evidence.
- **Val contamination note for B19v:** E017 already computed the unconditional short 03:00-08:00 NY on val (European leg +1.776).
  No vol-conditional 02:00-08:15 NY return has been computed on val, so B19v's exact statistic is unseen, but a related window was.
- Not a calendar artifact by construction beyond the ECB-fix window itself, which *is* the mechanism; ECB policy days unidentified.

## Next
Queue B19v (val confirmation, rule unchanged). B20 stays `ready` behind it.
