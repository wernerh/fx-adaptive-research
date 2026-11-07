# E004 Results

**Run:** GitHub Actions run 42395207715, 2026-11-07. Block: **dev only**. val and OOS untouched.
**Raw outputs:** `backtests/validation_reports/E004_asian_range_breakout_dev.json` (+ `_trades.csv`), diagnostic `E004diag_*`.

| Metric | Full costs (decision) | Diagnostic: spread only |
|---|---|---|
| trades | 1344 | 1344 |
| win_rate | 0.4576 | 0.4643 |
| avg_win_pips | 10.442 | 10.478 |
| avg_loss_pips | -10.07 | -9.984 |
| expectancy_pips | -0.684 | -0.484 |
| expectancy_r | -0.0472 | -0.0362 |
| t_stat | -1.96 | -1.39 |
| profit_factor | 0.875 | 0.909 |
| total_net_pips | -919.4 | -650.6 |
| max_drawdown_pips | -1306.0 | -1077.6 |
| max_consecutive_losses | 10 | 10 |
| sharpe_daily_annualised | -0.79 | -0.56 |
| avg_hold_min | 51.4 | 51.4 |
| median_hold_min | 60.0 | 60.0 |
| pct_within_5m | 0.0126 | 0.0126 |
| pct_within_15m | 0.0595 | 0.0595 |
| pct_within_30m | 0.1414 | 0.1391 |
| pips_per_exposure_hour | -0.799 | -0.565 |
| avg_mae_pips | 9.87 | 9.8 |
| avg_mfe_pips | 9.35 | 9.43 |
| avg_spread_at_entry_pips | 0.271 | 0.271 |
| costs_share_of_gross | 0.0098 | 0.0 |

Note: `costs_share_of_gross` counts only slippage and commission, because the spread is already inside gross P&L. It understates total costs. See lessons.
