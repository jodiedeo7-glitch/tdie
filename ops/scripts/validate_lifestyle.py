#!/usr/bin/env python3
"""Validate the /lifestyle founder storefront records (schema wys-founder-1).

Run before every commit that touches src/lifestyle/ (the founder pin factory
runs it as recipe section 8c step 2):

    python3 ops/scripts/validate_lifestyle.py            # whole folder
    python3 ops/scripts/validate_lifestyle.py a.json b.json   # just these

Exit code 0 = every record passes. Anything else prints one line per problem
and exits 1, and nothing may be uploaded. Rules mirror src/data/lifestyle.js.
Legacy files (the retired 24 Sep to 3 Oct layout: "ideaList", -flatlay /
-lifestyle images, no schema) always fail, so the old presentation can never
be written back.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIR = ROOT / "src" / "lifestyle"
SCHEMA = "wys-founder-1"
CATS = {"clothing", "accessories", "jewelry", "beauty", "perfume", "home-decor", "dorm", "car", "books", "gifts"}
AMAZON = re.compile(r"^https://(link\.amazon/|amzn\.to/|www\.amazon\.com/)")
LIST = re.compile(r"^https://www\.amazon\.com/shop/thedigitalincomeedit/list/[A-Z0-9]+$")
SLUG = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
IMG_EXT = (".jpg", ".jpeg", ".png", ".webp")


def problems(path: Path, data) -> list:
    p = []
    if not isinstance(data, dict):
        return ["not a JSON object"]
    if data.get("schema") != SCHEMA:
        p.append(f'schema must be "{SCHEMA}"')
    if "ideaList" in data:
        p.append('legacy field "ideaList" (use "listLink")')
    slug = data.get("slug", "")
    if not SLUG.match(slug):
        p.append("slug must be lowercase words joined by hyphens")
    if len(slug) > 60:
        p.append("slug longer than 60 characters")
    if slug in CATS:
        p.append("slug equals a category name")
    if path.stem != slug:
        p.append(f"file name must be {slug}.json")
    if not data.get("title"):
        p.append("title missing")
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", data.get("date", "")):
        p.append("date must be YYYY-MM-DD")
    if data.get("category") not in CATS:
        p.append(f'category "{data.get("category")}" is not one of the ten')
    if not data.get("season"):
        p.append("season missing")
    intro = data.get("intro", "")
    if not intro:
        p.append("intro missing")
    words = len(intro.split())
    if intro and not 60 <= words <= 160:
        p.append(f"intro is {words} words (80 to 150 expected)")
    if re.search(r"\$\s?\d", intro):
        p.append("intro contains a price")
    for field in ("title", "intro"):
        if "—" in data.get(field, ""):
            p.append(f"{field} contains an em dash")
    imgs = data.get("images") or []
    if len(imgs) != 2:
        p.append("exactly two images (pin1, pin2) required")
    for i, im in enumerate(imgs, 1):
        f = im.get("file", "")
        if Path(f).stem != f"{slug}-pin{i}" or not f.lower().endswith(IMG_EXT):
            p.append(f"image {i} must be {slug}-pin{i}.jpg (or .png/.webp)")
        elif not (path.parent / f).exists():
            p.append(f"image file {f} is not in src/lifestyle/")
        if not im.get("alt"):
            p.append(f"image {i} alt text missing")
        if "persona" in im and not isinstance(im["persona"], bool):
            p.append(f"image {i} persona must be true or false")
    ll = data.get("listLink", "")
    if ll and not LIST.match(ll):
        p.append("listLink is not an Idea List on the thedigitalincomeedit storefront")
    items = data.get("items") or []
    if not items:
        p.append("no items")
    for i, it in enumerate(items, 1):
        if not it.get("name"):
            p.append(f"item {i} name missing")
        if not AMAZON.match(it.get("link", "")):
            p.append(f"item {i} link is not an Amazon affiliate link")
        if re.search(r"\$\s?\d", it.get("name", "") + it.get("note", "")):
            p.append(f"item {i} contains a price")
    allowed = {"schema", "slug", "title", "date", "category", "season", "intro", "images", "listLink", "items"}
    extra = set(data) - allowed
    if extra:
        p.append("unknown fields: " + ", ".join(sorted(extra)))
    return p


def main(argv) -> int:
    files = [Path(a) for a in argv] if argv else sorted(DIR.glob("*.json"))
    bad = 0
    slugs = {}
    for f in files:
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:  # noqa: BLE001
            print(f"{f.name}: does not parse ({e})")
            bad += 1
            continue
        for msg in problems(f, data):
            print(f"{f.name}: {msg}")
            bad += 1
        s = data.get("slug") if isinstance(data, dict) else None
        if s in slugs:
            print(f"{f.name}: slug also used by {slugs[s]}")
            bad += 1
        slugs[s] = f.name
    if not argv:
        legacy = [p.name for p in DIR.iterdir() if re.search(r"-(flatlay|lifestyle)\.(jpe?g|png|webp)$", p.name)]
        for name in legacy:
            print(f"{name}: legacy image name (retired layout); remove it")
            bad += 1
        jsons = {p.stem for p in DIR.glob("*.json")}
        for p in DIR.iterdir():
            m = re.match(r"^(.*)-pin[12]\.(jpe?g|png|webp)$", p.name)
            if m and m.group(1) not in jsons:
                print(f"{p.name}: image with no matching look JSON")
                bad += 1
    print("OK: every lifestyle record passes" if not bad else f"FAILED: {bad} problem(s)")
    return 0 if not bad else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
