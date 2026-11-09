"""Builds public/finds/finds.json for Tommy Kate's Finds of the Week
(https://tommy-kate-finds.vercel.app).

Every published look in src/lifestyle dated within the last 7 days (Eastern
time) is listed, newest first. The store comes from the look's product links:
walmart.com -> walmart, samsclub.com -> samsclub, anything else -> amazon.
Run by .github/workflows/build-finds.yml whenever a look is added or changed,
and once a day so old looks drop off.
"""
import glob
import json
import os
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DAYS = 7


def store_of(look):
    links = " ".join(i.get("link", "") for i in look.get("items", []) if isinstance(i, dict)).lower()
    if "samsclub.com" in links:
        return "samsclub"
    if "walmart.com" in links:
        return "walmart"
    return "amazon"


def main():
    today = datetime.now(ZoneInfo("America/New_York")).date()
    oldest = today - timedelta(days=DAYS - 1)
    looks = []
    for path in glob.glob(os.path.join(ROOT, "src", "lifestyle", "*.json")):
        try:
            look = json.load(open(path, encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if look.get("status") != "published" or not look.get("slug"):
            continue
        try:
            added = datetime.strptime(str(look.get("date", ""))[:10], "%Y-%m-%d").date()
        except ValueError:
            continue
        if not (oldest <= added <= today):
            continue
        if not any(isinstance(i, dict) and str(i.get("link", "")).startswith("https://") for i in look.get("items", [])):
            continue
        looks.append({"slug": look["slug"], "store": store_of(look), "added": added.isoformat()})
    looks.sort(key=lambda x: (x["added"], x["slug"]), reverse=True)
    out = {
        "about": "Tommy Kate's Finds of the Week. Built automatically from the published looks in src/lifestyle "
                 "by ops/scripts/build_finds.py; do not edit by hand. Looks older than 7 days drop off.",
        "updated": today.isoformat(),
        "looks": looks,
    }
    dest = os.path.join(ROOT, "public", "finds", "finds.json")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
        f.write("\n")
    print(f"{len(looks)} looks from {oldest} to {today}")


if __name__ == "__main__":
    main()
