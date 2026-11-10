# E037 Methodology (pre-registered 2026-11-10 R080, before any run)

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask, mid derived. Dukascopy index CFDs `eusidxeur` (EU Stocks 50, EUR) and
  `usa500idxusd` (US 500, USD) 1-minute bid/ask, downloaded on the GitHub Actions runner only (`scripts/download_dukascopy_index.sh`,
  E034, defaults 2015-01-01 -> 2021-01-01). **Dev block only** (2015-01-01..2020-12-31, `splits.DEFAULT_PLAN`). The script drops every
  EUR/USD bar whose trading date is not `dev` and every index bar at or after 2021-01-01 UTC **before** any computation; val and OOS
  untouched.
- **Dates:** sorted EUR/USD dev trading dates (17:00 NY roll, SPEC 2) on Monday-Friday (weekend trading-date artefacts dropped and
  counted). "Previous" / "next" valid trading date = neighbour in this list (weekends and holidays held).
- **Quotes:** bid/ask **open** of the first 1-minute bar in [T, T+5 min) Europe/London on London calendar date D (E011 rule,
  `month_end_hedging.london_quotes`); missing -> excluded, never filled. 16:00 London always falls inside trading date D.
- **Signals (fixed in backlog R079):** index mid at 16:00 London on D. **No holiday fallback.**
  - B35: S1(D) = [ln EU(D) - ln EU(prev)] - [ln US(D) - ln US(prev)]; position -sign(S1).
  - B36: S20(D) = same with the date 20 places before D; position -sign(S20). First date (B35) / first 20 dates (B36) = burn-in.
- **Trade per date (both arms):** enter at the 16:05 London EUR/USD quote on D, exit at the 16:00 London quote on the next date.
  Signed return = position x (mid exit - mid entry) / pip. Trades never overlap.
  Exclusions per arm, counted, first reason in this order: `burn_in`, `missing_index_quote` (either index, either end),
  `zero_signal`, `missing_entry`, `missing_exit` (incl. the last dev date, no next date), `entry_skipped_spread` (ask-bid at entry
  > 2.0 pips, SPEC 4).
- **Data gate (first, 0 trials if it fails):** either index series empty, or no 16:00 London quote in either index on > 10% of dev
  dates -> BLOCKED; no trade result computed.
- **Statistic (2 trials):** `relative_equity.evaluate` (= `overnight_reversal.evaluate_b32`): mean, median, SD, hit rate, one-sided
  t-test (H1 mean > 0), moving-block bootstrap 95% CI of the mean (**block 20 dates**, 2000 draws, seed 0).
- **Decision rule (`decide_b35`, same for B36, unchanged from the backlog draft):**
  - < 500 tested dates -> **NONE** (insufficient sample).
  - **SIGNAL** if mean > 1.0 pip AND block-bootstrap CI lower > 0 AND one-sided t p < 0.025 (Bonferroni for 2 trials).
  - **WEAK** if mean > 0 and (CI lower > 0 or t p < 0.025), but not SIGNAL.
  - **NONE** otherwise.
- **Descriptive (not trials, do not change the decision):** contemporaneous corr(S1(D), EUR/USD 16:00 prev -> 16:00 D) and its sign
  (Hau-Rey predicts negative in this convention; if not, say so); |S| terciles; EU-only (-sign(EU return)) and US-only (+sign(US
  return)) legs; Mondays; Fridays (weekend hold); by year; share long; SD of the hold move; unconditional long EUR/USD on B35 dates;
  share of dates where B35 and B36 agree; results excluding FOMC statement dates (D in `data/calendars/fomc_dates.csv`, scheduled, not
  cancelled) and excluding dates where D or the next date is a month-end; median spreads; net per date at bid/ask, SPEC 4 (bid/ask net
  - 0.1 slippage - 0.1 commission) and costs x1.5 (gross - 1.5 x (gross - SPEC 4 net)).
- **What follows:**
  - SIGNAL in either arm -> B37 (val confirmation of that arm, own experiment and pre-registration, rule unchanged, p < 0.05 for one
    arm, < 0.025 if both). Not a LEAD until val passes and SPEC 4 and x1.5 net > 0.
  - WEAK or NONE in both -> B35 and B36 closed; B37 closed unearned; no re-test on dev with other windows, anchors or lags.
    Next: backlog refill (no other `ready` item).
- **Power note (written before data):** ~1,550 dev dates; 16:05 -> 16:00 next-date SD likely ~50 pips -> SE ~1.3 pips (block
  bootstrap may widen it); the p < 0.025 bar binds near +2.6 pips.
- **Calendar label:** entry just after the London 4pm fix; holds through the 08:30 NY releases, FOMC statements on D and the next
  fix (exit at it). Not a fix strategy.
- **Code:** `src/fxresearch/relative_equity.py`; `scripts/run_e037_relative_equity.py`; tests `tests/test_relative_equity.py`
  (constants fixed, B35 sign convention, 16:05 -> next 16:00 trade, B36 window and burn-in, no holiday fallback, exclusion order,
  side independent of later prices, data gate, random-walk SIGNAL rate <= 0.05 over 80 arm-seeds, injected effect -> SIGNAL and
  < 500 dates -> NONE, cost columns, quotes from bars at London 16:00/16:05). Synthetic smoke run passed.
- **Command (batch.sh):** `bash scripts/download_dukascopy_index.sh` (log to `E037_index_download.log`; failure does not fail the job,
  the data gate then records BLOCKED) then `python scripts/run_e037_relative_equity.py | tee
  backtests/validation_reports/E037_results.txt` (also writes `E037_results.json` and `E037_days.csv`).
- **Trial count:** dev +2 when it runs (244 -> 246); val unchanged at 9; total 253 -> 255.
