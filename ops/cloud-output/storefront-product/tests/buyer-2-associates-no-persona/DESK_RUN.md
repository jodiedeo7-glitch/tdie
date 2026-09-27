# Desk run: weekly themed-look build, one look, end to end

Role: the scheduled task "While-You-Sleep: weekly themed looks", first run.
Run time: Saturday 3 October 2026, 1:05 pm US Eastern (EDT).
Path: Associates-only, Squarespace (manual paste), no persona, not a Brand Closet(TM) member, pace 3.
No browser was used. Everything marked SIMULATED would come from Amazon, Higgsfield or Pinterest in a live run.
Tester notes in [square brackets] mark each point where the kit forced a guess. They are carried into FINDINGS.md.

---

## 0. Read first and lock

1. Read MY_RECIPE.txt, 03_THEMED_LOOK_RECIPE.txt, 07_PERSONA_PATHS.txt, 08_STOREFRONT_PATHS.txt, storefront-log.md, pin-tab.md, browser-lock.txt. All present. BLOG HALF is off, so 09 is not read.
   [08 line 29 says the task "writes each page into your folder as a file", but there is no spec for that file anywhere: no format, no file name, no URL slug, no images. 09 has the only page spec, and the task is told not to read 09 when BLOG HALF is off. I used 09's page layout as the closest thing.]
2. browser-lock.txt says `free`. Write `busy While-You-Sleep: weekly themed looks 1:05 pm`.
   [R16 time has no date. A lock left from last Saturday at "1:05 pm" reads as fresh today.]
3. R11 board check (SIMULATED): Coastal Grandmother Decor: Public. Linen Outfits Over 40: Public.
4. Leftovers: storefront-log.md is empty. Nothing to schedule first.

## 1. Pick the looks (Part 2)

Task prompt says: "Build the next 7 days of looks at my pace, starting from the first day with no pin 1 scheduled."
- Literal reading: today, Saturday 3 Oct, has no pin 1, so the first look is today at the 1:30 pm slot, 25 minutes after the run starts. Three looks of sourcing, links, four image generations, copy and a Squarespace page each take far longer than 25 minutes, and on this path the page must be live first. Not possible.
- Also, at pace 3 there will always be days with no pin 1, so next Saturday's literal "first day with no pin 1" is a day in the past.
- Decision: use the look days in MY_RECIPE.txt (Mon, Wed, Fri) starting after Dana's Sunday paste. [Those look days were invented by the setup chat. The kit has no rule for spreading 3 or 5 looks across 7 days.]

Window for the look dates (5 to 9 Oct 2026): WINDOW 1, Coastal Harvest. Evergreen rule: at least one evergreen look. Mix: mostly home, 1 outfit. No two clothing looks back to back.

| look date (pin 1) | look | source | kind | board |
|---|---|---|---|---|
| Mon 5 Oct | Coastal fall entryway | Window 1, idea 1 | theme list | Coastal Grandmother Decor |
| Wed 7 Oct | Oatmeal linen wide-leg pants with a cream fisherman sweater | Window 1, idea 7 | outfit | Linen Outfits Over 40 |
| Fri 9 Oct | Blue and white kitchen open shelving refresh | Evergreen line 1, idea 1 | theme list | Coastal Grandmother Decor |

This desk run builds look 1 in full: **Coastal Fall Entryway**. It is home decor, which is most of Dana's content, so it tests the image prompts on the thing she'll use most.

## 2. Source on Amazon (Part 3)

Rules applied: in stock, 4.0 stars or better, 100+ ratings, Prime where possible, in the look's colors, no character, film, toy or designer brand in the listing name. Piece names are descriptive, never brand. All ASINs and links below are SIMULATED.

| # | piece (short name, as it appears on the page) | colors | ASIN | SiteStripe short link |
|---|---|---|---|---|
| 1 | Large blue and white ginger jar vase with lid | cobalt blue floral on bright white porcelain | B0SIMUL001 (simulated) | https://amzn.to/SIMUL01 (simulated) |
| 2 | Set of 3 matte white ceramic pumpkins | chalk white, pale wood-look stems | B0SIMUL002 (simulated) | https://amzn.to/SIMUL02 (simulated) |
| 3 | Seagrass storage basket with handles | honey natural weave | B0SIMUL003 (simulated) | https://amzn.to/SIMUL03 (simulated) |
| 4 | Round rattan wall mirror, 24 inch | natural rattan | B0SIMUL004 (simulated) | https://amzn.to/SIMUL04 (simulated) |
| 5 | Faux eucalyptus and dried-look hydrangea stems | dusty sage green, cream, faded dusty blue | B0SIMUL005 (simulated) | https://amzn.to/SIMUL05 (simulated) |
| 6 | Cream cable knit throw blanket | warm cream | B0SIMUL006 (simulated) | https://amzn.to/SIMUL06 (simulated) |
| 7 | Blue and cream striped cotton runner rug, 2 by 6 feet | denim blue and oatmeal stripe | B0SIMUL007 (simulated) | https://amzn.to/SIMUL07 (simulated) |

Step 5, the pin link, ASSOCIATES-ONLY PATH: "follow 08_STOREFRONT_PATHS.txt, Associates-only section." 08 says the page lives on Dana's site and she pastes it in. The pin link is therefore the page's future address, which has to be decided now so the pins can carry it. [No URL pattern exists in the kit. I chose a Squarespace blog collection called Shop the Look, one post per look, because regular Squarespace pages don't nest under a parent path the way blog posts do. Verify in Squarespace before shipping this advice.]

**Link for both pins:** `https://danashoreandhome.com/shop-the-look/coastal-fall-entryway-decor`

Step 6, product sheet: one screenshot of the 7 main product images in a grid on an amazon.com tab. Reference only, never posted.

## 3. Make the images (Part 4, no-persona path)

Pin 1 is Format A (first look of the run). Pin 2 is Format B on a different background with a different title.

### Pin 1 prompt, Format A, sent to Seedream 4.5 on Higgsfield, portrait 2:3, product sheet attached

[The Format A template says "flat lay photo of the outfit" and "The outfit is laid out as if worn". "Keep every other word" would send a home decor sheet to Seedream with instructions to lay it out "as if worn". I changed exactly three phrases, marked in the list below the prompt. A literal task would either send the outfit wording (wrong image) or improvise differently every week.]

```
Please make me a very realistic overhead flat lay photo of the home decor pieces in the attached image. I can't use the exact Amazon images outside of Amazon, so this needs to be a new photo. Shot straight down, portrait 2:3, like a good-quality photo taken on a phone. The pieces are styled together as a real entryway vignette seen from above, overlapping and touching, on warm whitewashed wood floorboards: a large ginger jar vase with a lid, painted in a cobalt blue floral pattern on bright white porcelain, never navy; three matte chalk white ceramic pumpkins in small, medium and large, with pale wood-look stems; a honey natural seagrass basket with two handles; a round mirror with a natural rattan frame, lying flat and catching soft light; a loose bundle of faux eucalyptus in dusty sage green with dried-look hydrangea heads in warm cream and faded dusty blue; a chunky warm cream cable knit throw, softly folded and draped into the basket; a flat-woven runner in denim blue and oatmeal stripes, partly unrolled under the other pieces. Each piece matches its screenshot in color, shape and detail. Tucked in around the pieces, filling the frame edge to edge with almost no empty background: a few small white scallop shells, a brass taper candlestick with an unlit ivory candle, a folded blue and white striped linen napkin, two linen-bound books with blank spines, a sprig of dried wheat, a pair of tortoiseshell reading glasses. Every product sits fully inside the frame. Soft natural window light, gentle real shadows, visible fabric texture, small real-life imperfections, photorealistic. Across the upper third, set directly on the photo, a large two-style title: "COASTAL FALL" in a bold high-contrast serif in capitals, with "entryway" beneath it in a thick flowing brush script, both in near-black, perfectly spelled, sharp edges, filling about two thirds of the width. No logos, no brand names, no labels on products, no watermark, no person, no other text.
```

Changes from the template (3): "of the outfit" became "of the home decor pieces"; "The outfit is laid out as if worn, pieces overlapping and touching" became "The pieces are styled together as a real entryway vignette seen from above, overlapping and touching"; "around the outfit" became "around the pieces".
Image title: COASTAL FALL / entryway (3 words, inside the 3 to 5 rule).
Honest expectation: a 24 inch mirror, a 6 foot runner and a large vase in one overhead frame will not be to scale. Seedream will shrink the mirror and runner. That is acceptable for a styled flat lay but worth knowing.

### Pin 2 prompt, Format B, sent to Seedream 4.5 on Higgsfield, portrait 2:3, same product sheet attached

[Kept word for word as the template requires, including "that girl", "small hearts, little sparkles and one small bow". Those accents are wrong for a coastal grandmother home look. See FINDINGS.md. The background color is the one bracket that allowed a theme choice.]

```
Please make me a "that girl" shoppable Amazon finds collage for Pinterest, portrait 2:3, on a soft sea-glass blue, never bright turquoise, background with a faint paper texture. I can't use the exact Amazon images outside of Amazon, so please create a new clean cut-out product photo of each item in the attached image, each with a soft drop shadow: a large ginger jar vase with a lid in cobalt blue floral on bright white porcelain; three matte chalk white ceramic pumpkins with pale wood-look stems; a honey natural seagrass basket with two handles; a round mirror with a natural rattan frame; a bundle of faux eucalyptus in dusty sage green with dried-look hydrangea heads in warm cream and faded dusty blue; a folded warm cream cable knit throw; a rolled flat-woven runner in denim blue and oatmeal stripes. Add a small bundle of dried wheat, a ribbed ivory pillar candle, two white scallop shells and a folded blue and white striped linen napkin. Pack them around a central title so the whole canvas is full edge to edge, items overlapping slightly, every product fully inside the frame. Add a few tiny accents: small hearts, little sparkles and one small bow. In the middle, set directly on the background, a large two-style title: "SEASIDE AUTUMN" in a bold high-contrast serif with "at home" in a thick flowing brush script, near-black, perfectly spelled, crisp and fully legible, filling about half the width. Each item matches its screenshot and looks like a real photo, not a render. No logos, no brand names, no labels, no prices, no other text.
```

Image title: SEASIDE AUTUMN / at home (4 words). Different surface, background and title from pin 1, as 07 requires.

Letter check at phone size: required before shipping both (Part 4). Cannot be done on the desk.

## 4. Pin copy (Part 5)

Counts are exact character counts including spaces, measured with a script.

### Pin 1

- **Board:** Coastal Grandmother Decor
- **Title (91 chars):** Coastal Grandmother Fall Entryway Decor: Blue and White, Ceramic Pumpkins and Woven Texture
- **Description (494 chars, including disclosure):**

  Coastal grandmother fall entryway decor that feels calm, collected and a little seaside. This look pairs a blue and white ginger jar vase, three matte white ceramic pumpkins, a seagrass basket, a rattan mirror, faux eucalyptus with dried-look hydrangeas, a cream cable knit throw and a blue striped runner. Autumn, but make it breezy. Every piece is linked in my shop page. #coastalgrandmother #falldecor #entrywaydecor #coastaldecor #ad As an Amazon Associate I earn from qualifying purchases.

- **Alt text (198 chars):** Overhead photo of a fall entryway flat lay on whitewashed floorboards: blue and white ginger jar, white ceramic pumpkins, seagrass basket, rattan mirror and knit throw, titled Coastal Fall entryway.
- **Link:** https://danashoreandhome.com/shop-the-look/coastal-fall-entryway-decor
- **AI label:** on (R13), if the pin builder offers it.

### Pin 2

- **Board:** Coastal Grandmother Decor
- **Title (76 chars):** Coastal Fall Home Decor Ideas: A Calm Sea Blue and Cream Entryway for Autumn
- **Description (491 chars, including disclosure):**

  Coastal fall home decor ideas for anyone who wants autumn without all the orange. Sea blue and cream do the work here: a blue and white ginger jar, white ceramic pumpkins, a seagrass basket, a rattan mirror, a cable knit throw, eucalyptus stems and a striped runner. My kind of front hall has shells on the table and the door open to the breeze. Every piece is linked in my shop page. #coastalhome #autumndecor #coastalgrandmother #ad As an Amazon Associate I earn from qualifying purchases.

- **Alt text (194 chars):** Collage on a sea-glass blue background: blue and white ginger jar, white pumpkins, woven basket, rattan mirror, knit throw, eucalyptus and striped runner around the title Seaside Autumn at home.
- **Link:** https://danashoreandhome.com/shop-the-look/coastal-fall-entryway-decor
- **AI label:** on (R13), if the pin builder offers it.

[Order conflict: Part 5 lists "Then the DISCLOSURE LINE. 3 to 5 keyword hashtags", which puts hashtags after the disclosure, but R3 says every description "ends with the DISCLOSURE LINE". I put hashtags before the disclosure so R3 holds. Also unclear whether #ad counts toward the 3 to 5 hashtags. I kept 3 to 4 keyword hashtags plus #ad. Pin 2 alt text leaves out the hearts and bow that the Format B template forces into the image, so if they appear, the alt text is incomplete.]

## 5. The site page Dana pastes into Squarespace

File the task writes to the folder (name chosen by me, the kit gives none): `pages/2026-10-05-coastal-fall-entryway-decor.txt`

```
PASTE INTO SQUARESPACE: Coastal Fall Entryway
Paste by: Monday 5 October 2026, 12:00 pm Eastern (the noon sweep schedules pin 1 for 1:30 pm only if this page loads)

WHERE
Pages > Shop the Look (blog) > + New post
Post title: Coastal Grandmother Fall Entryway Decor
Post URL (Settings > URL slug): coastal-fall-entryway-decor
Full address when live: https://danashoreandhome.com/shop-the-look/coastal-fall-entryway-decor
SEO description (151 characters): Coastal grandmother fall entryway decor in sea blue and cream: a ginger jar, white ceramic pumpkins, a seagrass basket and a rattan mirror, all linked.

IMAGES (the task can't save image files to your folder)
Open Higgsfield, go to your image history, and download the two images made on Saturday 3 October around 1:30 pm:
  1. the flat lay titled "COASTAL FALL entryway". Alt text: Overhead photo of a fall entryway flat lay on whitewashed floorboards: blue and white ginger jar, white ceramic pumpkins, seagrass basket, rattan mirror and knit throw, titled Coastal Fall entryway.
  2. the collage titled "SEASIDE AUTUMN at home". Alt text: Collage on a sea-glass blue background: blue and white ginger jar, white pumpkins, woven basket, rattan mirror, knit throw, eucalyptus and striped runner around the title Seaside Autumn at home.
Add them with an Image block, flat lay first.

TEXT BLOCK 1 (intro, paste as normal text)
The entryway is the first thing you see coming home, so this fall I wanted it calm, not costume. Sea blue and cream, a ginger jar full of eucalyptus, three white pumpkins and a seagrass basket holding the throw for chilly mornings. It says autumn without shouting it.

As an Amazon Associate I earn from qualifying purchases.

The images on this page are AI-generated styling photos. The linked pieces may look slightly different in real life.

CODE BLOCK (paste into a Code block, set to HTML)
<h2>Shop the look</h2>
<ol>
  <li><a href="https://amzn.to/SIMUL01" target="_blank" rel="sponsored nofollow noopener">Large blue and white ginger jar vase with lid</a></li>
  <li><a href="https://amzn.to/SIMUL02" target="_blank" rel="sponsored nofollow noopener">Set of 3 matte white ceramic pumpkins</a></li>
  <li><a href="https://amzn.to/SIMUL03" target="_blank" rel="sponsored nofollow noopener">Seagrass storage basket with handles</a></li>
  <li><a href="https://amzn.to/SIMUL04" target="_blank" rel="sponsored nofollow noopener">Round rattan wall mirror</a></li>
  <li><a href="https://amzn.to/SIMUL05" target="_blank" rel="sponsored nofollow noopener">Faux eucalyptus and dried-look hydrangea stems</a></li>
  <li><a href="https://amzn.to/SIMUL06" target="_blank" rel="sponsored nofollow noopener">Cream cable knit throw blanket</a></li>
  <li><a href="https://amzn.to/SIMUL07" target="_blank" rel="sponsored nofollow noopener">Blue and cream striped cotton runner rug</a></li>
</ol>
<p>As an Amazon Associate I earn from qualifying purchases. Every link on this page is an affiliate link: if you buy through it, I earn a small commission at no extra cost to you.</p>

If your Squarespace plan doesn't offer Code blocks, paste the list as normal text links instead. You lose the "sponsored" tag on the links, which Google prefers but Amazon doesn't require. Keep the disclosure line either way.

Then click Publish, open the full address above on your phone, and check it loads.
```

(All links above are SIMULATED. No prices anywhere. No brand names.)

[The kit never says the site page needs an AI-image note. I added it because the page shows AI images next to "shop the look" links for real products.]

## 6. Schedule (Part 6)

Pinterest posts these; Dana's computer does not need to be on at the post times.

| pin | date and time (US Eastern) | board | condition |
|---|---|---|---|
| Pin 1, Format A flat lay | Monday 5 October 2026, 1:30 pm EDT | Coastal Grandmother Decor | page loads when checked |
| Pin 2, Format B collage | Thursday 8 October 2026, 8:30 pm EDT | Coastal Grandmother Decor | page loads when checked |

Checks: 3 days apart (R7). 7 hours from any other pin that week. Furthest pin is 5 days ahead of the run, inside 14 (R12). Before the renewal date.

What actually happens on this path, run by run:
1. Sat 3 Oct, 1:05 pm, weekly run: page not live yet, so no pin can ship (08: "A pin never links to a page that doesn't load"). Both pins logged `built`. Page file written. Lock released. Report sent.
2. Sun 4 Oct: Dana pastes the page, downloads the 2 images from Higgsfield, publishes.
3. Sun 4 Oct 12:00 pm or 5:00 pm, pull sweep: finds `built` pins and schedules up to 4 of them.
   [The pull sweep reads only Part 1 and Part 6 of 03, not 08. Nothing in its prompt says "check the page loads first". It would schedule pins to a page that may still be a 404. It also says "next free slots" without saying which slot type (pin 1 or pin 2) or which day, so it could put look 2's pin 1 into Sunday's 8:30 pm slot.]
4. The sweep verifies on Pinterest's scheduled pins page, then adds rows to pin-tab.md.

Week plan for all 3 looks, if every page is pasted by Sunday:

| look | pin 1 | pin 2 |
|---|---|---|
| Coastal fall entryway | Mon 5 Oct 1:30 pm | Thu 8 Oct 8:30 pm |
| Oatmeal linen pants and fisherman sweater | Wed 7 Oct 1:30 pm | Sat 10 Oct 8:30 pm |
| Blue and white kitchen open shelving | Fri 9 Oct 1:30 pm | Mon 12 Oct 8:30 pm |

## 7. Log rows written at end of the weekly run

storefront-log.md:

| date | window or line | look name | kind | items (short name + ASIN) | list or page link | pin 1 title | pin 2 title | scheduled times | status | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10-05 | Window 1, Coastal Harvest | Coastal Fall Entryway | theme list | ginger jar vase B0SIMUL001; ceramic pumpkins B0SIMUL002; seagrass basket B0SIMUL003; rattan mirror B0SIMUL004; eucalyptus and hydrangea stems B0SIMUL005; cable knit throw B0SIMUL006; striped runner B0SIMUL007 (all simulated) | https://danashoreandhome.com/shop-the-look/coastal-fall-entryway-decor | Coastal Grandmother Fall Entryway Decor: Blue and White, Ceramic Pumpkins and Woven Texture | Coastal Fall Home Decor Ideas: A Calm Sea Blue and Cream Entryway for Autumn | planned 2026-10-05 1:30 pm / 2026-10-08 8:30 pm | built | waiting for Dana to paste pages/2026-10-05-coastal-fall-entryway-decor.txt into Squarespace |

pin-tab.md: no rows yet. Part 7 step 1 adds pins only after verifying them on Pinterest. [So until the sweep schedules them, Dana has nothing to PULL, and the pin tab doesn't show her what's coming.]

browser-lock.txt: `free`.

## 8. Report to Dana

The kit's report format is "Built 5 looks, 10 pins scheduled and verified." and a second line only if something needs her. On this path something always needs her, so every week's report is two lines:

```
Built 3 looks. 6 pins are ready and waiting for their pages.
Paste the 3 files in the pages folder into Squarespace (with the 2 Higgsfield images each), and the next pull sweep schedules the pins.
```

[06 Task 1's REPORT and VERIFY sections have no case for this. VERIFY only checks look pages "if the blog half is on", and BLOG HALF is off for Dana, so the weekly task never checks her pages either.]
