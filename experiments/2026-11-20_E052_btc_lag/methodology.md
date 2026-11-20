# E052 Methodology (pre-registered 2026-11-20 R308, before any run)

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask (repo pipeline). **Dev block only**; the script drops every EUR/USD bar whose
  FX trading date is not `dev` **before** any computation. Val and OOS untouched. BTC/USD: Dukascopy `btcusd` 1-minute bid/ask,
  downloaded on the runner (phase 1, `scripts/download_dukascopy_btc.sh`, 2017-05-07..2021-01-01, into data/raw_btc); the script
  also drops BTC bars at or after 2021-01-01 UTC.
- **Data gate (first, fixed now):** valid BTC quote at both 16:00 NY points on >= 90% of EUR/USD grid dates in
  [2017-05-09, 2020-12-31]; otherwise BLOCKED (0 trials), download fixed once or item blocked.
- **Quotes:** EUR/USD: `tsmom.daily_quotes` (bid/ask OPEN of the first bar in [16:00, 16:05) New York per trading date). BTC: same
  rule on NY calendar date D (`fomc.ny_edge_quotes`), bid/ask <= 0 or missing -> invalid; no fill, no fallback.
- **Signal:** B(D) = ln(BTC mid16(D)) - ln(BTC mid16(previous EUR/USD grid date)); Monday's B spans the weekend. s(D) = sign(B).
- **Hold:** signed = s(D) x (EUR/USD mid16(D+1) - mid16(D)) in pips, D+1 = next grid date.
- **Exclusions (counted, first failing check in this order):** `no_next`, `missing_now`, `missing_next`, `missing_btc`,
  `zero_signal` (B == 0), `btc_jump` (|B| > 0.50, bad-print guard).
- **No look-ahead:** s(D) uses BTC bar opens at 16:00 NY D and the previous date only, the same instant as the EUR/USD entry open.
  Tests in `tests/test_btc_lag.py`: truncating both series after the 16:00 NY D bar open leaves s(D) unchanged; perturbing BTC after
  it leaves s(D) unchanged; a random-walk series gives no SIGNAL.
- **Pre-registered decision rule (`btc_lag.decide_b64`, 1 dev trial):** < 500 tested dates -> NONE. SIGNAL if mean daily signed
  return > 1.0 pip AND moving-block bootstrap (block 20 dates, 2000 draws, seed 0) 95% CI lower > 0 AND one-sided t-test p < 0.05.
  WEAK if mean > 0 and (CI lower > 0 or p < 0.05). Else NONE. SIGNAL earns B65 (val confirmation); NONE/WEAK close B65 unearned.
- **Descriptive only (not in rule):** hit rate; same-day corr(B, EUR/USD 16:00 -> 16:00); lag corr; by year; Mondays (weekend B)
  vs Tue-Fri; |B| terciles; buy-and-hold on the same dates; net per day at bid/ask, SPEC 4 and costs x1.5 (`tsmom.cost_summary`,
  swap/carry not included).
- **Cost model:** SPEC 4 (bid/ask, slippage 0.1 pip entry, commission 0.1 pip round trip), x1.5 stress. Descriptive.
- **Command:** `bash scripts/download_dukascopy_btc.sh; python scripts/run_e052_btc_lag.py | tee backtests/validation_reports/E052_results.txt`
  (outputs `E052_results.json`, `E052_results.txt`, `E052_daily.csv`, `E052_download.txt`). Synthetic smoke: `--synthetic`.
