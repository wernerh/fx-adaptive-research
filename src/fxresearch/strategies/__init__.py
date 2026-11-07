"""Strategy implementations. Each module exposes `generate_signals(bars, feats, params) -> list[Signal]`.

A strategy may only read `signal_inputs(feats)` columns plus bars with ts < signal time.
Parameters live in a dataclass with defaults recorded in strategies/<name>.md.
"""
from . import asian_range_breakout, london_us_continuation

REGISTRY = {
    "asian_range_breakout": asian_range_breakout,
    "london_us_continuation": london_us_continuation,
}
