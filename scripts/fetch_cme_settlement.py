"""E016 phase 1: fetch official CME Group pages that state the FX futures daily settlement window (runs on the GitHub
runner; this workspace's fetch access is unreliable). NO price data are used.

Sources (fxresearch.cme_settle.SOURCE_URLS, all cmegroup.com; the Confluence pages may redirect to CME's client wiki):
  - Daily Settlement Time Ranges (PDF)
  - Client Systems Wiki: Daily Settlement Time Details
  - Client Systems Wiki: Euro (product page for Euro FX futures)

Outputs (committed by the research-batch workflow for review BEFORE E016 phase 2 is queued):
  backtests/calendars/raw_html/cme_*.{pdf,html,txt}     raw responses (+ text extracted with pdftotext when available)
  backtests/calendars/cme_settlement_fetch_report.json  per-URL HTTP status, final URL, sha256, FX windows found, validity

Never exits non-zero on a fetch/parse problem, so the report is always committed. A 403 or bot-check page is recorded
as a refusal and is NOT worked around (R024 lesson).

    python scripts/fetch_cme_settlement.py
"""
import hashlib
import json
import re
import shutil
import subprocess
import urllib.error
import urllib.request

from _common import ROOT
from fxresearch.cme_settle import SOURCE_URLS, find_fx_windows, validate_settlement

UA = "fx-adaptive-research/0.1 (non-commercial research script; https://github.com/wernerh/fx-adaptive-research)"

out_dir = ROOT / "backtests" / "calendars"
raw_dir = out_dir / "raw_html"
raw_dir.mkdir(parents=True, exist_ok=True)


def get(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,application/pdf",
                                               "Accept-Language": "en-US"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, r.geturl(), r.headers.get("Content-Type", ""), r.read()
    except urllib.error.HTTPError as e:
        try:
            body = e.read()[:2000]
        except Exception:  # noqa: BLE001
            body = b""
        return e.code, url, e.headers.get("Content-Type", "") if e.headers else "", body
    except Exception as e:  # noqa: BLE001 - report every failure
        return -1, url, "", f"ERROR {type(e).__name__}: {e}".encode()


def html_to_text(raw: bytes) -> str:
    s = raw.decode("utf-8", errors="replace")
    s = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>|</(p|div|tr|li|h\d)>", "\n", s)
    s = re.sub(r"(?i)</t[dh]>", " ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"&nbsp;|&#160;", " ", s)
    return "\n".join(re.sub(r"[ \t]+", " ", ln).strip() for ln in s.splitlines() if ln.strip())


report = {"user_agent": UA, "sources": [], "note": "no price data used; review before promoting"}
all_windows = []
for i, url in enumerate(SOURCE_URLS):
    status, final_url, ctype, body = get(url)
    entry = {"url": url, "final_url": final_url, "http_status": status, "content_type": ctype,
             "bytes": len(body), "sha256": hashlib.sha256(body).hexdigest()}
    stem = f"cme_{i}_" + re.sub(r"[^A-Za-z0-9]+", "_", url.rsplit("/", 1)[-1])[:60]
    is_pdf = "pdf" in ctype.lower() or body[:4] == b"%PDF"
    raw_path = raw_dir / (stem + (".pdf" if is_pdf else ".html"))
    raw_path.write_bytes(body)
    entry["raw_file"] = str(raw_path.relative_to(ROOT))
    text = ""
    if status == 200:
        if is_pdf:
            if shutil.which("pdftotext"):
                txt_path = raw_dir / (stem + ".txt")
                subprocess.run(["pdftotext", "-layout", str(raw_path), str(txt_path)], check=False)
                text = txt_path.read_text(errors="replace") if txt_path.exists() else ""
                entry["text_file"] = str(txt_path.relative_to(ROOT))
            else:
                entry["text_note"] = "pdftotext not available on runner; review the PDF offline"
        else:
            text = html_to_text(body)
            txt_path = raw_dir / (stem + ".txt")
            txt_path.write_text(text)
            entry["text_file"] = str(txt_path.relative_to(ROOT))
    else:
        entry["error_body_head"] = body[:500].decode("utf-8", errors="replace")
    w = find_fx_windows(text)
    entry["fx_windows"] = w
    entry["refused"] = status in (401, 403, 429) or "access denied" in text.lower()[:2000]
    for x in w:
        all_windows.append({**x, "source_url": url})
    report["sources"].append(entry)
    print(f"{url}\n  status {status} final {final_url} type {ctype} bytes {len(body)} windows {len(w)}")
    for x in w:
        print("   ", x["line"])

ok, note, settle = validate_settlement(all_windows)
report.update({"valid": ok, "validation_note": note, "settle_time_ct": settle, "n_windows": len(all_windows)})
(out_dir / "cme_settlement_fetch_report.json").write_text(json.dumps(report, indent=2))
print("valid:", ok, "|", note, "| settle_time_ct:", settle)
