# E004 Conclusion (2026-11-07)

## Decision: **REJECT S001 v0.1** (pre-registered rule)
Rule: trades >= 150 AND net expectancy > 0 AND t >= 2.0 AND PF >= 1.15. Result: 1,344 trades, expectancy **-0.684 pips** (-0.047R),
t = -1.96, PF 0.875. Fails on expectancy, t-stat and profit factor. **Val not run.**

## What we learned
- The strategy loses money **before** slippage and commission (spread only: -0.484 pips/trade, PF 0.909). The failure is not just a cost problem; the breakout direction has no edge over 60 minutes.
- Win rate 45.8% at 1R targets, average win 10.4 pips and average loss 10.1 pips: close to a coin flip, minus the spread.
- Average MFE (9.35 pips) is below average MAE (9.87 pips): after the break, price moved slightly further against the trade than for it.
- Holds: median 60 minutes (the time stop); only 14% of trades closed within 30 minutes. Most trades never reached the stop or target inside an hour.
- The negative t-stat (-1.96) hints that breaks may tend to fail. This was **not** pre-registered. With the diagnostic at t = -1.39, it is not evidence for a fade strategy. A fade would be a new hypothesis and a new trial.
- Consistent with Neely & Weller (2003) and the external vendor backtest (research/external_research.md).

## Next
S001 v0.1 rejected. Variants (no ATR filter, 2R target, 30-minute hold, fade) would each be new trials on dev. Given the E001/E006 results, they are low priority.
