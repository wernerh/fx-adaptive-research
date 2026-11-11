# E038 Hypothesis: intraday momentum into the 17:00 NY spot roll, dev only (pre-registered 2026-11-11 R083, before any run)

- **H1 (B38):** on every valid dev trading date D (17:00 NY roll), the sign of the EUR/USD mid return from the start of D (17:00 NY)
  to 16:25 NY predicts the mid return 16:25 -> 16:55 NY on D: mean of sign(r1) x r2 > 1 pip per date, with hit rate > 0.5.
- **H0:** the mean signed return per date is zero (no continuation into the roll).
- **Mechanism [PUB, abstract only]:** Baltussen, Da, Lammers & Martens (2021, JFE 142(1) 377-403, DOI 10.1016/j.jfineco.2021.04.029;
  research/academic_studies.md, VERIFIED (abstract)): in 60+ futures including currencies, the rest-of-day return predicts the
  last 30 minutes before the close (hedging demand of option gamma hedgers and leveraged products). **Anchor variant, not a
  replication:** spot EUR/USD has no exchange close; the 17:00 NY value-date roll is the market-wide daily cut. Exact
  currency-futures close convention and currency effect sizes: UNVERIFIED.
- **Parent experiment / variable changed:** E016/B13 (same rule, anchor = CME settlement, blocked before any trial). One variable
  changed: the anchor (17:00 NY spot roll instead of the CME settlement time).
- **Prior:** weak. The 1.0-pip bar on a 30-minute window will probably bind. A clean NONE closes the line (B39 closes unearned).
- **Why dev is clean:** E009 scanned unconditional hourly means only; this conditional statistic has never been computed. E027/B22 and
  E026/B21 used other predictors and targets.
- **Why now:** top `ready` backlog item after the R082 refill; no research-batch run queued or in progress (last run 42915756793
  recorded as E037 in R081).
