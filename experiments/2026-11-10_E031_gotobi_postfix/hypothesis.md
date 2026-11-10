# E031 Hypothesis: USD depreciation after the Tokyo fix on gotobi dates (dev only; pre-registered 2026-11-10 R063, before any run)

- **H1 (B26):** on gotobi Tokyo dates, a long EUR/USD position from 09:55 to 10:55 Asia/Tokyo (the hour after the 09:55 JST Tokyo
  fix) earns a mean signed mid return > 1 pip per event (USD gives back fix-time gains once the order imbalance is filled).
- **H0:** the mean signed return per event is zero.
- **Mechanism [PUB]:** Ito & Yamada (2017, Journal of International Economics 109, 214-234, DOI 10.1016/j.jinteco.2017.09.005;
  NBER WP 22820; abstracts opened R060): predictable dollar-buying customer flow into the Tokyo fix moves the price; a fix-time
  spike from an order imbalance implies a partial reversal afterwards. That the reversal is strongest on gotobi dates is
  **UNVERIFIED** as the paper's finding; the gotobi day rule is the practitioner convention (UNVERIFIED as the paper's). The paper
  studies USD/JPY; EUR/USD carries only the USD leg (loose transfer).
- **Parent experiment / variable changed:** E011 (Tokyo fix, all dates, dev), window `tky_fix_post`. One variable changed: restricting
  to gotobi dates. Sibling E030 (B25) tested the pre-fix window on the same dates.
- **Prior expectation:** low. E011 all-date post-fix mean was +0.785 pips (CI (0.318, 1.173), WEAK). E030 found no gotobi pre-fix
  USD appreciation (+0.180, below the non-gotobi control), which weakens the "larger imbalance on gotobi -> larger reversal" story.
  SE ~0.35-0.4 pips at n ~460, so the 1-pip bar binds.
- **Why dev is still usable for this statistic:** E011 published only the all-date post-fix mean; no gotobi split of the post-fix
  window has been computed on dev or val. E030 computed only the pre-fix window on gotobi dates. Because the all-date post-fix effect
  is already positive, a gotobi SIGNAL must also beat the non-gotobi control descriptively to be interesting; this does not change
  the rule.
- **Why now:** top `ready` backlog item (B26) after B25 closed in R062.
