"""One-off: convert the 22 legacy look records to schema wys-founder-1.
Keeps every verified fact (slug, title, date, category, season, Idea List,
item links); replaces the copy (copy.json); renames brand-named items;
drops the one item whose link was verified to open a different product.
Image alt text is written after the founder images pass QA (alts.json)."""
import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "src" / "lifestyle"
HERE = Path(__file__).parent
copy = json.loads((HERE / "copy.json").read_text())
alts = json.loads((HERE / "alts.json").read_text()) if (HERE / "alts.json").exists() else {}
legacy = json.loads((HERE / "legacy-records.json").read_text())
THEME = {"pink-car-interior-accessories", "pink-dog-halloween-finds", "pink-dorm-halloween-decor",
         "pink-halloween-party-decor", "pink-halloween-porch-decor", "pink-halloween-trick-or-treat-porch-essentials"}
for slug, old in legacy.items():
    c = copy[slug]
    ren = {k: v for k, v in c["items"].items() if k != "drop"}
    drop = set(c["items"].get("drop", []))
    items = []
    for it in old["items"]:
        if it["name"] in drop:
            continue
        new = {"name": ren.get(it["name"], it["name"]), "link": it["link"]}
        if it.get("note"):
            new["note"] = it["note"]
        items.append(new)
    a = alts.get(slug, {})
    rec = {
        "schema": "wys-founder-1",
        "slug": slug,
        "title": old["title"],
        "date": old["date"],
        "category": old["category"],
        "season": old["season"],
        "intro": c["intro"],
        "images": [
            {"file": a.get("file1", f"{slug}-pin1.jpg"), "alt": a.get("pin1", ""), "persona": False},
            {"file": a.get("file2", f"{slug}-pin2.jpg"), "alt": a.get("pin2", ""), "persona": slug not in THEME},
        ],
        "listLink": old["ideaList"],
        "items": items,
    }
    (SRC / f"{slug}.json").write_text(json.dumps(rec, indent=2, ensure_ascii=False) + "\n")
print("wrote", len(legacy))
