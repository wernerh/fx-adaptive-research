# E050 Methodology (pre-registered 2026-11-16 R209, before any run)

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask (repo pipeline, cached on the runner). **Dev block only**
  (2015-01-01..2020-12-31, `splits.DEFAULT_PLAN`); the script drops every bar whose FX trading date is not `dev` **before** any
  computation. Val and OOS untouched. No external download.
- **Daily quotes:** `tsmom.daily_quotes` (unchanged E019 code): bid/ask OPEN of the first bar in [16:00, 16:05) New York on each
  trading date; NaN where missing. mid = (bid + ask) / 2.
- **Model returns:** r(D) = 1e4 x ln(mid16(D) / mid16(D-1)) for consecutive trading dates in the list with both quotes present;
  pairs with a missing quote are dropped from the model series and counted (`dropped_model_pairs`).
- **Model (fixed):** statsmodels `MarkovRegression(r, k_regimes=2, trend="c", switching_variance=True)`, `fit(disp=False)` defaults
  (EM then quasi-Newton), Gaussian, constant transition matrix. A fit counts as failed if it raises, reports
  `mle_retvals["converged"] = False`, or returns non-finite / non-positive parameters; then the previous parameters are kept and the
  failure counted. If the **first** fit fails the result is BLOCKED (0 trials), fixed and re-queued.
- **Walk-forward:** first fit on all model returns dated <= 2015-12-31. The trading dates after 2015-12-31 are walked in order with
  k = 0, 1, ...; at k = 21, 42, ... (every 21 trading dates, counted over all walked dates) the model is refitted on all model returns
  dated <= D before the signal of D is formed.
- **Signal:** filtered probabilities p(D) from this repo's Hamilton filter (`markov_switch.hamilton_filter`, start = stationary
  distribution) with the parameters in force at D over all model returns dated <= D. E8(D) = sum_{h=1..8} p(D)' P^h mu
  (P row-stochastic transition matrix, mu state means). s(D) = sign(E8(D)).
- **Daily outcome:** signed = s(D) x (mid16(D+1) - mid16(D)) in pips (D+1 = next trading date). Exclusions, counted in order:
  `missing_now`, `missing_next`, `flat` (E8 = 0 exactly), and `no_next` (last date).
- **No look-ahead:** tests in `tests/test_markov_switch.py`: truncating/perturbing prices after D leaves every s(D) unchanged (real
  statsmodels fitter); the filter uses r[:t+1] only; a random-walk series gives no SIGNAL.
- **Statistics and pre-registered decision rule (as B16/E019, `tsmom.decide_b16`, 1 dev trial):** SIGNAL if mean daily signed
  return > 1.0 pip AND moving-block bootstrap (block 20 dates, 2000 draws, seed 0) 95% CI lower > 0 AND one-sided t-test p < 0.05.
  WEAK if mean > 0 and (CI lower > 0 or p < 0.05), not SIGNAL. Else NONE. SIGNAL earns B61 (val confirmation); NONE/WEAK close B61
  unearned.
- **Descriptive only (not in rule):** sign flips, round trips and mean holding spell; net per round trip at bid/ask, SPEC 4 and costs
  x1.5 (`tsmom.cost_summary`, swap/carry not included); by year; long and short days; buy-and-hold on the same dates; E019 TSMOM
  signal on the same dates (agreement, mean); fit attempts/failures and fitted parameters; mean of the two state SDs.
- **Cost model:** SPEC 4 (bid/ask, slippage 0.1 pip entry, commission 0.1 pip round trip), x1.5 stress. Descriptive.
- **Command:** `python scripts/run_e050_markov_switch.py | tee backtests/validation_reports/E050_results.txt`
  (outputs `E050_results.json`, `E050_results.txt`, `E050_daily.csv`). Synthetic smoke: `--synthetic` (runs end to end).
- **Dependency:** statsmodels >= 0.14 added to pyproject (installed on the runner by `pip install -e ".[dev]"`).
