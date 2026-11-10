# E034 Hypothesis: month-end pre-fix equity-hedging flow, Melvin-Prins (B30), dev only (pre-registered 2026-11-10 R072, before any run)

- **H1a (B30-hour):** on dev month-ends D, a EUR/USD position -sign(S(D)) held 15:00 -> 16:00 London on D (the hour before the
  month-end WM/Reuters 4pm fix) earns a mean signed mid return > 1 pip, where S(D) is the EU Stocks 50 log return minus the US 500 log
  return from the previous month-end 16:00 London fix to 16:00 London on D-1.
- **H1b (B30-day):** the same position held 16:00 London on D-1 -> 16:00 London on D earns a mean signed mid return > 1 pip.
- **H0 (each):** the mean signed return is zero.
- **Mechanism [PUB]:** Melvin & Prins (2015), Journal of Financial Markets 22, 50-72, DOI 10.1016/j.finmar.2014.11.001 (abstract
  opened R071 on IDEAS/RePEc): "equity market appreciation over the month can be used to predict currency depreciation before the
  end-of-month fix" (investors hedging foreign equity holdings rebalance their FX hedges at the month-end London fix). A US holder of
  EU equities that rose must sell more EUR forward; an EU holder of US equities that rose must sell more USD. Marsh, Panagiotou &
  Payne (2017, preliminary WP, opened R071) describe it as relative equity outperformance -> negative effect on that currency before
  the last fix (secondary). **UNVERIFIED:** the paper's exact signal construction, window and EUR/USD effect size (full text and
  slides not openable).
- **Parent experiment / variable changed:** none formally; new conditioning variable (relative equity index return, never used).
  Relative: E007 `pre_month_end` (dev, unconditional short EUR/USD 15:00 -> 16:00 London on month-ends: -2.771 pips, i.e. EUR/USD rose
  on average). Conditioning on the equity signal has never been computed.
- **Contamination:** E007 published the unconditional dev month-end pre-fix hour; E030 published a month-end gotobi subset (Tokyo, not
  London). Neither used equity returns. The unconditional mean is reported beside the conditional one (descriptive).
- **Prior expectation (written before data):** low to moderate. n ~ 71 month-ends; E007 pre-fix-hour SD 19.7 pips -> SE ~2.3, so a
  SIGNAL needs a mean of roughly 5 pips in the hour window; the day window has a larger SD (~50 pips estimated) and needs ~12 pips.
  Since the 2015 WM/Reuters fix-window widening (5 minutes) and post-2014 enforcement, pre-fix positioning may have shrunk. The
  published effect size is unknown here.
- **LEAD status:** a dev SIGNAL is not a LEAD; it earns B31 (val confirmation, its own experiment; ~29 val month-ends, low power).
- **Calendar label:** month-end London 4pm fix (WMR). The fix *is* the strategy (AUTONOMOUS_PROTOCOL lead criterion 4).
- **Why now:** top `ready` backlog item (B30, added R071).
