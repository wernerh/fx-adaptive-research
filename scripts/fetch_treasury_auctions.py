"""E039 phase 1 (runner only): US Treasury auction calendar for DEV dates (2015-01-01..2020-12-31) from the Fiscal Data API.

    python scripts/fetch_treasury_auctions.py [--out-dir backtests/validation_reports]

Endpoint: https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/od/auctions_query
Only dev auction dates are requested (val/OOS calendars stay unread). Each page request is tried at most twice (pre-registered stop
rule: 403/timeouts on 2 attempts -> E039 BLOCKED, 0 trials, no substitute source). Always exits 0 so the batch commits the log;
the status is in E039_auctions_fetch.json and the experiment script reads it.
Outputs: E039_auctions_raw.csv (every record returned, all fields), E039_auctions_fetch.json (status, field names, counts).
"""
import argparse
import csv
import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/od/auctions_query"
FROM, TO = "2015-01-01", "2020-12-31"
PAGE = 1000

ap = argparse.ArgumentParser()
ap.add_argument("--out-dir", default=str(ROOT / "backtests" / "validation_reports"))
args = ap.parse_args()
out = Path(args.out_dir)
out.mkdir(parents=True, exist_ok=True)
meta = {"endpoint": BASE, "from": FROM, "to": TO, "status": "started", "attempts": [], "records": 0}


def get(page: int) -> dict:
    q = {"filter": f"auction_date:gte:{FROM},auction_date:lte:{TO}", "sort": "auction_date", "page[size]": str(PAGE),
         "page[number]": str(page)}
    url = BASE + "?" + urllib.parse.urlencode(q, safe=":,()[]")
    last = None
    for attempt in (1, 2):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "fx-adaptive-research (research; GitHub Actions)"})
            with urllib.request.urlopen(req, timeout=60) as r:
                body = json.loads(r.read().decode())
            meta["attempts"].append({"page": page, "attempt": attempt, "ok": True})
            return body
        except Exception as e:  # noqa: BLE001 - any failure counts as an attempt
            last = e
            meta["attempts"].append({"page": page, "attempt": attempt, "ok": False, "error": repr(e)[:300]})
            time.sleep(5)
    raise RuntimeError(f"page {page} failed twice: {last!r}")


records = []
try:
    first = get(1)
    pages = int(first.get("meta", {}).get("total-pages", 1) or 1)
    meta["total_count"] = first.get("meta", {}).get("total-count")
    meta["field_names"] = list(first.get("meta", {}).get("labels", {}).keys()) or (list(first["data"][0]) if first.get("data") else [])
    records.extend(first.get("data", []))
    for p in range(2, pages + 1):
        records.extend(get(p).get("data", []))
    records = [r for r in records if FROM <= str(r.get("auction_date", ""))[:10] <= TO]
    meta["records"] = len(records)
    meta["status"] = "ok" if records else "empty"
    if records:
        meta["first_record"] = records[0]
except Exception as e:  # noqa: BLE001
    meta["status"] = "failed"
    meta["error"] = repr(e)[:500]

if records:
    fields = sorted({k for r in records for k in r})
    with open(out / "E039_auctions_raw.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(records)
(out / "E039_auctions_fetch.json").write_text(json.dumps(meta, indent=2, default=str))
print("E039 auction fetch:", meta["status"], "| records:", meta["records"], "| fields:", meta.get("field_names"))
