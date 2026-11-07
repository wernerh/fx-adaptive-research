# Risk framework

Risk management takes precedence over profitability. The risk reviewer agent may veto any promotion.

## Scope
Research, backtesting and paper trading only. No live orders from this system.

## Pre-trade checks (paper trading)
1. Strategy status is at least `oos_validated` and risk-approved.
2. Spread at entry <= strategy max spread (default 2.0 pips; see SPEC 4).
3. Not inside a restricted window (risk/trading_restrictions.md).
4. Daily loss limit and consecutive-loss limit not breached.
5. Position size from risk/position_sizing.md.

## Strategy-level risk review (required for promotion)
- Max drawdown in val and OOS, in R and pips
- Longest losing streak, and the probability of a streak of 2x that length (Monte Carlo resample of trades)
- Worst single trade versus stop (slippage / gap risk)
- Performance by year and by volatility regime: no single year > 50% of total P&L
- Exposure to event days: results with event days excluded must still pass
- Sensitivity: +/-20% on each parameter must not flip expectancy sign

## Suspension triggers (paper)
- Rolling 50-trade expectancy below zero AND drawdown > 1.5x worst OOS drawdown
- Live spread or slippage > 2x modelled for 20+ trades
- Any data or clock fault (see data/data_quality_reports.md)
