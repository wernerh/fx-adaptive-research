# E017 Hypothesis: home-hours depreciation, EUR down in European-only hours and up in US-only hours (val only; pre-registered 2026-11-08 R029, before any run)

- **H1 (B14):** on each FX trading date, -(EUR/USD mid return 03:00-08:00 America/New_York) + (mid return 12:00-17:00 America/New_York)
  is positive, > 1 pip on average (short EUR/USD in European-only hours, long in US-only hours).
- **H0:** the mean daily signed return is zero.
- **Mechanism [PUB]:** currencies tend to depreciate during their own region's trading hours and appreciate outside them, consistent
  with local participants being net buyers of foreign currency (Breedon & Ranaldo 2013, JMCB, DOI 10.1111/jmcb.12032; entry in
  research/academic_studies.md, VERIFIED (abstract) 2026-11-07). The abstract states a simple EUR/USD strategy based on it was profitable.
  Sample ended 2007; the effect may have been arbitraged away (Neely, Weller & Ulrich 2009).
- **Paper hour definitions: UNVERIFIED.** R029 tried to open the SNB working paper (working_paper_2012_04 page and PDF on snb.ch)
  and the DOI page; all three fetches failed (fetch-permission timeout, nothing read). The windows below were fixed in the backlog
  (R025) from the mechanism, not from data or the paper, and are **not** changed.
- **Parent experiment / variable changed:** none (new hypothesis); E001 `unconditional_long` (08:00-12:00 NY) is the nearest prior result.
- **Prior expectation:** low. E001 found no drift 08:00-12:00 NY (+0.59 dev / +0.71 val, CIs include 0); E007/E010/E011 found
  sub-pip time-of-day effects.
- **Why val only:** E009 scanned every hour of dev, so dev is not clean for any time-of-day window. Consequence fixed now: a val SIGNAL
  cannot meet the LEAD definition (needs a dev pass + separate val confirmation). A val SIGNAL that survives costs x1.5 is logged in
  agent_logs/agent_decision_log.md as a candidate needing a human OOS decision (no notification, not a LEAD).
- **Why now:** top `ready` backlog item (B13 blocked in R028).
