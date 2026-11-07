# E001 Methodology

- **Data:** Dukascopy EUR/USD 1-minute bid/ask, 2015-01-01 to latest. Quality report must be saved to data/data_quality_reports.md first.
- **Sessions:** SPEC section 2 (Tokyo 09:00-15:00, London 08:00-12:00, New York 08:00-12:00 local time).
- **Blocks:** dev 2015-01-01..2020-12-31, val 2021-01-21..2023-06-30, OOS 2023-07-21..latest (20-day embargoes). OOS NOT used in this run.
- **Statistics per predictor and block:** hit rate with Wilson 95% CI, two-sided binomial p, Bonferroni-adjusted p (x7),
  Spearman IC, mean signed pips with 20-day moving-block bootstrap 95% CI. Costs NOT included (this is a signal test).
- **Decision rule (pre-registered):**
  - SIGNAL if Bonferroni p < 0.05 in dev AND same sign with p < 0.05 (unadjusted) in val AND mean signed pips > 1.0 (the rough round-trip cost) in both.
  - WEAK if significant in one block only, or mean signed pips <= 1.0.
  - NONE otherwise. Record in knowledge/rejected_hypotheses.md.
- **Benchmark rule:** a conditional predictor counts as SIGNAL only if its mean signed pips also exceed the
  `unconditional_long` mean in the same block (otherwise it is just picking up the time-of-day drift).
- **Known confound:** the London 4pm WM/Reuters fix (11:00 New York) falls inside the US window. Krohn, Mueller &
  Whelan (2024) document USD strength before fixes and weakness after. Exploratory breakdown: 08:00-10:55 vs 11:05-12:00 NY.
- **Breakdowns (exploratory, label as such):** by year, by asia_range_atr tercile, by weekday, excluding high-impact event days once the calendar is available.
- **Command:** `python scripts/run_e001_baseline.py`
