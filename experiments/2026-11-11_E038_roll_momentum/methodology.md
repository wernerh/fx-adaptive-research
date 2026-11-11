# E038 Methodology (pre-registered 2026-11-11 R083, before any run)

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask (repo pipeline), mid derived. **Dev block only** (2015-01-01..2020-12-31,
  `splits.DEFAULT_PLAN`). The script drops every bar whose trading date is not `dev` **before** any computation (E035 pattern);
  val and OOS untouched. No external data.
- **Dates:** sorted dev trading dates D (17:00 NY roll, SPEC 2, `sessions.trading_date`), Monday-Friday only (weekend trading-date
  artefacts dropped and counted). A Monday date opens Sunday 17:00 NY (repo convention).
- **Quotes (E011 rule):** bid/ask **open** of the first 1-minute bar in [T, T+5 min) America/New_York; missing -> excluded, never
  filled.
  - start quote P0: first bar in [17:00, 17:05) NY whose trading date is D (`overnight_reversal.evening_quotes(bars, 17, 0)`);
  - entry quote E: first bar in [16:25, 16:30) NY on NY calendar date D (`vol_state_fix.ny_quotes`);
  - exit quote X: first bar in [16:55, 17:00) NY on NY calendar date D.
- **Signals:** r1 = (mid E - mid P0) / pip; r2 = (mid X - mid E) / pip. Position = sign(r1); signed = sign(r1) x r2. The side uses
  only quotes at or before 16:25 NY (E is both the end of r1 and the entry), so no look-ahead (tested).
- **Exclusions, counted, first reason in this order:** `missing_start` (P0), `missing_entry` (E), `zero_signal` (r1 == 0),
  `missing_exit` (X), `entry_skipped_spread` (ask - bid at E > 2.0 pips, SPEC 4).
- **Statistic (1 trial):** over tested dates: mean, median, SD of signed; moving-block bootstrap 95% CI of the mean (**block 20
  dates**, 2000 draws, seed 0); one-sided binomial test of sign agreement (hits = signed > 0, over tested dates with signed != 0,
  H1 share > 0.5). One-sided t p reported, descriptive.
- **Decision rule (`roll_momentum.decide_b38`, B13 rule unchanged, fixed in backlog R082):**
  - < 500 tested dates -> **NONE** (insufficient sample).
  - **SIGNAL** if mean > 1.0 pip AND CI lower > 0 AND binomial p < 0.05.
  - **WEAK** if mean > 0 and (CI lower > 0 or binomial p < 0.05), but not SIGNAL.
  - **NONE** otherwise. A significantly negative mean (CI upper < 0) is logged as exploratory "reversal" only, not a trial.
  - SIGNAL earns B39 (val confirmation, own pre-registration). Not a lead on its own.
- **Descriptive (not trials, do not change the decision):** OLS slope of r2 on r1; |r1| terciles; SD of r2; median / p90 spread at
  16:25 and 16:55 NY; net at bid/ask, SPEC 4 (slippage 0.1 + commission 0.1) and costs x1.5; by year; EDT vs EST (NY offset);
  Fridays vs Mon-Thu; next-date reversal reading sign(r1(D)) x (mid 16:25 NY D+1 - mid 17:05 NY opening D+1); excluding FOMC
  statement dates (data/calendars/fomc_dates.csv) and excluding the last trading date of each month; unconditional long r2.
- **Calendar label:** end-of-day roll effect; not the London 4pm fix and not the CME settlement (B13, blocked).
- **Command (GitHub Actions research-batch):** `python scripts/run_e038_roll_momentum.py | tee backtests/validation_reports/E038_results.txt`
- **Outputs:** backtests/validation_reports/E038_results.{txt,json}, E038_days.csv.
