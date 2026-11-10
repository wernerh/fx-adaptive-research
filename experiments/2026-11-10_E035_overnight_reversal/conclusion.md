# E035 Conclusion (2026-11-10, R076)

## Decision: **B32 NONE, B33 SIGNAL on dev** (pre-registered rule `overnight_reversal.decide_b32`, same for B33, applied exactly). **Not a LEAD yet.**
Rule per arm: < 500 tested dates -> NONE; SIGNAL if mean > 1.0 pip AND block-bootstrap (block 20) CI lower > 0 AND one-sided t p < 0.025
(Bonferroni, 2 trials); WEAK if mean > 0 and (CI lower > 0 or p < 0.025); else NONE.
- B32: n 1554 (>= 500), mean -0.285 (not > 1), CI lower -2.421, t p 0.598 -> **NONE**.
- B33: n 1536 (>= 500), mean +2.695 > 1.0, CI lower 0.47 > 0, t p 0.0093 < 0.025 -> **SIGNAL**.
- LEAD definition (docs/AUTONOMOUS_PROTOCOL.md) needs a separate pre-registered val confirmation; B33 passes condition 1 only.
  Cost check positive (descriptive): SPEC 4 net +2.047, x1.5 +1.723. No notification.

## Reading the result (cautions, no new numbers)
- **The daily reversal does not exist on dev:** a single overnight move does not predict the 07:00 -> 16:55 NY return (slope about 0).
  The smoothed arm works while the daily arm does not, and the two take the same side on only ~half of dates, so B33 is not "B32
  averaged"; it behaves more like a 20-date trend-fade of the overnight session.
- **Marginal and front-loaded:** 2015 (+8.9) carries much of the mean; 2019-2020 are below +1 pip. With ~252 registered trials, one dev
  SIGNAL at p 0.009 is within what chance produces. Val is the real test.
- **Not the unconditional drift:** unconditional long r_id is +0.56 and B33 is ~half long (0.482), so the result is not a long bias.
- The |O20| tercile pattern is not monotone (low +2.6, mid +1.2, high +4.3); it is descriptive and must not be used to change the rule.
- Calendar label: the hold spans 08:30 NY releases, the 10:00 NY cut and the London 4pm fix; not a fix strategy.

## Next
Per methodology: B33 SIGNAL -> **B34** (val confirmation of the B33 arm only, rule unchanged, own pre-registration, 1 val trial,
p < 0.05 since only one arm is carried, O20 burn-in from val dates only). B32 closed (rejected_hypotheses.md).
