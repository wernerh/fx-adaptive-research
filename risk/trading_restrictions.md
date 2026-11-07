# Trading restrictions

| Restriction | Default | Reason |
|---|---|---|
| High-impact US/EU releases (NFP, CPI, FOMC, ECB) | No entry from 5 min before to 15 min after, unless the strategy is explicitly an event strategy | Spread widening and slippage |
| Rollover | No entry 16:55 to 17:10 New York | Spreads widen sharply at the daily roll |
| Weekend | No open positions over Friday 17:00 New York | Gap risk |
| Thin holidays | Skip 24 Dec to 2 Jan, US/UK bank holidays | Thin liquidity |
| Max spread | 2.0 pips at entry | Cost control |
| DST mismatch weeks | Allowed, but tracked separately in results | Session overlap shifts by an hour |
