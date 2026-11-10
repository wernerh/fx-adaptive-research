# E030 Hypothesis: USD appreciation into the Tokyo fix on gotobi dates (dev only; pre-registered 2026-11-10 R061, before any run)

- **H1 (B25):** on gotobi Tokyo dates, a short EUR/USD position from 08:55 to 09:55 Asia/Tokyo (the hour before the 09:55 JST Tokyo
  fix) earns a mean signed mid return > 1 pip per event (USD appreciates into the fix).
- **H0:** the mean signed return per event is zero.
- **Mechanism [PUB]:** Ito & Yamada (2017, Journal of International Economics 109, 214-234, DOI 10.1016/j.jinteco.2017.09.005;
  NBER WP 22820; abstracts opened R060): customer order flow before the Tokyo fix is biased toward buying dollars, giving a
  predictable price pattern, and calendar effects matter for the fixing rate and the price move around fixing time. The paper's
  gotobi definition and magnitude could not be read (full text not fetchable): the day rule used here is the practitioner
  convention and is **UNVERIFIED** as the paper's. The paper studies USD/JPY; EUR/USD carries only the USD leg (loose transfer).
- **Parent experiment / variable changed:** E011 (Tokyo fix, all dates, dev). One variable changed: restricting to gotobi dates.
  Window, direction and data block are E011's `tky_fix_pre`.
- **Prior expectation:** low. E011 all-date pre-fix mean was +0.321 pips (CI incl. 0); gotobi dates are ~30% of those dates. To pass
  the 1-pip bar the gotobi subset would need ~+1 pip and the remaining 70% of dates ~+0.03 or less. SE ~0.4 pips at n ~460, so the
  1-pip bar binds; a significant sub-pip effect is WEAK at best, by design.
- **Why dev is clean for this statistic:** E011 published only the all-date mean; no gotobi split of any window has been computed on
  dev or val. The all-date number bounds but does not reveal the subset.
- **Why now:** top `ready` backlog item (B25; ordered above B26 in R060).
