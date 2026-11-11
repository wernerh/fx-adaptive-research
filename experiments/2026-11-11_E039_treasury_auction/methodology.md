# E039 Methodology (pre-registered 2026-11-11 R086, before any run)

- **Phase 1, auction calendar (runner):** `scripts/fetch_treasury_auctions.py` requests the Fiscal Data API endpoint
  `v1/accounting/od/auctions_query` (https://api.fiscaldata.treasury.gov) for auction dates **2015-01-01..2020-12-31 only** (dev; val
  and OOS calendars stay unread). Each page is tried at most twice; on failure the status is `failed` and E039 is **BLOCKED with 0
  trials**; no other source is substituted without a human decision. Raw records -> `backtests/validation_reports/E039_auctions_raw.csv`.
  Field names (`auction_date`, `security_type`, `security_term`, `original_security_term`, `closing_time_comp`,
  `inflation_index_security`, `floating_rate`, `cusip`) are UNVERIFIED until the runner reads them; the field list is logged.
- **Qualifying auctions (`treasury_auction.qualify`):** `security_type` Note or Bond (incl. reopenings); excluded: Bills, CMBs, TIPS
  (`inflation_index_security` = Yes or "TIPS" in type/term), FRNs (`floating_rate` = Yes or "FRN" in type/term).
- **Gate (fixed in backlog R085):** every full dev year 2015-2020 has 50-110 qualifying auctions AND >= 95% of qualifying auctions have a
  parsed competitive close time (`parse_close_time`: "01:00 PM", "1:00 PM", "13:00", "01:00:00 PM"). Gate failure -> BLOCKED; the
  parser may be fixed **once** (new pre-registration note, no result seen), else the item is blocked.
- **Descriptive data:** `scripts/download_dukascopy_ustb.sh` downloads US T-Bond CFD (`ustbondtrusd`) m1 bid/ask for 2019-2020 into
  data/raw_ustb. Its failure never blocks E039 and it never enters the decision.
- **EUR/USD data:** Dukascopy 1-minute bid/ask (repo pipeline), mid derived. **Dev block only** (`splits.DEFAULT_PLAN`): bars whose
  trading date is not `dev` are dropped before any computation.
- **Events:** distinct (D, T) pairs of qualifying auctions with a parsed close time; several auctions at the same T on D form one event,
  distinct times on one date are separate events. T is America/New_York (DST-aware).
- **Quotes (E011 rule):** bid/ask OPEN of the first 1-minute bar in [t, t+5 min); missing -> excluded, never filled.
- **Signal and entry:** window = (mid(T+10) - mid(T-10)) / pip; s = sign(window); entry at the T+10 quote (mid); entry skipped if
  ask - bid at T+10 > 2.0 pips (SPEC 4). The side uses only quotes at or before T+10 on D (no look-ahead, tested).
- **Exits:** trading dates = Mon-Fri dev trading dates (17:00 NY roll, `sessions.trading_date`). B40: 16:00 NY quote (`ny_quotes`, E019
  convention) on the 10th trading date after D; B41: on the 1st trading date after D. Signed return = s x (exit mid - entry mid) / pip.
- **Exclusions per arm, counted, first reason in this order:** `not_trading_date` (D not a dev weekday trading date),
  `missing_window`, `zero_signal`, `entry_skipped_spread`, `exit_outside_dev` (exit date beyond the dev block -> dropped),
  `missing_exit`.
- **Statistic (2 trials, one per arm):** mean, median, SD of signed; moving-block bootstrap 95% CI of the mean (**block 20 consecutive
  events in time order**, 2000 draws, seed 0, `roll_momentum.evaluate`); one-sided t-test p (H1 mean > 0). Note: B40 holds overlap,
  so the t p is overlap-naive; the block-bootstrap CI (required for SIGNAL) is the overlap-aware guard.
- **Decision rule (`treasury_auction.decide`, per arm, fixed in backlog R085):**
  - < 150 tested events -> **NONE** (insufficient sample).
  - **SIGNAL** if mean > 1.0 pip AND bootstrap CI lower > 0 AND one-sided t p < 0.025.
  - **WEAK** if mean > 0 and (CI lower > 0 or t p < 0.025), but not SIGNAL.
  - **NONE** otherwise. A SIGNAL in either arm earns B42 (val confirmation, own pre-registration). Not a lead on its own.
- **Cost model (SPEC 4, descriptive here):** net at bid/ask (half entry + half exit spread), minus slippage 0.1 and commission 0.1 pips;
  costs x1.5.
- **Descriptive (not trials, do not change the decision):** hit rate; OLS slope of arm return on window move; by tenor (short 2/3/5/7-y
  vs long 10/20/30-y original term); unconditional long; non-auction control (same T on the same weekday one week earlier, if that date
  had no qualifying auction); 2019-2020 `ustbondtrusd` window sign as signal and its sign agreement with the EUR/USD window; by year;
  close-time distribution.
- **Calendar label:** Treasury auction (scheduled supply event); not a fix, not a data release.
- **Trial count:** dev +2 when it runs (247 -> 249); val unchanged at 9; total 256 -> 258. 0 trials if BLOCKED.
- **Commands (GitHub Actions research-batch):**
  `python scripts/fetch_treasury_auctions.py`; `bash scripts/download_dukascopy_ustb.sh` (failure tolerated);
  `python scripts/run_e039_treasury_auction.py | tee backtests/validation_reports/E039_results.txt`
- **Outputs:** backtests/validation_reports/E039_results.{txt,json}, E039_events.csv, E039_calendar_parsed.csv, E039_auctions_raw.csv,
  E039_auctions_fetch.json, E039_ustb_download.log.
