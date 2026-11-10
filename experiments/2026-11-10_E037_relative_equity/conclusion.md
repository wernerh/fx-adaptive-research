# E037 Conclusion (2026-11-10, R081)

## Decision: **NONE / NONE on dev** (pre-registered rule `decide_b35`, same for B36, applied exactly). **Not a LEAD.**
Rule: data gate first; < 500 tested dates -> NONE; SIGNAL if mean > 1.0 pip AND block-bootstrap (block 20) CI lower > 0 AND one-sided
t p < 0.025 (Bonferroni, 2 trials); WEAK if mean > 0 and (CI lower > 0 or p < 0.025); else NONE.
- Data gate ok (1.8% of dates missing an index quote, limit 10%).
- B35: n 1509, mean +1.268 (> 1.0) but CI lower -1.411 (not > 0) and t p 0.191 (not < 0.025) -> **NONE**.
- B36: n 1482, mean -0.88 (not > 0) -> **NONE**.
- LEAD condition 1 fails for both arms. No notification.

## Reading the result (cautions, no new numbers)
- The Hau-Rey contemporaneous relation shows up in our data (corr -0.228, the predicted sign), but yesterday's relative equity return
  does not predict the next 16:05 -> 16:00 EUR/USD move at a size we can detect (bar ~ +2.7 pips). The rebalancing effect, if it
  exists at daily frequency, is priced the same day.
- B35's positive mean is about one SE, driven by no single tercile and reversed in 2020; not evidence of an effect.
- The 20-date arm (B36) is negative: no support for slow, accumulated rebalancing flow at this horizon.

## Next
Per methodology: B35 and B36 closed; B37 closed unearned (0 trials); no re-test on dev with other windows, anchors or lags. Both go
to rejected_hypotheses.md. No other `ready` backlog item -> next run is a backlog refill.
