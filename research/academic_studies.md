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
