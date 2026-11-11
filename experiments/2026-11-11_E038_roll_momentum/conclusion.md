# E038 Conclusion (2026-11-11, R084)

## Decision: **WEAK on dev** (pre-registered rule `decide_b38`, B13 rule unchanged, applied exactly). **Not a LEAD.**
Rule: < 500 tested dates -> NONE; SIGNAL if mean > 1.0 pip AND block-bootstrap (block 20) CI lower > 0 AND one-sided binomial
p < 0.05; WEAK if mean > 0 and (CI lower > 0 or p < 0.05); else NONE.
- n 1542 (>= 500). Mean +0.255 (not > 1.0), CI lower 0.023 (> 0), binomial p 0.06924 (not < 0.05) -> **WEAK**.
- LEAD condition 1 fails (not SIGNAL). Costs also fail: SPEC 4 net -0.425, x1.5 -0.765. No notification.

## Reading the result (cautions, no new numbers)
- There is a small, statistically detectable continuation into the 17:00 NY roll (t p 0.018, CI just above 0), in the direction
  Baltussen et al. report for futures, but at about a quarter of a pip it is below the round-trip cost and far below the 1-pip bar.
  As predicted in the pre-registration, the bar bound, not the CI.
- The size bar is not loosened (CLAUDE.md rule 7; lesson 2026-11-08 "a fails-only-the-size-bar WEAK is still WEAK").
- The EDT/EST split and the mid |r1| tercile look stronger; these are descriptive slices after the fact and must not be turned into
  dev re-tests (lesson R076: post-hoc subsets of a marginal dev effect have not survived val).

## Next
Per methodology: B38 closed WEAK (not sent to val); B39 closed unearned (0 trials). No re-test on dev with other windows, exit
times, terciles or seasons. Goes to rejected_hypotheses.md as WEAK. No other `ready` backlog item -> next run is a backlog refill.
