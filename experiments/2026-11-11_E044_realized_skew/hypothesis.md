# E044 Hypothesis: daily realized skewness -> next-day EUR/USD (B50), dev only (pre-registered 2026-11-11 R100, before any run)

- **H1 (B50):** on the dev block, a position s = sign(RS(D)), where RS(D) is the realized skewness of 5-minute EUR/USD mid returns
  from 18:00 NY (start of trading date D) to 16:55 NY on D, entered at 20:00 NY on D and exited at 16:55 NY on D+1, earns a mean
  signed mid return > 1 pip per date (positive skew today -> EUR/USD up tomorrow).
- **H0:** the mean signed return per date is zero.
- **Mechanism [PUB, cross-section only]:** Jiang, Han & Yin (2019, NAJEF 48, DOI 10.1016/j.najef.2018.07.018, abstract): "a positive
  and significant relationship between skewness and future currency excess returns". Reading: right-tail bursts not yet fully
  priced / crash-risk premium paid later. Measure, horizon and currency list UNVERIFIED; the single-pair daily time-series version is
  our extension. Sign fixed from the abstract, not from data.
- **Parent experiment / variable changed:** none (new family: shape of the intraday return distribution). Same hold window as E033
  (B28/B29, both NONE on dev); RS is correlated with the daily return R(D), reported descriptively.
- **Contamination note:** no skewness or higher-moment statistic has been computed in this repo before (grep R099). The E033 hold
  window's daily-return-conditioned means on dev are known (B28 -2.034, B29 -0.213, both NONE). Dev usable.
- **Prior expectation:** weak. ~262 registered trials: a single p just under 0.05 is expected noise (lesson R092), hence the separate
  val confirmation (B51) before anything counts.
- **Why now:** top `ready` backlog item after the R099 refill; no research-batch run queued or in progress.
