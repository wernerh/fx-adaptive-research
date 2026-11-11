# E040 Conclusion (2026-11-11, R090)

## Decision: **NONE on dev** (pre-registered rule `post_fomc_reversal.decide_b43`, applied exactly). **Not a LEAD.**
Rule: < 40 tested events -> NONE; SIGNAL if mean > 1.0 pip AND i.i.d. bootstrap CI lower > 0 AND one-sided t p < 0.05; WEAK if
mean > 0 and (CI lower > 0 or t p < 0.05); else NONE.
- B43: n 47, mean +2.623 pips, CI (-14.684, 21.44), t p 0.3863 -> **NONE**.
- LEAD condition 1 fails. No notification.

## Reading the result (cautions, no new numbers)
- With SD ~62 pips and 47 events (SE ~9 pips), only a reversal several times larger than the 1-pip bar could have shown up; the power
  note in the pre-registration said so. The point estimate is indistinguishable from zero and from the non-FOMC Wednesday control.
- The slope of the t+1 return on the pre-statement drift is positive (not significant), so there is no hint of reversal on dev.
- Lee & Wang (2025) is read from the abstract only; currency set and EUR magnitude are UNVERIFIED. The NONE says the symmetric
  reversal rule has no usable edge on EUR/USD dev; it does not refute the paper.
- The 2019-2020 negative years and the control's +5.093 are descriptive and must not be turned into new dev tests (lesson R076).

## Next
B43 closed NONE; B44 (val confirmation) closed unearned, 0 trials. No re-test with other windows, drift anchors or subsets. B43 goes
to rejected_hypotheses.md. Next `ready` item: B45 (lagged WTI -> next-day EUR/USD).
