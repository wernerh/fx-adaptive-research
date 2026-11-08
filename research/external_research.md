# External research (non-peer-reviewed)

Practitioner material, vendor backtests and trading education. **None of this counts as evidence for promotion.**
It is recorded so we know which claims are circulating and can test them. Label every entry with how it could be checked.

### 2026-11-07: Backtrex, "Does the London breakout strategy work on EUR/USD?"
- **Link:** https://backtrex.com/en/backtests/london-breakout-eur-usd
- **Claim:** a 10-year (Oct 2016 to Oct 2026) 1-hour backtest of the Asian-range (00:00-06:00 UTC) breakout during 07:00-10:00 UTC with a 2:1 target reported 1,230 trades, a 36.3% win rate, a profit factor of 0.87 and a -28% total return, with only 3 of 11 calendar years positive. A 15-minute GBP/USD version also lost.
- **Our view:** consistent with the academic prior (Neely & Weller 2003). Rules differ from S001 (hourly bars, fixed 2R, different windows), so it does not reject S001, but it lowers our prior.
- **How to check:** E004 runs S001 with our cost model; a variant can replicate these exact rules.

### 2026-11-07: Retail education claims about Asian-range breakouts
- Several retail sites claim high follow-through rates for Tokyo-range breakouts at the London open (for example ~70% when aligned with the prior day's trend), with no data, method or cost model given.
- **Our view:** **UNVERIFIED**, treated as hypotheses only. "Follow-through" is usually undefined and costs are ignored.
- **How to check:** the alignment idea can become an E00x predictor (`lon_break_side` x sign of prior-day return).

### 2026-11-07: "Opening range" variants
- Practitioner versions define the range differently: the 30 minutes before London, 00:00-06:00 UTC, 00:00-08:00 GMT, candle bodies only, and so on.
- **Our view:** each definition is a separate trial and counts towards the multiple-testing correction. Pick one in advance (SPEC 2) and test others only as one-variable experiments.

### 2026-11-08: Robot Wealth, "Exploiting the Non-Farm Payrolls drift" (K. Longmore, 2020)
- **Link:** https://robotwealth.com/exploiting-the-non-farm-payrolls-drift/
- **Claim:** EUR/USD 5-minute bars, 2009-2018, first-Friday NFP days: on days with a bullish first-hour post-release reaction, price drifted up in the hours before 08:30 ET on average, and down before bearish reactions. The author says this uses future information to classify days, is not tradable as written, and gives no performance figures.
- **Our view:** look-ahead by construction; not a testable strategy. It does show NFP-day intraday paths are used in practice. Not used for B12, which tests post-release continuation with information available at 08:45 NY.
- **How to check:** n/a without an ex-ante predictor of the release surprise.
