# Market microstructure notes for EUR/USD

How the market works, as far as it matters for session-based short-term trading. Sources are in academic_studies.md
unless linked here. Labels: **[PUB]** published, **[ASSUMPTION]** our working belief, not yet tested.

## Size and where it trades
- [PUB] BIS Triennial Survey 2025: global OTC FX turnover was **$9.6 trillion per day** in April 2025, up 28% from 2022 ([BIS release](https://www.bis.org/statistics/rpfx25_fx.htm)). EUR/USD remains the most traded pair.
- [PUB] Bank of England / FXJSC: USD/EUR was 23% of UK FX turnover in October 2025. London is the largest trading centre.
- Implication: EUR/USD is the most liquid pair, which means **tight spreads but heavy competition**. Any easy edge is likely to have been competed away (Neely, Weller & Ulrich 2009).

## Market structure
- Decentralised OTC market: dealer banks, interdealer platforms (EBS, Refinitiv/LSEG Matching), many ECNs, and retail brokers that internalise or hedge flow. There is **no single consolidated price or volume**.
- Our data (Dukascopy) is one venue's quotes. Tick volume counts quote updates, not traded amounts.
- [PUB] Order flow (net buyer-initiated volume) drives short-run prices (Evans & Lyons 2002). We cannot observe it, so price-based features are a noisy proxy.

## Time-of-day effects
- [PUB] Activity and volatility rise at the Tokyo and London opens and in the overlap windows; spreads tend to narrow when activity is high (Ito & Hashimoto 2006).
- [PUB] Currencies tend to weaken during their own region's hours (Breedon & Ranaldo 2013), so EUR/USD may show a drift by time of day.
- [PUB] Benchmark fixes cause predictable flows: USD strength into Tokyo (09:55 JST), ECB (14:15 CET) and London 4pm (WM/Reuters) fixes, weakness after (Krohn, Mueller & Whelan 2024). Around the London fix, price changes are very volatile and negatively autocorrelated, most of all at month end (Evans 2018).

| Event | Local time | New York time | Inside our session window? |
|---|---|---|---|
| Tokyo fix | 09:55 Tokyo | 19:55 / 20:55 prior day | Asia (09:00-15:00 Tokyo) |
| ECB reference rate | 14:15 CET/CEST | 08:15 (usually) | US window, 15 min after open (shifts in DST mismatch weeks) |
| US data (NFP, CPI, etc.) | 08:30 New York | 08:30 | US window, 30 min after open |
| London 4pm fix | 16:00 London | 11:00 (usually) | US window, 1 hour before end |
| NY 10:00 options cut | 10:00 New York | 10:00 | US window |
| Daily roll | 17:00 New York | 17:00 | Outside (spreads widen) |

**Takeaway:** our US window (08:00-12:00 NY) contains the ECB fix, 08:30 data, the 10:00 options cut and the 4pm London fix.
It is the busiest scheduled-event window of the day. Any "US-session bias" must be checked against these events.

## Levels and orders
- [PUB] Take-profit orders cluster at round numbers; stop-loss orders cluster just beyond them (Osler 2003). This gives a mechanism for reversals at levels and accelerations through them.
- [ASSUMPTION] The Asian high/low act as stop-cluster levels for London. This is the core idea behind S001/S002 and is not established in the literature.

## Costs
- [ASSUMPTION] Retail ECN all-in round trip on EUR/USD in liquid hours: about 0.2-1.0 pip. Wider around news, at the roll and in thin Asian hours.
- To be measured: the hourly spread profile from Dukascopy (data quality report) and from the paper-trading broker.
