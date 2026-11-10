# E035 Hypothesis: overnight -> intraday reversal in EUR/USD, daily (B32) and 20-date smoothed (B33), dev only (pre-registered 2026-11-10 R075, before any run)

- **H1a (B32):** on every valid dev trading date D, a position -sign(r_on(D)) held from 07:00 to 16:55 America/New_York on D earns a
  mean signed mid return > 1 pip per date, where r_on(D) = mid 07:00 NY on D - mid 17:05 NY on the evening that opens D (fade the
  overnight move).
- **H1b (B33):** the same trade with position -sign(O20(D)), O20(D) = sum of r_on over the 20 previous dates with a valid r_on
  (D's own overnight excluded), earns a mean signed mid return > 1 pip per date.
- **H0 (each arm):** the mean signed return per date is zero.
- **Mechanism [PUB, partly]:** Krohn, Mueller & Whelan ("Uncovered Interest Parity in High Frequency", 2024 WP, opened R074): the
  Fama slope "switches from a positive value of 1.32 ... during the overnight hours, to -1.28 during the intraday period" (overnight =
  17:00 ET t-1 -> 7:00 ET t; intraday = 7:00 -> 17:00 ET), read as different clienteles pricing currencies at different times. Lou,
  Polk & Skouras (LSE FMG DP 961, 2026, opened R074): in US equities intraday returns mean-revert past overnight returns
  ("t-statistic of -3.98") using a smoothed multi-year overnight signal. **This is an FX daily analogue, not a replication:** neither
  paper reports that a single EUR/USD overnight move reverses intraday. The 20-date window of B33 is our choice (their EWMA has a
  ~10-year centre of mass on monthly data, impossible on 6 dev years). All parameters were fixed in the backlog (R074) before any data.
- **Parent experiment / variable changed:** none formally. New conditioning variable: the sign of the 17:05 -> 07:00 NY overnight
  return (B32) or its 20-date sum (B33). Relatives: E021 (fade large daily moves from 20:00 NY), E027 (London-open sign -> pre-fix half
  hour), E028 (2-SD 17:00 -> 12:00 moves).
- **Prior expectation:** weak. A clean NONE is informative and closes the line.
- **Why dev is clean:** E009 published unconditional hour means on dev, never a sign-agreement statistic between the overnight and
  intraday windows; E021/E027/E028 used different predictors and windows. The conditional statistic has never been computed.
- **Why now:** top `ready` backlog items (B32, B33) after the R074 refill; no research-batch run queued or in progress.
