# E040 Methodology (pre-registered 2026-11-11 R089, before any run)

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask (repo pipeline), mid derived. **Dev block only** (2015-01-01..2020-12-31,
  `splits.DEFAULT_PLAN`). The script drops every bar whose trading date is not `dev` **before** any computation; val and OOS
  untouched. Calendar: data/calendars/fomc_dates.csv (official Fed pages, validated 2015-2023).
- **Events:** scheduled, not cancelled statement dates t with t in dev (expected 48). Unscheduled actions excluded (listed).
  Statement time 14:00 America/New_York.
- **Quotes (E011 rule):** bid/ask **open** of the first 1-minute bar in [T, T+5 min) America/New_York (`vol_state_fix.ny_quotes`);
  missing -> excluded, never filled.
  - A: 16:00 NY on the previous business day (`fomc.prev_business_day(t)`); B: 13:55 NY on t;
  - E (entry): 02:00 NY on t+1 (next calendar day); X (exit): 14:00 NY on t+1.
- **Signal:** P = (mid B - mid A) / pip. Position s = -sign(P). Target r = (mid X - mid E) / pip; signed = s x r. The side uses only
  quotes at or before 13:55 NY on t; the trade runs 02:00 -> 14:00 NY on t+1 (no look-ahead, tested).
- **Exclusions, counted, first reason in this order:** `not_trading_day` (no bars on NY calendar date t+1), `missing_pre` (A or B),
  `zero_signal` (P == 0), `missing_entry` (E), `missing_exit` (X), `entry_skipped_spread` (ask - bid at E > 2.0 pips, SPEC 4).
- **Statistic (1 trial):** mean, median, SD of signed; i.i.d. bootstrap 95% CI of the mean (2000 draws, seed 0; events ~6 weeks
  apart do not overlap; implemented as `metrics.block_bootstrap_mean_ci` with block = 1); one-sided t test (H1 mean > 0).
  Binomial sign test reported, descriptive.
- **Decision rule (`post_fomc_reversal.decide_b43`, fixed in backlog R088):**
  - < 40 tested events -> **NONE** (insufficient sample).
  - **SIGNAL** if mean > 1.0 pip AND bootstrap CI lower > 0 AND one-sided t p < 0.05.
  - **WEAK** if mean > 0 and (CI lower > 0 or t p < 0.05), but not SIGNAL.
  - **NONE** otherwise. SIGNAL earns B44 (val confirmation, own pre-registration). Not a lead on its own.
- **Descriptive (not trials, do not change the decision):** unconditional short EUR/USD over 02:00 -> 14:00 NY t+1; P > 0 and P < 0
  subsets; the 0-12 h window -sign(P) x (mid 02:00 NY t+1 - mid 14:00 NY t) (14:00 quote = first bar in [14:00, 14:05) on t); OLS
  slope of r on P; mean P and mean |P|; by year; net at bid/ask, SPEC 4 (slippage 0.1 + commission 0.1) and costs x1.5; median
  spread at E and X; non-FOMC Thursday control: same rule on every dev Wednesday that is not a scheduled/unscheduled FOMC date.
- **Calendar label:** FOMC statement (scheduled policy event); this effect *is* the strategy if it passes.
- **Cost model:** SPEC 4, gates only the LEAD label.
- **Command (GitHub Actions research-batch):** `python scripts/run_e040_post_fomc_reversal.py | tee backtests/validation_reports/E040_results.txt`
- **Outputs:** backtests/validation_reports/E040_results.{txt,json}, E040_events.csv.
