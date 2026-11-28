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

**Added 2026-11-08 (R016 refill pass): central-bank and release-day evidence.**

### Mueller, Tahbaz-Salehi & Vedolin (2017): Exchange rates and monetary policy uncertainty
- **Venue:** Journal of Finance 72(3), 1213-1252. DOI [10.1111/jofi.12499](https://doi.org/10.1111/jofi.12499). Accepted versions: [LSE eprint 77256](https://eprints.lse.ac.uk/77256/), [Warwick WRAP 94006](https://wrap.warwick.ac.uk/94006/)
- **Finding:** a strategy short the USD and long other currencies earns significantly larger excess returns on scheduled FOMC announcement days; larger for currencies with higher rate differentials vs the US, rising with monetary-policy uncertainty and when the Fed is easing. Interpreted as compensation for policy uncertainty borne by constrained intermediaries.
- **Relevance:** **Medium.** Gives a signed, ex-ante-definable FOMC-day prediction for EUR/USD (long EUR). EUR had a *negative* rate differential vs USD for most of 2015-2023, so the cross-sectional part predicts a weaker effect for EUR than for high-yielders. Magnitudes not in the abstract. -> backlog B11.
- **Status:** VERIFIED (abstract, repository records opened 2026-11-08)

### Karnaukh (2018, working paper): The dollar ahead of FOMC target rate changes
- **Venue:** working paper dated 2018-07-26, Ohio State University; no journal stated in the text read. [PDF (AUT ACFR conference copy)](https://acfr.aut.ac.nz/__data/assets/pdf_file/0019/190315/DollarAheadFOMC_NinaKarnaukh.pdf)
- **Finding (1994-2015, 176 scheduled meetings, Olsen 5-min EUR/GBP/CHF/JPY):** the USD rises from 14:00 two days before to 14:00 on announcement day ahead of raises signalled by fed funds futures (mean +20 bp, t 1.99) and falls before signalled cuts (-32 bp, t -2.06; -16 bp excl. fall 2008). Unconditionally, neutral meetings show only a 5-10 bp USD drift down. Partial, weak reversal in the two days after.
- **Relevance:** **Medium, blocked on data.** The signal needs daily fed funds futures, which we do not have. The unconditional "neutral meeting" USD-down drift overlaps with MTV (B11). EUR-specific numbers were only in a model-extracted part of the fetch: UNVERIFIED.
- **Status:** VERIFIED (working paper, first ~40k characters read 2026-11-08); not peer-reviewed as far as checked

### Almeida, Goodhart & Payne (1998): The effects of macroeconomic news on high frequency exchange rate behavior
- **Venue:** Journal of Financial and Quantitative Analysis 33(3), 383-408. DOI [10.2307/2331101](https://doi.org/10.2307/2331101). [Cambridge page](https://www.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/effects-of-macroeconomic-news-on-high-frequency-exchange-rate-behavior/CE5AB6783BC3486CD07ACF242A73FBB8); working paper [LSE eprint 119153](https://researchonline.lse.ac.uk/id/eprint/119153)
- **Finding:** DEM/USD at 5-minute frequency: most announcements move the rate significantly in the 15 minutes after release; significance falls quickly as the horizon lengthens, with little effect left after three hours for most announcements. US scheduled releases are absorbed much faster than German ones.
- **Relevance:** **Medium.** Prior for B12: the NFP reaction should be mostly complete within ~15 minutes, so continuation over the next hour should be absent (efficient) unless liquidity is slow to return.
- **Status:** VERIFIED (abstract; Cambridge page metadata lists the authors inconsistently, the LSE record lists all three)

### Osler (2002 staff report; journal version 2005): Stop-loss orders and price cascades in currency markets
- **Venue:** FRBNY Staff Report 150 (June 2002), [HTML/PDF](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr150.html), [RePEc record](https://econpapers.repec.org/RePEc:fip:fednsr:150). RePEc lists a 2005 journal article of the same title; journal, volume and DOI **UNVERIFIED** (not on the pages opened).
- **Finding (abstract, opened 2026-11-08 R031):** currency stop-loss orders contribute to rapid, self-reinforcing "price cascades"; trends are unusually rapid when rates reach stop-loss clusters; the response to stop-loss orders is larger and lasts longer than to take-profit orders; "Most results are statistically significant for hours, although not for days." Stop-loss sells cluster just below, buys just above, round numbers (rates ending in 00 or 50).
- **Relevance:** **Medium.** Basis for B15 (round-number crossing continuation), a price-level test that does not reuse the dev time-of-day scan.
- **Caveats:** 1990s/2000 dealer order data; only the first ~40% of the staff-report text was read verbatim.
- **Status:** VERIFIED (abstract, staff report); journal version UNVERIFIED

### Moskowitz, Ooi & Pedersen (2012): Time series momentum
- **Venue:** Journal of Financial Economics 104(2), 228-250. DOI [10.1016/j.jfineco.2011.11.003](https://doi.org/10.1016/j.jfineco.2011.11.003). [RePEc record](https://econpapers.repec.org/RePEc:eee:jfinec:v:104:y:2012:i:2:p:228-250)
- **Finding (abstract, opened 2026-11-08 R031):** time series momentum in equity index, currency, commodity and bond futures for 58 liquid instruments; "persistence in returns for one to 12 months that partially reverses over longer horizons"; a diversified portfolio earns substantial abnormal returns and performs best in extreme markets.
- **Relevance:** **Medium.** Basis for B16 (12-month TSMOM on EUR/USD, daily hold). Evidence is portfolio-level; single-pair power is low.
- **Caveats:** lookback and holding period of the main strategy not read (abstract only).
- **Status:** VERIFIED (abstract)

### Dao, McGroarty & Urquhart (2016): A calendar effect: weekend overreaction (and subsequent reversal) in spot FX rates
- **Venue:** Journal of Multinational Financial Management 37-38, 158-167. DOI [10.1016/j.mulfin.2016.11.001](https://doi.org/10.1016/j.mulfin.2016.11.001). [RePEc record](https://econpapers.repec.org/RePEc:eee:mulfin:v:37-38:y:2016:i::p:158-167), [Southampton record](https://eprints.soton.ac.uk/402301), [NTU record](https://irep.ntu.ac.uk/id/eprint/35555)
- **Finding (abstract, opened 2026-11-09 R036):** in spot FX for 8 major and 9 emerging currencies, "after a large price difference between Friday close and subsequent Monday open, most markets are likely to reverse" over multiple horizons in the following week; a reversal strategy is reported robust to transaction costs and interest rates and profitable out of sample.
- **Relevance:** **Medium.** Basis for B17 (weekend-gap reversal on EUR/USD). A spot-FX, price-data-only test.
- **Caveats:** abstract only. Data period, currency list, the "large" gap threshold and the holding horizons were not on the pages opened (UNVERIFIED); the post-print PDF was not read. Reading record (centaur.reading.ac.uk/79172) returned a bot-protection page.
- **Status:** VERIFIED (abstract)

### Rentzler, Tandon & Yu (2006): Intraday price-reversal patterns in the currency futures market: the impact of the introduction of GLOBEX and the euro
- **Venue:** Journal of Futures Markets 26(11), 1089-1130. DOI [10.1002/fut.20226](https://doi.org/10.1002/fut.20226). [RePEc record](https://ideas.repec.org/a/wly/jfutmk/v26y2006i11p1089-1130.html), [Montclair record](https://researchwith.montclair.edu/en/publications/intraday-price-reversal-patterns-in-the-currency-futures-market-t/)
- **Finding (abstract, opened 2026-11-09 R036):** in seven CME currency futures, 1988-2003, "Significant intraday price-reversal patterns are observed in five of the seven currency futures contracts" after large 1-day returns and opening gaps; GLOBEX reduced pricing errors; after the euro's introduction patterns (mostly reversals) were significant in most contracts.
- **Relevance:** **Low to medium.** Basis for B18 (next-session reversal after a large daily move on spot EUR/USD). Old futures data; the effect may have been arbitraged away (Neely, Weller & Ulrich 2009).
- **Caveats:** abstract only; "large" threshold and intraday horizon not on the pages opened (UNVERIFIED).
- **Status:** VERIFIED (abstract)

---

### Krohn, Mueller & Whelan (2018 draft, AEA 2019 preliminary): FX premia around the clock
- **Venue:** AEA 2019 annual meeting preliminary paper ("please do not cite or circulate without permission"; version December 2018). [AEA page](https://topcat.aeaweb.org/conference/2019/preliminary/paper/QQ73KSH8). Earlier draft of the line of work published as Krohn, Mueller & Whelan (2024, JF), listed above.
- **Finding (opened 2026-11-09 R041, abstract and opening sections read verbatim):** splitting G10 close-to-close returns into U.S. hours (8:00 a.m.-5:00 p.m. EST) and overnight, "positive average returns for going long foreign currencies are almost entirely generated during U.S. main trading hours"; EUR, GBP and CHF "strongly increase in value against the U.S. dollar between 8:00 a.m. and 5:00 p.m."; the pattern holds on macro-announcement and non-announcement days. Sample January 1994-December 2017, 5-minute spot quotes, nine currencies vs USD.
- **Relevance:** **Medium.** Same mechanism family as B14/E017 (val WEAK) and E010. Basis, with the 2024 paper, for B19/B20 (vol-state conditioning).
- **Caveats:** EUR/USD table values (intraday +7.80% p.a., overnight -7.52% p.a.) were read only through a model summary of the truncated PDF: **UNVERIFIED**. The fixings working paper ([AEA 2020 page](https://topcat.aeaweb.org/conference/2020/preliminary/paper/2dedYfDH), opened 2026-11-09 R041) states verbatim that the USD "systematically appreciates against all currencies ahead of the three major currency fixes"; its report that the reversal is larger in high-volatility and high-spread states (Table 5) and its window returns (EUR pre-ECB 2:00-8:15 a.m. ET, post-London 11:00 a.m.-5:00 p.m. ET) were read only through a model summary: **UNVERIFIED**.
- **Status:** VERIFIED (abstract)

### Kostakis, McBride, Sarno & Wang (2025, SSRN 5781462): Large moves in the foreign exchange market
- **Venue:** working paper; [Cambridge CEAM project page](https://www.jbs.cam.ac.uk/centres/ceam/research/the-cambridge-foreign-exchange-initiative/fx-initiative-research/large-moves-in-the-foreign-exchange-market/) opened 2026-11-09 R041 (the SSRN abstract itself was not opened).
- **Finding (project page):** "three-sigma" moves in 6 major pairs incl. EUR/USD (CME options and spot, 2006-2024) are rare but carry a disproportionate share of risk; an inverted short-over-long implied-volatility term structure warns that "markets expect a big move in the exchange rate soon, although not necessarily whether it will be up or down".
- **Relevance:** **Low** for direction (the signal is about size, not sign) and it needs options data we do not hold. Logged only.
- **Status:** VERIFIED (project page; paper not read)

### Evans & Lyons (2008): How is macro news transmitted to exchange rates?
- **Venue:** Journal of Financial Economics 88(1), 26-50. [RePEc record](https://econpapers.repec.org/RePEc:eee:jfinec:v:88:y:2008:i:1:p:26-50) (opened 2026-11-09 R050). NBER [w9433](https://www.nber.org/papers/w9433) (listed on the RePEc page, not opened). DOI not shown on the page opened: UNVERIFIED.
- **Finding (abstract, opened 2026-11-09 R050):** "This paper shows that the arrival of macro news can account for more than 30% of daily price variance"; news affects prices directly and indirectly through order flow, and about two-thirds of the total news effect on DM/$ is transmitted via order flow (paraphrase of the abstract).
- **Relevance:** **Medium.** Mechanism for B21: if part of the news effect arrives through order flow that is spread over time, a large move right after the 08:30 NY release window may continue. The paper does not state a tradable post-announcement drift; that is our hypothesis.
- **Caveats:** abstract only; DM/$ interdealer data from the 1990s; horizon of the order-flow transmission not on the page opened (UNVERIFIED).
- **Status:** VERIFIED (abstract)

### Love & Payne (2008): Macroeconomic news, order flows, and exchange rates
- **Venue:** Journal of Financial and Quantitative Analysis 43(2), 467-488. [RePEc record](https://econpapers.repec.org/RePEc:cup:jfinqa:v:43:y:2008:i:02:p:467-488_00) (opened 2026-11-09 R050); [Cambridge article link](https://www.cambridge.org/core/product/identifier/S0022109000003598/type/journal_article) (listed on the RePEc page, not opened).
- **Finding (abstract, opened 2026-11-09 R050):** using transaction-level FX prices and trades around scheduled macro announcements, even public information is partly incorporated through order flow: "approximately one third of price-relevant information is incorporated via the trading process."
- **Relevance:** **Medium.** Second mechanism source for B21 (post-release continuation). Currency pairs and the time scale of the order-flow effect not on the page opened (UNVERIFIED).
- **Status:** VERIFIED (abstract)

### Caporale & Plastun (2019 working paper): Price overreactions in the Forex and trading strategies
- **Venue:** Brunel University London, Economics and Finance Working Paper No. 19-09, March 2019 (not a journal version; none mentioned). [PDF](https://www.brunel.ac.uk/economics-finance-and-accounting/research/pdf/1909-Mar-GMC-Overreactions-and-trading-strategies.pdf) (opened 2026-11-09 R055, first ~40k characters read verbatim). DOI: none shown.
- **Finding (opened 2026-11-09 R055):** EURUSD, USDJPY, USDCAD, AUDUSD, EURJPY, daily and hourly MetaQuotes data 2008-2018. Overreaction days defined by a "dynamic trigger": daily open-to-close return beyond the average plus k = 2 standard deviations of daily returns over a period n (n not stated; formulas garbled in the text). Abstract: "prices tend to change in the direction of the overreaction during the overreaction day, but move in the opposite direction on the following day." EURUSD tables: overreaction becomes identifiable at 19:00 (positive days) / 17:00 (negative days) data-clock time; next-day contrarian move from the start of the day to the "start of European session" (09:00 / 08:00 data-clock). Strategy 1 (follow the overreaction from the identification hour to day end), EURUSD: positive 67 trades, 70% hit, t 5.87; negative 79 trades, 86% hit, t 8.98. Strategy 2 (fade next day to European session start): positive t 2.45, negative t 1.23 (failed). No transaction costs.
- **Relevance:** **Medium.** States a tradable horizon in spot FX (lesson R052). Basis for B23 (intraday continuation on overreaction days) and B24 (next-morning fade, val only).
- **Caveats:** working paper, no costs; time zone of the data clock not stated (UNVERIFIED; MetaQuotes servers commonly run GMT+2/+3 with the day rolling at 17:00 NY, so 19:00 data-clock is about 12:00 NY: our assumption, UNVERIFIED); whether the trigger is observable in real time at the identification hour is not discussed (the full-day open-to-close return is not known at 19:00); 2008-2018 overlaps our dev block.
- **Status:** VERIFIED (working paper text, partial)

### Wiśniewska (2014): EURUSD intraday price reversal
- **Venue:** Folia Oeconomica Stetinensia 14(2), 152-162. [CEEOL record](https://ceeol.com/search/article-detail?id=525800) (opened 2026-11-09 R055). DOI not shown.
- **Finding (abstract):** "The study reveals that the mean reversion is present in the intraday EURUSD" (1-minute data; ADF rejects a unit root in deviations from a moving mean). No numbers, horizon or sample period on the page.
- **Relevance:** **Low.** Too vague to pre-register a test from; not used.
- **Status:** VERIFIED (abstract)

### Not used this pass (opened 2026-11-09 R055)
- Quantpedia blog, "Uncovering the Pre-ECB Drift and Its Trading Strategy Applications" (22 Apr 2025, [link](https://quantpedia.com/uncovering-the-pre-ecb-drift-and-its-trading-strategy-applications/)): European equity indices drift up the day before ECB press conferences; equities, not FX; in-house, not peer reviewed; no underlying paper linked. A EUR/USD analogue would be loose and needs an ECB meeting-date calendar: not added.
- Rif & Utz (2021), QREF 81, 123-133, DOI 10.1016/j.qref.2021.05.004 ([RePEc](https://econpapers.repec.org/RePEc:eee:quaeco:v:81:y:2021:i:c:p:123-133)): one-minute reversals in Nasdaq-100 stocks; not FX, horizon below our bar granularity: not added.

### Ito & Yamada (2017): Puzzles in the Tokyo fixing in the forex market: order imbalances and bank pricing
- **Venue:** Journal of International Economics 109, 214-234, DOI 10.1016/j.jinteco.2017.09.005 ([RePEc](https://ideas.repec.org/a/eee/inecon/v109y2017icp214-234.html), opened 2026-11-10 R060). Working paper: NBER WP 22820, DOI 10.3386/w22820 ([NBER](https://www.nber.org/papers/w22820), opened R060).
- **Finding (abstracts):** banks announce the Tokyo fixing rate from interbank transactions at 9:55 a.m.; "spikes in prices at the fixing time occur despite a high level of liquidity"; order flow before the fixing is biased toward the dollar, giving a predictable price pattern; bank fixing rates are biased toward dollar appreciation; "The calendar effects also matter for determination of the fixing rate and the price fluctuation around fixing time." USD/JPY.
- **Not read:** full text (NBER PDF fetch not permitted this run). The gotobi-day definition, sample period and any magnitudes are UNVERIFIED.
- **Relevance:** **Medium.** Basis for B25/B26 (gotobi subset of the E011 Tokyo-fix test); EUR/USD is a loose transfer via the USD leg.
- **Status:** VERIFIED (abstract)

### Popović & Đurović (2014): Intraweek and intraday trade anomalies: evidence from FOREX market
- **Venue:** Applied Economics 46(32), 3968-3979, DOI 10.1080/00036846.2014.948676 ([RePEc](https://ideas.repec.org/a/taf/applec/v46y2014i32p3968-3979.html), opened R060).
- **Finding (abstract):** hourly EUR/USD, Swiss FOREX market, 1 Jan 2004 - 11 Jan 2014; day-by-hour anomalies present; best opportunity on Fridays buying EUR at 00:00 and selling at 03:00. Time zone, magnitudes, t-stats not on the page (UNVERIFIED).
- **Relevance:** **Low.** Dev already scanned by E009 (weekday x NY hour) without support; not added (backlog refill note R060).
- **Status:** VERIFIED (abstract)

### Zheng (2023, job market paper): Dividend flows and the foreign exchange rate
- **Venue:** University of Chicago Booth JMP, Nov 2023 ([PDF](https://socialsciences.uchicago.edu/sites/default/files/2023-11/JMP_Zheng_2.pdf), opened R060; introduction read).
- **Finding:** "upon and after its large dividend payment, the local currency depreciates against USD"; G10, Jan 2001 - Jun 2023; "around 4.70 basis points" two days after the payment date. Month-end is treated as a confound only.
- **Relevance:** **Low** for now: needs a dividend-payment calendar not in the repo. Not added.
- **Status:** VERIFIED (introduction)

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

**Added 2026-11-10 (R065 refill pass).**

### Krohn, Mueller & Whelan (2021 SWP version): window definitions (addendum to the 2024 JF entry above)
- **Source:** [Bank of Canada SWP 2021-48](https://www.bankofcanada.ca/wp-content/uploads/2021/10/swp2021-48.pdf), opened R065; first ~40k characters read verbatim, rest via model summary.
- **Verbatim:** windows in ET: pre-Tokyo 5:00 p.m.-8:55 p.m.; post-Tokyo 8:55 p.m.-2:00 a.m.; pre-ECB 2:00 a.m.-8:15 a.m.; ECB to London 8:15 a.m.-11:00 a.m.; post-London 11:00 a.m.-5:00 p.m. Sample 1999-2019, 5-minute Refinitiv mid-quotes, nine currencies vs USD incl. EUR. "Dealers hedge this demand pre-fix, driving intraday reversals." Results "are not driven by day of the week or month of the year effects".
- **UNVERIFIED (summary only):** Table I annualized EUR values (pre-Tokyo -4.54, post-Tokyo +5.89, pre-ECB -8.87, post-London +6.87).
- **Relevance:** basis for B27 (post-Tokyo window, val only).

### Neuhierl & Weber (2017 working paper): Monetary momentum
- **Venue:** working paper ([Chicago Booth page](https://www.chicagobooth.edu/research/fama-miller/finance-research/working-papers/2017/monetary-momentum), opened R065; [SSRN 3030126](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3030126) not opened). No journal on the page.
- **Finding (abstract):** stock returns drift ahead of and after monetary policy surprises; the drift is also present in "the US-dollar exchange rate and US treasuries". No FX magnitudes on the page.
- **Relevance:** **Low** here: the signal needs a policy-surprise measure (fed funds futures) we do not have, and FOMC events are too rare for our dev/val split (lesson E014). Not added.
- **Status:** VERIFIED (abstract page)

### Kumar (2015): Turn-of-month effect in the Indian currency market
- **Venue:** International Journal of Managerial Finance 11(2), 232-243, DOI 10.1108/IJMF-05-2014-0068 ([RePEc](https://ideas.repec.org/a/eme/ijmfpp/v11y2015i2p232-243.html), opened R065).
- **Finding (abstract):** 1999-2014; "USD and JPY exhibit turn-of-month effect" vs INR; post-2008 the effect "vanishes for all the currencies except for USD". No magnitudes.
- **Relevance:** **Low** (INR pairs; not EUR/USD). Not added.
- **Status:** VERIFIED (abstract)

### Kumar (2018): On the disappearance of calendar anomalies: have the currency markets become efficient?
- **Venue:** Studies in Economics and Finance 35(3), 441-456, DOI 10.1108/SEF-08-2015-0192 ([EconPapers](https://econpapers.repec.org/RePEc:eme:sefpps:sef-08-2015-0192), opened R065).
- **Finding (abstract):** 20 USD pairs, 1995-2014; returns higher (lower) in January (TOM days), but the anomalies "seem to have disappeared for almost all currencies during 2005 to 2014".
- **Relevance:** **Low**; prior against calendar-anomaly tests in our 2015+ sample. Not added.
- **Status:** VERIFIED (abstract)

### Ranaldo & Santucci de Magistris (2022): Liquidity in the global currency market
- **Venue:** Journal of Financial Economics 146, 859-883, DOI 10.1016/j.jfineco.2022.09.004 ([accepted PDF, LUISS IRIS](https://iris.luiss.it/bitstream/11385/221438/1/JFE2022.pdf), opened R065; first ~40k characters verbatim).
- **Finding:** CLS hourly volume 2011-2021, 29 pairs; price impact is higher "outside London hours" and on US bank holidays. No return-predictability results.
- **Relevance:** **Methodology/costs.** Supports keeping entries out of thin hours (lesson R059). Not a signal source.
- **Status:** VERIFIED (text, partial)

### Evans & Speight (2006 working paper): Dynamic news effects in high frequency euro exchange rate returns and volatility
- **Venue:** Cardiff Working Papers in Accounting and Finance A2006/05 ([PDF](https://orca.cardiff.ac.uk/77683/1/a2006_4.pdf), opened R065). Not peer reviewed as shown.
- **Finding (verbatim):** EUR-USD 5-minute, 2002-2003: the reaction to US news "occurs within the first five minutes of the release with very little reaction in the following fifteen minutes".
- **Relevance:** **Low**; consistent with E026 (post-08:30 continuation NONE). Not added.
- **Status:** VERIFIED (text, partial)

**Added 2026-11-10 (R068 refill pass).**

### Cespa, Gargano, Riddiough & Sarno (RFS, "forthcoming" as of 2021): Foreign exchange volume
- **Venue:** Review of Financial Studies (volume, issue, pages and DOI **UNVERIFIED**; the paper itself was not opened). Source opened R068:
  [Cambridge Judge Business School insight, 9 Aug 2021](https://www.jbs.cam.ac.uk/insight/2021/voluminous-breakthrough/) (news summary of the paper).
- **Finding (from that page, quoted):** CLS settlement volume, "31 currency pairs over six years"; daily returns depend on the
  interaction of the previous day's return and "unexpected volume (deviation of volume from a 21-day moving average)". When volume is
  "abnormally low" there is "a return reversal over the following day"; the reversal "weakens and moves toward a next-day continuation"
  when volume is particularly high. Regression design (time-series vs cross-sectional), coefficients and sample dates: not stated.
- **Relevance:** **Medium.** New predictor for this repo (volume has never been used in an experiment). Our volume field is Dukascopy's
  single-venue quote volume, not CLS traded volume: a proxy only. Spawned B28/B29 (R068).
- **Status:** VERIFIED (secondary summary only); paper text UNVERIFIED.

### Borisenko & Pozdeev (2017 working paper): Monetary policy and currency returns: the foresight saga
- **Venue:** working paper, "This version: July 2017" ([PDF, AUT ACFR conference](https://acfr.aut.ac.nz/__data/assets/pdf_file/0011/105500/90345-Borisenko-and-Pozdeev,-Monetary-Policy-and-Currency-Returns-the-Foresight-Saga.pdf), opened R068; first ~40k characters verbatim, rest via summary).
- **Finding (verbatim abstract):** "Currencies tend to depreciate by 0.7 percent over ten days before policy rate cuts and appreciate by
  0.5 percent before policy rate increases"; the drift "does not appear before the announcements at which no policy rate change was
  implemented"; the trade needs the OIS-implied direction about twelve days ahead.
- **Relevance:** **Low for this repo.** Needs OIS expectations (not in repo; using realised decisions is look-ahead) and has very few
  EUR/USD-relevant rate changes on dev (ECB 2015-2020: almost none; Fed ~9 hikes, ~5 scheduled cuts). Not added (backlog note R068).
- **Status:** VERIFIED (text, partial)

### Not used this pass (opened 2026-11-10 R068)
- Stauskas & Sucarrat (2025), J. Financial Econometrics 23(3) nbaf013 (mirror page opened): zero-return periodicity, no direction results.
- Erdemlioglu, Laurent & Neely (2012), St. Louis Fed WP 2012-008A ([PDF](https://files.stlouisfed.org/files/htdocs/wp/2012/2012-008.pdf)): volatility periodicity survey, no return-direction results.

### Melvin & Prins (2015): Equity hedging and exchange rates at the London 4p.m. fix
- **Source:** Journal of Financial Markets 22, 50-72, DOI 10.1016/j.finmar.2014.11.001. Abstract opened 2026-11-10 R071 on IDEAS
  (https://ideas.repec.org/a/eee/finmar/v22y2015icp50-72.html). Full text (ScienceDirect) and ECB 2013 workshop slides not opened.
- **Finding (abstract, verbatim):** "equity market appreciation over the month can be used to predict currency depreciation before the
  end-of-month fix, providing evidence that hedging activity plays a role in exchange rate determination."
- **UNVERIFIED:** exact signal (indices, relative vs absolute), pre-fix window, currencies, EUR/USD magnitude.
- **Relevance:** Medium. Basis for B30/B31 (month-end, ~12 events/yr: low power).

### Marsh, Panagiotou & Payne (2017 preliminary WP): The WMR Fix and its Impact on Currency Markets
- **Source:** Norges Bank PDF (https://www.norges-bank.no/contentassets/619c8b75e1ed4ba691e8ad6a006855e6/39-panagiotou---the-wmr-fix-and-its-impact-on-currency-markets-.pdf),
  opened R071, first ~40% read verbatim.
- **Finding:** GBP/USD, AUD/USD, NZD/USD, 2010-2013; inter-dealer order flow "completely uninformative for spot returns at the Fix
  window"; small reversal in the one minute after the fix. Describes Melvin-Prins as a negative effect of relative equity outperformance
  on the currency before the last fix of the month (secondary).
- **Relevance:** Low for direct trading (no EUR/USD, one-minute horizon); supporting description for B30.

### Krohn, Mueller & Whelan (2024 WP): Uncovered Interest Parity in High Frequency
- **Source:** first version November 2024, Cambridge JBS PDF
  (https://jbs.cam.ac.uk/wp-content/uploads/2024/11/uncovered-interest-parity-in-high-frequency.pdf), opened 2026-11-10 R074; first
  ~40% read verbatim, rest model-summarised (UNVERIFIED).
- **Data (verbatim):** nine G9 currencies vs USD incl. EUR, Refinitiv ticks resampled to 5 minutes, 1999-2023; overnight = 17:00 ET t-1
  -> 7:00 ET t, intraday = 7:00 -> 17:00 ET (robust to 8:00 ET start).
- **Finding (abstract, verbatim):** the Fama slope "switches from a positive value of 1.32 ... during the overnight hours, to -1.28
  during the intraday period"; carry returns "are almost exclusively earned during the day"; over 60% of carry excess returns are
  earned on FOMC/macro announcement days (17% of the sample).
- **UNVERIFIED (summary only):** EUR mean spot change overnight -1.71 bp, intraday +2.03 bp; dollar portfolio overnight -1.19 bp
  (t 2.95), intraday +1.59 bp (t 3.28).
- **Relevance:** Medium. Basis for B32/B33 (overnight -> intraday reversal, an FX daily analogue the paper does not test).

### Lou, Polk & Skouras (2026): The Day Destroys the Night, Night Extends the Day
- **Source:** LSE FMG Discussion Paper 961, July 2026 (https://www.fmg.ac.uk/sites/default/files/2026-07/DP961.pdf), opened
  2026-11-10 R074; first ~33% verbatim.
- **Finding (verbatim, US equities, 1993-2023):** intraday returns regressed on past smoothed overnight returns: "the coefficient on
  the former is negative, with a t-statistic of -3.98 and an R2 of 7%"; smoothing is an EWMA of monthly returns (~10-year centre of
  mass). Cites Ranaldo (2009) and Jiang (2019) for clientele-driven diurnal currency patterns (not opened; UNVERIFIED).
- **Relevance:** Low-medium (equities, slow signal). Clientele mechanism behind B33.

### Hau & Rey (2006): Exchange Rates, Equity Prices, and Capital Flows
- **Source:** Review of Financial Studies 19(1), 273-317, DOI 10.1093/rfs/hhj008. Abstract pages opened 2026-11-10 R079:
  https://econpapers.repec.org/RePEc:oup:rfinst:v:19:y:2006:i:1:p:273-317 and NBER WP 9398 https://nber.org/papers/w9398
  (abstract only; full text not opened).
- **Finding (abstract, read via fetch summary with short verbatim fragments):** in an equilibrium with incomplete FX risk trading,
  higher home equity returns relative to foreign returns go with a home-currency depreciation, and net equity inflows into the foreign
  market go with a foreign-currency appreciation; predictions supported at "daily, monthly and quarterly frequencies" for 17 OECD
  countries vs the US, strongest after 1990. These are **contemporaneous correlations**; the abstract mentions no lags or forecasting.
  Any lagged (predictive) effect on EUR/USD is our extension: **UNVERIFIED**.
- **Relevance:** Low-medium. Mechanism behind B35/B36 (portfolio-rebalancing flows that may be spread over days after relative
  equity performance). Sign for EUR/USD: US equities outperform EU equities -> USD depreciates -> EUR/USD up (same sign as B30).

### Camanho, Hau & Rey (2022): Global Portfolio Rebalancing and Exchange Rates
- **Source:** Review of Financial Studies 35(11), 5228-5274, DOI 10.1093/rfs/hhac023; abstract pages opened 2026-11-10 R079:
  https://econpapers.repec.org/RePEc:oup:rfinst:v:35:y:2022:i:11:p:5228-5274. and https://www.nber.org/papers/w24320 (NBER WP 24320).
- **Finding (abstract):** fund-level international equity allocations rebalance after excess foreign returns, more intensely when FX
  volatility is higher; a granular IV approach identifies a "positive currency supply elasticity". The abstract does not state a
  frequency, a sign for EUR/USD or any lag: **UNVERIFIED** for our purposes. (NBER page lists Koijen as a fourth author on the
  published version; RePEc does not. Author list UNVERIFIED.)
- **Relevance:** Low. Supports that rebalancing flows respond to past relative equity returns (the time-series ingredient of B36).

### Klitgaard & Weir (2004): Exchange Rate Changes and Net Positions of Speculators in the Futures Market
- **Source:** FRBNY Economic Policy Review, May 2004, 17-28 (volume 10(1) per URL). Full PDF opened 2026-11-11 R082 via web-fetch
  summary with short verbatim quotes: https://www.newyorkfed.org/medialibrary/media/research/epr/04v10n1/0405klitpdf.pdf
- **Finding:** CFTC COT noncommercial (+ nonreportable) net positions in CME futures, weekly Tuesday-to-Tuesday, 1993-2003, seven
  currencies vs USD. Contemporaneous: ~75% sign agreement (euro 74%), adj. R^2 30-45% (euro .36, 1999-2003). Predictive: none, "position
  data do not help predict exchange rate changes over the following week" (Granger, euro F 0.31, p 0.73).
- **Relevance:** Low. Argues against a COT-positioning -> next-week EUR/USD item (not added, backlog note R082).
- **Status:** VERIFIED (full text via summary)

### Ranaldo (2007 working paper, EFMA 2008 Athens): Segmentation and Time-of-Day Patterns in Foreign Exchange Markets
- **Source:** https://www.efmaefm.org/0efmameetings/EFMA%20ANNUAL%20MEETINGS/2008-Athens/papers/376.pdf (dated 2007-10-08; opened
  2026-11-11 R082, first ~40% verbatim). Journal version (Ranaldo 2009, JBF) not opened: UNVERIFIED.
- **Finding (verbatim fragments):** Reuters FXFX indicative quotes, 4-hour returns, EUR/USD 1999-2005; "the US dollar appreciates
  significantly from 8:00 to 12:00 GMT and the euro appreciates significantly from 16:00 to 22:00 GMT"; "On Thursdays, the dollar
  experiences an additional depreciation of 2%-4%" (US hours). Holiday "natural experiment" results seen only in an untrusted
  extraction summary: UNVERIFIED.
- **Relevance:** Low now. Same home-hours mechanism as Breedon-Ranaldo (B14/E017, WEAK on val, line closed).
- **Status:** VERIFIED (partial text)

### Krohn, Vala, Uthemann & Yang (2025): Demand-Driven Risk Premia in Foreign Exchange and Bond Markets
- **Source:** Bank of Canada Staff Working Paper 2025-29, last updated 2025-11-03, DOI [10.34989/swp-2025-29](https://doi.org/10.34989/swp-2025-29),
  [PDF](https://www.bankofcanada.ca/wp-content/uploads/2025/11/swp2025-29.pdf); earlier version Jan 2025
  ([FRBSF PDF](https://www.frbsf.org/wp-content/uploads/Krohn-Paper.pdf), 2002-2018, 944 auctions). Opened 2026-11-11 R085; title page,
  abstract, introduction and data section read verbatim (first ~35%); tables read only via a model summary (UNVERIFIED).
- **Finding (verbatim fragments):** Treasury demand shocks are measured as Treasury futures moves "from 10 minutes before the time of
  the auction (i.e., say at 13:00) until 10 minutes after the auction" (ET); "the U.S. dollar systematically depreciates following
  positive Treasury demand shocks", "approximately 2 basis points" in the window (2004-2024, 1,395 auctions); "U.S. dollar depreciation
  peaks at nearly 20 basis points around 10 days after an auction", "gradually reverting to insignificance after 14 days". Non-auction
  placebo insignificant. EUR coefficient (2.12 bp) summary-only: UNVERIFIED. No trading rule, costs or OOS test.
- **Relevance:** Medium. A published lagged USD response to a scheduled, frequent event -> backlog B40/B41 (EUR/USD window move as the
  shock proxy; Dukascopy US T-Bond CFD minute data only from 2018-12).
- **Status:** VERIFIED (partial text)

### Krohn, Mueller & Whelan (2022 slides): Foreign Exchange Fixings and Returns Around the Clock
- **Source:** BIS-Banca d'Italia-ECB 12th Workshop on Exchange Rates, Basel, 13 Dec 2022,
  [slides](https://www.bis.org/events/221213_bis_bdi_ecb_exchange_rates/mueller.pdf) (opened in full 2026-11-11 R085). Adds to the JF
  2024 entry above (not a replacement).
- **Finding:** EUR vs USD mean returns by fix window, bp, 1999-2019 (ET): pre-Tokyo 17:00-20:55 -1.80, post-Tokyo 20:55-02:00 +2.34,
  pre-ECB 02:00-08:15 -3.52, ECB-London 08:15-11:00 +0.63, post-London 11:00-17:00 +2.73, close-to-close +0.37. "Estimated transaction
  cost-adjusted returns to liquidity provision are positive and significant" (verbatim; liquidity-demander returns are not).
- **Relevance:** Medium, but every window is already seen on dev and val in this repo; only OOS is clean (human decision).
- **Status:** VERIFIED (slides)

### Lee & Wang (2025): Jumps and Post-FOMC Announcement Returns in Currency Markets
- **Source:** Review of Asset Pricing Studies 15(3-4), 247-287, [IDEAS abstract page](https://ideas.repec.org/a/oup/rasset/v15y2025i3-4p247-287..html)
  (opened 2026-11-11 R088; abstract only, full text subscriber-restricted). DOI probably 10.1093/rapstu/raaf003 (handle seen on the
  download link, not confirmed: UNVERIFIED).
- **Finding (verbatim fragments):** post-FOMC currency returns are "mostly realized between 12 and 24 hours after FOMC announcements",
  "cancelling out approximately 65% of positive pre-FOMC announcement drifts"; high-frequency exchange-rate data. Currency set, sample
  period, the sign convention of a "positive" drift and EUR-specific magnitudes not read: UNVERIFIED.
- **Relevance:** Medium. A published *lagged* (12-24 h) USD-event effect -> backlog B43/B44. Events are few (8 a year).
- **Status:** VERIFIED (abstract only)

### Ferraro, Rogoff & Rossi (2012/2015): Can Oil Prices Forecast Exchange Rates?
- **Source:** NBER WP 17998 (April 2012), [PDF](https://www.nber.org/papers/w17998.pdf), opened 2026-11-11 R088, ~45% read verbatim;
  published JIMF 54 (2015) 116-141 ([author PDF](https://crei.cat/wp-content/uploads/2016/07/COPF_pub.pdf), not opened).
- **Finding (verbatim fragments):** "a very short-term relationship at the daily frequency"; it "holds no matter whether we use
  contemporaneous (realized) or lagged oil prices"; "the predictive ability of the lagged realized oil prices is more ephemeral".
  Main pair CAD/USD with WTI spot, daily 1984-12-14 to 2010-11-05; also NOK, ZAR, AUD, CLP. No EUR result. Section 4 (lagged model)
  not read verbatim: its exact lagged results are UNVERIFIED.
- **Relevance:** Low to medium. Lagged daily oil -> FX is published for commodity currencies only; a EUR/USD version is our extension
  -> backlog B45 (WTI CFD minute data from 2011-09 on Dukascopy, covers dev).
- **Status:** VERIFIED (partial text)

### Other sources opened 2026-11-11 R088 (not used for items)
- Chen & Hsu (2019, J. Forecasting 38(7) 699-713, DOI 10.1002/for.2592, [IDEAS abstract](https://ideas.repec.org/a/wly/jforec/v38y2019i7p699-713.html)):
  "stock return differentials have in-sample and out-of-sample predictive power for nominal exchange rates", "1-day-ahead". Already
  tested for EUR/USD as B35/E037 (NONE on dev); not re-added. Full text not read.
- Stavrakeva & Tang (2023, CEPR DP18119, [PDF](https://repec.cepr.org/repec/cpr/ceprdp/DP18119.pdf), ~35% verbatim): "exchange rates
  responding to past rather than contemporaneous news"; EUR/USD has the highest adjusted R2 (59% monthly, 74% quarterly, in-sample).
  Needs macro surprise data (Bloomberg/IGM), not in the repo; not added.
- Bae, Da & Zurita (2024, Management Science 70(3) 1943-1969, DOI 10.1287/mnsc.2023.4778, [PDF](https://academicweb.nd.edu/~zda/forex.pdf)):
  lagged FX returns predict US *stock* returns; not an FX-return predictor; not added.
- Chernov, Dahlquist & Lochstoer (2020, NBER WP 28260) and Filippou, Taylor & Wang (2021, CEPR DP16049): monthly cross-sectional
  currency signals; not single-pair EUR/USD timing; not added.

### Apergis (2014): Can gold prices forecast the Australian dollar movements?
- **Source:** International Review of Economics & Finance 29 (2014) 75-82, DOI 10.1016/j.iref.2013.04.004,
  [EconPapers](https://econpapers.repec.org/RePEc:eee:reveco:v:29:y:2014:i:c:p:75-82) (abstract verbatim), [author manuscript](https://espace.curtin.edu.au/bitstream/handle/20.500.11937/4847/197566_197566.pdf?sequence=2)
  (full text, opened 2026-11-11 R093). Published typeset version not opened.
- **Finding:** "whether gold prices have a reliable out-of-sample relationship" with AUD/USD, "using daily and quarterly data,
  respectively, spanning the period 2000–2012"; "the out-of-sample predictive ability is strong and robust across short- and long-run
  horizons" (verbatim). ECM with 8 lags; manuscript Table 3: lagged gold returns enter the exchange-rate equation with negative
  coefficients (lag 1 -0.328, t -4.34; lags 2-5 negative). Long-run sign reading inconsistent in the text (UNVERIFIED). Out-of-sample:
  RMSE below random walk, no formal test. AUD/USD only; no EUR.
- **Relevance:** Low to medium. Published lagged daily gold -> FX; EUR/USD is our extension -> backlog B46 (XAU/USD minute data from
  2003 on Dukascopy).
- **Status:** VERIFIED (abstract + author manuscript)

### Other sources opened 2026-11-11 R093 (not used for items)
- Basnarkov, Stojkoski, Utkovski & Kocarev (2019, arXiv [1906.10388](https://arxiv.org/abs/1906.10388), Physica A, related DOI
  10.1016/j.physa.2019.122986 not opened; full text): histdata 1-minute bid quotes 2016-2018, 66 pairs; "for most pairs of exchange
  rates lagged effects are absent" (verbatim); significant leads are 1-minute and come from indices/commodities; EUR/USD only as lagger
  of USD/CZK; no costs, "we are still uncertain of the existence of arbitrage" (verbatim). Not added.
- Ranaldo (2007) section 5.2 holidays, now read verbatim (supersedes the UNVERIFIED note in the entry above): German holidays as the
  EU proxy; EUR/USD 36 German-holiday and 54 US-holiday days (1999-2005); EU-hours mean +10.3% (annualised, regular) vs -3.2% on
  German holidays; Table 7 test column has no significance marks. Underpowered on dev (~35 events, lesson R090); not added.
- Krohn, Mueller & Whelan (BoC SWP 2021-48, [PDF](https://www.bankofcanada.ca/wp-content/uploads/2021/10/swp2021-48.pdf), ~35%
  verbatim): "The U.S. dollar systematically appreciates against all currencies ahead of the three major currency fixes" (verbatim);
  same windows as the existing KMW entries; already tested (E007, E010, E011, E022-E025, E030-E032). Not added.

### Xiao, Yin & Zhao (2020): Jumps, News, and Subsequent Return Dynamics: An Intraday Study
- **Source:** The Journal of Financial Research 43(3), 705-731, Fall 2020, DOI 10.1111/jfir.12223,
  [vLex reproduction](https://law-journals-books.vlex.com/vid/jumps-news-and-subsequent-855590156) (abstract + introduction opened
  2026-11-11 R096; jump-test section not read, method UNVERIFIED).
- **Finding:** "No-news jumps are followed by significant return reversals for at least 60 minutes" and "Scheduled-news jumps are
  followed by reversals, whereas unscheduled-news jumps are followed by momentum" (verbatim). 212,439 jumps across 205 US equity-index
  ETFs, 2002-2016; reversal "much stronger than the reversal following a normal 15-minute interval that does not contain jumps"
  (verbatim). Positive news jumps continue; negative jumps reverse more strongly. **Not FX.**
- **Relevance:** Medium-low. Published post-jump reversal over ~60 min; EUR/USD is our extension -> backlog B48.
- **Status:** VERIFIED (abstract + introduction)

### Frömmel, Han & Van Gysegem (2015): Further Evidence on Foreign Exchange Jumps and News Announcements
- **Source:** Emerging Markets Finance and Trade 51(4), 774-787, DOI 10.1080/1540496X.2015.1046348,
  [IDEAS](https://ideas.repec.org/a/mes/emfitr/v51y2015i4p774-787.html) (abstract opened 2026-11-11 R096; full text paywalled).
- **Finding:** "the postjump reversal patterns suggest that the realized jumps are mostly information based, whether they are
  obviously linked with news or not"; "nearly half of the significant jumps are explained by scheduled and unscheduled news releases"
  (verbatim). Bipower-variation jump detection. HUF/EUR only; horizon and magnitudes UNVERIFIED (abstract only).
- **Relevance:** Low-medium. FX evidence of post-jump reversal patterns (in an EM cross) -> supports B48 prior only weakly.
- **Status:** VERIFIED (abstract only)

### Erdemlioglu, Laurent & Neely (2012): Econometric Modeling of Exchange Rate Volatility and Jumps
- **Source:** FRB St. Louis WP 2012-008A, [PDF](https://files.stlouisfed.org/files/htdocs/wp/2012/2012-008.pdf) (opened 2026-11-11
  R096; the later part read only via a fetch summary, marked below).
- **Finding:** handbook chapter, "reviews the rapid advances in foreign exchange volatility modeling" (verbatim). Uses 5-minute Olsen
  mid-quotes 1995-2009; Lee-Mykland (2008) and Lee-Hannig tests; for EUR/USD LM flags 2,105 jumps (0.20% of 5-min returns) at
  alpha 0.0001 (fetch summary, not verbatim: UNVERIFIED). No post-jump return analysis.
- **Relevance:** Method only (jump test on 5-min EUR/USD and the expected jump frequency) for B48.
- **Status:** VERIFIED (document opened; jump counts UNVERIFIED)

### Other sources opened 2026-11-11 R096 (not used for items)
- Kumar (2015), "Turn-of-month effect in the Indian currency market", IJMF 11(2), 232-243, DOI 10.1108/IJMF-05-2014-0068,
  [IDEAS](https://ideas.repec.org/a/eme/ijmfpp/v11y2015i2p232-243.html) (abstract): "the returns in turn-of-month trading days are
  significantly lower than the returns during non-turn-of-month trading days" (verbatim) for USD-INR and JPY-INR, 1999-2014; post-2008
  "this effect vanishes for all the currencies except for USD" (verbatim). INR pairs only; window days not in the abstract. Not added:
  one event per month (~72 dev events) with a multi-day hold is far below the power floor (lesson R090), and month-end windows were
  already tested (E034).
- Ştefănescu & Dumitriu (2020), MPRA 99365, [PDF](https://mpra.ub.uni-muenchen.de/99365/1/MPRA_paper_99365.pdf): turn-of-the-year RON/USD
  depreciation, 90 TOY observations, two-tail p 5.15%; one event per year. Not added.
- Vasileiou (2024), DOI 10.1080/17520843.2021.1976944, [IDEAS](https://ideas.repec.org/a/taf/macfem/v17y2024i1p42-58.html) (USDZAR,
  "non-TOM anomaly" in FX, undescribed) and Aydoğan & Booth (2003), DOI 10.1080/09603100210129457,
  [EconPapers](https://econpapers.repec.org/RePEc:taf:apfiec:v:13:y:2003:i:5:p:353-360) (Turkish lira 1986-1994, day-of-week and
  week-of-month effects): not EUR/USD, not added.
- Caporin & Shahzad (2023?, [PDF](https://research.unipd.it/bitstream/11577/3492964/1/2023_CaporinShahzad_Finance.pdf)): jumps and
  next-day realized volatility by time zone, 5-min Kibot quotes 2009-2020, Lee-Mykland after Boudt-Croux-Laurent periodicity filter; no
  post-jump returns. Not added (volatility only; E008 already closed vol timing).

### Jiang, Han & Yin (2019): Can skewness predict currency excess returns?
- **Source:** The North American Journal of Economics and Finance 48, 628-641, DOI 10.1016/j.najef.2018.07.018,
  [EconPapers](https://econpapers.repec.org/RePEc:eee:ecofin:v:48:y:2019:i:c:p:628-641) (abstract page opened 2026-11-11 R099; full
  text paywalled, not opened).
- **Finding (abstract, verbatim):** "The empirical results indicate a positive and significant relationship between skewness and future
  currency excess returns." Paraphrase of the rest of the abstract: portfolio sorts with and without controls (volatility, liquidity,
  global FX volatility risk), currency-level regressions; robust after excluding carry and in emerging, non-Euro and G20 subsamples.
- **UNVERIFIED:** how skewness is measured (realized from intraday data or from daily returns), the formation and holding horizons,
  the currency list (whether EUR/USD is in it) and the sample period. The paper is mainly cross-sectional; a single-pair time-series
  version is our extension.
- **Relevance:** **Low to medium.** Basis for B50 (daily realized skewness -> next-day EUR/USD, sign fixed from the abstract: positive).

### Other sources opened 2026-11-11 R099 (not used for items)
- Gkillas, Gupta & Pierdzioch (2019), "Forecasting (downside and upside) realized exchange-rate volatility: Is there a role for
  realized skewness and kurtosis?", Physica A 532, 121867, DOI 10.1016/j.physa.2019.121867,
  [UP repository](https://repository.up.ac.za/handle/2263/70757?show=full) and
  [IDEAS](https://ideas.repec.org/a/eee/phsmap/v532y2019ics0378437119310957.html) (abstract): "We use intraday data to construct
  measures of realized volatility, realized kurtosis, and realized skewness of returns of six major exchange rates vis-à-vis the
  dollar" (verbatim; EUR included, 2003-07-01 .. 2015-08-28). The target is next-day realized volatility, not returns. Not added
  (E008 closed vol timing). It confirms the realized-skewness construction on EUR/USD intraday data is standard.
- Hoque, Le & Hassan (2020), "Does currency smirk predict foreign exchange return?", IMFI 17(3), 219-230, DOI
  10.21511/imfi.17(3).2020.17, [PDF](https://www.businessperspectives.org/images/pdf/applications/publishing/templates/article/assets/14013/IMFI_2020_03_Hoque.pdf):
  options-implied smirk predicts next-day FX returns (negative slope, EUR included, 2010-2014), "this forecast horizon is limited to
  the next trading day" (verbatim). Not added: no options data in the repo.

### Other sources opened 2026-11-11 R102 (not used for items)
- Li, Sakkas & Urquhart (2022), "Intraday time series momentum: global evidence and links to market characteristics", Journal of
  Financial Markets 57, 100619, DOI 10.1016/j.finmar.2021.100619, [accepted manuscript](https://reading-9.eprints-hosting.org/95566/1/Accepted-Version.pdf)
  (first ~25% verbatim): 16 MSCI developed-market equity indices, 2005-2017; "the US first half-hour return exhibits cross-country
  intraday predictability" (verbatim). FX enters only as a USD conversion; no currency result. Not added (intraday-momentum family
  already tested on EUR/USD: B22/E027, B38/E038).
- Xu, Kozhan & Taylor, "Prospect Theory and Currency Returns" (AEA 2020 preliminary paper,
  [link](https://aeaweb.org/conference/2020/preliminary/paper/RTR7eK6k)): "High prospect theory value currencies significantly
  underperform low prospect theory value currencies" (verbatim); cross-sectional, 15 currencies, monthly rebalancing. Not added
  (cross-sectional, monthly; lessons R081/R101).
- Phylaktis & Yamani (2022), "Foreign currency forecasting: What can stock and bond markets tell us?", Bayes EMG WP-EMG-03-2022
  ([PDF](https://www.bayes.citystgeorges.ac.uk/__data/assets/pdf_file/0005/652523/WP-EMG-03-2022.pdf)): monthly, 28 currencies, lagged
  local equity/bond returns. Not added (B35/E037 family NONE; monthly n too small).
- Raza (2015), "Essays on Foreign Exchange Rate Predictability", Massey University PhD thesis
  ([PDF](https://mro.massey.ac.nz/bitstreams/8d7c87d0-7a19-46ab-b2ad-fa49a8176b48/download)): 52-week-high momentum across 63 currencies
  "is not profitable in the foreign exchange market" (verbatim abstract); cross-sectional. Not added.
- Fetch-permission timeouts (not opened, nothing used from them): Osler FRBNY Staff Report 125 PDF, Osler (2000) FRBNY EPR PDF, IDEAS
  pages for Osler (2003) and Osler (2000). B52 relies only on the Osler (2003) abstract entry VERIFIED 2026-11-07 above.

### Other sources opened 2026-11-11 R105 (not used for items)
- Osler (2002), "Stop-loss orders and price cascades in currency markets", FRBNY Staff Report 150,
  [PDF](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr150.pdf) (opened R105, first ~40% verbatim; adds to the
  R031 abstract entry above, which is not changed). Verbatim: "executed stop-loss buy orders cluster just above round numbers
  (specifically numbers ending in 00 or 50), and executed stop-loss sell orders tend to cluster at rates just below round numbers";
  "'reaching' a number is defined as coming within 0.01 percent of it"; "The rate is defined to have crossed a number if it is above
  (below) the number 15 minutes after rising (falling) to the number"; "dollar-mark moves an average 0.061 percent during the 15
  minutes after crossing a round number, but only 0.054 percent after crossing an arbitrary number". Data: minute Reuters quotes,
  Jan 1996 - Apr 1998, DEM/JPY/GBP vs USD, 9:00-16:00 NY. Nothing on recent highs/lows or previous-day range in the verbatim text.
  Horizon results beyond 15 minutes (dollar-yen table, "at least two hours") seen only in a summary: UNVERIFIED. RePEc lists the 2005
  journal article; the record's link slug suggests JIMF 24(2), 219-241: UNVERIFIED (not stated on the page).
- Kloks, Mattille & Ranaldo (2024-09-26), "Hunting for Dollars",
  [PDF](https://ecb.europa.eu/press/conferences/shared/pdf/20241107_money_markets/Ranaldo_paper.pdf) (ECB money-markets conference
  2024-11-07; ~60% verbatim): non-US banks "substitute dollar borrowing from US repo markets with foreign exchange (FX) swaps at the
  quarter-end" (verbatim); swap volumes and the cross-currency basis rise at quarter-ends. No spot-rate direction, size or timing in the
  verbatim text. Not added (no spot prediction; ~24 dev quarter-ends).


### Cieslak, Morse & Vissing-Jorgensen (2014 draft; JF 2019): Stock returns over the FOMC cycle
- **Venue:** working-paper draft "Current draft: June 25, 2014", [NBER conference PDF](https://conference.nber.org/conf_papers/f74573/f74573.pdf)
  (opened 2026-11-12 R109, ~32% verbatim, rest model summary = UNVERIFIED). Published version: Journal of Finance 74(5), 2201-2248
  ([RePEc record](https://econpapers.repec.org/RePEc:bla:jfinan:v:74:y:2019:i:5:p:2201-2248), seen in search results only, not
  opened: published-version details UNVERIFIED). Stern PDF and BIS link: fetch-permission timeout / agenda page only.
- **Cycle definition (verbatim):** "Date 0 ... is the day of a scheduled FOMC meeting. For two-day meetings, date 0 refers to the second
  day. The graph omits weekends"; week 0 = days -1 to 3; week -1 days -6 to -2; week 1 days 4-8; week 2 days 9-13; week 3 days 14-18;
  week 4 days 19-23; week 5 days 24-28; week 6 days 29-33; days -6 or closer to the next meeting belong to the next cycle.
- **Finding (verbatim):** US equity excess returns "13.6 basis points (bps) higher on days that fall in week 0" and "10.1 bps higher on
  days that fall in week 2, 4, or 6" vs odd weeks (Table 1, 1994-2013); "our fact does not hold up prior to 1994". Non-US equities
  (Table 2): developed ex-US "8.8 bps (t-stat=2.66) higher in weeks 2, 4 and 6 than in odd weeks"; EM "18 bps per day (t-stat=4.75)
  higher during FOMC cycle weeks 2, 4 and 6". Fed funds futures yield volatility "roughly twice as high in even as in odd weeks".
- **FX:** no exchange-rate or dollar result in the verbatim portion. EUR/USD application is our extension (B54).
- **Relevance:** Medium. Gives a calendar-defined, ~1,250-date dev partition with a published risk-asset pattern; no FX evidence, no
  post-2013 evidence in the text read. -> backlog B54/B55.
- **Status:** VERIFIED (draft, partial verbatim, opened 2026-11-12 R109)

### Rosa (2013): The Financial Market Effect of FOMC Minutes
- **Source:** Carlo Rosa, FRBNY Economic Policy Review, December 2013, pp. 67-81 (no DOI shown; RePEc:fip:fednep:00004).
  [PDF](https://www.newyorkfed.org/medialibrary/media/research/epr/2013/0913rosa.pdf) (opened 2026-11-12 R112 via web-fetch, full
  extracted text; chart values not extractable), [RePEc](https://econpapers.repec.org/RePEc:fip:fednep:00004),
  [Fed in Print](https://www.fedinprint.org/item/fednep/19802) (abstract pages).
- **Data (verbatim):** "five-minute intervals of on-the-run two- and ten-year Treasury yields, futures prices on the S&P 500 stock
  index, and the U.S. dollar exchange rate against the euro, Swiss franc, and Japanese yen", "January 2005 to March 2011" (EBS).
- **Timing (verbatim):** minutes "come out three weeks after the FOMC meets", release at "2 p.m. ET".
- **Finding (verbatim):** minutes induce "higher than normal" volatility "especially at the time of the release, and up to roughly one
  hour after the announcement"; "Treasuries ... are the most affected asset class, closely followed by U.S. dollar exchange rates";
  euro volume "four times as large as on nonevent days"; the response "has declined since 2008".
- **Not in the text:** no signed FX return, no tone/surprise measure ("there are no direct measures of market expectations about the
  information contained in the FOMC minutes", verbatim), no post-release drift, continuation or reversal analysis.
- **Relevance:** Low for direction. A volatility-timing fact only; see backlog refill note R112.
- **Status:** VERIFIED (full extracted text, opened 2026-11-12 R112)

### Nower (2024): Losing sleep at the international market: Daylight Saving Time and exchange rates
- **Source:** Michael Nower (Durham University), Economics Letters 241 (2024) 111813, DOI 10.1016/j.econlet.2024.111813 (open access).
  [Repository PDF](https://durham-repository.worktribe.com/OutputFile/2485572) (opened 2026-11-12 R114 via web-fetch, ~95% of the
  extracted text incl. Tables 1-2), [Durham press release](https://www.durham.ac.uk/business/news-and-events/news/2024/october/daylight-saving-time-weakens-the-pound-and-other-currencies)
  (opened, full body). DOI landing page not opened.
- **Data:** FRED daily noon rates, 12 currency areas (10 DST-observing incl. Eurozone and US), "4th January 1971 to 3rd January 2020"
  (verbatim); regressions on weekly averages (log mean noon rate over week t), indicators for weeks after DST start/end in base or
  quoted area, currency-pair fixed effects (currency, currency-year, currency-month-year); SEs clustered by currency.
- **Finding (verbatim):** "When a country starts DST, the value of its currency depreciates, which is reversed when the country exits
  DST." Table 1: DST Start (Base) +0.0156 (n.s.) with currency FE only; -0.00101 (***) with currency-month-year FE incl. US; -0.00134
  (***) excluding the US; "Once this is excluded, the significance increases and the coefficients increase in size" (verbatim).
  With an equity-market control the effect is "approximately 0.1%" (verbatim). Press release: the US dollar "saw minimal negative
  impact" on entering DST.
- **Relevance:** Low for EUR/USD trading. The effect is a ~10 bp level shift in weekly averages relative to month-year fixed effects
  (not a time-series return), insignificant without those FEs, and weakest for the USD. Euro area and US switch on different dates,
  so EUR/USD has ~4 events per year: ~24 on dev (2015-2020). See backlog refill note R114.
- **Status:** VERIFIED (repository PDF text + press release, opened 2026-11-12 R114)

### Anonymous (June 2013), "Information arrival, jumps and cojumps in European financial markets: Evidence using tick by tick data", EFMA 2013 Reading
- **Link:** [PDF](https://www.efmaefm.org/0efmameetings/EFMA%20ANNUAL%20MEETINGS/2013-Reading/papers/Paper_June_2013.pdf) (~52% verbatim; authors not shown in the text)
- **Data:** tick-by-tick level-1 quotes, FESX, FCE, FDAX, 3-month EURIBOR and EUR/USD futures, 26 May 2003 - 31 Jan 2010, 5-min mid-quotes; 23 scheduled US releases.
- **Finding (verbatim):** "Our results suggest that scheduled U.S macroeconomic announcements cause significant jumps on all asset classes." Cross-market links are same-interval cojumps; no lead-lag result.
- **Relevance:** Low. Contemporaneous announcement jumps only; no Bund/Treasury data, no predictive rule. See backlog refill note R118.
- **Status:** VERIFIED (PDF text opened 2026-11-12 R118)

### Bartsch (2019), "Economic policy uncertainty and dollar-pound exchange rate return volatility", JIMF 98
- **Link:** [EconPapers](https://econpapers.repec.org/RePEc:eee:jimfin:v:98:y:2019:i:c:1), DOI 10.1016/j.jimonfin.2019.102067 (abstract only)
- **Finding (verbatim):** "estimate a GARCH model using daily USD/British pound returns"; "EPU contributes to exchange rate volatility much more quickly than monthly data can detect." Volatility only; no direction result.
- **Relevance:** Low (GBP, volatility). See backlog refill note R119.
- **Status:** VERIFIED (abstract opened 2026-11-12 R119)

### Christou, Gupta, Hassapis, Suleman (2018), "The role of economic uncertainty in forecasting exchange rate returns and realized volatility: Evidence from quantile predictive regressions", J. Forecasting 37(7)
- **Link:** [KFUPM record](https://pure.kfupm.edu.sa/en/publications/the-role-of-economic-uncertainty-in-forecasting-exchange-rate-ret/), DOI 10.1002/for.2539 (abstract only)
- **Finding (verbatim):** "EPU is useful for forecasting exchange rate returns and volatility"; 13 countries; frequency, currencies, horizon and magnitudes not shown on the page.
- **Relevance:** Low until the full text is read (frequency likely not daily). Not used. See backlog refill note R119.
- **Status:** VERIFIED abstract only (opened 2026-11-12 R119); design details `UNVERIFIED`

### Fossati, Lu (2025), "Exchange Rate Predictability and Financial Conditions", U. Alberta WP 2025-06
- **Link:** [PDF](https://sites.ualberta.ca/~econwps/2025/wp2025-06.pdf) (~56% verbatim)
- **Data:** weekly (Wednesday) log returns of 9 USD pairs incl. EUR, NFCI predictor, OOS 2000-2021, rolling 520 weeks.
- **Finding (verbatim):** "the NFCI does not provide a strong signal about the direction of exchange rate movements"; "none of the alternative forecasts outperforms the RW benchmark in terms of the OOS point forecasts." Gains are in density forecasts only.
- **Relevance:** Low for a directional rule. See backlog refill note R119.
- **Status:** VERIFIED (PDF opened 2026-11-12 R119)

### Tornell, Yuan (2012), "Speculation and hedging in the currency futures markets: Are they informative to the spot exchange rates", J. Futures Markets 32(2), 122-151
- **Link:** [EconPapers journal record](https://econpapers.repec.org/RePEc:wly:jfutmk:v:32:y:2012:i:2:p:122-151) (metadata only, no abstract);
  [EconPapers WP 09-116 record](https://econpapers.repec.org/RePEc:umb:econwp:09116) (abstract). DOI not shown on either page.
- **Finding (abstract, verbatim fragments):** "the peaks and troughs of net positions are generally useful predictors" of spot rates;
  speculative measures "usually forecast price-continuations in spot rates", hedging measures reversals. Currencies, frequency, horizon,
  peak/trough definition (real-time or ex post), magnitudes and out-of-sample results are not shown.
- **Relevance:** Low until the full text is read. WP PDF (umbc.edu) fetch-permission timeout. Not used. See backlog refill note R120.
- **Status:** VERIFIED abstract only (opened 2026-11-12 R120); design details `UNVERIFIED`

### Filippou, Taylor, Wang (2021), "Media Sentiment and Currency Reversals", CEPR Discussion Paper DP16049
- **Link:** https://repec.cepr.org/repec/cpr/ceprdp/DP16049.pdf (opened 2026-11-12 R121, ~39% verbatim through the start of section 5)
- **Finding (verbatim fragments):** strategy "buys (sells) currencies with low (high) media sentiment"; 1-month formation/holding gives
  "annualized Sharpe ratios of 0.57 and 0.80 for the sample of all 48 countries and developed countries"; time-series version
  "annualized returns of 2.24% ... and 3.39% for developed countries"; "mean reversion occurring between three to five months".
  Daily-frequency results (section 6.5, Table A9) and main-table t-stats not read verbatim, `UNVERIFIED`.
- **Data:** monthly (and daily in 6.5) spot/forward vs USD, 1983-2019, 48 currencies incl. euro area; signal = news-tone score.
- **Relevance:** Low for this repo: needs a news-sentiment dataset not available to the runner. Not used. See backlog refill note R121.
- **Status:** VERIFIED (partial full text)

### Osler (2000), "Support for Resistance: Technical Analysis and Intraday Exchange Rates", FRBNY Economic Policy Review 6(2)
- **Link:** [HTML/PDF](https://www.newyorkfed.org/medialibrary/media/research/epr/00v06n2/0007osle.html) (opened 2026-11-12 R124, ~64% verbatim; rest summary-only, not used)
- **Data:** USD/DEM, USD/JPY, USD/GBP Reuters indicative quotes, 1-minute, 09:00-16:00 NY, Jan 1996 - Mar 1998; S/R levels published daily by six firms.
- **Finding (verbatim):** hit = within 0.01% of a level; bounce if price is back on the near side 15 minutes later; published levels bounced 60.8% vs 56.2% for 10,000 sets of arbitrary levels; "predictive power ... appeared to last at least five business days"; >70% of levels end in 0. Effect weaker in the higher-volatility second half.
- **Relevance:** Background only; levels are firm-published (not available), not mechanical. Not used for any sign. See backlog refill note R124.
- **Status:** VERIFIED (partial full text)

### Johnsson, Frykmer (2019), "Pivot Point Trading in the Foreign Exchange Market - A Test for Market Efficiency", Lund University master's essay (NEKP01)
- **Link:** [record](https://lup.lub.lu.se/student-papers/record/8979805), [PDF](https://lup.lub.lu.se/student-papers/record/8979805/file/8979814.pdf) (opened 2026-11-12 R124, ~70% verbatim: abstract, intro, method, data, EUR/USD Tables 2-3; conclusion and GBP/JPY results summary-only, `UNVERIFIED`)
- **Data:** EUR/USD and USD/CHF level-1 tick mid, 2017-06-01 .. 2017-12-29; GBP/JPY 1-minute 2003-2017. Day starts at UTC 00:00; Sunday merged into Monday.
- **Method (verbatim):** P = (H + L + C)/3 of the previous day; S1-S3, R1-R3 (eqs. 2-7); long at support, short at resistance; target/stop = level +- P x X, X in 0.01%-0.25% (0.15% ~ 2-3 h); one trade per level per day; binomial test vs 50%; no transaction costs.
- **Finding (verbatim):** "we find no support for the hypothesis that pivot points reveal useful information in their traditional way"; "the technique can be profitable if it is implemented inversely for two of the pairs". EUR/USD at 0.15%: weighted win 41.4% (5%), R-only 39.0% (5%), R1 38.5% (10%), S1 45.8% (n.s.). No P&L reported.
- **Relevance:** Medium-low (non-peer-reviewed, win rates only, short EUR/USD sample inside our dev block). Basis for B56 (continuation at R1/S1). See backlog B56.
- **Status:** VERIFIED (partial full text)

### de Palacio (2016): Is there a maturity effect on the EUR/USD foreign exchange market?
- **Source:** Banque & Stratégie n° 348 (Revue Banque, ESCP Europe applied research), [page](https://www.revue-banque.fr/archive/there-maturity-effect-eurusd-foreign-exchange-m-NQRB00807), [PDF](https://www.revue-banque.fr/binrepository/0000000000000000000_RB00807_MG108084818.pdf) (opened 2026-11-13 R137, full text via web-fetch)
- **Data/method:** daily EUR/USD spot (Bloomberg) 2003-01-01 .. 2014-12-31; GARCH(1,1) 1-5-day volatility regressed on J = days since last CME futures expiry (0-32).
- **Finding (verbatim):** "the weekly rolling volatility increases when approaching the expiration date of future contracts, which creates an upward or downward trend closer to this date"; "These results are not definitive". J significant only for 4-day (10%) and 5-day (5%) volatility; R2 ~0.06; coefficient units unclear.
- **Relevance:** Low. Volatility only, no return sign; not a basis for a direction test (R137).
- **Status:** VERIFIED (full text)

### Han, Kling & Sell (1999): Foreign exchange futures volatility: day-of-the-week, intraday, and maturity patterns
- **Source:** Journal of Futures Markets 19(6) 665-693, [IDEAS](https://ideas.repec.org/a/wly/jfutmk/v19y1999i6p665-693.html) (opened 2026-11-13 R137, abstract only)
- **Finding:** volatility patterns in DEM/JPY/GBP/CAD futures with days-to-expiry as a control; no directional claim in the abstract.
- **Relevance:** Low (volatility, futures). **Status:** VERIFIED (abstract only)

### Joensuu (2010): Expiration day effects of the EURO STOXX 50 index futures and options
- **Source:** Aalto University MSc thesis, [record](https://epub.lib.aalto.fi/en/ethesis/id/12297) (opened 2026-11-13 R137, abstract only)
- **Finding (verbatim):** "the intraday returns before expiration are significantly higher and the returns after expiration significantly lower on expiration days" (equity index, 2000-2009).
- **Relevance:** None for FX directly (equity analogue only). **Status:** VERIFIED (abstract only)

### Volta & Aste (2022): Causal coupling between European and UK markets triggered by announcements of monetary policy decisions
- **Source:** Royal Society Open Science 9(3); LSE Research Online 114947, [EconPapers](https://econpapers.repec.org/paper/ehllserod/114947.htm) (opened 2026-11-13 R138, abstract only)
- **Finding (verbatim):** "there is a significant information flow between the markets with prevalent direction going from the market where the announcement is made towards the other" (Euro Stoxx 50 / FTSE 100, 1-minute, ECB and BoE decisions).
- **Relevance:** None for FX directly (equities, same-window). **Status:** VERIFIED (abstract only)

### Vanhanen (2024): ECB's Monetary Policy Spillovers to Financial Markets: Evidence from Small Open Economies
- **Source:** Helsinki GSE Discussion Papers 25, [PDF](https://www.helsinkigse.fi/media/pages/discussion-papers/discussion-paper-25/be9c359dc4-1731573877/dp25re.pdf) (opened 2026-11-13 R138, full text)
- **Finding (verbatim):** "The target surprise on euro US dollar rate does not demonstrate statistical significance"; path surprise positive in a same-window validation regression (168 ECB meetings 2006-2022). No post-announcement horizon.
- **Relevance:** Low (same-window reaction, not a predictable drift). **Status:** VERIFIED (full text)

### Herbst (2007): Lunacy in the Stock Market - What is the Evidence?
- **Source:** Journal of Bioeconomics 9(1), 1-18, DOI 10.1007/s10818-007-9016-3, [IDEAS](https://ideas.repec.org/a/kap/jbioec/v9y2007i1p1-18.html) (opened 2026-11-13 R139, abstract only)
- **Finding (verbatim):** "no consistent, predictable lunar influence is found on either daily returns or daily price volatility" (DJIA).
- **Relevance:** None (equities; null result; no FX test). **Status:** VERIFIED (abstract only)

### Worms (2025): Predictability of Monetary Policy Surprises and Euro Area Macroeconomic Dynamics
- **Source:** DNB Working Paper 850, [PDF](https://www.dnb.nl/media/tbkmwen4/working_paper_no-850.pdf) (opened 2026-11-13 R139, ~half verbatim)
- **Finding:** ECB OIS surprises are predictable from pre-dated macro/financial data; EUR/USD appears only as a same-window reaction and impulse responses, no test of predictable EUR/USD returns. Macro surprises Bloomberg-based (proprietary).
- **Relevance:** Low (no EUR/USD return predictability). **Status:** VERIFIED (partial full text)

### Gerdrup, Hallerud & Maffei-Faccioli (2026): Macroeconomic News and Exchange Rate Dynamics
- **Source:** Norges Bank Staff Memo 5/2026, [PDF](https://www.norges-bank.no/contentassets/1da9f16a950d4dba9e5b1f32865cacd5/staff-memo-5-2026-macroeconomic-news.pdf) (opened 2026-11-13 R139, intro verbatim)
- **Finding (verbatim):** "exchange rates adjust sharply at the time of the announcements, with much of the immediate repricing occurring within the first few minutes." No post-announcement drift test; monthly SVAR level responses only.
- **Relevance:** Low (supports no post-release drift; consistent with B12 efficient-market prior). **Status:** VERIFIED (partial full text)

### Danielsson, Luo & Payne (2012): Exchange rate determination and inter-market order flow effects
- **Source:** The European Journal of Finance 18(9), 823-840, DOI 10.1080/1351847X.2011.601655, [IDEAS](https://ideas.repec.org/a/taf/eurjfi/v18y2012i9p823-840.html) (opened 2026-11-13 R140, abstract only); working paper (2011) [PDF](https://www.riskresearch.org/files/DanielssonLuoPayne2012.pdf) (opened R140, ~69% verbatim)
- **Finding (verbatim):** "GBP exchange rates are very strongly influenced by EUR/USD order flow." Cross-pair effects are contemporaneous order flow (Reuters D2000-2, 1999-2000); the one-step-ahead test uses own-pair flow only: "Only at the highest frequencies is the relationship between order flow at t and the one-period price change to t+1 positive and significant."
- **Relevance:** None for a lagged cross-pair EUR/USD return rule (direction runs EUR/USD -> GBP; order-flow data not available). **Status:** VERIFIED (abstract + partial full text)

### Cai & Zhang (year UNVERIFIED): High-Frequency Exchange Rate Forecasting
- **Source:** [Durham repository](https://durham-repository.worktribe.com/OutputFile/1394665) (opened 2026-11-13 R140, ~half verbatim; venue and year not seen)
- **Finding (verbatim):** "Studying three pairs of currencies, we find strong predictability in the high-frequency quote change data" (EUR/USD, GBP/USD, USD/JPY tick quotes, 2010; own-pair next-quote-change direction, seconds horizon). No cross-pair lead-lag.
- **Relevance:** None (tick horizon, below tradable horizon after SPEC 4 costs). **Status:** VERIFIED (partial full text)

### Maier-Paape & Platen (2015): Lead-Lag Relationship using a Stop-and-Reverse-MinMax Process
- **Source:** arXiv preprint 1504.06235, [PDF](https://arxiv.org/pdf/1504.06235) (opened 2026-11-13 R140, full text)
- **Finding:** timing of local extrema on 60-minute candles (FX 2009-2014): GBP-USD and CHF-USD extrema tend to precede EUR-USD extrema by roughly 20-30 minutes (confirmed-extrema table, as extracted). Authors (verbatim): "we cannot view the value ℓ(w) as an absolute value but more as a tendency of the lead or lag"; extrema only known to about +-30 minutes.
- **Relevance:** Low (not peer-reviewed; extrema timing, not lagged returns; resolution below the claimed lag). **Status:** VERIFIED (full text)

### Alanazi (2020): The bullish and the bearish engulfing patterns: beating the forex market or being beaten?
- **Source:** The European Journal of Finance 26(15), 1484-1505, DOI 10.1080/1351847X.2020.1748679, [IDEAS](https://ideas.repec.org/a/taf/eurjfi/v26y2020i15p1484-1505.html) (opened 2026-11-13 R142, abstract only; full text paywalled)
- **Finding (abstract, verbatim):** "we document the significance of profitability of technical analysis in the forex market, particularly for the seven majors." 24 pairs, daily in-sample and 4-hour out-of-sample candles, 2000-2018. Pattern definition, holding horizon, cost treatment and any EUR/USD-specific sign/magnitude: UNVERIFIED (not in abstract).
- **Relevance:** Potential basis for a daily engulfing-pattern test on EUR/USD, but design unverified. **Status:** VERIFIED (abstract only); design UNVERIFIED

### Neely & Weller (2011): Technical Analysis in the Foreign Exchange Market
- **Source:** Federal Reserve Bank of St. Louis WP 2011-001B, [PDF](https://fraser.stlouisfed.org/docs/publications/frbsl_wp/2011-001.pdf) (opened 2026-11-13 R142, ~42% verbatim); survey chapter, Wiley Handbook of Exchange Rates ch. 12
- **Finding (abstract, verbatim):** "simple technical trading rules on dollar exchange rates provided 15 years of positive, risk-adjusted returns" (1970s-80s), returns later extinguished. Filter / MA / channel rule definitions; no verified EUR/USD figure in the part read.
- **Relevance:** Background (consistent with Neely-Weller-Ulrich 2009 decay). **Status:** VERIFIED (partial full text)

### Gupta (2011): Fibonacci Retracements and Self-Fulfilling Prophecy
- **Source:** Macalester College Economics Honors Project 41, [PDF](https://core.ac.uk/download/46721086.pdf) (opened 2026-11-13 R142, ~59% verbatim; not peer-reviewed)
- **Finding:** "bounce" frequency at Fibonacci retracement levels (0.236-0.764) vs other levels, GAIN Capital ticks 2003-2008 (AUD, EUR, CAD, CHF, JPY vs USD), 1/5/15-min data; gross, no trading test. EUR/USD table values garbled in the fetch; conclusion that retracements "cannot meaningfully predict short-term exchange rates" seen only in a model summary (UNVERIFIED verbatim).
- **Relevance:** None (no verified directional result). **Status:** VERIFIED (partial full text)

### Coakley, Marzano & Nankervis (2016): How profitable are FX technical trading rules?
- **Source:** International Review of Financial Analysis (2016), DOI [10.1016/j.irfa.2016.03.010](https://doi.org/10.1016/j.irfa.2016.03.010); accepted manuscript [PDF](https://core.ac.uk/download/74373954.pdf) (opened 2026-11-13 R143, ~73% verbatim; appendix parameter ranges and part of Table 4 model-summarised)
- **Finding:** 113,148 daily rules (MA, channel breakout, trading-range break, filter, Bollinger, RSI, MACD) on 22 USD pairs incl. EUR, 1997-2015, no transaction costs, interest-differential-adjusted. Abstract (verbatim): "Virtually no traditional rule is significant in the 2006-2015 sub-sample". Under Step-SPA, traditional rules are "robustly significant only in a few cases" (MA/filter for HKD, INR). Channel breakout has the lowest share of nominally significant rules (~12% mean; EUR 9.85% before data-snooping control). Best EUR rules (in-sample, Bollinger/RSI/MACD) are best-of-many selections.
- **Relevance:** Low (no data-snooping-robust EUR/USD rule; channel breakout weakest family; no costs). **Status:** VERIFIED (partial full text)

### Hsu & Taylor (2013) / Hsu, Taylor & Wang (2016): large-scale technical-rule tests in FX (secondary summaries only)
- **Source:** CXO Advisory write-ups ([2014](https://www.cxoadvisory.com/technical-trading/comprehensive-long-term-test-of-technical-currency-trading/), [2016](https://www.cxoadvisory.com/technical-trading/updated-comprehensive-long-term-test-of-technical-currency-trading/)) of SSRN 2517125 and SSRN 2765673 (opened 2026-11-13 R143, CXO pages full text; underlying papers not opened: UNVERIFIED)
- **Finding (per CXO):** 21,195 daily rules (incl. 3,000 channel breakout), 30 USD pairs 1971-2015; developed-market predictability "gradually disappears since the early 1990s"; no EUR/USD or channel-specific result reported.
- **Relevance:** Background (decay in developed pairs). **Status:** secondary summary only; papers UNVERIFIED

### Ranaldo & Söderlind (2007): Safe Haven Currencies (abstract only)
- **Source:** SNB Working Paper 2007-17, [landing page](https://www.snb.ch/en/publications/research/working-papers/2007/working_paper_2007_17) (opened 2026-11-13 R144, abstract and metadata only; PDF download blocked by a fetch permission prompt, not circumvented; body UNVERIFIED). Also CEPR DP7249.
- **Finding (abstract, verbatim):** "the (Swiss) franc, euro, Japanese yen and the pound tend to appreciate against the U.S. dollar when (a) S&P has negative returns; (b) U.S. bond prices increase; and (c) when currency markets become more volatile", 1993-2006, "from a few hours to several days". Whether any regression is predictive (lagged) rather than contemporaneous, the EUR/DEM series construction and magnitudes: UNVERIFIED.
- **Relevance:** Background (contemporaneous safe-haven co-movement; no verified lagged equity -> EUR/USD effect). **Status:** abstract only
### Marsh & Miao (2012): High frequency information content in end-user FX order flows
- **Source:** European Journal of Finance 18(9), 865-884, DOI [10.1080/1351847X.2011.601652](https://doi.org/10.1080/1351847X.2011.601652); accepted version [PDF](https://openaccess.city.ac.uk/id/eprint/12154/8/MarshMiao.pdf) (opened 2026-11-13 R144, ~35% verbatim, rest model-summarised and UNVERIFIED)
- **Finding:** one London bank's EUR/USD customer/interbank trades, 25 days Oct-Nov 2005, 1-30 min horizons. Direction tested is FX order flow -> later SPY/DIA returns ("FX flows do appear to have significant power to forecast stock index returns over 1-minute to 30-minute horizons"); lagged stock returns are not used to forecast EUR/USD (footnote 5). In-sample only ("not true forecasts"), no costs.
- **Relevance:** None for us (needs proprietary signed flow; wrong direction; 25-day sample). **Status:** VERIFIED (partial full text)

### Boyarchenko, Larsen & Whelan (2020, rev. 2022): The Overnight Drift
- **Source:** Federal Reserve Bank of New York Staff Report 917, [PDF](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr917.pdf) (opened 2026-11-13 R145; cover and pp. 1-13 plus appendix tables A.1-A.12, A.14-A.15 read verbatim; middle appendix text model-summarised only, UNVERIFIED)
- **Finding:** S&P 500 e-mini futures returns are large and positive around the European open (~2:00-3:00 ET), linked to order imbalance at the preceding US close (dealer inventory risk); selloffs produce larger overnight reversals than rallies. Data are ES futures only; no euro, EUR/USD or FX result found in the pages read.
- **Relevance:** None for a EUR/USD direction rule (equity-only mechanism; dealer-inventory channel not shown for FX). **Status:** VERIFIED (partial full text)

### Goddard, Kita & Wang: Investor Attention and FX Market Volatility
- **Source:** [PDF](https://orca.cardiff.ac.uk/73438/1/Attetion_FX.pdf) (Cardiff ORCA; opened 2026-11-13 R146, ~51% verbatim incl. abstract, data, methods, results 4.1-4.3; rest model-summarised, UNVERIFIED; journal/year not in the text read: UNVERIFIED)
- **Finding (verbatim):** "Investor attention comoves with contemporaneous FX market volatility and predicts subsequent FX market volatility"; Google search volume, weekly, Jan 2004-Sep 2011, seven pairs incl. EUR/USD. Returns enter only as controls; no return-direction prediction.
- **Relevance:** None for a direction rule (volatility only). **Status:** VERIFIED (partial full text)

### Han, Xu & Yin (2018): Does investor attention matter? The attention-return relationships in FX markets
- **Source:** Economic Modelling 68, 644-660, DOI [10.1016/j.econmod.2017.06.015](https://doi.org/10.1016/j.econmod.2017.06.015); [EconPapers abstract](https://econpapers.repec.org/RePEc:eee:ecmode:v:68:y:2018:i:c:p:644-660) (opened 2026-11-13 R146, abstract only; body UNVERIFIED)
- **Finding (abstract, verbatim):** "Lagged investor attention significantly influences currency returns at present, and this effect is short-lived (usually at first lag)"; nonlinear, depends on sign of past returns; nine countries. Frequency, sample, sign, EUR coverage and costs: UNVERIFIED.
- **Relevance:** Background only (abstract-level, no EUR/USD direction or horizon). **Status:** abstract only

### Han, Wu & Yin (2018): Investor attention and currency performance: international evidence
- **Source:** Applied Economics 50(23), 2525-2551, DOI [10.1080/00036846.2017.1403556](https://doi.org/10.1080/00036846.2017.1403556); [EconPapers abstract](https://econpapers.repec.org/RePEc:taf:applec:v:50:y:2018:i:23:p:2525-2551) (opened 2026-11-13 R146, abstract only)
- **Finding (abstract, verbatim):** attention predicts "emerging currency performance in the out-of-sample analysis. By contrast, statistical predictability and economic value do not exist in the currencies from developed markets."
- **Relevance:** Negative evidence for a EUR/USD attention rule. **Status:** abstract only

### Kubitza, Sigaux & Vandeweyer (ECB WP 3017): The implications of CIP deviations for international capital flows
- **Source:** [ECB Working Paper 3017 PDF](https://www.ecb.europa.eu//pub/pdf/scpwps/ecb.wp3017~2c077fb436.en.pdf) (opened 2026-11-13 R147, ~26% verbatim; year not seen in text read, data to 2024Q1)
- **Finding:** cross-currency basis widening leads euro-area investors to cut hedging and USD bond holdings. No spot EUR/USD direction result around tax dates, mid-quarter dates or reserve drains in the text read.
- **Relevance:** Background only (basis/flows, not spot direction). **Status:** partial text

### Abbassi & Bräuning (Boston Fed WP 18-6, revised July 2020): Demand Effects in the FX Forward Market
- **Source:** [Boston Fed WP 18-6 revised PDF](https://www.bostonfed.org/-/media/Documents/Workingpapers/PDF/2018/wp1806-revised.pdf) (opened 2026-11-13 R147, ~29% verbatim)
- **Finding (verbatim):** German banks make "cross-quarter dollar forward sales at higher prices (15 basis points higher) and higher volumes (20 percent higher)" around quarter-ends. Forward premia only; no spot direction.
- **Relevance:** Background only; quarter-end funding line already closed (refill note R138). **Status:** partial text

### DeBruin Martos, Sekkel, Stern & Zhang (2025, Bank of Canada SAN 2025-10): Is anyone surprised? The high-frequency impact of US and domestic macroeconomic data announcements on Canadian asset prices
- **Source:** [Bank of Canada Staff Analytical Note 2025-10 PDF](https://bankofcanada.ca/wp-content/uploads/2025/03/san2025-10.pdf) (opened 2026-11-13 R148, ~95% of text; chart values not read)
- **Data:** CAD/USD spot, BAX futures, GoC bonds, TSX 60 futures; US and Canadian CPI, employment, production, retail sales; Jan 2002 - Dec 2023 excl. Mar-Jun 2020; window 10-15 min before to 20-25 min after each release.
- **Finding (verbatim):** "our analysis focuses on their immediate impact using high-frequency data"; "the CAD/USD exchange rate moves more around domestic macroeconomic announcements than around US ones". No delayed / post-announcement drift test.
- **Relevance:** Background only (same-window reaction, CAD/USD, no EUR/USD, no drift). **Status:** near-full text

### Zheng (2023, University of Chicago job market paper): Dividend Flows and the Foreign Exchange Rate
- **Source:** [JMP_Zheng_1.pdf, version 31 Oct 2023](https://socialsciences.uchicago.edu/sites/default/files/2023-11/JMP_Zheng_1.pdf) and [JMP_Zheng_2.pdf, version 13 Nov 2023](https://socialsciences.uchicago.edu/sites/default/files/2023-11/JMP_Zheng_2.pdf) (both opened 2026-11-13 R149 via web-fetch, ~27-30% verbatim each; rest model-summary only, table coefficients UNVERIFIED)
- **Data:** daily G10 vs USD incl. EUR (euro area aggregated), WM/Refinitiv hourly snapshots at local stock close, Jan 2001 - Jun 2023; dividends from Compustat Global / CRSP (commercial).
- **Finding (verbatim):** "upon and after its large dividend payment, the local currency depreciates against USD"; "Two days after the dividend payment date, the cumulative currency depreciation against USD is around 4.70 basis points"; "Eight days after the dividend payment date, it further depreciates to 6.48 basis points". Announcement-date effects "economically small and statistically insignificant". Strategy (top-5% dividend days, 1-day hold, all G10 pooled): "4.4% return annually before the transaction cost".
- **Relevance:** Published direction for EUR (paying currency depreciates after large payment dates), but (i) the payment-date calendar needs commercial Compustat data the runner cannot download, (ii) the pooled effect (~4.7 bp over 2 days ~ 0.5 pip on EUR/USD) is below the 1-pip bar and roughly the SPEC 4 round-trip cost, and EUR-specific results are UNVERIFIED. Not added (refill note R149). **Status:** partial text

### Zavodny & Ginther (2005, Southern Economic Journal 72(1), 138-151): Does the Beige Book Move Financial Markets?
- **Source:** [GintherSEJ05.pdf](https://ipsr.unit.ku.edu/dginther/Publications/GintherSEJ05.pdf) (opened 2026-11-13 R150 via web-fetch, ~78% verbatim; expectations section, Table 6 and conclusion model-summary only, UNVERIFIED)
- **Data:** 149 Beige Book releases May 1983 - Dec 2001; daily close-to-close changes in US Treasury yields (3m-10y) and CRSP value-weighted US equity index; authors' own -2..2 score of the national summary.
- **Finding (verbatim):** "the Beige Book index is positively associated with changes in most measures of interest rates"; "We do not find a significant relationship between the Beige Book index and stock returns". Same-day effect only; no exchange rate studied; no delayed drift test.
- **Relevance:** Background only (US rates/equities, same-day, needs a hand-scored text index; no FX, no drift). Not added (refill note R150). **Status:** most of text

### Evans (2020, MPRA Paper 102702): Exchange Rates and Liquidity Risk
- **Source:** [MPRA_paper_102702.pdf](https://mpra.ub.uni-muenchen.de/102702/1/MPRA_paper_102702.pdf) (opened 2026-11-13 R151 via web-fetch, ~38% verbatim; rest model-summary only, UNVERIFIED)
- **Data:** Hotspot FX limit order book, 17 USD pairs, 2006-2015, 30-second snapshots aggregated to monthly; liquidity measures depth, spread, trend, volatility.
- **Finding:** cross-sectional monthly portfolio sorts (depth HML ~3.5% p.a., p = 0.076; trend 3.9%, p = 0.018; spread 0.9%, p = 0.401); verbatim rationale "if a reduction in depth is a precursor of a future fall in the price of foreign currency". EUR/USD-specific results are contemporaneous betas only.
- **Relevance:** Background only (cross-section of 17 pairs, monthly, commercial order-book data; no EUR/USD time-series direction test). Not added (refill note R151). **Status:** partly read

### Osler, Mende & Menkhoff (2010, Brandeis working paper, UNVERIFIED venue): Price Discovery in Currency Markets
- **Source:** [Brandeis_WP03.pdf](https://www.brandeis.edu/economics/RePEc/brd/doc/Brandeis_WP03.pdf) (opened 2026-11-13 R151 via web-fetch, ~38% verbatim)
- **Data:** one German bank's complete USD/EUR transaction record, 87 trading days Jul-Nov 2001, transaction time.
- **Finding:** trade-level adverse-selection / spread decomposition models; order-flow -> return links cited from Lyons/Payne, not tested as a later-return predictor in the text read.
- **Relevance:** Background only (trade-level, proprietary dealer data, no direction forecast). Not added (refill note R151). **Status:** partly read

### Aliyev, Aquilina, Rzayev & Zhu (2024, BIS Working Paper 1229): Through stormy seas: how fragile is liquidity across asset classes and time?
- **Source:** [BIS landing page / work1229.pdf](https://www.bis.org/publ/work1229.pdf) (landing page and abstract opened 2026-11-13 R151; PDF body blocked by proxy, 0% of body read, body UNVERIFIED)
- **Finding (abstract level):** distribution of bid-ask spreads for stocks, FX and government bonds over 25 years; no return-direction test described.
- **Relevance:** Background only. Not added (refill note R151). **Status:** abstract only

### Beetsma, Giuliodori, Hanson & de Jong (2018): Cross-border auction cycle effects of sovereign bond issuance in the euro area
- **Source:** Journal of Money, Credit and Banking 50(7), 1401-1440, DOI 10.1111/jmcb.12510
  ([IDEAS](https://ideas.repec.org/a/wly/jmoncb/v50y2018i7p1401-1440.html), [UvA DARE](https://dare.uva.nl/id/e17a86bf-e8f1-4cdc-9685-3e6935b4ec0d));
  opened 2026-11-13 R152, abstract and metadata only (body not read; DARE gives 2017, IDEAS 2018).
- **Finding (abstract):** foreign euro-area debt auctions spill over into domestic secondary-market yield auction cycles; domestic
  cycles stronger in the crisis period, cross-border effects stronger pre-crisis. No exchange-rate result in the abstract.
- **Relevance:** Low. No EUR/USD basis for an auction-day item (R152 refill note).

### Zou (2025, working paper, UNVERIFIED venue): Bond Demand and the Yield-Exchange Rate Nexus: Risk Premium vs. Convenience Yield
- **Source:** Dongchen Zou (Indiana University, Kelley), draft July 2025, no DOI
  ([PDF](https://fbe.unimelb.edu.au/__data/assets/pdf_file/0003/5462940/paper_128.pdf)); opened 2026-11-14 R158, ~26% read verbatim,
  rest only via a fetch summary (summary-only details below are marked UNVERIFIED).
- **Finding (verbatim):** "I focus on 10-year government bond auctions"; "a unit increase in the bid-to-cover ratio appreciates the
  domestic currency by approximately 16 basis points"; "domestic currency begins appreciating on the auction day as the bid-to-cover
  ratio rises". G10 incl. the euro (Bund as euro benchmark, UNVERIFIED); daily, ~2002-2022, window k = -4..+5 days, ~4 bp per 1 SD,
  p < 0.05 (all UNVERIFIED, summary only). Auction data from commercial vendors (UNVERIFIED).
- **Relevance:** Low for us. Signal is the auction *outcome* (bid-to-cover), released at auction time, so a tradable version needs a
  Bund auction-results history (not in repo; download source not verified) and the effect (~4 bp per SD, ~4-5 pips) on roughly
  monthly 10y Bund auctions (~70 dev events, UNVERIFIED count) is below the lesson R090 power floor at a daily horizon. Not added
  (refill note R158). **Status:** partial text

### Hossfeld & Röthig (2015), Bundesbank Discussion Paper 41/2015 (added 2026-11-14 R160)
- "Do speculative traders anticipate or follow USD/EUR exchange rate movements?" ([PDF](https://bundesbank.de/resource/blob/703976/fcd518354ae96703103d929dfea7582e/472B63F073F071307366337C94F8C870/2015-11-30-dkp-41-data.pdf));
  opened 2026-11-14 R160 via a fetch summary (quotes below as relayed; treat numbers as UNVERIFIED until read directly).
- **Finding:** weekly CFTC net positions in EUR futures vs USD/EUR (ECB fixing), 1999-2015; FX changes lead position changes; positions
  do not reliably predict FX once Benjamini-Hochberg/Bonferroni corrections are applied ("the evidence does not support a leading
  indicator role in the other direction").
- **Relevance:** Low. Weekly COT positioning is not a usable EUR/USD direction signal per this paper; no bond lead-lag. **Status:** read (summary)

### Comazzi, Domenech Palacios, Ehrmann, Ferrari Minesso & Mehl (2026), CEPR DP 21606 "ECB exchange rate communication" (added 2026-11-14 R161)
- Read via the VoxEU column ([page](https://cepr.org/voxeu/columns/exchange-rate-communication-practice-evidence-two-decades-ecb-press-conferences));
  paper itself not opened; quotes as relayed by a fetch summary.
- **Finding:** ECB press conferences 2002 - mid-2023, ~100 exchange-rate statements in opening statements plus Q&A references: "little
  evidence that statements expressing a preference for appreciation or depreciation systematically move the euro in the desired
  direction"; effects "fade within days", not significant after about one week; weaker after the crisis / at the lower bound. No pip
  magnitudes in the column; no published list of mention dates/times.
- **Relevance:** Low. Null-ish published result, ~100 events over 21 years (~30 in dev, UNVERIFIED) is below the lesson R090 power floor,
  and no event list is available. **Status:** read (column summary)

### Babiak & Baruník, "Volatility Shocks and Currency Returns", arXiv:2101.09738 v3 (added 2026-11-14 R161)
- [abstract](https://arxiv.org/abs/2101.09738); HTML v3 opened (first part verbatim, rest via summary).
- **Finding:** 20 USD-based currencies incl. euro, daily Bloomberg OTC 1-month implied vols, monthly portfolio sorts: "Currencies that
  transmit more volatility shocks ... earn lower excess returns". Cross-sectional, one-month horizon; plain IVOL / risk-reversal sorts
  reported insignificant (UNVERIFIED figures from summary).
- **Relevance:** Low. Cross-sectional result, not a single-pair time-series signal; Bloomberg implied-vol history not in repo and no free
  source verified. **Status:** partial text

### Hashemi (2025), "Intraday Stock Return Prediction: A Comparative Study of Econometrics and Machine Learning Models" (added 2026-11-14 R162)
- M.Sc. thesis, HEC Montréal, August 2025 (supervisor V. Grégoire); [PDF](https://biblos.hec.ca/biblio/memoires/hashemi_zahrasadat_m2025.pdf)
  opened via web-fetch (cover-p. 12 and appendices/tables verbatim; middle chapters incl. the backtest only via summary, UNVERIFIED).
- **Finding:** US stocks/ETFs (TAQ), predictors from open to 13:00 incl. relative VWAP (log vwap_1pm/open) and morning momentum, target
  13:00 -> close return; Lasso / random-forest out-of-sample R^2 about 0.07-0.21 for returns (Table 1, verbatim); "order-flow measures
  are substantially more predictable than returns". Backtest figures and any VWAP-reversion sign are summary-only and gross of costs.
- **Relevance:** Low. Equity-only, no FX; no verified VWAP-deviation direction result for any currency pair. **Status:** partial text

### Franz (2020), "Central bank information shocks and exchange rates", Deutsche Bundesbank DP 13/2020 (added 2026-11-14 R163)
- [PDF](https://bundesbank.de/resource/blob/828896/2d2e88314163a04e1eb8af798401a1e4/mL/2020-03-20-dkp-13-data.pdf) opened via
  web-fetch (~40% verbatim, rest summary-only; event count and impulse-response magnitudes UNVERIFIED).
- **Finding:** ECB Governing Council meetings 2002-2018, high-frequency 2y Bund / Euro STOXX 50 surprises as proxies, monthly BVAR:
  EUR "appreciates strongest directly on impact following a monetary policy shock", fading to insignificance after about two years;
  "I do not find a significant reaction of the nominal effective EUR exchange rate" to information shocks; EUR-USD the only pair with
  some delayed overshooting.
- **Relevance:** Low. Monthly macro horizon, no intraday or daily post-event EUR/USD drift; surprise series not in repo. **Status:** partial text

### Iyke, Phan & Narayan (2022), "Exchange rate return predictability in times of geopolitical risk", IRFA 81, 102099 (added 2026-11-14 R164)
- [Repository record](https://research.monash.edu/en/publications/exchange-rate-return-predictability-in-times-of-geopolitical-risk/)
  opened via web-fetch (abstract and metadata only); DOI [10.1016/j.irfa.2022.102099](https://doi.org/10.1016/j.irfa.2022.102099) not opened.
- **Finding (abstract):** "geopolitical risk predicts 10 out of 17 (59%) exchange rate returns in in-sample tests"; out-of-sample
  predictability for 88% of currencies; model beats the historical-average benchmark in 11 of 17 currencies.
- **Not on the page (UNVERIFIED):** data frequency, currency list (EUR/USD inclusion), GPR index definition, forecast horizon, sign of
  the effect, costs.
- **Relevance:** Low until full text is read. No verified EUR/USD sign or horizon; GPR series not in repo. **Status:** abstract only

### Filippou, Gozluklu, Nguyen & Viswanath-Natraj (2025 version), "Signal in the Noise: Trump Tweets and the Currency Market", working paper (added 2026-11-14 R165)
- [PDF](https://ganeshvnatraj.netlify.app/pubs/trumpfx/trumpFX-paper.pdf) opened via web-fetch (~37% verbatim, rest model summary);
  version dated 2025-05-03, previously "The Information Content of Trump Tweets and the Currency Market"; journal not stated.
- **Data:** 14 USD pairs incl. EUR (Thomson Reuters Tick History), minute event study aggregated to 30/60-min windows, hourly panel;
  sample 2015-06-16 to 2019-08-20.
- **Finding (abstract, verbatim):** "Informative tweets result in a USD appreciation and a decline in intraday volatility"; about
  0.5 bp vs an equal-weighted basket, cumulative return peaking "within an hour of the tweet". In-sample UUP ETF rule ~2 bp gross within
  1 h, costs ~1.5-1.75 bp "naturally absorb some of this return" (authors' figures, not EUR/USD spot).
- **Relevance:** Low. Effect ~0.05 pips on the basket, far below the 1-pip bar and SPEC 4 costs; needs a tweet timestamp/classification
  series not in repo; sample overlaps dev only partly. **Status:** partial text

### Krohn, Mueller & Whelan (2021), "Foreign Exchange Fixings and Returns Around the Clock", Bank of Canada SWP 2021-48 (re-opened 2026-11-14 R165)
- [PDF](https://www.bankofcanada.ca/wp-content/uploads/2021/10/swp2021-48.pdf) opened via web-fetch (~35% verbatim). Same paper family as
  the KMW entry already in this file (fix reversals, tested E007, E010, E011, E022-E025). New detail read: one-s.d. pre-fix Refinitiv
  Matching order imbalance is followed by "a post-fix reversal of around 2.5 to 3.5 basis points" (AUD/GBP regressions shown; EUR not
  confirmed); "most of the trading profits disappear when transaction costs are incorporated". Order-flow data not in repo.
- **Relevance:** None new (family closed; order flow unavailable). **Status:** partial text

### Zhang (2025), "Interpretable Machine Learning for Macro Alpha: A News Sentiment Case Study", arXiv:2505.16136v1 (added 2026-11-14 R166)
- [arXiv HTML](https://arxiv.org/html/2505.16136v1) opened via web-fetch (full text read); single author, personal capacity, not peer reviewed.
- **Data/design:** GDELT v2 event records (EventCode 100-199, top 100 events/day by num_articles), headlines re-fetched from stored URLs
  and scored for sentiment, plus technical features; daily, Jan 2015 - Apr 2025; target = sign of next-day close-to-close log return
  for EUR/USD, USD/JPY and ZN futures; always long/short; expanding TimeSeriesSplit (5 folds), OOS ~2017 - Apr 2025.
- **Finding (Table 1, authors' figures):** EUR/USD XGBoost CAGR 55.4%, Sharpe 5.87, "Win (%)" 72.7, 1158 trades; logistic baseline
  CAGR 6.6%, Sharpe 0.83, win 53.1%. Costs "0.02% of the traded value per round-trip"; block-bootstrap CIs "not explicitly detailed".
- **Concerns:** Sharpe ~5.9 at ~7% vol is implausible for a daily FX rule; how GDELT/headline timestamps map to the day-t close is not
  explained (headlines fetched later from URLs: look-ahead risk UNVERIFIED either way); signal is a fitted ML model, not a fixed rule.
- **Relevance:** Low. Not reproducible as one pre-registered rule; GDELT event/headline history for 2015-2023 is not in repo and is too
  large for the runner (daily event files plus headline scraping). **Status:** full text

### Istrefi, Odendahl & Sestieri (2025-04-15), "ECB communication and its impact on financial markets", CEMLA 2025 meeting paper (added 2026-11-14 R166)
- [PDF](https://www.cemla.org/actividades/2025/2025-11-xxx-meeting-central-bank-researchers/papers/ECB%20communication%20and%20its%20impact%20on%20financial%20markets.pdf)
  opened via web-fetch (~30% verbatim, rest model summary, untrusted).
- **Data/design:** EA-CED database, 304 Governing Council meetings and ~5,100 inter-meeting communication events, Jan 1999 - Feb 2024;
  47 variables incl. EUR/USD; speeches/interviews use a 90-min window, 15-min medians before vs after; database "publicly available".
- **Finding (verbatim part):** reported impacts are **absolute** (no signed direction); variance model assumes Brownian motion "(without
  drift)"; no post-speech continuation/drift test for FX in the text read. OIS: IMC events before tightening decisions shift the short
  end "in the same direction as the subsequent policy move" (rates, not FX).
- **Relevance:** Low. No signed or delayed EUR/USD direction; the speech tone is known only after the event. **Status:** partial text

### Andrikopoulos, Wang & Zheng (2019), "Is There Still A Weather Anomaly? An Investigation of Stock and Foreign Exchange Markets", Finance Research Letters 30, 51-59, DOI 10.1016/j.frl.2019.03.026 (added 2026-11-14 R167)
- [Accepted manuscript](https://hull-repository.worktribe.com/OutputFile/1571292) opened via web-fetch (essentially full text; some table
  cells garbled); [record](https://hull-repository.worktribe.com/output/1562223) opened for metadata.
- **Data/design:** daily, 02/01/2002 - 29/06/2018 (N 4,077); seven weather variables (wind, temperatures, humidity, precipitation,
  temperature range dummy); New York weather for USD pairs (incl. EUR/USD), London for GBP pairs; OLS (Newey-West) and logit.
- **Finding:** "the weather has no effect during 2002–2018, suggesting that any effect may have dissipated after discovery"; "only nine
  out of 294 ... coefficients are significant." EUR/USD: low temperature -0.0002 (t -1.91), average temperature +0.0002 (t 1.67), 10% only;
  logit nothing significant. No trading or cost test.
- **Relevance:** None (null for EUR/USD; weather data not in repo). **Status:** full text

### Demir, Lau & Fung (2014), "The Effect of International Soccer Games on Exchange Rates Using Evidence from Turkey", Journal of Advanced Studies in Finance 5(2), 145-156 (added 2026-11-14 R167)
- [Huddersfield record](https://pure.hud.ac.uk/en/publications/the-effect-of-international-soccer-games-on-exchange-rates-using-/)
  opened via web-fetch (abstract only; frequency, size, significance UNVERIFIED).
- **Finding (abstract):** TRY vs USD/EUR, 2003-2010: "draws and losses do not affect the exchange rates"; win effect "exists only for the
  Turkish national team" (lira appreciates). No EUR/USD, no euro-area team.
- Also opened: Samadi (2017), Erasmus bachelor thesis, [PDF](https://thesis.eur.nl/pub/39256/Samadi-H.-416255-.pdf) (~80% verbatim):
  German national team results vs next-day DAX, 79 matches 1990-2016: "no statistical significant relationship was found". No FX.
- **Relevance:** None (no EUR/USD basis; major-tournament match days ~10-20 in dev, far below the R090 power floor). **Status:** abstract / partial text

### Chortareas, Jiang & Nankervis (2013), "Volatility and Spillover Effects of Yen Interventions", Review of International Economics 21(4), 671-689 (added 2026-11-14 R168)
- [RePEc record](https://ideas.repec.org/a/bla/reviec/v21y2013i4p671-689.html) opened via web-fetch: no abstract, full text restricted
  (doi:10.1111/roie.12063, not opened). Findings, frequency, sample and any EUR/USD effect: UNVERIFIED.
- **Relevance:** None for now (no verified EUR/USD direction; no MoF yen intervention in dev 2015-2020). **Status:** record only

### Caporale & Plastun (2019), "The day of the week effect in the cryptocurrency market", Finance Research Letters (doi:10.1016/j.frl.2018.11.012) (added 2026-11-14 R168)
- [Brunel full text](https://bura.brunel.ac.uk/bitstream/2438/17208/3/FullText.pdf) opened via web-fetch.
- **Finding:** daily BTC/LTC/XRP/DASH 2013-2017; "The only exception is BitCoin, for which returns on Mondays are significantly higher";
  authors: "no conclusive evidence that the cryptocurrency market is inefficient". No fiat FX variable.
- **Relevance:** None (no crypto -> EUR/USD test). **Status:** full text

### Baum, Schäfer & Stephan (2016), "Credit rating agency downgrades and the Eurozone sovereign debt crises", Journal of Financial Stability 24, 117-131 (doi:10.1016/j.jfs.2016.05.001) (added 2026-11-14 R169)
- [EconPapers record](https://econpapers.repec.org/article/eeefinsta/v_3a24_3ay_3a2016_3ai_3ac_3ap_3a117-131.htm) opened via web-fetch
  (abstract only; full text subscriber-only, not opened).
- **Finding (abstract):** Moody's/S&P/Fitch euro-area sovereign downgrades, watchlist and outlook changes 2010-2012 "had no impact on
  the value of the Euro currency" "but increased exchange rate volatility" (event study + GARCH). Event count and window: UNVERIFIED.
- **Relevance:** None for direction (null level effect; sample precedes dev). **Status:** abstract only

### Yang & Zhang (2011), "The Impacts of Sovereign Credit Ratings on Exchange Rates - Evidence from Eurozone Sovereign Debt Crisis", Lund University master's thesis (added 2026-11-14 R169)
- [LUP record](https://lup.lub.lu.se/student-papers/search/publication/1973880) opened via web-fetch (abstract only; not peer-reviewed).
- **Finding (abstract):** 2009-01-01 to 2011-03-31; rating announcements "greatly affect the volatility rather than the mean of USD/EUR".
  Sign, window, event count: UNVERIFIED.
- **Relevance:** None for direction. **Status:** abstract only

### Vissing-Jorgensen (2025), "Fluctuations in the Treasury General Account and their effect on the Fed's balance sheet", FEDS Notes 2025-08-06 (doi:10.17016/2380-7172.3873) (added 2026-11-14 R170)
- [IDEAS record](https://ideas.repec.org/p/fip/fedgfn/2025-08-06.html) opened via web-fetch (abstract only). The full note on
  federalreserve.gov could not be opened this run (fetch permission timed out); its contents are UNVERIFIED.
- **Finding (abstract):** describes the TGA as the government's deposits at the Fed providing payment services; no exchange-rate
  variable in the abstract. Any USD or EUR/USD effect: UNVERIFIED.
- **Relevance:** None for now (no verified EUR/USD direction; daily TGA series not in repo). **Status:** abstract only

### Molodtsova, Nikolsko-Rzhevskyy & Papell (2011), "Taylor Rules and the Euro", JMCB 43(2-3), 535-552 (doi:10.1111/j.1538-4616.2011.00384.x) (added 2026-11-14 R171)
- [EconPapers record](https://econpapers.repec.org/RePEc:wly:jmoncb:v:43:y:2011:i:2-3:p:535-552) opened via web-fetch (abstract only;
  full text not opened, data frequency UNVERIFIED).
- **Finding (abstract):** real-time Taylor-rule fundamentals (inflation plus output gap or unemployment) give "evidence of out-of-sample
  predictability for the U.S. dollar/euro exchange rate from 1999 to 2007", with "both one-quarter-ahead and longer-horizon forecasts";
  strongest with symmetric coefficients, no smoothing, no real exchange rate.
- **Relevance:** None for the intraday/daily programme: quarterly horizon (~24 non-overlapping quarters on dev, below the R090 power
  floor), sample ends before dev, real-time macro vintages not in repo. **Status:** abstract only

### Caporale & Plastun (2022), "Persistence in High Frequency Financial Data", Brunel Economics and Finance WP 2215 (added 2026-11-14 R172)
- [Brunel WP PDF](https://www.brunel.ac.uk/economics-finance-and-accounting/research/pdf/2215-Oct-GMC-High-Frequency-persistence.pdf)
  opened via web-fetch (~100% of text; figures unreadable).
- **Finding:** EuroStoxx 50 futures only (Eurex, 2002-2018); R/S Hurst exponent: monthly H 0.72, daily 0.54, intraday 0.37
  ("intraday ones are anti-persistent"). Profitability of intraday reversal strategies is inferred from H values, not tested; no trading
  rule, no out-of-sample or direction test.
- **Relevance:** None directly: no FX data. Intraday mean-reversion families on EUR/USD are already tested in this repo. **Status:** verified (no FX)

### Geman & Li (2018), "An analysis of intraday market response to crude oil inventory shocks", Journal of Energy Markets 11(2), 1-35 (added 2026-11-14 R173)
- [Risk.net abstract page](https://www.risk.net/node/5728636), doi:10.21314/JEM.2018.174, opened via web-fetch (~10%: abstract and
  "need to know" bullets; full text paywalled).
- **Finding:** WTI crude futures only: "a positive (negative) inventory shock will result in an immediate price decline (rise)", effects
  "lasting for about twenty-five minutes". No exchange-rate variable in the readable text (any FX result UNVERIFIED).
- **Relevance:** None directly: no FX test; EIA consensus/surprise series not in repo. **Status:** abstract only (no FX)

### Wen, Indriawan, Lien & Xu, "Intraday Return Predictability in the Crude Oil Market: The Role of EIA Inventory Announcements", The Energy Journal 44(5) (added 2026-11-14 R173)
- [IAEE executive summary PDF](https://www.iaee.org/ej/ejexec/ej44-5-Xu-exsum.pdf) opened via web-fetch (executive summary only, <5% of
  the paper; year/DOI not shown in fetched text).
- **Finding:** WTI intraday momentum on EIA days: third half-hour return "can significantly and positively predict the returns in the
  last half-hour". No exchange-rate variable.
- **Relevance:** None directly: crude only; the oil -> EUR/USD lag family was already tested (E041). **Status:** exec summary only (no FX)

### Caporale, Plastun & Oliinyk, "The Frequency of One-Day Abnormal Returns and Price Fluctuations in the Forex", Brunel Economics and Finance WP 2005 (cover dated March 2020) (added 2026-11-14 R174)
- [Brunel PDF](https://www.brunel.ac.uk/economics-finance-and-accounting/research/pdf/2005-Mar-GMC-FOREX-frequency.pdf) opened via
  web-fetch (~65% verbatim, abstract through Table C.6; remainder not verified).
- **Data:** daily and monthly closes, EURUSD, GBPUSD, USDJPY, EURJPY, GBPCHF, AUDUSD, USDCAD, 1994-01-03 .. 2019-05-28 (Yahoo! Finance).
- **Finding:** monthly returns regressed on the count of same-month "abnormal" daily returns (> 1 SD); "the highest coefficient corresponds
  to lag length zero" (contemporaneous, not a forecast). EUR/USD monthly correlation 0.76 (Table 4), in-sample. "the results suggest that
  the latter is an important driver of price dynamics in the FOREX". No trading rule backtested, no costs, no out-of-sample test.
- **Relevance:** None: contemporaneous monthly relation, no lagged direction basis; monthly horizon below the R090 power floor. **Status:** read (partial)

### Popović & Đurović, "Intraweek and intraday trade anomalies: evidence from FOREX market", Applied Economics 46(32), 3968-3979, 2014, doi:10.1080/00036846.2014.948676 (added 2026-11-14 R176)
- **Opened:** IDEAS/RePEc record https://ideas.repec.org/a/taf/applec/v46y2014i32p3968-3979.html (abstract only; full text paywalled; econbiz record returned a bot-block page, not retried).
- **Data:** hourly EUR/USD, "Swiss FOREX market", 2004-01-01 .. 2014-01-11; ANOVA, t-tests and Tukey HSD on day, hour and day-by-hour mean returns.
- **Finding (abstract):** "The best arbitrage opportunity is evidenced on Fridays, when selling USD and buying EUR at 00:00", reversed at 03:00 the same day. No magnitude, significance figures or costs in the abstract; the clock time zone of "00:00" is UNVERIFIED (server time not stated).
- **Relevance:** Low. If 00:00 is CET/CEST, the window is 18:00-21:00 America/New_York on trading-date Friday, which E009 already scanned on dev (Fri_ny_18 +0.685, Fri_ny_19 -0.471, Fri_ny_20 +0.021 pips, all NONE; sum ~+0.2 pips, below the 1-pip bar) and which sits in the post-roll 18:00 NY family tested on val as B9/B10 (E012, WEAK/NONE). **Status:** read (abstract)

### Smeets, EU summit meetings and financial markets during the Eurozone crisis, Journal of Common Market Studies, doi:10.1111/jcms.12062 (added 2026-11-14 R177)
- **Opened:** LSE EUROPP blog summary by the author, LSE Research Online PDF https://researchonline.lse.ac.uk/id/eprint/72262/1/blogs.lse.ac.uk-EU%20summit%20meetings%20have%20had%20little%20effect%20on%20financial%20markets%20during%20the%20Eurozone%20crisis.pdf (full blog text read via web-fetch; the JCMS article itself not opened, its title UNVERIFIED; SSRN abstract_id=2340272 linked, not opened).
- **Data:** daily data, 10-year sovereign yields, stock indices (FR, DE, GR, IE, IT, PT, ES) and EUR/USD, autumn 2008 .. April 2012; event window not stated in the blog.
- **Finding:** "for the euro-US dollar exchange rate, no significant effects could be detected"; no direction or magnitude given.
- **Relevance:** None: null for EUR/USD; ~4-8 summits per year, below the R090 power floor. **Status:** read (author summary only)

### Krivosheev, "The seasonal effect of Chinese New Year in cryptocurrency market", B.Sc. thesis, Erasmus University Rotterdam, 2019 (added 2026-11-14 R178)
- **Opened:** https://thesis.eur.nl/pub/48070/Thesis_Krivosheev_453271.pdf (full text via web-fetch; some regression tables garbled).
- **Data:** daily BTC/USD (Bitfinex), 2013-03-10 .. 2019-05-08; dummies for 1 month before / after Chinese New Year; OLS and ARDL.
- **Finding (abstract, verbatim):** "we did not observe any seasonal effect except small negative movement of price (return)"; ARDL makes the CNY dummies insignificant; author notes the effect is too small to profit after costs.
- **Relevance:** None: Bitcoin only, no fiat FX, no EUR/USD. **Status:** read

### Carrière-Swallow, Kindberg-Hanlon & Smirnov, "Macroeconomic Effects and Spillovers from Bank of Japan Unconventional Monetary Policy", IMF WP/25/227, 2025 (added 2026-11-14 R178)
- **Opened:** https://www.imf.org/-/media/files/publications/wp/2025/english/wpiea2025227-source-pdf.pdf (~48% verbatim via web-fetch; remainder, incl. Table 4, only as model summary = UNVERIFIED).
- **Data:** 151 BoJ meetings 2010-01 .. 2023-12; intraday window "starting 5 minutes before the announcement and ending 30 minutes after the announcement"; FG and LSAP shocks.
- **Finding:** expansionary shocks "depreciate the yen" (USD/JPY only); spillovers measured on foreign 10y yields at h = 0..5 days (UNVERIFIED part). No EUR/USD result and no hour-scale post-announcement drift analysis.
- **Relevance:** None for a pre-registrable EUR/USD item: no EUR/USD evidence, no drift; BoJ meetings ~8/year, below the R090 power floor. **Status:** read (partial)

### Jandejsek, "The impact development of scheduled U.S. macroeconomic announcements on foreign exchange rates: An empirical study of the nonfarm payrolls announcement and the EURUSD over the past two decades", Master thesis, 2021 (added 2026-11-15 R179)
- **Opened:** https://web-typo3.modul.ac.at/uploads/files/Theses/Master/Grad_2021/MBA_2021/Master_Thesis_Jandejsek.pdf (~60% verbatim via web-fetch; remainder incl. conclusion not read = UNVERIFIED; institution inferred from host, UNVERIFIED).
- **Data:** 1-minute EUR/USD closes (HistData.com), 237 monthly NFP events 2000-2020, 26-minute event window.
- **Finding (partly model summary, UNVERIFIED):** immediate publication-minute jump (order of 25 pips average 2017-2020) with some later reversal; no formal post-announcement drift test, no transaction costs.
- **Relevance:** NFP family already covered (B12 blocked on release-date source, calendar-free 08:30 NY variant tested E015/E040 line). Not about ADP; no new pre-registrable item. **Status:** read (partial)

### "Volatility Risk Premia and Exchange Rate Predictability", CEPR Discussion Paper DP9549 (added 2026-11-15 R180)
- **Opened:** https://cepr.org/publications/dp9549 (listing page only; abstract marked as an AI translation on the page; authors, year, frequency and horizon not stated on the page = UNVERIFIED).
- **Finding (page summary):** a cross-sectional portfolio selling currencies with high volatility-insurance cost (realized volatility minus model-free option-implied expected volatility) and buying low-cost currencies earns sizeable out-of-sample returns, mostly from spot predictability.
- **Relevance:** None for a pre-registrable EUR/USD item: predictor needs currency-option implied volatility (not in repo, no verified download source), result is cross-sectional, EUR/USD not mentioned. **Status:** read (summary)

### Frömmel & Lampaert (2016): Does frequency matter for intraday technical trading?
- **Venue:** Finance Research Letters 18, 177-183. DOI 10.1016/j.frl.2016.04.014. [core.ac.uk PDF](https://core.ac.uk/download/55846873.pdf) (opened 2026-11-15 R184, full text via web-fetch; table extraction garbled, no cell figures used).
- **Finding (verbatim abstract):** "The adjustment for real, rather than estimated transaction costs wipes away most of the profits." RUB/USD (MICEX tick data with bid/ask), 4950 MA and 3069 RSI parameterisations on 10/15/30/60-minute bars, Jan 2000 - Jun 2011, Hansen SPA test.
- **Relevance:** **Low.** RUB/USD only (managed rate), no EUR/USD; supports the prior that intraday RSI/MA rules do not survive real spreads. Not used.
- **Status:** VERIFIED (full text, abstract quote)

### Aalto bachelor's thesis: Monetary policy announcement shocks and high-frequency exchange rate dynamics: evidence from the euro area (added 2026-11-15 R185)
- **Opened:** https://aaltodoc.aalto.fi/items/4dcf8e0b-b547-4905-a85a-64c7d58e84a3 (abstract and metadata only; full text behind Aalto login; author and year not shown = UNVERIFIED).
- **Finding (verbatim abstract):** "on average, a 100-basis point monetary policy announcement shock results in an immediate 3-4% appreciation of the exchange rate." EURUSD, EURGBP, EURJPY, 1999-2023, press-release window, shocks from 1- and 3-month OIS.
- **Relevance:** **Low.** Contemporaneous reaction only, needs OIS shock data (not in repo); bachelor's thesis, not peer reviewed. Not used. **Status:** read (abstract)

### Herbst (2007): Lunacy in the Stock Market - What is the Evidence?
- **Venue:** Journal of Bioeconomics 9(1), 1-18. DOI 10.1007/s10818-007-9016-3. [IDEAS](https://ideas.repec.org/a/kap/jbioec/v9y2007i1p1-18.html) (opened 2026-11-15 R185, abstract only).
- **Finding (verbatim abstract):** "no consistent, predictable lunar influence is found on either daily returns or daily price volatility in the Dow Jones Industrial Average, for either new or full moons."
- **Relevance:** None for EUR/USD (equities, published null, no mechanism). Not used. **Status:** read (abstract)

### Riddiough & Zhang (2022 WP): Cross-Border M&A Flows, Economic Growth, and Foreign Exchange Rates (added 2026-11-15 R194)
- **Opened:** https://www.bis.org/events/221213_bis_bdi_ecb_exchange_rates/paper_riddiough.pdf (draft dated 4 July 2022; ~22% read verbatim: intro, literature, data).
- **Finding (verbatim):** "currencies associated with the most abnormally high level of net investment inflows appreciate on average"; local-firm-driven outflows "typically experience an annualized exchange rate depreciation of 5.07% over the following month". 41 currencies vs USD, monthly, 1994-2018, SDC Platinum deal data.
- **Relevance:** **Low.** Monthly cross-sectional signal, needs licensed M&A data (not in repo), EUR/USD coverage not confirmed; FX result tables not read verbatim (UNVERIFIED). Not used. **Status:** read (partial)

### Fender & Galati (2001): The impact of transatlantic M&A activity on the dollar/euro exchange rate
- **Venue:** BIS Quarterly Review, December 2001. [IDEAS](https://ideas.repec.org/a/bis/bisqtr/0112g.html) (opened 2026-11-15 R194, abstract only).
- **Finding (verbatim abstract):** "the euro depreciated against the dollar by 1.06% - a significant move for a single day" on the Deutsche Telekom/VoiceStream news (19 July 2000).
- **Relevance:** **Low.** Single-event case study, no statistical test, pre-dates the dev block. Not used. **Status:** read (abstract)

### Correa, Du & Liao (2020): U.S. Banks and Global Liquidity (added 2026-11-15 R196)
- **Venue:** Federal Reserve IFDP 1289, July 2020, DOI 10.17016/IFDP.2020.1289. [PDF](https://www.federalreserve.gov/econres/ifdp/files/ifdp1289.pdf) (opened 2026-11-15 R196; ~32% read verbatim: cover, abstract, intro, sections 1-3).
- **Finding (verbatim):** "We find that an increase in the TGA balance is significantly associated with wider repo and FX swap spreads." Daily FR2052a GSIB data; same-day changes; outcomes are funding spreads and bank quantities, not spot FX returns.
- **Relevance:** **Low.** No exchange-rate return or forecast test in the part read (rest UNVERIFIED); weekly TGA/RRP data not in repo. Not used. **Status:** read (partial)

### Deng, Yu, Wei, Yang & Tatsuro (2021): Ichimoku Kinkohyo trading rules in stock and FX markets (added 2026-11-15 R197)
- **Venue:** International Journal of Finance & Economics 26(4), 5321-5336, DOI 10.1002/ijfe.2067. [RePEc record](https://ideas.repec.org/a/wly/ijfiec/v26y2021i4p5321-5336.html) (opened 2026-11-15 R197; abstract only, full text not opened).
- **Finding (abstract, paraphrased):** four stock indices (1995-2018) and four "important currency pairs" (2003-2018); with default (9, 26, 52) settings some rules were profitable in FX in subperiod 1 but not consistently in subperiod 2; the parameter sweep found no profitable rule for currency trading. Pairs named, data frequency and costs: UNVERIFIED.
- **Relevance:** **Low (negative evidence).** No stable FX effect reported; nothing to pre-register. Not used. **Status:** read (abstract)

### Franco Silva (2012): Optimization of technical trading rules in Forex using genetic algorithm (added 2026-11-15 R197)
- **Venue:** M.Sc. thesis, ISCTE Business School, Oct 2012 (not peer-reviewed). [PDF](https://repositorio.iscte-iul.pt/bitstream/10071/6396/1/master_pedro_franco_silva.pdf) (opened 2026-11-15 R197; ~45% read verbatim, rest via extracted summary = UNVERIFIED).
- **Finding:** daily bars, EUR/USD, EUR/JPY, EUR/GBP, EUR/CHF; MACD, double crossover, Bollinger, RSI, Stochastic, Parabolic SAR, ADX with GA-optimised parameters; in-sample 2005-2009, out-of-sample 2010-2011. EUR/USD MACD figures (from summary, UNVERIFIED): in-sample profit factor 1.52 (p 0.083), out-of-sample profit factor 0.97 (p 0.487).
- **Relevance:** **Low (negative evidence).** Optimised daily rules do not hold out of sample; consistent with lesson on technical rules (E047-E049 NONE). Not used. **Status:** read (partial)

### Della Corte, Jeanneret & Patelli (2023): A credit-based theory of the currency risk premium (added 2026-11-15 R201)
- **Venue:** Journal of Financial Economics (accepted 8 June 2023, ISSN 0304-405X; DOI 10.1016/j.jfineco.2023.06.002 UNVERIFIED, not seen in text read). [PDF](https://spiral.imperial.ac.uk/bitstream/10044/1/96561/9/1-s2.0-S0304405X23001162-main.pdf) (opened 2026-11-15 R201; ~32% read verbatim: abstract, intro, section 2, start of section 3; tables not read).
- **Finding (verbatim):** "We find that the credit-implied risk premium positively predicts future dollar-euro exchange rate returns at any horizon between one week and one year". Predictor = gap between USD- and EUR-denominated one-year CDS premia on 16 euro-area sovereigns ("daily CDS premia on 16 Eurozone member states quoted in both currencies between August 2010 and April 2019", IHS Markit). At one month a one-s.d. increase is "associated with a positive exchange rate return of 7.9% per annum" (verbatim). t-statistics not read (UNVERIFIED). Only trading test is a weekly euro-vs-dollar bond allocation.
- **Relevance:** **Medium in principle, not testable here.** A published, signed USD/EUR predictor at weekly+ horizon, but it needs licensed quanto-CDS data (IHS Markit) that is not in the repo and not downloadable on the runner; weekly horizon gives ~312 dev observations (below power floor). Would need a human data decision. Not used. **Status:** read (partial)

### (Draft, authors not shown) Sovereign credit risk and exchange rates: Evidence from CDS quanto spreads (added 2026-11-15 R201)
- **Venue:** conference draft dated 10 Nov 2017. [PDF](https://www.runi.ac.il/media/o5wklx5n/sovereign-credit-risk-and-exchange-rates.pdf) (opened 2026-11-15 R201; ~36% read verbatim).
- **Finding:** no-arbitrage pricing model of euro-area CDS quanto spreads; weekly (Wednesday) data 2010-2016; USD/EUR is a model state variable, no predictive regression or trading rule ("We work with weekly data frequency to minimize noise due to potential staleness of some of the price", verbatim).
- **Relevance:** **Low.** Pricing model, no return forecast. Not used. **Status:** read (partial)

### Safa & Maroney (2012), "Bid-Ask Spread, Futures Market Sentiment and Exchange Rate Returns", Journal of Economic Cooperation and Development 33(4), 63-85, doi:10.5281/zenodo.20762890 (added 2026-11-15 R202)
- **Venue:** [article page](https://journal.sesric.org/Article/Detail/ART12083101) (abstract opened 2026-11-15 R202). PDF not opened (fetch not permitted in this run; not circumvented) -> body UNVERIFIED.
- **Finding (abstract, verbatim):** "Time series and cross-sectional analyses of three different currency exchange rates; Australian Dollar, British Pound and Canadian Dollar – to US Dollar suggest that the spot market bid-ask spread is one important variable that positively affects the spot exchange rate returns." Volume-based futures sentiment index significant, return-based not. Frequency, sample, lag structure (predictive vs contemporaneous) and magnitudes not stated in the abstract (UNVERIFIED).
- **Relevance:** **Low.** No EUR/USD in the abstract, unknown frequency and no evidence that the spread effect is lagged (predictive). Not used. **Status:** abstract only

### Roy Trivedi (2022), "Technical analysis using Heiken Ashi Stochastic: To catch a trend, use a HASTOC", International Journal of Finance & Economics 27(2), 1836-1847, doi:10.1002/ijfe.2245 (added 2026-11-16 R204)
- **Venue:** [IDEAS/RePEc page](https://ideas.repec.org/a/wly/ijfiec/v27y2022i2p1836-1847.html) (abstract and metadata opened 2026-11-16 R204 via web-fetch summary; paper body not opened -> body UNVERIFIED).
- **Finding (abstract, short verbatim fragments):** HASTOC indicator built from Heiken Ashi candles, reflecting "in a single number the likelihood of trend generation and momentum in the market"; backtested on three (unnamed) currencies, one index and one stock over "three major time frames"; "consistent positive returns for select time frames and markets". Currency pairs, frequency, costs and holding period not stated (UNVERIFIED).
- **Relevance:** **Low.** Selected-time-frame positive results (in-sample selection), no EUR/USD confirmed, no costs. Not used. **Status:** abstract only

### Roy Trivedi (2018), "Technical Analysis Strategies: Development of Heiken Ashi Stochastic", MPRA Paper 89594 (added 2026-11-16 R204)
- **Venue:** [IDEAS/RePEc page](https://ideas.repec.org/p/pra/mprapa/89594.html) (abstract opened 2026-11-16 R204; PDF not opened).
- **Finding (abstract):** HASTOC rule "back tested with an entry-exit strategy" on "intraday hourly USD/INR data from May, 2018 to September, 2018" (~4 months); long and short signals; costs and horizon not stated.
- **Relevance:** **Low.** USD/INR only, 4-month sample. Not used. **Status:** abstract only

### Papaioannou, Russo, Papaioannou & Siettos, "Can social microblogging be used to forecast intraday exchange rates?" (added 2026-11-16 R206)
- **Venue:** [arXiv 1310.5306](https://arxiv.org/abs/1310.5306) (opened 2026-11-16 R206 via web-fetch, ~100% of text read); page states it is a prior version of the paper published in NETNOMICS (Springer; volume/pages UNVERIFIED).
- **Finding:** 20,250 tweets matching "buy EUR/USD" (posted limit-order target prices, not sentiment), 25/10/2010-05/01/2011 (54 trading days), aggregated hourly; ARX vs random walk, 60/40 out-of-sample split. Verbatim: "no ARX model could significantly outperform the random walk model in terms of the RMSE and MAE". Directional hit up to ~0.59 in the returns setup only; no signed coefficient; no transaction costs.
- **Relevance:** **Low.** 54-day sample, no significant forecast gain, no costs, and no tweet archive is available on the runner. Not used. **Status:** read

### Gholampour & van Wincoop (2016), "What Can we Learn from Euro-Dollar Tweets?" (added 2026-11-16 R206)
- **Venue:** NBER conference paper dated 17 Oct 2016, [PDF](https://conference.nber.org/conf_papers/f89970/f89970.pdf) (opened 2026-11-16 R206 via web-fetch; ~34% verbatim, rest model summary -> details from the rest UNVERIFIED). VoxEU column of the same title not opened (permission prompt timed out; not circumvented).
- **Finding:** 268,770 EURUSD tweets, 9 Oct 2013-11 Mar 2016 (633 trading days), lexicon sentiment, "informed" = >= 500 followers. Verbatim: "We document that the direction of exchange rate changes is predicted by tweets in a way that is statistically significant" and "Twitter Sentiment does not predict the magnitude of future exchange rate changes in a statistically significant way". Horizons 20/40/60 trading days; short-lag (t to t-4 days) regressions insignificant (verbatim section 2.6). No cost treatment found in the part read.
- **Relevance:** **Low for this repo.** Predictability is directional only at 1-3 month horizons (below power floor on dev, R090), the data (historical Twitter archive) is not downloadable on the runner, and short lags are insignificant. Not used. **Status:** read (partial)

### Alanazi, Alanazi & McMillan (2020), "The profitability of technical analysis: Evidence from the piercing line and dark cloud cover patterns in the forex market" (added 2026-11-16 R207)
- **Venue:** Cogent Economics & Finance 8(1), article 1768648, doi:10.1080/23322039.2020.1768648, [IDEAS](https://ideas.repec.org/a/taf/oaefxx/v8y2020i1p1768648.html) (abstract opened 2026-11-16 R207 via web-fetch). Publisher full text not opened (permission prompt timed out; not circumvented).
- **Finding (abstract):** 112,792 daily candles, 24 currency pairs, 2000-2018. Verbatim: "We find that chart patterns are profitable." and "Nevertheless, the transaction costs are substantial. In particular, the spread is a large burden on profitability." EUR/USD not named; pattern definition, prior-trend filter, entry and holding horizon not in the abstract (UNVERIFIED).
- **Relevance:** **Low until the full text is read.** Same author and design family as Alanazi 2020 EJF (R142, engulfing patterns, abstract only). Daily two-candle reversal patterns give few EUR/USD events on dev and the rule cannot be pre-registered without the paper's definition. Not used. **Status:** VERIFIED (abstract only); design UNVERIFIED

### Detollenaere & Mazza (2012), "Do Japanese Candlesticks help solving the trader's dilemma?" (added 2026-11-16 R207)
- **Venue:** working paper draft dated 20 Aug 2012, [PDF](https://acfr.aut.ac.nz/__data/assets/pdf_file/0013/30064/AFM_2012_039.pdf) (opened 2026-11-16 R207 via web-fetch, partly verbatim, rest model summary -> UNVERIFIED).
- **Finding:** 81 Euronext stocks, 15-minute candles, Feb-Apr 2006; studies execution costs (market impact, timing) after Hammer-like and Doji patterns, not directional returns. No FX.
- **Relevance:** **None.** Equities, execution-cost question. Not used. **Status:** read (partial)

### Dueker & Neely, "Can Markov switching models predict excess foreign exchange returns?" (added 2026-11-16 R208)
- **Venue:** Federal Reserve Bank of St. Louis WP 2001-021 (revised version "2001-021F", text dated 30 Jan 2006), [PDF](https://s3.amazonaws.com/real.stlouisfed.org/wp/2001/2001-021.pdf) (opened 2026-11-16 R208 via web-fetch; ~77% of text read verbatim, remainder truncated -> details from the end of the paper UNVERIFIED). Title page lists publication in Journal of Banking & Finance, doi:10.1016/j.jbankfin.2006.03.002 (journal year/volume UNVERIFIED; cited as 2007 elsewhere).
- **Finding:** daily excess returns of DEM (EUR after 1998, spliced), JPY, CHF, GBP vs USD; Markov switching model; in-sample 1974-1981/82, out-of-sample 1982/83 to June 2005. Trading signal uses the model's average expected return over eight days; returns "net of 10-basis-point transactions costs". Verbatim (abstract): "The Markov models' out-of-sample, excess returns modestly exceed those of standard technical rules". Out-of-sample excess returns average 5.27%/yr across the four rates (1.08% GBP to 7.54% JPY); ~95 bp/yr above the best moving-average rules. Forecast accuracy (MSE/MAE) does not consistently beat the constant-return benchmark.
- **Relevance:** **Medium.** Published, cost-adjusted, out-of-sample daily rule on a series that includes EUR/USD; price data only. Caveats: sample ends 2005 (decay per Neely-Weller-Ulrich 2009), the published model has switching in mean, variance and kurtosis with interest differentials (our spot-only Gaussian version is a simplification), EUR/USD-specific figure not read. Basis for B60. **Status:** VERIFIED (partial full text)

### Parikakis & Merika (2009), "Evaluating volatility dynamics and the forecasting ability of Markov switching models" (added 2026-11-16 R208)
- **Venue:** Journal of Forecasting 28(8), 736-744, doi:10.1002/for.1135, [EconPapers](https://econpapers.repec.org/RePEc:jof:jforec:v:28:y:2009:i:8:p:736-744) (abstract opened 2026-11-16 R208 via web-fetch; full text subscription-only, not opened).
- **Finding (abstract):** daily returns of four euro rates; in- and out-of-sample "Markov trading rules based on Dueker and Neely"; verbatim: "the model provides exceptional out-of-sample returns" for EUR/USD and EUR/GBP; loses power for EUR/BRL, EUR/MXN. No numbers, sample period, horizon or cost treatment in the abstract (UNVERIFIED).
- **Relevance:** **Medium (supporting).** Names EUR/USD directly, but abstract only and "exceptional" is unquantified. Supports B60. **Status:** VERIFIED (abstract only)

### Theofilatos, Likothanassis & Karathanasopoulos (2012), "Modeling and Trading the EUR/USD Exchange Rate Using Machine Learning Techniques" (added 2026-11-16 R211)
- **Venue:** Engineering, Technology & Applied Science Research 2(5), 269-272, doi:10.48084/etasr.200, [article page](https://www.etasr.com/index.php/ETASR/article/view/200) (abstract opened 2026-11-16 R211 via web-fetch); full text read from a third-party mirror of the PDF ([distantreader.org](https://distantreader.org/stacks/journals/etasr/etasr-200.pdf); not the publisher copy; Table III partly garbled in extraction, cross-checked against the text by the fetch agent).
- **Data/design:** EUR/USD ECB daily reference rate (Datastream), 17 Jan 2002 - 30 Dec 2010 (2294 days); training 1363 / validation 459 / test 471 days (3 Mar 2009 - 30 Dec 2010). Inputs: 10 lagged daily returns only; target: next-day direction. Classifiers KNN, Naive Bayes, MLP, SVM (RBF), Random Forest (51 trees); parameters tuned by genetic algorithm on training + validation. Rule: always in the market, long if predicted up, short if predicted down. Costs ~1 pip per position.
- **Finding (as extracted):** Random Forest annualized return 8.29% gross, 7.28% after costs, information ratio 0.72, 53.50% correct direction; SVM 4.90% / 3.98%; MACD 3.08% / 2.80%; naive -5.51%. Verbatim: "SVM and Random Forests outperform all models in terms of annualized return and information ratio even when transaction costs are considered." No significance tests.
- **Caveats:** one pair, one 22-month test window; the text introducing Table III says it reports "the validation subset", contradicting the test-set claim (unresolved, UNVERIFIED which subset); GA-tuned hyperparameters other than tree count not reported for RF.
- **Relevance:** **Low-medium.** EUR/USD-specific, price-only, cost-aware daily rule that can be pre-registered with fixed settings (10 lags, 51 trees). Weak prior (short test, possible validation reporting, no t-stats). Basis for B62. **Status:** VERIFIED (full text via mirror; Table III subset UNVERIFIED)

### Fernández-Rodríguez, Sosvilla-Rivero & Andrada-Félix (2002/2003), "Nearest-Neighbour Predictions in Foreign Exchange Markets" (added 2026-11-16 R214)
- **Venue:** FEDEA Documento de Trabajo 2002-05, [full text page](https://documentos.fedea.net/documento/dt-2002-05/texto) (opened 2026-11-16 R214 via web-fetch, page truncated), [EconPapers record](https://econpapers.repec.org/RePEc:fda:fdaddt:2002-05); published as "Technical analysis in foreign exchange markets: evidence from the EMS", Applied Financial Economics 13(2), 113-122, doi:10.1080/09603100210100891, [EconPapers abstract](https://econpapers.repec.org/RePEc:taf:apfiec:v:13:y:2003:i:2:p:113-122) (abstract only; full text subscription).
- **Data/design:** daily, nine EMS currencies against the Deutsche mark, 1 January 1978 - 31 December 1994 (abstract). Simultaneous nearest-neighbour predictor (embedding m = 6, k about 2% of the sample, local linear regression); long/short on the sign of the predicted return. No EUR/USD, no USD pair.
- **Finding (abstract, verbatim):** "in most cases, a trading rule based on a non-linear predictor outperforms the moving average"; results consider "both interest rates and transaction costs". Cost size (0.05% per position change), per-currency net returns and test statistics are from a model-extracted summary of the truncated page: UNVERIFIED.
- **Relevance:** **Low.** Pre-euro EMS crosses in a managed-band regime (1978-1994), not EUR/USD; same family as B62 (nonparametric predictor on lagged daily returns, E051 NONE). **Status:** VERIFIED (abstract and partial text; trading-table numbers UNVERIFIED)

### Darvas & Schepp (2020/2024), "Forecasting exchange rates of major currencies with long maturity forward rates" (added 2026-11-16 R215)
- **Venue:** Bruegel Working Paper 02/2020, [abstract page](https://bruegel.org/working-paper/forecasting-exchange-rates-major-currencies-long-maturity-forward-rates) (opened 2026-11-16 R215 via web-fetch); revised version JIMF 2024, doi:10.1016/j.jimonfin.2024.103067 (not opened, UNVERIFIED). Full-text PDF fetch refused (permission timeout).
- **Data/design (abstract):** error-correction model built on long-maturity forward exchange rates, consistent with the monetary model; "twelve major currency pairs", 1990-2020. Pairs list, data frequency and horizons UNVERIFIED (not on the abstract page).
- **Finding (abstract, verbatim):** "outperforms the random walk in out-of-sample forecasting of twelve major currency pairs in both short and long horizons"; robust except around the Lehman collapse. No trading rule or costs on the abstract page.
- **Relevance:** **Low** for this repo: needs long-maturity forward rates (not in repo, not a proven runner download); monetary-model horizon is monthly and longer, below the power floor of lesson R090. **Status:** abstract VERIFIED, details UNVERIFIED.

### Jansen & de Haan (2005), "Were verbal efforts to support the euro effective? A high-frequency analysis of ECB statements" (added 2026-11-16 R216)
- **Venue:** working paper dated April 2005, [PDF on nbp.pl](https://nbp.pl/wp-content/uploads/2023/01/jansen_dehaan.pdf) (opened 2026-11-16 R216 via web-fetch, full text). Journal publication UNVERIFIED (the related "Talking heads", JIMF 24(2) 343-361, not opened).
- **Data/design:** 5-minute Olsen EUR/USD mid-quotes, 4 Jan 1999 - 17 May 2002; 146 ECB verbal interventions on 127 trading days (Governing Council days, official interventions and weekends excluded); +/- 3 h event windows, sign test vs p = 0.5 (baseline 48.1% positive 5-minute returns).
- **Finding (verbatim):** "ECB verbal interventions have had only small and short-lived effects"; effects "negligible and short-lived"; the only marginally significant window starts 10 minutes before the statement (p = 0.06); e.g. 66 positive returns in the 15-minute window, p = 0.86.
- **Relevance:** **None** for a directional rule: no lasting drift; pre-euro-crisis sample; needs statement timestamps not in repo. **Status:** VERIFIED (full text).

### Fanta (2025), "CB monetary Policy Communication: An Event Study on Intraday Returns and Volatility in the EUR/USD FX Market" (added 2026-11-16 R216)
- **Venue:** IES Working Paper 23/2025, Charles University, [RePEc/IDEAS](https://ideas.repec.org/p/fau/wpaper/wp2025_23.html) and [IES page](https://ies.fsv.cuni.cz/cb-monetary-policy-communication-event-study-intraday-returns-and-volatility-eur/usd-fx-market) (abstract opened 2026-11-16 R216; full PDF not read).
- **Data/design (abstract):** 1,868 Reuters-reported ECB statements 2008-2016 coded dovish/neutral/hawkish, outside policy-meeting days; 1-minute EUR/USD; cumulative abnormal returns and realised volatility.
- **Finding (abstract, verbatim):** "Cumulative abnormal returns remain within a few basis points by t=+20, and scattered significant minutes are not sequential"; communication "does not generate lasting directional moves". Coefficients UNVERIFIED (full text not read).
- **Relevance:** **None** for a directional rule (null on returns). **Status:** abstract VERIFIED.

### Khurram, Ali, Jiang & Xie (2022), "Predictability of extreme daily returns and Preference for lottery-like stocks in an emerging market" (added 2026-11-16 R217)
- **Venue:** Economic Research-Ekonomska Istraživanja 35(1), 1322-1344, doi:10.1080/1331677X.2021.1965000; [RePEc/IDEAS](https://ideas.repec.org/a/taf/reroxx/v35y2022i1p1322-1344.html) (abstract opened 2026-11-16 R217 via web-fetch; full text subscriber-only, not read).
- **Data/design (abstract):** cross-section of Pakistan Stock Exchange stocks sorted on the maximum daily return of the month (MAX effect); next-month risk-adjusted returns, 3- and 6-month holds. Sample period UNVERIFIED.
- **Finding (abstract):** a MAX effect that "persists even if we extend the holding period to three- and six-month". Equities only; no FX results.
- **Relevance:** **None**: cross-sectional equity lottery-preference effect, no single-currency time-series test, no EUR/USD. **Status:** abstract VERIFIED.

### Batten, Ellis & Hogan (2004/05), "Decomposing Intraday Dependence in Currency Markets: Evidence from the AUD/USD Spot Market" (added 2026-11-16 R218)
- **Venue:** arXiv [math/0412344](https://arxiv.org/abs/math/0412344) (opened 2026-11-16 R218 via web-fetch; full text returned). Publication venue/date UNVERIFIED (references run to 2005).
- **Data/design:** ~29,600 Reuters FX= AUD/USD bank quotes, 5 May - 15 Jun 2000; local Hurst exponents on rolling 10/20-quote windows averaged by GMT hour; ANOVA / Kruskal-Wallis and shuffled-series bootstrap.
- **Finding (abstract, verbatim):** "time-varying dependence and volatility clearly aligning with the opening and closing of markets"; "This variation is attributed to the effects of liquidity and the price-discovery actions of dealers". Authors call the results "tentative".
- **Relevance:** **None** for a directional rule: descriptive, 6 weeks of AUD/USD, no trading rule, no return-direction forecast, quote-window (sub-hour) horizon. **Status:** VERIFIED (full text via web-fetch).

### Chaboud, Chernenko, Howorka, Krishnasami Iyer, Liu & Wright (2004), "The High-Frequency Effects of U.S. Macroeconomic Data Releases on Prices and Trading Activity in the Global Interdealer Foreign Exchange Market" (added 2026-11-16 R219)
- **Venue:** Federal Reserve Board, International Finance Discussion Papers No. 823, November 2004; [HTML](https://www.federalreserve.gov/pubs/ifdp/2004/823/ifdp823.htm) (opened 2026-11-16 R219 via web-fetch; first ~half verbatim, remainder via fetch summary).
- **Data/design:** EBS interdealer EUR/USD and USD/JPY, Jan 1999 - Jan 2004; second-by-second best quotes, 1-minute returns and volume; six US releases incl. retail sales, GDP, PPI, NFP, trade balance, FOMC; return windows from 1 min before to up to ~1 hour after.
- **Finding (Sec. 4.3, verbatim):** the surprise "produces a movement in the conditional mean that is generally completed within a few minutes, and that is effectively a jump"; "the exchange rate returns subsequent to the few minutes around the time of the data release are orthogonal to the unexpected component of the macroeconomic announcement." Volatility and volume stay elevated afterwards (Sec. 4.2). No test beyond ~1 hour.
- **Relevance:** **Negative** for a post-release drift item (retail sales or other US releases) on EUR/USD: price adjustment is complete within minutes. **Status:** VERIFIED (partly via fetch summary as noted).

### Dimitriadou & Gregoriou (2023), "Predicting Bitcoin Prices Using Machine Learning" (added 2026-11-16 R220)
- **Venue:** Entropy 25(5):777, DOI [10.3390/e25050777](https://pmc.ncbi.nlm.nih.gov/articles/PMC10216962/) (PMC copy opened 2026-11-16 R220 via web-fetch; partly via fetch summary).
- **Data/design:** Bitcoin up/down direction as the target; 24 regressors incl. EUR/USD, GBP, JPY, AUD vs USD, rates, macro, 13 cryptocurrencies; Dec 2014 - Jul 2019, 239 observations (frequency stated inconsistently: daily/weekly); logit, linear SVM, random forest.
- **Finding:** best accuracy ~66% (logit) for Bitcoin direction. No test of crypto -> FX direction.
- **Relevance:** **None** for EUR/USD (FX is a regressor, not the target). **Status:** VERIFIED (partly via fetch summary).

### Pečiulis & Vasiliauskaitė (2021), "Exogenous factors that influence returns of Bitcoin and Ether" (added 2026-11-16 R220)
- **Venue:** 15th International Days of Statistics and Economics (MSED), Prague, 2021, pp. 809-818; [PDF](https://msed.vse.cz/msed_2021/article/529-Peciulis-Tomas-paper.pdf) (opened 2026-11-16 R220 via web-fetch).
- **Data/design:** daily BTC-USD and ETH-USD, Jul 2015 - Apr 2021; SARMAX with ten exogenous factors incl. EUR/USD as a same-period regressor.
- **Finding (verbatim):** "EUR/USD exchange rate, 10-yr US treasury bonds, Nikkei 225 has insignificant p-values". No Granger test in either direction.
- **Relevance:** **None** for a lagged crypto -> EUR/USD rule. **Status:** VERIFIED.

### Lustig, Roussanov & Verdelhan (2014), "Countercyclical currency risk premia" (added 2026-11-16 R221)
- **Venue:** Journal of Financial Economics 111(3):527-553, DOI 10.1016/j.jfineco.2013.12.005; [RePEc abstract](https://econpapers.repec.org/RePEc:eee:jfinec:v:111:y:2014:i:3:p:527-553) and [NBER WP 16427 PDF](https://www.nber.org/papers/w16427.pdf) (opened 2026-11-16 R221 via web-fetch; NBER text read verbatim to ~47%, rest via fetch summary; JFE version not opened).
- **Data/design:** "dollar carry": long a basket of foreign currencies vs USD when the average forward discount (average foreign short rate minus US short rate) is positive, short otherwise; end-of-month series from daily spot/forward quotes, Nov 1983 - Jun 2010; horizons 1-12 months.
- **Finding (verbatim):** "The key predictor in our study is the average forward discount on foreign currency against the U.S. dollar". Dollar carry Sharpe ~0.66 (developed basket), 1-month AFD R^2 ~3%, ~13% at 12 months. No EUR/USD-only result read; no daily or intraday horizon.
- **Relevance:** **Low** for this repo: monthly basket signal (below the R090 power floor on dev), needs forward points / short rates not in the repo. **Status:** VERIFIED (partly via fetch summary).

### Mir Yazdi & Habibi Lashkary (2012), "Technical analysis of Forex by Parabolic SAR Indicator" (added 2026-11-16 R221)
- **Venue:** conference paper, Nov 2012 (ResearchGate cover; conference name not in the text); [PDF mirror](https://c.mql5.com/forextsd/forum/221/Technical%20analysis%20of%20Forex%20by%20Parabolic%20SAR%20Indicator.pdf) (opened 2026-11-16 R221 via web-fetch).
- **Data/design:** hourly EUR/USD, GBP/USD, USD/CHF, USD/JPY, 2001-2010; Wilder default P-SAR, fixed 30-pip TP/SL, 10-hour time exit; no spreads/commissions modelled; no train/test split.
- **Finding:** EUR/USD net +1,459 pips over 4,967 orders (~0.29 pips/order gross); other pairs negative or marginal; authors call P-SAR "not a suitable indicator".
- **Relevance:** **None**: gross edge per trade is far below the SPEC 4 cost model; in-sample only. **Status:** VERIFIED (mirror copy, venue UNVERIFIED).

### Cerutti, Obstfeld & Zhou (2020 draft), "Covered Interest Parity Deviations: Macrofinancial Determinants" (added 2026-11-16 R222)
- **Venue:** NBER conference paper dated 31 May 2020, revision of NBER WP 26129 (2019); [PDF](https://conference.nber.org/conf_papers/f132236.pdf) (opened 2026-11-16 R222 via web-fetch, ~37% verbatim; rest only via fetch summary, not used).
- **Data/design:** daily 3-month LIBOR (and Treasury) cross-currency basis for 10 currencies incl. EUR vs USD, averaged to monthly, 2002-2019; regressions explain contemporaneous monthly basis changes.
- **Finding (verbatim, p.8):** "By using monthly averages, our regressions aim to highlight drivers of CIP deviations at a relatively lower frequency". No spot-return forecast in the verbatim part; quarter-end section not read verbatim (UNVERIFIED).
- **Relevance:** **None** for a spot EUR/USD direction rule (dependent variable is the basis, monthly). **Status:** VERIFIED (partial).

### Krohn & Sushko (2020), "FX spot and swap market liquidity spillovers" (added 2026-11-16 R222)
- **Venue:** BIS Working Paper 836, Jan 2020; [landing page](https://www.bis.org/publ/work836.pdf) (opened 2026-11-16 R222: abstract/summary only; PDF fetch permission timed out, not circumvented).
- **Finding (landing page):** uses "exogenous quarter-end funding liquidity shocks in FX swap markets"; worse funding liquidity (forward discount / CIP deviations) goes with wider spot bid-ask spreads. Dependent variable is spot liquidity, not returns.
- **Relevance:** **None** for a direction rule (liquidity, not returns; body UNVERIFIED). **Status:** VERIFIED (abstract only).

### Moreira & Muir (2016 WP / JF 2017), "Volatility-Managed Portfolios" (added 2026-11-16 R223)
- **Venue:** NBER Working Paper 22208 (April 2016, revised June 2016); [PDF](https://www.nber.org/papers/w22208.pdf) (opened 2026-11-16 R223; first ~40k characters read verbatim, rest summarised by the fetch tool, so table values below are UNVERIFIED).
- **Finding (verbatim part):** scaling factor exposure by the inverse of previous-month realized variance raises alphas for equity factors "as well as the currency carry trade"; the FX factor is "the monthly high minus low carry factor formed on the interest rate differential" (Lustig et al. 2011 portfolios); daily data only feed the variance estimate; rebalanced "once a month". Text reports an appraisal ratio of 0.44 for scaled Carry; "the alpha for the currency carry trade disappears" under common-volatility scaling (Table 7).
- **Relevance:** **None** for a pre-registrable EUR/USD item: monthly multi-currency carry basket, no single-pair or daily-horizon result; volatility scaling is a sizing overlay, not a direction signal, and the repo has no surviving dev/val signal to scale. **Status:** VERIFIED (partial verbatim read).

### Alexandridis, Panopoulou & Souropanis (2024), "Forecasting exchange rates: An iterated combination constrained predictor approach" (added 2026-11-16 R225)
- **Venue:** Journal of Forecasting 2024, 1-35, DOI 10.1002/for.3067; [accepted manuscript, Essex repository](https://repository.essex.ac.uk/36889/1/Journal%20of%20Forecasting%20-%202024%20-%20Alexandridis%20-%20Forecasting%20exchange%20rates%20An%20iterated%20combination%20constrained%20predictor.pdf) (opened 2026-11-16 R225 via web-fetch; first ~32% read verbatim, rest summarised by the fetch tool).
- **Data/design:** daily GBP, JPY, CHF, EUR, CAD, AUD vs USD; one-day-ahead recursive out-of-sample forecasts from 14 lagged daily predictors (changes in VIX and TED, gold, oil, Baltic Dry Index, CRB, MSCI, S&P 500 and its volatility, equity-market and yield-curve level/slope/curvature changes); no other exchange rates' lagged returns as predictors; transaction costs not seen in the verbatim part (UNVERIFIED for the rest).
- **Finding (abstract, verbatim):** "Positivity constraints significantly improve the forecasting ability of all methods." The headline is a ranking of forecast-combination methods, not an economically sized EUR/USD trading result.
- **Relevance:** **Low.** Its single-predictor building blocks overlap tests already run here (lagged gold E042, lagged oil E041, lagged equities/VIX refills), which lesson R095 says not to queue again; TED, BDI and CRB are not runner-downloadable from Dukascopy. **Status:** VERIFIED (partial).

### Chen & Tsang (2011 version), "What Does the Yield Curve Tell Us About Exchange Rate Predictability?" (added 2026-11-16 R226)
- **Venue:** working paper, "This version: June 2011"; [PDF](https://faculty.washington.edu/yuchin/Papers/CT1v3.pdf) (opened 2026-11-16 R226 via web-fetch; first ~40k characters read verbatim, rest summarised by the fetch tool, so per-country details are UNVERIFIED).
- **Data/design:** monthly CAD, GBP, JPY vs USD (no EUR or DEM), Aug 1985 - July 2005 (plus a 1991-2011 check); relative (home minus US) Nelson-Siegel level, slope, curvature factors; horizons 1-24 months; no daily or cost-adjusted trading result; rolling out-of-sample forecasts (footnote 6) "does not consistently outperform" random-walk benchmarks.
- **Finding (verbatim):** "the yield curve factors predict exchange rate movements and explain excess currency returns one month to two years ahead", "with the slope factor being the most robust across currencies".
- **Relevance:** **None** for a pre-registrable EUR/USD item: monthly horizon (below the R090 power floor), no EUR, weak out-of-sample, and euro-area yield curves are not in the data pipeline. **Status:** VERIFIED (partial verbatim read).

### Londono & Zhou (2012), "Variance Risk Premiums and the Forward Premium Puzzle" (added 2026-11-17 R228)
- **Venue:** Board of Governors of the Federal Reserve System, International Finance Discussion Papers 1068, Dec 2012; [page](https://www.federalreserve.gov/pubs/ifdp/2012/1068/ifdp1068.htm) (opened 2026-11-17 R228 via web-fetch; first ~40k of ~141k characters read verbatim, rest summarised by the fetch tool, so regression coefficients are UNVERIFIED).
- **Data/design:** JPY, GBP, EUR vs USD, Jan 2000 - Dec 2011; monthly currency depreciation; currency variance risk premium (JP Morgan OTC ATM implied vol minus realized variance from daily returns) and stock variance risk premium; horizons 1, 3, 6 months; EUR run separately; no transaction costs seen in the verbatim part.
- **Finding (abstract, verbatim):** appreciation "is predictable by the currency variance risk premium at a medium 6-month horizon" and "by the stock variance risk premium at a short 1-month horizon".
- **Relevance:** **None** for a pre-registrable EUR/USD item: 1-6 month horizons (below the R090 power floor on dev), and FX implied volatility is not in the repo or a proven runner download (EVZ already searched R223). **Status:** VERIFIED (partial verbatim read).

### Guyard & Deriaz (2024), "Predicting Foreign Exchange EUR/USD direction using machine learning" (added 2026-11-17 R228)
- **Venue:** arXiv 2409.04471 (Sep 2024, rev. Oct 2024); [RePEc abstract page](https://econpapers.repec.org/paper/arxpapers/2409.04471.htm) (opened 2026-11-17 R228: abstract only; full PDF not fetched).
- **Finding (abstract, verbatim):** "prediction accuracy of 58.52% for one-day ahead forecasts", "an annual return of 32.48% for the year 2022" (PCA feature sets, stacked meta-estimators). Sample period, features and costs not in the abstract (UNVERIFIED).
- **Relevance:** **Low.** Fitted multi-model ML on daily direction with a single-year return; overlaps the daily ML/lag family already tested (E050 Markov switching, E051 random forest, both NONE on dev) and has no published mechanism or pre-registrable feature list. **Status:** VERIFIED (abstract only).

### Shah (2024), "Combining Regression Price Channels and Directional Indicator for Unleveraged Mean-Reversion Strategy in Forex" (added 2026-11-17 R229)
- **Venue:** HKUST CSE COMP 4971C independent-study report (student work, supervisor D. Rossiter, Spring 2024; not peer-reviewed); [PDF](https://cse.hkust.edu.hk/~rossiter/independent_studies_projects/channels_aroon_fx/COMP4971C_channels_aroon_arya.pdf) (opened 2026-11-17 R229 via web-fetch, full text).
- **Data/design:** hourly Yahoo Finance data, EUR/USD, GBP/USD, AUD/USD, CAD/USD, JPY/USD, 20 May 2022 - 20 May 2024; linear-regression price channel (+/- k SD) mean reversion with stop loss, Aroon filter ("AU > 70 AND AD < 30"), final version long-only; fee level not stated in the readable text; all parameters grid-searched (625 combinations plus Aroon lookbacks) on the same 2-year window that is reported, no holdout.
- **Finding (verbatim):** the strategy "comes short when facing downtrends"; reported EUR/USD long-only MAR 2.518 (in-sample). Internal figures for CAD/USD are inconsistent between sections.
- **Relevance:** **None** for a pre-registrable EUR/USD item: in-sample grid-search selection, short single-regime window, long-only design that relies on the 2022-2024 drift, unquantified costs, not peer-reviewed. **Status:** VERIFIED (full text read via fetch tool).

### Fossati & Lu (2025), "Exchange Rate Predictability and Financial Conditions" (added 2026-11-17 R230)
- **Venue:** University of Alberta Economics Working Paper 2025-06 (Sep 2025); [PDF](https://sites.ualberta.ca/~econwps/2025/wp2025-06.pdf) (opened 2026-11-17 R230 via web-fetch; first ~40k of ~71k characters verbatim, remainder tool summary).
- **Data/design:** weekly (Wednesday) log changes of nine USD rates incl. EUR, predictor = Chicago Fed NFCI (real-time vintages); 520-week rolling OLS / quantile regressions; OOS 2000-2021; horizons 1 day, 1 week, 4 weeks; no transaction costs seen.
- **Finding (verbatim):** "none of the alternative forecasts outperforms the RW benchmark in terms of the OOS point forecasts"; "the NFCI does not provide a strong signal about the direction of exchange rate movements but rather about the level of uncertainty." Gains are in density (log score) forecasts only.
- **Relevance:** **None** for a directional EUR/USD item (no point/direction predictability); at most a volatility/sizing input, already covered by E008 (vol timing). **Status:** VERIFIED (partial verbatim read).

### Bianchi, Bigio & Engel (2021, rev. 2023), "Scrambling for Dollars: International Liquidity, Banks and Exchange Rates" (added 2026-11-17 R230)
- **Venue:** NBER Working Paper 29457; [PDF](https://nber.org/system/files/working_papers/w29457/w29457.pdf) (opened 2026-11-17 R230 via web-fetch; first ~40k of ~255k characters verbatim, remainder tool summary).
- **Data/design:** monthly, Feb 2001 - Jul 2021, G10 currencies with focus on the euro; regression of the same-month exchange-rate change on the change in US banks' liquidity ratio (reserves + Treasuries/agencies over short-term funding).
- **Finding (verbatim):** "an increase in the dollar funding risk leads to a rise in the convenience yield and an appreciation of the dollar"; regressions are explicitly contemporaneous ("how changes in the balance sheet between t - 1 and t contribute to changes in the exchange rate between t - 1 and t"). Euro OLS coefficient 0.227 (t 4.84) per the tool summary (UNVERIFIED verbatim).
- **Relevance:** **None** for a pre-registrable item: contemporaneous monthly relation, no lagged or out-of-sample test, below the R090 power floor. **Status:** VERIFIED (partial verbatim read).


### Andersen & Bondarenko (2014), "VPIN and the flash crash" (added 2026-11-17 R232)
- **Venue:** Journal of Financial Markets 17, 1-46; DOI [10.1016/j.finmar.2013.05.005](https://doi.org/10.1016/j.finmar.2013.05.005); [IDEAS abstract page](https://ideas.repec.org/a/eee/finmar/v17y2014icp1-46.html) (opened 2026-11-17 R232 via web-fetch: abstract only, full text paywalled).
- **Data/design:** not on the abstract page (UNVERIFIED). Re-examines the claim that VPIN (volume-synchronised probability of informed trading) predicts short-run volatility.
- **Finding (abstract, verbatim):** VPIN is "a poor predictor of short run volatility"; its predictive content "is due primarily to a mechanical relation with the underlying trading intensity."
- **Relevance:** **None** for a directional EUR/USD item: a volatility (not direction) measure whose volatility content is itself disputed; tick-volume intensity already tested (E033). **Status:** VERIFIED (abstract only).

### Fenn, Howison, McDonald, Williams & Johnson (2008), "The Mirage of Triangular Arbitrage in the Spot Foreign Exchange Market" (added 2026-11-17 R232)
- **Venue:** arXiv [0812.0913](https://arxiv.org/pdf/0812.0913) (v1, Dec 2008; opened 2026-11-17 R232 via web-fetch, full text).
- **Data/design:** second-by-second executable HSBC quotes, triangles {EUR/USD, USD/CHF, EUR/CHF} and {EUR/USD, USD/JPY, EUR/JPY}, main sample Oct 2005 (about four weeks); frequency, duration and size of triangular mispricings plus fill-probability trading simulations with costs.
- **Finding (verbatim):** "triangular arbitrage opportunities do exist, but that most have short durations and small magnitudes"; "the foreign exchange market appears internally self-consistent." About 60% of opportunities last 1 second or less. No test of later EUR/USD direction.
- **Relevance:** **None**: sub-second horizon, far below the repo's 5-minute bars and tradable horizon; no directional result. **Status:** VERIFIED (full text read via fetch tool).

### Iyke, Phan & Narayan (2022), "Exchange rate return predictability in times of geopolitical risk" (added 2026-11-17 R233)
- **Venue:** International Review of Financial Analysis 81, 102099; DOI [10.1016/j.irfa.2022.102099](https://doi.org/10.1016/j.irfa.2022.102099); [IDEAS abstract page](https://ideas.repec.org/a/eee/finana/v81y2022ics1057521922000692.html) (opened 2026-11-17 R233 via web-fetch: abstract only, full text subscriber-only, not opened).
- **Data/design:** 17 countries; data frequency, currency list (EUR/USD inclusion), GPR index version, horizon and cost treatment not on the abstract page (all UNVERIFIED).
- **Finding (abstract, verbatim):** geopolitical risk "predicts 10 out of 17 (59%) exchange rate returns in in-sample tests while in out-of-sample tests predictability is found for 88% of currencies"; the model "delivers excess profits relative to the benchmark model in 11 out of 17 (65%) currencies."
- **Relevance:** **Not usable yet**: frequency and EUR/USD coverage unverified; the related Salisu-Lasisi-Tchankam GPR paper opened alongside ([UP repository PDF](https://repository.up.ac.za/bitstream/handle/2263/86857/Salisu_Historical_2022.pdf?sequence=1), stock indices, monthly GPR, 6-24 month horizons, no FX) suggests the GPR literature works at monthly frequency, below the R090 power floor. **Status:** VERIFIED (abstract only).

### Rambaldi, Pennesi & Lillo (2015), "Modeling FX market activity around macroeconomic news: a Hawkes process approach" (added 2026-11-17 R233)
- **Venue:** arXiv [1405.6047](https://arxiv.org/abs/1405.6047) (Phys. Rev. E 91, 012819 per arXiv metadata; abstract and PDF opened 2026-11-17 R233 via web-fetch, PDF ~55% verbatim).
- **Data/design:** EBS EUR/USD, EUR/JPY, USD/JPY best-quote changes, 100 ms, 2012 (250 days), 07:30-16:30 UTC; Hawkes model of quote-change intensity with a news kernel (723 scheduled announcements).
- **Finding (verbatim):** "a large part of the activity is explained by the self-exciting mechanism"; the model "is able to capture the increase of trading activity after the news". Activity only, no direction or trading rule.
- **Related:** Lallouache & Challet, arXiv [1406.3967](https://arxiv.org/abs/1406.3967) (opened, full text): EBS EUR/USD trade arrivals Q1 2012; Hawkes fits pass significance tests only "for fitting an hour at a time", longer periods fail from non-stationarity. No direction.
- **Relevance:** **None** for a directional item: intensity/activity models; post-news activity already covered by the release-time family. **Status:** VERIFIED.

### Schmidt, Silvestrini & Szczerbowicz (2026), "Federal Reserve shocks: which securities really flow?" (added 2026-11-17 R234)
- **Venue:** Banque de France Working Paper 1040, April 2026; [PDF](https://www.banque-france.fr/system/files/2026-04/WP1040.pdf) (opened 2026-11-17 R234 via web-fetch; first ~45% verbatim, rest summarised by the fetch tool).
- **Data/design:** monthly US TIC cross-border securities flows by investor and asset class, March 1994 - June 2019; FOMC shocks split into pure policy and central-bank-information shocks; local projections over 12 months.
- **Finding (verbatim):** "much of the observed capital inflows into the US is actually due to US investors repatriating funds from foreign equities"; "a 100 basis-point monetary tightening leads to a cumulative repatriation of roughly $2.4 billion in foreign equities over nine months."
- **Relevance:** **None** for a directional item: TIC used as a monthly flow series, not as a release event; no exchange-rate return or release-window test. **Status:** VERIFIED (partly summarised).

### Simpson, Ramchander & Chaudhry (2005), "The impact of macroeconomic surprises on spot and forward foreign exchange markets" (added 2026-11-17 R234)
- **Venue:** Journal of International Money and Finance 24(5), 693-718; DOI [10.1016/j.jimonfin.2005.04.005](https://doi.org/10.1016/j.jimonfin.2005.04.005); [FGCU record page](https://scholarscommons.fgcu.edu/esploro/outputs/journalArticle/The-impact-of-macroeconomic-surprises-on/99384088378506570) (opened 2026-11-17 R234, abstract only; full-text PDF refused by fetch permission, not opened).
- **Finding (abstract):** surprises in 23 announcement types; "exchange rates respond to announcements related to consumer demand, inflation, and interest rates, but not to the announcements directly related to the general strength of the economy"; Treasury budget, trade balance and capacity utilization strongest. Whether TIC is among the 23 and whether any post-announcement drift is found: UNVERIFIED.
- **Relevance:** **Low**: contemporaneous response study; release-time drift family already covered (Chaboud et al. 2004, R219). **Status:** VERIFIED (abstract only).

### Afonso, Furceri & Gomes, "Sovereign credit ratings and financial markets linkages: application to European data" (added 2026-11-17 R235)
- **Link:** [UC3M author PDF](https://www.eco.uc3m.es/~pgomes/Papers/Pub_JIMF_RatingsEuro.pdf) (opened, read in full via fetch agent). Year and journal are not printed in the PDF; file name suggests JIMF: venue/DOI UNVERIFIED.
- **Design:** daily 10-year yield spreads over Germany, 5-year CDS spreads and national equity indices, 24 EU countries, January 1995 - October 2010; [-1,1] event windows, panel regressions, persistence regressions.
- **Finding:** "the reaction of EU spreads to credit rating events is clear and quick (within one to two days)"; downgrades keep spreads higher for up to ~6 months. Exchange rates are not studied.
- **Relevance:** **None** for a directional EUR/USD item (no FX test). **Status:** VERIFIED.

### Mo Ka Lok (HKUST COMP 4971C student report, 2021-22), "Analysis of Trading with Harmonic Patterns in US Stock, Forex, and Crypto Market" (added 2026-11-17 R235)
- **Link:** [HKUST PDF](https://cse.hkust.edu.hk/~rossiter/independent_studies_projects/trading_harmonic_patterns/trading_harmonic_patterns.pdf) (opened; last ~25% only summarised by fetch agent).
- **Design:** hourly Dukascopy SPY, EUR/USD, BTC/USD, 2017-09-01 to 2021-09-01; no commission; no out-of-sample split found.
- **Finding:** "the occurrence of these patterns is not high in general, which results in low profitability"; EUR/USD bullish Gartley ~3 signals/year, best CAGR 0.86%.
- **Relevance:** **None**: student report, in-sample, no costs, signal too rare for the R090 power floor. **Status:** VERIFIED (partly summarised).

### Zhalgasbek (2023), "Analysis of Elliott Wave Theory on Time-Series Data from Forex" (Nazarbayev University capstone/master's thesis) (added 2026-11-17 R235)
- **Link:** [NU repository record](https://nur.nu.edu.kz/handle/123456789/7226) (record page opened; PDF access restricted, not read).
- **Finding (abstract):** "the patterns identified by the Elliott wave theory did not have statistically significant predictive power for daily exchange rates of currencies." Pairs, sample and costs UNVERIFIED.
- **Relevance:** **None** (negative, daily, pairs unknown). **Status:** VERIFIED (abstract only).

### Orquín-Serrano (2020), "Predictive Power of Adaptive Candlestick Patterns in Forex Market. Eurusd Case", Mathematics 8(5), 802 (added 2026-11-17 R236)
- **Link:** [DOAJ record](https://doaj.org/article/9c856e1e9fa24613a25dd669aee0ce1c), doi:10.3390/math8050802 (record/abstract opened; full text not read).
- **Design (abstract):** EUR/USD only; adaptive candlestick patterns and supervised-learning variants using up to 24 preceding candles; out-of-sample evaluation with transaction costs. Frequency and sample UNVERIFIED.
- **Finding:** "No net positive average returns are found in any case after taking into account transaction costs."
- **Relevance:** **None** for a new item: negative after costs, same candlestick/fitted-ML family already NONE (engulfing R142, E050/E051). **Status:** VERIFIED (abstract only).

### Anderson & Faff (2008), "Point and Figure charting: A computational methodology and trading rule performance in the S&P 500 futures market", IRFA 17(1), 198-217 (added 2026-11-17 R236)
- **Link:** [RePEc record](https://ideas.repec.org/a/eee/finana/v17y2008i1p198-217.html) (record opened; no abstract shown; full text subscriber-only, not read).
- **Design:** S&P 500 futures only; no FX test. Frequency, costs and findings UNVERIFIED.
- **Relevance:** **None** (no FX evidence). **Status:** VERIFIED (bibliographic record only).

### Ornelas & Maaud, "Implied Volatility Term Structure and Exchange Rate Predictability", Banco Central do Brasil WP 492 (year UNVERIFIED) (added 2026-11-17 R237)
- **Link:** [BCB PDF](https://www.bcb.gov.br/pec/wps/ingl/wps492.pdf) (opened; first ~half read verbatim, rest only via fetch summary).
- **Design:** predictor is the slope of the OTC **FX** option implied-volatility term structure (ATM, 10-delta tails) vs USD, developed and EM currencies; daily data, overlapping 3- and 6-month holding periods, lagged slope, Hansen-Hodrick t-stats; in-sample regressions plus cross-sectional slope-sorted portfolios. Sample period UNVERIFIED (dates dropped in extraction). Out-of-sample test not seen in the read text.
- **Finding:** "For developed countries a steep term structure means negative future returns" (significance mainly on the right-tail slope).
- **Relevance:** **None** for a new item: equity implied vol (VSTOXX/VIX) is not tested as a predictor; horizon 3-6 months (below the R090 power floor at our sample length); needs OTC FX implied vols not in the pipeline. **Status:** VERIFIED (partial full text).

### Nippani, "Arbitrage Opportunities in Dollar Trading Due to Unexpected Political Events: An Empirical Note", Journal of Accounting and Finance 16(5), 2016, pp. 11-19 (added 2026-11-17 R238)
- **Link:** [articlegateway PDF/text](https://articlegateway.com/index.php/JAF/article/download/1048/990) (opened, read in full via web-fetch).
- **Design:** daily Bloomberg closes 2013-01-01 to 2013-12-31 (N = 261); DXY, EUR/USD, GBP/USD; dummies for the October 2013 US shutdown (1-16 Oct) and 17 Oct 2013 (day after the debt-ceiling deal). One episode only; no intraday data; no costs; trading suggestions untested.
- **Finding:** shutdown period not significant; on the day after the deal "the dollar index did drop significantly on October 17, 2013" (EUR/USD up). Single same-day event, no multi-day drift examined.
- **Relevance:** **None** for a new item (one 2013 event, no drift test, US debt-ceiling resolutions in dev 2016-2020 too few for the R090 power floor). **Status:** VERIFIED.

### Rosa, "The Financial Market Effect of FOMC Minutes", FRBNY Economic Policy Review, December 2013, pp. 67-81 (added 2026-11-17 R239)
- **Link:** [FRBNY PDF](https://www.newyorkfed.org/medialibrary/media/research/epr/2013/0913rosa.pdf) (opened, read via web-fetch).
- **Design:** five-minute data January 2005 to March 2011; 2y/10y Treasury yields, E-mini S&P 500, EBS USD vs EUR, CHF, JPY (with volume); window one hour before to two hours after the 14:00 ET minutes release vs matched control days. No surprise measure, so no direction (sign) of the FX response is estimated.
- **Finding:** volatility and volume rise at release; elevated "up to roughly one hour after the announcement"; EUR volume about four times non-event days; "The asset price response to the minutes has declined since 2008,".
- **Relevance:** **None** for a new item: volatility/volume only, no directional or drift result; FOMC minutes are 8 per year (~40 dev 2016-2020 dates, below the R090 power floor). **Status:** VERIFIED.

### Levich & Potì, "Predictability and 'Good Deals' in Currency Markets", working version 29 Sep 2013, "Forthcoming in the International Journal of Forecasting" (published venue details UNVERIFIED) (added 2026-11-17 R240)
- **Link:** [Uniba repository PDF](https://ricerca.uniba.it/retrieve/1d6a7e28-5ed3-4451-b179-c28eefbbd176/Levich-Poti_FXPredictability_GoodDeals_Final_130929.pdf) (opened via web-fetch; ~42% verbatim: abstract, Sections 1-4, start of Section 5; tables not read).
- **Design:** six majors vs USD (AUD, CAD, JPY, GBP, CHF, ECU/EUR; ECU basket before 1999), daily and monthly Bloomberg 6pm London rates, 1971-2012 (extended to Aug 2013); ARMA/AR(5) predictive models, in-sample R² compared with a "no good-deal" bound; a variance-scaled "rational trading rule" for Sharpe ratios.
- **Finding:** "predictability exceeds this bound during recurring albeit short-lived episodes"; "periods of high and low predictability tend to alternate"; "Transaction costs can explain much of the daily excess-predictability but not monthly excess-predictability"; at 5 bp "the SRs of daily strategies are negative for all currencies."
- **Relevance:** **None** for a new item: daily predictability does not survive 3-5 bp costs; the monthly result is below the R090 power floor at our sample length; fitted lagged-return models already NONE on dev (E051). **Status:** VERIFIED (partial full text).

### Tokar & Horvath, "Market inefficiency identified by both single and multiple currency trends", arXiv:1110.2612 (2011) (added 2026-11-17 R240)
- **Link:** [arXiv](https://arxiv.org/abs/1110.2612) (opened, read essentially in full via web-fetch).
- **Design:** OANDA EUR/USD ticks 2004-2009 resampled to 1 minute; sign-of-trend variables over ~100 lookbacks (1 minute to ~2 days); conditional matching statistics vs future shifts over 15/60/240 minutes. In-sample only; no trading rule, no returns, no costs.
- **Finding:** "clear non-suitability of naive trend estimator for the forecast purposes"; "the trend continuation is less good compared to the contrarian strategy of the trend turnover."
- **Relevance:** **None** for a new item: in-sample descriptive statistics without effect sizes in pips or costs; the short-horizon reversal family is already logged (Wiśniewska 2014) and tested. **Status:** VERIFIED.

### PMC7512194 (FX efficiency, multiscale entropy / recurrence quantification) (noted 2026-11-17 R240)
- Not openable (fetch permission timeout after redirect to pmc.ncbi.nlm.nih.gov); title from search result only. **Not cited.** UNVERIFIED.

### Clarida, "Hot Tip: Nominal Exchange Rates and Inflation Indexed Bond Yields", NBER WP 18726 (January 2013) (added 2026-11-17 R241)
- **Link:** [NBER PDF](https://www.nber.org/papers/w18726.pdf) (opened via web-fetch).
- **Design:** daily USD vs GBP, EUR (French/German linkers) and JPY; inflation-indexed bond yields; decomposition of real-rate differentials and risk premium; contemporaneous regressions (sample dates stated inconsistently in text vs regressions).
- **Finding:** "We do not make any inference of cause and effect"; dynamic lagged effects left to future research. No forecasting or out-of-sample exercise, no costs.
- **Relevance:** **None** for a new item: contemporaneous only, no lagged real-yield -> EUR/USD basis; real-yield (TIPS/linker) data are not in the pipeline. **Status:** VERIFIED.

### Canto & Kräussl, "Stock Market Interactions and the Impact of Macroeconomic News - Evidence from High Frequency Data of European Futures Markets", CFS WP 2006/25 (added 2026-11-17 R241)
- **Link:** [CFS PDF](https://gfk-cfs.de/media//06_25.pdf) (opened via web-fetch; ~half read verbatim).
- **Design:** 1-minute DAX, Euro Stoxx 50, FTSE 100 futures, Jul-Aug 2001; VAR with 9 lags. No exchange rates.
- **Finding:** "the spillovers vanish within the next five minutes after a change in any of the futures prices"; "even if some predictive ability can be achieved ... it may still not offset the transaction costs."
- **Relevance:** **None** (equity-only; lead-lag decays within minutes). **Status:** VERIFIED (partial).

### Huth & Abergel, "High Frequency Lead/lag Relationships - Empirical facts", arXiv:1111.7103 (2011/2012) (added 2026-11-17 R241)
- **Link:** [arXiv PDF](https://www.arxiv.org/pdf/1111.7103) (opened via web-fetch).
- **Design:** tick data, CAC40 stocks and European index futures, Mar-May 2010; Hayashi-Yoshida lead/lag in seconds. No FX.
- **Finding:** "We reach 60% of accuracy when forecasting the next midquote variation of the lagger"; "a naive strategy based on market orders cannot make any profit of this effect because of the bid/ask spread."
- **Relevance:** **None** for a new item: seconds-scale equity lead/lag, unprofitable after spread; no FX evidence. **Status:** VERIFIED (abstract verbatim, body partial).

### Fleming, Liu & Nguyen, "Intraday Price Pressure and Order Flow Around U.S. Treasury Auctions", FRBNY Staff Report 1188 (Mar 2026, revised 2026) (added 2026-11-17 R242)
- **Link:** [FRBNY page](https://www.newyorkfed.org/research/staff_reports/sr1188.html), [PDF](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr1188.pdf), DOI [10.59576/sr.1188](https://doi.org/10.59576/sr.1188) (opened via web-fetch; landing page and first ~40k PDF characters verbatim, rest summary-only).
- **Design:** 1-minute on-the-run nominal Treasury coupon yields (GovPX 1991-2000, BrokerTec 2001-2024), 1,684 auctions, six-hour window around auction close. No exchange rates (FX enters only as a foreign-demand proxy).
- **Finding:** "yields rise in the hours before auction and reverse afterward"; total intraday move 0.7-1.2 bp across maturities, smaller in 2015-2024 than 2007-2014. No FX returns, no out-of-sample or trading-cost analysis (the latter per summary of the unread part, UNVERIFIED).
- **Relevance:** **None** for a new item: Treasury-yield price pressure only, no EUR/USD evidence; consistent with the R123 note (no FX evidence for auction days). **Status:** VERIFIED (partial).

### Meisenzahl, Niepmann & Schmidt-Eisenlohr, "The Dollar Channel of Monetary Policy Transmission", FEDS 2025-046 (Jun 2025) (added 2026-11-17 R243)
- **Link:** [PDF](https://www.federalreserve.gov/econres/feds/files/2025046pap.pdf), DOI [10.17016/FEDS.2025.046](https://doi.org/10.17016/FEDS.2025.046) (opened via web-fetch; first ~40k characters verbatim, rest summary-only).
- **Design:** loan-level US leveraged term loans (PitchBook LCD, 6,430 loans, Aug 2011-Dec 2023); ECB surprises from intraday event windows around ECB announcements (Altavilla et al. 2019). Outcome is US loan-spread flexes, not exchange rates.
- **Finding:** "This paper documents a new dollar channel that transmits monetary policy across borders." No test of bank-lending-survey (SLOOS / ECB BLS) releases; no EUR/USD return forecast.
- **Relevance:** **None** for a new item (found while searching for bank-lending-survey release effects on EUR/USD). **Status:** VERIFIED (partial).

### Ostry, "Tails of Foreign Exchange-at-Risk (FEaR)", Janeway Institute WP 2311 / CWPE 2343 (7 Jun 2023) (added 2026-11-17 R245)
- **Link:** [PDF](https://www.janeway.econ.cam.ac.uk/working-paper-pdfs/jiwp2311.pdf) (opened via web-fetch; ~180k of ~200k characters verbatim, appendices not read).
- **Design:** monthly 1986-2020, G-10 vs USD (DEM before 1999, EUR after), quantile regressions of overlapping 3-month FX changes on the interest differential; in-sample, block-bootstrap CIs.
- **Finding:** "interest differentials predict high-yield currencies to suffer depreciations ten times as large as suggested by UIP". No daily/intraday horizon, no out-of-sample or trading-cost test (in the text read).
- **Relevance:** **None** for a new item (found while searching for USD funding-stress -> EUR/USD): monthly/3-month tail predictability, far below the lesson-R090 power floor on dev at that horizon. **Status:** VERIFIED (partial).

### Ballensiefen, Somogyi & Winterberg, "Demand for Dollars: Evidence from Survey Expectations", CFR WP 26-04 (26 Apr 2026) (added 2026-11-17 R247)
- **Link:** [PDF](https://www.cfr-cologne.de/download/workingpaper/cfr-26-04.pdf) (opened via web-fetch; first ~40k characters verbatim, later sections summary-only, last ~14k not read).
- **Design:** monthly panel, nine G10 currencies vs USD incl. EUR, Sep 2012-May 2025 (return local projection from Dec 1994); Consensus Economics FX forecasts at 3/12/24-month horizons; currency and time fixed effects; no out-of-sample or trading-cost test found.
- **Finding:** "forward-looking expectations accurately predict both currency returns and flows"; once flows are controlled, "currency flows subsume the predictive content of exchange rate forecasts" (verbatim). Short-horizon (3-month) forecasts have limited predictive power (summary).
- **Relevance:** **None** for a new item (found while searching for consensus FX forecasts -> EUR/USD): monthly/24-month horizon, in-sample panel, and Consensus Economics data is not in the pipeline. **Status:** VERIFIED (partial).

### Pyun, "The Wikipedia effect: Analyzing investor attention for strategic investment decisions", Economics Letters 241, 2024 (added 2026-11-17 R248)
- **Link:** [IDEAS](https://ideas.repec.org/a/eee/ecolet/v241y2024ics0165176524003203.html), doi:10.1016/j.econlet.2024.111836 (abstract page opened via web-fetch; full text not read).
- **Design/finding (abstract):** long-short stock portfolios on changes in Wikipedia page views earn positive abnormal returns; listed equities only.
- **Relevance:** **None** for a new item (found while searching for Wikipedia attention -> EUR/USD): no FX test. **Status:** VERIFIED (abstract only).

### Hervé, Zouaoui & Belvaux, "Noise traders and smart money: Evidence from online searches", Economic Modelling 83, 2019 (added 2026-11-17 R248)
- **Link:** [IDEAS](https://ideas.repec.org/p/hal/journl/hal-02065042.html), doi:10.1016/j.econmod.2019.02.005 (abstract page opened via web-fetch; full text not read).
- **Design/finding (abstract):** 87 French stocks 2008-2018; Wikipedia traffic (smart-investor proxy) vs Google SVI (noise-trader proxy); only noise-trader attention influences returns. Its FX reference (Han-Xu-Yin 2018) is already logged above.
- **Relevance:** **None** for a new item: equities only, no FX test. **Status:** VERIFIED (abstract only).

### "Examining the Return-Volatility Relation for Foreign Exchange: Evidence from the Euro VIX", Journal of Futures Markets, 2012 (added 2026-11-17 R249)
- **Link:** [metatoc abstract page](https://metatoc.com/papers/19126-examining-the-return-volatility-relation-for-foreign-exchange-evidence-from-the-euro-vix) (opened via web-fetch; abstract only, authors and DOI not shown there: UNVERIFIED; the zendy page for doi:10.1002/fut.21582 opened with an empty body, so that DOI is UNVERIFIED).
- **Design/finding (abstract):** euro-currency ETF (FXE) returns vs its option implied-volatility index (EVZ); quantile regressions; the return-implied volatility relation is asymmetric, weaker than for equities and can be positive; abstract reports only **contemporaneous** relations.
- **Relevance:** **None** for a new item (found while searching for EVZ -> EUR/USD returns): no lagged/predictive result, ETF not spot, and EVZ data is not in the pipeline. **Status:** VERIFIED (abstract only; bibliographic details UNVERIFIED).

### Leutert, "The Swiss franc safety premium", Swiss Journal of Economics and Statistics 154:13, 2018 (added 2026-11-17 R250)
- **Link:** [Springer](https://link.springer.com/article/10.1186/s41937-017-0014-7), doi:10.1186/s41937-017-0014-7 (opened via web-fetch; first part of the page read verbatim, the rest summarised).
- **Design/finding:** monthly, 1990-2011; trade-weighted CHF index and EUR/CHF vs S&P 500 / SPI; instrumental-variable (Maggiori-style) and GARCH/DCC conditional covariances; CHF acts as a safe haven in crises with a time-varying safety premium. All tests **contemporaneous**; no EUR/USD analysis, no lagged or out-of-sample forecast.
- **Relevance:** **None** for a new item (found while searching for EUR/CHF safe-haven moves -> next-day EUR/USD): monthly, contemporaneous, no EUR/USD. **Status:** VERIFIED (partial).

### Bush & Stephens, "The Monday effect in the EUR/USD currency pair: Periods of EUR strength and weakness", Journal of Behavioral and Experimental Finance 10, 72-74, 2016 (added 2026-11-18 R251)
- **Link:** [IDEAS](https://ideas.repec.org/a/eee/beexfi/v10y2016icp72-74.html), doi:10.1016/j.jbef.2016.03.003 (IDEAS abstract page opened via web-fetch; full text not opened).
- **Design/finding (abstract):** EUR/USD over "six different periods"; the Monday effect "varies in periods of EUR strength versus periods of EUR weakness". Sample, frequency, sign, magnitude and significance not given on the page (UNVERIFIED); no out-of-sample or cost test mentioned.
- **Relevance:** **None** for a new item: a regime-dependent in-sample calendar description; Monday cells already scanned on dev (E009), weekend-gap reversal tested (B17/E020 NONE). **Status:** VERIFIED (abstract only).

### Cellini & Cuccia, "Seasonal processes in the Euro-US Dollar daily exchange rate", Applied Financial Economics 24(3), 161-174, 2014 (added 2026-11-18 R251)
- **Link:** [IDEAS](https://ideas.repec.org/a/taf/apfiec/v24y2014i3p161-174.html), doi:10.1080/09603107.2013.870651 (IDEAS abstract page opened via web-fetch; full text subscriber-only, not opened).
- **Design/finding (abstract):** daily EUR/USD 1999-2012; "evidence of the presence of day effects, even if they play a more limited role"; some significant month effects in first differences, strong month variation in variance. Days/months, signs and magnitudes not given (UNVERIFIED); no out-of-sample or trading test.
- **Relevance:** **None** for a new item: in-sample, unnamed cells; day-of-week cells already scanned on dev (E009), month-end windows tested (E034). **Status:** VERIFIED (abstract only).

### Uz Akdogan, "Monetary policy responses to COVID-19 in emerging European economies: measuring the QE announcement effects on foreign exchange markets", Empirica 50(3), 625-655, 2023 (added 2026-11-18 R252)
- **Link:** [Springer](https://link.springer.com/article/10.1007/s10663-023-09578-9), doi:10.1007/s10663-023-09578-9 (article page opened via web-fetch; only part of the text visible, tables not seen).
- **Design/finding:** daily HUF, PLN, TRY vs USD and EUR around domestic central-bank QE announcements in 2020 (3 Hungary, 7 Poland, 1 Turkey); contemporaneous day-0 and 3/7/11-day event windows; qualitative appreciation vs USD in a 3-day window. ECB QE only in the literature review. No EUR/USD event, no drift, predictive, out-of-sample or cost test. Sample dates inconsistent in the text (UNVERIFIED).
- **Relevance:** **None** for a new item: not EUR/USD, contemporaneous only, 11 events. **Status:** VERIFIED (partial text).

### Sun, "Performance of Pairs Trading Strategies Based on Renko and Kagi Charts", University of Warsaw Faculty of Economic Sciences Working Papers No. 20/2025 (483), 2025 (added 2026-11-18 R253)
- **Link:** [WNE UW PDF](https://www.wne.uw.edu.pl/download_file/6099/0) (opened via web-fetch; first ~40k of 184k characters read, rest via model summary; table figures not checked verbatim, UNVERIFIED).
- **Design/finding:** daily S&P 500 and CSI index constituents, log-price spread pairs, 12-month formation / 6-month trading, Renko/Kagi threshold contrarian rule, 0.10%-0.30% costs; positive net monthly means for most indices per the summary. FX pairs mentioned only as examples; no FX or EUR/USD test.
- **Relevance:** **None** for a new item: equity pairs, daily, not a single-pair EUR/USD rule. **Status:** VERIFIED (partial text).

### Holý and Tomanová, "Estimation of Ornstein-Uhlenbeck Process Using Ultra-High-Frequency Data with Application to Intraday Pairs Trading Strategy", arXiv 1811.09312 (added 2026-11-18 R253)
- **Link:** [ar5iv](https://ar5iv.labs.arxiv.org/html/1811.09312) (opened via web-fetch; first ~180k of 483k characters read; empirical profit section not reached).
- **Design/finding:** noise-robust MLE for OU parameters on tick data; seven NYSE oil stocks (21 pairs), 2015-2018; first-passage entry/exit levels. Naive tick MLE overstates reversion speed ~6x. No FX, no out-of-sample split seen, no numeric cost assumption seen.
- **Relevance:** **None** for a new item: equities only; methodological point (microstructure noise inflates apparent mean reversion at tick scale) consistent with SPEC bid/ask costing. **Status:** VERIFIED (partial text).

### Hong and Yogo, "What Does Futures Market Interest Tell Us about the Macroeconomy and Asset Prices?", NBER Working Paper 16712, January 2011, revised June 2012 (added 2026-11-18 R254)
- **Link:** [NBER PDF](https://www.nber.org/system/files/working_papers/w16712/w16712.pdf) (opened via web-fetch; abstract and Sections 3-4 partly read verbatim, the rest via model summary; table coefficients UNVERIFIED).
- **Design/finding:** monthly excess returns; predictor = growth of futures open interest smoothed by a 12-month geometric average; eight currency futures incl. euro from May 1998. Abstract: "To a lesser degree, movements in open interest predict returns in currency, bond, and stock markets." Intro: rising currency market interest "predicts appreciation of a portfolio of foreign currencies relative to the US dollar". Caveat in the text: OTC currency activity is largely outside futures open interest. Out-of-sample and cost evidence not seen (summary says in-sample only; UNVERIFIED).
- **Relevance:** **None** for a new item: monthly horizon (~72 dev months), a foreign-currency portfolio not EUR/USD alone, in-sample, and CME open-interest data are not in the pipeline. **Status:** VERIFIED (partial text).

### Dobrev and Schaumburg, "High-Frequency Cross-Market Trading: Model Free Measurement and Applications", working paper, version 2018-10-07 (added 2026-11-18 R256)
- **Link:** [Atlanta Fed conference PDF](https://www.atlantafed.org/-/media/documents/news/conferences/2018/1018-financial-stability-implications-of-new-technology/papers/dobrev-schaumburg_high-frequency-cross-market-trading.pdf) (opened via web-fetch; first ~40k of 126k characters verbatim, rest via model summary; EUR/USD figure and regression design UNVERIFIED).
- **Design/finding:** 10y/5y Treasury cash (BrokerTec) vs CME futures, SPY vs E-mini; Jul-Dec 2014 core sample. Abstract (verbatim): "price discovery in US Treasury and equity markets primarily takes place in futures rather than cash markets". Lead-lag peaks at about +/-5 milliseconds (microwave Secaucus-Aurora). Price-impact regressions reported as contemporaneous per the summary; no minute-plus directional strategy, no out-of-sample test, no cost analysis seen. Bund futures not mentioned.
- **Relevance:** **None** for a new item: the cross-market lead is milliseconds, untradeable with 1-minute bars and SPEC 4 costs; no bond-futures data in the pipeline. **Status:** VERIFIED (partial text).

### Cotter and Dowd, "Intra-Day Seasonality in Foreign Exchange Market Transactions", arXiv 1103.5664 (submitted 2011; PDF dated 2007) (added 2026-11-18 R257)
- **Link:** [arXiv abstract](https://arxiv.org/abs/1103.5664), [PDF](https://arxiv.org/pdf/1103.5664) (opened via web-fetch; abstract verbatim, body via model summary).
- **Design/finding:** Reuters D2000-2 DEM/USD (pre-euro), one week 6-10 Oct 1997, 5-minute returns of filled limit and market orders grouped in 3-hour GMT blocks; EVT tail estimates. Abstract: "limit and market orders exhibit seasonality through the variation of their returns and volatility". No minute-of-hour / top-of-hour test, no directional forecast, no trading rule, no out-of-sample design, no costs.
- **Relevance:** **None** for a new item: one week of 1997 DEM/USD, descriptive volatility/tail seasonality only; hour-of-day cells already scanned on dev in E009. **Status:** VERIFIED (partial text).

### Huang, "Financial Trading as a Game: A Deep Reinforcement Learning Approach", arXiv 1807.02787 (2018, NCTU thesis) (added 2026-11-18 R257)
- **Link:** [arXiv abstract](https://arxiv.org/abs/1807.02787) (opened via web-fetch; abstract verbatim, tables via model summary, table values UNVERIFIED).
- **Design/finding:** LSTM deep recurrent Q-network, 12 FX pairs incl. EUR/USD, TrueFX ticks resampled to 15-minute bars, 2012-2017, trained "in a purely online fashion" (no held-out test period). Fixed spread 0.08 bp main case (0.1/0.15/0.2 bp also), no slippage. Reported EUR/USD annualised 9.5% at 0.08 bp, 5.8% at 0.1 bp, 0.1% at 0.15 bp, 1.1% at 0.2 bp; ~31k trades.
- **Relevance:** **None** for a new item: assumed spreads (<= 0.2 bp) are far below the SPEC 4 cost model and the EUR/USD result already falls to ~0 at 0.15 bp; no held-out evaluation; high-turnover 15-minute trading cannot survive SPEC 4 costs; ML-on-lags family already NONE on dev (E051). **Status:** VERIFIED (partial text).

### Baum, Kurov and Wolfe, "What do Chinese macro announcements tell us about the world economy?", Journal of International Money and Finance 59 (2015) 100-122, DOI 10.1016/j.jimonfin.2015.07.002 (added 2026-11-18 R258)
- **Link:** [IDEAS record](https://ideas.repec.org/a/eee/jimfin/v59y2015icp100-122.html), [Skidmore PDF](https://www.skidmore.edu/economics/documents/WhatDoChineseMacroAnnouncementsTellUsAboutTheWorldEconomy.pdf) (opened via web-fetch; abstract and citation verbatim, ~40% of PDF verbatim, rest via model summary; table values UNVERIFIED).
- **Design/finding:** 5-minute futures incl. CME euro FX futures (USD per euro), 30 Sep 2009 - 31 Dec 2013; Bloomberg-consensus surprises; event window 10 minutes before to 10 minutes after release; contemporaneous OLS reaction only. Abstract: "the world markets view strong Chinese output as a rising tide that lifts all boats"; "News about Chinese domestic consumption leaves most markets unaffected." No later-drift test, no out-of-sample design, no costs.
- **Relevance:** **None** for a new item: contemporaneous surprise reaction (needs consensus data not in the repo), effect within ~20 minutes, no drift evidence. **Status:** VERIFIED (partial text).

### Dal Bianco, Camacho and Pérez Quirós, "Short-run forecasting of the euro-dollar exchange rate with economic fundamentals", Banco de España Working Paper 1203 (2012) (added 2026-11-18 R258)
- **Link:** [BdE page](https://www.bde.es/wbe/en/publicaciones/analisis-economico-investigacion/documentos-trabajo/shortrun-forecasting-eurodollar-exchange-rate-with-economic-fundamentals.html) (opened via web-fetch; about half verbatim, rest incl. author list via model summary; claims UNVERIFIED verbatim).
- **Design/finding (summary):** mixed-frequency model of weekly EUR/USD changes on economic fundamentals; out-of-sample forecasts at one week to one month reported to improve significantly on the random walk, including direction of change. No trading costs mentioned; sample period not shown on the page.
- **Relevance:** **None** for a new item now: needs a multi-series real-time macro panel (US and euro-area activity data with release vintages) that is not in the pipeline and has no sanctioned download path on the runner (see B12 FRED blocker); weekly horizon. Could become an item only after a human-approved macro data source. **Status:** VERIFIED (partial text).

### Heimer and Imas, "Doing Less with More" (AEA 2019 preliminary paper) (added 2026-11-18 R259)
- **Link:** [AEA 2019 preliminary paper](https://aeaweb.org/conference/2019/preliminary/paper/st39SEQz) (opened via web-fetch; ~40% verbatim, rest via model summary; pair list and table values UNVERIFIED).
- **Design/finding:** retail forex traders on myForexBook (~480 US, ~589 European, >270,000 trades), 1 Sep - 1 Dec 2010, around the CFTC 50:1 leverage cap (18 Oct 2010); difference-in-differences on per-trade "unlevered returns" (trader market timing), plus a lab experiment. Verbatim: "the reduction in available leverage directly reduces traders' disposition effect by about 13 percent"; "The leverage constraint improves U.S. traders' performance by 1.9 basis points per-trade" (10% level). No exchange-rate return predictability test, no out-of-sample or cost test.
- **Relevance:** **None** for a new item: measures trader behaviour and trader performance, not a predictable EUR/USD price pattern; retail position data are not in the pipeline. **Status:** VERIFIED (partial text).

### Kozhan, Moore and Payne, "Market Order Flows, Limit Order Flows and Exchange Rate Dynamics" (15 June 2012 version) (added 2026-11-18 R259)
- **Link:** [Bank of Canada conference PDF](https://www.bankofcanada.ca/wp-content/uploads/2012/11/Michael-Moore.pdf) (opened via web-fetch; ~2/3 verbatim, tables via model summary; coefficients UNVERIFIED).
- **Design/finding:** Reuters Dealing 3000 tick data, EUR/USD, GBP/USD, EUR/GBP, 2 Jan 2003 - 30 Dec 2004, daily (hourly robustness). Contemporaneous regressions of same-interval returns on market, limit and cancelled order flow; verbatim: "Within an interval, flows of new and cancelled limit orders and price changes are likely to be simultaneously determined." Lagged flow used only as IV instruments. No forecasting, out-of-sample or cost test.
- **Relevance:** **None** for a new item: contemporaneous price impact, not prediction; order-book data are not in the pipeline (1-minute bid/ask bars only). **Status:** VERIFIED (partial text).

### Liu, Ślepaczuk and Tang, "EXFormer: A Multi-Scale Trend-Aware Transformer with Dynamic Variable Selection for Foreign Exchange Returns Prediction" (arXiv 2512.12727, Dec 2025) (added 2026-11-18 R260)
- **Link:** [arXiv 2512.12727v1](https://arxiv.org/html/2512.12727v1) (opened via web-fetch; abstract verbatim, tables via model summary; table values UNVERIFIED).
- **Design/finding:** transformer on daily closing spot log returns for EUR/USD, USD/JPY, GBP/USD, 7 May 2010 - 29 Aug 2024, 80/10/10 time split. Abstract verbatim: "Using the daily data for EUR/USD, USD/JPY, and GBP/USD"; post-cost cumulative returns "7%, 19%, and 9%". Costs 5 bp + 2 bp slippage per position change (summary). The 15-day input window is reported as the best performer, i.e. chosen with test-period outcomes (selection on the test block).
- **Relevance:** **None** for a new item: daily horizon (not the intraday session frame of SPEC), window chosen on the test block, and the ML-on-lagged-returns family is already NONE on dev (E051, B62). **Status:** VERIFIED (partial text).

### Lahaye and Neely, "The Role of Jumps in Volatility Spillovers in Foreign Exchange Markets: Meteor Shower and Heat Waves Revisited" (St. Louis Fed WP 2014-034B, Sep 2016 version) (added 2026-11-18 R262)
- **Link:** [AMSE-hosted PDF](https://www.amse-aixmarseille.fr/sites/default/files/events/2014-034.pdf) (opened via web-fetch; ~39% verbatim, remainder via model summary; R² figures UNVERIFIED).
- **Design/finding:** EUR/USD and USD/JPY 5-minute returns, 5 Jan 1999 - 26 Apr 2013; HAR regressions of realized volatility and jumps across Asian/European/US sessions. Verbatim: "meteor showers contribute 60 percent of explanatory power for realized volatility versus 40 percent for heat waves." Volatility/jump forecasting only; no return-direction, out-of-sample trading or cost test.
- **Relevance:** **None** for a new item: volatility, not direction (session volatility spillovers already covered by the realized-volatility entries). Found via a "geomagnetic storms -> exchange rates" search; no geomagnetic/space-weather FX return study was among the hits. **Status:** VERIFIED (partial text).

### Lenzo (Russell Investments), "The holiday trading effect: Timing, liquidity and investor impact" (12 Nov 2025) (added 2026-11-18 R262)
- **Link:** [Russell Investments research note](https://russellinvestments.com/content/ri/us/en/insights/russell-research/2025/11/holiday-trading-effect.html) (opened via web-fetch, full text).
- **Design/finding:** practitioner note on year-end/holiday liquidity across asset classes; no instruments, frequency or sample stated. FX: volumes "running 30–50% below normal by the second half of the month"; Christmas Eve and Boxing Day "roughly 20% of normal". No return-direction test.
- **Relevance:** **None** for a new item: liquidity/volume only, practitioner note, no EUR/USD price pattern; US early-close days are ~3/yr (~18 dev events, below the R090 floor). **Status:** VERIFIED.

### Kebe and Uhl, "High-Frequency Effects of Novel News on the EURUSD Exchange Rate", Journal of Behavioral Finance 25(2), 194-207, 2024 (added 2026-11-18 R263)
- **Link:** [IDEAS record](https://ideas.repec.org/a/taf/hbhfxx/v25y2024i2p194-207.html), doi:10.1080/15427560.2022.2100386 (abstract only via web-fetch; full text paywalled, not opened).
- **Design/finding (abstract):** >100 million news articles with millisecond timestamps, novel Euro-specific news vs intraday EURUSD returns. Verbatim: "We show a predictive but not contemporaneous relationship between these news and their sentiment and EURUSD returns." Regime change since the GFC; positive sentiment relation strongest in the euro debt crisis. Sample, horizon, out-of-sample design and costs UNVERIFIED.
- **Relevance:** Low for a new item: needs a timestamped news/sentiment feed not in the pipeline; no tradable rule or cost test verified. **Status:** VERIFIED (abstract only).

### Ostry, Lloyd and Corsetti, "Trading blows: The exchange-rate response to tariffs and retaliations" (Bank of England Staff Working Paper No. 1,139, Aug 2025) (added 2026-11-18 R264)
- **Link:** [BoE PDF (wwwtest mirror)](https://wwwtest.bankofengland.co.uk/-/media/boe/files/working-paper/2025/trading-blows-the-exchange-rate-response-to-tariffs-and-retaliations.pdf) (opened via web-fetch, full text read in two parts; figure values not readable, EUR/USD magnitudes UNVERIFIED).
- **Design/finding:** new daily database of effective tariff-rate shocks; local projections on effective USD/EUR indices, bilateral EUR/USD, CNY/CNH and 2y/10y yields. 2018-2020: 46 event days after filtering (35 US, 19 RoW); 2025: 17 event days. Horizons 0-60 business days (2018-2020), 0-24 (2025). Verbatim: unretaliated shock "associated with around 1% appreciation over the four weeks following the event" (per 1pp effective tariff shock); with retaliation "the USD will actually depreciate—both in effective terms and vis-à-vis the euro"; 2025 actions "depreciate the USD, both in effective terms and bilaterally against the EUR". Retaliation is defined as a foreign response within 7 days after the event.
- **Relevance:** Low for a new item: the sign depends on retaliation observed up to 7 days later (look-ahead for a tradable rule); daily, multi-week horizon outside the intraday SPEC frame; the 2018-2020 events fall in dev and were used by the authors (not independent); val (2021-01-21 to 2023-06-30) has no comparable tariff episode, so no val confirmation is possible; the event list is not in the pipeline. **Status:** VERIFIED (text; figures not read).

### Pinter, Smets and Üslü, "Market whiplash after the 2025 tariff shock: an event-targeted VAR approach" (BIS Working Paper 1282, Aug 2025) (added 2026-11-18 R264)
- **Link:** [BIS landing page](https://www.bis.org/publications/working-paper-1282-market-whiplash-after-2025-tariff-shock-event-targeted-var-approach) (landing page opened; PDF fetch failed, not retried; details UNVERIFIED).
- **Finding (landing page):** "the dollar's persistent depreciation and movements in government bond yields largely stem from other orthogonal shocks" (Treasury-market liquidity), not tariff shocks. EUR/USD not mentioned.
- **Relevance:** None for a new item: one 2025 episode (OOS period), no EUR/USD result. **Status:** VERIFIED (landing page only).

### Aldasoro, Beltrán and Grinberg, "Stablecoin flows and spillovers to FX markets" (BIS Working Paper 1340, Mar 2026) (added 2026-11-18 R265)
- **Link:** [BIS landing page](https://www.bis.org/publ/work1340.htm) (landing page opened via web-fetch; 69-page PDF not read; frequency, currency list and lag structure UNVERIFIED).
- **Design/finding (landing page):** four USD-pegged stablecoins vs 27 fiat currencies on 64 exchanges, 2021-2025; granular instrumental variable on net stablecoin inflows. Verbatim: "An exogenous surge in stablecoin demand depreciates the local currency in the traditional spot market"; "a 1% exogenous increase in net stablecoin inflows raises parity deviations by 40 basis points"; emerging-market currencies "are most exposed". No FX magnitude, no out-of-sample or trading/cost test stated; whether EUR is in the sample is not stated.
- **Relevance:** None for a new item: causal (IV) rather than predictive design, emphasis on EM currencies, sample starts 2021 (no dev coverage), exchange-level stablecoin flow data not in the pipeline. **Status:** VERIFIED (landing page only).

### Gnan and Rieder, "The (Not So) Quiet Period: Communication by ECB Decision-makers during Monetary Policy Blackout Days" (CEPR DP15735, 2021, rev. 2022) (added 2026-11-18 R265)
- **Link:** [CEPR page](https://cepr.org/publications/dp15735) (landing page opened via web-fetch; PDF not read).
- **Finding (landing page):** confidential data on ECB quiet-period breaches 2008-2021; breaches "trigger high-frequency market reactions that are up to twice as large as the median market reaction to speeches in inter-meeting periods". No exchange-rate series named; no direction, predictive or cost test.
- **Relevance:** None: breach records are confidential; no FX direction result. **Status:** VERIFIED (landing page only).

### Gerdrup, Hallerud and Maffei-Faccioli, "Macroeconomic News and Exchange Rate Dynamics" (Norges Bank Staff Memo 5/2026, Oct 2026) (added 2026-11-18 R266)
- **Link:** [Norges Bank PDF](https://www.norges-bank.no/contentassets/1da9f16a950d4dba9e5b1f32865cacd5/staff-memo-5-2026-macroeconomic-news.pdf) (opened via web-fetch; text truncated, later sections model-summarised, details UNVERIFIED).
- **Design/finding:** CPI and monetary-policy surprises from daily event windows (30-minute windows as robustness), LSEG tick data from 2002; monthly proxy-SVAR 1999-2025; USDEUR and EURNOK. Abstract: news shocks explain "roughly 70–80 percent of EURNOK forecast-error variance and 60–70 percent of USDEUR". Contemporaneous/structural; the memo states it does not test forecasting. No out-of-sample or cost test found. No German state CPI or equity-open result.
- **Relevance:** None for a new item: variance decomposition, not a predictive or tradable rule; needs a surprise (consensus) calendar, which is the B6 blocker. **Status:** VERIFIED (PDF opened, partly read).

### Cagliesi, Della Bina and Tivegna, "Market Response to News: Rationality and Conformism in an Euro-Dollar Exchange Rate Model" (Univ. of Greenwich CEPGR working paper 2, 2014) (added 2026-11-18 R266)
- **Link:** [Greenwich repository PDF](https://gala.gre.ac.uk/11195/1/CEPGR2_Cagliesi_Bina_Tivegna.PDF) (opened via web-fetch; latter part not read).
- **Design/finding:** EUR/USD at three 8-hour periods per day (CQG), 2003 to Aug 2011, 68 scheduled indicators (Bloomberg surprises: US, euro area, UK, Germany national CPI preliminary). EGARCH(3,1) news model, in-sample only; reported mean reversion: the rate "is expected to revert back by about 20% (18% in the second sub period)" over one day. Forecasting/trading signals mentioned only as future work. No out-of-sample or cost test in the read text. No German state CPI or equity-open result.
- **Relevance:** None for a new item: in-sample, depends on a surprise calendar (B6 blocker); daily-scale reversal of 8-hour moves overlaps the already-tested big-move reversal family (E023/E025 lineage). **Status:** VERIFIED (PDF opened, partly read).

### Salvagnin, Glielmo, De Giuli and Mira, "Investigating the price determinants of the European Emission Trading System: a non-parametric approach" (arXiv 2406.05094, 2024) (added 2026-11-18 R267)
- **Link:** [arXiv PDF](https://arxiv.org/pdf/2406.05094) (opened via web-fetch; text truncated, later part model-summarised, details UNVERIFIED).
- **Design/finding:** daily EUA closing prices Jan 2014 - Apr 2023 (2374 obs); information-imbalance tests Δ(X_t -> EUA_t+δt) with EUR/USD spot and EUR/USD uncertainty among the candidate drivers; carbon price is the target. Abstract: "with the uncertainty in the EUR/CHF exchange rate emerging as a crucial determinant." No test of carbon returns predicting EUR/USD; no out-of-sample or cost test found.
- **Relevance:** None: causal direction is FX -> carbon, the opposite of what a EUR/USD signal needs; EUA prices not in the pipeline. **Status:** VERIFIED (PDF opened, partly read).

### Kloks, "Swap Line Dollar Supply" (University of St. Gallen working paper, 16 Sep 2025) (added 2026-11-18 R268)
- **Link:** [Boston Fed conference PDF](https://www.bostonfed.org/-/media/Documents/events/2025/stress-testing-research-conference/Kloks_SwapLines.pdf) (opened via web-fetch; text truncated after ~40k of 110k characters, later part model-summarised, those details UNVERIFIED).
- **Design/finding:** daily CLS FX-swap settlement data Jan 2012 - Jun 2022, 17 USD pairs incl. EUR/USD, 8 tenors; IV design using pre-set swap-line auction days; finding (verbatim): "a one–standard-deviation decline in net U.S. dollar demand reduces the effective spread by 0.7 bps on average." Studies FX-swap spreads and order flow, contemporaneous and COVID event window; no forecast of spot EUR/USD returns, no out-of-sample or strategy cost test.
- **Relevance:** None for a new item: swap-market pricing, not spot direction; CLS swap data not in the pipeline. **Status:** VERIFIED (PDF opened, partly read).

### Bettendorf and Jochem, "TARGET balances in the euro area: the case of Germany" (Applied Economics 55(29), 2023, doi:10.1080/00036846.2022.2114993) (added 2026-11-18 R268)
- **Link:** [IDEAS/RePEc abstract](https://ideas.repec.org/a/taf/applec/v55y2023i29p3317-3328.html) (abstract opened; full text paywalled, body UNVERIFIED).
- **Design/finding:** BVAR identifying drivers of Germany's TARGET claims (monetary policy, euro-area risk, global risk); 2015-2017 flows attributed largely to monetary policy. No exchange-rate variable or prediction test.
- **Relevance:** None: not an FX study; TARGET2 balances are monthly and not in the pipeline. **Status:** VERIFIED (abstract only).

### Lengyel and Giuliodori, "Demand Shocks for Public Debt in the Eurozone" (DNB Working Paper 674, Mar 2020) (added 2026-11-18 R269)
- **Link:** [DNB landing page](https://www.dnb.nl/en/publications/research-publications/working-paper-2020/674-demand-shocks-for-public-debt-in-the-eurozone) and [PDF](https://www.dnb.nl/media/g5slxapq/working-paper-no-674_tcm47.pdf) (opened via web-fetch; PDF truncated, back half model-summarised, details UNVERIFIED).
- **Design/finding:** 1-minute German and Italian government bond futures around Treasury auctions (Germany 536, Italy 247 auctions, 1999-2017) identify auction demand shocks; daily outcomes are sovereign yields, CDS, equity and corporate bond indices. No exchange-rate variable in the abstract or read sections.
- **Relevance:** None: no FX test of euro-area bond auctions. **Status:** VERIFIED (page and PDF opened, partly read).

### Bräuer and Hau, "Can Time-Varying Currency Risk Hedging Explain Exchange Rates?" (BIS/BdI/ECB conference paper, 21 Nov 2022) (added 2026-11-18 R269)
- **Link:** [BIS PDF](https://www.bis.org/events/221213_bis_bdi_ecb_exchange_rates/paper_brauer.pdf) (opened via web-fetch; truncated after ~40k of 88k characters, later part model-summarised, those details UNVERIFIED).
- **Design/finding:** monthly Sep 2012 - Mar 2022; CLS fund forward/swap positions as hedging pressure, US TIC positions; EUR, GBP, JPY, CHF, CAD, AUD, NZD vs USD. Verbatim: "The contemporaneous relationships are economically and statistically significant at various frequencies (i.e. quarterly, monthly, weekly, daily)." In-sample VAR: dollar response to a hedging-pressure shock "peaks after 5 months". No out-of-sample forecast or cost test; lagged regressors reportedly not significant (summary, UNVERIFIED).
- **Relevance:** None for a new item: contemporaneous/monthly, CLS positioning data not in the pipeline. **Status:** VERIFIED (PDF opened, partly read).

### Heiden, Klein and Zwergel, "Beyond Fundamentals: Investor Sentiment and Exchange Rate Forecasting" (European Financial Management 19(3), 2013, pp. 558-578, doi:10.1111/j.1468-036X.2010.00593.x as listed) (added 2026-11-18 R270)
- **Link:** [EconPapers abstract](https://econpapers.repec.org/RePEc:bla:eufman:v:19:y:2013:i:3:p:558-578) (abstract opened via web-fetch; full text paywalled, body UNVERIFIED; DOI year 2010 vs issue 2013 not checked, DOI UNVERIFIED).
- **Design/finding (abstract):** EUR/USD only; private and institutional investor sentiment surveys; institutional sentiment predicts medium-term EUR/USD returns, private-investor sentiment contrarian but unstable and sample-dependent; a simple out-of-sample trading strategy is reported significant. Data frequency, survey source and transaction costs not stated in the abstract (UNVERIFIED).
- **Relevance:** Low for a new item: medium-term horizon, survey data (source UNVERIFIED) not in the pipeline; survey-release angle already searched in R183 with no study found. **Status:** VERIFIED (abstract only).

### Han, Wan and Xu, "Can the Baltic Dry Index predict foreign exchange rates?" (Finance Research Letters 32, 2020, doi:10.1016/j.frl.2019.04.014) (added 2026-11-18 R270)
- **Link:** [IDEAS/RePEc abstract](https://ideas.repec.org/a/eee/finlet/v32y2020ics1544612318307876.html) (abstract opened via web-fetch; full text paywalled, body UNVERIFIED).
- **Design/finding (abstract):** 14 major currencies vs USD (EUR inclusion not confirmed on the page); panel regression finds significant long-run predictability, a BDI rise going with currency depreciation; individual regressions in- and out-of-sample, "inverted U-shaped predictive pattern". Frequency and costs not stated; no trading test in the abstract.
- **Relevance:** None for a new item: long-run horizon, no cost/strategy test, BDI not in the pipeline; BDI as a lagged daily predictor already appears in the daily-predictor study logged above (line with "Baltic Dry Index"). **Status:** VERIFIED (abstract only).

### Dao, McGroarty and Urquhart, "The Brexit vote and currency markets" (Journal of International Financial Markets, Institutions and Money 59, 2019, pp. 153-164, doi:10.1016/j.intfin.2018.11.004) (added 2026-11-18 R271)
- **Link:** [EconPapers abstract](https://econpapers.repec.org/RePEc:eee:intfin:v:59:y:2019:i:c:p:153-164) (abstract opened via web-fetch; full text not opened, body UNVERIFIED).
- **Design/finding (abstract):** event study of the Brexit vote on intraday correlation and volatility transmission among CHF, JPY, GBP, EUR and gold; correlation of safe havens with GBP and EUR falls, GBP-EUR volatility transmission drops. Sample, interval and quote pairs not stated on the page (EUR/USD inclusion UNVERIFIED).
- **Relevance:** None for a new item: one event, correlation/volatility only, no return-direction or cost test. **Status:** VERIFIED (abstract only).

### Istrefi, Odendahl and Sestieri, "How policymakers' speeches and interviews move markets" (ECB Blog, 24 Sep 2026) (added 2026-11-18 R271)
- **Link:** [ECB Blog](https://www.ecb.europa.eu/press/blog/date/2026/html/ecb.blog20260924~3240af33dc.en.html) (opened via web-fetch; page partly truncated; full author list UNVERIFIED, metadata names Sestieri).
- **Design/finding (as extracted, not verbatim):** 1999 - early 2024, 304 formal announcements and ~5,000 inter-meeting communication events; contemporaneous intraday reactions (90-minute speech windows, 15-minute other windows) of 1-year OIS and other assets; EUR/USD in the variable set but no separate EUR/USD result; no return-forecast, OOS or cost test.
- **Relevance:** None for a new item: contemporaneous reaction only, and no historical ECB speech-time calendar in the pipeline. **Status:** VERIFIED (blog, partly read).

### Huther, Pettit and Wilkinson, "Fiscal Flow Volatility and Reserves" (FEDS Notes, Federal Reserve Board, 16 Dec 2019) (added 2026-11-18 R272)
- **Link:** [FEDS Note](https://www.federalreserve.gov/econres/notes/feds-notes/fiscal-flow-volatility-and-reserves-20191216.html) (opened via web-fetch).
- **Design/finding:** daily TGA balances 1995-2005 and average absolute weekly changes of TGA/reserves/bills/repo 2003-2019; TGA weekly changes "less than $1 billion" pre-crisis vs ~$24bn (2010-2018) and ~$35bn (Mar 2018 - Sep 2019). Descriptive only.
- **Relevance:** None for a new item: no exchange-rate, return, OOS or cost analysis; tax-date events too few on dev. **Status:** VERIFIED.

### Yuan and Gupta, "Chinese Lunar New Year effect in Asian stock markets, 1999-2012" (Quarterly Review of Economics and Finance, 2014, doi:10.1016/j.qref.2014.06.001) (added 2026-11-18 R272)
- **Link:** [Griffith PDF (in-press copy)](https://news.griffith.edu.au/wp-content/uploads/2014/09/CLNY-Effect.pdf) (opened via web-fetch; first ~2/3 read verbatim, rest only as extracted summary).
- **Design/finding:** daily index returns of seven Asian equity markets, Sep 1999 - Mar 2012, ARMA(1,1)-GARCH(1,1) with 3-day pre/post holiday dummies; significant pre-holiday returns (e.g. Korea 0.68%, Japan 0.49%, Hong Kong 0.47%). Trading-rule/cost results UNVERIFIED (later part not read verbatim). No FX test, no OOS.
- **Relevance:** None for a new item: equities only, ~6 dev events for EUR/USD. **Status:** VERIFIED (partly read).

### Borner, "Central bank information and pure monetary policy surprises in Switzerland" (SNB Working Paper 2025-01, 22 Jan 2025) (added 2026-11-18 R273)
- **Link:** [SNB WP 2025-01 landing page](https://www.snb.ch/de/publications/research/working-papers/2025/working_paper_2025_01) (opened via web-fetch; abstract/metadata only, PDF not read).
- **Design/finding:** 30-minute event windows around SNB policy announcements; interest-rate futures, stock market and exchange rates; sign-restriction split into pure policy vs central-bank-information surprises; abstract (verbatim fragment): "these effects differ from each other only for the exchange rates and stock market responses". Currencies and sample UNVERIFIED (PDF not read). Contemporaneous only; no EUR/USD return-forecast, OOS or cost test in the abstract.
- **Relevance:** None for a new item: contemporaneous CHF reaction, ~4 SNB decisions/yr (below the R090 floor on dev). **Status:** VERIFIED (abstract only).

### Ito, Lyons and Melvin, "Is There Private Information in the FX Market? The Tokyo Experiment" (NBER WP 5936, 1997; Journal of Finance 53(3), 1998, 1111-1130; doi:10.3386/w5936) (added 2026-11-18 R273)
- **Link:** [NBER w5936](https://www.nber.org/papers/w5936) (opened via web-fetch; abstract/metadata only).
- **Finding (verbatim, abstract):** "Lunch return variance doubles with the introduction of trading." Evidence on private information via volatility around the end of the Tokyo lunch-hour trading ban (1994); currency pair/sample UNVERIFIED (full paper not read). No predictive return, OOS or cost test.
- **Relevance:** None for a new item: volatility only, a 1990s regime change outside the repo's data; Tokyo-hours return windows already scanned on dev (E009) and the home-hours line closed on val (E017). **Status:** VERIFIED (abstract only).

### Chaudhary, "Multi-Scale Markov-Switching GARCH: Volatility Regime Detection in EUR/USD" (arXiv:2606.06190v1, Jun 2026; single-author preprint) (added 2026-11-18 R274)
- **Link:** [arXiv 2606.06190](https://arxiv.org/abs/2606.06190) (opened via web-fetch; first ~70% read verbatim, remainder summarised only).
- **Design/finding:** EUR/USD 1-minute mid 2015-2025 resampled to 1H/4H/1D; three AR(1)-MS-GARCH models (3 regimes each) feeding 27 RidgeCV experts; train to 2021-01-01, quarterly walk-forward test 2021-2024. Verbatim (abstract): volatility forecast vs GARCH(1,1) "DM = +4.7040 (p = 1.28 x 10^-6)"; OOS directional IC "+0.0252 (p = 6.75 x 10^-5)"; positioned "as a risk management tool rather than a standalone alpha engine". No trading P&L or cost treatment found (costs statement from the summarised part, UNVERIFIED).
- **Relevance:** None for a new item: volatility/regime focus; directional IC tiny with no cost test; test period overlaps the repo's val/OOS blocks; Markov-switching direction line already NONE on dev (E050). **Status:** VERIFIED (partly read).

### Kumar, "On the disappearance of calendar anomalies: have the currency markets become efficient?" (Studies in Economics and Finance 35(3), 441-456, 2018; doi:10.1108/SEF-08-2015-0192) (added 2026-11-19 R275)
- **Link:** [IDEAS](https://ideas.repec.org/a/eme/sefpps/sef-08-2015-0192.html) (opened via web-fetch; abstract/metadata only, full text paywalled).
- **Design/finding (paraphrased, abstract):** 20 currency pairs vs USD, Jan 1995 - Dec 2014 split 1995-2004 / 2005-2014; OLS with GARCH(1,1) and Kruskal-Wallis. Day-of-week, January (higher) and turn-of-month (lower) effects found in the first half largely disappear in 2005-2014. No magnitudes in abstract; EUR/USD inclusion UNVERIFIED; no OOS or cost test.
- **Relevance:** None for a new item: reported decay before the repo's dev block, ~6 Januaries on dev (below the R090 power floor); day-of-week and month-end already tested (E009, E034). **Status:** VERIFIED (abstract only).

### Cho & Rho, "On asymmetric volatility effects in currency markets" (Empirical Economics 62(5), 2149-2177, 2022; doi:10.1007/s00181-021-02091-7) (added 2026-11-19 R275)
- **Link:** [Springer](https://link.springer.com/10.1007/s00181-021-02091-7) (opened via web-fetch; abstract only).
- **Design/finding (paraphrased, abstract):** 5-minute bid/ask mid quotes 2004-2017 for the most actively traded currencies (list UNVERIFIED); HAR models with quantile regression and positive/negative realized semivariances. Safe-haven currencies' future volatility is driven by appreciation-side semivariance, others by depreciation-side; effects stronger in high-volatility phases. Volatility forecasting only; no direction, OOS or cost test.
- **Relevance:** None for a new item: no return-direction claim. **Status:** VERIFIED (abstract only).

### Gkillas, Gupta & Pierdzioch, "Forecasting (downside and upside) realized exchange-rate volatility: Is there a role for realized skewness and kurtosis?" (Physica A 532, 121867, 2019; doi:10.1016/j.physa.2019.121867) (added 2026-11-19 R275)
- **Link:** [IDEAS](https://ideas.repec.org/a/eee/phsmap/v532y2019ics0378437119310957.html) (opened via web-fetch; abstract only).
- **Design/finding (paraphrased, abstract):** AUD, CAD, CHF, EUR, GBP, JPY vs USD, intraday-based realized measures, 1 Jul 2003 - 28 Aug 2015; in-sample and out-of-sample one-day-ahead RV forecasts. Mainly realized kurtosis improves OOS RV forecasts, depending on loss function and pair. No magnitudes in abstract; no direction or cost test.
- **Relevance:** None for a new item: volatility only; realized skewness -> next-day direction already NONE on dev (E044/B50). **Status:** VERIFIED (abstract only).


### Lee, Ranaldo & Tsuruga, "Settlement Risk and Currency Markets" (IMF Working Paper WP/2026/156, Jul 2026; doi:10.5089/9798229054355.001) (added 2026-11-19 R277)
- **Link:** [IMF landing page](https://www.imf.org/en/publications/wp/issues/2026/07/24/settlement-risk-and-currency-markets-578075/index.md) and [IMF PDF markdown rendering](https://www.imf.org/-/media/files/publications/wp/2026/english/wpiea2026156-source-pdf.pdf.md) (both opened via web-fetch; table numbers from the rendering, which repeats sections, so treat as UNVERIFIED against the PDF).
- **Design/finding:** difference-in-differences around Hungary's CLS payment-versus-payment adoption (16 Nov 2015); HRK, CZK, HUF, PLN, RON, RSD vs USD and EUR, daily Bloomberg mids, 2015-2016, +-1/+-3 month windows. Summary (verbatim): "currency excess returns decline by about ten basis points after CLS adoption". Excess return = daily log FX change minus overnight rate differential. Holiday DiDiD on 30-min data for 4 CEE/USD pairs around 4 US holidays/yr. In-sample only (placebos, randomization inference); no OOS or transaction-cost test; one treated currency.
- **Relevance:** None for a new item: no EUR/USD spot-direction result; EUR/USD is CLS-settled across the whole repo sample, so no comparable event exists. **Status:** VERIFIED (partly read).

### Ornelas & Mauad, "Volatility Risk Premia and Future Commodity Returns" (Banco Central do Brasil Working Paper 455, Apr 2017) (added 2026-11-19 R278)
- **Link:** [BCB PDF](https://www.bcb.gov.br/pec/wps/ingl/wps455.pdf) (opened via web-fetch; first ~40k of ~90k characters verbatim, rest via model summary).
- **Design/finding:** predictors are volatility risk premia (implied minus 5-min realized vol, 1-month OTC options) of AUD/CAD (commodity currencies), EUR/GBP/JPY (non-commodity group), gold (GVZ), oil (OVX) and S&P 500; daily overlapping obs, currencies Feb 2003 - Dec 2014; targets are commodity, currency (Dollar index, EM/Latam/Asia indices), equity, yield and spread indices at 1-3 month horizons. Commodity-currency VRP coefficient negative for the Dollar index. Verbatim: "The results indicate that the predictive ability of VRPs exists almost only in the post-crisis period." In-sample HAC regressions; no OOS or transaction-cost test (absence of OOS/costs per summary of unread part, UNVERIFIED). No EUR/USD return target; no vol-of-vol or MOVE predictor.
- **Relevance:** None for a new item: monthly-horizon index regressions, in-sample, no EUR/USD; FX option implied vols not in pipeline. **Status:** VERIFIED (partly read).

### Phylaktis & Yamani, "Foreign currency forecasting in emerging markets: What can stock and bond markets tell us?" (Journal of Empirical Finance 83, 2025; doi:10.1016/j.jempfin.2025.101641) (added 2026-11-19 R279)
- **Link:** [IDEAS abstract page](https://ideas.repec.org/a/eee/empfin/v83y2025ics0927539825000635.html) (opened via web-fetch; abstract only, full text paywalled).
- **Design/finding (abstract, paraphrased):** out-of-sample tests (statistical and a trading strategy) of whether international stock and bond returns predict future spot exchange-rate changes, developed vs emerging countries. Profits appear in emerging markets (driven mainly by emerging stock returns, less by bond returns); no such profitability in developed-country data. Currencies, frequency and sample period not stated in the abstract (UNVERIFIED).
- **Relevance:** None for a new item: the developed-market (which would include EUR/USD) result is negative; studies stock/bond returns, not the stock-bond correlation regime; equity/bond-return -> FX line already NONE (B35/E037). **Status:** VERIFIED (abstract only).

### Li, de Haan & Scholtens, "Are International Fund Flows Related to Exchange Rate Dynamics?" (Open Economies Review 29, 31-48, 2018; doi:10.1007/s11079-017-9469-5) (added 2026-11-19 R280)
- **Link:** [Springer article page](https://link.springer.com/article/10.1007/s11079-017-9469-5) (opened via web-fetch; page truncated, later sections summary-based).
- **Design/finding:** monthly EPFR Global equity (1996-2015) and bond (2004-2015) fund flows, 53 countries; dependent variable is each country's bilateral real exchange rate change vs USD; in-sample dynamic panel (LSDV, GMM robustness). Inflows co-move with real appreciation, mostly contemporaneously. No out-of-sample or cost test seen; EUR/USD not modelled as a pair.
- **Relevance:** None for a new item: contemporaneous/in-sample monthly panel, no EUR/USD direction test; EPFR flow data not in pipeline. **Status:** VERIFIED (partly read).

### Gefang, Hall & Tavlas, "Dynamics of the Currency Composition of Central Bank Reserves" (arXiv:2608.24468, Aug 2026) (added 2026-11-19 R280)
- **Link:** [arXiv PDF](https://arxiv.org/pdf/2608.24468) (opened via web-fetch; truncated, later sections summary-based).
- **Design/finding:** annual unbalanced panel of reserve-currency shares (AUD, CAD, CNY, EUR, GBP, JPY, USD, Other), 53 countries 1999-2023, constrained SUR. Shares are highly persistent; exchange-rate variables largely lose significance with year effects. Models reserve shares, not exchange-rate returns; no forecasting test.
- **Relevance:** None for a new item: annual frequency, reserve shares as the dependent variable, no EUR/USD return prediction. **Status:** VERIFIED (partly read).

### Jessen & Poulsen, "Empirical Performance of Models for Barrier Option Valuation", Quantitative Finance 13(1), 1-11 (2013) (doi:10.1080/14697688.2012.723820) (added 2026-11-19 R281)
- **Link:** [CBS open-archive PDF](https://research-api.cbs.dk/ws/files/58805670/cathrine_jessen_BarrierPaper_Revised030812_openarchive.pdf) (opened via web-fetch; Aug 2012 working version, later sections summary-based).
- **Design/finding:** USD/EUR, daily, Jan 2004 - Sep 2005; 156 Danske Bank single-barrier contracts (3,108 valuations). Compares option-pricing models on pricing error: continuous-path models (Black-Scholes, CEV, Heston) about equal, jump models worse. Does not study spot behaviour near barrier levels; no trading, out-of-sample P&L or cost test.
- **Relevance:** None for a new item: option-pricing study, no spot-direction evidence; barrier-level data not in pipeline. **Status:** VERIFIED (partly read).

### Heyes, Neidell & Saberian, "The Effect of Air Pollution on Investor Behavior: Evidence from the S&P 500", NBER WP 22753 (2016) (added 2026-11-19 R281)
- **Link:** [NBER page](https://www.nber.org/papers/w22753) (abstract opened via web-fetch).
- **Design/finding:** Manhattan PM2.5 vs same-day S&P 500 returns; one SD higher PM2.5 lowers same-day returns (abstract: "by 11.9% in our preferred specification"); effect strictly local, attributed to lower risk tolerance. No exchange rates studied.
- **Relevance:** None for a new item: equities only, no FX test; pollution data not in pipeline. **Status:** VERIFIED (abstract only).

### Rossi Júnior, "The Usefulness of Financial Variables in Predicting Exchange Rate Movements", Insper BEWP 198/2014 (added 2026-11-19 R282)
- **Link:** [Insper repository PDF](https://repositorio-api.insper.edu.br/server/api/core/bitstreams/e210bda8-8bca-4634-9e6f-720baa220200/content) (opened via web-fetch; truncated, later sections summary-based).
- **Design/finding:** weekly end-of-week data Jan 2001 - Apr 2013, 27 currencies vs USD (no euro, no DEM). Predictors include the US high-yield minus investment-grade corporate spread, 10-year Treasury yield, VIX, TED spread. HY-spread model beats a driftless random walk out-of-sample (rolling window, Clark-West) at 1-8 weeks for all but CHF; hit ratios ~52-63% (summary). The model uses realized (contemporaneous) fundamentals; the author concedes this is "not truly out-of-sample". No transaction costs.
- **Relevance:** None for a new item: EUR not covered, contemporaneous-fundamentals design (not a tradable forecast), no costs; credit-spread data not in pipeline. **Status:** VERIFIED (partly read).

### Federal Reserve Board IFDP Note, "The Sensitivity of the U.S. Dollar Exchange Rate to Changes in Monetary Policy Expectations" (22 Sep 2017) (added 2026-11-19 R283)
- **Link:** [Fed IFDP note, accessible version](https://www.federalreserve.gov/econres/notes/ifdp-notes/the-sensitivity-of-the-us-dollar-exchange-rate-to-changes-in-monetary-policy-expectations-accessible-20170922.htm) (opened via web-fetch; accessible-data page, method details summary-based; authors not visible in what was read).
- **Design/finding:** daily changes on FOMC announcement days, Jan 2002 - Jun 2017; rolling 2-year robust regressions of the advanced-economy dollar index change on policy-expectation changes (same-day sensitivity).
- **Relevance:** None for a new item: dollar index (EUR/USD not named), contemporaneous announcement-day sensitivity only, no later-drift, blackout-period, out-of-sample or cost test. **Status:** VERIFIED (partly read).

### Hayo & Iwatsubo, "Who Is Successful in Foreign Exchange Margin Trading? New Survey Evidence from Japan", Kobe University GSE DP 1909 (2019) / CityU GRU WP 2019-026 (added 2026-11-19 R284)
- **Link:** [Kobe DP 1909 PDF](https://www.econ.kobe-u.ac.jp/wp/wp-content/uploads/2023/06/1909.pdf); same study as [CityU GRU WP 2019-026 PDF](https://www.cb.cityu.edu.hk/ef/doc/GRU/WPS/GRU%232019-026%20Iwatsubo.pdf) (both opened via web-fetch; partly read, end sections summary-based).
- **Design/finding:** internet survey of 1,000 Japanese adults (Feb-Mar 2018, for the Financial Futures Association of Japan), 962 obs; in-sample OLS of self-reported 2017 trader profit on demographics, strategy and financial literacy (age negative, "no specific strategy" negative, self-reported FX skills positive). No exchange-rate data, no return-prediction test.
- **Relevance:** None for a new item: trader-performance survey, no positioning -> EUR/USD test, no out-of-sample or cost test. **Status:** VERIFIED (partly read).

### Keloharju, Linnainmaa & Nyberg, "Common Factors in Return Seasonalities", NBER WP 20815 (Dec 2014) (added 2026-11-19 R285)
- **Link:** [NBER WP 20815 PDF](https://www.nber.org/papers/w20815.pdf) (opened via web-fetch; first part read verbatim, rest summary-based).
- **Design/finding:** same-calendar-month return seasonality in US stocks (CRSP 1963-2011, long-short ~13%/yr), anomaly portfolios, 24 commodity futures and 15 MSCI country indices (1970-2011, summary). No currencies.
- **Relevance:** None for a new item: no FX or EUR/USD test; a monthly same-calendar-month rule would give ~3 dev observations per month cell. **Status:** VERIFIED (partly read).

### Barroso, Menichetti & Reichenecker, "Hedging with an edge: parametric currency overlay", first draft (9 Jan 2018) (added 2026-11-19 R285)
- **Link:** [CFR Cologne colloquium PDF](https://www.cfr-cologne.de/download/kolloquium/2018/BarrosoMenichettiReichenecker.pdf) (opened via web-fetch; partly read, rest summary-based).
- **Design/finding:** monthly cross-sectional parametric currency overlay for a global equity investor, 10 currencies, 1976-2016; OOS 1986-2016 with forward bid-ask costs; characteristics momentum, forward discount, long-term reversal, autocorrelation; Jensen's alpha 110-129 bps, Sharpe gain ~38% (abstract); volatility characteristics not significant.
- **Relevance:** None for a new item: cross-sectional monthly overlay, no EUR/USD single-pair result, carry/forward data not in pipeline, momentum-on-lags already tested on dev. **Status:** VERIFIED (partly read).

### Pojarliev & Levich, "Detecting Crowded Trades in Currency Funds", NBER WP 15698 (Jan 2010) (added 2026-11-19 R286)
- **Link:** [NBER WP 15698 PDF](https://www.nber.org/papers/w15698.pdf) (opened via web-fetch; first part read verbatim, rest summary-based).
- **Design/finding:** 80 currency managers (DB FXSelect), weekly returns Apr 2005 - Mar 2008; crowdedness = share of managers loading on carry/trend/value factor indices; EUR-USD only a component of the factor indices. Authors: "our sample period is too short for more formal statistical tests." No spot-direction forecast, no costs.
- **Relevance:** None for a new item: no EUR/USD direction test, manager-return data not in pipeline. **Status:** VERIFIED (partly read).

### Sokolovski, "Crowds, Crashes, and the Carry Trade", job market paper (15 Dec 2016) (added 2026-11-19 R286)
- **Link:** [UC3M seminar PDF](https://indem.uc3m.es/seminarios/filesem_1486993340.pdf) (opened via web-fetch; first part read verbatim, rest summary-based).
- **Design/finding:** nine G10 vs USD (EUR with DEM history), daily 1976-2016; crowdedness from abnormal return correlations among carry target currencies; abstract: "carry trade crowdedness negatively forecasts monthly carry trade returns" (equal-weighted carry portfolio, not single pairs). Costs explicitly ignored ("Ignoring transaction costs"); in-sample per summary (UNVERIFIED). Coefficient sizes summary-based only (UNVERIFIED).
- **Relevance:** None for a new item: monthly cross-sectional carry-portfolio target, needs forward rates and other G10 pairs not in pipeline, no EUR/USD direction or cost test. **Status:** VERIFIED (partly read).

### Costantini, Crespo Cuaresma & Hlouskova (2016), "Forecasting errors, directional accuracy and profitability of currency trading: The case of EUR/USD exchange rate", Journal of Forecasting 35(7), 652-668, doi:10.1002/for.2398 (added 2026-11-19 R288)
- **Link:** [WU research portal](https://research.wu.ac.at/de/publications/forecasting-errors-directional-accuracy-and-profitability-of-curr-3/) (opened via web-fetch; abstract and metadata only; accepted-manuscript PDF fetch failed, body UNVERIFIED).
- **Design/finding (abstract, verbatim):** out-of-sample EUR/USD forecasts "based on multivariate macroeconomic models and forecast combinations"; "forecast combinations, in particular those based on principal components of forecasts, help to improve over benchmark trading strategies, although the excess return per unit of deviation is limited." Data frequency, sample, model list and cost treatment not stated in the part read.
- **Relevance:** None for a new item: macro-model inputs not in pipeline, frequency/costs unverified, authors report limited risk-adjusted gain. **Status:** abstract only.

### Dunne, Hau & Moore (Nov 2005), "International Order Flows: Explaining Equity and Exchange Rate Returns" (added 2026-11-19 R294)
- **Link:** [Bank of Canada conference PDF](https://www.bankofcanada.ca/wp-content/uploads/2010/08/hau_dunne_moore.pdf) (opened via web-fetch; truncated, later sections summary-based).
- **Design/finding:** daily 1999-2003, S&P100 and CAC40 vs USD/EUR; EBS FX order flow (1999 only) as instrument. Abstract (verbatim): "Almost 60 percent of the daily returns in the S&P100 index is explained jointly by exchange rate returns and aggregate order flows." Same-day regressions only; no lagged/predictive, OOS or cost test.
- **Relevance:** None for a new item: contemporaneous, not a direction forecast. **Status:** VERIFIED (partly read).

### Cenedese, Payne, Sarno & Valente (2015), "What do stock markets tell us about exchange rates?", Bank of England Staff WP 537 (added 2026-11-19 R294)
- **Link:** [BoE PDF](https://www.bankofengland.co.uk/-/media/boe/files/working-paper/2015/what-do-stock-markets-tell-us-about-exchange-rates.pdf) (opened via web-fetch; truncated, net-of-cost figures summary-based, UNVERIFIED).
- **Design/finding:** monthly 1983-2011, 42 countries vs USD, cross-sectional portfolio sorts on equity-return predictors; euro-area members as separate entries, no single EUR/USD pair. Abstract (verbatim): "exchange rate movements are in fact unrelated to differentials in country-level equity returns."
- **Relevance:** None for a new item: monthly cross-sectional, no EUR/USD single-pair test, needs 42-country equity data. **Status:** VERIFIED (partly read).

- Also opened R294: Phylaktis & Yamani, Bayes EMG WP-EMG-02-2025 (https://www.bayes.citystgeorges.ac.uk/__data/assets/pdf_file/0009/889236/Phylaktis-and-Ehab-Foreign-Forecasting-06.05.25.pdf): working-paper version of the already-logged JEF 2025 paper (doi:10.1016/j.jempfin.2025.101641); abstract (verbatim) "this profitability is not evident in developed countries data." No new entry.

### Sharpe & Gil de Rubio Cruz (2024), "Predicting Analysts' S&P 500 Earnings Forecast Errors and Stock Market Returns using Macroeconomic Data and Nowcasts", FEDS 2024-049 (added 2026-11-19 R295)
- **Link:** [Federal Reserve PDF](https://federalreserve.gov/econres/feds/files/2024049pap.pdf), DOI 10.17016/FEDS.2024.049 (opened via web-fetch; ~first half read verbatim, later sections summary-based, UNVERIFIED).
- **Design/finding:** quarterly 1993-2023; a macro model of S&P 500 earnings (Blue Chip GDP forecasts, lagged broad-dollar change) predicts analysts' forecast errors, and the gap predicts 3-month-ahead stock returns. The broad dollar index is only a regressor; no exchange-rate return is forecast.
- **Relevance:** None for a new item: equity-return paper, no FX predictive/OOS/cost test, no EUR/USD. **Status:** VERIFIED (partly read).

### Hasbrouck & Levich, "FX Liquidity and Market Metrics: New Results Using CLS Bank Settlement Data" (NYU Stern, 30 Sep 2019) (added 2026-11-19 R296)
- **Link:** [PDF](https://pages.stern.nyu.edu/jhasbrou/Research/Hasbrouck-Levich%20v25.pdf) (opened via web-fetch; first part read verbatim, rest summary-based, UNVERIFIED).
- **Design/finding:** CLS settlement instructions for all of April 2010, 2013 and 2016 (ms timestamps), Olsen 10-second quotes, 13 pairs incl. EUR/USD; price impact falls 2010->2013 and rises 2013->2016; spreads, settlement sizes and price clustering decline (algorithmic trading). No return-predictability, OOS or cost test. Cites Ranaldo-Somogyi (2018) CLS hourly net flow -> spot (not fetched, UNVERIFIED).
- **Relevance:** None for a new item: liquidity metrics only; CLS flow data not in the pipeline. **Status:** VERIFIED (partly read).

### Etienne, Ohana, Benhamou, Guez, Setrouk & Jacquot, "Revisiting the Structure of Trend Premia: When Diversification Hides Redundancy" (arXiv:2510.23150v2, Oct 2025) (added 2026-11-19 R296)
- **Link:** [arXiv PDF](https://arxiv.org/pdf/2510.23150) (opened via web-fetch; partly verbatim, rest summary-based, UNVERIFIED).
- **Design/finding:** CTA trend-following on a pooled futures universe (EUR futures one of several FX contracts, 2 bp costs), signals at 20-500 days, rolling OOS from 2013; dropping the 125-day layer improves Sharpe. No EUR/USD-specific or intraday test.
- **Relevance:** None for a new item: pooled multi-asset daily trend; single-pair trend already tested on dev. **Status:** VERIFIED (partly read).

### Izadyar (4 Aug 2026), "AI and Exchange Rate Predictability", arXiv:2608.00761 (added 2026-11-19 R297)
- **Link:** [arXiv PDF](https://arxiv.org/pdf/2608.00761) (opened via web-fetch; abstract and Sections 1-4 verbatim, later sections summary-based, UNVERIFIED).
- **Design/finding:** GPT-4o labels 544 Investing.com macro indicators (1996-2024) as strengthening/weakening a currency; AIFX index over 1-60 month lookbacks; monthly long top-2 / short bottom-2 of G10 vs USD. Abstract (verbatim fragment): "generates a Sharpe ratio exceeding 0.7 per annum". Gross only; text (verbatim): "transaction costs are unlikely to significantly erode returns". No train/test split; look-ahead from LLM training data addressed with four checks.
- **Relevance:** None for a new item: monthly cross-sectional, no EUR/USD single-pair daily/intraday direction or net-of-cost result; LLM release-text pipeline not in repo. **Status:** VERIFIED (partly read).

### Levich & Poti (Dec 2008), "Predictability and 'Good Deals' in Currency Markets", NBER WP 14597 (added 2026-11-19 R297)
- **Link:** [NBER PDF](https://www.nber.org/papers/w14597.pdf) (opened via web-fetch; Sections 1-5 verbatim, rest summary-based, UNVERIFIED).
- **Design/finding:** daily and monthly spot vs USD 1971-2006 (AUD, CAD, JPY, GBP, CHF, ECU/EUR); rolling ARMA R-squared vs a no-good-deal bound. Footnote 7 (verbatim): "the empirical results are in-sample". Verbatim: "Excess-predictability is highest in the 1970s and tends to decrease over time, but it is still present in the final part of the sample period" and "With transaction costs of five basis points, the maximal SRs of daily strategies are negative for all currencies." Monthly strategies stay positive at 5 bp.
- **Relevance:** None for a new item: in-sample, daily predictability does not survive costs, no intraday result (adaptive-markets framing only). **Status:** VERIFIED (partly read).

### Molodtsova & Papell (2 Jun 2011), "Phoenix Taylor Rule Exchange Rate Forecasting During the Financial Crisis" (added 2026-11-19 R298)
- **Link:** [PDF (Banque de France host)](https://esurfi-banque.banque-france.fr/sites/default/files/media/2017/06/15/euro-dollar-forecasting.pdf) (opened via web-fetch; ~40k of 87k characters verbatim, rest summary-based, UNVERIFIED).
- **Design/finding:** real-time quarterly US/euro-area data 1999Q4-2010Q4, rolling 26-quarter regressions, one-quarter-ahead EUR/USD forecasts, MSPE ratio vs random walk with Clark-West test. Verbatim: "The Taylor rule specifications outperform the random walk with forecasts ending between 2007:Q1 and 2008:Q1"; "The monetary and PPP models cannot outperform the random walk for any forecast interval"; "Taylor rule predictability, however, rises from the dead in 2009 and 2010."
- **Relevance:** None for a new item: quarterly, statistical predictability only (no directional, trading or cost result seen), macro real-time data not in the pipeline. **Status:** VERIFIED (partly read).


### Edmans, García & Norli (Dec 2005 draft), "Sports sentiment and stock returns" (added 2026-11-20 R299)
- **Link:** [PDF (Colorado Leeds faculty page)](https://leeds-faculty.colorado.edu/garcia/paper91v32.pdf) (opened via web-fetch; front part verbatim, last part summary-based, UNVERIFIED).
- **Design/finding:** 39 national stock indices (local currency, Datastream), daily, first trading day after international soccer (1973-2004), cricket, rugby, ice hockey, basketball matches. Next-day loss effect: -38.4 bp after 138 elimination losses, -49.4 bp after 56 World Cup elimination losses, -21.2 bp across all 524 losses; no significant win effect. No currency returns tested; no OOS or cost test seen.
- **Relevance:** None for a new item: equities only, and euro-area/US elimination matches give far fewer events on dev than the R090 power floor. **Status:** VERIFIED (partly read).

### Lenzo / Russell Investments (11 Nov 2026), "Holiday trading effect" (added 2026-11-20 R300)
- **Link:** [Russell Investments research page](https://russellinvestments.com/content/ri/us/en/insights/russell-research/2026/11/holiday-trading-effect.html) (opened via web-fetch; summary-based, UNVERIFIED in detail).
- **Design/finding:** practitioner execution-planning note (not peer-reviewed), approximate figures from an undisclosed multi-year sample. Verbatim: FX volumes run "50–80% (depending on the currency pair) below normal by the second half of the month" (December); Christmas Eve / Boxing Day FX volumes "roughly 20-30% of normal"; the holiday effect "does not, by itself, indicate whether markets will rise or fall." No return-predictability, OOS or quantified cost test.
- **Relevance:** None for a new item: liquidity description only, no direction signal; holiday thin-liquidity periods are already handled by the session/holiday filters. **Status:** VERIFIED (partly read).

### Kwas, Beckmann & Rubaszek, "Are consensus FX forecasts valuable for investors?", International Journal of Forecasting 40(1), 2024, 268-284 (added 2026-11-20 R301)
- **Link:** [EconPapers](https://econpapers.repec.org/RePEc:eee:intfor:v:40:y:2024:i:1:p:268-284), doi:10.1016/j.ijforecast.2023.02.007 (EconPapers abstract page opened via web-fetch; IfW/Kiel Institute page redirect could not be fetched; full text not read).
- **Design/finding (abstract):** Consensus Economics survey forecasts used as currency-portfolio trading signals. Verbatim: surveys "provide trading signals which are not entirely driven by standard benchmark trading strategies such as momentum, carry, or value" and give "additional excess returns of up to two percentage points per year compared to benchmarks". Currencies (EUR/USD inclusion), frequency, horizon, out-of-sample design and costs: UNVERIFIED (not in abstract).
- **Relevance:** None for a new item: monthly-survey, cross-sectional portfolio signal; Consensus Economics data is not in the pipeline; at monthly frequency dev (2015-2020) has ~72 observations, below the lesson-R090 power floor. Same data family as Ballensiefen-Somogyi-Winterberg (R247). **Status:** VERIFIED (abstract only).

### Sekkel & Zhang (Bank of Canada; draft Nov 2024), "Speeches, Press Conferences and Minutes: The International Transmission of Federal Reserve Communication" (added 2026-11-20 R302)
- **Link:** [PDF (Princeton GCEPS)](https://gceps.princeton.edu/wp-content/uploads/2024/11/Fed_transmission_XuZhang.pdf) (opened via web-fetch; first ~40k of 121k characters verbatim, rest summary-based, UNVERIFIED in detail).
- **Design/finding:** high-frequency event study, Jan 1997-Jul 2023: FOMC announcements (228), press conferences (71), minutes (201), Chair/Vice Chair monetary-policy speeches (224/82), plus Bank of Canada events. Windows: announcement -10/+20 min, press conference -10/+80 min, minutes -10/+50 min, speeches -15/+105 min. Only exchange rate studied is CAD/USD (spot, futures, forwards); verbatim: "Both central banks significantly affect the exchange rate". Contemporaneous event-window and CIP analysis; no directional post-event predictability, OOS or cost test seen. No EUR/USD.
- **Relevance:** None for a new item: CAD/USD only, contemporaneous effects; Fed communication -> FX already logged (IES WP 23/2025, Ayadi et al. SEF 2023); a speech calendar with timestamps is not in the pipeline (same blocker as B6). **Status:** VERIFIED (partly read).


### Dao, Tan & Zhou, "Repo Market Volatility and the U.S. Debt Ceiling", IMF Working Paper WP/25/127, June 2025 (added 2026-11-20 R303)
- **Link:** [PDF](https://www.imf.org/-/media/files/publications/wp/2025/english/wpiea2025127-print-pdf.pdf) (opened via web-fetch; front part verbatim, last ~25k characters summary-based, UNVERIFIED in detail).
- **Design/finding:** daily GC repo-to-IOR spread regressed on TGA balance changes, Fed reserves and ON RRP, 1 Jul 2009-16 May 2025, plus debt-ceiling event study. Verbatim (abstract): TGA swings "can create large swings in the repo spread and distort the supply of repo funding"; "the repo spread could fluctuate by 20-30 basis points around the lift-off date". USD money markets only; no exchange rate, no OOS, no costs.
- **Relevance:** None for a new item: no FX target; TGA/tax-date liquidity angle has no EUR/USD direction evidence (FEDS Note "Fiscal flow volatility and reserves" already logged). **Status:** VERIFIED (partly read).

### Correa, Du & Liao, "U.S. Banks and Global Liquidity", NBER conference draft, March 2021 (added 2026-11-20 R303)
- **Link:** [PDF](https://conference.nber.org/conf_papers/f150492/f150492.pdf) (opened via web-fetch; front part verbatim, last ~20k characters summary-based, UNVERIFIED in detail).
- **Design/finding:** daily FR 2052a supervisory data for six US GSIBs from Dec 2015; banks use excess reserves to lend in repo and FX swap markets; quarter-end/TGA reserve shifts move intermediation spreads (CIP basis). Verbatim: "a large Fed balance sheet may be necessary even when short-term interest rates are well above the zero-lower bound." EUR enters only via CIP/FX-swap basis (summary). No spot-return forecast, OOS or cost test.
- **Relevance:** None for a new item: FX-swap/basis channel, not EUR/USD spot direction; quarter-end window dressing -> FX swaps already logged (BIS WP 836, Boston Fed WP 18-6, Ranaldo ECB 2024). **Status:** VERIFIED (partly read).

### Corhay, Fatemi & Tourani Rad, "On the Presence of a Day-of-the-Week Effect in the Foreign Exchange Market", Managerial Finance 21(8), 1995, pp. 32-43 (added 2026-11-20 R304)
- **Link:** [ORBi postprint PDF](https://orbi.uliege.be/bitstream/2268/96132/1/Corhay_A_%201995_Managerial%20finance_21_32-43.pdf) (opened via web-fetch; read in full, summary-based, details UNVERIFIED verbatim).
- **Design/finding:** daily log spot returns of GBP, CAD, DEM, FRF, JPY, CHF vs USD, Jan 1973-Dec 1992 (5,218 obs), day-of-week dummies with Wednesday intercept, OLS and GARCH(1,1)-t. Wednesday returns significantly higher before the 1 Oct 1981 settlement-procedure change (GBP t = 3.33), not after (t = 1.23); attributed to the settlement cycle. In-sample only, no trading rule, no costs. Found while searching a "payday / payroll date" angle; no payday study surfaced.
- **Relevance:** None for a new item: no EUR/USD, pre-1993 settlement artefact, day-of-week family already covered (E009 hour/day cells on dev). **Status:** VERIFIED (summary-read).

### UNVERIFIED (not opened): City, University of London open-access JFE revision "TS_v35" (eprint 24178)
- **Link:** [PDF](https://openaccess.city.ac.uk/id/eprint/24178/1/TS_v35%20%5BJFE_Revision_v6%5D.pdf) — fetch returned an access-denied bot page; title, authors and findings UNVERIFIED. Surfaced by a "VIX term structure -> currency returns" search; not used.

### Lupinu & Machura-Urbaniak, "The Next Generation EU (NGEU) as a catalyst for the promotion of the international role of the euro", REBUILD Working Paper 4, January 2023 (added 2026-11-20 R305)
- **Link:** [ORBilu PDF](https://orbilu.uni.lu/bitstream/10993/54742/1/REBUILD%20Working%20Paper%20-%20Lupinu%20%26%20Machura-Urbaniak.pdf) (opened via web-fetch; first ~40k of 85k characters read verbatim, rest summary-based).
- **Design/finding:** qualitative policy/legal analysis of whether NGEU green bonds and EU safe assets could raise the euro's international role. No dataset, no exchange-rate return or direction test, no OOS or cost test.
- **Relevance:** None for a new item (no EUR/USD return evidence). **Status:** VERIFIED (partly summary-read).

### Bulut, "Google Trends and the forecasting performance of exchange rate models", Journal of Forecasting 37(3), 2018, pp. 303-315, doi:10.1002/for.2500 (added 2026-11-20 R306)
- **Link:** [IDEAS/RePEc abstract page](https://ideas.repec.org/a/wly/jforec/v37y2018i3p303-315.html) (opened via web-fetch; abstract only, paraphrased; full text not opened).
- **Design/finding:** monthly nominal exchange-rate returns of 11 OECD currencies, Jan 2004-Jun 2014; Google Trends search-query predictors vs structural (PPP, monetary) models and a random walk, out-of-sample, Clark-West test. Google Trends beats the random walk for 5 of 11 pairs (monetary model 1 of 11) and is better at direction. Pairs not named in the abstract (EUR/USD inclusion UNVERIFIED); no trading or cost test mentioned.
- **Relevance:** None for a new item: monthly horizon (~60 dev months), Google Trends data not in the pipeline (new data source = human decision, R219 observation), no net-of-cost evidence. **Status:** VERIFIED (abstract only).

### Feng & Zhang, "Currency exchange rate predictability: The new power of Bitcoin prices", Journal of International Money and Finance 132 (2023) 102811, doi:10.1016/j.jimonfin.2023.102811 (added 2026-11-20 R307)
- **Link:** [NSF PAR accepted manuscript](https://par.nsf.gov/servlets/purl/10470586) (opened via web-fetch; ~120k of 137k characters read verbatim in parts; online appendix not in the PDF; table p-values inferred from extraction alignment).
- **Data/design:** daily Bitcoin (CoinMarketCap, USD) 2014-01-01 to 2022-08-31; 32 currencies + broad dollar index from IMF data (closing time not stated, UNVERIFIED); ADL and ECM, one lag, robust regression, 180-trading-day rolling windows; forecast FX t -> t+h from Bitcoin return at t (h = day, week, month); OOS vs random walk with direction-of-change and Clark-West.
- **Finding (verbatim):** "Bitcoin prices have surprisingly predictive power for nominal currency exchange rates, both in-sample and out-of-sample." EUR row, Table 4 (ADL vs RW): "EUR 51.79% 2.0081 | 51.16% -0.3938 | 53.49% 1.1038" (daily | weekly | monthly DoC, CW). Table 5 (ECM) EUR daily 52.30%, CW 1.6908. In-sample ADL daily average b1 for EUR +0.0002. Table 6 EUR long-only strategy 2.35%/yr vs 0.84% risk-free (difference not starred); no transaction costs in the strategy section.
- **Relevance:** basis of B64 (lagged daily BTC -> next-day EUR/USD, dev). Gross only; implied edge ~1-1.5 pips/day, below our dev detection limit. **Status:** VERIFIED (accepted manuscript, mostly verbatim).

### Ciganovic & D'Amario, "Forecasting Cryptocurrencies Log-Returns: a LASSO-VAR and Sentiment Approach", Sapienza working paper dated 2024-01-09 (added 2026-11-20 R307)
- **Link:** [IRIS Sapienza PDF](https://iris.uniroma1.it/retrieve/1d32ef71-fae2-444c-a49b-40d528a423d4/Ciganovic_Forecasting_2023.pdf) (opened via web-fetch; ~40k of 85k characters verbatim, rest summary-based).
- **Design/finding:** 10 cryptocurrencies, daily 2018-2022, LASSO-VAR with social-media sentiment, Google Trends, volume; "social media sentiment does not Granger-cause cryptocurrencies returns". No fiat FX variable.
- **Relevance:** None. **Status:** VERIFIED (partly summary-read).

### Drożdż, Minati, Oświęcimka, Stanuszek & Wątorek, "Signatures of crypto-currency market decoupling from the Forex", Future Internet 11(7) (2019) 154, doi:10.3390/fi11070154 (added 2026-11-20 R310)
- **Link:** [arXiv:1906.07834](https://arxiv.org/abs/1906.07834) (abstract and PDF opened via web-fetch; ~40k of 52k characters verbatim, rest summary-based).
- **Design/finding:** Kraken 10-second returns 2016-07-01 to 2018-12-31 for BTC/EUR, BTC/USD, ETH/EUR, ETH/USD, BTC/ETH vs Dukascopy EUR/USD; descriptive multifractal (MFDFA/MFCCA, qDCCA) cross-correlation analysis. Verbatim: "do not show any noticeable relationships"; "the cryptocurrency market has begun decoupling itself from the Forex." No forecasting, out-of-sample or cost test.
- **Relevance:** None for a new item; contemporaneous/scaling only. Ethereum -> EUR/USD would be a sibling of B64 (NONE, E052) with no EUR/USD predictive evidence. **Status:** VERIFIED (partly summary-read).

### Castagneto-Gissey & Green, "Exchange rates, oil prices and electricity spot prices: empirical insights from European Union markets", Journal of Energy Markets (RePEc:rsk:journ2:2349510; year/volume not shown on the record) (added 2026-11-20 R311)
- **Link:** [EconPapers record](https://econpapers.repec.org/RePEc:rsk:journ2:2349510) (abstract opened via web-fetch; full text not read). Publisher page: [risk.net](https://www.risk.net/journal-of-energy-markets/2349510/exchange-rates-oil-prices-and-electricity-spot-prices-empirical-insights-from-european-union-markets) (not opened).
- **Design/finding:** daily electricity spot returns in six European countries, 2005-7 and 2008-11, AR(1)-GARCH(1,1) / AR(1)-NGARCH(1,1) with oil and exchange-rate returns as regressors. Verbatim: "In many cases, the level of returns in either the oil price or the exchange rate had little impact on the level of electricity price returns, but the volatility of these prices affected the volatility of electricity prices". Direction is FX/oil -> electricity; currency pair not named in the abstract; no out-of-sample, forecast or cost test.
- **Relevance:** None for a new item (wrong causal direction, volatility only, pre-dev sample). **Status:** VERIFIED (abstract only).

### Deutsche Bundesbank, "What determines the exchange rate movements of the euro against the US dollar?", Monthly Report January 2026 (added 2026-11-20 R312)
- **Link:** [Bundesbank publication page](https://publikationen.bundesbank.de/content/972880) (full article text opened via web-fetch; charts and statistical annex not read).
- **Design/finding:** Bayesian proxy VAR, daily, March 2002 - December 2025, 10 variables (German/US 2y and 10y yields, EuroStoxx 50, S&P 500, VIX, Brent, gold, EUR/USD), shocks identified with high-frequency instruments around ECB/FOMC announcements, macro releases, OPEC/gas news and VIX jumps. Historical decompositions: US policy expectations the largest driver of the 2014-15 and 2022 euro falls; a 10% VIX rise lowers EUR/USD by about 0.2% (summary). Verbatim: "risk premiums also play an important role in determining exchange rates"; "permits almost real-time conclusions to be drawn about determinants of exchange rate movements". Contemporaneous attribution only; no lagged/out-of-sample forecast and no trading or cost test.
- **Relevance:** None for a new item (no predictive EUR/USD evidence; drivers overlap rate-differential, VIX and oil angles already logged). **Status:** VERIFIED (text read via summary).

### Kilic, "Virtue or Mirage? Complexity in Exchange Rate Prediction", FEDS 2025-089r1 (Federal Reserve Board staff working paper, revision dated June 2026) (added 2026-11-20 R313)
- **Link:** [federalreserve.gov PDF](https://www.federalreserve.gov/econres/feds/files/2025089r1pap.pdf) (opened via web-fetch; title page, abstract, introduction and most of the literature review verbatim, ~40k of 211k characters; Section 3 onward summary-based).
- **Design/finding:** monthly log returns of eight USD pairs (AUD, CAD, CHF, EUR, GBP, JPY, NOK, SEK); Taylor-rule (k=7) and monetary (k=4) fundamentals at t forecast t+1; rolling windows 12/60/120 months; Ridge with random Fourier features vs OLS vs random walk; Clark-West / Diebold-Mariano. Verbatim: "Ridge–RFF substantially outperforms OLS at short training windows"; "the cross-currency mean out-of-sample R2 is bounded above by zero everywhere". Random-walk outperformance significant only for AUD, CHF, JPY (Taylor rule) and JPY (monetary), so not EUR. Market-timing Sharpe ratios gross (summary); sample period UNVERIFIED (Appendix A not read).
- **Relevance:** None for a new item (monthly, EUR not among significant pairs, negative panel result). **Status:** VERIFIED (partly summary-read).

### Zhang, Zhang & Majeed, "Exchange Rate Determination and Forecasting: Can the Microstructure Approach Rescue Us from the Exchange Rate Disparity?", MPRA Paper No. 57673 (2013, posted 2014) (added 2026-11-20 R313)
- **Link:** [MPRA PDF](https://mpra.ub.uni-muenchen.de/57673/1/MPRA_paper_57673.pdf) (opened via web-fetch; ~40k of 48k characters verbatim, last tables summary-based).
- **Design/finding:** Reuters D2000-2 interdealer DEM/USD, 6-10 Oct 1997 (5 days), 5-30 minute bars; daily Evans-Lyons DEM/USD and JPY/USD. Returns on five lags of order flow, in-sample OLS only. Verbatim: "the results indicate weak predictability of order flow on the future exchange rate return"; "lagged order flow coefficients are not jointly different from zero" (5-min F-test p 0.13-0.59 by day). Only contemporaneous order flow is significant. No out-of-sample or cost test; not EUR/USD.
- **Relevance:** None (lagged order flow fails; consistent with the order-flow entries already logged; interdealer order flow is not in the pipeline). **Status:** VERIFIED (partly summary-read).

### Rink, "The predictive ability of technical trading rules: an empirical analysis of developed and emerging equity markets", Financial Markets and Portfolio Management 37 (2023) 403-456, doi:10.1007/s11408-023-00433-2 (added 2026-11-20 R315)
- **Link:** [Springer PDF](https://link.springer.com/content/pdf/10.1007/s11408-023-00433-2.pdf) (opened via web-fetch; abstract and introduction verbatim, results sections summary-based).
- **Design/finding:** 41 equity indices, daily, samples to May 2016; 6406 rules; stepwise SPA test (Hsu et al. 2010). Verbatim: out of sample, "recently best-performing rules perform significantly worse than simple buy-and-hold strategies in the future"; "in the last subperiod between 2009 and 2016, almost all emerging market indices are unpredictable." No currencies.
- **Relevance:** None for a new item (equity only); supports the prior that snooping-adjusted technical rules decay. **Status:** VERIFIED (partly summary-read).

### Zarrabi, Snaith & Coakley, "FX technical trading rules can be profitable sometimes!", International Review of Financial Analysis (2017), doi:10.1016/j.irfa.2016.12.010 (added 2026-11-20 R315)
- **Link:** [Essex repository accepted manuscript](https://repository.essex.ac.uk/18805/1/1-s2.0-S1057521916301958-main.pdf) (opened via web-fetch; ~40k of 72k characters verbatim; out-of-sample tables and conclusion summary-based).
- **Design/finding:** daily GBP, CAD, JPY, SEK, CHF, NOK vs USD, 1994-2014 (no EUR/USD); false-discovery-rate control (Barras et al. 2010); 2.5 bp one-way costs. Verbatim: "These TTRs generate profits for periods of between one and three months but not over the full sample"; "The outperformance of technical analysis disappears for the post-crisis period across all currencies" (SEK the exception).
- **Relevance:** None for a new item (no EUR/USD, no persistent rule, post-crisis null). Consistent with E049/E051 NONE on rule/ML families. **Status:** VERIFIED (partly summary-read).

### Evans & Speight, "Dynamic news effects in high frequency Euro exchange rates", Journal of International Financial Markets, Institutions and Money 20(3) (2010) 238-258 (added 2026-11-20 R316)
- **Link:** [EconPapers](https://econpapers.repec.org/RePEc:eee:intfin:v:20:y:2010:i:3:p:238-258) (opened via web-fetch; abstract only). Published version of the 2006 Cardiff WP logged above (R065).
- **Design/finding (abstract):** intraday EUR-USD and EUR-GBP, 5-minute reactions to macro announcements. Verbatim: "US macroeconomic news generates far more dramatic responses in EUR-USD returns"; reactions occur "within the first 5 min of the release". No out-of-sample direction or cost test.
- **Relevance:** None for a new item (contemporaneous reaction; UK-news spillover to EUR/USD smaller than US news; consistent with E026 NONE). **Status:** VERIFIED (abstract only).

### Hambuckers & Ulm, "Interest rate differentials and the dynamic asymmetry of exchange rates" (working paper, ORBi file dated February 2021) (added 2026-11-20 R316)
- **Link:** [ORBi PDF](https://orbi.uliege.be/bitstream/2268/257214/1/directional%20forecast%20with%20time%20varying%20skewness_february2021.pdf) (opened via web-fetch; data section and abstract verbatim, results summary-based). Journal/DOI not shown: UNVERIFIED.
- **Design/finding:** daily Fed noon rates, USD per EUR and per CHF, 6 Jan 1999 - 25 Mar 2019; time-varying skewness driven by the 3-month LIBOR differential (VIX robustness). Abstract (verbatim): out-of-sample performance "significantly superior to benchmark models" in "sign forecasts and trading profits", for "some periods of time". Summary-based: rolling 1,075 one-step forecasts; best EUR profit ARMAX(2) ~4.94%/yr gross; Giacomini-Rossi rejects zero profit at 5%, DM/GW inconclusive; evidence "less obvious after 2018". Costs not mentioned (UNVERIFIED).
- **Relevance:** Low. Daily LIBOR/€STR-SOFR differential is not in the pipeline (FRED access blocked, B12 note); gross only; effect fades after 2018 (inside our dev/val span). Not added. **Status:** VERIFIED (partly summary-read).

### Mukoyama, Kikuta & Washimi, "Investment Patterns of Japanese Retail Investors in Foreign Exchange Margin Trading", Bank of Japan Review 2018-E-3 (20 Nov 2018) (added 2026-11-20 R317)
- **Link:** [BoJ page](https://www.boj.or.jp/en/research/wps_rev/rev_2018/rev18e03.htm) (opened via web-fetch; abstract only; full-text PDF fetch not permitted: UNVERIFIED beyond the abstract).
- **Design/finding (abstract):** high-frequency transaction data of Japanese retail FX margin traders; positions held overnight or longer are contrarian; within-day trading can be trend-following "depending on the market situation"; within-day trading "does not necessarily reduce intraday fluctuations". No return-prediction, out-of-sample or cost test in the abstract; EUR/USD not mentioned.
- **Relevance:** None for a new item (behavioural description of flows, not a price-prediction result; retail positioning data not in the pipeline, R222). **Status:** VERIFIED (abstract only).

### Hayo & Iwatsubo, "Who Is Successful in Foreign Exchange Margin Trading? New Survey Evidence from Japan", Sustainability 14 (2022) 11662, doi:10.3390/su141811662 (added 2026-11-20 R317)
- **Link:** [Kobe University repository PDF](https://da.lib.kobe-u.ac.jp/da/kernel/0100476804/0100476804.pdf) (opened via web-fetch; ~40k of 60k characters verbatim, rest summary-based). Previously listed as a not-opened hit (MDPI 14/18/11662, ~R222 area).
- **Design/finding:** 2018 internet survey of 962 Japanese FX margin traders; cross-sectional OLS of self-reported trader profit/loss on age, strategy, trade amount, fundamental-analysis preference and self-rated skill. No exchange-rate return prediction, no EUR/USD.
- **Relevance:** None (trader-level survey, not a market-direction signal). **Status:** VERIFIED (partly summary-read).

### Gholizadeh & Narayanan (Quantitative Brokers), "Descriptive Study of U.S. Treasury Futures' Calendar Spread Around the Roll Period", CME Group, 20 Aug 2018 (added 2026-11-20 R319)
- **Link:** [CME PDF](https://www.cmegroup.com/market-data/files/a-descriptive-study-of-us-treasury-rolls-aug-20-2018.pdf) (opened via web-fetch).
- **Design/finding:** end-of-day settlements of ZB/ZN (1980-2018), ZF/ZT (from 1990), UB (from 2010); calendar-spread behaviour around the quarterly roll; descriptive full-sample correlations (early-roll vs later-roll spread changes ~18%, post-roll reversal ~-31%). No currencies, no forecast/OOS/cost test.
- **Relevance:** None (Treasury calendar spreads, no FX channel). **Status:** VERIFIED.

### Dedola, Georgiadis, Gräb & Mehl, "Does a big bazooka matter? Central bank balance-sheet policies and exchange rates", ECB Working Paper No 2197 (Nov 2018) (added 2026-11-20 R319)
- **Link:** [ECB PDF](https://ecb.europa.eu/pub/pdf/scpwps/ecb.wp2197.it.pdf) (opened via web-fetch; partly summary-read).
- **Design/finding:** monthly (weekly robustness), ~2009-2017 (summary-based, UNVERIFIED); local-projection impulse responses of USD/EUR to relative balance-sheet (QE) shocks; verbatim: APP "depreciated the euro vis-à-vis the US dollar by 12%". Structural attribution, no return-forecast, OOS or cost test.
- **Relevance:** None for a new item (monthly structural, ECB QE angle already covered ~R252 area). **Status:** VERIFIED (partly summary-read).

### Ahelegbey, Ibhagui & Gerth, "The Dollar's Double Life: Not All Dollar Appreciations Are Born Equal for the Cross-Currency Basis", Journal of Futures Markets (2026), doi:10.1002/fut.70081 (added 2026-11-20 R319)
- **Link:** [Essex repository PDF](https://repository.essex.ac.uk/42654/1/Ahelegbey%20-%20The%20Dollar%20s%20Double%20Life.pdf) (opened via web-fetch; partly summary-read).
- **Design/finding:** weekly Bloomberg G10 cross-currency basis (EUR 1Y-30Y), 2005-2021 (end date unclear); threshold regressions of basis changes on same-week dollar changes. Contemporaneous, no spot-return forecast, OOS or cost test.
- **Relevance:** None (explains the basis, not EUR/USD direction; cross-currency basis already covered). **Status:** VERIFIED (partly summary-read).

### McDonald, Suleman, Williams, Howison & Johnson, "Detecting a Currency's Dominance or Dependence using Foreign Exchange Network Trees", arXiv cond-mat/0412411 (Dec 2004) (added 2026-11-20 R320)
- **Link:** [arXiv PDF](https://arxiv.org/pdf/cond-mat/0412411) (opened via web-fetch, full text).
- **Design/finding:** hourly quotes 1 Apr 1993 - 30 Dec 1994 (08:00-16:00 GMT), 110 USD and cross series incl. USD/DEM (no EUR/USD); minimum-spanning-tree correlation clustering; lagged cross-correlations up to ~100 h show lead-lag under one hour only; authors state the method has no predictive power. No OOS or cost test.
- **Relevance:** None (pre-euro, descriptive, no usable lagged signal). **Status:** VERIFIED.

### Misik, "Forecasting and Correlation Dynamics in Regional and Global Currency Trios", PhD thesis, Corvinus University of Budapest (2026) (added 2026-11-20 R320)
- **Link:** [Corvinus PDF](https://phd.lib.uni-corvinus.hu/1517/1/PhD%20Thesis%20Sandor%20Misik.pdf) (opened via web-fetch; first ~40k of ~310k characters read, rest not read).
- **Design/finding:** daily 2005-2026 EUR/USD currency triangles with HUF, CZK, PLN, NOK, SEK, CHF, JPY, GBP; OOS one-month-ahead correlation forecasts (RMSE/QLIKE); ultra-high-frequency (100-200 ms) VAR/impulse-response spillovers within trios. Forecasts correlation, not direction; no trading or cost test seen; Chapter 4 results not read (UNVERIFIED).
- **Relevance:** None for an item (no EUR/USD direction forecast; ms-level spillovers are not tradable at SPEC 4 costs). Unreviewed thesis. **Status:** VERIFIED (partly read).

### Kočenda & Moravcová, "Exchange rate comovements, hedging and volatility spillovers on new EU forex markets", AEA 2019 preliminary paper (added 2026-11-20 R320)
- **Link:** [AEA conference page](https://aeaweb.org/conference/2019/preliminary/paper/bQA4KdAR) (opened via web-fetch; ~40k of 92k characters verbatim, rest summary-based).
- **Design/finding:** daily ECB reference rates 1999 - May 2018 for CZK/EUR, PLN/EUR, HUF/EUR and USD/EUR; DCC correlations (contemporaneous) and Diebold-Yilmaz volatility spillovers; HUF leads volatility in distress periods. No return-direction forecast, OOS or cost test.
- **Relevance:** None (volatility transmission, not EUR/USD direction). **Status:** VERIFIED (partly summary-read).

### Hashimoto & Ito, "Effects of Japanese Macroeconomic Announcements on the Dollar/Yen Exchange Rate: High-Resolution Picture", NBER WP 15020 (May 2009), published JJIE 24(3), 334-354 (2010) (added 2026-11-20 R321)
- **Link:** [NBER](https://www.nber.org/papers/w15020), DOI 10.3386/w15020 (abstract page opened via web-fetch; full PDF not read).
- **Design/finding:** EBS intraday quotes and deals, USD/JPY only; "Market impacts of Japanese macroeconomic announcements within minutes on the dollar/yen foreign exchange are analyzed"; Tankan, GDP, industrial production (preliminary), PPI among influential releases; announcements raise deals and volatility immediately after release. Contemporaneous/volatility focus; no directional drift, OOS or cost test on the abstract page; sample period UNVERIFIED.
- **Relevance:** None for an item (USD/JPY, no EUR/USD direction test). **Status:** VERIFIED (abstract only).

### Kamada, "Central bank's surprise policy and its potential to change people's deflationary mindset: evidence from the yen-dollar exchange market", Keio-IES DP2025-015 (14 Jul 2025) (added 2026-11-20 R321)
- **Link:** [Keio-IES PDF](https://ies.keio.ac.jp/upload/DP2025-015_EN.pdf) (opened via web-fetch; first part verbatim, rest summary-based).
- **Design/finding:** daily yen-dollar candlesticks (Nikkei NEEDS) 5 Jun 1984 - 15 May 2024 used to build a same-day BoJ surprise measure; outcomes are policy classification and the Phillips curve. No EUR/USD (no London/EU data), no direction forecast, OOS or cost test.
- **Relevance:** None. **Status:** VERIFIED (partly summary-read).

### Söderlind & Somogyi, "When does Liquidity matter?", AEA 2020 preliminary paper (version 6 Nov 2019) (added 2026-11-20 R322)
- **Link:** [AEA conference page](https://aeaweb.org/conference/2020/preliminary/paper/i5H7K9kR) (opened via web-fetch; extended abstract PDF).
- **Design/finding:** 15 USD-base pairs (EUR/USD inclusion not confirmed on the page), hourly CLS order flow Sep 2013 - Jan 2019 with Olsen quotes; low-frequency liquidity factor (PC of nine measures); monthly portfolios sorted on trailing 252-day liquidity betas. "FX liquidity is only priced conditional on volatility being high"; high-minus-low liquidity-beta portfolio 4.97% p.a., Sharpe 0.88, t 2.07 (cross-sectional, monthly). Cost robustness with quoted spreads "qualitatively unchanged"; no OOS test described.
- **Relevance:** None for an item (cross-sectional monthly risk premium, not a EUR/USD time-series direction signal; CLS data not in pipeline). **Status:** VERIFIED (extended abstract).

### Ranaldo & Santucci de Magistris, "Trading Volume, Illiquidity and Commonalities in FX Markets", AEA 2020 preliminary paper (20 Dec 2019) (added 2026-11-20 R322)
- **Link:** [AEA conference page](https://aeaweb.org/conference/2020/preliminary/paper/8nYYaKbD) (opened via web-fetch; first part verbatim, rest summary-based). Working-paper precursor of the JFE 2022 paper already logged above (line ~276).
- **Design/finding:** 29 pairs incl. EURUSD, hourly CLS volume Nov 2011 - Oct 2016, Olsen quotes, EBS 2016; HF Amihud illiquidity; contemporaneous volume/volatility/illiquidity regressions and commonality ("EURUSD is by far the most traded FX rate, with a share above 30% between 7AM to 6PM"). No return-predictability, OOS or cost test.
- **Relevance:** None (contemporaneous). **Status:** VERIFIED (partly summary-read).

### Mancini, Ranaldo & Wrampelmeyer, "Liquidity in the Foreign Exchange Market: Measurement, Commonality, and Risk Premiums", AEA 2012 paper (version 16 Dec 2011), published J. Finance 68(5), 1805-1841 (2013) (added 2026-11-20 R322)
- **Link:** [AEA 2012 PDF](https://aeaweb.org/conference/2012/retrieve.php?pdfid=585) (opened via web-fetch; first part verbatim, rest summary-based; journal DOI not opened).
- **Design/finding:** 1-second EBS data, 9 pairs incl. EUR/USD ("EUR/USD is the most liquid exchange rate"), daily liquidity measures Jan 2007 - Dec 2009; strong liquidity commonality; liquidity risk factor priced in carry returns (contemporaneous). Lagged VIX/TED predict next-day liquidity, not FX returns. No direction forecast, OOS or net-of-cost test. Table values read only via summary: UNVERIFIED.
- **Relevance:** None for an item. **Status:** VERIFIED (partly summary-read).

### Fortes & Le Guenedal, "Tracking ECB's Communication: Perspectives and implications for financial markets", MPRA Paper 108746 (Dec 2020, posted 22 Jul 2021) (added 2026-11-21 R323)
- **Link:** [MPRA PDF](https://mpra.ub.uni-muenchen.de/108746/1/MPRA_paper_108746.pdf) (opened via web-fetch; first part verbatim, rest summary-based).
- **Design/finding:** text database of ECB speeches, interviews and press conferences 1997 - Jul 2020; Lasso-selected OLS of same-day daily EUR/USD change on same-day topic signals, 2002 - Jul 2020 in three sub-periods; text "improve[s] financial-linked models consistently in all periods analyzed (2.5% on average)" (adjusted R2). Contemporaneous; authors state they "did not test for the value added of this database in a predictive process". No OOS or cost test. Table values read only via summary: UNVERIFIED.
- **Relevance:** None for an item (contemporaneous, no lagged direction test; ECB-day family already tested). **Status:** VERIFIED (partly summary-read).

### Nguyen (co-author UNVERIFIED), "ECB's central bank communication and monetary policy transmission: predictability from text-based sentiment indicators?", Macroeconomic Dynamics 29, e102 (2025), doi:10.1017/S1365100525000239 (added 2026-11-21 R323)
- **Link:** [Cambridge Core](https://www.cambridge.org/core/journals/macroeconomic-dynamics/article/ecbs-central-bank-communication-and-monetary-policy-transmission-predictability-from-textbased-sentiment-indicators/9A8225BEFA56175C87F3FD7DA47DE35C) (opened via web-fetch; partly summary-read).
- **Design/finding:** press-conference sentiment (266 meetings 1998-2022) -> EONIA, policy-rate and SPF expectations, in-sample lags 0-12; no exchange rate, no OOS, no trading/cost test.
- **Relevance:** None. **Status:** VERIFIED (partly summary-read).

### Collodel, "Interpreting the Interpreter: Can We Model Post-ECB Conferences Volatility with LLM Agents?", arXiv:2508.13635 (v4, May 2026) (added 2026-11-21 R323)
- **Link:** [arXiv PDF](https://arxiv.org/pdf/2508.13635) (opened via web-fetch; partly summary-read).
- **Design/finding:** LLM-agent "synthetic disagreement" from ECB press-conference transcripts -> next-day euro-area OIS high-low range (3M/2Y/10Y), 1998 - Mar 2026; Spearman 0.38-0.53 in sample, small OOS (10 conferences). Volatility of rates, not EUR/USD direction; no cost test.
- **Relevance:** None. **Status:** VERIFIED (partly summary-read).

### Nolte & Nolte, "The Information Content of Retail Investors' Order Flow" (Lancaster working version 7 Nov 2014) (added 2026-11-21 R323)
- **Link:** [Lancaster eprints PDF](https://eprints.lancs.ac.uk/71649/1/_paper.pdf) (opened via web-fetch; venue not read).
- **Design/finding:** OANDA retail order flow, EUR/USD focus, Oct 2003 - May 2004; lagged retail order-flow categories improve 1-5 minute mid-quote forecasts OOS (last 4 weeks; modified DM test). No net-of-cost trading test; retail order-flow data not in the pipeline; minute horizon far below cost hurdle.
- **Relevance:** None for an item (data unavailable; horizon too short for SPEC 4 costs). **Status:** VERIFIED (partly summary-read).

### Temprano Arroyo, "The EU's Response to the COVID-19 Crisis: A Game Changer for the International Role of the Euro?" (European Economy Discussion Paper 164, Jun 2022; doi:10.2765/24542) (added 2026-11-21 R324)
- **Link:** [European Commission PDF](https://economy-finance.ec.europa.eu/system/files/2022-11/dp164_en_0.pdf) (opened via web-fetch; middle sections summary-read).
- **Design/finding:** descriptive policy analysis of NGEU/SURE safe-asset supply, reserve shares (COFER 1995-2020), investor composition, spreads over Bunds and bid-ask liquidity; verbatim: NGEU/SURE are "unlikely to sufficiently boost on their own the euro's global role". No exchange-rate return, event-study, OOS or cost test.
- **Relevance:** None. **Status:** VERIFIED (partly summary-read).

### Liu & Xie, "Forecasting swap rate volatility with information from swaptions", BIS Working Paper 1068 (25 Jan 2023) (added 2026-11-21 R325)
- **Link:** [BIS abstract page](https://www.bis.org/publ/work1068.htm) (opened via web-fetch; abstract page only, 48-page PDF not read).
- **Design/finding:** model-free implied volatility from OTC swaption quotes -> future realized volatility of swap rates across tenors; abstract: it "demonstrates significant predictability on future realized volatility of swap rates" and holds "out of sample". Currencies, sample and frequency UNVERIFIED (PDF not read). Volatility of rates only; no FX direction, no cost test.
- **Relevance:** None. **Status:** VERIFIED (abstract only).

### Della Corte, Ramadorai & Sarno, "Volatility Risk Premia and Exchange Rate Predictability", J. Financial Economics 120(1), 21-40 (2016), doi:10.1016/j.jfineco.2016.02.015 (accepted manuscript Feb 2015) (added 2026-11-21 R325; supplements the R180 CEPR DP9549 entry, which stays as written)
- **Link:** [City Research Online PDF](https://openaccess.city.ac.uk/id/eprint/13156/1/VRP_Paper_18Feb2015%20%28with%20Figures%29.pdf) (opened via web-fetch; first ~35% verbatim, rest summary-based; journal DOI not opened).
- **Design/finding:** VRP = 1-year realized vol minus 1-year volatility-swap rate from JP Morgan OTC implied vols; monthly end-of-month quintile sorts over 10 developed (incl. Euro Area) and 20 developed+emerging USD pairs, Jan 1998 - Dec 2013; verbatim: "currencies with relatively cheap volatility insurance tend to appreciate"; excess returns "adjusted for transaction costs using bid-ask quotes on spot and forward rates". Net Sharpe ratios (0.61 / 0.51) and the OOS design read only via summary: UNVERIFIED. EUR/USD not reported as a single-pair time-series test.
- **Relevance:** None for an item (cross-sectional, monthly, OTC option-implied vol not in the pipeline). **Status:** VERIFIED (partly summary-read).


### Greenwood, Hanson, Stein & Sunderam, "A Quantity-Driven Theory of Term Premia and Exchange Rates", Quarterly Journal of Economics 138(4), 2327-2389 (2023), doi:10.1093/qje/qjad024 (added 2026-11-21 R326)
- **Link:** [Harvard scholar page PDF](https://stein.scholars.harvard.edu/resource/pdf-30) (opened via web-fetch; ~48% verbatim, rest summary-based); advance-access copy [pdf-26](https://stein.scholars.harvard.edu/resource/pdf-26) also opened (first ~40k chars verbatim). Journal DOI not opened.
- **Design/finding:** monthly panel of six USD pairs incl. EUR, 2001m1-2021m12; lagged foreign-minus-US 3y7y forward-rate differential (term-premium proxy) predicts 3- and 12-month borrow-USD/lend-foreign excess returns (pooled 12-month coefficient -3.59, SE 1.03; N 1,440; within R2 0.04); authors say results are "strong for ... EUR" in isolation, no EUR-only table read. Daily QE event study 2008-2019 (N 128) is contemporaneous. No out-of-sample or transaction-cost test found (absence partly summary-based).
- **Relevance:** None for an item (monthly horizon gives far too few dev observations; carry-inclusive excess return, not spot direction; zero-coupon forward-rate data not in the pipeline). **Status:** VERIFIED (partly summary-read).

### Raza, Marshall & Visaltanachoti, "Is there momentum or reversal in weekly currency returns?", J. International Money and Finance 45, 38-60 (2014), doi:10.1016/j.jimonfin.2014.02.009 (added 2026-11-21 R326)
- **Link:** [EconPapers abstract](https://econpapers.repec.org/RePEc:eee:jimfin:v:45:y:2014:i:c:p:38-60) (opened via web-fetch; abstract only, full text paywalled).
- **Design/finding:** cross-section of 63 currencies, 1-4 week formation; "Momentum strategy returns are as large as 8% p.a." EUR/USD time-series result, sample period, OOS and cost tests not on the abstract page (UNVERIFIED).
- **Relevance:** None (cross-sectional; weekly EUR/USD reversal family already reviewed R174/R19x, below the dev power floor). **Status:** VERIFIED (abstract only).

### Kearney, Cummins & Murphy, "Forecasting Implied Volatility in Foreign Exchange Markets: A Functional Time Series Approach", European Journal of Finance (forthcoming at time of the repository copy; DOI not shown) (added 2026-11-21 R327)
- **Link:** [DORAS (DCU) accepted manuscript PDF](https://doras.dcu.ie/24127/1/MARK%20CUMMINS%20EJOF%20FOR%20DORAS.pdf) (opened via web-fetch; first ~55% verbatim, rest summary-based).
- **Design/finding:** daily Bloomberg ATM, risk-reversal and butterfly implied-vol quotes for EUR-USD, EUR-GBP, EUR-JPY (1-9 month maturities), Jan 2006 - Nov 2013; functional time-series model forecasts one-day-ahead implied-volatility levels/changes, recursive OOS Dec 2011 - Nov 2013: "the FTS model significantly outperforms implied volatility forecasts produced by traditionally employed parametric models." Does not test spot-return direction; butterfly/risk reversal are smile inputs, not spot predictors.
- **Relevance:** None for an item (forecasts implied vol, not EUR/USD spot direction; OTC option data not in the pipeline). **Status:** VERIFIED (partly summary-read).
- City, University of London eprint 24959 ("Cross section of FX options returns and volatility", filename only) blocked by bot wall: UNVERIFIED, not used.

### Martins & Lopes, "What events matter for exchange rate volatility?", arXiv 2411.16244v1 (Oct 2024) (added 2026-11-21 R328)
- **Link:** [arXiv HTML](https://arxiv.org/html/2411.16244v1) (opened via web-fetch; first ~40,000 characters verbatim, rest summary-based).
- **Design/finding:** 5-minute AUD and CHF returns vs USD, Jan 2017 - Dec 2023 (OOS from Jul 2022); 117 US/Australian events (Bloomberg calendar) enter a stochastic-volatility model's log-variance for up to 30 minutes; returns modelled as zero-mean. Verbatim: "we find a link between intraday seasonality, trading volume, and the opening hours of major markets across the globe."
- **Relevance:** None for an item (volatility only, no return-direction or drift test, no EUR/USD or euro-area events, no costs). **Status:** VERIFIED (partly summary-read).

### Gordon & Lunsford, "The Effects of the Federal Reserve Chair's Testimony on Interest Rates and Stock Prices", FRB Cleveland Working Paper 23-26 (Nov 2023), doi:10.26509/frbc-wp-202326 (added 2026-11-21 R329)
- **Link:** [Cleveland Fed WP 23-26 PDF](https://www.clevelandfed.org/-/media/project/clevelandfedtenant/clevelandfedsite/publications/working-papers/2023/wp2326.pdf) (opened via web-fetch). Companion: [Economic Commentary EC 2024-01](https://www.clevelandfed.org/publications/economic-commentary/2024/ec-202401-effects-of-federal-reserve-chairs-testimony), doi:10.26509/frbc-ec-202401 (opened; page text partly summary-read).
- **Design/finding:** minute-level Eurodollar futures, 2/5/10-year Treasury yields and S&P 500 around 179 Fed Chair testimonies (125 Monetary Policy Report, 54 other), Jul 1991 - Mar 2023; window 15 min before start to 15 min after end. Interest-rate moves largest around first-day MPR testimonies; "Second-day MPR testimonies cause the smallest movements in interest rates and generate no co-movement" (abstract wording as reported).
- **Relevance:** None for an item (no exchange rate tested; contemporaneous window only; no drift, OOS or cost test). **Status:** VERIFIED.

### Koch & Yung, "Macroeconomic News and Asset Prices Before and After the Zero Lower Bound", FRB Dallas Globalization and Monetary Policy Institute WP 287 (Oct 2016) (added 2026-11-21 R329)
- **Link:** [Dallas Fed GMPI WP 287 PDF](https://www.dallasfed.org/institute/~/media/documents/institute/wpapers/2016/0287.pdf) (opened via web-fetch).
- **Design/finding:** 21 US macro announcements (NFP, CPI, GDP, claims, etc.) vs Bloomberg consensus, 1996-10 - 2016-01 split pre/post 2008; 5-minute 10-year T-note futures and EUR, GBP, JPY, AUD, CAD futures; symmetric window around release. "domestic interest rates tend to be more sensitive to U.S. macroeconomic news than exchange rates."
- **Relevance:** None for an item (contemporaneous announcement responses only, no later-drift, OOS or cost test; regional Fed surveys not singled out). **Status:** VERIFIED.

### Žukovič, "Dynamics of episodic transient correlations in currency exchange rate returns and their predictability", arXiv:1301.1893 (Jan 2013, preprint) (added 2026-11-21 R337)
- **Link:** [arXiv PDF](https://arxiv.org/pdf/1301.1893) (opened via web-fetch, full text).
- **Design/finding:** hourly average rates per euro for USD, CAD, CHF, GBP, JPY (EUR/USD included), 2004-03-01 .. 2009-12-17, 37,620 obs; rolling portmanteau test flags windows of significant autocorrelation, then next-hour direction = sign(lag-1 autocorrelation x last standardized return). Verbatim: "during these relatively brief periods the returns are predictable to a certain degree." Hit rate ~0.5 on random data.
- **Relevance:** None for an item (hourly, in-sample evaluation, no costs; same hourly autocorrelation / variance-ratio family already covered R199, R~2329). **Status:** VERIFIED.

### Grobys & Heinonen, "Does Option-Implied Cross-Sectional Return Dispersion Forecast Realized Cross-Sectional Return Dispersion? Evidence From the G10 Currencies", J. Futures Markets 37(1), 3-22 (2017) (added 2026-11-21 R337)
- **Link:** [RePEc/IDEAS record](https://ideas.repec.org/a/wly/jfutmk/v37y2017i1p3-22.html) (abstract only; full text not opened: data details UNVERIFIED).
- **Design/finding:** option-implied cross-sectional variance (1- and 3-month options) "outperforms past cross-sectional return variance in forecasting future cross-sectional return variance."
- **Relevance:** None for an item (forecasts dispersion, not EUR/USD direction; needs OTC option data not in the pipeline). **Status:** VERIFIED (abstract only).

### Wellmann & Trück, "Exchange Rates and Unobservable Fundamentals: A New Approach to Out-of-sample Forecasting", Macquarie University WP 16-07 (Oct 2016) (added 2026-11-21 R346)
- **Link:** [Macquarie PDF](https://www.mq.edu.au/__data/assets/pdf_file/0010/583282/working_paper_16-07.pdf) (opened via web-fetch; ~40% read verbatim, results/trading section model-summarised: UNVERIFIED).
- **Design/finding:** monthly USD vs AUD, CAD, CHF, JPY, GBP plus three crosses, 1995-01 .. 2014-12, rolling 60-month window; predictors = foreign-minus-US yield-spread level and slope; horizons 1-12 months. Verbatim: "We do not include the Euro because there is no Euro yield curve"; abstract: "superior to a random walk in terms of direction of change forecasts and profitability". Cost treatment UNVERIFIED.
- **Relevance:** None for an item (monthly, EUR/USD excluded, far below the R090 power floor on dev; same yield-curve-factor family as Chen & Tsang, R226). **Status:** VERIFIED (partial read).

### Gräb & Kostka, "Predicting risk premia in short-term interest rates and exchange rates", ECB preliminary paper (ICMAIF 2018) (added 2026-11-21 R346)
- **Link:** [ICMAIF PDF](https://icmaif.soc.uoc.gr/Year/2018/papers/paper_3_69.pdf) (opened via web-fetch, main body read).
- **Design/finding:** monthly G10 panel incl. USD/EUR (DEM before 1999), 1997-04 .. 2015-12; relative 3m/2y/10y yields and Nelson-Siegel factors predict excess currency returns 1-12 months ahead. Verbatim: "can predict, in-sample, both surprises in money market rates ... and future exchange rate risk premia". No OOS, no costs.
- **Relevance:** None for an item (monthly, in-sample only, no cost test; yield-curve-factor family already covered R226). **Status:** VERIFIED.


### Harris, Karadotchev, Sowerbutts & Stoja, "Have FSRs got news for you? Evidence from the impact of Financial Stability Reports on market activity", Bank of England Staff WP 792 (Apr 2019) (added 2026-11-22 R348)
- **Link:** [BoE page](https://www.bankofengland.co.uk/working-paper/2019/have-fsrs-got-news-for-you) / [PDF](https://www.bankofengland.co.uk/-/media/boe/files/working-paper/2019/have-fsrs-got-news-for-you.pdf) (opened via web-fetch; ~40k chars verbatim, remainder model-summarised: UNVERIFIED).
- **Design/finding:** daily returns, volume, spreads of 73 UK-listed financials and CDS of 7 large UK banks, Jan 2010 .. Jan 2018, 16 FSR publications, event window day 0..+2, bootstrap vs random days. Verbatim: "publication of the FSR is, on average, associated with no abnormal returns". No FX, no OOS, no costs.
- **Relevance:** None for an item (no exchange-rate test; semi-annual events far below the R090 power floor). **Status:** VERIFIED (partial read).

### D'Amico, King & Torralba, "How Do Market Expectations React to the FOMC Dot Plot?", NY Fed Staff Report 1204 (Sep 2026); also Chicago Fed Letter 527 (2026) (added 2026-11-22 R349)
- **Link:** [NY Fed PDF](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr1204.pdf) (opened via web-fetch, read verbatim) / [Chicago Fed Letter 527](https://www.chicagofed.org/publications/chicago-fed-letter/2026/527) (opened; ~40k of 124k chars verbatim, remainder model-summarised: UNVERIFIED).
- **Design/finding:** quarterly SEP (dot plot) releases, Sep 2015 .. Jun 2026; daily and 30-minute event windows on OIS forward rates (fed funds futures before Sep 2023); surprises vs NY Fed SME / Bloomberg surveys; VECM for convergence. Same-day pass-through ~0.2 of the FFR-path surprise, then gradual convergence over ~two quarters. Verbatim: "the market only partially and gradually takes on board the unexpected changes in the SEP projections". Interest rates only: no EUR/USD or USD exchange-rate test, no OOS, no costs.
- **Relevance:** None for an item: rates-only drift measured over quarters; the SEP surprise needs survey data not in the pipeline; ~24 SEP meetings on dev are below the R090 power floor; FOMC statement-day EUR/USD already tested (E013 SIGNAL dev / E014 NONE val). **Status:** VERIFIED (NY Fed PDF read in full).

### Arabadjis, Melvin, Savage & Velis, "Seasonal affective disorder and currency markets", Annals of Operations Research 346(1), 549-565 (Mar 2025), doi:10.1007/s10479-024-06364-z (added 2026-11-22 R350)
- **Link:** [IDEAS/RePEc abstract page](https://ideas.repec.org/a/spr/annopr/v346y2025i1d10.1007_s10479-024-06364-z.html) (opened via web-fetch; abstract only, full text paywalled: methodology UNVERIFIED).
- **Design/finding (abstract):** daylight-driven (SAD) seasonality in currency positioning and returns; verbatim "In the spring/summer season of long daylight hours, we find evidence of greater short positions for the euro." and "Finally, we construct and backtest a SAD-inspired currency portfolio." Whether the backtest is out-of-sample or net of costs is not stated; a EUR/USD-specific return rule is not given in the abstract.
- **Relevance:** None for an item now: positioning data not in the pipeline; return rule, OOS and costs UNVERIFIED; a half-year seasonal regime gives only ~6 independent cycles on dev (2015-2020), below the R090 power floor. **Status:** VERIFIED (abstract only).

### Ehrmann & Jansen, "It Hurts (Stock Prices) When Your Team Is About to Lose a Soccer Match", Bank of Canada WP 2014-2 (Jan 2014) (added 2026-11-22 R350)
- **Link:** [BoC PDF](https://www.bankofcanada.ca/wp-content/uploads/2014/01/wp2014-2.pdf) (opened via web-fetch; PDF truncated, table details model-summarised: UNVERIFIED).
- **Design/finding:** minute-by-minute STMicroelectronics prices in Paris vs Milan, 3 May - 30 Jul 2010, around France/Italy 2010 World Cup matches; verbatim "During the soccer matches, stock prices in the country that eventually loses are lower by up to seven basis points." No exchange rates, no OOS, no costs.
- **Relevance:** None (single stock, intraday, no FX; sports events far too rare for a dev test). **Status:** VERIFIED (partial read).

### Frieder & Subrahmanyam, "Non-Secular Regularities in Stock Returns: The Impact of the High Holy Days on the U.S. Equity Market", Financial Analysts Journal (forthcoming per working paper dated 2002-02-06) (added 2026-11-22 R351)
- **Link:** [eScholarship record](https://escholarship.org/uc/item/8jb1q6z6) and [PDF](https://escholarship.org/content/qt8jb1q6z6/qt8jb1q6z6.pdf) (opened via web-fetch; ~40k of ~55k chars verbatim, rest model-summarised: UNVERIFIED). Final published version not checked.
- **Design/finding:** daily S&P 500 returns and NYSE dollar volume, Jul 1962 - Dec 2000 (returns extended back to 1946). Verbatim "returns are significantly positive around Rosh HaShanah and significantly negative around Yom Kippur." Window t-stats +2.14 (Rosh HaShanah 3-day) and -2.31 (Yom Kippur 2-day); single-day dummies n.s.; volume falls on both days. No FX, no forward OOS, no costs; authors call results "far from conclusive".
- **Relevance:** None for an item: US equities only; ~2 events per year gives ~12 Rosh HaShanah and ~12 Yom Kippur dates on dev, far below the R090 power floor; no EUR/USD mechanism beyond thin US liquidity (holiday-liquidity angles already covered). **Status:** VERIFIED (partial read).

### Batrinca, Hesse & Treleaven, "European trading volumes on cross-market holidays", International Journal of Finance & Economics 23, 675-704 (2018), doi:10.1002/ijfe.1643 (added 2026-11-22 R351)
- **Link:** [UCL Discovery PDF](https://discovery.ucl.ac.uk/id/eprint/10059527/1/Batrinca_et_al-2018-International_Journal_of_Finance_%2526_Economics.pdf) (opened via web-fetch; ~40k of ~113k chars verbatim, results sections model-summarised: UNVERIFIED).
- **Design/finding:** ~2,353 pan-European stocks, 21 countries, Jan 2000 - May 2015; verbatim "The trading volumes on dates when there is at least one cross-market holiday are on average 8.5% lower than the volumes of the previous period." Volume only; no returns, no FX, no costs; validation by cross-validation (not a chronological holdout).
- **Relevance:** None (equity volume, no direction claim, no FX). **Status:** VERIFIED (partial read).

### Hayes (IHS Markit), "Estimating short-term FX equilibria using PMIs: EUR/USD case study", vendor commentary dated 19 Oct 2021 (added 2026-11-22 R352)
- **Link:** [PDF](https://cdn.ihsmarkit.com/www/pdf/1021/FX-model-21-10-18.pdf) (opened via web-fetch; 4 pages, full verbatim text).
- **Design/finding:** OLS "short-term 'fair value'" of the EUR/USD level on contemporaneous 6-month rolling eurozone-minus-US manufacturing output and input-price PMI differentials, STOXX 600 minus S&P 500 6-month return, Bund-UST 10y spread and BTP 10y yield, Jan 2004 - Sep 2021; verbatim "explain approximately 70% of the variation in EUR/USD"; PMIs add ~6 pp adjusted R2. Misvaluation > 1 SD followed by "sharp movements" is a visual claim with no test. In-sample, no lagged predictor, no OOS, no costs.
- **Relevance:** None for an item (contemporaneous level fit; PMI data not in pipeline). **Status:** VERIFIED (full read).

### Pan (S&P Global Market Intelligence), "Using PMI data to gauge the direction of the US dollar index", blog 23 Jul 2025 (added 2026-11-22 R352)
- **Link:** [page](https://www.spglobal.com/market-intelligence/en/news-insights/research/2025/07/using-pmi-data-to-gauge-the-direction-of-the-us-dollar-index) (opened via web-fetch; ~40k of ~124k chars verbatim, rest model-summarised: UNVERIFIED).
- **Design/finding (as extracted):** monthly PMI-based regression signals for the broad USD index, entry on the 6th of each month, May 2012 - May 2025; reports win rates only (~55% simple, 59% multi-factor, 64% in a 3-year point-in-time test from May 2022). No returns, no costs, no EUR/USD pair result.
- **Relevance:** None for an item (USD index, monthly, ~72 monthly signals on dev, win-rate only, PMI data not in pipeline). **Status:** VERIFIED (partial read).

### Baldovin, Camana, Caraglio, Stella & Caporin, "Ensemble properties of high frequency data and intraday trading rules", arXiv:1202.2447v2 (2013) (added 2026-11-22 R352)
- **Link:** [arXiv PDF](https://arxiv.org/pdf/1202.2447) (opened via web-fetch; ~40k of ~70k chars verbatim, OOS tables model-summarised: UNVERIFIED).
- **Design/finding:** S&P 500 10-minute returns 1985-2010; martingale-scaling conditional-density bounds give trend-following intraday signals; rolling 15-year calibration with forward evaluation; verbatim in-sample Table I average profit 4.479 bp per trade (25% quantile). No costs ("profits ... would be sensibly reduced" per summary); no FX results.
- **Relevance:** None for an item (equity index, no costs, no EUR/USD; intraday trend/quantile-breakout family already tested in E048/E049). **Status:** VERIFIED (partial read).

### Bieganowski & Slepaczuk, "Explainable Patterns in Cryptocurrency Microstructure", arXiv:2602.00776 (2026) (added 2026-11-22 R354)
- **Link:** [arXiv PDF](https://arxiv.org/pdf/2602.00776) (opened via web-fetch; ~40k of ~59k chars verbatim; sections 8-9 not verified: UNVERIFIED).
- **Design/finding:** Binance Futures perpetuals (BTC, LTC, ETC, ENJ, ROSE), 1-second order books 2022-01-01..2025-10-12; order-flow imbalance, spread and VWAP-to-mid features in CatBoost predict the 3-second log mid return; purged walk-forward CV, outer folds only; taker fills at best bid/ask, gross and fee-adjusted. Taker t-tests significant at 5% only for ETC, ENJ, ROSE; ROSE "largely due to the extreme event on 2025-10-10" (verbatim). No FX.
- **Relevance:** None for an item (crypto, 3-second horizon, full order book not in the Dukascopy pipeline, no EUR/USD). **Status:** VERIFIED (partial read).

### Farrell & O'Connor, "The CNN Fear and Greed Index as a predictor of US equity index returns: Static and time-varying Granger causality", Finance Research Letters 72 (2025) (doi:10.1016/j.frl.2024.106492) (added 2026-11-22 R356)
- **Link:** [IDEAS/RePEc](https://ideas.repec.org/a/eee/finlet/v72y2025ics1544612324015216.html) (abstract/metadata only; full text paywalled: details beyond the abstract UNVERIFIED).
- **Design/finding:** static and Shi et al. (2020) time-varying Granger tests of the CNN Fear and Greed Index on S&P 500, Nasdaq, Russell 3000 and gold returns, 2011-2020 and 2021-2024; verbatim "the Fear and Greed Index Granger causes returns on the S&P 500" (2011-2020), weaker 2021-2024, possibly "driven by a stronger relationship existing pre-2014". In-sample only; no FX, no costs.
- **Relevance:** None for an item (equities/gold, in-sample, no EUR/USD; index not in pipeline). **Status:** VERIFIED (abstract).

### Mahmoud (Vontobel Asset Management), "Currency of Emotions" (practitioner article, undated; chart files suggest Jan 2025) (added 2026-11-22 R356)
- **Link:** [Vontobel insights](https://am.vontobel.com/en/insights/currency-of-emotions) (full text read via web-fetch).
- **Design/finding:** RavenPack macro/currency news sentiment for 7 unnamed currencies vs USD, monthly long-positive/short-negative rebalancing, 2005-2024; verbatim "achieving a Sharpe ratio of approximately 1.2", "driven primarily by the short leg". Hypothetical full-sample backtest; no OOS split, no costs; EUR/USD not named.
- **Relevance:** None for an item (cross-sectional monthly basket, RavenPack data not in pipeline, no OOS/costs; news-sentiment family already reviewed R121/R166/R355). **Status:** VERIFIED (practitioner, not peer reviewed).

### Fornari & Zaghini, "It's not time to make a change: sovereign fragility and the corporate credit risk", ECB WP 2740 (2022) (added 2026-11-22 R356)
- **Link:** [ECB PDF](https://www.ecb.europa.eu/pub/pdf/scpwps/ecb.wp2740~927e1f5458.en.pdf) (~40k of ~90k chars verbatim; rest model-summarised: UNVERIFIED; DOI not verified).
- **Design/finding:** 68 unconfounded euro-area sovereign downgrades 2006-2018, weekly corporate CDS changes; verbatim "the delivery of a sovereign downgrade has a negative spillover to the euro area corporate credit risk". Euro NEER is a control only; no EUR/USD test, no OOS, no costs.
- **Relevance:** None for an item (CDS outcome; sovereign-rating -> EUR/USD angle already reviewed R169/R235). **Status:** VERIFIED (partial read).

### Donati & Jung, "Gold Price Dynamics Around the Clock", MSc thesis, Copenhagen Business School (2019; supervisor P. Whelan) (added 2026-11-22 R357)
- **Link:** [CBS research portal](https://research.cbs.dk/en/studentProjects/gold-price-dynamics-around-the-clock/) (abstract and metadata only; full thesis not linked/opened: body UNVERIFIED).
- **Design/finding:** intraday 24h gold returns, eastern vs western trading hours; verbatim "We find a hat-shaped intraday seasonality, with gold appreciating during eastern trading hours in a robust way" and "in the years of alleged manipulation gold prices drop around the London fixing times". Backtests up to Sharpe 1.61 before costs; after costs underperform the market but "still show some profitability". Sample, data source and OOS design not stated on the page.
- **Relevance:** None for an item (gold, not EUR/USD; no FX test; student thesis; London-fix return patterns already covered for FX via Evans / Marsh-Panagiotou-Payne / Krohn-Mueller-Whelan). **Status:** VERIFIED (abstract only).

### Zhang, Feng & Wei, "Realized skewness of oil price returns and the short-term predictability for exchange rate", Quantitative Finance 25(7):1031-1046 (2025) (added 2026-11-22 R359)
- **Link:** [IDEAS/RePEc](https://ideas.repec.org/a/taf/quantf/v25y2025i7p1031-1046.html); DOI 10.1080/14697688.2025.2522177 (listed on IDEAS; publisher full text paywalled, not opened: body UNVERIFIED).
- **Design/finding (abstract):** realized skewness of oil returns predicts exchange-rate returns for nine countries; verbatim "statistically and economically more effective than the random walk model". Currency pairs, data frequency, OOS design and transaction costs not stated on the page (UNVERIFIED); EUR/USD not named.
- **Relevance:** None for an item (needs intraday oil data not in pipeline; EUR/USD inclusion, OOS and costs unverified; lagged-oil -> EUR/USD mechanism already rejected, see rejected_hypotheses.md / R335). **Status:** VERIFIED (abstract only).

### Goudvis, "A Cointegration Trading Strategy for Currency Exchange Rates", Bachelor thesis, Erasmus School of Economics (2020; supervisor L. A. P. Swinkels) (added 2026-11-22 R360)
- **Link:** [EUR thesis repository PDF](https://thesis.eur.nl/pub/53210/Final-A-Cointegration-Trading-Strategy-for-Currency-Exchange-Rates-Bachelor-paper-by-Jeroen-Goudvis.pdf) (opened via web-fetch; first ~40k of ~70k characters verbatim, remainder summarised: later sections partly UNVERIFIED).
- **Design/finding:** daily spot rates of 27 USD-quoted currencies, 2000-2019; pairs selected by cointegration on 2000-2009, distance-rule trading 2010-2019 (open at 2 rolling SD, close at crossing). Verbatim abstract: 38 closed positions, "an average realized return of 6,5% over 10 years", significant at 1%. No transaction costs, no Sharpe ratio; EUR/USD cannot be a leg (USD is the base currency of every series).
- **Relevance:** None for an item (no EUR/USD leg, no costs, 38 trades over 10 years, student thesis; cointegration/pairs angle already reviewed ~backlog line 2686). **Status:** VERIFIED (partial read).

### Ghazei, "High-Frequency Identification of Monetary Policy Surprises in Canada: Evidence from Intraday Exchange Rate Data", MA extended essay, University of Victoria (2025) (added 2026-11-22 R361)
- **Link:** [UVic PDF](https://www.uvic.ca/socialsciences/economics/_assets/docs/pantea-ghazei-exteneded-essay.pdf) (opened via web-fetch; first ~40k of ~48k characters verbatim, remainder UNVERIFIED).
- **Design/finding:** minute USD/CAD 2001-2024 around 53 Bank of Canada announcements; intraday-window surprise measures (w = 1..10 min), contemporaneous only. Verbatim conclusion: "markets regularly misjudge either the magnitude or the direction of the Bank's intended move." No later-return/drift test, no OOS, no costs; EUR/USD not included.
- **Relevance:** None for an item. **Status:** VERIFIED (partial read).

### Ferrari, Kearns & Schrimpf, "Monetary policy's rising FX impact in the era of ultra-low rates", BIS Working Paper 626 (2017) (added 2026-11-22 R361)
- **Link:** [BIS landing page](https://www.bis.org/publ/work626.pdf) (abstract opened; PDF body fetch refused: body UNVERIFIED).
- **Design/finding (abstract):** high-frequency event study of policy news from seven central banks, 2004-2015; verbatim "The FX impact of monetary policy is state-dependent and is stronger the lower the level of interest rates." Event-window (contemporaneous) reaction; pairs, any later-return test, OOS and costs UNVERIFIED.
- **Relevance:** None for an item (contemporaneous; central-bank announcement family already tested, E013/E022-E025). **Status:** VERIFIED (abstract only).

### Istrefi, Odendahl & Sestieri, "ECB Communication and its Impact on Financial Markets", Banque de France WP 859 (Dec 2021, rev. Apr 2025); also Banco de España Documento de Trabajo 2431 (2024), doi:10.53479/37792 (added 2026-11-22 R362)
- **Links:** [Banque de France WP859 PDF](https://www.banque-france.fr/system/files/2025-05/WP859.pdf); [Banco de España DT 2431 PDF](https://repositorio.bde.es/bitstream/123456789/37792/1/dt2431e.pdf) (both opened via web-fetch; early pages verbatim, later results UNVERIFIED).
- **Design/finding:** minute-by-minute mid-quotes (Refinitiv) of 47 euro-area market variables including EUR/USD, Jan 1999 - 16 Feb 2024; event windows of 15 min pre / 90 min event / 15 min post around ECB Governing Council meetings, speeches and interviews. Contemporaneous reaction only; no later-return/drift test, no out-of-sample forecast evaluation, no transaction costs. No EUR/USD figure verified.
- **Relevance:** None for an item (contemporaneous; ECB communication family already covered: ECB accounts ~backlog line 2086, ECB speeches line 2926, E013/E022-E025). **Status:** VERIFIED (partial read).

### Zhang (Yunhe), "Price Discovery in the CSI 300 Index Futures and Spot Markets: An Empirical Analysis Using High-Frequency Data in China", NYU Shanghai honors thesis (May 2025) (added 2026-11-22 R363)
- **Link:** [PDF](https://cdn.shanghai.nyu.edu/sites/default/files/honorsthesis2025_yunhe_zhang.pdf) (opened via web-fetch; ~55% verbatim, rest model-summarised: UNVERIFIED).
- **Design/finding:** CSI 300 futures vs spot, 5-minute, 2024; Granger/VECM/information share, in-sample. Verbatim: "I find strong evidence that futures prices significantly Granger-cause spot prices." No FX, no OOS, no costs (internal table/text inconsistencies noted by the reader).
- **Relevance:** None (no FX). **Status:** VERIFIED (partial read).

### Cuestas & Tang, "Exchange Rate Changes and Stock Returns in China: A Markov Switching SVAR Approach", Sheffield Economic Research Paper Series 2015024 (Dec 2015) (added 2026-11-22 R363)
- **Link:** [PDF](https://sheffield.ac.uk/media/3882/download) (opened via web-fetch; main text verbatim).
- **Design/finding:** daily 1994-2012, USD/RMB and HKD/RMB vs Shanghai/Shenzhen A/B shares and Hang Seng; in-sample Granger tests and MS-SVAR. Verbatim: "exchange rate changes exhibit little effect on stock returns." Stock returns Granger-cause RMB changes (in-sample). No EUR/USD, no OOS, no costs.
- **Relevance:** None for an item (RMB, not EUR/USD; Chinese equity data not in pipeline). **Status:** VERIFIED.

### Kim & Ochoa, "International Yield Spillovers", FEDS 2021-001 (Federal Reserve Board) (added 2026-11-22 R363)
- **Link:** [PDF](https://www.federalreserve.gov/econres/feds/files/2021001pap.pdf) (opened via web-fetch; abstract/intro verbatim, later sections UNVERIFIED).
- **Design/finding:** daily Treasury/Bund/Gilt futures 2010-2017 (contemporaneous spillovers) and weekly 10y zero yields 2000-2019 (in-sample predictive regressions for bond yields). Verbatim: "a low level of foreign yields relative to U.S. yields predicts a decline in distant forward U.S. yields." Bond yields only; FX enters only for hedged returns; no OOS, no costs.
- **Relevance:** None for an item (no EUR/USD direction result; rate-differential family already covered). **Status:** VERIFIED (partial read).

### Dobrynskaya (2014), "Downside risk in stock and currency markets", LSE PhD thesis (Department of Finance) (added 2026-11-22 R364)
- **Link:** [LSE Research Online eprint 132024](https://researchonline.lse.ac.uk/id/eprint/132024) (record page and abstract opened via web-fetch; thesis body UNVERIFIED).
- **Design/finding:** cross-sectional asset pricing: two-beta (downside/upside) CAPM for global stock momentum portfolios and a "global downside market factor" for carry-trade / forward-discount-sorted currency portfolios; GMM estimates. Verbatim: "I propose a new factor – the global downside market factor – to explain high returns to carry trades." No single-pair EUR/USD test, no directional time-series forecast, no OOS, no costs stated.
- **Relevance:** None for an item (cross-sectional risk premia, not next-period EUR/USD direction). **Status:** VERIFIED (abstract only).

### LeCompte / CXO Advisory (2015), "Short-term VIX Calendar Effects" (added 2026-11-22 R365)
- **Link:** [cxoadvisory.com/calendar-effects/vix-calendar-effects/](https://www.cxoadvisory.com/calendar-effects/vix-calendar-effects/) (opened via web-fetch).
- **Design/finding:** daily VIX (1990-2015) and VXX (2009-2015) by day of week, turn of month and options expiration; VIX rises on Mondays on average and drops abnormally on the day before VIX options expiration (VXX 56 of 77 OE-1 returns negative). Gross returns, no costs, no OOS; author warns of small samples and snooping. No currency tested.
- **Relevance:** None for an item (volatility products only, no EUR/USD). **Status:** VERIFIED (practitioner article, not peer reviewed).

### Lombardi (2017), "Financial Reporting and the Market Risk Premium", University of Chicago PhD dissertation (added 2026-11-22 R365)
- **Link:** [knowledge.uchicago.edu record 163 PDF](https://knowledge.uchicago.edu/record/163/files/Lombardi_uchicago_0330D_14112.pdf) (opened via web-fetch; front matter verbatim, body partly via extracted summary, UNVERIFIED in detail).
- **Design/finding:** CRSP daily US equity 1926-2015: market excess returns concentrated in earnings seasons (~67-70% of the premium in ~half the days; bellwether announcement days 9.53 bp vs 1.98 bp). US equities (plus Australian replication); no currency test, no OOS, no costs.
- **Relevance:** None for an item (equity risk premium, no EUR/USD direction). **Status:** VERIFIED (partial read).

### McCarthy & Snudden (2025), "Forecasts of Period-average Exchange Rates: Insights from Real-time Daily Data", RBA RDP 2025-09 (added 2026-11-22 R366)
- **Link:** [rba.gov.au/publications/rdp/2025/2025-09/full.html](https://www.rba.gov.au/publications/rdp/2025/2025-09/full.html) (opened via web-fetch; introduction verbatim, later sections via extracted summary or unread, UNVERIFIED in detail).
- **Design/finding:** daily nominal/real bilateral and effective exchange rates for 83 countries, real-time monthly vintages, expanding-window forecasts 2004-2022 of month-average and end-of-month levels against no-change benchmarks. Verbatim: "the month-average no-change benchmark is less accurate than the end-of-month no-change benchmark"; "we find new evidence of real-time predictability for period-average EERs in up to 50 per cent of countries". Gain comes from forecasting a period average (a smoothing artefact), not a tradable next-day spot return; EUR/USD inclusion and costs not confirmed in the text read.
- **Relevance:** None for an item (period-average target, monthly horizon, not a tradable EUR/USD direction signal). **Status:** VERIFIED (partial read).

### Alquist, Ellwanger & Jin (2020), "The Effect of Oil Price Shocks on Asset Markets: Evidence from Oil Inventory News", Bank of Canada SWP 2020-8 (added 2026-11-22 R366)
- **Link:** [bankofcanada.ca swp2020-8.pdf](https://www.bankofcanada.ca/wp-content/uploads/2020/03/swp2020-8.pdf) (opened via web-fetch; abstract and data section verbatim, rest via summary).
- **Design/finding:** 15-minute windows around weekly EIA Petroleum Status Report releases, 2003-2017 (EUR from April 2006); oil inventory news as IV for oil price shocks. Verbatim: "Positive oil price shocks cause a depreciation of the U.S. dollar against a broad range of currencies". Contemporaneous reaction only; no forecast of later returns, no OOS, no costs.
- **Relevance:** None for an item (contemporaneous release-window reaction needing EIA surprise data not in the pipeline; lagged-oil -> EUR/USD mechanism already rejected). **Status:** VERIFIED (partial read).

### Okudan Soytürk & Açık (2024), "Unraveling the link: Examining the influence of dollar strength on dirty tanker freight rates", Marine Science and Technology Bulletin 13(4):304-317, DOI 10.33714/masteb.1549020 (added 2026-11-22 R367)
- **Link:** [dergipark.org.tr article-file 4209724](https://dergipark.org.tr/en/download/article-file/4209724) (opened via web-fetch; title, abstract and early sections verbatim, results/conclusions via extracted summary, UNVERIFIED in detail).
- **Design/finding:** monthly US Dollar Index (DXY) and Baltic Dirty Tanker Index, 2002-08..2024-04 (261 obs), Hatemi-J asymmetric causality, in-sample only. Reported: dollar weakening (negative DXY shocks) causes positive BDTI shocks; freight -> dollar direction not significant. No EUR/USD series, no container freight, no OOS, no costs.
- **Relevance:** None for an item (monthly, in-sample, causality runs dollar -> freight, not freight -> EUR/USD; freight data not in the pipeline). **Status:** VERIFIED (partial read).

### Crespo Cuaresma, Hlouskova & Obersteiner (2021), "Agricultural commodity price dynamics and their determinants: A comprehensive econometric approach", Journal of Forecasting 40(7):1245-1273, DOI 10.1002/for.2768 (added 2026-11-22 R368)
- **Link:** [core.ac.uk download 527948921](https://core.ac.uk/download/527948921.pdf) (opened via web-fetch; first ~40k of 87k characters verbatim, rest via extracted summary, UNVERIFIED in detail).
- **Design/finding:** monthly wheat, soybean and corn prices, 1980-01..2016-12; predictors include the USD real effective exchange rate; OOS 2005-01..2016-12 (rolling 240-month window, Diebold-Mariano vs random walk, directional accuracy and a trading return). Direction is exchange rate -> commodity prices; no EUR/USD series, no commodity -> FX test, no transaction costs in the verbatim part.
- **Relevance:** None for an item (wrong causal direction, monthly, USD REER not EUR/USD; grain prices not in the pipeline). **Status:** VERIFIED (partial read).

### Brophy, Herrala, Jurado, Katsalirou, Le Quéau, Lizarazo & O'Donnell (2019), "Role of cross currency swap markets in funding and investment decisions", ECB Occasional Paper No 228 (added 2026-11-22 R369)
- **Link:** [ecb.europa.eu ecb.op228](https://ecb.europa.eu/pub/pdf/scpops/ecb.op228~bb3e50120a.fi.pdf) (opened via web-fetch; first ~40k of ~84k characters verbatim, rest via extracted summary, UNVERIFIED in detail).
- **Design/finding:** descriptive/analytical study of the EUR/USD cross-currency basis and its drivers (Eurosystem APP, cross-border corporate and SSA issuance, quarter-end balance-sheet constraints). Mentions US tax changes (TCJA 2017, BEAT, repatriation) but not US tax payment dates. No forecast of EUR/USD spot direction, no OOS, no costs.
- **Relevance:** None for an item (basis, not spot direction; no tax-date FX test). **Status:** VERIFIED (partial read).

### Dyer, Fleming & Shachar (2026), "Treasury Trading at the Close", Liberty Street Economics, FRBNY, DOI 10.59576/lse.20260922 (added 2026-11-22 R370)
- **Link:** [libertystreeteconomics.newyorkfed.org](https://libertystreeteconomics.newyorkfed.org/2026/09/treasury-trading-at-the-close/) (opened via web-fetch; article body verbatim).
- **Design/finding:** BrokerTec on-the-run Treasury volume 2016-2025; trading increasingly concentrated around the 3 p.m. and 4 p.m. index strike times, especially month-end (~58% higher volume on the last trading day); volume shifted 3pm -> 4pm after Bloomberg moved its strike in Jan 2021. No FX variable, no return prediction, no OOS, no costs.
- **Relevance:** None for an item (Treasury volume only; late-NY hours already covered by the E009 hourly scan and the month-end fix tests). **Status:** VERIFIED.

### Filippou, Gozluklu, Nguyen & Viswanath-Natraj (2025), "Signal in the noise: Trump tweets and the currency market", JIMF 156, DOI 10.1016/j.jimonfin.2025.103343 (added 2026-11-22 R370)
- **Link:** [IDEAS/RePEc](https://ideas.repec.org/a/eee/jimfin/v156y2025ics0261560625000786.html) (abstract/metadata opened; full text paywalled, UNVERIFIED). Published version of the working paper logged R165.
- **Design/finding (abstract):** informative (macro/trade) tweets -> USD appreciation and lower intraday volatility, robust to macro announcements; contemporaneous event response, no lagged forecast, OOS or costs mentioned.
- **Relevance:** None for an item (same family as R165 entry; event-response, tweet data not in pipeline). **Status:** VERIFIED (abstract only).

### Zawadowski, Andor & Kertész (2004), "Short-term market reaction after extreme price changes of liquid stocks", arXiv cond-mat/0406696 (added 2026-11-23 R371)
- **Link:** [arxiv.org/pdf/cond-mat/0406696](https://arxiv.org/pdf/cond-mat/0406696) (opened via web-fetch).
- **Design/finding:** minute-level TAQ data, liquid NYSE (2000-2002) and NASDAQ stocks; "significant reversal for both intraday price decreases and increases" over 30-60 minutes after 4% / 8x-volatility moves. Bid-ask spread included, other costs omitted; no OOS; no FX.
- **Relevance:** None for an item (US equities only; post-jump reversal family already covered in research/). **Status:** VERIFIED.

### Rif & Utz (2021), "Short-term stock price reversals after extreme downward price movements", Q. Rev. Econ. Finance 81, 123-133, PII S1062976921000922 (DOI not confirmed, UNVERIFIED) (added 2026-11-23 R371)
- **Link:** [opus.bibliothek.uni-augsburg.de](https://opus.bibliothek.uni-augsburg.de/opus4/files/94257/1-s2.0-S1062976921000922-main.pdf) (opened via web-fetch; partial read).
- **Design/finding:** Nasdaq-100 stocks, 1-minute intervals 2014-2019; "31% of such an extreme one-minute interval's return is reversed in the subsequent trading minute". Full-sample fixed-effects regressions, no OOS, no net-of-cost profit; no FX.
- **Relevance:** None for an item (equities only, one-minute horizon, no costs). **Status:** VERIFIED (partial read).

### Altavilla, Brugnolini, Gürkaynak, Motto & Ragusa (2019), "Measuring euro area monetary policy", ECB Working Paper No 2281 (added 2026-11-23 R372)
- **Link:** [ecb.europa.eu WP 2281](https://www.ecb.europa.eu/pub/pdf/scpwps/ecb.wp2281~3303fd281b.en.pdf) (opened via web-fetch; partial read, first ~40k of ~120k characters).
- **Design/finding (readable part):** EA-MPD intraday event-study database; press-release window 13:25-14:15 CET and press-conference window 14:15-15:50 CET; factors (target, timing, forward guidance, QE) extracted from OIS/yield moves; forward guidance factor "affected the middle of the yield curve most heavily, with a peak effect at about two years". EUR/USD reaction table (Table 10) seen only in a model summary, not verified; contemporaneous window response, no post-window drift test, no OOS, no costs.
- **Relevance:** None for an item (contemporaneous response to an unobservable-in-real-time surprise factor; ECB communication family already covered: E013-area, ECB accounts R185, ECB speeches). **Status:** VERIFIED (partial read; EUR/USD figures UNVERIFIED).

### Duarte (2025), "The Effect of ECB Forward Guidance on the Euro Area Yield Curve", NOVA SBE Master's work project (added 2026-11-23 R372)
- **Link:** [run.unl.pt 10362/181613](https://run.unl.pt/bitstream/10362/181613/1/2024_25_Fall_47195_Tom_sFaluaDuarte.pdf) (opened via web-fetch; partial read).
- **Design/finding:** daily event study on ECB communication dates, July 2005-July 2024, euro OIS 1m-10y; forward-guidance factor coefficient negative and significant at 1% at all maturities (e.g. -5.436 bp per SD at 2y, ARCH(1), Table 1). No FX, no OOS, no costs.
- **Relevance:** None for an item (rates only, student thesis). **Status:** VERIFIED (partial read).

### Caporin, Ranaldo & Santucci de Magistris (2011), "On the Predictability of Stock Prices: a Case for High and Low Prices", Univ. Padova "Marco Fanno" WP 136 (added 2026-11-23 R373)
- **Link:** [economia.unipd.it 20110136.pdf](https://economia.unipd.it/en/sites/decon.unipd.it/files/20110136.pdf) (opened via web-fetch; middle section read only via extractor summary).
- **Design/finding:** 30 DJIA stocks, daily high/low/close 2003-2010; fractional VECM on daily high and low with the range as error-correction term; "high-low bands" as trading signals on 1-minute data for 20 stocks. OOS 2009 one-step forecasts (Diebold-Mariano). Verbatim: "We find strong support for the forecasting ability of FVECM". Costs: flat per-trade fee only (from extractor summary, UNVERIFIED). No FX, no close-location-value predictor.
- **Relevance:** None for an item (US equities only; range-based level forecasting, not FX direction). **Status:** VERIFIED (partial read).

### Hsu, Taylor & Wang, "Technical Trading: Is it Still Beating the Foreign Exchange Market?" (primary full text; SSRN 2765673; year/journal UNVERIFIED from the fetched text) (added 2026-11-23 R373; supplements the secondary-summary entry above, line ~769)
- **Link:** [hub.hku.hk 10722/229640](https://hub.hku.hk/bitstream/10722/229640/1/Content.pdf?accept=1) (opened via web-fetch; full read).
- **Design/finding:** 30 USD rates, daily London midday quotes (no high/low), developed 1971-2015; 21,195 rules on closing rates; selection to 2011-12-31, OOS 2012-01-01..2015-09-11; costs = one-third of 1m forward bid-ask (developed avg "just under 4.5 basis points" one-way). Germany/E.U. series: in-sample best rule MA1 OOS annualized 0.843%, Sharpe 0.141; developed-currency OOS portfolio Sharpe 0.244, t-ratio 0.469 (not significant).
- **Relevance:** None for an item (daily closing-rate technical rules, family already tested; euro OOS not significant). **Status:** VERIFIED.

### ter Ellen, Jansen & Larsson Midthjell (2018), "ECB spillovers and domestic monetary policy effectiveness in small open economies", Norges Bank Working Paper 9/2018 (added 2026-11-23 R374)
- **Link:** [norges-bank.no working_paper_9_18.pdf](https://www.norges-bank.no/contentassets/405144032222464fb50a0928a5cb73e6/working_paper_9_18.pdf) (opened via web-fetch; first ~40k of ~69k characters read verbatim, rest model-summarised). Later EER publication cited in another paper's bibliography only, UNVERIFIED.
- **Design/finding:** 5-minute data, window 13:30-15:45 CET around ECB decisions, 2002-06/2018 (FX from 2004); EUR/NOK, EUR/SEK, EUR/DKK; EUR/USD appears only in ECB factor loadings (Table 1). Verbatim: "Our findings show that domestic monetary policy is still effective". Contemporaneous window responses plus in-sample local projections; no OOS, no costs.
- **Relevance:** None for an item (contemporaneous, non-USD crosses; ECB-meeting family already covered). **Status:** VERIFIED (partial read).

### Rossi & Wolff (2020), "Spillovers to exchange rates from monetary and macroeconomic communications events", SNB Working Paper 2020-18 (added 2026-11-23 R374)
- **Link:** [snb.ch landing page](https://www.snb.ch/en/publications/research/working-papers/2020/working_paper_2020_18) (opened via web-fetch; abstract only, PDF not opened).
- **Design/finding (abstract):** event study of EUR, CHF, BRL, MXN vs USD around U.S. monetary and macro communication events since the GFC. Verbatim: "Approximately 20 percent of the U.S. communications events were associated with statistically significant exchange rate effects." Contemporaneous event windows; drift, OOS and costs not described (UNVERIFIED without the PDF).
- **Relevance:** None for an item (contemporaneous; FOMC/US-release families already covered). **Status:** VERIFIED (abstract only).

### Hager & Nitschka (2023), "Responses of Swiss interest rates and stock prices to ECB policy surprises", Swiss J. Econ. Stat. 159:13, DOI [10.1186/s41937-023-00117-8](https://doi.org/10.1186/s41937-023-00117-8) (added 2026-11-23 R374)
- **Link:** [Springer](https://link.springer.com/article/10.1186/s41937-023-00117-8) (opened via web-fetch; ~40% read verbatim, rest summarised).
- **Design/finding:** daily ECB announcement days 2004-2023; Swiss swap rates and stocks only; verbatim: "we do not examine exchange rate reactions to ECB policy surprises". No OOS, no costs.
- **Relevance:** None (no FX). **Status:** VERIFIED (partial read).

### Jansen, Shin & von Peter (2024), "Which exchange rate matters to global investors?", BIS Working Paper 1210 (added 2026-11-23 R375)
- **Link:** [BIS page](https://www.bis.org/publ/work1210.htm) (opened via web-fetch; abstract page only, PDF not opened).
- **Design/finding (abstract):** security-level bond holdings of euro-area investors plus a VaR portfolio-choice model. Verbatim: "euro area-based investors systematically shed sovereign bonds as the dollar strengthens". Portfolio-allocation responses, not a spot-direction forecast; sample, frequency, OOS and costs not stated on the page (UNVERIFIED without the PDF).
- **Relevance:** None for an item (holdings responses, contemporaneous; no lagged EUR/USD direction test). **Status:** VERIFIED (abstract only).

### Eurex (30 June 2023), "Fixed income futures - June roll analysis" (added 2026-11-23 R375)
- **Link:** [Eurex news item](https://eurex.com/ex-de/ressourcen/news/Fixed-income-futures-June-roll-analysis-3612036) (opened via web-fetch).
- **Design/finding:** exchange note; descriptive volumes, open interest, deliveries, CTD switches and calendar spreads for Bund/Bobl/Schatz/Buxl/BTP/OAT futures over the June 2023 roll. Verbatim: "The introduction of the minimum exchange day rule ensured that there were no front month CTD switches". No FX data, no tests.
- **Relevance:** None (no FX; not evidence of a price effect). **Status:** VERIFIED.

### Kloks, Mattille & Ranaldo (26 Sep 2024), "Hunting for Dollars" (ECB money-market conference paper) (added 2026-11-23 R376)
- **Link:** [ECB conference PDF](https://ecb.europa.eu/press/conferences/shared/pdf/20241107_money_markets/Ranaldo_paper.pdf) (opened via web-fetch; first ~30% verbatim, rest summarized by the fetch tool).
- **Design/finding:** daily CLS FX-swap settlement data, 40 currency pairs (17 USD pairs), 8 tenors, 2012-09-03 to 2022-06-30, plus repo and money-market data; quarter-end repo-to-FX-swap substitution by euro-area banks (leverage-ratio window dressing) and the cross-currency basis. Verbatim: "Eurozone banks pay no more than 37 million of USD per year as a result of repo-FX swap substitution." Swap volumes and basis only; no spot-direction or lagged-return test, no OOS, no costs.
- **Relevance:** None for an item (swap/basis, not EUR/USD spot direction; quarter-end calendar already covered by E034/R-notes). **Status:** VERIFIED (partial read).

### Gargano, Riddiough & Sarno (16 Aug 2017), "The Value of Volume in Foreign Exchange" (working paper) (added 2026-11-23 R377)
- **Link:** [Norges Bank PDF](https://www.norges-bank.no/contentassets/619c8b75e1ed4ba691e8ad6a006855e6/21-sarno-the-value-of-volume-in-exchange-rates.pdf) (opened via web-fetch; first ~56% verbatim, rest summarised by the fetch tool).
- **Design/finding:** CLS settlement volume via Quandl, 1 Nov 2011 - 31 Dec 2016, 31 pairs incl. EUR/USD; volume = log deviation from 21-day moving average; daily next-day WM/R 4pm returns; cross-sectional 3x3 double sorts rebalanced daily. Verbatim: low-volume reversal portfolio "an annualized return of over 19%", "a Sharpe ratio of 1.82"; net of Dukascopy spreads "13.1% per annum". Interaction positive "for 26 of the 31 currency pairs"; no single-pair (EUR/USD) trading result reported in the part read.
- **Relevance:** None for a new item: earlier version of the Cespa-Gargano-Riddiough-Sarno mechanism already tested on EUR/USD with a Dukascopy volume proxy (B28/B29, E033 NONE on dev, line closed on dev). **Status:** VERIFIED (partial read).

### Beetsma, Giuliodori, Hanson & de Jong (May 2017), "Bid-to-cover and yield changes around public debt auctions in the euro area", ECB Working Paper 2056 (added 2026-11-23 R377)
- **Link:** [ECB PDF](https://www.ecb.europa.eu/pub/pdf/scpwps/ecb.wp2056.en.pdf) (opened via web-fetch; first ~36% verbatim, rest summarised).
- **Design/finding:** Belgian, French, German and Italian primary auctions; daily secondary-market yield change from close t-1 to close of auction day. Verbatim: "more successful auctions of euro area public debt ... lead to lower secondary-market yields following the auctions". No exchange-rate variable, no drift, OOS or cost test in the part read.
- **Relevance:** None (no FX; euro-area auction demand family already logged via DNB WP 674, R269). **Status:** VERIFIED (partial read).

### Menkhoff, Sarno, Schmeling & Schrimpf (2011), "Carry Trades and Global Foreign Exchange Volatility", CEPR Discussion Paper 8291 (added 2026-11-23 R378)
- **Link:** [CEPR abstract page](https://cepr.org/publications/DP8291) (opened via web-fetch; abstract only, full PDF not read).
- **Design/finding:** global FX volatility innovations as a priced risk factor; verbatim: "captures more than 90% of the cross-sectional excess returns in five carry trade portfolios". Cross-sectional asset pricing, no single-pair EUR/USD direction test; OOS and costs not stated in the abstract.
- **Relevance:** None for a new item (cross-sectional carry pricing, not EUR/USD time-series direction). **Status:** VERIFIED (abstract).

### Frost & Saiki (March 2013), "Early warning for currency crises: what is the role of financial openness?", DNB Working Paper 373 (added 2026-11-23 R378)
- **Link:** [DNB PDF](https://www.dnb.nl/media/5rgjh1bx/working-paper-373.pdf) (opened via web-fetch; first ~half verbatim).
- **Design/finding:** quarterly panel, 46 advanced and emerging economies, 1975Q1-2011Q4; random-effects probit for crisis probability from an exchange-market-pressure index vs USD. Verbatim: "our model performs well out-of-sample". No EUR/USD pair, no direction or cost test.
- **Relevance:** None (quarterly crisis probability, not EUR/USD direction; far below the R090 power floor). **Status:** VERIFIED (partial read).

### Chen (2024), "Foreign investments of Japanese life insurance companies", Economics Letters 240 (added 2026-11-23 R379)
- **Link:** [IDEAS abstract page](https://ideas.repec.org/a/eee/ecolet/v240y2024ics0165176524002581.html), doi:10.1016/j.econlet.2024.111774 (abstract page opened via web-fetch; full text paywalled, not read).
- **Design/finding:** Japanese life insurers' foreign portfolio returns, volatility and currency-hedging choices, including a yen-funded carry-trade scenario. Verbatim: "Third, the investment returns significantly decrease under the carry trade scenario." Pairs, frequency, OOS and costs UNVERIFIED (not in abstract); no EUR/USD spot-direction test visible.
- **Relevance:** None for a new item (insurer portfolio returns, not lagged EUR/USD direction; semiannual plan dates ~2/year are below the R090 power floor). **Status:** VERIFIED (abstract).

### Graziano & Habib, "Mutual funds and safe government bonds: do returns matter?", ECB Working Paper 2931 (added 2026-11-23 R379)
- **Link:** [ECB PDF](https://www.ecb.europa.eu/pub/pdf/scpwps/ecb.wp2931~8b0e21c2d2.en.pdf) (opened via web-fetch; first ~40k of 146k characters verbatim, rest summarised only).
- **Design/finding:** quarterly panel 2010Q1-2021Q4 of US mutual funds' currency shares in safe sovereign bonds (USD, EUR, JPY, GBP, CHF, AUD, CAD). Verbatim: "We find evidence of active rebalancing towards government bonds that offer relatively higher returns on an unhedged basis". Contemporaneous returns; no spot-direction, OOS or cost test. Lagged-return appendix result UNVERIFIED (summary only).
- **Relevance:** None (portfolio-share regressions, same rebalancing family as Camanho-Hau-Rey already logged). **Status:** VERIFIED (partial read).

### Avramov & Xu, "Predicting currency returns: New evidence on the forward premium puzzle and dollar-trade strategy", working paper (Jan 2019; Mannheim Finance Area Seminar 2019) (added 2026-11-23 R380)
- **Link:** [Mannheim seminar PDF](https://www.bwl.uni-mannheim.de/media/Lehrstuehle/bwl/Area_Finance/Finance_Area_Seminar/FSS_2019/Avramov_Paper.pdf) (opened via web-fetch; first ~40k characters verbatim, rest summarised only).
- **Design/finding:** monthly, Dec 1979-Sep 2017, 25 economies vs USD (euro included). Verbatim: "currency strategies that condition on the lagged foreign interest rate deliver significant abnormal payoffs and outperform the dollar-trade strategy." Expanding-window forecasts; a 2001-2017 OOS period is mentioned but its results were not seen; transaction costs not mentioned in the part read (UNVERIFIED).
- **Relevance:** None for a new item (monthly cross-country rate-conditioned dollar strategy; a single-pair monthly signal gives ~60 dev observations, below the R090 power floor; rate-differential / carry line already covered). **Status:** VERIFIED (partial read).

### Chung & Bellotti (2021), "Evidence and Behaviour of Support and Resistance Levels in Financial Time Series", arXiv:2101.07410 (added 2026-11-23 R382)
- **Link:** [arXiv PDF](https://web3.arxiv.org/pdf/2101.07410) (opened via web-fetch; first ~40k of 57k characters verbatim, rest summarised only).
- **Design/finding:** 1-minute bars for calendar year 2018, EURUSD (HistData.com), LLOY and Brent. Levels = rolling min/max over 60- and 240-minute lag windows +/- the average price increment; estimates the bounce probability p(b|bprev) with a Beta-binomial model and compares it with shuffled returns (permutation statistic; EURUSD 60-minute Lambda 1.000 for bprev 1-6). Verbatim: "we determine local minima and maxima to be local support and resistance levels, then count the number of bounces these levels have in the recent past, and finally observe if prices in the future bounce or penetrate these levels." No trading rule, no P&L, no out-of-sample period, no transaction costs in the part read.
- **Relevance:** None for a new item (in-sample bounce statistics on one year that lies inside our dev block; no direction/P&L or cost test; support/resistance reversal mechanism already covered by Osler 2000/2003 and tested in B15/B52). **Status:** VERIFIED (partial read).

### Petric (2025), "How the Trajectory of Asset Prices Can Predict FX Movements", CFA Institute Enterprising Investor blog (added 2026-11-23 R383)
- **Link:** [CFA Institute blog](https://blogs.cfainstitute.org/blog/2025/07/19/how-the-trajectory-of-asset-prices-can-predict-fx-movements) (opened via web-fetch, full text).
- **Design/finding:** practitioner opinion piece (not peer-reviewed), 19 July 2025. Promotes path-signature (rough-path) features of recent return paths. Verbatim: "Early studies show that these shape-based features can improve forecasts for both volatility and FX forecasts". No underlying path-signature study named or cited (reference list covers crisis early-warning and Meese-Rogoff / Mark predictability only); no data, frequency, currencies, out-of-sample design, costs or numbers.
- **Relevance:** None for a new item (no evidence; the "early studies" are UNVERIFIED as no source is given). **Status:** VERIFIED (opened; contains no study).

### Pandolfi & Williams (2017), "Capital Flows and Sovereign Debt Markets: Evidence from Index Rebalancings", CSEF Working Paper No. 487 (added 2026-11-23 R384)
- **Link:** [CSEF PDF](https://www.csef.it/WP/wp487.pdf) (opened via web-fetch; ~40k of ~102k characters verbatim, rest summarised only).
- **Design/finding:** "Flows Implied by Rebalancings" (FIR) from monthly mechanical rebalancings of the J.P. Morgan GBI-EM Global Diversified bond index (10% country cap); 16 emerging-market local currencies vs USD; September 2009 - March 2016; daily bond prices, spreads and exchange rates. Verbatim: FIR inflows lead to "an appreciation of 36 basis points in the cumulative change of the exchange rate" (per 1 s.d. of FIR, 0.872 pp). No EUR/USD; OOS test and cost model not seen in the verbatim part (UNVERIFIED).
- **Relevance:** None for a new item (EM currencies only; EUR is not an index-rebalancing target currency in this design; event-study, not a tradable EUR/USD rule). **Status:** VERIFIED (partial read).

### Hao, Guo, Keppo & Peng (2026), "Intraday Forecasting Ability and Liquidity Provision of Institutional Traders", arXiv 2610.31141 (added 2026-11-23 R385)
- **Link:** [arXiv PDF](https://arxiv.org/pdf/2610.31141) (opened via web-fetch; ~40k of ~364k characters verbatim, rest summarised only).
- **Design/finding:** five anonymised stocks, full limit-order-book events, 22-26 November 2010 (five trading days); trader-level execution flow vs next-interval VWAP change at 26 horizons (1 s to 30 min); traders classified on days 1-2, verbatim "The subsequent three-day period serves as the out-of-sample validation window". Flow-following Sharpe ratios verbatim "ranging from 16 to 63" "before transaction costs" (cost sensitivity reported in figures; not read verbatim, UNVERIFIED).
- **Relevance:** None for a new item (equities only, no FX pair; needs trader-identified order flow we do not have; five-day sample). **Status:** VERIFIED (partial read).

### Rosenberg & Traub (2008), "Price Discovery in the Foreign Currency Futures and Spot Market", FRBNY Staff Report 262 (added 2026-11-23 R387)
- **Link:** [FRBNY SR262](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr262.html) (opened via web-fetch; ~40k of ~89k characters verbatim, rest summarised only).
- **Design/finding:** CME futures vs interdealer/composite spot, 3-minute returns, daily VECM; 1996 sample (DEM, JPY, CHF, GBP) and March-May 2006 sample (EUR, JPY, GBP). Verbatim 1996: "futures returns lead spot returns by up to 12 minutes"; verbatim 2006: "in our more recent sample that the spot market has the dominant information share". No trading rule, OOS or cost test.
- **Relevance:** None for a new item (spot leads in the electronic era; no CME futures data in repo). **Status:** VERIFIED (partial read).

### Cabrera, Wang & Yang (2009), "Do futures lead price discovery in electronic foreign exchange markets?", J. Futures Markets 29(2) 137-156 (added 2026-11-23 R387)
- **Link:** [IDEAS record](https://ideas.repec.org/a/wly/jfutmk/v29y2009i2p137-156.html) (abstract only; full text not opened, sample details UNVERIFIED).
- **Finding:** EUR and JPY, CME GLOBEX regular and E-mini futures vs EBS spot; verbatim "the spot market is found to consistently lead the price discovery process for both currencies during the sample period". No trading rule/OOS/costs in the abstract.
- **Relevance:** None for a new item (same as Rosenberg-Traub 2006 sample). **Status:** VERIFIED (abstract only).

### Czech, Della Corte, Huang & Wang (2022), "FX option volume", Bank of England Staff Working Paper No. 964 (added 2026-11-23 R388)
- **Link:** [BoE SWP 964 PDF](https://www.bankofengland.co.uk/-/media/boe/files/working-paper/2022/fx-option-volume.pdf) (opened via web-fetch; ~40k characters verbatim, Sections 4.4 onward summarised only).
- **Data/design:** EMIR trade-repository (DTCC) FX option trades with a UK-regulated counterparty, daily, Nov 2014 - Dec 2016; 19 currencies vs USD incl. EUR; volume standardised over a 21-day window; cross-sectional low-minus-high (LMH) volume portfolios, signal lagged one day.
- **Finding (verbatim abstract):** "FX option volume can predict future exchange rate returns, especially when the demand for the US dollar is high." Major currencies (AUD, CAD, CHF, EUR, GBP, JPY, NZD) LMH 14.63% p.a., t = 2.66 (gross); all 19 currencies 5.91% p.a., t = 1.11 (n.s.). Dealer-client volume drives it.
- **Limits:** cross-sectional (not a single-pair EUR/USD timing rule); ~2 years of data; no OOS test and no transaction-cost analysis identified (summary-only for later sections, UNVERIFIED); DTCC data not public; Bloomberg aggregate option volume (public per footnote 1) is not in the repo and not downloadable on the runner.
- **Relevance:** None for a new item now (no option-volume data source; cross-sectional design). **Status:** VERIFIED (partial read).

### Oort (2020), "Predicting Asset Returns using the Copper to Gold Ratio", BSc thesis, Erasmus School of Economics (added 2026-11-23 R388)
- **Link:** [thesis.eur.nl 53697 PDF](https://thesis.eur.nl/pub/53697/BSc-Thesis-Sebastiaan-Oort-Final-version.pdf) (opened via web-fetch; ~40k of ~54k characters verbatim).
- **Design/finding:** CME copper/gold futures ratio, daily Dec 1988 - Jan 2020, predicting the US 10y yield and equity/commodity/bond indices. No exchange rates studied (no EUR/USD). Verbatim: "the results of the the out of sample test are not more predictive than their in sample counter part"; negative OOS R² values and zero transaction costs are summary-only (UNVERIFIED). Undergraduate thesis, not peer-reviewed.
- **Relevance:** None (no FX; OOS fails for its own targets). **Status:** VERIFIED (partial read).

### Xu, Li, Singh, Chen & Li (2025), "Cross-market overnight time-series momentum", JIFMIM 105, 102239 (added 2026-11-23 R391)
- **Link:** [Griffith repository record](https://research-repository.griffith.edu.au/items/77d29c70-c6f9-426e-a28a-fca4c540dedd) (record page and abstract opened via web-fetch; full text embargoed to 2027-10-21, not read; DOI not shown on the page).
- **Design/finding (abstract):** "the US stock market's last half-hour return predicts the next day's first half-hour stock returns in international markets"; significant "both in- and out-of-sample"; "remains profitable with the consideration of transaction costs". Equity indices only; no FX or EUR/USD in the abstract.
- **Relevance:** None for an item (equities only; an EUR/USD transfer would be our own untested extension). **Status:** VERIFIED (abstract only).

### Enkhbayar & Ślepaczuk (2024), "Predictive modeling of foreign exchange trading signals using machine learning techniques", University of Warsaw WNE WP 10/2024 (446) (added 2026-11-23 R392)
- **Link:** [wne.uw.edu.pl download 4308](https://www.wne.uw.edu.pl/download_file/4308/0) (opened via web-fetch; partly read verbatim, later results sections summary-only).
- **Design:** EUR/USD and five other USD majors, daily and 4-hour bars (ICMarket), 2000-01-01..2023-06-30; Ridge, KNN, RF, XGBoost, GBDT, ANN, LSTM, GRU on technical/statistical features; verbatim "Implement a rolling walk-forward optimization to solve the overfitting problem"; 40 walk-forward windows testing 2003-2023 (summary, UNVERIFIED); fixed 0.02% cost (summary, UNVERIFIED).
- **Finding:** EUR/USD daily ANN annualised Sharpe ~0.49 vs buy-and-hold 0.22, 775 trades (summary-only, table row match uncertain, UNVERIFIED); some 4-hour EUR/USD results not significant at 0.10 (summary, UNVERIFIED).
- **Relevance:** None for a new item: ML on lagged daily features is the E051 family (closed NONE, lesson R213: no re-test with other classifiers); headline numbers not verified. **Status:** VERIFIED (partial read).

### Cheevirot, Smanchat & Nuchitprasitchai (2026), "ML-Augmented High-Frequency Grid Trading: Strategy-Embedded Labeling, Soft Martingale Execution, and Drawdown Dichotomy Quantification", Algorithms 19(6), 442 (added 2026-11-23 R392)
- **Link:** [MDPI](https://www.mdpi.com/1999-4893/19/6/442/htm), DOI [10.3390/a19060442](https://doi.org/10.3390/a19060442) (opened via web-fetch; results read).
- **Design/finding:** EUR/USD H1, CatBoost on 14 MA-deviation features with grid-simulation labels, grid execution with soft-martingale lot scaling; one OOS window 2024-11-20..2025-11-19 (261 days), 1.0 pip flat spread, 1:500 leverage. 444 trades, win rate 65.77%, profit factor 2.85, max equity drawdown 79.97% (verbatim Table 4). Authors: "should be read as a methodological demonstration ... rather than a universal performance claim."
- **Relevance:** None: martingale lot scaling and ~80% equity drawdown conflict with SPEC risk rules; single 12-month window after our data; profit comes from position sizing, not a direction signal. **Status:** VERIFIED.

### Lo Duca & Stracca (2015), "Worth the hype? The effect of G20 summits on global financial markets", J. International Money and Finance 53, 192-217 (added 2026-11-23 R393)
- **Link:** [IDEAS](https://ideas.repec.org/a/eee/jimfin/v53y2015icp192-217.html), DOI [10.1016/j.jimonfin.2015.01.003](https://doi.org/10.1016/j.jimonfin.2015.01.003) (IDEAS record opened via web-fetch; full text paywalled, not read).
- **Design/finding:** event study of G20 Ministerial and Leaders meetings, 2007-2013, on equity returns, bond yields and implied volatility/skewness/kurtosis. Abstract: "G20 summits have not had a strong, consistent and durable effect on any of the markets that we consider". No FX result stated in the abstract; event count not stated.
- **Relevance:** None for an item: published null, no EUR/USD result, and too few events for our power floor. **Status:** VERIFIED (abstract only).

### Dodd, Fernandez-Perez & Sosvilla-Rivero (2022), "Currency and commodity return relationship under extreme geopolitical risks: Evidence from the invasion of Ukraine", IREA WP 2022/04 (added 2026-11-23 R394)
- **Link:** [UB repository PDF](https://diposit.ub.edu/dspace/bitstream/2445/187101/1/IR22_004_Dodd%2bFdez%2bSosvilla.pdf) (opened via web-fetch; full extracted text read).
- **Design/finding:** pooled daily panel of 31 floating currencies vs USD (euro one of them), 2012-01-01..2022-03-11, panel OLS with fixed effects; contemporaneous currency-commodity relation reverses in the ~3-week war window (pooled Commodity x War -0.137, t = -4.30). Caldara-Iacoviello GPR only in a robustness check. No euro-only estimate, no OOS, no trading rule, no costs.
- **Relevance:** None for an item: in-sample, contemporaneous, one short event window, no EUR/USD-specific result. **Status:** VERIFIED.

### Bondarenko, Kang, Lewis, Rottner & Schüler (2026), "Geopolitical risk in the euro area: measurement and transmission", BIS WP 1348 (added 2026-11-23 R394)
- **Link:** [BIS landing page](https://www.bis.org/publications/working-paper-1348-geopolitical-risk-euro-area-measurement-and-transmission) (landing page/abstract opened via web-fetch; full PDF not read).
- **Design/finding:** builds a euro-area GPR index (monthly and daily) from European newspapers; VAR transmission to output, prices and policy rates. Abstract mentions no exchange-rate or EUR/USD result. FX content UNVERIFIED (full text not read).
- **Relevance:** None for an item: macro VAR, no stated FX predictability, OOS or cost test; GPR -> FX predictability already covered by Iyke-Phan-Narayan 2022 (R164/R233). **Status:** VERIFIED (abstract only).

### Almeida, Goodhart & Payne (1997), "The Effects of Macroeconomic 'News' on High Frequency Exchange Rate Behaviour", LSE FMG Discussion Paper 258 (added 2026-11-24 R395)
- **Link:** [FMG PDF](https://www.fmg.ac.uk/sites/default/files/2020-10/dp258.pdf) (opened via web-fetch; first ~40% read verbatim, remainder (German-release section, appendices) only summarised by the fetch tool: UNVERIFIED).
- **Design/finding:** DEM/USD 5-minute Reuters quotes, 1992-01-01..1994-12-31, MMS survey surprises for US and German monthly releases; returns 5 min to 12 h after release. Verbatim: US impacts "lose significance very quickly when the observation horizon for the exchange rate is increased", except Payroll and Consumer Confidence, which stay significant to 12 h (units not stated in the text read). Aggregate sign test: 15-min return sign agrees with the 12 h sign for 202 of 325 releases. No OOS, no trading rule, no cost test seen in the text read.
- **Relevance:** None for an item: pre-euro DEM/USD, 3-year in-sample, needs consensus surprises not in the repo; the surprise-free continuation reading is the E026 mechanism (closed NONE on dev), and Conference Board releases (~12/year, ~60 dev events, 12 h hold) sit below the R090 power floor. **Status:** VERIFIED (partial read).

### Valentin (2023), "The Post-ECB Announcement Drift", AFA 2023 poster (added 2026-11-24 R395)
- **Link:** [AEA program page](https://aeaweb.org/conference/2023/program/paper/52E2ERbB) (poster text read in full via web-fetch).
- **Design/finding:** 190 ECB announcement days (~2002-2020); intraday press-conference "information shocks" predict Eurostoxx and 2y OIS drift over t+1..t+20 days. Verbatim: "Direction of drift depends on intraday price reaction during press conference." Strategy: annualised 4.8%, Sharpe 0.45, no costs, no OOS stated. No FX result.
- **Relevance:** None for an item: equities/rates only, ~40 dev ECB meetings (below R090 power floor); EUR/USD post-ECB windows already tested (E013/E014 family, B-items on ECB). **Status:** VERIFIED (poster).

### Roodbar (2018), "An Intraday Examination of the Role of Priors in the Price Discovery Process", PhD thesis, Newcastle University (added 2026-11-24 R396)
- **Link:** [Newcastle eTheses PDF](https://theses.ncl.ac.uk/jspui/bitstream/10443/4230/1/Roodbar%20Mohammadi%2c%20B%202018.pdf) (opened via web-fetch; ~180k of 386k characters read verbatim, rest summary; Chapter 4 incl. Table 4.5 not read).
- **Design/finding:** Ch.2 1-minute EUR/USD volatility (~420 days 2013-2015); Ch.3 5-minute DAX and EUR/USD Nov 2010-Nov 2015, returns in the 24 h before ECB decisions conditional on press rumours: drift positive in tightening, negative in easing with rumours, zero without rumours; full-sample EUR/USD rule no notable advantage; in-sample, costs explicitly ignored. Ch.4 headline (not read, **UNVERIFIED**): "ECB conditional Friday effect", large negative EUR/USD returns on Fridays after Thursday ECB decisions.
- **Relevance:** None for an item: does not test European equity open -> EUR/USD (the searched angle); ECB-meeting events (~48 on dev) sit below the R090 power floor, the ECB meeting calendar is not in the repo (unreachable from the runner, R106/R107/R129), rumour data unavailable, Friday-after-ECB claim unread. **Status:** VERIFIED (partial read); Ch.4 claim UNVERIFIED.

### Domenech Palacios, Jančoková & Tomov (2025), "Reverse Yankee bonds", ECB box in "The international role of the euro" (June 2025) (added 2026-11-24 R397)
- **Link:** [ECB box (Danish-language page of the box)](https://www.ecb.europa.eu/press/other-publications/ire/focus/html/ecb.irebox202506_02~e5ae550b00.da.html) (opened via web-fetch; ~47% read verbatim, rest summary; author list from summary, page metadata shows Tomov only).
- **Design/finding:** monthly local projections from January 2017: lower hedged and unhedged euro borrowing costs relative to USD are followed by a higher euro share of US investment-grade corporate issuance. No EUR/USD spot-direction test, no OOS, no costs.
- **Relevance:** None for an item: issuance shares, monthly, no FX direction; issuance data not in the repo. **Status:** VERIFIED (partial read).

### Časta (2022), "How Credit Improves the Exchange Rate Forecast", CNB Working Paper 7/2022 (added 2026-11-24 R397)
- **Link:** [CNB PDF](https://www.cnb.cz/export/sites/cnb/en/economic-research/.galleries/research_publications/cnb_wp/cnbwp_2022_07.pdf) (opened via web-fetch; abstract and introduction read verbatim, results tables summary only: UNVERIFIED).
- **Design/finding:** monthly error-correction model with US and euro-area corporate-loan stocks; EUR/USD sample 2003-01..2021-10; recursive/rolling OOS vs random walk (Clark-West, DM). Verbatim: "We empirically show statistically and economically significant exchange rates forecastability in the medium and long run". Summary (UNVERIFIED): EUR/USD RMSFE ratio 1.02 at 1 month, below 1 only from ~6 months. No cost test.
- **Relevance:** None for an item: 6-36 month horizons give at most a handful of independent dev observations (far below the R090 power floor); 1-month forecast no better than a random walk; loan data not in the repo. **Status:** VERIFIED (partial read); results figures UNVERIFIED.

### Ederington, Guan & Yang (2019), "The impact of the U.S. employment report on exchange rates", JIMF 90, 257-267, doi:10.1016/j.jimonfin.2018.10.003 (added 2026-11-24 R399)
- **Link:** [RePEc/IDEAS record](https://ideas.repec.org/a/eee/jimfin/v90y2019icp257-267.html) (opened via web-fetch; abstract and metadata only, full text paywalled).
- **Design/finding (abstract):** GBP/USD, JPY/USD, EUR/USD reactions to payrolls, payroll revisions and unemployment-rate surprises vs Bloomberg median forecasts; payroll response strongly conditioned on pre-release analyst uncertainty; markets appear to respond to analyst forecasts before the release. Sample, frequency, post-release drift, OOS and costs not stated in abstract.
- **Relevance:** None for an item: surprise/forecast-dispersion data not in the repo; NFP release-time continuation without surprises already covered by the E026 mechanism (NONE). **Status:** VERIFIED (abstract only).

### Evans & Speight (2011), "Intraday euro exchange rates and international macroeconomic announcements", European Journal of Finance 17(2), 83-110, doi:10.1080/13518470903448457 (added 2026-11-24 R399)
- **Link:** [Cardiff ORCA record](https://orca.cardiff.ac.uk/id/eprint/33529/) (opened via web-fetch; abstract and metadata only).
- **Design/finding (abstract):** 5-minute returns on three euro rates (not named in abstract), 19-month sample; asymmetric responses to surprise components of US/euro-area announcements, state-dependent on economic climate; rate announcements cause jumps beyond the surprise. No post-announcement drift, OOS, costs or trading rule mentioned.
- **Relevance:** None for an item: surprise data not in the repo; short in-sample window. **Status:** VERIFIED (abstract only).

### Fatum & Scholnick (2003), "Do Exchange Rates Respond to Day-to-Day Changes in Monetary Policy Expectations? Evidence from the Federal Funds Futures Market", UC Santa Cruz Center for International Economics, Recent Work (added 2026-11-24 R400)
- **Link:** [eScholarship record](https://www.escholarship.org/uc/item/4cc3291n) (opened via web-fetch; PDF read to ~65% verbatim, later event-study tables and conclusion summary only: UNVERIFIED).
- **Design/finding:** daily DEM/USD, JPY/USD, GBP/USD vs daily changes in 2- and 3-month fed funds futures, 1989-03..2002-02 (DEM/USD to 1998-12); in-sample GARCH with 15 lags plus target-change event study. Verbatim: "day-to-day changes in policy expectations trigger same-day exchange rate responses as opposed to systematic delayed effects"; for DEM/USD "there is no sign of significant next-day effects" (isolated significant lags for JPY/USD only). No OOS, no costs.
- **Relevance:** None for an item: the paper itself finds the response is same-day, not lagged, for the EUR predecessor (DEM/USD); fed funds futures data not in the repo. **Status:** VERIFIED (partial read).

### Piazzesi & Swanson (2006), "Futures Prices as Risk-Adjusted Forecasts of Monetary Policy", FRBSF Working Paper 2006-23 (added 2026-11-24 R400)
- **Link:** [FRBSF PDF](https://www.frbsf.org/wp-content/uploads/wp06-23bk.pdf) (opened via web-fetch; read to ~48% verbatim).
- **Design/finding:** monthly fed funds futures (1988-2005) and quarterly eurodollar futures excess returns predicted by payrolls, Treasury and BBB spreads. Verbatim: "excess returns are surprisingly well predicted by macroeconomic indicators such as employment growth and financial business-cycle indicators such as Treasury yield spreads and corporate bond spreads." No exchange rates.
- **Relevance:** None for an item: no FX outcome; monthly horizon below the R090 power floor. **Status:** VERIFIED (partial read).

### Bernoth & von Hagen (2003), "The Performance of the Euribor Futures Market: Efficiency and the Impact of ECB Policy Announcements", NY Fed conference paper (added 2026-11-24 R402)
- **Link:** [NY Fed PDF](https://www.newyorkfed.org/medialibrary/media/research/conference/2003/bernoth_final.pdf) (opened via web-fetch; first ~40k of ~69k characters read verbatim).
- **Design/finding:** daily 3-month Euribor futures (LIFFE, Dec 1998 - Mar 2002); efficiency tests of futures vs realized rates and futures volatility on ECB Governing Council days. Verbatim: "the Euribor futures show to be unbiased and informational efficient." No exchange rates; no OOS or cost analysis stated.
- **Relevance:** None for an item: no FX outcome; ECB-day effects are same-day; Euribor futures data not in the repo. **Status:** VERIFIED (partial read).

### Ferrero & Nobili (2009), "Futures Contract Rates as Monetary Policy Forecasts", International Journal of Central Banking 5(2) (added 2026-11-24 R402)
- **Link:** [IJCB abstract](https://ijcb.org/journal/ijcb09q2a4.pdf) (abstract page opened; full PDF not opened).
- **Design/finding:** excess returns of euro-area and US short-rate futures, decomposed into risk premium and forecast error. Verbatim: "Excess returns ... are positive, on average, and statistically significant." No exchange rates.
- **Relevance:** None for an item: no FX outcome. **Status:** VERIFIED (abstract only).

### Hossfeld & Röthig (2016), "Do speculative traders anticipate or follow USD/EUR exchange rate movements? New evidence on the efficiency of the EUR currency futures market", Finance Research Letters 18, 218-225 (added 2026-11-24 R402)
- **Link:** [EconPapers record](https://econpapers.repec.org/RePEc:eee:finlet:v:18:y:2016:i:c:p:218-225), DOI 10.1016/j.frl.2016.04.019 (abstract opened; full text paywalled, WP version Bundesbank DP 41/2015 not opened).
- **Design/finding:** CFTC speculative positions vs USD/EUR, predictive regressions with multiple-testing control. Verbatim: "the evidence for speculative positions leading exchange rate movements ... largely collapses if we account for multiple testing, such a pattern does not emerge in the other direction."
- **Relevance:** Negative evidence for a COT-positioning item (weekly, below R090 power floor, already covered by COT refill notes). **Status:** VERIFIED (abstract only).

### Hambuckers & Ulm, "On the role of interest rate differentials in the dynamic asymmetry of exchange rates" (later version of the R316 entry; venue/year not stated in the file) (added 2026-11-24 R405)
- **Link:** [ORBi PDF](https://orbi.uliege.be/bitstream/2268/307590/1/dynamic_skewness.pdf) (opened via web-fetch; first ~40k characters verbatim, tail summary-based).
- **Design/finding:** daily Fed noon rates USD/EUR and USD/CHF, 6 Jan 1999 - 25 Mar 2019; GARCH-SH model with asymmetry driven by the lagged 3-month LIBOR differential (and VIX); one-step-ahead direction forecasts. Abstract (verbatim): "we document superior out-of-sample mean returns of a trading rule exploiting IRD information for EUR and CHF." Trading returns gross; no cost model in the text read. OOS window and per-year figures are summary-based: UNVERIFIED.
- **Relevance:** None new: same paper and data constraint as the R316 entry (daily rate differential not in the pipeline; gross only). Not added. **Status:** VERIFIED (partial read).

### Hui, Genberg & Chung (2009), "Liquidity, Risk Appetite and Exchange Rate Movements during the Financial Crisis of 2007-2009", HKMA Working Paper 11/2009 (added 2026-11-24 R405)
- **Link:** [HKMA PDF](https://www.hkma.gov.hk/media/eng/publication-and-research/research/working-papers/HKMAWP09_11_full.pdf) (opened via web-fetch; first ~40k characters verbatim, tail summary-based).
- **Design/finding:** daily AUD, GBP, EUR, JPY, NZD, CHF vs USD, 9 Aug 2007 - 31 Mar 2009; EGARCH regressions of daily returns on *same-day* changes in risk reversals, carry-to-risk and LIBOR-OIS spreads. Verbatim: "liquidity risk measured by the LIBOR-OIS spread was a significant factor affecting the exchange-rate movements of the euro." In-sample, contemporaneous, crisis sample only, no costs.
- **Relevance:** None for an item: contemporaneous explanation, not prediction; sample precedes dev; LIBOR-OIS not in the pipeline (and LIBOR discontinued). **Status:** VERIFIED (partial read).

### Ghanem, Harasheh, Sbaih & Ajmal (2024), "The predictability of technical analysis in foreign exchange market using forward return: evidence from developed and emerging currencies", Cogent Business & Management 11(1), 2428781, doi:10.1080/23311975.2024.2428781 (added 2026-11-24 R406)
- **Link:** [Unibo CRIS PDF](https://cris.unibo.it/retrieve/handle/11585/996996/56154880-2ad1-4dae-8c72-8a75de65fb83/punlication%2032_Cogent_Technical.pdf) (opened via web-fetch; ~40k of ~76k characters verbatim, tail summary-based).
- **Design/finding:** daily data Jan 2000 - Dec 2022, 10 USD pairs incl. EUR/USD; 497 SMA/RSI/HAMA/KAMA rules; one-way ANOVA of mean forward returns (1-7 days) after buy vs sell signals; full sample, no OOS split. Verbatim: "The returns are calculated without adjustment for transaction costs or interest rates." Developed-pair group finding (verbatim): "no significant and correctly signed SMA indicators for the next day's holding position". EUR/USD-specific figures (e.g. SMA(6,150) 3-day short) are from the summary-based tail: UNVERIFIED.
- **Relevance:** None new: moving-average rules on daily EUR/USD are already covered (B16 / E019 family); in-sample, gross, massive multiple testing. **Status:** VERIFIED (partial read).

### Vlasiuk & Smirnov (2025), "Push-response anomalies in high-frequency S&P 500 price series", arXiv:2511.06177v1 (added 2026-11-24 R406)
- **Link:** [arXiv PDF](https://arxiv.org/pdf/2511.06177v1) (opened via web-fetch, read in full).
- **Design/finding:** SPY NBBO quote updates in event time, Jan 2018 - Dec 2023; lag-resolved push-response decomposition; full-sample with bootstrap bands, no OOS, no costs ("Extending the analysis with explicit transactioncost overlays should also improve trading implementability."). No FX.
- **Relevance:** None (equity ETF microstructure; no EUR/USD). **Status:** VERIFIED.

### Kozhan & Salmon (2008), "On Uncertainty, Market Timing and the Predictability of Tick by Tick Exchange Rates", Warwick FERC WP08-06 (added 2026-11-25 R426)
- **Link:** [CORE PDF](https://core.ac.uk/download/47866.pdf) (opened via web-fetch; first ~40k of ~160k characters verbatim, rest summary-based or unread).
- **Design/finding:** USD/DM transaction data, Reuters D2000-2, one week from 5 Oct 1998 (18,065 trades); GA-evolved rules with a no-trade band, in-sample Mon-Tue, out-of-sample Wed-Fri, White's reality check; abstract reports significant OOS directional predictability and economic value after costs when trade frequency is controlled. Names of the comparison "classic" rules and the cost rate are summary-based: UNVERIFIED.
- **Relevance:** None for the pipeline: pre-euro DM, one week of tick data, no EUR/USD. **Status:** VERIFIED (partial read).

### Schulmeister (2005), "Components of the Profitability of Technical Currency Trading", WIFO WP 263/2005 (added 2026-11-25 R426)
- **Link:** [WIFO PDF](https://wifo.ac.at/wp-content/uploads/upload-8712/WP_2005_263.pdf) (opened via web-fetch; first ~40k of ~57k characters verbatim, tail summary-based).
- **Design/finding:** daily NY noon rates; 1024 MA and momentum models, in-sample DM/$ 1973-1999, out-of-sample euro/dollar 2000-2004; costs 0.02% per trade stated (analysis mainly gross). Table 2 all-models 2000-2004 gross mean 3.82 %/yr, t 0.775 (as extracted; column layout ambiguous for the 25-best row).
- **Relevance:** None new: daily MA/momentum rules on EUR/USD are already covered (B16 / E019 family, NONE on dev); OOS period 2000-2004 predates the repo's dev block. **Status:** VERIFIED (partial read).

### Das & Goswami (2018?), "Testing of Binary Regime Switching Models Using Squeeze Duration Analysis", arXiv:1807.04393 (added 2026-11-25 R426)
- **Link:** [arXiv PDF](https://arxiv.org/pdf/1807.04393) (opened via web-fetch). Year inferred from the arXiv ID: UNVERIFIED.
- **Design/finding:** 18 Indian NIFTY indices, 5-minute data Dec 2016 - Jun 2017; Bollinger-band squeeze durations used as a statistic to test GBM vs regime-switching models (surrogate-data Monte Carlo); no trading rule, no FX, no costs.
- **Relevance:** None (not a trading test; no EUR/USD). **Status:** VERIFIED.

### Tharavanij, Siraprapasiri & Rajchamaha (2015), "Performance of technical trading rules: evidence from Southeast Asian stock markets", SpringerPlus 4:552 (added 2026-11-25 R427)
- **Link:** [Springer PDF](https://link.springer.com/content/pdf/10.1186/s40064-015-1334-7.pdf), DOI 10.1186/s40064-015-1334-7 (opened via web-fetch; first ~40k of ~113k characters verbatim, results tables summary-based: UNVERIFIED).
- **Design/finding:** RSI, Stochastic oscillator (incl. %K/%D cross), MACD, DMI, OBV on five SE Asian stock indices, daily 2000-2013; breakeven vs assumed round-trip costs; most rules not profitable net of costs. No held-out test (summary-based). No Stochastic RSI.
- **Relevance:** None (equities only, no EUR/USD). **Status:** VERIFIED (partial read).

### Oktaba & Grzywińska-Rąpca (2023), "Modification of technical analysis indicators and increasing the rate of return on investment", Central European Economic Journal 10(57) 148-162 (added 2026-11-25 R427)
- **Link:** [reference-global](https://reference-global.com/article/10.2478/ceej-2023-0009?tab=article), DOI 10.2478/ceej-2023-0009 (opened via web-fetch; first ~40k of ~73k characters verbatim, results summary-based: UNVERIFIED).
- **Design/finding:** EUR/USD H1 (MT4) Sep 2021 - Feb 2023; Parabolic SAR + RSI with default vs modified settings/stops; settings chosen and evaluated on the same period, no held-out test, costs not mentioned; summary reports default -1,735 points vs modified +5,970 points over 126 signals.
- **Relevance:** None: in-sample parameter tuning, gross, tiny sample; Parabolic SAR/RSI families already covered. **Status:** VERIFIED (partial read).

### Gröhn (2012), "Using technical analysis to predict future performance of interest rate futures: RSI, its modifications and Moving Average as trading rules", University of Vaasa MSc thesis (added 2026-11-25 R427)
- **Link:** [CORE PDF](https://core.ac.uk/download/197965922.pdf) (opened via web-fetch; first ~40k of ~341k characters verbatim; results sections not read: UNVERIFIED).
- **Design/finding:** RSI, dual-RSI and 1-50 MA rules on 132 short-term interest-rate futures (7 currencies), daily 2000-2009; costs excluded; abstract: no consistent outperformance of buy-and-hold.
- **Relevance:** None (rate futures, no EUR/USD spot). **Status:** VERIFIED (partial read).

### Hassanniakalager, Sermpinis & Stasinakis (2021), "Trading the Foreign Exchange Market with Technical Analysis and Bayesian Statistics", Journal of Empirical Finance 63, 230-251 (added 2026-11-25 R428)
- **Link:** [Glasgow eprint PDF](https://eprints.gla.ac.uk/246954/2/246954.pdf), DOI 10.1016/j.jempfin.2021.07.006 (opened via web-fetch; first ~40k of ~120k characters verbatim; data period, OOS design, costs and all numbers summary-based: UNVERIFIED).
- **Design/finding:** EUR/USD, GBP/USD, USD/JPY daily; 7,846 technical rules (filters, MAs, support/resistance, channel breakouts, OBV) screened with a Romano-Shaikh-Wolf data-snooping test, survivors combined by Naive Bayes / RVM / DMA / DMS / Bayesian NN; rolling 3-year in-sample / 1-year OOS; costs reportedly 3 bp per trade. Abstract: TA has value "but the profit margins are small". Summary: simple average of top rules about -0.9% on EUR/USD; Bayesian combinations about 2-6% annualised. Footnote: reported results use best in-sample performance. No Gann, Wyckoff or market-profile rules.
- **Relevance:** None for a new item: daily rule-ensemble / ML family already covered (E051 line), single-rule survivors are near zero after costs, and replicating a 7,846-rule screen would inflate the trial count without a single pre-registrable mechanism. **Status:** VERIFIED (partial read).

### Krauss & Stübinger (2015), "Nonlinear dependence modeling with bivariate copulas: Statistical arbitrage pairs trading on the S&P 100", FAU IWQW Discussion Paper 15/2015 (added 2026-11-25 R429)
- **Link:** [FAU PDF](https://www.iwf.rw.fau.de/files/2015/12/15-2015.pdf) (opened via web-fetch; partial read, figures beyond the introduction summary-based: UNVERIFIED).
- **Design/finding:** S&P 100 constituents, daily 1990-2014; copula mispricing signals, 60-month formation / 12-month out-of-sample trading; 0.50% per round trip and one-day wait; intro: net returns "remain above 5 percent per annum".
- **Relevance:** None (US equities pairs, no FX). **Status:** VERIFIED (partial read).

### Cerrato, Li & Zhang (2021), "Factor Investing and Currency Portfolio Management", University of Glasgow working paper (added 2026-11-25 R429)
- **Link:** [Glasgow PDF](https://www.gla.ac.uk/media/Media_734975_smxx.pdf) (opened via web-fetch; partial read, numbers summary-based: UNVERIFIED).
- **Design/finding:** weekly allocation across four currency factors (DOL, carry, momentum, value) from 31 USD crosses, DCC skewed-t copula, real-time OOS 1994-2020 with forward bid/ask costs.
- **Relevance:** None for a single-pair EUR/USD rule (multi-currency factor allocation, weekly). **Status:** VERIFIED (partial read).

### Anatolyev, Gospodinov, Jamali & Liu (2017), "Foreign exchange predictability and the carry trade: A decomposition approach", Journal of Empirical Finance 42, 199-211 (added 2026-11-25 R429)
- **Link:** [AUB repository PDF](https://scholarworks.aub.edu.lb/server/api/core/bitstreams/3126a2e8-780e-4115-8741-1cf0f5015db8/content) (opened via web-fetch; partial read, all numbers summary-based: UNVERIFIED).
- **Design/finding:** nine USD crosses incl. EUR (DEM-spliced), monthly 1976-2016, OOS 2004-2016; sign/magnitude decomposition model sets carry positions, bid/ask used; summary: significance for GBP, CHF, EUR only.
- **Relevance:** None for a new item: monthly horizon gives ~60-100 decisions in dev/val, below the power floor; needs monthly forward/interest-rate data not in the pipeline. **Status:** VERIFIED (partial read).

### Landgraf (2016), "High-Frequency copula-based pairs trading on U.S. Goldmine Stocks", Erasmus University Rotterdam MSc thesis (added 2026-11-25 R429)
- **Link:** [thesis.eur.nl PDF](https://thesis.eur.nl/pub/34694/Landgraf.pdf) (opened via web-fetch; partial read: UNVERIFIED beyond abstract/intro).
- **Design/finding:** 11 US gold-mining stocks, minute bars 1998-2016, intraday formation/trading windows; abstract: no variant remains profitable after costs (intro states up to 26 bp/day for distance/cointegration: conflicting).
- **Relevance:** None (equities, no FX). **Status:** VERIFIED (partial read).

### Harris & Yilmaz (2008), "A Momentum Trading Strategy Based on the Low Frequency Component of the Exchange Rate", Exeter Xfi WP 08/04 (added 2026-11-25 R430)
- **Link:** [ore.exeter.ac.uk PDF](https://ore.exeter.ac.uk/repository/bitstream/10036/3463/7/0804.pdf) (opened via web-fetch; partial read, tables UNVERIFIED).
- **Design/finding:** 9 USD pairs incl. EUR, monthly 1986-2008, recursive OOS 1993-2008; MA(m,n) rules vs MA(1,2) on HP-filter / kernel trend; costs ignored. EWP: HP/kernel trend improves accuracy and Sharpe over raw MA; text says EUR is the exception where HP does not beat MA.
- **Relevance:** None for a new item: monthly horizon below power floor; MA/trend family already tested; no costs. No MA-envelope/regression-channel/Elder rule. **Status:** VERIFIED (partial read).

### Hutchinson, Kyziropoulos, O'Brien, O'Reilly & Sharma (2022), "Technical trading rule profitability in currencies: It's all about momentum", RIBAF 63, 101779 (added 2026-11-25 R430)
- **Link:** [repository.adu.ac.ae PDF](https://repository.adu.ac.ae/bitstreams/30d15095-739e-4967-a33f-7233bf0644df/download) (opened via web-fetch; partial read).
- **Design/finding:** G11 vs USD (EUR incl.) daily, in-sample 1980-1998, OOS 1999-2020; filter, MA, channel (price-range) breakout and trading-range breakout, 388 parameterisations, net of costs (paper states two inconsistent cost schedules). Mean Sharpe falls 0.62 in-sample -> 0.06 OOS; no rule class significant OOS for the G11 portfolio; only MA keeps a small significant net alpha. No EUR-specific rule result in text read.
- **Relevance:** Corroborates lessons on technical-rule decay (B16 family); no new admissible item. **Status:** VERIFIED (partial read).

### Potì, Levich & Pattitoni (2012 WP), "Technical Trading, Predictability and Learning in Currency Markets" (added 2026-11-25 R430)
- **Link:** [archive.nyu.edu PDF](https://archive.nyu.edu/jspui/bitstream/2451/31452/2/PLP1.pdf) (opened via web-fetch; partial read, EUR table values UNVERIFIED).
- **Design/finding:** CME currency futures 1988-2010, monthly, rolling-window ARMA+GARCH "rational" rules vs AFX momentum and carry indices; says costs controlled. Text says the euro shows a high alpha; table values not verified.
- **Relevance:** None for a new item: monthly futures, below power floor; ARMA/ML lag-return family already tested (E050/E051). **Status:** VERIFIED (partial read).

### Ciucu & Paun (2015), "Financial data analysis using nonlinear time series methods. Fluctuations interpretation of foreign currency exchange rates", U.P.B. Sci. Bull. Series A 77(1) (added 2026-11-25 R431)
- **Link:** [scientificbulletin.upb.ro PDF](https://scientificbulletin.upb.ro/static/pdfs/rezc22_956953.pdf) (opened via web-fetch).
- **Design/finding:** EUR/RON and CHF/RON daily NBR rates 2013-01-01..2015-02-05; descriptive box-counting fractal dimension (~1.7 EUR/RON, ~1.67-1.68 CHF/RON). No trading rule, forecast, OOS or costs; no EUR/USD.
- **Relevance:** None. **Status:** VERIFIED.

### Miranda-Agrippino & Nenova (2021), "A Tale of Two Global Monetary Policies", CFM Discussion Paper 2021-17 (added 2026-11-25 R433)
- **Link:** [lse.ac.uk PDF](https://www.lse.ac.uk/CFM/assets/pdf/CFM-Discussion-Papers-2021/CFMDP2021-17-Paper.pdf) (opened via web-fetch; partial read).
- **Design/finding:** daily event-window/local projections 1999-2017 and monthly BVAR 2000-2018 of responses to Fed and ECB policy surprises (conventional and unconventional); EUR/USD is a response variable. Verbatim abstract: "Monetary policy tightenings in both areas are followed by a global retrenchment in capital flows". No prediction of future FX returns, no OOS, no costs in text read.
- **Relevance:** None for a new item: contemporaneous responses; policy-announcement windows already covered (ECB/FOMC lines). **Status:** VERIFIED (partial read).

### Bartram, Grinblatt & Xu (2025), "Monetary Policy Predicts Currency Movements", NBER WP 33423 (also CEPR DP 19881) (added 2026-11-25 R433)
- **Link:** [IDEAS/RePEc abstract](https://ideas.repec.org/p/nbr/nberwo/33423.html) (abstract page opened; full text not opened).
- **Design/finding:** verbatim: "The relative restrictiveness of a central bank's supply of money predicts the raw and risk-adjusted returns of its currency" — "next month and at least three years into the future"; restrictiveness built from out-of-sample panel regressions of M1 on macro variables. Sample, EUR/USD-specific results, OOS test of returns and costs not stated on the page (UNVERIFIED).
- **Relevance:** None for a new item: monthly cross-currency signal, below the single-pair power floor on dev/val; M1 data not in pipeline. **Status:** VERIFIED (abstract only).

### Doganov (2012), "Exchange rates and economic surprise indexes", MSc thesis, Erasmus School of Economics (added 2026-11-25 R434)
- **Link:** [thesis.eur.nl PDF](https://thesis.eur.nl/pub/12870/Doganov,%20V.S.%20%28324535%29.pdf) (opened via web-fetch; partial read).
- **Design/finding:** monthly EUR/USD, USD/JPY, GBP/USD, Jan 2003 - Mar 2012; Citi economic surprise indexes (CESI); estimation to Dec 2006, OOS 2007 - Mar 2012 with lagged index values. Abstract: "economic surprises only influence the direction of change of exchange rates". Transaction costs reportedly not included (from summary, not verbatim: UNVERIFIED); per-table EUR/USD figures came from a garbled extraction and are not cited.
- **Relevance:** None for a new item: monthly horizon (below the single-pair power floor on dev/val, lesson R090), unpublished thesis, no costs; CESI data not in pipeline. **Status:** VERIFIED (partial read).

### Evans & Speight (2010), "Dynamic news effects in high frequency Euro exchange rates", JIFMIM 20(3), 238-258 (added 2026-11-25 R434)
- **Link:** [ORCA record](https://orca.cardiff.ac.uk/id/eprint/22759/), DOI [10.1016/j.intfin.2010.03.002](https://doi.org/10.1016/j.intfin.2010.03.002) (repository record opened; full text not read).
- **Design/finding:** 5-minute EUR/USD and EUR/GBP responses to macro announcement surprises. Verbatim abstract: "The reaction of exchange rate returns to news is very quick and occurs within the first 5 min of the release with very little reaction in the 15 min before and after"; US news "generates far more dramatic responses in EUR–USD returns". No lagged prediction, OOS or costs stated.
- **Relevance:** None: contemporaneous reaction; argues against a post-release (incl. UK-release) EUR/USD drift item. **Status:** VERIFIED (abstract only).

### Castrén & Mazzotta (2005), "Foreign exchange option and returns based correlation forecasts: evaluation and two applications", ECB WP 447 (added 2026-11-25 R435)
- **Link:** [ECB PDF](https://www.ecb.europa.eu/pub/pdf/scpwps/ecbwp447.pdf) (opened via web-fetch; partial read).
- **Design/finding:** daily OTC 1-month implied vols for cross-rate triangles incl. USD/EUR, Jan 1992 - Mar 2004; implied vs historical/RiskMetrics/GARCH correlation forecasts of 21-day realised correlation. Verbatim: regressions are "carried out in-sample". Appendix Fama-type regressions of one-month spot changes reported only via a model summary (UNVERIFIED, not cited). No costs.
- **Relevance:** None for a new item: forecasts correlation, not EUR/USD direction; in-sample; monthly horizon below the power floor; option-implied data not in pipeline. **Status:** VERIFIED (partial read).

### Tsaknaki, Lillo & Mazzarisi (2024), "Bayesian Autoregressive Online Change-Point Detection with Time-Varying Parameters", arXiv 2407.16376 (added 2026-11-25 R436)
- **Link:** [ar5iv HTML](https://ar5iv.labs.arxiv.org/html/2407.16376) (opened via web-fetch; partial read, appendices and end of Section 5.3 not read).
- **Design/finding:** BOCPD extended with AR(q) structure and score-driven time-varying variance/correlation. Applications: bee waggle-dance trajectories, quarterly US real GNP 1951-2019, 4-minute order flow for MSFT (Mar 2020) and TSLA (Dec 2021). Evaluation is one-step-ahead out-of-sample MSE / Diebold-Mariano only; no trading rule, returns or costs; no FX in text read.
- **Relevance:** None: methodology only, no EUR/USD direction or cost-aware trading evidence. **Status:** VERIFIED (partial read).

### Costantini, Crespo Cuaresma & Hlouskova (2016), "Forecasting errors, directional accuracy and profitability of currency trading: The case of EUR/USD exchange rate", Journal of Forecasting 35, 652-668 (added 2026-11-25 R437)
- **Link:** [BURA 2438/12673](https://bura.brunel.ac.uk/handle/2438/12673), DOI [10.1002/for.2398](https://doi.org/10.1002/for.2398) (abstract page opened via web-fetch; full text not read).
- **Design/finding:** out-of-sample EUR/USD forecasts from multivariate macroeconomic models and forecast combinations (incl. principal components of forecasts), evaluated by forecast error, directional accuracy and trading profit with data-snooping-robust tests; combinations improve over benchmark trading strategies but "the excess return per unit of deviation is limited".
- **Relevance:** None for a new item: macro-model inputs not in pipeline, low-frequency horizon, limited economic value. **Status:** VERIFIED (abstract only).

### Ballarin, Capra & Dellaportas (2025), "Multi-Horizon Echo State Network Prediction of Intraday Stock Returns", arXiv 2504.19623 (added 2026-11-25 R437)
- **Link:** [arXiv HTML](https://arxiv.org/html/2504.19623v1) (opened via web-fetch; partial read).
- **Design/finding:** ESN on ~500 US stocks, 10-min bars, tuning Q4 2012, evaluation 2013; MSFE gains vs linear baseline (>0.87% at 10 min, shrinking with horizon); no directional/trading results or costs; no FX.
- **Relevance:** None: no EUR/USD, no cost-aware trading evidence. **Status:** VERIFIED (partial read).

### Edlund (2025), "AI-Driven Predictions of Industrial Metal Prices on the London Metal Exchange: Optimizing Echo State Networks with Genetic Algorithms", MSc thesis, Chalmers (added 2026-11-25 R437)
- **Link:** [Chalmers ODR PDF](https://odr.chalmers.se/server/api/core/bitstreams/91a98bfc-3cf6-455d-bead-16658012600e/content) (opened via web-fetch; partial read).
- **Design/finding:** daily LME metal cash prices 2008-2024; ESN-GA does not consistently outperform a random walk on the held-out test set; no costs; no FX.
- **Relevance:** None. **Status:** VERIFIED (partial read).

### Maitah, Prochazka, Cermak et al. (2016), "Commodity Channel Index: Evaluation of Trading Rule of Agricultural Commodities", Int. J. Econ. Financial Issues 6(1) 176-178 (added 2026-11-25 R438)
- **Link:** [IDEAS record](https://ideas.repec.org/a/eco/journ1/2016-01-23.html) (opened via web-fetch; abstract page only, full text not fetched).
- **Design/finding:** CCI trading rule on agricultural commodities; abstract reports results "positive in term of % CCI", no figures; no FX; sample, OOS and costs not stated on the page.
- **Relevance:** None (no EUR/USD). **Status:** VERIFIED (abstract only).

### Zafeiriou & Kalles (2024), "Comparative analysis of neural network architectures for short-term FOREX forecasting", arXiv 2405.08045 (added 2026-11-25 R438)
- **Link:** [arXiv 2405.08045](https://www.arxiv.org/pdf/2405.08045) (opened via web-fetch; read in full).
- **Design/finding:** EUR/USD tick data Oct-Dec 2021 only; custom ANN with indicator inputs including CCI-300 (thresholds +/-150, +/-100) vs LSTMs (trained on first half of each month, tested on second half); "successful signal" = threshold move within 900 ticks, 81.13% (ANN) vs 72.64% (best LSTM); no P&L figures, no costs, three-month sample.
- **Relevance:** None for the pipeline: signal-hit metric, not cost-aware returns; sample far below the power floor; not a held-out period. **Status:** VERIFIED.

### Shahria (2026), "Artificial Intelligence for Time Series", MSc thesis, Vilnius University (added 2026-11-25 R438)
- **Link:** [VU ePublications PDF](https://epublications.vu.lt/object/elaba:308157703/308157703.pdf) (opened via web-fetch; partial read, ~1/3 verbatim plus summary).
- **Design/finding:** daily EUR/USD Dec 2003-Dec 2025; single-hidden-layer FFNN and KNN on distance-filtered patterns; test set 2024-2025 is 11 patterns; best single seed 72.73% accuracy, 100-seed median 54.55%; thesis states the test is not statistically significant; no trading simulation or costs; no CCI or Kolmogorov-Arnold networks.
- **Relevance:** None (11 test patterns, seed selection, no costs). **Status:** VERIFIED (partial read).

### Saly-Kaufmann, Wood, Calliess & Zohren (2026), "How do standard time series forecasting benchmarks translate to finance? A broad study of risk adjusted performance", arXiv 2603.01820 (added 2026-11-25 R439)
- **Link:** [arXiv 2603.01820](https://arxiv.org/pdf/2603.01820) (opened via web-fetch; ~1/3 verbatim plus summary).
- **Design/finding:** daily multi-asset futures 1990-2024/25, walk-forward (train 1990-2010, OOS 2010 on, 5-year retraining); deep models incl. Temporal Fusion Transformer (OOS Sharpe 2.27), VLSTM 2.40, LPatchTST 2.29 on a portfolio; headline tables gross (c=0); FX futures listed are DX, USD/SEK, USD/SGD, USD/NZD, NOK/USD, CAD/JPY, JPY, CHF; no EUR/USD contract seen; per-asset FX breakeven costs ~1-2 bps (summary only, not checked).
- **Relevance:** None for the pipeline: no EUR/USD result, portfolio-level gross headline, per-asset FX breakevens near or below EUR/USD costs. **Status:** VERIFIED (partial read).

### Bilis, Papadimitriou, Diamantaras & Goulianas (2025), "EXPERT: EXchange Rate Prediction Using Encoder Representation from Transformers", Forecasting 7(4) 65, DOI 10.3390/forecast7040065 (added 2026-11-25 R439)
- **Link:** [MDPI Forecasting 7/4/65](https://www.mdpi.com/2571-9394/7/4/65) (opened via web-fetch; ~3/4 read, part summary).
- **Design/finding:** daily OHLC, nine pairs incl. EUR/USD 1999-2022 (MetaTrader); transformer encoder forecasts next-day close; final 14% split held out; EUR/USD next-day MAPE 0.298% equals the random-walk benchmark (summary); trading test Dec 2018-Mar 2022 +2.36%/yr vs -0.77% buy-and-hold, no costs stated.
- **Relevance:** None: point forecast ties the random walk on EUR/USD; trading result gross; deep-learning-on-lagged-prices family already closed on dev (E051 random forest NONE). **Status:** VERIFIED (partial read).

### Noguer i Alonso & Pereira Franklin (2026), "Pretrained Time-Series Foundation Models for Financial Return Forecasting", arXiv 2606.27100 (added 2026-11-25 R440)
- **Link:** [arXiv 2606.27100](https://arxiv.org/pdf/2606.27100) (opened via web-fetch; ~first third verbatim plus summary).
- **Design/finding:** zero-shot TSFMs (Chronos, Moirai, TimesFM) on five US equities, daily 2014-2026, 20-business-day returns, rolling-origin evaluation after Aug 2024; abstract: gains over the random walk "small and sparse"; forecast error only, no trading or costs.
- **Relevance:** None (no FX, no trading test). **Status:** VERIFIED (partial read).

### Marconi (2025), "Time Series Foundation Models for Multivariate Financial Time Series Forecasting", arXiv 2507.07296 (added 2026-11-25 R440)
- **Link:** [arXiv 2507.07296](https://arxiv.org/abs/2507.07296v1) (opened via web-fetch; abstract plus ~first half of PDF; rest unread).
- **Design/finding:** TTM/Chronos on daily 2005-2025; EUR/USD task is 21-day realised volatility (MSE), not direction; abstract: specialised models "matched or exceeded" TTM in two of three tasks; no costs.
- **Relevance:** None (volatility, not direction; no trading). **Status:** VERIFIED (partial read).

### Lemeneh, Hadad, ... Tomasic & Shasha (2026), "ForExAI: Time Series Inference and News Article Analysis Reveal Profitable Foreign Exchange Signals", Mathematics 14(13) 2319, DOI 10.3390/math14132319 (added 2026-11-25 R440)
- **Link:** [MDPI Mathematics 14/13/2319](https://www.mdpi.com/2227-7390/14/13/2319) (opened via web-fetch; parts verbatim, cost section via summary only).
- **Design/finding:** minute USD/EUR (plus CNY, BRL, GBP); train Jan-Jun 2024, val Jul-Aug 2024, test Sep 2024-Dec 2025; Chronos-Bolt/Toto/TCN/N-BEATS + news; headline profits at zero cost; abstract: "not directly actionable"; cost table caption (summary): costs "eliminate the profitability of all strategies" except one Kelly trend variant; no random-walk comparison.
- **Relevance:** None for the pipeline: gross headline, test period entirely after OOS start, one surviving variant out of many. **Status:** VERIFIED (partial read; cost table UNVERIFIED verbatim).

### Petric (2025), "How the Trajectory of Asset Prices Can Predict FX Movements", CFA Institute Enterprising Investor blog, 19 July 2025 (added 2026-11-25 R441)
- **Link:** [CFA Institute blog](https://blogs.cfainstitute.org/blog/2025/07/19/how-the-trajectory-of-asset-prices-can-predict-fx-movements) (opened via web-fetch).
- **Design/finding:** non-technical commentary on path-signature (rough-path) features for FX forecasting; no pair named, no data, no OOS test, no costs, no numbers; "early studies" cited without references.
- **Relevance:** None (commentary, no evidence). **Status:** VERIFIED (opened).

### de Favereau de Jeneret & Diamantis (2026), "Topology of Currencies: Persistent Homology for FX Co-movements: A Comparative Clustering Study", Data Science in Finance and Economics 6(2) 183-211, DOI 10.3934/DSFE.2026007; preprint arXiv 2510.19306 (added 2026-11-25 R441)
- **Link:** [DSFE PDF](https://www.aimspress.com/aimspress-data/dsfe/2026/2/PDF/DSFE-06-02-007.pdf), [arXiv 2510.19306](https://arxiv.org/html/2510.19306v1) (both opened via web-fetch; arXiv HTML truncated).
- **Design/finding:** unsupervised clustering of 13 currencies vs EUR (incl. USD), ECB daily reference rates 2000-2022/2024 resampled to 266 monthly returns; TDA features give modestly better silhouette scores (0.19 vs 0.11) than correlation features; descriptive, no forecasting, no OOS, no costs.
- **Relevance:** None (no directional prediction, monthly). **Status:** VERIFIED.

### Auerbach & Gorodnichenko (2016), "Effects of Fiscal Shocks in a Globalized World", IMF Economic Review 64(1) (added 2026-11-26 R453)
- **Link:** [eScholarship PDF](https://escholarship.org/content/qt8s21f6sg/qt8s21f6sg.pdf) (opened via web-fetch; truncated, rest from fetch summary).
- **Design/finding:** daily US fiscal news (DoD contract announcements; Treasury Daily Statement defense payments) vs the Fed trade-weighted USD index (index name and ~1994-2014 sample from summary, UNVERIFIED verbatim); the dollar "appreciates" on announcement, peak "after about 25 working days"; payments show "no tangible effect". Impulse responses only; no OOS forecast, no costs (absence UNVERIFIED for unread parts). Not about the Monthly Treasury Statement.
- **Relevance:** None for the pipeline: USD index not EUR/USD, DoD contract data not in pipeline, no predictive test. **Status:** VERIFIED (partial read).

### Adrian, Etula & Shin (2009, rev. 2015), "Risk Appetite and Exchange Rates", FRB New York Staff Report 361 (added 2026-11-26 R453)
- **Link:** [NY Fed SR361 page](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr361.html) (opened via web-fetch; PDF content truncated, rest from fetch summary). Full PDF fetch failed (permission not granted in time), not retried.
- **Design/finding:** monthly; 23 USD bilateral rates (9 advanced, 14 emerging) and USD indices, 1993-2014; predictors detrended log primary-dealer repo and financial commercial paper outstanding ("published weekly by the Federal Reserve Board and the Federal Reserve Bank of New York"; detrending "performed out of sample"). Recursive OOS from 1997 (Clark-West, DM/West vs random walk): model "outperforms both benchmarks for 6 out of 9 advanced countries" (verbatim). EUR/DEM row of the OOS table NOT read: UNVERIFIED. No costs (absence UNVERIFIED).
- **Relevance:** weak prior only: EUR-specific OOS result unverified (lesson R095 bar not met); monthly horizon gives ~72 dev months (underpowered); dealer-repo series reporting changed over time and is not in the pipeline. **Status:** VERIFIED (partial read); EUR row UNVERIFIED.

### Caruso (2016), "The Impact of Macroeconomic News on the Euro-Dollar Exchange Rate", Working Papers ECARES 2016-32, ULB (added 2026-11-26 R454)
- **Link:** [IDEAS/RePEc page](https://ideas.repec.org/p/eca/wpaper/2013-235612.html) (abstract page opened via web-fetch; full PDF not fetched).
- **Design/finding (abstract only):** daily USD/EUR, 1999-2012; "news" = Bloomberg-consensus surprises for US and euro-zone releases, incl. country-level announcements for Germany, France, Italy and Spain; both US and euro-zone news significantly affect USD/EUR, and "the effect of the euro-zone "news" has become larger since the 2008 crisis" (verbatim). Abstract does not mention German CPI specifically, post-release drift, OOS tests or costs (absence UNVERIFIED for the full paper).
- **Relevance:** None for an item: contemporaneous daily reaction to surprises; Bloomberg consensus not in pipeline. **Status:** VERIFIED (abstract only).

### Garcia & Werner (2018), "Inflation News and Euro Area Inflation Expectations", IMF Working Paper WP/18/167 (added 2026-11-26 R455)
- **Link:** [IMF PDF](https://www.imf.org/-/media/Files/Publications/WP/2018/wp18167.ashx) (opened via web-fetch; text truncated, first part read).
- **Design/finding:** reaction of euro-area 5y5y inflation-linked swap rates to inflation news incl. HICP flash estimates (Germany, Spain, Italy, euro area); daily regressions 2005-2017, intraday IL-swap windows of 15 and 120 minutes after release; surprises vs Bloomberg consensus. "statistically significant reactions mainly refer to the release of flash estimates at country level".
- **Relevance:** None for an item: no EUR/USD, contemporaneous windows only, no drift/OOS/costs; consensus data not in pipeline. **Status:** VERIFIED (partial read).

### Spange & Sørensen (2016), "Effects of Danmarks Nationalbank's interventions in the foreign exchange market", Danmarks Nationalbank Monetary Review Q4 2016, p. 61 (added 2026-11-26 R460)
- **Link:** [DN page](https://nationalbanken.dk/en/news-and-knowledge/publications-and-speeches/archive-publications/2017/effects-of-danmarks-nationalbank-s-interventions-in-the-foreign-exchange-market), [PDF](https://www.nationalbanken.dk/media/ts2h0rfe/effects-of-dns-interventions-in-the-foreign-exchange-markets-mon4q-2016.pdf) (both opened via web-fetch; PDF read in full).
- **Design/finding:** daily EUR/DKK (17:00 Danish close), 2002 to 2016-10-24; regression of daily krone change on DN interventions with IV (prior five days' interventions) and sub-periods; "interventions constitute an effective instrument to stabilise the exchange rate". No EUR/USD, no OOS, no costs; DN "does not publish data on its interventions on a daily basis".
- **Relevance:** None for an item: EUR/DKK peg only, intervention dates not public at daily frequency. **Status:** VERIFIED.

### Bugaenko (2019), "Empirical Study of Market Impact Conditional on Order-Flow Imbalance", MSc dissertation (arXiv 2004.08290) (added 2026-11-27 R473)
- **Link:** [arXiv PDF](https://arxiv.org/pdf/2004.08290) (opened via web-fetch; last ~7% not read).
- **Design/finding:** NASDAQ LOBSTER event-level order-book data for a few stocks, 2015; price impact vs order-flow imbalance; "for small signed order-flows, the price impact grows linearly with increase in the order-flow imbalance". No FX, no directional/profit test, no costs.
- **Relevance:** None for an item: equities, impact not direction. **Status:** VERIFIED (partial read).

### Temnov (2015), "Analysis of Ornstein-Uhlenbeck process stopped at maximum drawdown and application to trading strategies with trailing stops", arXiv 1507.01610 (added 2026-11-27 R473)
- **Link:** [arXiv abstract](https://arxiv.org/abs/1507.01610), [v1 PDF](https://arxiv.org/pdf/1507.01610v1) (opened via web-fetch).
- **Design/finding:** weekly EUR/USD strategy (entry after a set move from a weekly zero-level; exit on trailing stop, profit call or week end), 2011-mid 2015; four parameters re-optimised on the prior 1-3 years and applied to the next year; mean weekly P&L ~107-127 EUR per 1000 EUR position at 1:200 leverage, unstable by year (2014 weak); overnight commission 0.14% only, no spread; no significance test; abstract calls results "hypothetical".
- **Relevance:** Low: no fixed parameter set to pre-register, no spread cost, unstable. **Status:** VERIFIED.

### Tuzun (2013), FEDS WP 2013-48: Are Leveraged and Inverse ETFs the New Portfolio Insurers? (R483)
- https://www.federalreserve.gov/pubs/feds/2013/201348/201348pap.pdf (~50% verbatim). US equity-index LETFs 2006-2011; late-day
  (3-4 pm ET) rebalancing price impact on constituents, partial next-day reversal. Equities only, no FX, in-sample, no costs.

### Zhao (2026 draft), arXiv 2608.03703: Preying on Leveraged ETFs (R483)
- https://arxiv.org/pdf/2608.03703 (~14% verbatim). Korean single-stock LETFs (Samsung, SK Hynix) 2026; predictable closing
  rebalance, close overshoot and ~60% next-close reversal. Equities only, no FX, no OOS; cost treatment UNVERIFIED.

### Nguyen & Nguyen (2024), IMF WP/24/186: Currencies in Turbulence: Exploring the Impact of Natural Disasters on Exchange Rates (R489)
- https://www.imf.org/en/Publications/WP/Issues/2024/08/30/Currencies-in-Turbulence-Exploring-the-Impact-of-Natural-Disasters-on-Exchange-Rates-553991
  (landing page and text extraction opened via web-fetch; DOI 10.5089/9798400289385.001). Monthly NEER/REER, 177 countries 1970-2019,
  EM-DAT disasters >= 0.1% of GDP, local projections. Large NEER effects in non-pegged EMDEs, mostly insignificant for advanced
  economies. No bilateral EUR/USD, no trading rule, no OOS, no costs. **Relevance:** none for an item. **Status:** VERIFIED (partial read).

### van Donk (2020), Erasmus BSc thesis: Natural disaster effects on exchange rates, a preliminary study (R489)
- https://thesis.eur.nl/pub/53079/thesis_final.pdf (full text opened via web-fetch; tables partly garbled). JPY, NZD, THB, PHP vs USD,
  four Asia-Pacific disasters (2004-2013), daily GARCH / event study, minute data for JPY/NZD. Only Japan 2011 significant (yen up);
  author calls longer-term results exploratory and not robust. No EUR/USD, no OOS, no trading rule, no costs. **Relevance:** none.
  **Status:** VERIFIED.

### Cai & Zhang (2016) venue/year update (R490; supersedes only the "year UNVERIFIED" note of the R140 entry above)
- https://econpapers.repec.org/RePEc:bla:eufman:v:22:y:2016:i:1:p:120-141 and https://durham-repository.worktribe.com/output/1394658
  (abstract pages opened via web-fetch 2026-11-27) and https://eu.vlex.com/vid/highfrequency-exchange-rate-forecasting-855644276
  (introduction only, rest paywalled). European Financial Management 22(1), 120-141, 2016, DOI 10.1111/eufm.12052. ACM-ACD
  (Russell-Engle) model of tick-by-tick quote-change direction, out-of-sample evaluation per the introduction; abstract (verbatim):
  "with the rate of correct predictions varying from 54 to 70%". Transaction costs not seen. **Relevance:** unchanged (tick-horizon
  next-quote-change direction, below tradable horizon after SPEC 4 costs). **Status:** VERIFIED (abstract + partial text).

### "Financial market geometry: The tube oscillator", arXiv 2407.08036v1 (2024; added 2026-11-28 R496)
- https://arxiv.org/html/2407.08036v1 (full text opened via web-fetch 2026-11-28). Author names not shown in the fetched text
  (affiliations Blacklace Finance, Vienna, and Universität Heidelberg): **authors UNVERIFIED**. Abstract (verbatim, in parts): "a
  simple trading strategy" "based on this oscillator and fixed threshold leads to consistent positive monthly returns" "of average
  magnitude of 2% or more." Data: DAX 40 and EUR/USD, Dukascopy bid/ask ticks resampled to 1 second, 2019-01 to 2024-05, intraday
  positions closed at end of day. Parameters calibrated "visually along 3 trading days" and reported for four configurations over
  the full sample: **no out-of-sample test**. Bid/ask spread charged per trade; no commissions, slippage beyond a 1-second delay,
  or financing. EUR/USD best configuration (bandwidth 300 s, thresholds 0.4/0.1): average monthly return 4.659% (sd 3.334),
  86,774 trades, win rate ~35-43%. **Relevance:** low; sub-minute strategy (repo data are 1-minute bars, SPEC section 2), in-sample
  only, sample overlaps our dev/val years, implausibly high Sharpe for a spread-paying ~70 trades/day rule. **Status:** VERIFIED
  (text opened; authors UNVERIFIED).

### Neely & Weller, "Lessons from the Evolution of Foreign Exchange Trading Strategies" (added 2026-11-28 R498)
- **Venue:** Federal Reserve Bank of St. Louis WP 2011-021D (Sept 2011, revised Apr 2013), [PDF](https://files.stlouisfed.org/files/htdocs/wp/2011/2011-021.pdf)
  (opened 2026-11-28 R498 via web-fetch; full text read, second pass verbatim). Published version not checked.
- **Data / design:** 21 USD rates + 19 crosses, daily, 1975-2012; 17 bilateral rules per currency (7 filter, vma(1,5), vma(5,20),
  vma(1,200), momentum 5/20/60, channel 5/10/20, carry); ex ante ranking on past Sharpe, monthly rebalance; costs = 1/3 of quoted
  forward bid-ask. EUR series is DEM spliced with EUR after 1999-01-01.
- **Finding (verbatim numbers):** Table 2 EUR row, full sample, average of the 17 rules: "EUR 4.21 3.73 4.12 0.64 0.15 16.53 9716"
  (gross AR, net AR, t, Sharpe, s.e., trades/yr/rule, obs). Table 7: "EUR ch(10)" is a top-5 rule in 1973-82 (15.3) and 1983-92
  (24.8) but not in 1993-2002 or 2003-2012. Developed-currency-only re-run: "about half of the 10-strategy and 50-strategy portfolios
  earn negative excess returns in the final sample (2000-2012)" and "none of the portfolios earn statistically significant positive
  Sharpe ratios". Post-1998 rebound "coincides with a strong shift ... away from major currencies to emerging markets".
- **Relevance:** **Low for EUR/USD now.** Full-sample EUR profit is dominated by 1973-1992; for advanced currencies in 2000-2012 the
  paper itself finds no significant profit. Consistent with Neely-Weller-Ulrich (2009) decay and E019 (TSMOM NONE on dev).
  **Status:** VERIFIED (full text opened).

### Kuang, Schröder & Wang (2014), "Illusory Profitability of Technical Analysis in Emerging Foreign Exchange Markets" (added 2026-11-28 R498)
- **Venue:** International Journal of Forecasting 30(2), 192-205, doi:10.1016/j.ijforecast.2013.07.015;
  [author accepted version](https://orca.cardiff.ac.uk/66242/1/WangQ%20-%20IllusoryProfitability.pdf) (opened 2026-11-28 R498 via web-fetch, partly verbatim).
- **Finding:** 25,988 rules on 10 emerging-market currencies vs GBP, daily 1994-2007, OOS 08/2002-07/2007, Reality Check/SPA/StepM;
  abstract (verbatim): "Almost all these profits vanish once the data snooping bias is taken into account." No EUR or DEM.
- **Relevance:** **None** for EUR/USD directly; background on data-snooping in rule searches. **Status:** VERIFIED (partial full text).

### BSIC (2026), "Do Norges Bank's Announced FX Transactions Contain Information About NOK Exchange Rate Dynamics?" (added 2026-11-28 R499)
- **Venue:** Bocconi Students Investment Club article, 18 Oct 2026, authors not named;
  [link](https://bsic.it/do-norges-banks-announced-fx-transactions-contain-incremental-information-about-nok-exchange-rate-dynamics/) (opened 2026-11-28 R499 via web-fetch; short quotes only).
- **Data/design:** daily EUR/NOK 14:15 CET fixing, 5 Jan 2015 - 30 Sep 2026, 143 monthly announcements; announcement-day, execution-day and next-month tests; expanding-window OOS from Feb 2020 (OOS R² and Clark-West). No costs.
- **Finding (quoted):** a NOK1bn increase in the announced daily purchase "weakens the krone by about 0.41% against the euro on the day of the release (p = 0.004)"; execution flow "has no measurable effect"; monthly OOS R² negative ("adding the flow makes the forecasts worse"). Day-0 result rests on a few 2020/2022 events.
- **Relevance:** **None** for EUR/USD: EUR/NOK only, non-peer-reviewed, OOS null. **Status:** VERIFIED (opened).

### CESifo Working Paper 5357 (hit for Italian BTP auctions -> euro) (added 2026-11-28 R499)
- **Link:** https://www.cesifo.org/DocDL/cesifo1_wp5357.pdf (redirects to ifo.de; fetch failed). Title, authors and content **UNVERIFIED**. Not used.

### Aquilina, Garavito, Gelos, Lewrick, Packer, Pinter, Sushko & Todorov (2025), "The transformation of the life insurance industry: systemic risks and policy challenges" (added 2026-11-28 R500)
- **Venue:** BIS Papers No 161, 27 Oct 2025; [link](https://www.bis.org/publ/bppdf/bispap161.pdf) (landing page opened 2026-11-28 R500 via web-fetch; PDF body not readable).
- **Content (abstract only):** private equity, riskier/opaque assets, derivatives, offshore reinsurance; rising systemic importance in the Americas and Asia. No FX-hedging or EUR/USD return evidence in the abstract.
- **Relevance:** **None** for EUR/USD. **Status:** VERIFIED (abstract only; body UNVERIFIED).
