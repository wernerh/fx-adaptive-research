# E036 Hypothesis: smoothed overnight -> intraday reversal in EUR/USD, VAL confirmation of E035/B33 (pre-registered 2026-11-10 R077, before any run)

- **H1 (B34):** on every valid val trading date D (2021-01-21..2023-06-30), a position -sign(O20(D)) held from 07:00 to 16:55
  America/New_York on D earns a mean signed mid return > 1 pip per date. O20(D) = sum of r_on over the 20 previous val dates with a
  valid r_on (D's own excluded); r_on(D) = mid 07:00 NY on D - mid 17:05 NY on the evening that opens D.
- **H0:** the mean signed return per date is zero.
- **Parent experiment:** E035 (B33 arm), dev SIGNAL: n 1536, mean +2.695 pips, block-20 CI (0.47, 5.027), one-sided t p 0.0093,
  SPEC 4 net +2.047, x1.5 +1.723 (backtests/validation_reports/E035_results.json, run 42865880407). **Variable changed (one):** block
  (dev -> val). The B32 daily arm was NONE on dev and is not re-tested (reported on val as a descriptive only, not a trial).
- **Mechanism [PUB, partly]:** as E035 (Krohn-Mueller-Whelan overnight vs intraday Fama slopes; Lou-Polk-Skouras smoothed overnight ->
  intraday reversal in equities). FX daily analogue, not a replication.
- **Prior expectation (written before data):** low-to-moderate. The dev effect was concentrated early (2015 +8.9 pips; 2019 +0.7,
  2020 +0.6), the |O20| terciles were non-monotone (low +2.6, mid +1.2, high +4.3), and the daily B32 arm showed nothing, so a
  decaying or chance result is plausible. ~600 val dates x SD ~40 pips -> SE ~1.6-2 pips: a val mean near +1 pip (the 2019-2020 level)
  would give NONE; the dev level (+2.7) would be borderline. The rule is not loosened for this.
- **Why val is clean for this statistic:** no earlier experiment computed an overnight-sign-conditional intraday return on val.
  E017 used unconditional 03:00-08:00 and 12:00-17:00 NY legs; E001/E006 08:00-12:00 NY; E025 a vol-state 11:05-16:00 NY trade;
  E029 a next-morning fade from 17:05 NY on overreaction days; E032 20:55 -> 02:00 NY. None used O20 or the 07:00 -> 16:55 hold
  conditioned on overnight returns.
- **Why now:** top `ready` backlog item (B34, earned R076, fixed in the E035 methodology before data).
