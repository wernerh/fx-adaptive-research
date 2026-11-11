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

### 2026-11-08 R025 (unattended)
- **State:** latest research-batch run 42484931936 (E015 phase 1) already recorded in R024 (042cd44). No run queued or in progress.
  No `ready` backlog items (B6/B12 blocked, B7/B8 parked) -> Refill step (protocol step 4). pytest passed (93) before any change.
- **Pass:** this workspace could not open any page this run (fetch permission timeout on nd.edu, cmegroup.com, snb.ch, doi.org). No new
  citation is added to research/. Both new items rest on entries already VERIFIED (abstract) on 2026-11-07 (Baltussen et al. 2021;
  Breedon & Ranaldo 2013); the one new factual input (CME Euro FX settlement time) is marked UNVERIFIED and must be fetched on the runner.
- **Added:** B13 (intraday momentum into the CME FX futures settlement, dev, 1 trial; phase 1 = official settlement time on runner) and
  B14 (home-hours depreciation: short 03:00-08:00 NY, long 12:00-17:00 NY, val only, 1 trial). Windows and draft rules fixed now, before data.
- **Ranking:** B13 above B14. B13 has a recent multi-asset publication incl. currencies, a liquid US-afternoon window, and leaves val clean
  for confirmation; B14 can only use val (dev scanned in E009), so it cannot reach LEAD status without an OOS decision, and E001 lowers its prior.
- **Not added:** a 17:00 NY roll-anchored intraday-momentum variant (roll-hour spreads 1.5+ pips, E012 lesson).
- **Next run:** pre-register B13 (E016); phase 1 fetches the CME settlement procedure page on the runner; a 403 blocks the item (no circumvention).

### 2026-11-08 R026 (unattended)
- **State:** latest research-batch run 42484931936 already recorded (R024). No run queued or in progress. pytest passed (93) before
  any change. Top `ready` item: B13 (intraday momentum into the CME FX futures settlement) -> protocol step 3, pre-register as E016.
- **Why B13 (unchanged from R025 ranking):** published multi-asset mechanism incl. currencies, liquid US-afternoon window, keeps val
  clean for confirmation; B14 can only use val.
- **Source check before pre-registering (R024 lesson):** a web-fetch from this workspace opened
  https://www.cmegroup.com/market-data/files/Daily-Settlement-Time-Ranges.pdf (HTTP 200): one FX row, "FX: 13:59:30-14:00:00 CT"
  (undated, not split by product). The two Client Systems Wiki pages redirect to cmegroupclientsite.atlassian.net and could not be
  read here. So CME permits automated access to at least one official source. The value is NOT used yet: phase 1 fetches the pages
  on the runner and saves them; the next run reviews and promotes S. https://www.cmegroup.com/notices/ser/2020/09/SER-8591.pdf was
  also opened: it moved equity-index settlement (3:15 -> 3:00 pm CT, Oct 2020) and says nothing about FX.
- **Fixed before data:** window r1 = roll -> S-30, r2 = S-30 -> S (CT), 1-pip no-trade band, B1 rule, block-20 bootstrap, dev only,
  1 trial. Holidays/early closes not excluded (no exchange calendar). Dropped the backlog's descriptive next-day reversal reading.
- **Risk:** the PDF is undated; if no source shows S over 2015-2020, the review records the "unchanged S" assumption as a risk.
- **Next run:** review the phase-1 report; promote and queue phase 2, or block (no circumvention of a refusal).

### 2026-11-08 R027 (unattended)
- **State:** research-batch run 42500439921 (E016 phase 1) completed; outputs committed by github-actions[bot] (4942183) and not yet
  reviewed -> protocol step 1 (collect). pytest passed (102) before any change.
- **Review:** all three official CME URLs returned `TimeoutError` after 60 s (http_status -1, no body). Not a refusal, not valid;
  nothing promoted, no price data touched, 0 trials used.
- **Decision:** diagnose as a transport timeout and re-queue phase 1 once, with a 120 s timeout and up to 3 attempts on transport
  errors only (refusals final), same honest User-Agent and URLs. A stop rule was written into the E016 methodology before the
  re-fetch: a second failure blocks B13 (silent timeouts treated as refusal; no further workaround).
- **Why not fetch in-session instead:** the E016 methodology fixes the runner copy as the record; changing that after a failed run
  would be a protocol change, not a fix.
- **Next run:** review the re-fetch report; promote S and queue phase 2, or block B13 and move to B14.

### 2026-11-08 R028 (unattended)
- **State:** research-batch run 42504753112 (E016 phase-1 re-fetch) completed; outputs committed by github-actions[bot] (f543bec)
  and not yet reviewed -> protocol step 1 (collect). pytest passed (103) before any change.
- **Review:** all three CME URLs timed out on all 3 attempts (120 s each); `valid: false`, no settlement window.
- **Decision:** apply the R027 stop rule exactly: E016/B13 `blocked`, 0 trials, no further fetch attempts. Not a pipeline failure
  (the workflow itself succeeded), so no human notification; B12 and B13 both await a human source decision.
- **Next run:** top `ready` item is B14 (home-hours depreciation, val only, 1 trial, data in repo).

### 2026-11-08 R029 (unattended)
- **State:** last research-batch run 42504753112 already recorded (R028); no run queued or in progress -> protocol step 3 (next experiment).
  pytest passed (103) before any change.
- **Pick:** B14 (home-hours depreciation, val only, 1 trial) is the top `ready` item; B6/B12/B13 blocked, B7/B8 parked.
- **Source check:** tried the SNB working paper 2012-04 page, its PDF and the DOI page via web-fetch; all failed (fetch-permission
  timeout, nothing read). Paper hour definitions stay UNVERIFIED; the R025 windows (03:00-08:00 and 12:00-17:00 NY) are used unchanged.
- **Fixed before data:** both legs required per date (>= 275/300 bars each), B1 rule, block-20 bootstrap, val only; SPEC 4 costs per leg
  (2 round trips/day); max-spread rule reported, not applied. A val SIGNAL surviving x1.5 is a human-OOS candidate, not a LEAD.
- **Next run:** collect E017 results from the research-batch run.

### 2026-11-08 R030 (unattended)
- **State:** research-batch run 42515271388 (E017) finished successfully; outputs committed in 86f67f5 and not yet recorded -> protocol step 1 (collect).
  pytest passed (112).
- **Decision:** pre-registered B1 rule applied exactly: mean +2.179 > 1 and CI lower 0.001 > 0, but binomial p 0.451 -> **WEAK**.
  Cost gate fails (SPEC 4 -0.382, x1.5 -1.663). Not a human-OOS candidate, not a LEAD; no notification.
- **Next run:** no `ready` backlog items (B6/B12/B13 blocked, B7/B8 parked) -> refill pass, preferring inputs already in the repo.

### 2026-11-08 R031 (unattended)
- **State:** last research-batch run 42515271388 (E017) already recorded (R030, 5df2345); no run queued or in progress. No `ready`
  backlog items (B6/B12/B13 blocked, B7/B8 parked) -> protocol step 4 (refill). pytest passed (112) before any change.
- **Literature pass:** opened (HTTP 200) the RePEc record for Moskowitz, Ooi & Pedersen (2012, JFE) and the FRBNY Staff Report 150 page
  plus RePEc record for Osler (2002, price cascades). Osler's 2005 journal venue was not on the pages: marked UNVERIFIED.
- **Selection criteria (R028/R030 lessons):** inputs already in the repo (price data only, no external source); not a time-of-day
  window (dev was scanned by E009); no entries/exits between 16:30 and 18:30 NY.
- **Added:** B15 round-number crossing continuation (dev, 1 trial, B1 rule) and B16 12-month time-series momentum with 16:00-16:00 NY
  daily hold (dev, 1 trial, mean/CI/t rule). Ranked B15 above B16: higher power (~2,000 events vs ~1,250 overlapping days) and a
  microstructure mechanism closer to the project's intraday focus. 0 trials used.
- **Next run:** pre-register B15 as E018.

### 2026-11-08 R032 (unattended)
- **State:** last research-batch run 42515271388 (E017) already recorded (R030); no run queued or in progress -> protocol step 3.
  pytest passed (112) before any change.
- **Pick:** B15 (round-number crossing continuation, dev, 1 trial) is the top `ready` item; B6/B12/B13 blocked, B7/B8 parked; B16 next.
- **Fixed before data (beyond the backlog draft, all mechanical):** crossing price = mid close held as integer (exact levels);
  down-crossing = mid(t-1) > L >= mid(t) (mirror of the up rule); crossings across the 17:00 NY roll ignored; multi-level bars use the
  level nearest the close; "first crossing" counts either direction; entry/exit fill within 5 min; skip reasons counted in a fixed order.
  Bars outside dev are dropped before computing. Decision rule unchanged from the backlog draft.
- **Next run:** collect E018 results from the research-batch run.

### 2026-11-08 R033 (unattended)
- **State:** research-batch run 42530297453 (E018) finished successfully; outputs committed in 2c6178c and not yet recorded -> protocol step 1 (collect).
  pytest passed (124).
- **Decision:** pre-registered B1 rule applied exactly: mean -0.128 (not > 0), CI (-0.989, 0.714), binomial p 0.280 -> **NONE**.
  Cost check negative (SPEC 4 -0.628, x1.5 -0.879). Not a LEAD; no notification. Control-level reversal noted as descriptive only.
- **Next run:** B16 (12-month TSMOM, daily hold, dev) is the top `ready` item.

### 2026-11-09 R034 (unattended)
- **State:** last research-batch run 42530297453 (E018) already recorded (R033); no run queued or in progress -> protocol step 3.
  pytest passed (124) before any change.
- **Pick:** B16 (12-month time-series momentum, daily 16:00 NY hold, dev, 1 trial) is the top `ready` item; B6/B12/B13 blocked,
  B7/B8 parked.
- **Fixed before data (beyond the backlog draft, all mechanical):** trading-date list = unique `sessions.trading_date` of dev bars;
  16:00 NY quote = open of first bar in [16:00, 16:05) NY; s = 0 days kept as flat (signed 0); exclusion order missing_now ->
  missing_past -> missing_next, last date no_next; round trips = runs of the same non-zero signal on consecutive dates, costs charged
  per round trip. Bars outside dev are dropped before computing, so lookback and hold never leave dev. Decision rule unchanged.
- **Next run:** collect E019 results from the research-batch run.

### 2026-11-09 R035 (unattended)
- **State:** research-batch run 42540081769 (E019) finished successfully; outputs committed in 99da3aa and not yet recorded -> protocol step 1 (collect).
  pytest passed (133).
- **Decision:** pre-registered `tsmom.decide_b16` rule applied exactly: mean -0.644 pips/day (not > 0), CI (-3.196, 1.978), t p 0.678 -> **NONE**.
  Cost check negative (SPEC 4 -0.674, x1.5 -0.689 per day). Not a LEAD; no notification.
- **Next run:** no `ready` backlog items -> refill (literature/evidence pass, verified links only).

### 2026-11-09 R036 (unattended)
- **State:** last research-batch run 42540081769 (E019) already recorded (R035, 31cb2f8); no run queued or in progress. No `ready`
  backlog items (B6/B12/B13 blocked, B7/B8 parked) -> protocol step 4 (refill). pytest passed (133) before any change.
- **Literature pass:** opened the RePEc, Southampton and NTU records for Dao, McGroarty & Urquhart (2016, JMFM, weekend overreaction in
  spot FX) and the RePEc and Montclair records for Rentzler, Tandon & Yu (2006, JFM, intraday reversals in currency futures). Thresholds
  and horizons of both papers are not in the abstracts: marked UNVERIFIED; all B17/B18 parameters fixed here before any data.
  Bush & Stephens (2016, JBEF, Monday effect in EUR/USD) opened but its abstract has no testable definition: not used.
  centaur.reading.ac.uk returned a bot-protection page: not circumvented.
- **Selection criteria (R028/R030/R035 lessons):** repo price data only; conditional, not an unconditional time-of-day window; no fixed
  timestamp between 16:30 and 18:30 NY; event-based tests with a power note stating the mean needed to clear the CI.
- **Added:** B17 weekend-gap reversal (dev, 1 trial) and B18 next-session reversal after a large daily move (dev, 1 trial), both with a
  rolling past-only percentile threshold. Ranked B17 above B18: spot-FX source with a reported out-of-sample result vs 1988-2003 futures.
  0 trials used (dev 229, total 233).
- **Next run:** pre-register B17 as E020.

### 2026-11-09 R037 (unattended)
- **State:** last research-batch run 42540081769 (E019) recorded in R035; no run queued or in progress. Top `ready` backlog item is
  B17 (weekend-gap reversal) -> protocol step 3. pytest passed (133) before any change.
- **Choice:** B17 ranked above B18 in R036 (spot-FX source with a reported out-of-sample result). Pre-registered as E020 with the
  backlog draft unchanged; implementation choices fixed now, before data: weekends indexed by calendar Monday, numpy linear
  percentile, spread-skipped events kept in the |G| history, missing-bar exclusion order F, M, X.
- **Next run:** collect the research-batch outputs for E020 and apply `decide_b17`.

### 2026-11-09 R038 (unattended)
- **State:** research-batch run 42556248995 (E020) finished successfully; outputs committed in 7e24c07 and not yet recorded -> protocol step 1 (collect).
  pytest passed (143).
- **Decision:** pre-registered `weekend_gap.decide_b17` rule applied exactly: mean -1.574 pips (not > 0), CI (-12.699, 7.03), t p 0.6267 -> **NONE**.
  Cost check negative (SPEC 4 -2.108, x1.5 -2.374 per event). Not a LEAD; no notification. The descriptive gap-extension reading is
  post-hoc; not added to the backlog as a dev re-test.
- **Next run:** pre-register B18 (next-session reversal after a large daily move, dev) as E021.

### 2026-11-09 R039 (unattended)
- **State:** last research-batch run 42556248995 (E020) recorded in R038; no run queued or in progress. Top (only) `ready` backlog
  item is B18 (next-session reversal after a large daily move) -> protocol step 3. pytest passed (143) before any change.
- **Choice:** B18 pre-registered as E021 with the backlog draft unchanged. Implementation choices fixed now, before data: quotes are
  bar opens in [hh:mm, hh:mm+5) NY; previous/next trading date = adjacent dates in the dev trading-date set; Fridays stay in the
  rolling |R| history but are not events; a large D whose next trading date is not D + 1 calendar day is excluded and counted;
  exclusion order friday, next_not_adjacent, missing_entry, missing_exit, spread. Descriptive control = same trade on non-large,
  non-Friday dates.
- **Next run:** collect the research-batch outputs for E021 and apply `decide_b18`.

### 2026-11-09 R040 (unattended)
- **State:** research-batch run 42567407426 (E021) finished successfully; outputs committed in 73ecba1 and not yet recorded -> protocol step 1 (collect).
  pytest passed (154).
- **Decision:** pre-registered `daily_reversal.decide_b18` rule applied exactly: mean -2.55 pips (not > 0), CI (-7.097, 4.167), t p 0.7756 -> **NONE**.
  Cost check negative (SPEC 4 -3.041, x1.5 -3.287 per event). Not a LEAD; no notification. The up/down asymmetry is post-hoc
  (dev downtrend) and is not added to the backlog as a dev re-test.
- **Next run:** no `ready` backlog items -> refill (literature pass, verified links only).

### 2026-11-09 R041 (unattended)
- **State:** last research-batch run 42567407426 (E021) recorded in R040; no run queued or in progress (latest 5 runs all completed
  success). No `ready` backlog items (B6, B12, B13 blocked; B7, B8 parked) -> protocol step 4 (refill). pytest passed (154).
- **Literature pass:** opened (HTTP 200) Krohn-Mueller-Whelan AEA 2019 "FX Premia Around the Clock" and AEA 2020 fixings draft,
  Evans MPRA 60171 (already listed as Evans 2018), Kostakis-McBride-Sarno-Wang CEAM project page, CXO summary of Breedon-Ranaldo
  (already listed), and a Stern 2018 SNB-event paper without title page (not used). Table values read only via model summary of
  truncated PDFs are marked UNVERIFIED in research/academic_studies.md.
- **Choice:** added B19 (short 02:00-08:15 NY on high-vol dates) and B20 (long 11:05-16:00 NY on high-vol dates), both dev, 1 trial
  each, one variable (vol-state conditioning) relative to tested unconditional relatives (E010/E007/E017). Ranked B19 first: its window
  avoids the 08:30 US releases and the FOMC 14:00 statement. Month-end hedge-rebalancing idea not added (practitioner sources only,
  needs equity data). Fix-pattern line has been weak across E007/E010/E011/E017, so prior expectation is low; a NONE closes the
  vol-state reading of this line.
- **Next run:** pre-register B19 as E022.

### 2026-11-09 R042 (unattended)
- **State:** last research-batch run 42567407426 (E021) recorded in R040; no run queued or in progress (latest 5 runs all completed
  success). Top `ready` backlog item is B19 (pre-ECB-fix short on high-vol dates) -> protocol step 3. pytest passed (154) before any
  change.
- **Choice:** B19 pre-registered as E022 with the backlog draft unchanged. Implementation choices fixed now, before data: range =
  full trading-date mid high-low from 1-minute bars; coverage >= 90% of 1,440 bars, invalid dates left out of the rolling history;
  P = adjacent date in the dev trading-date set; exclusion order missing_entry, missing_exit, spread; exit fixed at 08:15 NY (not
  shifted in DST-mismatch weeks). Descriptive control = same short on normal (non-high-vol) dates after burn-in.
- **Test note:** the random-walk check is a SIGNAL rate <= 0.10 over 40 seeds rather than "never SIGNAL" over 5 seeds (seed 0 gave a
  chance SIGNAL at alpha 0.05; 2/40 = 0.05 overall, as expected under the null).
- **Next run:** collect the research-batch outputs for E022 and apply `decide_b19`.

### 2026-11-09 R043 (unattended)
- **State:** research-batch run 42585915012 (E022) finished successfully; outputs committed in 6b6aba6 and not yet recorded -> protocol
  step 1 (collect). pytest passed (165).
- **Decision:** pre-registered `vol_state_fix.decide_b19` applied exactly: mean +3.646 pips (> 1.0), CI (0.011, 7.751) lower > 0,
  one-sided t p 0.0133 -> **SIGNAL on dev**. Cost check positive (SPEC 4 +3.139, x1.5 +2.886). Not a LEAD (no val confirmation yet);
  no notification.
- **Re-rank:** added B19v (val confirmation, identical rule, val only, 1 trial) and ranked it above B20. Reason: E022's methodology,
  written before data, specified "SIGNAL -> queue val confirmation B19v"; a confirmation step on an open SIGNAL is higher value than a
  new dev idea, and B20 does not depend on B19 (fixed in R041), so the order change does not alter B20's pre-registration.
- **Cautions logged (no new numbers):** marginal CI; normal-date control also positive, so the conditioning is not shown to matter;
  E017 already saw an unconditional related window on val.
- **Next run:** pre-register B19v as E023 (val only) and queue it.

### 2026-11-09 R044 (unattended)
- **State:** last research-batch run 42585915012 (E022) recorded in R043; no run queued or in progress (latest 5 runs all completed
  success). Top `ready` backlog item is B19v -> protocol step 3. pytest passed (165) before any change.
- **Choice:** B19v pre-registered as E023 (val only, 1 trial) with the E022 definitions and `decide_b19` rule unchanged; the only
  variable changed is the block. Implementation choices fixed now, before data: bars at or after 2023-07-01 UTC dropped first, then
  non-val trading dates (`vol_state_fix.restrict_to_block`); rolling history and 60-date burn-in built from val dates only (no dev
  history), so val is independent of dev. LEAD flag computed in the script from the pre-registered gate (SIGNAL and SPEC 4 and x1.5
  net > 0).
- **Expectation stated before data:** with ~190 val events the SE is ~2.2-2.6 pips; a val mean near dev's +3.6 would likely be WEAK.
- **Next run:** collect the research-batch outputs for E023 and apply `decide_b19`.

### 2026-11-09 R045 (unattended)
- **State:** research-batch run 42600685892 (E023) completed success; outputs committed by github-actions[bot] (4ab24c6) and not yet
  recorded -> protocol step 1 (collect). No run queued or in progress. pytest passed (166) before recording.
- **Decision:** `decide_b19` applied exactly to the val outputs: mean +1.197 > 1.0 but CI lower -3.144 and t p 0.304 -> NONE. LEAD
  condition 2 fails; no notification. B19 line closed per the pre-registered "what follows".
- **Next run:** B20 is the top `ready` item -> pre-register and queue it (dev only).

### 2026-11-09 R046 (unattended)
- **State:** last research-batch run 42600685892 (E023) recorded in R045; no run queued or in progress (latest 5 runs all completed
  success). Top (only) `ready` backlog item is B20 -> protocol step 3. pytest passed (166) before any change. Local clone's stale
  `main` (old pre-rewrite hashes) was reset to origin/main; the old ref kept as local branch `stale-local-main`, nothing pushed.
- **Choice:** B20 pre-registered as E024 (dev only, 1 trial), all parameters as fixed in R041: E022's vol-state definition, long
  11:05 -> 16:00 NY, entry spread skip 2.0 pips, `decide_b20` = E022 rule. Implementation: `vol_state_fix.build_days` /
  `frame_from_bars` got optional `side` and window arguments whose defaults keep E022/E023 behaviour (tested). FOMC statement days
  (scheduled, non-cancelled) reported descriptively, not in the rule.
- **Context stated before data:** same condition failed val in E023; prior expectation low. SE ~1.1-1.3 pips.
- **Next run:** collect the research-batch outputs for E024 and apply `decide_b20`.

### 2026-11-09 R047 (unattended)
- **State:** research-batch run 42617055931 (E024) finished successfully; outputs committed in a1bfd0d by github-actions[bot] and not yet
  recorded -> protocol step 1 (collect). No run queued or in progress. pytest passed (173) before recording. Local stale `main` (diverged,
  pre-rewrite hashes) reset to origin/main again; nothing pushed from it.
- **Decision:** pre-registered `vol_state_london.decide_b20` applied exactly: mean +2.983 pips (> 1.0), CI (0.566, 4.847) lower > 0,
  one-sided t p 0.0053 -> **SIGNAL on dev**. Cost check positive (SPEC 4 +2.515, x1.5 +2.281). Not a LEAD (no val confirmation yet);
  no notification.
- **Backlog:** added B20v (val confirmation, identical rule, val only, 1 trial) as the only `ready` item, as fixed in E024's methodology
  before data ("SIGNAL -> queue val confirmation B20v").
- **Cautions logged (no new numbers):** all-dates result also positive, normal-date control CI includes 0, so the conditioning is not
  shown to matter; 2018-2019 negative; E017 saw an unconditional related window on val.
- **Next run:** pre-register B20v as E025 (val only) and queue it.

### 2026-11-09 R048 (unattended)
- **State:** last research-batch run 42617055931 (E024) completed and already recorded (a1522b7); no run queued or in progress ->
  protocol step 3 (next experiment). pytest passed (173) before changes; local detached checkout reset to origin/main.
- **Choice:** B20v is the only `ready` backlog item (fixed in E024's methodology before data). Pre-registered as E025: E024's rule and
  definitions unchanged, val block only, handled exactly as E023 (bars >= 2023-07-01 UTC dropped first, val-only burn-in), 1 val trial.
- **Prior stated before data:** low-to-moderate (sibling E022 failed val; E024 conditioning not shown to beat unconditional drift;
  SE ~1.8 pips on val so WEAK is plausible even if the effect is real). Rule not loosened.
- **Next run:** collect E025 outputs and apply `decide_b20` + lead cost gate.

### 2026-11-09 R049 (unattended)
- **State:** research-batch run 42634668404 (E025) completed success; outputs committed by github-actions[bot] (3b9cb59) and not yet
  recorded -> protocol step 1 (collect). No run queued or in progress. pytest passed (174) before recording; local checkout reset to origin/main.
- **Decision:** `decide_b20` applied exactly to the val outputs: mean +0.582 < 1.0, CI lower -1.992, t p 0.369 -> NONE. LEAD
  condition 2 fails (and cost gate fails at x1.5, -0.197); no notification. B20 line closed per the pre-registered "what follows".
- **Next run:** no `ready` backlog item remains -> refill pass (protocol step 4).

### 2026-11-09 R050 (unattended)
- **State:** last research-batch run 42634668404 (E025) completed and already recorded (164ddd5); no run queued or in progress; no
  `ready` backlog item (B6, B12, B13 blocked; B7, B8 parked) -> protocol step 4 (refill). Local stale `main` reset to origin/main
  (backup branch kept locally, nothing pushed from it).
- **Choice:** two price-data-only items not yet covered by any experiment. B21 gives a calendar-free route to the release-reaction
  question that B12 could not test (no sanctioned date source). B22 tests the intraday-momentum mechanism already in the literature file
  (Elaut et al. 2018) with a London-session analogue, without the CME settlement time that blocked B13. Order: B21 first (stronger
  mechanism evidence: two order-flow papers; B22 is a loose analogue, prior low after E001/E007 NONE).
- **Sources opened this run:** Evans & Lyons (2008) and Love & Payne (2008) RePEc abstract pages; DOIs not shown there (UNVERIFIED).
- **Next run:** pre-register B21 as E026 (dev only, 1 trial) and queue it.

### 2026-11-09 R051 (unattended)
- **State:** last research-batch run 42634668404 (E025) completed and already recorded; no run queued or in progress -> protocol
  step 3 (next experiment). Top `ready` item: B21 (ranked above B22 in R050).
- **Choice:** pre-register B21 as E026 (dev only, 1 trial) with every parameter and the decision rule exactly as drafted in the backlog
  (R050); no change after seeing any data (no conditional 08:30-08:45 return has been computed on dev).
- **Next run:** collect the E026 batch outputs and apply the rule; SIGNAL -> B21v (val), else B22.

### 2026-11-09 R052 (unattended)
- **State:** research-batch run 42664624217 (E026) completed success; outputs committed by github-actions[bot] (067d5aa) and not yet
  recorded -> protocol step 1 (collect). No run queued or in progress. pytest passed (183) before recording; local checkout reset to origin/main.
- **Decision:** `decide_b21` applied exactly to the dev outputs: mean -0.42 (not > 0), CI lower -5.278, t p 0.564 -> NONE. LEAD
  condition 1 fails (costs negative too); no notification. B21 line closed per the pre-registered "what follows".
- **Next run:** pre-register B22 (top `ready` item) as E027.

### 2026-11-09 R053 (unattended)
- **State:** last research-batch run 42664624217 (E026) completed and already recorded (R052); no run queued or in progress ->
  protocol step 3 (next experiment). Top `ready` item: B22 (only `ready` item). pytest passed (183) before any change. Local `main`
  had diverged from origin (stale pre-rewrite history); work done on a fresh branch from origin/main and pushed to main.
- **Choice:** pre-register B22 as E027 (dev only, 1 trial) with every parameter and the decision rule exactly as drafted in the backlog
  (R050), including the block-20 bootstrap; no change after seeing any data (no conditional 15:25-15:55 London return computed on dev).
- **Next run:** collect the E027 batch outputs and apply `decide_b22`; SIGNAL -> B22v (val), else backlog refill.

### 2026-11-09 R054 (unattended)
- **State:** research-batch run 42683469479 (E027) completed success; outputs committed by github-actions[bot] (405319c) and not yet
  recorded -> protocol step 1 (collect). No run queued or in progress. pytest passed (192) before recording; local checkout reset to origin/main.
- **Decision:** `decide_b22` applied exactly to the dev outputs: mean -0.008 (not > 0), CI lower -0.553, t p 0.511 -> NONE. LEAD
  condition 1 fails (costs negative too); no notification. B22 line closed per the pre-registered "what follows".
- **Next run:** no `ready` backlog item -> refill (literature pass, verified links only).

### 2026-11-09 R055 (unattended)
- **State:** last research-batch run 42683469479 (E027) completed and already recorded (R054, cae557d); no run queued or in progress;
  no `ready` backlog item (B6, B12, B13 blocked; B7, B8 parked) -> protocol step 4 (refill). pytest passed (192). Local stale `main`
  reset to origin/main.
- **Choice:** following lesson R052 (prefer sources that state a tradable horizon in spot FX), added two items from Caporale & Plastun
  (2019, Brunel WP 19-09), which states EURUSD overreaction-day entry/exit hours. B23 (same-day continuation, dev) uses only
  information known at entry, unlike the paper's full-day trigger. B24 (next-morning fade) is val only because E021's dev descriptive
  already covered the 16:00 -> 20:00 NY reversal window. Order: B23 then B24.
- **Not added:** pre-ECB drift (Quantpedia blog; equities, not FX, needs an ECB date calendar); Wiśniewska 2014 (no horizon or
  numbers); Rif & Utz 2021 (stocks, 1-minute).
- **Sources opened this run:** Brunel WP 19-09 PDF (partial verbatim), CEEOL record, RePEc QREF record, Quantpedia post. Data-clock
  time zone of the paper UNVERIFIED; NY mapping is our assumption, fixed before any data.
- **Next run:** pre-register B23 as E028 (dev only, 1 trial) and queue it.

### 2026-11-09 R056 (unattended)
- **State:** last research-batch run 42683469479 (E027) completed and already recorded (R054); no run queued or in progress ->
  protocol step 3 (next experiment). Top `ready` item: B23. pytest passed (192) before any change. Local stale `main` reset to
  origin/main (old history kept on local branch `stale-local-main`, not pushed).
- **Choice:** pre-register B23 as E028 (dev only, 1 trial) with every parameter and the decision rule exactly as drafted in the backlog
  (R055), including the block-5 bootstrap. Implementation details fixed now, before data: SD is the sample SD (ddof=1); the open quote
  is the first bar in [17:00, 17:05) NY assigned to trading date D; fewer than 10 events -> insufficient sample -> NONE.
  No conditional 12:00-16:30 NY return has been computed on dev.
- **Next run:** collect the E028 batch outputs and apply `decide_b23`; SIGNAL -> B23v (val), else B24.

### 2026-11-09 R057 (unattended)
- **State:** research-batch run 42712247364 (E028) completed success; outputs committed by github-actions[bot] (612642d) and not yet
  recorded -> protocol step 1 (collect). No run queued or in progress. pytest passed (202) before recording; local stale `main`
  reset to origin/main (old history kept on local branch `old-local-main`, not pushed).
- **Decision:** `decide_b23` applied exactly to the dev outputs: mean +1.061 (> 1.0) but CI lower -5.625 and t p 0.390 -> neither
  SIGNAL nor WEAK -> NONE. LEAD condition 1 fails; no notification. B23 line closed per the pre-registered "what follows". The
  up-move/down-move split is post-hoc and is not queued.
- **Next run:** pre-register B24 (val only) and queue it.

### 2026-11-10 R058 (unattended)
- **State:** last research-batch run 42712247364 (E028) completed and already recorded (R057); no run queued or in progress ->
  protocol step 3 (next experiment). Top `ready` item: B24. pytest passed (202) before any change. Worked on a detached HEAD at
  origin/main (local stale `main` left untouched).
- **Choice:** pre-register B24 as E029 (val only, val-only burn-in, 1 trial) with every parameter and the decision rule exactly as
  drafted in the backlog (R055). Implementation details fixed now, before data: close quote = first bar in [16:55, 17:00) NY; entry =
  first bar in [17:05, 17:10) NY of the next trading date (N = D + 1 calendar day); valid Fridays stay in the rolling history, only
  their trade is excluded; exclusion order friday -> missing entry -> missing exit -> spread; SD ddof=1; fewer than 10 events ->
  insufficient sample -> NONE. Null calibration at val size (scratch, 300 seeds): SIGNAL rate 4.3%.
- **Why val is clean:** no val experiment has conditioned an overnight return on the previous day's move (E012/E017 unconditional,
  E023/E025 other windows on unsigned range).
- **Next run:** collect the E029 batch outputs and apply `decide_b24`. Any outcome: no LEAD possible from a val-only test; WEAK/NONE
  -> B24 closed and backlog refill; SIGNAL -> logged for a human decision.

### 2026-11-10 R059 (unattended)
- **State:** research-batch run 42728790080 (E029) completed successfully; outputs (commit cf4751a) not yet recorded -> protocol step 1
  (collect). pytest passed (213) before any change. Worked on a branch at origin/main (stale local `main` kept as
  `stale-local-main-backup`, untouched).
- **Decision applied exactly:** `decide_b24` -> NONE (insufficient sample, 4 tested events < 10). Thresholds, spread cap and entry time
  unchanged after seeing results (CLAUDE.md rule 7).
- **Why it failed:** 19 of 34 events were above the 2.0-pip spread cap at 17:05 NY. Logged as a lesson: check roll-hour entry spreads
  on dev before pre-registering.
- **Next run:** no `ready` backlog item -> refill (literature/evidence pass, 2-3 pre-registrable items). No LEAD, no notification.

### 2026-11-10 R060 (unattended)
- **State:** last research-batch run 42728790080 (E029) completed and already recorded (R059); no run queued or in progress; no
  `ready` backlog item -> protocol step 4 (refill). pytest passed (213) before any change. Worked on a branch at origin/main (stale
  local `main` left untouched).
- **Literature pass:** opened Ito & Yamada (JIE 2017 / NBER 22820 abstracts), Popović & Đurović (Applied Economics 2014 abstract),
  Zheng (2023 JMP introduction), Vasileiou (2024, JSE equity TOM; not relevant). NBER full-text PDF could not be fetched (permission
  not granted), so the gotobi definition is marked UNVERIFIED.
- **Choice:** added B25 (short EUR/USD 08:55 -> 09:55 Tokyo on gotobi dates, dev) and B26 (long 09:55 -> 10:55 Tokyo on gotobi
  dates, dev). Reason: the mechanism (predictable dollar-buying order flow into the Tokyo fix) exists in the spot FX market itself
  (lesson R054), E011 deliberately left the gotobi subset untested, n ~460 on dev gives a tight CI (lesson R057), and the entry is
  far from the 17:00 NY roll (lesson R059; E011 median entry spread 0.4). Popović-Đurović Friday 00-03 not added: E009 dev cells do
  not support it and the time zone is unknown.
- **Next run:** pre-register B25 as the next experiment.

### 2026-11-10 R061 (unattended)
- **State:** last research-batch run 42728790080 (E029) completed and already recorded (R059); no run queued or in progress ->
  protocol step 3 (next experiment). Top `ready` item: B25. pytest passed (213) before any change. Local `main` was a stale shallow
  history; moved to origin/main with `checkout -B` (old history kept on local branch `old-local-main`, not pushed).
- **Choice:** pre-register B25 as E030 (dev only, 1 trial), parent E011, with every parameter and the decision rule exactly as drafted
  in the backlog (R060). Implementation details fixed now, before data: universe = Mon-Fri trading dates (= Tokyo date for this
  window); E011's >= 55-of-60-bar coverage rule kept as an exclusion (`low_coverage`, counted, after missing quotes and before the
  spread cap); quotes are the first-bar open in [hh:mm, hh:mm+5) Tokyo as written in the backlog; fewer than 40 events (2 x block)
  -> insufficient sample -> NONE. `month_end` flag = a source day is the month's last day (descriptive only).
- **Next run:** collect the E030 batch outputs and apply `decide_b25`; SIGNAL -> B25v (val), else B26.

### 2026-11-10 R062 (unattended)
- **State:** research-batch run 42749648254 (E030) completed success; outputs committed by github-actions[bot] in 9e2c50a, not yet
  recorded -> protocol step 1 (collect). pytest passed (235) before recording. Local `main` was again a stale divergent history;
  reset to origin/main (old history kept on local branch `stale-local-main`, not pushed).
- **Decision:** applied `gotobi_fix.decide_b25` exactly: mean +0.180 < 1.0, CI (-0.552, 1.245) includes 0, t p 0.3224 -> NONE. No lead.
  Dev trial count 236 -> 237, total 243 -> 244.
- **Post-hoc note:** month-end gotobi subset (n 72, +2.639) is descriptive only; not queued (would be a dev re-test of a subset seen
  after the result, against CLAUDE.md rule 6/7 spirit). No backlog item added for it.
- **Next run:** B26 is the top `ready` item: pre-register as E031 (dev, 1 trial) with the backlog rule unchanged.

### 2026-11-10 R063 (unattended)
- **State:** last research-batch run 42749648254 (E030) completed and recorded in R062; no run queued or in progress -> protocol step 3
  (next experiment). Top `ready` item: B26. pytest passed (235) before any change. Local `main` was again stale/divergent; reset to
  origin/main (old history on local branch `stale-local-main`, not pushed).
- **Choice:** pre-register B26 as E031 (dev only, 1 trial), parent E011 (post-fix window), with every parameter and the decision rule
  exactly as drafted in the backlog (R060) and E030's implementation details reused unchanged (universe, quote rule, exclusion order,
  >= 55-of-60 coverage on the post-fix hour, spread cap at the 09:55 entry, block 20, < 40 events -> NONE). The 08:55 quote is used
  only for the descriptive pre-fix-sign split (exploratory, fixed now) and never excludes an event. Written before any data.
- **Next run:** collect the E031 batch outputs and apply `decide_b26`; SIGNAL -> B26v (val), else B26 closed and backlog refill.

### 2026-11-10 R064 (unattended)
- **State:** research-batch run 42762105863 (E031) completed success; outputs committed by github-actions[bot] in 74fae18, not yet
  recorded -> protocol step 1 (collect). pytest passed (243) before recording. Local clone was on a detached HEAD; reset to origin/main.
- **Decision:** applied `gotobi_postfix.decide_b26` exactly: mean +0.799 < 1.0 and CI (-0.154, 1.632) includes 0 -> not SIGNAL;
  mean > 0 and t p 0.0244 < 0.05 -> WEAK. No lead. Dev trial count 237 -> 238, total 244 -> 245.
- **Post-hoc note:** exploratory splits (after pre-fix down move +1.365, not weekend-shifted +1.160) are descriptive only and not
  queued; the control shows the same pattern, so they are not gotobi-specific.
- **Next run:** no `ready` backlog items -> refill (literature pass, 2-3 pre-registrable items).

### 2026-11-10 R065 (unattended)
- **State:** last research-batch run 42762105863 (E031) completed and recorded (R064); no run queued or in progress; no `ready`
  backlog item -> protocol step 4 (refill). pytest passed (243) before any change. Local clone was on a detached HEAD; reset to
  origin/main.
- **Literature pass (opened):** KMW Bank of Canada SWP 2021-48 (window definitions verbatim), Neuhierl & Weber 2017 (Booth page),
  Kumar 2015 and 2018 (abstracts), Ranaldo & Santucci de Magistris 2022 JFE (accepted PDF), Evans & Speight 2006 (Cardiff WP).
  Lucca & Moench (NY Fed SR512) could not be opened. Details in research/academic_studies.md.
- **Choice:** added one item, B27 (KMW post-Tokyo window, long EUR/USD 20:55 -> 02:00 NY, **val only**, 1 trial). Reason: published,
  unconditional, daily (n ~600 on val, lesson E014), entry away from the 17:00 roll (lesson R059), and the window's val returns have
  never been computed; dev is contaminated by E009's published hourly cells, so val is the only clean non-OOS block. Only one item
  was added (protocol asks for 2-3): FOMC-drift, turn-of-month, pre-Tokyo and pre-ECB candidates each failed a lesson or a
  contamination check (backlog refill note R065). Adding weaker items to reach a count would break CLAUDE.md rule 7 in spirit.
- **For the human (no action taken, not a lead):** the KMW unconditional pre-ECB window (short 02:00 -> 08:15 NY) is clean only on the
  locked OOS block. Dev E009 cells for 02:00-08:00 NY sum to about -3.2 pips (EUR down, the published sign); val all-date is
  contaminated by E023's descriptive output (~+1.2 pips signed). Testing it would need explicit OOS approval.
- **Next run:** pre-register B27 as the next experiment.

### 2026-11-10 R066 (unattended)
- **State:** last research-batch run 42762105863 (E031) completed and recorded (R064); no run queued or in progress; B27 is the top
  (only) `ready` item -> protocol step 3. pytest passed (243) before any change. Local main had diverged from origin (stale local
  history); kept as local branch `backup-old-local-main`, reset main to origin/main. Nothing pushed from the old history.
- **Choice:** pre-register B27 as E032 (val only, 1 trial), parameters and rule exactly as the backlog draft (R065): long EUR/USD
  20:55 -> 02:00 NY, E011 quote rule, >= 280/305 bars, 2.0-pip entry-spread cap, block-20 bootstrap, SIGNAL/WEAK/NONE thresholds as
  B25/B26, < 200 dates -> NONE. Val contamination check: no earlier val experiment computed this window's mean (E029 4 conditional
  events; E014 ~20 FOMC dates; E001/E006 Asian structure as predictors only); written in the hypothesis.
- **Outcome handling (fixed now):** val-only SIGNAL is not a LEAD; with SPEC 4 and x1.5 net > 0 it is logged here as an OOS candidate
  for the human, no notification. WEAK/NONE closes B27.
- **Next run:** collect E032 when the research-batch run finishes.

### 2026-11-10 R067 (unattended)
- **State:** research-batch run 42783232861 (E032) completed success; outputs committed by github-actions[bot] in a21f2cd, not yet
  recorded -> protocol step 1 (collect). pytest passed (252) before recording. Local main had diverged again (stale old history);
  renamed to local branch `stale-local-main-20261110`, checked out origin/main. Nothing pushed from the old history.
- **Decision:** applied `post_tokyo_kmw.decide_b27` exactly: n 636 >= 200; mean -0.534 not > 0 -> NONE (t p 0.830, CI (-1.606,
  0.669)). Not an OOS candidate, no lead. Val trial count 7 -> 8, total 245 -> 246.
- **Next run:** no `ready` backlog items -> refill (literature pass, 2-3 pre-registrable items). Tokyo-fix windows are closed.

### 2026-11-10 R068 (unattended)
- **State:** last research-batch run 42783232861 (E032) completed and recorded (R067, fb0d723); no run queued or in progress; no
  `ready` backlog item -> protocol step 4 (refill). pytest passed (252) before any change. Local clone was on a detached HEAD; reset
  main to origin/main.
- **Literature pass (opened):** Cespa-Gargano-Riddiough-Sarno "Foreign exchange volume" (JBS summary page; paper text not opened,
  journal details UNVERIFIED), Borisenko-Pozdeev 2017 WP (PDF), Stauskas-Sucarrat 2025 and Erdemlioglu-Laurent-Neely 2012 (not used).
  Details in research/academic_studies.md.
- **Choice:** added B28 (low-unexpected-volume next-day reversal) and B29 (high-unexpected-volume next-day continuation), dev, one shared
  experiment, 2 trials, p < 0.025 each. Reason: lesson R064 asks for new signals rather than date subsets of known WEAK effects; volume is
  a variable no experiment has used, the mechanism is published, the events are daily (n ~380 each on dev), and entry at 20:00 NY avoids
  the roll spread (lesson R059). B28 ranked first (the stronger published claim). Risks recorded in the items: Dukascopy volume is a proxy
  for CLS volume; high-UV days overlap E021 large-move days. A volume gate (missing/zero volume -> BLOCKED, 0 trials) is fixed now.
- **Not added:** central-bank pre-announcement drift (needs OIS expectations, too few events), same-time-of-day persistence (no FX
  source; E009 contamination), round-number reversals (redundant with E018). Backlog note R068.
- **Next run:** pre-register B28+B29 as the next experiment.

### 2026-11-10 R069 (unattended)
- **State:** last research-batch run 42783232861 (E032) completed and recorded (R067); no run queued or in progress; B28 and B29 are
  the top `ready` items -> protocol step 3. pytest passed (252) before any change. Local main was stale/diverged; reset to origin/main
  (nothing pushed from the old history).
- **Choice:** pre-register B28+B29 as E033 (dev only, one experiment, 2 trials, precedent E012), parameters and rule exactly as the
  backlog drafts (R068): UV = V / mean(previous 21 valid dates) - 1, rolling p33/p67 of 60 past UV values, R = 16:55 NY - 17:00 NY open,
  hold 20:00 NY D -> 16:55 NY D+1, Fridays excluded, 2.0-pip entry cap, block-10 bootstrap, p < 0.025 per arm, < 150 events -> NONE.
  Volume gate first (no column or > 1% zero/NaN dev bars -> BLOCKED, 0 trials).
- **Judgement calls fixed before data (written in the methodology):** a missing R quote is `missing_signal_quote` (not an event, listed
  first in the exclusion order); low-coverage dates never enter the volume history; percentile = numpy linear; the E021 overlap uses
  `daily_reversal.mark_events` on the same dev bars.
- **Outcome handling (fixed now):** SIGNAL in an arm -> its val confirmation (B28v/B29v) as a separate pre-registered experiment, not a
  LEAD yet; WEAK/NONE closes that arm; BLOCKED -> both items `blocked`, 0 trials.
- **Next run:** collect E033 when the research-batch run finishes.

### 2026-11-10 R070 (unattended)
- **State:** research-batch run 42808245508 (E033) completed, outputs committed by github-actions[bot] (b7585fc), not yet recorded ->
  protocol step 1 (collect). pytest passed (261).
- **Decision (rule applied exactly):** B28 NONE (mean -2.034, not > 0), B29 NONE (mean -0.213, not > 0). Both arms closed; no re-test.
  No lead. Trials: dev 240, val 8, total 248.
- **Next run:** no `ready` item remains -> backlog refill (lesson R070: prefer intraday windows or mechanisms with a stated effect size
  that clears the power bar).

### 2026-11-10 R071 (unattended)
- **State:** last research-batch run 42808245508 completed and recorded (R070); no run queued or in progress; no `ready` backlog item
  -> protocol step 4 (refill). pytest passed (261).
- **Evidence pass:** Melvin & Prins (2015) abstract opened on IDEAS (DOI 10.1016/j.finmar.2014.11.001); Marsh-Panagiotou-Payne (2017)
  WMR fix WP opened (first ~40% verbatim). Melvin-Prins slides and full text not openable: window, signal and EUR magnitude UNVERIFIED.
  Checked dukascopy-node 1.51.1 instrument list: `eusidxeur` (from 2014-06) and `usa500idxusd` exist, so the signal is buildable on the
  runner.
- **Added:** B30 (`ready`): month-end pre-fix equity-hedging flow, -sign(EU minus US equity MTD return to 16:00 London D-1), two windows
  (15:00 -> 16:00 London on D; 16:00 London D-1 -> 16:00 London D), dev only, 2 trials, p < 0.025 each, data gate first. B31 (`blocked`)
  val confirmation, earned only by a B30 SIGNAL.
- **Why this despite low power:** first mechanism in the queue that uses information outside EUR/USD prices (equity-driven hedge flow),
  and the fix is a known flow concentration point. Known weaknesses recorded in the item: ~72 dev events, no verified effect size
  (lesson R070), val ~29 events (lesson E014). Not added: Hau-Rey rebalancing (contemporaneous only), Marsh-Panagiotou-Payne
  one-minute post-fix reversal (below tradable horizon).
- **Next run:** pre-register B30 (hypothesis, methodology, record.json, registry row), add the index download to the workflow, then queue.

### 2026-11-10 R072 (unattended)
- **State:** last research-batch run 42808245508 (E033) completed and recorded (R070); no run queued or in progress; B30 is the top
  `ready` item -> protocol step 3. pytest passed (261) before any change. Local main was stale/diverged; reset to origin/main.
- **Choice:** pre-register B30 as E034 (dev only, one experiment, 2 trials: HOUR 15:00 -> 16:00 London on D, DAY 16:00 London D-1 ->
  16:00 London D), signal and rule exactly as the backlog draft (R071): position -sign(EU50 minus US500 log return from the previous
  month-end 16:00 London fix to 16:00 London on D-1), i.i.d. bootstrap, p < 0.025 per window, < 50 events -> NONE.
- **Judgement calls fixed before data (written in the methodology):** (1) holiday fallback for index quotes: latest London date up to
  5 days back with a 16:00 quote (Eurex is closed on 24/31 Dec and Good Friday, which fall on several month-ends; without it the 5%
  data gate would likely fail for calendar reasons, not data errors); (2) the anchor is the previous month-end in the EUR/USD dev set,
  so Jan 2015 is `no_prev_month_end` (dev bars only; expected n 71); (3) index data downloaded in batch.sh into data/raw_index/ (not
  data/raw, which the EUR/USD ingest globs) for 2015-2020 only; the download may fail without failing the job so the gate records
  BLOCKED; no workflow file change.
- **Outcome handling (fixed now):** SIGNAL in a window -> B31 (val confirmation, own experiment), not a LEAD yet; WEAK/NONE in both ->
  B30 closed and B31 closed unearned; BLOCKED -> 0 trials, one diagnosis/re-fetch if the cause is a download error.
- **Next run:** collect E034 when the research-batch run finishes.

### 2026-11-10 R073 (unattended)
- **State:** research-batch run 42834778439 (E034) completed, outputs committed by github-actions[bot] (2adc3fe), not yet recorded ->
  protocol step 1 (collect). pytest passed (274). Local main had diverged from origin/main (stale history); worked on a branch
  tracking origin/main (reset of local main was not permitted in this session) and pushed to origin main.
- **Decision (rule applied exactly):** index data gate ok (0 missing quotes). B30-hour NONE (mean +1.731 > 1 but CI lower -4.152, t p
  0.285); B30-day NONE (mean +3.354, CI lower -9.322, t p 0.300). B30 closed, B31 closed unearned; no re-test. No lead.
  Trials: dev 242, val 8, total 250.
- **Judgement call:** the descriptive US-only leg (DAY +23.082, t p 0.0001) is recorded as post-hoc and not acted on; it is not a
  backlog item. A future refill may consider it only as a val-only pre-registration against the unconditional-long control.
- **Next run:** no `ready` item remains -> backlog refill.

### 2026-11-10 R074 (unattended)
- **State:** last research-batch run 42834778439 (E034) completed and recorded (R073); no run queued or in progress; no `ready`
  backlog item -> protocol step 4 (refill). pytest passed (274). Local main had stale diverged history; reset to origin/main.
- **Literature pass:** opened KMW "UIP in High Frequency" (2024 WP), Lou-Polk-Skouras FMG DP 961 (2026), Marsh-Miao (2012),
  Kloks-Mattille-Ranaldo (2024); Jiang (2019) not openable. Details and UNVERIFIED markings in research/academic_studies.md and the
  backlog refill note R074.
- **Added:** B32 (daily overnight -> intraday reversal, -sign(r_on 17:05 -> 07:00 NY) x r_id 07:00 -> 16:55 NY) and B33 (same with a
  20-date summed overnight signal), one experiment, dev only, 2 trials, p < 0.025 each; B34 val confirmation blocked until earned.
  Chosen because the conditional overnight-sign statistic is uncontaminated on dev, n ~1,500 gives adequate power, and only repo price
  data are needed. Prior is weak (an FX analogue, not a published FX result).
- **For the human (no action taken):** the KMW-UIP unconditional intraday long EUR/USD (07:00 -> 17:00 ET) is a published direction
  whose dev and val are already largely seen (E009, E017, E001/E006); only the locked OOS block could test it cleanly. Same status as
  the R065 pre-ECB window. Needs a human decision; not queued.
- **Next run:** pre-register B32+B33 as E035 (hypothesis, methodology, record.json, registry row), implement with tests, queue.

### 2026-11-10 R075 (unattended)
- **State:** last research-batch run 42834778439 (E034) completed and recorded (R073); no run queued or in progress; B32 and B33
  are the top `ready` items (one experiment) -> protocol step 3. pytest passed (274) before any change. Local main was stale/diverged;
  reset to origin/main.
- **Choice:** pre-register B32+B33 as E035 (dev only, 2 trials), definitions and rule exactly as the backlog draft (R074):
  B32 -sign(r_on) and B33 -sign(O20), hold 07:00 -> 16:55 NY, block-20 bootstrap, p < 0.025 per arm, < 500 dates -> NONE.
- **Judgement calls fixed before data (in the methodology):** the 17:05 NY open quote is taken from the first bar in [17:05, 17:10) NY
  whose trading date is D; a missing 07:00 quote counts as `missing_signal` for B32 (it is both signal end and entry); B33 burn-in is
  the first 20 dev dates with a valid r_on (dev bars only, no pre-dev history).
- **Outcome handling (fixed now):** SIGNAL in an arm -> B34 (val confirmation, own experiment), not a LEAD yet; WEAK/NONE in both ->
  B32/B33 closed, B34 closed unearned, refill next.
- **Next run:** collect E035 when the research-batch run finishes.

## 2026-11-10 R076 (unattended)
- **State:** research-batch run 42865880407 (E035) completed success; outputs commit cfd1951 not yet recorded. No run queued or in progress.
- **Choice:** protocol step 1 (Collect): record E035 and apply `decide_b32` exactly. pytest 284 passed.
- **Result:** B32 NONE, B33 SIGNAL on dev. LEAD gate: condition 1 only (val confirmation not yet run) -> no LEAD, no notification.
- **Next run:** pre-register B34 (B33 arm unchanged on val, own experiment, 1 val trial, p < 0.05, O20 burn-in from val dates only;
  check val contamination: E017/E032 used other windows).

## 2026-11-10 R077 (unattended)
- **State:** last research-batch run 42865880407 (E035) completed and recorded (R076); no run queued or in progress; B34 is the only
  `ready` backlog item -> protocol step 3. pytest 284 passed before any change.
- **Choice:** pre-register B34 as E036: E035 B33 arm unchanged on the val block only (O20 burn-in from val dates, bars >= 2023-07-01 UTC
  dropped first), 1 val trial, rule = E035 rule with p < 0.05 (`decide_b34`), exactly as fixed in backlog B34 before E035 ran.
- **Judgement calls fixed before data:** MIN_EVENTS 500 kept from E035 (val ~610 tested dates expected); known-calendar check =
  results excluding FOMC statement days and month-end dates (descriptive, required in any LEAD write-up); B32 daily arm reported on val
  as descriptive only, not a trial.
- **Outcome handling (fixed now):** SIGNAL + SPEC 4 and x1.5 net > 0 -> LEAD (LEADS.md, notify, pause line, propose OOS command, no
  OOS run); otherwise B33/B34 line closed, refill next.
- **Next run:** collect E036 when the research-batch run finishes.

## 2026-11-10 R078 (unattended)
- **State:** research-batch run 42885844344 (E036) completed success; outputs committed by github-actions[bot] (69cf81e) and not yet
  recorded -> protocol step 1 (collect). No run queued or in progress. pytest 287 passed.
- **Decision:** `decide_b34` applied exactly to the val outputs: n 616, mean +0.193 (not > 1.0), CI lower -2.683, t p 0.456 -> NONE.
  LEAD condition 2 fails (cost gate also fails: SPEC 4 net -0.492, x1.5 -0.834); no notification. B33/B34 line closed per the
  pre-registered "what follows". The positive high-|O20| tercile on val is descriptive only and is not turned into a new val test.
- **Next run:** no `ready` backlog item -> refill (literature/evidence pass, 2-3 pre-registrable items).

## 2026-11-10 R079 (unattended)
- **State:** last research-batch run 42885844344 (E036) completed and recorded (R078); no run queued or in progress (latest 5 runs all
  completed success). No `ready` backlog item (B6, B12, B13 blocked; B7, B8 parked) -> protocol step 4 (refill). pytest 287 passed.
- **Housekeeping:** the workspace clone's local `main` had diverged from origin (stale pre-R003 history); reset to origin/main
  (6785a44), old local state kept as local branch `old-local-main`. No remote history touched.
- **Choice:** relative equity performance -> next-day EUR/USD (B35 daily, B36 20-date smoothed, one experiment, 2 dev trials;
  B37 val confirmation blocked). Reason: price-only EUR/USD timing lines keep failing (E019-E036); this uses a second data source the
  runner already downloads (E034) and a published mechanism with a stated sign (Hau & Rey 2006, abstract opened). Weak prior stated:
  the published relation is contemporaneous; the lag is our extension, effect size unknown.
- **Not added:** a canonical moving-average rule (would mostly re-test B16 TSMOM, NONE); minute-scale FX lead-lag (below tradable
  horizon after SPEC 4 costs).
- **Next run:** pre-register B35+B36 as E037 (reuse E034 index loader/download script; data gate first).

## 2026-11-10 R080 (unattended)
- **State:** last research-batch run 42885844344 (E036) completed and recorded (R078); no run queued or in progress (latest 5 runs all
  completed success). Top `ready` backlog items: B35 + B36 (one experiment) -> protocol step 3 (next experiment). pytest passed
  before changes (287) and after (299).
- **Choice:** pre-register B35 + B36 as E037 (dev only, 2 trials, p < 0.025 each, block-20 bootstrap, index data gate first), rule
  and parameters exactly as drafted in the backlog (R079). Implementation choices fixed now, before data: date list = Mon-Fri EUR/USD
  dev trading dates; data gate counts dev dates with no 16:00 London quote in either index; FOMC exclusion (descriptive) = D is a
  statement date; month-end exclusion (descriptive) = D or next date is a month-end.
- **Reuse:** E034 index loader (`month_end_hedging.load_index`, `london_quotes`) and download script; E035 statistic and rule
  (`evaluate_b32`/`decide_b32`, identical thresholds).
- **Next run:** collect E037 when the research-batch run finishes.

## 2026-11-10 R081 (unattended)
- **State:** research-batch run 42915756793 (E037) completed success; outputs committed by github-actions[bot] (b92e783) and not yet
  recorded -> protocol step 1 (collect). No run queued or in progress. pytest 299 passed.
- **Decision:** data gate ok (28/1561 dates missing an index quote, 1.8%). `decide_b35` applied exactly: B35 n 1509, mean +1.268,
  CI lower -1.411, t p 0.191 -> NONE; B36 n 1482, mean -0.88 -> NONE. LEAD condition 1 fails; no notification. B35/B36 closed and
  B37 closed unearned per the pre-registered "what follows". Descriptive terciles/years not turned into new tests.
- **Next run:** no `ready` backlog item -> refill (literature/evidence pass, 2-3 pre-registrable items).

## 2026-11-11 R082 (unattended)
- **State:** last research-batch run 42915756793 (E037) completed and recorded (R081, ae4a183); no run queued or in progress (latest 5
  runs all completed success). No `ready` backlog item (B6, B12, B13 blocked; B7, B8 parked) -> protocol step 4 (refill). pytest 299
  passed. Workspace clone was on a detached HEAD; checked out `main` and pulled (no remote history touched).
- **Choice:** B38 intraday momentum into the 17:00 NY spot roll (sign(17:00 -> 16:25 NY) x 16:25 -> 16:55 NY, dev, 1 trial, B13 rule
  unchanged) + B39 val confirmation (blocked). Reason: lesson R081 says to prefer published *lagged* effects; Baltussen et al. (2021) is
  one that covers currencies, and B13 is blocked only on the CME settlement time. The 17:00 NY roll needs no external source. One
  variable changed vs B13 (anchor). Weak prior stated: convention mismatch (futures close vs spot roll) and a 1-pip bar on a 30-min hold.
- **Not added:** COT positioning (Klitgaard-Weir 2004: no weekly predictability); Ranaldo Thursday / holiday effects (home-hours line
  closed on val by E017; holiday numbers UNVERIFIED).
- **Next run:** pre-register B38 as E038 (dev only).

## 2026-11-11 R083 (unattended)
- **State:** last research-batch run 42915756793 (E037) completed and recorded in R081; no run queued or in progress. pytest 299
  passed before changes. Top `ready` backlog item: B38 -> protocol step 3 (next experiment).
- **Decision:** pre-register B38 as E038 (dev only, 1 trial), parameters and rule exactly as fixed in the R082 backlog entry (B13
  rule: mean > 1.0 pip AND block-20 bootstrap CI lower > 0 AND one-sided binomial p < 0.05; < 500 dates -> NONE). Parent E016
  (anchor changed only).
- **Implementation:** `fxresearch.roll_momentum` (reuses `overnight_reversal.evening_quotes` for the 17:00 NY start quote of
  trading date D and `vol_state_fix.ny_quotes` for 16:25/16:55 NY); exclusion order missing_start, missing_entry, zero_signal,
  missing_exit, entry_skipped_spread; Mon-Fri trading dates only (weekend artefacts counted). 9 new tests (no look-ahead,
  random-walk SIGNAL rate, quote timing incl. next-date reading, rule thresholds); synthetic smoke ok.
- **Next run:** collect E038 when the research-batch run finishes.

## 2026-11-11 R084 (unattended)
- **State:** research-batch run 42939744082 (E038) completed success; outputs committed by github-actions[bot] (64780e4) and not yet
  recorded -> protocol step 1 (collect). No run queued or in progress. pytest 308 passed.
- **Decision:** `decide_b38` applied exactly: n 1542 (>= 500), mean +0.255 (not > 1.0), CI lower 0.023 (> 0), binomial p 0.06924
  (not < 0.05) -> WEAK. LEAD condition 1 fails (and SPEC 4 net -0.425); no notification. B38 closed WEAK, B39 closed unearned per
  the pre-registered "what follows". Descriptive slices (EDT, mid |r1| tercile) not turned into new tests.
- **Next run:** no `ready` backlog item -> refill (literature/evidence pass, 2-3 pre-registrable items).

## 2026-11-11 R085 (unattended)
- **State:** last research-batch run 42939744082 (E038) completed and recorded (R084, ddcd239); no run queued or in progress (latest 5
  runs all completed success). No `ready` backlog item (B6, B12, B13 blocked; B7, B8 parked) -> protocol step 4 (refill). pytest 308
  passed. Workspace clone was on a detached HEAD; checked out `main` and pulled.
- **Choice:** B40 (10-date hold) + B41 (next-date hold): Treasury-auction demand shock -> EUR/USD continuation, signal = sign of the
  EUR/USD move T-10 -> T+10 min around the competitive close, dev, one experiment, 2 trials, p < 0.025 each; B42 val confirmation
  (blocked). Reason: Krohn-Vala-Uthemann-Yang (2025) report a published *lagged* USD response (lessons R081) over a multi-day horizon
  with a large-SD target (lesson R084), on ~70 events a year; needs only an official auction calendar (Fiscal Data API, phase 1 on the
  runner, gate and stop rule fixed in the backlog). The paper's Treasury-futures shock cannot be measured on most of dev (Dukascopy
  US T-Bond CFD minute data start 2018-12-18), so the EUR/USD window move is the stated proxy.
- **Not added:** Raza et al. weekly momentum (re-tests B16 with a shorter lookback; E019 requires fresh data + human decision);
  Valentin post-ECB drift (equities); Fanta ECB communication (no lasting EUR/USD move); Kloks et al. (swaps); EXFormer (ML model);
  KMW EUR window means (all windows seen on dev/val; OOS only, human decision).
- **Next run:** pre-register B40+B41 as E039 (phase 1 auction-calendar fetch on the runner first).

## 2026-11-11 R086 (unattended)
- **State:** last research-batch run 42939744082 (E038) completed and recorded (R084); no run queued or in progress (latest 5 runs all
  completed success). Top `ready` items: B40 + B41 (one experiment). pytest 308 passed before changes, 318 after (10 new tests).
  Workspace clone was on a detached HEAD; checked out `main` and pulled.
- **Choice:** pre-register B40+B41 as E039 (Treasury coupon-auction demand shock -> EUR/USD continuation, dev only, 2 trials,
  p < 0.025 each, block-20 bootstrap, < 150 events NONE). Rule, gate and stop rule exactly as fixed in the backlog (R085); no change.
  Phase 1 (auction calendar from the Fiscal Data API, dev dates only) runs on the runner in the same batch; the run script reads the
  fetch status and gate and records BLOCKED (0 trials) on failure. ustbondtrusd 2019-2020 download is descriptive only.
- **Next run:** collect the research-batch outputs for E039 (or diagnose phase 1 if BLOCKED; parser may be fixed once).

## 2026-11-11 R087 (unattended)
- **State:** research-batch run 42960104359 (E039) completed success; outputs committed by github-actions[bot] (a04cc2c), not yet
  recorded. No run queued or in progress. Workspace clone was on a detached HEAD; checked out `main` and pulled.
- **Choice:** collect E039 (protocol priority 1). Applied `treasury_auction.decide` exactly as pre-registered (R086): calendar gate
  pass; B40 NONE, B41 NONE. No rule or threshold changed.
- **Action:** E039 recorded; B40/B41 `done`, B42 closed unearned (0 trials). Trials dev 249, val 9, total 258. No lead, no
  notification.
- **Next run:** no `ready` backlog item -> backlog refill.
