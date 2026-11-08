# E016 Methodology (pre-registered 2026-11-08 R026, before any run; code at parent commit f071847 + this commit)

## Two phases (backlog B13 data rule; same pattern as E013/E015)
1. **Phase 1, settlement time (this run):** `scripts/fetch_cme_settlement.py` runs on the research-batch runner and downloads
   official CME Group pages (`fxresearch.cme_settle.SOURCE_URLS`): the Daily Settlement Time Ranges PDF and the Client Systems
   Wiki pages "Daily Settlement Time Details" and "Euro". It saves the raw files and extracted text under
   `backtests/calendars/raw_html/` and writes `backtests/calendars/cme_settlement_fetch_report.json` (HTTP status, final URL,
   sha256, FX windows found). **No experiment runs in phase 1 and no price data are used.** No time is typed by hand.
   - Pre-registration context (not the source of S): in R026 a web-fetch from this workspace opened the Daily Settlement Time
     Ranges PDF (HTTP 200), which lists one FX row: "FX: 13:59:30-14:00:00 CT" (undated, not split by FX product). The two
     Wiki pages redirected to cmegroupclientsite.atlassian.net and could not be read here. The runner copy is the record.
2. **Review (next run):** valid only if (a) at least one official page gives an FX (or Euro FX) settlement window, (b) all
   windows found agree on the end time S, and (c) nothing read states a different FX settlement time or a change of it during
   2015-2020. S = the window END (the settlement instant). If a page is refused (401/403/429, "Access Denied"), it is recorded
   and not worked around. If no page establishes the time for the dev period, the item stays blocked; the test definition
   below does not change. Only then is `data/calendars/cme_fx_settlement.json` written
   (`settle_time_ct`, `source_url`, `reviewed: true`, review notes) and phase 2 queued.
   - Known limitation (written now): the PDF is undated. If the reviewed sources show the current time only and no change
     history, the review records the assumption "S unchanged over 2015-2020" as a risk in the conclusion; it does not block.
3. **Phase 2, test:** `python scripts/run_e016_cme_settle_momentum.py | tee backtests/validation_reports/E016_results.txt`.

## Test definition (fixed now)
- **Data:** Dukascopy EUR/USD 1-minute bid/ask, mid derived. **Dev block only** (trading dates 2015-01-01..2020-12-31,
  `splits.DEFAULT_PLAN`; bars truncated before 2021-01-01 inside the script). Weekday trading dates (Mon-Fri, `sessions.trading_date`).
  Expected n ~1,500. US/CME holidays and early-close days are **not** excluded (no exchange calendar in the repo); they dilute
  the effect and are a stated limitation.
- **Times:** S in America/Chicago on the calendar date of trading date D; DST via the IANA tz database (Chicago and New York
  share US DST rules, so S - 30 is a fixed NY time too).
- **Quotes (`cme_settle.momentum_frame`):** P0 = mid open of the first bar of trading date D, only if that bar is within 60
  minutes after the 17:00 NY roll (late Sunday opens are allowed; later -> dropped); P1 = mid close of the last bar in
  [S-35, S-30) CT; E = mid open of the first bar in [S-30, S-25) CT; X = mid close of the last bar in [S-5, S) CT.
  r1 = P1 - P0, r2 = X - E (pips). r1 uses only bars before S-30, r2 only bars from S-30 (tested: no look-ahead).
  A day with any missing edge quote is dropped and listed (never filled).
- **Signed return:** sign(r1) x r2 if |r1| >= 1.0 pip; otherwise 0 (no trade). **No-trade days stay in n.**
- **Trials:** 1 (dev). OLS slope, per-year and per-weekday tables and the reversal reading are descriptive, not trials.
- **Statistics (`cme_settle.evaluate`):** n, n_traded, n_no_trade, mean / median / sd of signed return, moving-block bootstrap
  95% CI of the mean (block 20 days, 2000 draws, seed 0; SPEC default block for daily series), one-sided binomial test of the
  continuation share among traded days with r2 != 0 (H1 > 0.5).
- **Decision rule (`cme_settle.decide_b13`, B1 rule, 1 trial):**
  - **SIGNAL** if mean signed > 1.0 pip AND block-bootstrap CI lower > 0 AND binomial p < 0.05.
  - **WEAK** if mean signed > 0 and (CI lower > 0 or binomial p < 0.05), but not SIGNAL.
  - **NONE** otherwise. Mean < 0 with CI upper < 0 sets `reversal_exploratory = true` (logged only; needs its own pre-registration).
- **Cost check (descriptive; gates only the LEAD label):** traded days; enter at the S-30 bid/ask open in the signal direction,
  exit at the bid/ask close of the last bar before S; SPEC 4 net = bid/ask net - 0.1 slippage - 0.1 commission; costs x1.5 net =
  gross - 1.5 x (gross - SPEC 4 net). Median entry spread reported.
- **Dropped from the backlog draft before data:** the next-day reversal reading (descriptive only; not needed for the rule).
- **Power note (written before data):** 30-minute US-afternoon moves are small relative to a daily hold; with n ~1,500 the CI
  half-width is expected to be well under 1 pip, so the 1-pip mean bar (about a retail round trip) will usually bind.
- **What follows:**
  - SIGNAL -> pre-register B13v (val only, same S, window and rule, 1 trial). Not a LEAD until val confirms and the cost gate passes.
  - WEAK / NONE -> B13 closed; no re-test with other windows, thresholds or settlement-adjacent times on dev.
- **Code:** `src/fxresearch/cme_settle.py`, `scripts/fetch_cme_settlement.py`, `scripts/run_e016_cme_settle_momentum.py`;
  tests `tests/test_cme_settle.py` (FX-row parser, conflicting/implausible windows, reviewed-file guard, CT edges, no look-ahead,
  missing quotes -> NaN, no-trade days in n, bid/ask net, decision rule, random-walk no-SIGNAL).
- **Trial count:** dev +1 when phase 2 runs (227 -> 228; total 230 -> 231).
