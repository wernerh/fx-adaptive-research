# E043 Hypothesis: post-jump reversal after 5-minute Lee-Mykland jumps, 60-minute fade (B48), dev only (pre-registered 2026-11-11 R097, before any run)

- **H1 (B48):** after a 5-minute EUR/USD jump (Lee-Mykland statistic |L| > 5.395 and |move| >= 5 pips) starting at slot t on the
  dev block, a position -sign(r_t) entered at the quote of t+10 min and exited at t+70 min earns a mean signed mid return > 1 pip
  per event (jumps partly reverse within the hour).
- **H0:** the mean signed return per event is zero.
- **Mechanism [PUB, not EUR/USD]:** Xiao, Yin & Zhao (2020, JFR): no-news jumps in US equity ETFs are followed by significant
  return reversals for at least 60 minutes; Frömmel, Han & Van Gysegem (2015, EMFT abstract): post-jump reversal patterns in
  HUF/EUR. Liquidity-provision reading: a jump overshoots on one-sided order flow and dealers are paid to absorb it. EUR/USD is our
  extension; prior weak to medium (deepest pair; B21/E026 found no 08:30 continuation).
- **Parent experiment / variable changed:** none (new family: event-time, calendar-free, all hours). Nearest relatives: E026 (B21,
  2-h continuation after large 08:30-08:45 NY moves, NONE, mean -0.42) and E028 (daily overreaction continuation, NONE).
- **Contamination note:** E026's dev result is known (faint reversal at 08:30 NY). 08:30 jumps are a subset of B48 events; the
  sign (fade) is fixed from Xiao et al., not from E026. No 5-minute jump test has been run in this repo before. Dev usable.
- **Prior expectation:** weak to medium. ~261 registered trials: a single p just under 0.05 is expected noise (lesson R092), hence
  the separate val confirmation (B49) before anything counts.
- **Why now:** top `ready` backlog item after the R096 refill; no research-batch run queued or in progress.
