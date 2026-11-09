# E021 Methodology (pre-registered 2026-11-09 R039, before any run)

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask, mid derived. **Dev block only** (2015-01-01..2020-12-31,
  `splits.DEFAULT_PLAN`). The script drops every bar whose trading date is not `dev` **before** any computation; val and OOS untouched.
- **Quote at hh:mm NY on NY date d:** bid/ask **open** of the first bar in [hh:mm, hh:mm+5) America/New_York
  (`daily_reversal.ny_quotes`). Missing -> excluded, never filled. No timestamp between 16:30 and 18:30 NY is used (R030 lesson).
- **Trading dates:** the sorted set of `sessions.trading_date` values present in the dev bars (17:00 NY roll).
- **Daily move:** R(D) = (mid 16:00 NY on D - mid 16:00 NY on P) / pip, P = the trading date immediately before D in that set.
  Excluded and counted, first reason in this order: `no_prev` (first date), `missing_16_D`, `missing_16_prev`. The rest are "valid".
- **Large:** a valid D is large if |R(D)| > `np.percentile(|R| of the previous 60 valid dates, 80)` (numpy default linear
  interpolation, strictly greater, past only). The first 60 valid dates are burn-in. All valid dates, Fridays included, enter the
  rolling history.
- **Trade per large D:** position -sign(R(D)) from 20:00 NY on calendar date D (start of the next trading date N, after the roll and
  the Tokyo open) to 10:45 NY on calendar date N (before the London 4pm fix at 11:00 NY). Exclusions, counted, first reason in this
  order: `friday` (D is a Friday); `next_not_adjacent` (N missing or N != D + 1 calendar day, e.g. holidays); `missing_entry`;
  `missing_exit`; `entry_skipped_spread` (ask-bid at entry > 2.0 pips, SPEC 4).
- **Statistic (1 trial):** signed return per tested event = -sign(R(D)) x (mid exit - mid entry) / pip. `daily_reversal.evaluate`:
  mean, median, SD, hit rate, one-sided t-test (H1 mean > 0), moving-block bootstrap 95% CI of the mean (block 10 events, 2000 draws,
  seed 0).
- **Decision rule (`daily_reversal.decide_b18`), unchanged from the backlog draft:**
  - **SIGNAL** if mean > 1.0 pip AND block-bootstrap CI lower > 0 AND one-sided t p < 0.05.
  - **WEAK** if mean > 0 and (CI lower > 0 or t p < 0.05), but not SIGNAL.
  - **NONE** otherwise.
- **Descriptive (not trials, do not change the decision):** the 16:00-20:00 NY move on D signed against R(D) (reversal before entry,
  not tradable under our rules); the same 20:00 -> 10:45 trade on non-large, non-Friday valid dates after burn-in (control); up-move
  and down-move events separately; by year; median spreads at entry and exit; net per event at bid/ask (half spread at entry and at
  exit), SPEC 4 (bid/ask net - 0.1 slippage - 0.1 commission) and costs x1.5 (gross - 1.5 x (gross - SPEC 4 net)); median threshold;
  count of events whose move day D or exit day N is a scheduled FOMC statement date (`data/calendars/fomc_dates.csv`). A significant
  negative mean (continuation) is logged as exploratory only and needs its own pre-registration on fresh data.
- **What follows:**
  - SIGNAL -> queue val confirmation B18v as its own experiment with this rule unchanged (LEAD needs dev SIGNAL + val pass + SPEC 4
    and x1.5 net > 0).
  - WEAK or NONE -> B18 closed for this definition; no re-test with other thresholds, windows or horizons on dev.
- **Power note (written before data):** ~1,500 dev trading dates, ~1,200 non-Friday, ~240 events after burn-in; ~15 h SD ~35-40 pips
  -> SE ~2.5 pips; only a mean of ~5 pips clears the CI bar. A NONE does not rule out a small effect.
- **Calendar label:** daily-move reversal; the hold contains the Tokyo fix, the ECB fix (08:15 NY) and US 08:30 releases; it ends
  before the London 4pm fix (11:00 NY).
- **Code:** `src/fxresearch/daily_reversal.py`, `scripts/run_e021_daily_reversal.py`; tests `tests/test_daily_reversal.py`
  (constants fixed, past-only strict threshold, Friday exclusion, no look-ahead, spread skip, non-adjacent next date, cost ordering,
  16:00/20:00/10:45 quotes from bars, missing bar counted, random walk no SIGNAL (5 seeds), strong reversal gives SIGNAL, rule edges,
  FOMC overlap). Synthetic smoke run passed (no events: 43 valid dates < 60 burn-in, as expected).
- **Command:** `python scripts/run_e021_daily_reversal.py | tee backtests/validation_reports/E021_results.txt` (also writes
  `E021_results.json` and `E021_days.csv`).
- **Trial count:** dev +1 when it runs (230 -> 231); val unchanged at 4; total 234 -> 235.
