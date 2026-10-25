#!/usr/bin/env python3
"""Check a WYS Basic prompt against every standing rule in claude/WYS_BASIC_PROMPT_CHECKLIST.md.
Usage: python3 check_basic_prompt.py prompt.txt [more.txt ...]
A prompt passes only when every check passes. When Jodie adds or changes a rule,
add or change its line here and in the checklist; never delete another rule to make room."""
import re, sys
EXACT = "EXACT PRODUCTS: every product looks EXACTLY like its photo on the attached product sheet: the same shape, colour, pattern, material, proportions, hardware, logos, tags and details. Never redesign, simplify, recolour or swap any product for a similar one."
REF = "Use the product sheet to identify each product's shape, colour, pattern and material. Render the products as real three-dimensional objects photographed together in the new scene. Never reproduce the sheet's layout, white backgrounds, cutout edges or rectangular product photographs."
BAS = "Show only the listed products and their included accessories on the specified surface. Frame the shot so no additional background décor is visible. Keep every product fully inside the frame with breathing room around the outer edges. The surface should fill the background. Preserve the specified headline and lettering treatment."
CHECKS = [
 ("17 Oct: opens with 'Highest quality finished photograph'", lambda t: t.startswith("Highest quality finished photograph")),
 ("2:3 vertical", lambda t: "vertical 2:3" in t),
 ("25 Oct: photorealistic, never cutouts or stickers", lambda t: "photorealistic" in t and "never cutouts" in t),
 ("25 Oct: camera about 60 degrees down, surface fills frame, no wall", lambda t: "60 degrees" in t and "fills the frame" in t and "no wall" in t),
 ("25 Oct 12:37 pm: EXACT PRODUCTS block word for word", lambda t: EXACT in t),
 ("17 Oct: reference-handling block word for word", lambda t: REF in t),
 ("17 Oct: Basic block word for word (with headline line)", lambda t: BAS in t),
 ("17 Oct: 'Only these N product types appear, in the quantities specified below.'", lambda t: re.search(r"Only these \d+ product types appear, in the quantities specified below", t)),
 ("25 Oct: close together, never in rows", lambda t: "never in rows" in t),
 ("25 Oct: headline on two centred lines", lambda t: "two centred lines" in t),
 ("10 Oct + 25 Oct: laid over the photo where the products meet", lambda t: "laid over the photo where the products meet" in t),
 ("25 Oct: each line 85% of the image width", lambda t: "85% of the image width" in t),
 ("25 Oct: bold brush script, thick strokes", lambda t: "Bold brush script with thick strokes" in t),
 ("10 Oct: never thin, never block capitals", lambda t: "never thin or block capitals" in t),
 ("10 Oct: no outline", lambda t: "no outline" in t),
 ("26 Sep: no box/band behind the words", lambda t: "no box" in t or "or box" in t),
 ("25 Oct 1:36 pm: soft white glow", lambda t: "soft white glow" in t),
 ("10 Oct + 25 Oct 1:42 pm: colour named for this photo and what it stands out against", lambda t: re.search(r"letters with a soft white glow behind them, so they stand out against \S", t)),
 ("26 Sep + 25 Oct: every product near the words stays sharp", lambda t: "every product under or near it stays sharp and recognisable" in t),
 ("16 Oct: SCALE line, nothing enlarged", lambda t: "SCALE, nothing enlarged:" in t),
 ("9 Oct: only the headline and printed product words; no price, people or extras", lambda t: "The only words are the headline and what is printed on the products" in t and "No price, people or extras" in t),
 ("9 Oct: no bed lays or upholstery as the surface", lambda t: not re.search(r"\b(bed|duvet|bedspread|upholster)", t.split("Only these")[0], re.I)),
 ("14 Oct: 2,500 characters or fewer", lambda t: len(t) <= 2500),
]
ok_all = True
for path in sys.argv[1:]:
    t = open(path, encoding="utf-8").read().strip()
    fails = [name for name, fn in CHECKS if not fn(t)]
    print(f"{path}: {len(t)} characters, {'PASS' if not fails else 'FAIL'}")
    for f in fails: print("   missing:", f)
    ok_all &= not fails
sys.exit(0 if ok_all else 1)
