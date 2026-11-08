# E014 Hypothesis: FOMC statement-day long EUR/USD, val confirmation of E013 (pre-registered 2026-11-08 R021, before any val run)

- **H1 (B11v):** over the 24 hours from 16:00 America/New_York on the business day before a **scheduled** FOMC statement to
  16:00 NY on the statement day, EUR/USD (mid) rises on average by more than 10 pips, on the **val block** (2021-01-21..2023-06-30).
- **H0:** mean long return over that window on val is zero.
- **Origin:** E013 SIGNAL on dev (n 47, mean +21.284 pips, block-4 CI (2.747, 38.163), one-sided t p 0.029;
  backtests/validation_reports/E013_results.json). The E013 methodology fixed this follow-up before its run.
- **Mechanism [PUB]:** as E013 (Mueller, Tahbaz-Salehi & Vedolin 2017, JF, DOI 10.1111/jofi.12499).
- **Parent experiment / variable changed:** E013; variable changed = block (dev -> val). Window, rule, thresholds, bootstrap block,
  cost check and date file are unchanged.
- **Prior expectation:** low. Dev means are often inflated by selection (E013 was the 227th dev trial), and val (2022 hiking cycle,
  dollar spike) is a regime where USD *strength* around hawkish meetings is plausible. Only ~20 val meetings; with sd ~75 pips the CI
  bar needs a mean of roughly +35 pips. A NONE result here does not disprove the published few-bp effect.
- **Why now:** top `ready` backlog item (B11v), ranked above B12 in R020 (agent_decision_log). It is the only open line that can produce a lead.
