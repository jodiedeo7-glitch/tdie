# WYS Free Preview Guide: build report (10 October 2026)

Sources checked: CLAUDE.md; claude/WYS_REFERENCE_PACK_2026-10-07.md (full); ops/cloud-kit/TDIE_DESIGN_RULES.md; ops/canon/canon.json (claims and locked-feature rules); ops/ai-router/TDIE_CURRENT_HANDOFF_RULES_2026-10-04.md; src/pages/shop/while-you-sleep-storefront.astro (kit contents list); ops/wys-runtime/README.md and rejected-assets.json; src/lifestyle/README.md.

NOT FOUND in the repo: claude/WYS_FOUNDER_INTAKE.md, claude/WYS_LOOK_RULES.md, claude/WYS_PROMO_FACTS.md, claude/TDIE_DESIGN_RULES.md. They are claude.ai Project documents, and this cloud session cannot open the "TDIE Website" project. Intake answers relayed on 10 October 2026 are listed under "Confirmed" below.

Status: prepared file only. Nothing posted, published, scheduled or uploaded. The WYS release hold is unchanged.

## Files

- `index.html`: source, ten 1080 x 1440 pages, Newsreader SemiBold and Inter self-hosted in `type/` (OFL licences included)
- `out/WYS-Free-Preview-Guide.pdf`: 10 pages at 1080 x 1440 px, embedded fonts are only Inter and Newsreader
- `out/wys-preview-guide-p01.png` to `p10.png`: one PNG per page
- `out/wys-preview-guide-contact-sheet.png`: all pages, checked by eye
- `render.cjs`: to rebuild, run `NODE_PATH=$(npm root -g) node render.cjs . out`
- `img/`: resized copies of repo photos (originals untouched)

## Conflicts between files (one line each, with the fix)

1. The sales page (`src/pages/shop/while-you-sleep-storefront.astro`, 4 Oct) says ChatGPT plus approval of every Pin before scheduling, but the brief says Claude desktop plus automatic by default. Fix: not part of this guide. The sales page is left untouched.
2. The reference pack (section 19) says no three-pin timetable is set, but the brief says 2 looks a day = 6 Pins a day. Fix: resolved. Jodie's intake confirms 2 looks a day = 6 Pins a day.
3. The design rules call for gradient pill buttons and soft pink shadows, but the brief bans gradients and soft shadows so the file imports into Canva. Fix: none needed. The guide uses solid fills and solid offset blocks.
4. The handoff rules put Hello Kitty and Kuromi plushies in the attic loft, but the brief bans anything branded in a photo. Fix: the only loft photo used (`g2-loft-night-desk`) has no plushies.
5. The reference pack's visual direction lists black and silver. Fix: per the skill, the guide never describes her palette in words.
6. The sales-page kit list includes "A Preparation Guide and a Setup Guide" (PDFs), but the skill says buyer delivery is an interactive website, not a PDF. Fix: page 8 says "a guided setup" and names no format.

## Photos (every placed photo, path, why it passes)

Photo order is always Basic, Styled, Lifestyle. Both former "PHOTO NEEDED / Styled" slots are filled with Jodie's approved, publish-ready styled photos from `cloudflare-migration`.

| Page | Repo path (branch cloudflare-migration) | Role | Why it passes |
|---|---|---|---|
| 1 | src/lifestyle/pink-plaid-pumpkin-patch-outfit-basic.jpg | Basic, clothing | Approved set named by Jodie. Laid out on wood floorboards, not a bed. |
| 1 | src/lifestyle/pink-plaid-pumpkin-patch-outfit-styled.jpg | Styled, clothing | Approved styled photo named by Jodie. Hung by a farmhouse window, fully styled. |
| 1 | src/lifestyle/pink-plaid-pumpkin-patch-outfit-lifestyle.png | Lifestyle, clothing | Approved set. Tommy Kate, brown hair, at the pumpkin patch in the same outfit. |
| 4 | src/lifestyle/pink-ghost-coffee-bar-basic.jpg | Basic, home decor | Approved set named by Jodie. Decor pieces on a wood sideboard. |
| 4 | src/lifestyle/pink-ghost-coffee-bar-styled.jpg | Styled, home decor | Approved styled photo named by Jodie. |
| 4 | src/lifestyle/pink-ghost-coffee-bar-lifestyle.png | Lifestyle, home decor | Approved set. Tommy Kate, brown hair, in her kitchen with the same decor. |
| 2 | ops/cloud-output/storefront-product/graphics/photos/g3-kitchen-late.jpg | Scene | Unchanged from the first build. |
| 3 | ops/cloud-output/storefront-product/graphics/photos/g4-nightstand-phone.jpg | Scene | Unchanged. |
| 5, 6 | src/lifestyle/pink-halloween-porch-decor-flatlay.jpg | Basic, home decor | Unchanged. |
| 6 | ops/cloud-output/storefront-product/graphics/photos/hoodie-flatlay.jpg | Basic, clothing | Unchanged. |
| 6 | src/lifestyle/pink-halloween-trick-or-treat-porch-essentials-lifestyle.jpg | Lifestyle | Unchanged. |
| 6 | src/lifestyle/pink-cat-halloween-costume-lifestyle.jpg | Lifestyle, costume | Unchanged. |
| 7 | ops/cloud-output/storefront-product/graphics/photos/g2-loft-night-desk.jpg | Scene | Unchanged. |
| 10 | ops/cloud-output/storefront-product/graphics/photos/g1-porch-morning.jpg | Scene | Unchanged. It shows a real potted lilac on the porch; the decorative daisies were removed. |

The Legally Blonde knit set is no longer used, and its two resized copies were removed from `img/`.

UNVERIFIED: whether Jodie approved the unchanged images on pages 2, 3, 5, 6, 7 and 10 for WYS use.

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

## Confirmed from Jodie's founder intake (relayed 10 October 2026)

- Automatic by default; 2 looks a day = 6 Pins a day; Instagram carousel order lifestyle, styled, clean; each Pin links to the Amazon list its products came from. CONFIRMED.
- Tools line: kept as "Claude desktop and Chrome, Amazon Associates or Influencer, Pinterest, image tools" because those words are in the brief Jodie gave the build session (session_01L4FEsrrVUy6uBJZPpTHnrw). Her intake adds that publishing runs through Metricool and the browser is only for Amazon Idea Lists.
- "NO THINKING." credited to Jodie: kept because the brief Jodie gave says 'Pull quote in her words: "NO THINKING."'.
- Buyers get an interactive website, not a PDF guide. Page 8 names no PDF or file format.

## Lines I could not verify (UNVERIFIED)

- Page 8 kit contents come from the 4 Oct sales-page list, not a delivered kit build.
- The p10 button links to /shop/while-you-sleep-storefront. Whether that page is live is not checked.
- Page 4 Basic caption changed from "every piece, plus its text overlay" to "every piece, laid out", because the approved Basic photo has no text overlay.

## Design fixes (10 October 2026)

- Lavender is back as a signature accent (Jodie's correction, 10 October 2026; her intake lists pink, green, blue, purple/lavender, multicolor/prints). Light lavender #EAE5F8 is the background on pages 3 and 9. The panels on pages 6 and 8 and the lavender glitter frames on pages 4 and 6 use it, and the number badges on pages 2, 4, 5, 6 and 8 and the page 7 sticker use the deeper #7E66C4. No page is washed in pink and lavender together, and there are no gradients or ombre backgrounds.
- Text: headlines are near-black Newsreader SemiBold with hot pink only on the key words. Body text is near-black Inter. The page 1 tagline and the page 9 "does not promise" line are now near-black. There is no bubble or rounded cartoon lettering.
- Decorative daisies removed from page 10, replaced with a glitter "Your taste" sticker. No flowers, butterflies or bows in the design.
- The page 10 button is now white with a hot pink outline and hot pink text and arrow. There are no filled pink buttons.
- Glitter: fine multi-size flecks (white, pale pink, soft gold, a few four-point glints) built in code as hand-placed solid SVG circles. They sit only on the offset frame blocks behind each polaroid, the round stickers and the numbered badges. There is no glitter over any photo or across a page. The flecks use solid colours with no transparency, so the file still imports into Canva.
- The page 9 callout label now reads "How it runs".
- The sales page was not touched.

## QA done

The automated check covered every page: exact 1080 x 1440, no overflow, nothing outside the page, nothing over the footer, no text under 18px, no em or en dashes, no "$", "spots" or "Warmly". Headline lines fit without widow words. The remaining overlap flags come from the rotated callout boxes, and inspection showed no real text overlap. I checked the contact sheet and a 390px phone-width version by eye. Body copy is 45 words or fewer on every page except p9 (about 75), because the required lines are long.

Page headlines are 74 to 104px at 1080px wide, which is about 27 to 38px on a phone. The 52px headline cap applies to site sales pages, not to a 1080px graphic.

This matches CLAUDE.md, claude/WYS_REFERENCE_PACK_2026-10-07.md and ops/cloud-kit/TDIE_DESIGN_RULES.md, with conflicts 1 to 6 above. It could not be checked against claude/WYS_FOUNDER_INTAKE.md, WYS_LOOK_RULES.md or WYS_PROMO_FACTS.md (not reachable).

## Website-match rebuild (10 October 2026)

Jodie asked for the guide to match her website. Every page now uses the live home page's own design pieces, with values read from the site's rendered styles:
- the glitter drip strip (`public/images/drip-top.webp`, copied to `img/`), the brand band and the masthead line;
- the cream #FFFBF8 page;
- outlined pink kicker pills with a gold rule;
- Newsreader headlines in near-black with hot pink on the key words;
- glossy numbered circles with a halo;
- method-style cards with 36/12 corners that alternate pink and lavender borders;
- the rounded pink cover frame with a caption bar;
- white outline pill buttons;
- a gold rule above the footer.

Glitter stays in the photo frame borders and the number circles. Lavender is the alternate card, frame and number colour. The copy and photos are unchanged. These styles use the site's soft shadows and the gradient number circles, which goes against the original brief's no-gradient rule for Canva import.

## Built from the website itself (10 October 2026)

Jodie rejected the drip and asked for the PDF to look like her website. The guide is now rendered from the live site's own home page: its compiled stylesheets and its real components (cover, masthead, kicker pills, cover-meta stats, the "Sound familiar?" list, the "Faceless" two-part section with the refuse list, showroom cards, method staircase cards, manifesto line, e-btn). Pages are laid out at the site's 720px tablet width and exported at 1080 x 1440 (PNG) and 720 x 960 pt (PDF).

- No drip.
- Photo frames copy the site's cover frame (14px pink border, 28px corners, pink outline, white caption strip), with fine glitter in the border.
- All of the site's scripts, its Meta Pixel and analytics, and its meta tags are stripped from the guide.
- Copy and photos are unchanged. I removed three short card descriptions I had drafted that are not in the approved copy.
- To rebuild: build the site (`npx astro build` on cloudflare-migration), serve `dist/`, copy `img/*.jpg` to `dist/_wysguide-img/`, then run `python3 site-build/site_build.py dist dist/_wysguide.html site-build/glitter.txt` and `node site-build/site_render.mjs out`.
- `index.html` and `render.cjs` are the earlier standalone version, kept for reference only.

## Page-by-page visual audit (10 October 2026)

Every page was checked on its own at full size, fixed, re-rendered and checked again.

- All pages: the header and footer glitter lines were greyish and looked dirty, so they now use the hot pink glitter. Sticker words spilled past the white centre, so they were resized. The corner sparkle stars floated off the rounded corners, so they now sit on them.
- p1: "Planned. Pinned..." was a different font from page 12 (now Newsreader with "You Slept." in pink). The photo tags covered the shoes in the Basic photo (tags moved to hang below the photos). There was a large gap above the chips (photos are larger).
- p2: "The photos" and "The words" wrapped unevenly. "6 Pins a day. By / hand?" broke badly. The sticker collided with the card corner and the headline.
- p3: "Storefront™" was split from its name, "lists." sat alone on a line, and there was empty space at the bottom (larger photo).
- p4: there was a big empty gap above the disclaimer (taller photos).
- p5: the Pin 1 title band looked see-through and cheap (now a solid white band with a pink line under it). "from." sat alone on a line.
- p6: "3 slides" overflowed the sticker, there was a big empty gap above the note, and the slide cards were unevenly sized.
- p7: "jack-o-" broke across a line and item 05 was badly broken up. The browser frame was too small.
- p8: one photo card had a glitter edge and the other didn't (they now match). The sticker overlapped the header card edge.
- p9: "Then" sat alone at the end of a headline line, and "2 / looks" was split.
- p10: "01 · First" repeated the big number, the cards had big empty bottoms, and cards in the same row didn't line up.
- p11: the "Your path" card was mostly empty and "image tools." sat alone on a line (the boxes are now full width).
- p12: the sticker word overflowed, and the closing line was small and close to the footer.
