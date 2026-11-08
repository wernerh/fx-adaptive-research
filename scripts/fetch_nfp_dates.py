"""Fetch and parse official US Employment Situation (NFP) release dates (runs on the GitHub runner; this workspace
cannot reach bls.gov).

Source (Bureau of Labor Statistics): https://www.bls.gov/bls/news-release/empsit.htm  (archived releases index;
each release is linked as /news.release/archives/empsit_MMDDYYYY.htm, MMDDYYYY = release date).

Outputs (committed by the research-batch workflow for review BEFORE E015 phase 2 runs):
  backtests/calendars/nfp_dates.csv           one row per release date in the requested years, with source URL and link
  backtests/calendars/nfp_fetch_report.json   per-year counts, validity, HTTP status, non-Friday releases
  backtests/calendars/raw_html/bls_empsit_archive.html   raw index page (always saved, for offline review / parser fixes)

Never exits non-zero on a fetch/parse problem, so the report is always committed; validity is in the report.

    python scripts/fetch_nfp_dates.py [--years 2015-2023]
"""
import argparse
import json
import urllib.request

import pandas as pd

from _common import ROOT
from fxresearch.nfp import INDEX_URL, non_friday, parse_archive_index, validate_year

UA = "fx-adaptive-research/0.1 (non-commercial research script; https://github.com/wernerh/fx-adaptive-research)"

ap = argparse.ArgumentParser()
ap.add_argument("--years", default="2015-2023")
args = ap.parse_args()
y0, y1 = (int(x) for x in args.years.split("-"))
years = list(range(y0, y1 + 1))

out_dir = ROOT / "backtests" / "calendars"
raw_dir = out_dir / "raw_html"
raw_dir.mkdir(parents=True, exist_ok=True)


def get(url: str) -> tuple[int, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html", "Accept-Language": "en-US"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, r.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        try:
            body = e.read().decode("utf-8", errors="replace")[:500]
        except Exception:  # noqa: BLE001
            body = ""
        return e.code, body
    except Exception as e:  # noqa: BLE001 - report every failure, never crash before writing the report
        return -1, f"ERROR {type(e).__name__}: {e}"


status, page = get(INDEX_URL)
report = {"source_url": INDEX_URL, "http_status": status, "user_agent": UA, "years": {}}
if status != 200:
    report["error_body_head"] = page[:500]
else:
    (raw_dir / "bls_empsit_archive.html").write_text(page)

releases = parse_archive_index(page) if status == 200 else []
report["n_links_parsed_all_years"] = len(releases)
rows = []
for y in years:
    ok, note = validate_year(releases, y) if releases else (False, f"index status {status}, 0 releases parsed")
    ry = [r for r in releases if r.release_date.year == y]
    report["years"][y] = {"valid": ok, "note": note, "n": len(ry), "non_friday": non_friday(ry)}
    for r in ry:
        rows.append({"year": y, "release_date": r.release_date.isoformat(), "release_time_ny": "08:30",
                     "weekday": r.release_date.strftime("%a"), "archive_link": r.link, "source_url": INDEX_URL})

df = pd.DataFrame(rows, columns=["year", "release_date", "release_time_ny", "weekday", "archive_link", "source_url"])
df.to_csv(out_dir / "nfp_dates.csv", index=False)
report["all_years_valid"] = bool(years) and all(v["valid"] for v in report["years"].values())
report["n_rows"] = int(len(df))
(out_dir / "nfp_fetch_report.json").write_text(json.dumps(report, indent=2, default=str))

print("HTTP status:", status)
for y, v in report["years"].items():
    print(y, "VALID" if v["valid"] else "INVALID", v["note"], "non-Friday:", v["non_friday"] or "none")
print("all_years_valid:", report["all_years_valid"], "rows:", report["n_rows"])
print(df.to_string(index=False))
