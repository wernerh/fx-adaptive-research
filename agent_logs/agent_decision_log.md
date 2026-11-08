# Agent decision log

Why each run chose what it did, and any judgement calls.

### 2026-11-07 R000
- **Decision:** first experiment is E001 (cost-free directional signal test), not a strategy backtest.
- **Reason:** cheapest way to test the core hypothesis; avoids tuning strategies on noise.
- **Decision:** added the unconditional benchmark to E001 after the literature review found documented time-of-day drift and fixing effects.
- **Decision:** default sessions anchored to local exchange clocks (Tokyo / London / New York), see SPEC 2.

### 2026-11-07 R001
- **Decision:** ran E001 via GitHub Actions; the workspace cannot reach Dukascopy and the user is away from their PC.
- **Decision:** applied the pre-registered rule exactly -> NONE. Did not run unregistered variants to find a positive result.
- **Decision:** deprioritised S002/S003 without formally rejecting them (statuses unchanged); their core premise is in rejected_hypotheses.md.

### 2026-11-07 R002
- **Decision:** ran E004 and E006 together (user request), both pre-registered and committed before the run (0a57f09).
- **Decision:** rejected S001 v0.1 and did not run val, per the rule.
- **Decision:** did NOT follow up the exploratory `lon_false_break_fade` 08:00-09:00 observation. It would be trial 23 on dev, chosen after seeing the data.
- **Recommendation for R003:** pivot away from session-price predictors. Candidates: (a) US data release reaction (S005; needs a historical calendar with timestamps); (b) time-of-day volatility timing for entry windows (predicting *when* to trade, not direction); (c) London-fix reversal (published mechanism, Krohn et al. 2024).

### 2026-11-07 R004 (unattended)
- **State:** no research-batch run queued or in progress; last batch (42395207715) already recorded in 7cc4427.
- **Decision:** took top `ready` backlog item B1 -> E007 London 4pm fix reversal, dev only, 4 trials. Pre-registered rule in experiments/2026-11-07_E007_london_fix_reversal/methodology.md, committed before the run.
- **Reason:** published mechanism (Krohn, Mueller & Whelan 2024; Evans 2018), a different information source from the three failed session-price tests, and data already available.

### 2026-11-07 R005 (unattended)
- **State:** research-batch run 42400981266 completed; outputs (0db6d13) not yet recorded -> Collect step.
- **Decision:** applied E007 rule exactly -> NONE on all 4 tests; B1v not queued. No lead; no notification.
- **Decision:** logged the wrong-sign month-end post-fix result as exploratory backlog B8, `parked` (not `ready`): post hoc, n=72, binomial n.s.

### 2026-11-07 R006 (unattended)
- **State:** no research-batch run queued or in progress; last batch (42400981266) already recorded in eece61e.
- **Decision:** took top `ready` backlog item B2 -> E008 volatility timing, dev only, 4 trials (2 predictors x 2 outcomes).
- **Judgement call (before any data):** decision statistic changed from the draft "IC of range/ATR vs |move|" to partial Spearman given prior ATR, because the random-walk test showed a shared-denominator bias (~+0.04). Rule is stricter (adds CI lower > 0). Recorded in methodology.md.

### 2026-11-07 R007 (unattended)
- **State:** research-batch run 42411061401 completed; outputs (0a4f98d) not yet recorded -> Collect step.
- **Decision:** applied E008 rule exactly -> NOT_USEFUL on all 4 tests; B2v not queued. No lead; no notification.
- **Next:** top `ready` backlog item is B3 (hourly return profile scan, exploratory, dev only).

### 2026-11-07 R008 (unattended)
- **State:** no research-batch run queued or in progress; last batch (42411061401) already recorded in 022a6c2.
- **Decision:** took top `ready` backlog item B3 -> E009 hourly return profile scan, exploratory, dev only, 192 cells (all counted as trials).
- **Rule fixed before data:** CANDIDATE needs |mean| >= 1 pip, bootstrap CI excluding 0, t p < 0.05/192 and sign p < 0.05; at most 3 candidates become val-only 1-trial backlog items. No lead can come from this scan alone.

### 2026-11-07 R009 (unattended)
- **State:** research-batch run 42420473476 completed; outputs (89082ec) not yet recorded -> Collect step.
- **Decision:** applied E009 rule exactly (re-checked from the JSON) -> CANDIDATES: Wed_ny_18, Thu_ny_18 (both long). Per the pre-registered follow-up rule, added B9/B10 (val only, 1 trial each) at the bottom of the backlog as `ready`; not re-ranked. Exploratory scan, so no lead; no notification.
- **Next:** top `ready` backlog item is B4 (ECB fix, dev).

### 2026-11-08 R010 (unattended)
- **State:** no research-batch run queued or in progress; last batch (42420473476) already recorded in 56295b1.
- **Decision:** took top `ready` backlog item B4 -> E010 ECB 14:15 CET fix reversal, dev only, 2 trials (pre short, post long), E007 rule with n_trials=2.
- **Noted before data:** post window contains 08:30 NY US releases on most days; a SIGNAL would need a release-day split at val before any lead claim.

### 2026-11-08 R011 (unattended)
- **State:** research-batch run 42429506649 completed; outputs (cda15e9) not yet recorded -> Collect step.
- **Decision:** applied E010 rule exactly -> WEAK overall (pre WEAK: +0.76 pips < 1.0 bar, p 0.53; post NONE). WEAK does not go to val; B4v not queued. No lead; no notification.
- **Next:** top `ready` backlog item is B5 (Tokyo fix, E011).

### 2026-11-08 R012 (unattended)
- **State:** no research-batch run queued or in progress; last batch (42429506649) already recorded in 03e47f7.
- **Decision:** took top `ready` backlog item B5 -> E011 Tokyo 09:55 JST fix reversal, dev only, 2 trials (pre short, post long), E007 rule with n_trials=2.
- **Added before data:** descriptive bid/ask cost check (median entry spread, net, net at costs x1.5), because B5 flags wider Asian-hours spreads. Not part of the decision rule. Gotobi-day subset deliberately not tested (would add trials).

### 2026-11-08 R013 (unattended)
- **State:** research-batch run 42438344654 completed; outputs (b985245) not yet recorded -> Collect step.
- **Decision:** applied E011 rule exactly -> WEAK overall (pre WEAK: +0.32 pips, CI includes 0, p 0.021; post WEAK: +0.79 pips < 1.0 bar despite CI > 0 and p 0.003). WEAK does not go to val; B5v not queued. No lead; no notification.
- **Judgement call:** descriptive post-window net (+0.48, x1.5 +0.32) is noted in knowledge but not used to re-rank or create a val item, because that would loosen the pre-registered size bar after seeing data.
- **Next:** top `ready` backlog item is B9 (NY 18:00 Wednesday drift, val only).

### 2026-11-08 R014 (unattended)
- **State:** no research-batch run queued or in progress; last batch (42438344654) already recorded in 2169b7e.
- **Decision:** took top `ready` backlog item B9 and, as the backlog allows, B10 in the same run -> E012, val only, 2 trials, each with the E009 follow-up rule (mean > 1.0 pip, CI lower > 0, binom p < 0.05). Experiment ID E012 reassigned from blocked B6 (which had no registry row).
- **Fixed before data:** a SIGNAL counts as a LEAD only if mean net at SPEC 4 costs (bid/ask + 0.1 slippage + 0.1 commission) and at costs x1.5 are both > 0 on val. Reason: E009 pooled ny_18 up-share 0.595 on all weekdays suggests a possible post-roll spread-normalisation artifact in mid quotes. E009 CANDIDATE (its pre-registered dev rule) is taken as lead criterion 1.
- **Next:** wait for the research-batch run, then Collect.

### 2026-11-08 R015 (unattended)
- **State:** research-batch run 42446726453 completed; outputs (82c6ccd) not yet recorded -> Collect step.
- **Decision:** dev reproduction matched E009 (n 312/313, +1.333/+1.240), so results are valid. Applied E012 rule exactly -> WEAK overall (Wed WEAK: +0.65 pips, CI includes 0, p 0.049; Thu NONE: +0.94 pips, p 0.14). Cost gate fails for both. Hypothesis rejected for these cells; no lead; no notification.
- **Next:** no `ready` backlog items (B6 blocked, B7/B8 parked) -> next run does a refill pass (step 4).

### 2026-11-08 R016 (unattended)
- **State:** no research-batch run queued or in progress; last batch (42446726453) already recorded in ed4dc35. No `ready` backlog items (B6 blocked, B7/B8 parked) -> Refill step (protocol step 4).
- **Pass:** literature on event-driven USD moves, following the E012 lesson (target liquid hours or event mechanisms). Verified: Mueller, Tahbaz-Salehi & Vedolin (2017, JF); Karnaukh (2018 WP); Almeida, Goodhart & Payne (1998, JFQA). Robot Wealth NFP-drift note logged as external (look-ahead, not testable).
- **Added:** B11 (FOMC statement-day long EUR/USD, dev, 1 trial) and B12 (NFP 15-min reaction continuation, dev, 1 trial), both with draft rules fixed now, before any data.
- **Not added:** Karnaukh's signalled-meeting drift (needs fed funds futures, no source); pre-NFP drift (look-ahead).
- **Blocker noted:** federalreserve.gov could not be opened from this workspace (fetch permission timeout). Event dates must come from official pages, fetched on the runner if needed; no dates typed from memory.
- **Next:** top `ready` item is B11; its first step is building and checking the FOMC date file.

### 2026-11-08 R017 (unattended)
- **State:** no research-batch run queued or in progress; last batch (42446726453) recorded in ed4dc35. Top `ready` backlog item: B11.
- **Decision:** pre-registered B11 as E013 (dev only, 1 trial; rule: mean > 10 pips AND block-bootstrap CI lower > 0 AND one-sided
  t p < 0.05). Bootstrap block fixed at 4 meetings before any data (meetings ~6 weeks apart).
- **Data route:** federalreserve.gov still blocked from this workspace (proxy 403), so B11 option (a): the runner fetches and parses
  the official pages and commits `backtests/calendars/` for review **before** the test runs. This batch does no experiment.
- **Next:** after the run, review the fetch report (8 scheduled meetings per year 2015-2023, source URLs, unscheduled actions listed).
  If valid, copy to `data/calendars/fomc_dates.csv` and queue phase 2 (`scripts/run_e013_fomc_day.py`). If not, fix the parser from
  the committed raw HTML and re-fetch (pipeline fix, not a new trial).

### 2026-11-08 R018 (unattended)
- **State:** research-batch run 42458841737 (E013 phase 1, FOMC date fetch) finished `success`; outputs in bec9c7b. No run queued.
- **Review of `backtests/calendars/fomc_fetch_report.json`:** `all_years_valid: false`. 2015, 2016, 2020 valid (historical pages);
  2021-2023 valid (fomccalendars.htm; historical pages 404). **2017 (6), 2018 (7), 2019 (7 scheduled) invalid.** Cause, from the
  committed raw HTML: the historical pages write cross-month meetings as `Jan/Feb 31-1 Meeting - 2017`, `Oct/Nov 31-1`,
  `Jul/Aug 31-1`, `April/May 30-1`; `parse_heading` only handled `April 30-May 1`. A second issue: 2020's
  `March 17-18 (cancelled) Meeting` was parsed as a normal scheduled meeting, but no statement was issued that day.
- **Decision (pipeline fix, no new trial, no price data seen):** fix the parser (slash cross-month headings) and add a `cancelled`
  flag. Cancelled slots still count toward the 8-per-year check (they were scheduled) but are excluded from the E013 test and listed,
  in the same way as unscheduled actions. This applies the methodology's intent (a statement day needs a statement); the window,
  rule, thresholds and block are unchanged. Tests added against the committed 2017-2019 raw pages (all now parse to 8).
- **Next:** re-queue phase 1 (re-fetch with the fixed parser). The following run reviews the new report; if every year is valid it
  promotes the CSV to `data/calendars/fomc_dates.csv` and queues phase 2. Pipeline failures so far on this line: 1 (parse).

### 2026-11-08 R019 (unattended)
- **State:** research-batch run 42462817989 (E013 phase 1 re-fetch) finished `success`; outputs in 952a8a1. No run queued.
- **Review of `backtests/calendars/fomc_fetch_report.json`:** `all_years_valid: true`; 8 scheduled meetings each year 2015-2023 (72);
  statement dates all weekdays; cross-month meetings correct (2017-02-01, 2017-11-01, 2018-08-01, 2019-05-01, 2023-02-01, 2023-11-01);
  unscheduled 2019-10-04, 2020-03-02, 2020-03-15 and cancelled 2020-03-18 flagged for exclusion. Source URL on every row.
- **Decision:** promote the file unchanged to `data/calendars/fomc_dates.csv` (test pins it to the runner output and the
  8-per-year / weekday / 47-dev-days checks) and queue E013 phase 2 exactly as pre-registered (dev only, 1 trial). No rule change.
- **Next:** record E013 results from `backtests/validation_reports/E013_results.json` with `fomc.decide_b11`.

### 2026-11-08 R020 (unattended)
- **State:** research-batch run 42467005834 (E013 phase 2, dev test) finished `success`; outputs in 48d4d0e, not yet recorded. No run queued.
  Protocol step 1 (collect). pytest 81 passed before recording.
- **Decision (rule applied exactly, `fomc.decide_b11`):** n 47, mean +21.284 pips > 10, block-4 CI (2.747, 38.163) lower > 0, one-sided t p 0.029 < 0.05 -> **SIGNAL** on dev.
  Cost gate passes on dev (SPEC 4 +20.81, x1.5 +20.57) but a LEAD needs a pre-registered val confirmation, so **no lead and no notification**.
- **Re-rank:** B11v (val confirmation, fixed by the E013 methodology before the run) is placed above B12. Reason: it is the only line
  that can produce a lead, its rule and window are already fixed, and the date file is validated, so it needs no new data work.
  B12 stays `ready` behind it.
- **Next run:** pre-register E014 = B11v (val only, 1 trial) with hypothesis/methodology/record.json/registry row before running; no OOS.

### 2026-11-08 R021 (unattended)
- **State:** latest research-batch run 42467005834 (E013 phase 2) already recorded in R020 (94dfc47). No run queued or in progress.
  Protocol step 3 (next experiment). pytest passed before any change.
- **Open questions:** B11v (val confirmation of E013 SIGNAL; `ready`, top), B12 NFP continuation (`ready`), B6 blocked (calendar), B7/B8 parked.
- **Decision:** pre-register and queue **E014 = B11v**, val only, 1 trial. Reason: it is the only open line that can produce a lead;
  window, rule, thresholds, bootstrap block and date file are fixed by E013 and unchanged. Expected val set: 20 scheduled statement days
  (2021-01-27..2023-06-14; test pins this). Script truncates bars to 2021-01-01..2023-06-30 so OOS is never read.
- **Next run:** record E014 from `backtests/validation_reports/E014_results.json` with `fomc.decide_b11` and the LEAD cost gate.

### 2026-11-08 R022 (unattended)
- **State:** research-batch run 42475560383 (E014, queued in R021) completed success; outputs committed by github-actions[bot] in 671906f, not yet recorded.
  Protocol step 1 (collect). pytest passed (82) before any change.
- **Decision (rule applied exactly, `fomc.decide_b11`):** n 20, mean +19.99 > 10 but block-4 CI (-9.53, 51.02) lower <= 0 and one-sided t p 0.115 >= 0.05
  -> neither SIGNAL nor WEAK -> **NONE**. LEAD criterion 2 fails; no notification, no LEADS.md.
- **Consequence:** B11 line closed (rejected_hypotheses: not confirmed on val). OOS is not touched and not requested.
- **Next run:** top `ready` item is B12 (NFP 15-min reaction continuation, dev, 1 trial); needs the BLS release-date file fetched on the runner first.

### 2026-11-08 R023 (unattended)
- **State:** latest research-batch run 42475560383 (E014) already recorded in R022 (75ba047). No run queued or in progress.
  Protocol step 3 (next experiment). pytest passed before any change.
- **Open questions:** B12 NFP continuation (`ready`, top), B6 blocked (calendar), B7/B8 parked. No other `ready` items.
- **Decision:** pre-register **E015 = B12**, dev only, 1 trial. Reason: only `ready` item; monthly events answer the E014 lesson
  (~72 dev / ~29 val releases, so a dev SIGNAL can be confirmed on val); 08:45-09:45 NY is a liquid hour; builds the first piece of B6's calendar.
- **Phase 1 queued:** `scripts/fetch_nfp_dates.py` on the runner (bls.gov unreachable here: proxy 403). Source: BLS archive index
  `empsit.htm`; dates parsed from `empsit_MMDDYYYY.htm` links, never typed. Rule, windows and thresholds fixed in the E015 methodology now.
- **Risk:** BLS may refuse automated requests (403) from the runner too; the report records the HTTP status and the next run diagnoses.
- **Next run:** review `backtests/calendars/nfp_fetch_report.json` (12/yr, one per month, weekdays); promote and queue phase 2, or fix and re-fetch.

### 2026-11-08 R024 (unattended)
- **State:** research-batch run 42484931936 (E015 phase 1, BLS NFP date fetch) completed `success`; outputs in b8abbd6 (github-actions[bot]),
  not yet reviewed. No run queued or in progress. Protocol step 1 (collect). pytest passed (93) before any change.
- **Review of `backtests/calendars/nfp_fetch_report.json`:** HTTP 403, body "Access Denied"; 0 links parsed; `all_years_valid: false`.
  The date file is empty, so phase 2 cannot run.
- **Decision:** the 403 is the source refusing automated access, not a parser fault. A fix that tried alternative user agents / HTTP
  clients until one got through was drafted and then **dropped**: it would be bot-check circumvention. No workaround via mirrors or
  web caches either. E015 stays `preregistered` (0 trials); B12 set to `blocked`. Rule, windows, thresholds unchanged.
- **Needs human (not urgent, not a lead):** a sanctioned NFP release-date source, e.g. add a `FRED_API_KEY` Actions secret (FRED API
  release dates for the Employment Situation) or commit an official BLS schedule file by hand-download. Changing the source requires
  a dated data-rule note in backlog B12 before the re-fetch.
- **Pipeline:** the research-batch workflow itself is healthy (5/5 recent runs success); this is a single-source data block, so no
  "pipeline blocked" notification. Next run: no `ready` items remain (B6/B12 blocked, B7/B8 parked) -> refill pass (step 4).
