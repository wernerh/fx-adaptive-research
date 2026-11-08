# E015 Methodology (pre-registered 2026-11-08 R023, before any run; code at parent commit 75ba047 + this commit)

## Two phases (backlog B12 data rule; same pattern as E013)
1. **Phase 1, date file (this run):** `scripts/fetch_nfp_dates.py` runs on the research-batch runner (this workspace cannot reach
   bls.gov), downloads the official BLS archive index `https://www.bls.gov/bls/news-release/empsit.htm`, parses the archived
   release links `empsit_MMDDYYYY.htm` (release date in the file name) with `fxresearch.nfp`, and commits
   `backtests/calendars/nfp_dates.csv`, `nfp_fetch_report.json` and the raw index page. **No experiment runs in phase 1 and no
   price data are used.** Release dates are not derived from a "first Friday" rule and none is typed by hand.
2. **Review (next run):** every year 2015-2023 valid (exactly 12 releases, one per calendar month, all on weekdays); non-Friday
   releases listed (allowed; e.g. holiday shifts); every row carries the source URL and archive link. Only then is the file
   copied to `data/calendars/nfp_dates.csv` and phase 2 queued. If the fetch or parse fails (e.g. HTTP 403), fix from the report /
   raw page and re-fetch; the test definition below does not change.
3. **Phase 2, test:** `python scripts/run_e015_nfp_continuation.py | tee backtests/validation_reports/E015_results.txt`.

## Test definition (fixed now)
- **Data:** Dukascopy EUR/USD 1-minute bid/ask, mid derived. **Dev block only** (release dates 2015-01-01..2020-12-31,
  `splits.DEFAULT_PLAN`; bars truncated before 2021-01-01 inside the script). Expected n ~72.
- **Release time:** 08:30 America/New_York for every release (BLS standard). DST via the IANA tz database.
- **Quotes (`nfp.reaction_frame`):** P0 = mid open of first bar in [08:30, 08:35) NY; P1 = mid close of last bar in [08:40, 08:45);
  E = mid open of first bar in [08:45, 08:50); X = mid close of last bar in [09:40, 09:45).
  r1 = P1 - P0, r2 = X - E (pips). r1 uses only bars before 08:45, r2 only bars from 08:45 (tested: no look-ahead).
  A release with any missing edge quote is dropped and listed (never filled).
- **Signed return:** sign(r1) x r2 if |r1| >= 1.0 pip; otherwise 0 (no trade). **No-trade days stay in n** for mean, t and CI.
- **Trials:** 1 (dev). Reversal reading and benchmark are descriptive, not trials.
- **Statistics (`nfp.evaluate`):** n, n_traded, n_no_trade, mean / median / sd of signed return, moving-block bootstrap 95% CI of the
  mean (block 4 releases, 2000 draws, seed 0; block 4 as in E013 for sparse events), binomial test of continuation share among
  traded days with r2 != 0 (one-sided, H1 > 0.5).
- **Decision rule (`nfp.decide_b12`, B1 rule with 1 trial):**
  - **SIGNAL** if mean signed > 1.0 pip AND block-bootstrap CI lower > 0 AND binomial p < 0.05.
  - **WEAK** if mean signed > 0 and (CI lower > 0 or binomial p < 0.05), but not SIGNAL.
  - **NONE** otherwise. If mean < 0 with CI upper < 0, `reversal_exploratory = true` is logged only; a reversal test needs its
    own pre-registration and val data.
- **Cost check (descriptive; gates only the LEAD label):** traded days only; enter at the 08:45 bid/ask open in the signal
  direction, exit at the 09:45 bid/ask close; SPEC 4 net = bid/ask net - 0.1 pip slippage - 0.1 pip commission; costs x1.5 net =
  gross - 1.5 x (gross - SPEC 4 net). Median entry spread at 08:45 reported.
- **Descriptive (not trials):** same windows on all other dev Fridays (non-NFP benchmark); per-year counts and means; per-release table.
- **Power note (written before data):** the sd of r2 on release days is not known yet. CI half-width ~ 2 x sd / sqrt(72) ~ 0.24 sd
  on dev; val has ~29 releases (Feb 2021..Jun 2023), so a val confirmation needs a mean of roughly 0.37 sd or more.
- **What follows:**
  - SIGNAL -> pre-register B12v (val only, same window and rule, 1 trial). Not a LEAD until val confirms and the cost gate passes.
  - WEAK / NONE -> B12 closed; no re-test with other windows or thresholds on dev.
- **Code:** `src/fxresearch/nfp.py`, `scripts/fetch_nfp_dates.py`, `scripts/run_e015_nfp_continuation.py`; tests `tests/test_nfp.py`
  (index parser incl. html/pdf dedup and invalid dates; 12-per-year / one-per-month validation; DST-aware edges; no look-ahead;
  missing quotes -> NaN; no-trade days in n; bid/ask net; decision rule; random-walk no-SIGNAL).
- **Trial count:** dev +1 when phase 2 runs (227 -> 228; total 230 -> 231).
