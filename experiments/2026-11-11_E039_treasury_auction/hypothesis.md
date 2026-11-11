# E039 Hypothesis: Treasury coupon-auction demand shock -> EUR/USD continuation, dev only (pre-registered 2026-11-11 R086, before any run)

- **H1 (B40):** on dev US Treasury nominal coupon-auction events (auction date D, competitive close time T, NY), the sign s of the
  EUR/USD mid move T-10 min -> T+10 min predicts the mid return from T+10 min to 16:00 NY on the **10th** trading date after D:
  mean of s x return > 1 pip per event.
- **H1 (B41):** same events, signal and entry; exit at 16:00 NY on the **1st** trading date after D: mean > 1 pip per event.
- **H0 (each arm):** the mean signed return per event is zero (no continuation of the auction-window move).
- **Mechanism [PUB, partial text]:** Krohn, Vala, Uthemann & Yang (2025, Bank of Canada Staff Working Paper 2025-29; research
  backlog B40, R085): a positive Treasury demand shock at a coupon auction (Treasury futures up from 10 minutes before to 10 minutes
  after the auction close, ET) is followed by USD depreciation against G9 currencies that "peaks at nearly 20 basis points around 10
  days after an auction" and reverts to insignificance after 14 days (verbatim, local projections). EUR-specific coefficient seen only
  in a summary: UNVERIFIED. **Proxy variant, not a replication:** the shock sign is the EUR/USD move in the paper's own window
  (EUR up = USD down = positive demand shock), because Dukascopy Treasury CFD minute data start 2018-12-18. The paper reports no
  trading rule, costs or OOS test.
- **Parent experiment / variable changed:** none (new conditioning event: Treasury coupon auctions). The two arms differ only in the
  hold (10 vs 1 trading dates) and are counted as 2 trials.
- **Prior:** weak to moderate. The proxy is noisy and 10-date holds overlap (~3-4 open at once), so a NONE does not rule out the
  paper's effect measured with Treasury futures.
- **Why dev is clean:** no auction-date conditioning has ever been computed on dev. E009 hour cells (13:00 NY) are unconditional,
  E026 used 08:30 NY windows, E019 used a 16:00 -> 16:00 trend.
- **Why now:** top `ready` backlog items (B40/B41) after the R085 refill; no research-batch run queued or in progress (last run
  42939744082 recorded as E038 in R084).
