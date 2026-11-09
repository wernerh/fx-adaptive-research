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
