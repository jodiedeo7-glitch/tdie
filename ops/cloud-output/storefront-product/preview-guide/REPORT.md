# WYS Free Preview Guide: build report, revision 2 (10 October 2026)

Sources checked: CLAUDE.md; claude/WYS_REFERENCE_PACK_2026-10-07.md; ops/cloud-kit/TDIE_DESIGN_RULES.md; ops/canon/canon.json; ops/ai-router/TDIE_CURRENT_HANDOFF_RULES_2026-10-04.md; src/lifestyle/pink-plaid-pumpkin-patch-outfit.json and src/lifestyle/pink-ghost-coffee-bar.json on origin/cloudflare-migration; Jodie's revision instructions of 10 October 2026.

Status: prepared file only. Nothing posted, published, scheduled or uploaded. The WYS release hold is unchanged. The photos were read from origin/cloudflare-migration. Nothing was committed to that branch.

## Revision 2 changes (Jodie, 10 October)

- Photos: only the six approved photos from src/lifestyle on cloudflare-migration. Every other photo and both PHOTO NEEDED boxes are removed. Order is always Basic, Styled, Lifestyle. No photo repeats within a page.
- Text overlay: only on Basic photos (a cream band with a Yellowtail script title, plus a Jost uppercase subtitle where it fits at 18px or larger). Styled and Lifestyle carry no text.
- No flowers, butterflies, bows, stripes or double outlines. The left edge stripe, the dashed sticker rings and the sparkles are gone.
- Every page background is cream #FBF8F5. Hot pink #D62E73 is used only for headline turn lines, numbers and small labels. Bubblegum #FF8AC2 appears once, on the button arrow. Text is near-black #1A1417. Frames, rules and cards use thin gold #C8A96A lines. Nothing has a shadow block, gradient or transparency. The CTA pill is near-black with cream text.
- Fonts: Gloock for headlines, Yellowtail for the pink script accent, Jost for everything else. All three come from the google/fonts GitHub repository (ofl/gloock, apache/yellowtail, ofl/jost). Licences are in `type/`. The PDF embeds only these three.
- Pace and approvals are founder-confirmed: 2 looks a day = 6 Pins a day; automatic by default with the option to approve, with approvals recommended for the first few days.

## Files

- `index.html` (source), `type/` (fonts and licences), `img/` (resized copies of the six photos)
- `out/WYS-Free-Preview-Guide.pdf`: 10 pages at 1080 x 1440 px
- `out/wys-preview-guide-p01.png` to `p10.png`
- `out/wys-preview-guide-contact-sheet.png`
- `render.cjs`: to rebuild, run `NODE_PATH=$(npm root -g) node render.cjs . out`

## Photo placement

| Page | Photos (in order) |
|---|---|
| 1 | Plaid outfit Basic, Styled, Lifestyle (fanned stack) |
| 2 | Ghost coffee bar Lifestyle |
| 3 | Plaid outfit Lifestyle |
| 4 | Plaid outfit Basic, Styled, Lifestyle |
| 5 | Ghost coffee bar Basic |
| 6 | Plaid outfit Basic, Plaid outfit Lifestyle, Coffee bar Basic, Coffee bar Lifestyle |
| 7 | Ghost coffee bar Styled |
| 10 | Ghost coffee bar Lifestyle |

Pages 8 and 9 have no photos, as before.

## Copy changes forced by the photo swap

- Page 3: the caption "Lights out. The list is not on you." is removed because it no longer matched the daytime pumpkin patch photo. The frame has no caption.
- Page 6: the old tile captions (Campus outfit, Porch decor, Treat night, Costume) are now "Outfit · Basic", "Outfit · Lifestyle", "Decor · Basic", "Decor · Lifestyle". Only two looks exist, so the grid shows two looks instead of four.
- Basic overlay titles: "Pumpkin Patch / The pink plaid outfit" and "Ghost Coffee Bar / Pink Halloween finds", taken from the two look records.

All other copy is unchanged.

## Conflicts with standing files

1. CLAUDE.md and the design rules set Newsreader and Inter as the brand fonts, and the louder pink look. Fix: this guide follows Jodie's 10 October instruction (Gloock, Yellowtail and Jost on cream). If this becomes the brand standard, update CLAUDE.md and ops/cloud-kit/TDIE_DESIGN_RULES.md.
2. The live sales page still describes ChatGPT and approval of every Pin. Fix: Codex updates it to match the founder-confirmed automatic-by-default rule.

## Still UNVERIFIED

- Page 8 kit contents. They come from the 4 Oct sales-page list, not a checked kit build.
- "Each Pin links to the Amazon list its products came from." This holds for Idea List buyers. Associates-only buyers have no Idea List.
- Whether the sales page linked from the page 10 button is live.
- The "NO THINKING." attribution.

## QA done

The automated check covered all 10 pages: exact size, no overflow, nothing outside the page, nothing over the footer, no text under 18px, no dashes, no prices or spot counts, and no repeated photo within a page. I looked at every page at full size and on the contact sheet. One defect was fixed: the "Ghost Coffee Bar" overlay script on page 5 was clipped and is now smaller.

This matches Jodie's 10 October revision instructions, claude/WYS_REFERENCE_PACK_2026-10-07.md (three roles, order, no text on Styled or Lifestyle) and the claims rules. It differs from CLAUDE.md and ops/cloud-kit/TDIE_DESIGN_RULES.md on fonts and palette, per conflict 1.
