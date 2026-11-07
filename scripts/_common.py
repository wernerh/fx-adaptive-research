"""Shared helpers for CLI scripts."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from fxresearch.data import load_bid_ask_csv, load_parquet, synthetic_bars  # noqa: E402

PROCESSED = ROOT / "data" / "processed" / "eurusd_m1.parquet"


def load_bars(synthetic: bool = False):
    if synthetic:
        return synthetic_bars()
    if PROCESSED.exists():
        return load_parquet(PROCESSED)
    raise SystemExit(
        f"No data at {PROCESSED}. Run scripts/ingest_dukascopy.py first, or pass --synthetic."
    )


def dump(obj, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, default=str))
