# E041 Conclusion (2026-11-11, R092)

## Decision: **NONE on dev** (pre-registered rule `oil_lag.decide_b45` = `overnight_reversal.decide_b34`, applied exactly). **Not a LEAD.**
Rule: data gate first; < 500 tested dates -> NONE; SIGNAL if mean > 1.0 pip AND block-20 bootstrap CI lower > 0 AND one-sided t
p < 0.05; WEAK if mean > 0 and (CI lower > 0 or t p < 0.05); else NONE.
- Data gate pass (0.9872 of dates with both WTI quotes).
- B45: n 1519, mean +2.306 pips, CI (-0.513, 5.184), t p 0.0555 -> **NONE**.
- LEAD condition 1 fails. No notification.

## Reading the result (cautions, no new numbers)
- A near miss: the point estimate is above the 1-pip bar and the sign matches the stated prior, but neither the bootstrap CI nor the
  t-test clears its bar. The pre-registered rule says NONE; it is not WEAK and is not sent to val.
- 2015 (+11.066, the oil collapse year) carries much of the mean; the other five years average close to zero. The high-|O| tercile
  result is post-hoc (one of three slices chosen after seeing data) and must not become a new dev test (lesson R076).
- The contemporaneous correlation is small (0.0405), so on dev EUR/USD does not behave as an oil-sensitive currency at daily
  frequency; Ferraro-Rogoff-Rossi is about commodity currencies (CAD) and is not refuted by this.
- Dukascopy CFD roll handling remains UNVERIFIED; 11 dates were skipped as |O| > 0.10.

## Next
B45 closed NONE (rejected_hypotheses.md). No re-test on dev with other lags, windows, |O| filters or oil benchmarks. No `ready`
item remains: next run is a backlog refill.
