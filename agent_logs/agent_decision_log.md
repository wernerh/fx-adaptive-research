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
