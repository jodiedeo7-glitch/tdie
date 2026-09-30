#!/usr/bin/env python3
"""Run canon.json `checks` (fail and review) over every file this job wrote.

Usage from the repo root:
    python3 ops/cloud-output/storefront-product/run_checks.py [extra files...]

Patterns are applied case-sensitively, exactly as canon writes them (canon lists
case variants separately, e.g. "Free Tier" and "free tier"). A `proximity_to`
check only fires when one of its trigger words sits within `window` characters.
Also flags em dashes, which are banned brand-wide.
"""
import json, re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[3]
HERE = pathlib.Path(__file__).resolve().parent
canon = json.loads((ROOT / "ops/canon/canon.json").read_text(encoding="utf-8"))
checks = canon["checks"]

files = [p for p in HERE.rglob("*") if p.is_file() and p.suffix in {".txt", ".md", ".html", ".astro", ".mjs", ".json"}
         and "fonts" not in p.parts and "thumbnails" not in p.parts and p.name != "run_checks.py"]
files += [pathlib.Path(a).resolve() for a in sys.argv[1:]]

def hits(text, chk):
    out = []
    for pat in chk["patterns"]:
        for m in re.finditer(pat, text):
            if "proximity_to" in chk:
                w = chk.get("window", 200)
                ctx = text[max(0, m.start() - w): m.end() + w]
                if not any(t in ctx for t in chk["proximity_to"]):
                    continue
            line = text.count("\n", 0, m.start()) + 1
            out.append((line, m.group(0)))
    return out

total = 0
for f in sorted(files):
    t = f.read_text(encoding="utf-8", errors="ignore")
    rel = f.relative_to(ROOT) if f.is_relative_to(ROOT) else f
    for level in ("fail", "review"):
        for chk in checks[level]:
            for line, s in hits(t, chk):
                total += 1
                print(f"{level.upper():6} {chk['id']:28} {rel}:{line}  {s!r}")
    for m in re.finditer("—", t):
        total += 1
        print(f"FAIL   em_dash                      {rel}:{t.count(chr(10), 0, m.start()) + 1}")
print(f"\n{total} hit(s) across {len(files)} file(s).")
