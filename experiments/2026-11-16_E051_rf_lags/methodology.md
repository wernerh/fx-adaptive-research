# E051 Methodology (pre-registered 2026-11-16 R212, before any run)

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask (repo pipeline, cached on the runner). **Dev block only**
  (2015-01-01..2020-12-31, `splits.DEFAULT_PLAN`); the script drops every bar whose FX trading date is not `dev` **before** any
  computation. Val and OOS untouched. No external data download (scikit-learn installed by pip from pyproject).
- **Daily quotes:** `tsmom.daily_quotes` (unchanged E019 code): bid/ask OPEN of the first bar in [16:00, 16:05) New York on each
  trading date; NaN where missing. mid = (bid + ask) / 2.
- **Returns on the trading-date grid:** ret[i] = 1e4 x ln(mid16(D_i) / mid16(D_{i-1})); NaN if either quote is missing.
- **Features at D_i:** ret[i], ret[i-1], ..., ret[i-9] (10 lags counted in trading-date positions; a gap is NOT skipped over).
  Usable only if all 10 are finite.
- **Label of row i:** 1 if ret[i+1] > 0, 0 if ret[i+1] < 0; dropped from training if ret[i+1] is 0 or NaN. Label date = D_{i+1}.
- **Model (fixed):** `sklearn.ensemble.RandomForestClassifier(n_estimators=51, random_state=0)`, all other arguments at library
  defaults; scikit-learn pinned to 1.9.1 in pyproject (version printed and saved in the result JSON). A fit counts as failed if it
  raises or the training labels have fewer than 2 classes; then the previous model is kept and the failure counted. If the **first**
  fit fails the result is BLOCKED (0 trials), fixed and re-queued.
- **Walk-forward:** first fit on all usable rows with label date <= 2015-12-31. The trading dates after 2015-12-31 are walked in
  order with k = 0, 1, ...; at k = 21, 42, ... (every 21 trading dates, counted over all walked dates) the model is refitted on all
  usable rows with label date <= D before the signal of D is formed. Model frozen between refits.
- **Signal:** p(D) = predicted probability of class 1 for the features at D; s(D) = +1 if p > 0.5, -1 if p < 0.5.
- **Daily outcome:** signed = s(D) x (mid16(D+1) - mid16(D)) in pips. Exclusions, counted, first failing check in this order:
  `no_next` (last date), `missing_now`, `missing_next`, `missing_lag`, `flat` (p = 0.5 exactly).
- **No look-ahead:** tests in `tests/test_rf_lags.py`: perturbing prices after position i leaves every p(D), s(D) at positions <= i
  unchanged (real scikit-learn fitter); training rows at a refit on D have label date <= D (checked via row counts); a random-walk
  series gives no SIGNAL; a synthetic strong-continuation series is learned (sanity).
- **Statistics and pre-registered decision rule (as B16/E019/E050, `tsmom.decide_b16`, 1 dev trial):** SIGNAL if mean daily signed
  return > 1.0 pip AND moving-block bootstrap (block 20 dates, 2000 draws, seed 0) 95% CI lower > 0 AND one-sided t-test p < 0.05.
  WEAK if mean > 0 and (CI lower > 0 or p < 0.05), not SIGNAL. Else NONE. SIGNAL earns B63 (val confirmation); NONE/WEAK close B63
  unearned.
- **Descriptive only (not in rule):** hit rate; sign flips, round trips; net per day at bid/ask, SPEC 4 and costs x1.5
  (`tsmom.cost_summary`, swap/carry not included); by year; long and short days; buy-and-hold on the same dates; E019 TSMOM and E050
  (from the committed `E050_daily.csv`) on the same dates; mean and quantiles of p(D); feature importances at the last refit; fit
  counts.
- **Cost model:** SPEC 4 (bid/ask, slippage 0.1 pip entry, commission 0.1 pip round trip), x1.5 stress. Descriptive.
- **Command:** `python scripts/run_e051_rf_lags.py | tee backtests/validation_reports/E051_results.txt`
  (outputs `E051_results.json`, `E051_results.txt`, `E051_daily.csv`). Synthetic smoke: `--synthetic` (runs end to end).
