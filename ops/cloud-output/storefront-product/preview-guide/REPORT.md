# WYS Free Preview Guide: build report (10 October 2026)

Sources checked: CLAUDE.md; claude/WYS_REFERENCE_PACK_2026-10-07.md (full); ops/cloud-kit/TDIE_DESIGN_RULES.md; ops/canon/canon.json (claims and locked-feature rules); ops/ai-router/TDIE_CURRENT_HANDOFF_RULES_2026-10-04.md; src/pages/shop/while-you-sleep-storefront.astro (kit contents list); ops/wys-runtime/README.md and rejected-assets.json; src/lifestyle/README.md.

NOT FOUND in the repo: claude/WYS_FOUNDER_INTAKE.md, claude/WYS_LOOK_RULES.md, claude/WYS_PROMO_FACTS.md, claude/TDIE_DESIGN_RULES.md. They are claude.ai Project documents, and this cloud session cannot open the "TDIE Website" project. Every line that depends on the intake is marked UNVERIFIED below.

Status: prepared file only. Nothing posted, published, scheduled or uploaded. The WYS release hold is unchanged.

## Files

- `index.html`: source, ten 1080 x 1440 pages, Newsreader SemiBold and Inter self-hosted in `type/` (OFL licences included)
- `out/WYS-Free-Preview-Guide.pdf`: 10 pages at 1080 x 1440 px, embedded fonts are only Inter and Newsreader
- `out/wys-preview-guide-p01.png` to `p10.png`: one PNG per page
- `out/wys-preview-guide-contact-sheet.png`: all pages, checked by eye
- `render.cjs`: to rebuild, run `NODE_PATH=$(npm root -g) node render.cjs . out`
- `img/`: resized copies of repo photos (originals untouched)

## Conflicts between files (one line each, with the fix)

1. The sales page (`src/pages/shop/while-you-sleep-storefront.astro`, 4 Oct) says ChatGPT plus approval of every Pin before scheduling, but the brief says Claude desktop plus automatic by default. Fix: once Jodie confirms the intake wording, Codex updates the sales page to match. The guide follows the brief.
2. The reference pack (section 19) says no three-pin timetable is set, but the brief says 2 looks a day = 6 Pins a day. Fix: save the 2-looks-a-day pace in the intake/state record. The guide uses Jodie's pace.
3. The design rules call for gradient pill buttons and soft pink shadows, but the brief bans gradients and soft shadows so the file imports into Canva. Fix: none needed. The guide uses solid fills and solid offset blocks.
4. The handoff rules put Hello Kitty and Kuromi plushies in the attic loft, but the brief bans anything branded in a photo. Fix: the only loft photo used (`g2-loft-night-desk`) has no plushies.
5. The reference pack's visual direction lists black and silver. Fix: per the skill, the guide never describes her palette in words.
6. The sales-page kit list includes "A Preparation Guide and a Setup Guide" (PDFs), but the skill says buyer delivery is an interactive website, not a PDF. Fix: page 8 says "a guided setup" and names no format.

## Photos (every placed photo, path, why it passes)

No repo look has an approved Styled photo. The three-role approved WYS sets (Pretty Wicked, Ghoul Fuel) are private, so they are not in the repo and were not used. Every Styled slot is a labelled empty frame: "PHOTO NEEDED / Styled, not on a bed" (pages 1 and 4).

| Page | Repo path | Role | Why it passes |
|---|---|---|---|
| 1, 4 | src/lifestyle/last-minute-legally-blonde-costume-flatlay.jpg | Basic | Overhead on weathered white porch boards: not a bed, no upholstery. Real-looking, nothing branded readable, with its text overlay. The guide never names Legally Blonde. |
| 1, 4 | src/lifestyle/last-minute-legally-blonde-costume-lifestyle.jpg | Lifestyle (same look) | Tommy Kate with brown hair on her porch steps, wearing the same sweater, jeans and scrunchie. Real, not staged-rich, no logos. |
| 2 | ops/cloud-output/storefront-product/graphics/photos/g3-kitchen-late.jpg | Scene | Farmhouse kitchen at night with laptop and retriever. Brown hair, real, no branding. |
| 3 | ops/cloud-output/storefront-product/graphics/photos/g4-nightstand-phone.jpg | Scene | Nightstand and bed at night with no outfit on the bed, nothing branded. Chosen instead of the sofa photo, which shows a closed laptop that could suggest it runs with the laptop closed. |
| 5, 6 | src/lifestyle/pink-halloween-porch-decor-flatlay.jpg | Basic, home decor (non-clothing) | Weathered porch boards, generic ghost and pumpkin decor, no licensed characters, real-looking. |
| 6 | ops/cloud-output/storefront-product/graphics/photos/hoodie-flatlay.jpg | Basic, clothing | Whitewashed wood floor, not a bed, no logos. |
| 6 | src/lifestyle/pink-halloween-trick-or-treat-porch-essentials-lifestyle.jpg | Lifestyle, home/holiday (non-clothing) | Brown hair, real porch, generic jack-o-lantern bucket. |
| 6 | src/lifestyle/pink-cat-halloween-costume-lifestyle.jpg | Lifestyle, costume | Brown hair, farmhouse porch and red barn, no branding. |
| 7 | ops/cloud-output/storefront-product/graphics/photos/g2-loft-night-desk.jpg | Scene | Laptop on at night, which matches "computer on when tasks run". No plushies or logos. |
| 10 | ops/cloud-output/storefront-product/graphics/photos/g1-porch-morning.jpg | Scene | Porch morning with lilacs and barn. Brown hair, real, nothing branded. |

Rejected as failing a hard rule: every flat lay on pink satin, fluffy fabric or bedding (angel, ballerina, bunny, car, cat, dog, dorm, fairy, flamingo, pageant, porch-essentials basic, sorority, witch, cowgirl). Also rejected: the cut-out collages that look fake (graduation, sequin, workwear, which also shows a branded-style ring), the sofa photo (closed laptop), and any loft image with plushies.

UNVERIFIED: whether Jodie approved these repo images for WYS use. The src/lifestyle images are legacy two-image /lifestyle data, and the graphics/photos set was made for the presale graphics. Four different looks appear across the guide, including two non-clothing ones.

## Psychology map

- Curiosity gap: p1 ("Your taste. / A repeatable system." with an empty Styled frame and "Free preview")
- Problem agitation: p2 (four jobs, "6 Pins a day. By hand?", "Passive income isn't passive")
- Reframe: p3 ("What if the treadmill ran without you?", "NO THINKING.")
- Visual proof: p4 (one look across the three roles)
- Concrete specifics: p4 (3 photos), p5 (3 Pins per look), p7 (2 looks a day = 6 Pins)
- Value stacking: p5 (Pin copy, Instagram carousel, blog post), p8 (four kit parts)
- Ownership language and future pacing: p6 ("My pink. Your recipe.", "Picture your first look")
- Ease, low effort: p7 (three steps with arrows, automatic by default)
- Honest objection handling: p9 (tools, computer on, browser step, separate costs, optional paths, no sales promise)
- Single CTA: p10 (one pill button)
- None used: fake scarcity, testimonials, prices, dates, spot counts, codes, affiliate rate or income claims.

## Lines I could not verify (UNVERIFIED)

- Every intake-based line (Claude desktop and Chrome; automatic by default; 2 looks a day; Instagram carousel order lifestyle, styled, clean; "NO THINKING."; the persona-or-flat-lays choice). The intake file was not reachable. These lines are copied from the brief, not from the intake.
- "Each Pin links to the Amazon list its products came from": per the reference pack, Associates-only buyers have no Idea List.
- Page 8 kit contents come from the 4 Oct sales-page list (setup, themed-look recipe, persona/no-persona, scheduled task prompts plus reconciliation, optional blog, Instagram add-on, Brand Closet Outfit of the Day). They are not checked against a delivered kit build. "Missed-run check" maps to the reconciliation job in reference pack sections 21 and 23.
- The p10 button links to /shop/while-you-sleep-storefront. Whether that page is live is not checked.
- The "NO THINKING." attribution ("Jodie, on why she built it") is not checked against the intake.

## QA done

The automated check covered every page: exact 1080 x 1440, no overflow, nothing outside the page, nothing over the footer, no text under 18px, no em or en dashes, no "$", "spots" or "Warmly". Headline lines fit without widow words. The remaining overlap flags come from the rotated callout boxes, and inspection showed no real text overlap. I checked the contact sheet and a 390px phone-width version by eye. Body copy is 45 words or fewer on every page except p9 (about 75), because the required lines are long.

Page headlines are 74 to 104px at 1080px wide, which is about 27 to 38px on a phone. The 52px headline cap applies to site sales pages, not to a 1080px graphic.

This matches CLAUDE.md, claude/WYS_REFERENCE_PACK_2026-10-07.md and ops/cloud-kit/TDIE_DESIGN_RULES.md, with conflicts 1 to 6 above. It could not be checked against claude/WYS_FOUNDER_INTAKE.md, WYS_LOOK_RULES.md or WYS_PROMO_FACTS.md (not reachable).
