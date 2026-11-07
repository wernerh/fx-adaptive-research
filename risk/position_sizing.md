# Position sizing

Default for paper trading: **fixed fractional, 0.25% of equity risked per trade**, size = risk / stop distance.

- Never size from win rate or Kelly until 300+ OOS/paper trades exist; even then use at most 1/4 Kelly.
- Cap: one open position per strategy; max 3 open positions system-wide.
- Daily loss limit: 1% of equity. Weekly: 2.5%. Hitting either stops paper trading until the next period.
- Stops must be placed with the order. No mental stops.
