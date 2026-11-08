"""Fetch and parse official FOMC meeting dates (runs on the GitHub runner; this workspace cannot reach federalreserve.gov).

Sources (Federal Reserve Board):
  https://www.federalreserve.gov/monetarypolicy/fomchistoricalYYYY.htm   (per-year historical pages)
  https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm        (recent five years)

Per year, the historical page is used if it parses to exactly 8 scheduled meetings; else the calendars page.
Outputs (committed by the research-batch workflow for review BEFORE E013 runs):
  backtests/calendars/fomc_dates.csv          one row per parsed meeting (scheduled and unscheduled) with source URL
  backtests/calendars/fomc_fetch_report.json  per-year counts, validity, HTTP status, parse notes
  backtests/calendars/raw_html/*.html         raw page for any page/year that failed validation (for offline fixing)

Never exits non-zero on a parse problem, so the report is always committed; validity is in the report.

    python scripts/fetch_fomc_dates.py [--years 2015-2023]
"""
import argparse
import json
import urllib.request

import pandas as pd

from _common import ROOT
from fxresearch.fomc import parse_calendars_page, parse_historical_page, validate_year

BASE = "https://www.federalreserve.gov/monetarypolicy/"
UA = "Mozilla/5.0 (compatible; fx-adaptive-research/0.1; research script)"

ap = argparse.ArgumentParser()
ap.add_argument("--years", default="2015-2023")
args = ap.parse_args()
y0, y1 = (int(x) for x in args.years.split("-"))
years = list(range(y0, y1 + 1))

out_dir = ROOT / "backtests" / "calendars"
raw_dir = out_dir / "raw_html"
out_dir.mkdir(parents=True, exist_ok=True)


def get(url: str) -> tuple[int, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, r.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception as e:  # noqa: BLE001 - report every failure, never crash before writing the report
        return -1, f"ERROR {type(e).__name__}: {e}"


report = {"years": {}, "pages": {}}
rows = []

cal_url = BASE + "fomccalendars.htm"
cal_status, cal_html = get(cal_url)
report["pages"][cal_url] = cal_status if cal_status != -1 else cal_html[:300]
cal = parse_calendars_page(cal_html) if cal_status == 200 else {}

for y in years:
    url = BASE + f"fomchistorical{y}.htm"
    status, page = get(url)
    report["pages"][url] = status if status != -1 else page[:300]
    hist = parse_historical_page(page, y) if status == 200 else []
    ok_h, note_h = validate_year(hist) if hist else (False, f"historical page status {status}, 0 meetings parsed")
    chosen, src, note = None, None, None
    if ok_h:
        chosen, src, note = hist, url, note_h
    elif y in cal:
        ok_c, note_c = validate_year(cal[y])
        if ok_c:
            chosen, src, note = cal[y], cal_url, f"calendars page ok (historical: {note_h})"
        else:
            note = f"historical: {note_h}; calendars: {note_c}"
    else:
        note = f"historical: {note_h}; calendars: year not found"
    if chosen is None and status == 200:
        raw_dir.mkdir(parents=True, exist_ok=True)
        (raw_dir / f"fomchistorical{y}.html").write_text(page)
    report["years"][y] = {
        "valid": chosen is not None,
        "source": src,
        "note": note,
        "historical_parsed": [m.label for m in hist],
        "calendars_parsed": [m.label for m in cal.get(y, [])],
    }
    for m in chosen or []:
        rows.append({"year": y, "meeting_start": m.start.isoformat(), "statement_date": m.statement_date.isoformat(),
                     "scheduled": m.scheduled, "source_label": m.label, "source_url": src})

if cal_status == 200 and not all(v["valid"] for v in report["years"].values()):
    raw_dir.mkdir(parents=True, exist_ok=True)
    (raw_dir / "fomccalendars.html").write_text(cal_html)

df = pd.DataFrame(rows, columns=["year", "meeting_start", "statement_date", "scheduled", "source_label", "source_url"])
df.to_csv(out_dir / "fomc_dates.csv", index=False)
report["all_years_valid"] = all(v["valid"] for v in report["years"].values())
report["n_scheduled"] = int(df["scheduled"].sum()) if len(df) else 0
(out_dir / "fomc_fetch_report.json").write_text(json.dumps(report, indent=2, default=str))

for y, v in report["years"].items():
    print(y, "VALID" if v["valid"] else "INVALID", v["note"])
print("all_years_valid:", report["all_years_valid"], "scheduled rows:", report["n_scheduled"])
print(df.to_string(index=False))
