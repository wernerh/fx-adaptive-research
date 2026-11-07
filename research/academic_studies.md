# Academic studies

Literature review, first pass: 2026-11-07. Every entry was checked against a publisher, RePEc, central bank or
university record on that date. Findings are paraphrased from abstracts and working-paper versions; read the full
paper before relying on a detail. Verification status: **VERIFIED (abstract)** = bibliographic details and main
finding confirmed from an official abstract page; full text not reviewed line by line.

## Summary: what the literature says about our hypothesis

1. **Time-of-day return patterns in FX are real.** Currencies tend to weaken during their own region's trading hours
   (Breedon & Ranaldo), and the USD follows a reversal pattern around the big benchmark fixes (Krohn, Mueller & Whelan).
   For us this means (a) the US session may have a directional drift of its own, so E001 must beat an
   "always long" benchmark, and (b) the London 4pm fix (11:00 New York) sits inside our US window.
2. **Order flow drives short-run FX prices** (Evans & Lyons). This is the best-supported mechanism for why one
   session's activity could carry into the next. We cannot see order flow directly, only price.
3. **Activity and spreads follow regional business hours** (Ito & Hashimoto). Liquidity, and therefore costs,
   change sharply at session opens, which matters for entries timed at the London or US open.
4. **Macro announcements move FX within minutes** (Andersen, Bollerslev, Diebold & Vega). US data at 08:30 New York
   falls inside our US window and can overwhelm any session-based signal.
5. **Order clustering at round numbers** gives a mechanism for both reversals at levels and accelerations through
   them (Osler). This is the closest academic support for "liquidity sweep" and breakout ideas.
6. **Intraday momentum** (early return predicts late return) is documented in equities, in currency futures anchored
   to the futures close (Baltussen et al.), and in a session-based FX market (RUB/USD on an exchange with fixed hours).
   We found no study showing that it carries **across sessions** in 24-hour spot EUR/USD. That is an open question, and E001 tests a version of it.
7. **The sobering part:** intraday technical rules in FX showed no excess returns after realistic costs
   (Neely & Weller 2003), and documented FX trading-rule profits faded once they became widely known (Neely, Weller & Ulrich 2009).
   Our prior should be that **most session-based edges are either absent or too small to survive costs**.
8. **Testing many variants inflates results.** The Deflated Sharpe Ratio (Bailey & López de Prado) is the correction we adopt.

**Net assessment:** published evidence supports the *mechanisms* (time-of-day flows, order flow, stop clustering,
fixing flows, news) but **not** the claim that Asian/London structure gives a cost-surviving directional edge in the
US session. That is unproven, which is exactly why E001 comes first.

---

## Entries

### Breedon & Ranaldo (2013): Intraday patterns in FX returns and order flow
- **Venue:** Journal of Money, Credit and Banking 45(5), 953-965. DOI [10.1111/jmcb.12032](https://doi.org/10.1111/jmcb.12032). Working paper: [SNB WP 2011-04](https://www.snb.ch/en/publications/research/working-papers/2011/working_paper_2011_04)
- **Data:** EBS interdealer spot rates and order flow, 1997-2007, several currencies; single-dealer data for corroboration.
- **Finding:** currencies tend to depreciate during their local trading hours and appreciate outside them. The pattern also shows up in order flow. The authors attribute it to participants being net buyers of foreign currency during their own hours. The SNB working-paper abstract says that for EUR/USD the pattern can form a simple profitable trading strategy.
- **Relevance:** **High.** Implies a time-of-day drift in EUR/USD across the Europe and US windows. Added `unconditional_long` as the E001 benchmark.
- **Caveats:** sample ends 2007, interdealer costs. Retail costs and post-2008 market structure are untested.
- **Status:** VERIFIED (abstract)

### Krohn, Mueller & Whelan (2024): Foreign exchange fixings and returns around the clock
- **Venue:** Journal of Finance 79(1), 541-578. DOI [10.1111/jofi.13306](https://doi.org/10.1111/jofi.13306). Working paper: [Bank of Canada SWP 2021-48](https://www.bankofcanada.ca/wp-content/uploads/2021/10/swp2021-48.pdf)
- **Finding:** the USD tends to appreciate in the run-up to the major fixes (Tokyo, ECB, London) and depreciate afterwards, producing a W-shaped 24-hour pattern. The explanation offered is dealers hedging an unconditional demand for dollars at the fixes. An earlier version notes the reversals may be exploitable after costs by low-cost traders.
- **Relevance:** **High.** The London 4pm fix (11:00 New York) is inside our US window, and the ECB reference rate (14:15 CET, about 08:15 New York) falls 15 minutes into it. Session returns are partly fixing effects, not "information". E001 now includes a pre-fix/post-fix breakdown.
- **Status:** VERIFIED (abstract)

### Evans (2018): Forex trading and the WMR Fix
- **Venue:** Journal of Banking & Finance 87, 233-247. DOI [10.1016/j.jbankfin.2017.09.017](https://doi.org/10.1016/j.jbankfin.2017.09.017). Preprint: [MPRA 81583](https://mpra.ub.uni-muenchen.de/81583/)
- **Finding:** across 21 currency pairs over a decade, price changes just before and after the 4pm London fix are unusually volatile and negatively serially correlated, especially on the last trading day of the month.
- **Relevance:** **Medium.** Avoid holding short-duration trades across 11:00 New York without testing for it. Month-end days should be flagged.
- **Status:** VERIFIED (abstract)

### Evans & Lyons (2002): Order flow and exchange rate dynamics
- **Venue:** Journal of Political Economy 110(1), 170-180. DOI [10.1086/324391](https://doi.org/10.1086/324391). NBER [w7317](https://www.nber.org/papers/w7317)
- **Finding:** interdealer order flow (net buying pressure) explains a large share of daily DM/USD changes. The authors report R-squared above 50-60%, far more than macro models, and better short-horizon forecasts than a random walk out of sample.
- **Relevance:** **Foundational.** The best-supported reason that price moves in one session could persist is that order flow carries information. We only observe prices and tick counts, so our features are a weak proxy for flow.
- **Status:** VERIFIED (abstract)

### Ito & Hashimoto (2006): Intraday seasonality in activities of the FX markets: evidence from the electronic broking system
- **Venue:** Journal of the Japanese and International Economies 20(4), 637-664. NBER [w12413](https://www.nber.org/papers/w12413)
- **Data:** EBS firm quotes and deals, USD/JPY and EUR/USD.
- **Finding:** activity is U-shaped within Tokyo and London business hours but not New York. Volatility rises with activity, while spreads narrow when deals are frequent. Trading concentrates in the overlap windows (Tokyo-London, London-New York).
- **Relevance:** **Medium.** Supports our session boundaries and warns that spreads and costs vary by time of day. Our cost model uses actual spreads per bar for this reason.
- **Status:** VERIFIED (abstract)

### Andersen, Bollerslev, Diebold & Vega (2003): Micro effects of macro announcements: real-time price discovery in foreign exchange
- **Venue:** American Economic Review 93(1), 38-62. DOI [10.1257/000282803321455151](https://doi.org/10.1257/000282803321455151)
- **Finding:** announcement surprises cause near-immediate jumps in the conditional mean of USD exchange rates, with timing and sign asymmetries (bad news has a larger effect).
- **Relevance:** **High** for the US window. US releases at 08:30 New York land at the start of our US session. Every strategy must be tested with and without event days, and S005 (announcement reaction) needs surprise data, not just release times.
- **Status:** VERIFIED (abstract)

### Osler (2003): Currency orders and exchange rate dynamics: an explanation for the predictive success of technical analysis
- **Venue:** Journal of Finance 58(5), 1791-1819. DOI [10.1111/1540-6261.00588](https://doi.org/10.1111/1540-6261.00588). Working paper: [FRBNY Staff Report 125](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr125.pdf)
- **Data:** roughly 9,700 stop-loss and take-profit orders at one large dealing bank, 1999-2000, including EUR/USD.
- **Finding:** take-profit orders cluster at round numbers, which helps explain reversals at support and resistance. Stop-loss orders cluster just beyond round numbers, which helps explain accelerations after levels break.
- **Relevance:** **High** for S001/S002 mechanism. A break of a level where stops cluster (e.g. Asian high/low, round numbers) can accelerate briefly. Candidate feature: distance of the Asian high/low from the nearest 50-pip round number.
- **Caveats:** single bank, eight months, 25 years ago.
- **Status:** VERIFIED (abstract)

### Elaut, Frömmel & Lampaert (2018): Intraday momentum in FX markets: disentangling informed trading from liquidity provision
- **Venue:** Journal of Financial Markets 37, 35-51. DOI [10.1016/j.finmar.2016.09.002](https://doi.org/10.1016/j.finmar.2016.09.002)
- **Finding:** in RUB/USD on the Moscow exchange (2005-2014), the first half-hour return predicts the last half-hour return. The effect is attributed to liquidity providers' reluctance to hold positions overnight, and is stronger in crises.
- **Relevance:** **Low to medium.** The effect relies on explicit trading hours; EUR/USD trades 24 hours. A loose analogue to test: does the London-session move predict the end of the US morning?
- **Status:** VERIFIED (abstract)

### Gao, Han, Li & Zhou (2018): Market intraday momentum
- **Venue:** Journal of Financial Economics 129(2), 394-414. DOI [10.1016/j.jfineco.2018.05.009](https://doi.org/10.1016/j.jfineco.2018.05.009)
- **Finding:** for the S&P 500 ETF (1993-2013), the first half-hour return (measured from the previous close) predicts the last half-hour return. Predictability is stronger on volatile, high-volume, recession and major-news days.
- **Relevance:** **Low.** Equity evidence; the origin of the intraday momentum idea.
- **Status:** VERIFIED (abstract)

### Baltussen, Da, Lammers & Martens (2021): Hedging demand and market intraday momentum
- **Venue:** Journal of Financial Economics 142(1), 377-403. DOI [10.1016/j.jfineco.2021.04.029](https://doi.org/10.1016/j.jfineco.2021.04.029). [Preprint](https://www3.nd.edu/~zda/intramom.pdf)
- **Finding:** across 60+ futures on equities, bonds, commodities **and currencies** (1974-2020), the return over the rest of the day predicts the return in the last 30 minutes before the close. The authors link this to gamma hedging by option market makers and leveraged ETFs, and the effect reverses over the following days.
- **Relevance:** **Medium.** Shows intraday momentum in currency futures, but anchored to the futures close, which has no clean equivalent in 24-hour spot. A testable analogue: does the 00:00-11:30 NY move predict 11:30-12:00 NY? This is not part of the current hypothesis; logged as an idea.
- **Status:** VERIFIED (abstract)

### Neely & Weller (2003): Intraday technical trading in the foreign exchange market
- **Venue:** Journal of International Money and Finance 22(2), 223-237. DOI [10.1016/S0261-5606(02)00101-8](https://doi.org/10.1016/S0261-5606(02)00101-8)
- **Finding:** intraday trading rules selected by genetic programming and by an optimised linear model earned **no excess returns out of sample** once realistic transaction costs and trading hours were included, although the rules found some stable patterns.
- **Relevance:** **High, cautionary.** This is the closest published test to what we are doing, and it found nothing after costs. A pattern can be real and still not be tradeable.
- **Status:** VERIFIED (abstract)

### Neely, Weller & Ulrich (2009): The adaptive markets hypothesis: evidence from the foreign exchange market
- **Venue:** Journal of Financial and Quantitative Analysis 44(2), 467-488. DOI [10.1017/S0022109009090103](https://doi.org/10.1017/S0022109009090103)
- **Finding:** trading-rule profits in the 1970s and 1980s were genuine, but filter and moving-average rule profits had disappeared by the early 1990s. Less-studied rules also declined. High volatility makes mean returns hard to estimate precisely.
- **Relevance:** **High.** Edges decay once known. Popular retail setups (Asian range breakout, London "kill zones") are widely known, so expect weak results, and re-validate on a schedule.
- **Status:** VERIFIED (abstract)

### Bailey & López de Prado (2014): The Deflated Sharpe Ratio: correcting for selection bias, backtest overfitting and non-normality
- **Venue:** Journal of Portfolio Management 40(5), 94-107. DOI [10.3905/jpm.2014.40.5.094](https://doi.org/10.3905/jpm.2014.40.5.094). [SSRN 2460551](https://papers.ssrn.com/abstract=2460551)
- **Finding:** reported Sharpe ratios are inflated by testing many variants and by non-normal returns. The DSR adjusts for the number of trials, skewness and kurtosis.
- **Relevance:** **Methodology.** Adopted in SPEC section 5.2. Every variant we try is counted in the experiment registry.
- **Status:** VERIFIED (abstract)

---

## Open research questions raised by the literature

| # | Question | Source of the idea | Experiment |
|---|---|---|---|
| Q1 | Does EUR/USD have an unconditional drift in 08:00-12:00 New York, and has it persisted after 2007? | Breedon & Ranaldo | E001 (`unconditional_long`) |
| Q2 | Do London/Asia predictors still work once the pre/post 4pm-fix split is controlled? | Krohn et al.; Evans | E001 breakdown, then E005 |
| Q3 | Are false breaks of the Asian range more common when the Asian high/low sits just inside a round number? | Osler | Future feature experiment |
| Q4 | Do session signals survive on days without high-impact US releases? | Andersen et al. | E003 |
| Q5 | Has any effect decayed over 2015-2026? | Neely, Weller & Ulrich | Year-by-year breakdown in every experiment |

## Not yet reviewed (candidates for the next literature pass; titles and venues recalled, NOT verified)
- Ranaldo & Somogyi (2021), asymmetric information risk in FX markets (JFE): FX order-flow information by participant type.
- Cespa, Gargano, Riddiough & Sarno (2022), FX volume (RFS): volume measures for FX.
- Chaboud, Chiquoine, Hjalmarsson & Vega (2014), "Rise of the machines" (JF): algorithmic trading's effect on FX microstructure.
- King, Osler & Rime (2013), FX microstructure survey (JIMF): broad context.
- Menkhoff & Taylor (2007), the "obstinate passion" survey of technical analysis in FX.
