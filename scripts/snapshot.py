#!/usr/bin/env python3
"""Fetch the HTTP Archive adoption series and write data/snapshot.json.

Measure: WordPress origins as a share of all origins in the Chrome UX Report
(CrUX), mobile, all ranks, all geos. Source: https://cdn.httparchive.org/v1/adoption
Standard library only; run with `uv run scripts/snapshot.py` or plain python3.
"""
import json, sys, urllib.request, datetime, pathlib

API = "https://cdn.httparchive.org/v1/adoption?geo=ALL&rank=ALL&start=2019-01-01&end=2099-01-01&technology={}"
OUT = pathlib.Path(__file__).resolve().parent.parent / "data" / "snapshot.json"

def fetch(tech):
    with urllib.request.urlopen(API.format(tech), timeout=60) as r:
        return {row["date"]: row["adoption"] for row in json.load(r)}

def main():
    wp, al = fetch("WordPress"), fetch("ALL")
    months = []
    for d in sorted(wp):
        if d not in al or not al[d].get("mobile"):
            continue
        months.append({
            "month": d,
            "wp_mobile": wp[d]["mobile"], "all_mobile": al[d]["mobile"],
            "wp_desktop": wp[d]["desktop"], "all_desktop": al[d]["desktop"],
            "share_mobile": round(wp[d]["mobile"] / al[d]["mobile"] * 100, 2),
            "share_desktop": round(wp[d]["desktop"] / al[d]["desktop"] * 100, 2),
        })
    prev = json.loads(OUT.read_text()) if OUT.exists() else {}
    snap = {
        "fetched_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "source": "https://cdn.httparchive.org/v1/adoption (HTTP Archive Technology Report, CrUX origins)",
        "latest_month": months[-1]["month"],
        "months": months,
    }
    changed = prev.get("months") != months
    OUT.write_text(json.dumps(snap, indent=1) + "\n")
    print(("updated" if changed else "unchanged") + f": latest {months[-1]['month']} = {months[-1]['share_mobile']}% (mobile)")
    return 0 if changed else 3

if __name__ == "__main__":
    sys.exit(main())
