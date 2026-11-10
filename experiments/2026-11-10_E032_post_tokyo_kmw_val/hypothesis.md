# E032 Hypothesis: post-Tokyo-fix EUR appreciation in the KMW window (val only; pre-registered 2026-11-10 R066, before any run)

- **H1 (B27):** on val trading dates, a long EUR/USD position from 20:55 to 02:00 America/New_York (Krohn, Mueller & Whelan's
  post-Tokyo window, used verbatim in NY clock time) earns a mean signed mid return > 1 pip per date (USD depreciation after the Tokyo
  fix as dealers unwind pre-fix hedges).
- **H0:** the mean signed return per date is zero.
- **Mechanism [PUB]:** Krohn, Mueller & Whelan (JF 2024, 79(1) 541-578; Bank of Canada SWP 2021-48, opened R065): "an appreciation of
  the U.S. dollar pre-fix and a depreciation post-fix", driven by dealers hedging dollar demand at the fixes; window verbatim
  "8:55 p.m. to 2:00 a.m. ET"; robustness "not driven by day of the week or month of the year effects". EUR-specific magnitude
  (+5.89% p.a., t 9.29) read via a model summary only: **UNVERIFIED**. Details: research/backlog.md B27, research/academic_studies.md.
- **Parent experiment / variable changed:** none formally (new window: the full 5h05m post-Tokyo window, unconditional, every date).
  Relatives: E011 (dev, first hour after the fix only, WEAK +0.785), E030/E031 (dev, gotobi subsets), E009 (dev hourly cells).
- **Why val only:** dev is contaminated: E009 published every NY-hour cell of this window on dev (ny_21 +0.655, ny_22 +0.591,
  ny_23 -0.027, ny_00 +0.197, ny_01 -0.240; sum about +1.18 pips). No experiment has computed this window's return on val (E029 val
  used 17:05 -> 02:00 NY on 4 conditional events; E012/E017/E023/E025 val windows do not overlap; E014 val FOMC 16:00 -> 16:00 NY
  covers ~20 dates; E001/E006 used Asian-session structure only as predictors of the US session, not its mean).
- **Prior expectation (written before data):** low to moderate. Dev-implied ~+1.2 pips gross would be WEAK at best given SE ~0.7-0.8
  pips (before block correction) at n ~600; a SIGNAL needs a val mean of roughly 1.6+ pips.
- **LEAD status:** a val-only SIGNAL cannot meet the LEAD definition (no clean pre-registered dev pass). A val SIGNAL that also
  survives costs x1.5 is logged in agent_decision_log.md as an OOS candidate for the human (no notification, no OOS run).
- **Why now:** top (only) `ready` backlog item (B27), added R065.
