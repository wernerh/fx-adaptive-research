# E004 Methodology (pre-registered before any run)

- **Strategy:** `asian_range_breakout` with `Params()` defaults (v0.1): Asian range 0.15-0.60 x prior 14-day ATR; entry at
  the next bar after the first 1-minute mid close outside the Asian range during London 08:00-12:00; stop = Asian range
  (cap 25 pips); target 1.0R; max hold 60 min; hard exit at London session end.
- **Data:** Dukascopy m1 bid/ask; **dev block only** (2015-01-01 to 2020-12-31). val and OOS untouched.
- **Costs:** actual bid/ask spread + 0.1 pip slippage per side + 0.1 pip commission per round trip (SPEC 4).
  Diagnostic run: slippage 0 and commission 0 (spread still paid). This run informs only and does not affect the decision.
- **Commands:**
  `python scripts/run_backtest.py asian_range_breakout --block dev --experiment E004`
  `python scripts/run_backtest.py asian_range_breakout --block dev --experiment E004diag --slippage 0 --commission 0`
- **Decision rule (pre-registered):**
  - **PROCEED to val** only if, in dev: trades >= 150 AND net expectancy > 0 AND t-stat >= 2.0 AND profit factor >= 1.15.
  - Otherwise **REJECT S001 v0.1**. Do not run val. Any variant (filter, target, hold) is a new experiment counted as a new trial.
- **Report:** full metric block (SPEC 7), including hold-time distribution, MAE/MFE and costs as a share of gross.
