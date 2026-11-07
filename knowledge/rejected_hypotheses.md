# Rejected hypotheses

Never delete entries. A rejected hypothesis may be re-opened only by a new experiment with a stated reason.

| Date | Hypothesis | Experiment | Why rejected | Evidence | Re-open conditions |
|---|---|---|---|---|---|
| 2026-11-07 | Asian/London session structure (7 simple predictors) predicts the sign of the EUR/USD 08:00-12:00 NY return | E001 | No predictor significant in dev or val; all Bonferroni p = 1.0; all bootstrap CIs include 0 | [EXP] experiments/2026-11-07_E001_session_direction_baseline | Short outcome windows, regime-conditional tests, or new predictor types (counted as new trials) |
| 2026-11-07 | S001 Asian range breakout v0.1 (first London close outside Asian range, 1R target, 60-min hold, range/ATR 0.15-0.60) has positive net expectancy | E004 | dev: 1,344 trades, -0.684 pips/trade, t=-1.96, PF 0.875; negative even before slippage/commission | [BT] experiments/2026-11-07_E004_asian_range_breakout_dev | A pre-registered variant with a new mechanism (not parameter tuning) |
| 2026-11-07 | E001 predictors predict sign of short early-US windows (08:00-09:00, 08:35-09:30 NY) | E006 | 28 tests, min p=0.16, all Bonferroni p=1.0 | [EXP] experiments/2026-11-07_E006_short_window_direction | New predictor types; regime conditioning pre-registered with a trial count |
