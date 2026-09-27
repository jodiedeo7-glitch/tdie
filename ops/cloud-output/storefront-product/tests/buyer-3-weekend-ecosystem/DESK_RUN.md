# Desk run: one look, end to end (simulated, no browser)

Tester role 3: the weekly task (06 Task 1) running 03_THEMED_LOOK_RECIPE.txt with 07 (persona path), 08 (Influencer path) and 09 STEP 3 (blog half), for Priya. Everything a browser would produce (ASINs, short links, the Idea List address, images) is marked **SIMULATED**. Every copy string below was counted with a script, not by eye.

Assumption for the blog-half part: Priya has since run 09 STEP 1 and added the STEP 2 lines to MY_RECIPE.txt (BLOG HALF: on, SITE: https://priyaplans.com, REPO UPLOAD PAGE: https://github.com/priyaplans/site/upload/main/src/lifestyle). The MY_RECIPE.txt the setup chat wrote says BLOG HALF: off, because 02 never offers it (FINDINGS F-09).

## 0. Run start

| Step | Time (PT) | What the task does | Kit source |
|---|---|---|---|
| Fire | Sat 3 Oct 2026, 1:05 pm | Scheduled task fires | 06 Task 1 header |
| Read | 1:05 pm | MY_RECIPE.txt, 03, 07, 08, storefront-log.md, pin-tab.md, browser-lock.txt, then 09 (blog half on) | 06 Task 1 READ FIRST |
| Lock | 1:06 pm | browser-lock.txt reads `free`; writes `busy weekly-themed-looks 2026-10-03 13:06` | R16 |
| Boards | 1:07 pm | Opens both boards, both Public | R11 |
| Leftovers | 1:08 pm | storefront-log.md empty, nothing built-not-scheduled | Part 2 step 1 |
| Pick | 1:09 pm | "Next 7 days starting from the first day with no pin 1 scheduled" = **today, Sat 3 Oct**. Today's 1:30 pm flat lay slot is 21 minutes away and cannot be met by a look that takes 45+ minutes to build. The task has no rule for this and must improvise: it starts from **Sun 4 Oct** and plans Sun 4 to Sat 10 Oct. | 06 Task 1 JOB 4 (FINDINGS F-04) |

R16 written time format: the kit says `busy [task name] [time]` with no date. I wrote a date so the 2-hour stale test is decidable across days. With the literal format, a lock left at "1:06 pm" on Saturday reads as fresh at 1:30 pm the following Monday.

## 1. Look choice (the week, then the one look run end to end)

Window for 4 to 10 Oct: WINDOW 1, Early fall and Halloween (27 Sep to 24 Oct). Pace 7. Rules applied: at least one evergreen, two clothing looks never back to back, no hero repeat within 30 days.

| Look date | Kind | Look | Source | Board |
|---|---|---|---|---|
| **Sun 4 Oct** | **Outfit** | **Plaid pleated skirt and cream turtleneck with penny loafers** | **Window 1, idea 1** | **Dark Academia Outfits** |
| Mon 5 Oct | Theme list | Moody candlelit study desk | Window 1, idea 3 | Study Desk Setup Ideas (section: fall) |
| Tue 6 Oct | Outfit | Burgundy cable knit, brown midi skirt, knee socks | Window 1, idea 4 | Dark Academia Outfits |
| Wed 7 Oct | Theme list | Autumn reading corner | Window 1, idea 5 | Study Desk Setup Ideas (fall) |
| Thu 8 Oct | Outfit | Walk-to-class trench, loafers, satchel | Window 1, idea 9 | Dark Academia Outfits |
| Fri 9 Oct | Theme list | Budget-friendly study desk makeover | EVERGREEN 13 | Study Desk Setup Ideas (fall) |
| Sat 10 Oct | Outfit | Tweed blazer over a striped button-down | Window 1, idea 2 | Dark Academia Outfits |

Problems met while picking:
- Sun 4 Oct and Thu 8 Oct outfits both want penny loafers. "No hero piece repeats within 30 days. Accessories may repeat once a week." Shoes are neither hero nor accessory in the kit's vocabulary. I chose different loafers for 8 Oct. (FINDINGS F-21)
- Theme-list looks on the persona path: 03 Part 4 says pin 2 is "your persona wearing every piece". A desk lamp and a candle cannot be worn. Mon, Wed and Fri have no defined pin 2. (FINDINGS F-06)
- Window 1 has 10 ideas and runs 4 weeks of builds at 7 a week. After this week, 5 window ideas remain for 2 more weeks of 6 non-evergreen looks each. (FINDINGS F-08)

The rest of this file runs **Sun 4 Oct** only.

## 2. Pieces (Part 3)

Kind: Outfit. Required: main piece (top plus bottom), shoes, bag, at least one jewelry, one accessory. 7 pieces.

| # | Short name (listing-safe, no brand) | Role | ASIN | Short link | Checks |
|---|---|---|---|---|---|
| 1 | Cream ribbed turtleneck sweater | top (hero) | B0SIMTNK01 (SIMULATED) | https://amzn.to/SIM0001 (SIMULATED) | in stock, 4.3 stars, 2,140 ratings, Prime, neutral piece |
| 2 | Brown plaid pleated midi skirt | bottom | B0SIMSKT02 (SIMULATED) | https://amzn.to/SIM0002 (SIMULATED) | 4.2, 860, Prime |
| 3 | Dark brown chunky penny loafers | shoes | B0SIMLOF03 (SIMULATED) | https://amzn.to/SIM0003 (SIMULATED) | 4.4, 3,900, Prime |
| 4 | Brown cable knit knee-high socks | accessory | B0SIMSOK04 (SIMULATED) | https://amzn.to/SIM0004 (SIMULATED) | 4.5, 1,200, Prime |
| 5 | Cognac faux leather satchel | bag | B0SIMBAG05 (SIMULATED) | https://amzn.to/SIM0005 (SIMULATED) | 4.3, 540, Prime |
| 6 | Gold oval locket necklace | jewelry | B0SIMLKT06 (SIMULATED) | https://amzn.to/SIM0006 (SIMULATED) | 4.4, 2,700, Prime |
| 7 | Round tortoiseshell glasses with clear lenses | accessory | B0SIMGLS07 (SIMULATED) | https://amzn.to/SIM0007 (SIMULATED) | 4.2, 310, not Prime |

Rejected during sourcing (typical for this theme, and each one is a rule the kit states):
- A plaid skirt whose listing name carried a school-uniform brand (R5 skip).
- A satchel with an embossed crest on the flap (R5: "no team or university crests").
- A "Harry-style" round glasses listing (R5: character likeness in the listing name).
- A clothbound classic novel as the optional "one book". Any real book has a title and author on the cover: printed text in the image (Format A "no other text") and a brand-like name in the listing (R6). The kit allows "one book" in an outfit but gives no way to show or name one. (FINDINGS F-20)

Idea List (Part 3 step 5): Storefront > Create content > Idea List, title "Plaid Pleated Skirt and Cream Turtleneck with Penny Loafers", 7 pieces added by ASIN, AI description dismissed, Save, Submit.
Public address: **https://www.amazon.com/shop/priyaplans/list/SIMULATED0001** (SIMULATED).
Unknown the kit does not cover: if the list shows "in review" and the public /list/ address 404s at this moment, the task has no instruction (wait? fall back to storefront home? ship anyway?). (FINDINGS F-22)

Product sheet: one screenshot of the 7 main images laid in a grid over an amazon.com tab (Part 3 step 6).

## 3. Images (Part 4 and 07)

### Pin 1: Format A (first look of the run, so Format A), Seedream 4.5 on Higgsfield, product sheet attached

Surface chosen from the list: warm wood floorboards. Title color: white (contrasts most with mid-brown wood). Title words: "DARK ACADEMIA" + "Fall Edit" = 4 words (rule: 3 to 5).

```
Please make me a very realistic overhead flat lay photo of the outfit in the attached image. I can't use the exact Amazon images outside of Amazon, so this needs to be a new photo. Shot straight down, portrait 2:3, like a good-quality photo taken on a phone. The outfit is laid out as if worn, pieces overlapping and touching, on warm wood floorboards: a cream ribbed turtleneck sweater with a fold-over neck and long sleeves, laid with the sleeves softly bent; a brown, camel and cream plaid pleated midi skirt with an even knife pleat, laid below the sweater as if tucked in; a pair of dark brown chunky penny loafers with a lug sole and a leather strap across the vamp, placed at the hem of the skirt; a pair of brown cable knit knee-high socks, one draped over a loafer; a cognac faux leather satchel with a front flap, two buckle straps and a top handle, set to the right of the sweater; a gold oval locket on a fine gold chain, curled on the sweater's chest; a pair of round tortoiseshell glasses with thin gold temples and clear lenses, folded beside the collar. Each piece matches its screenshot in color, shape and detail. Tucked in around the outfit, filling the frame edge to edge with almost no empty background: a small stack of old clothbound books with plain unmarked spines, a brass candlestick with a lit cream taper candle, a cup of black coffee on a white saucer, a scatter of dried oak leaves, a vintage-style fountain pen, a sprig of dried eucalyptus. Every product sits fully inside the frame. Soft natural window light, gentle real shadows, visible fabric texture, small real-life imperfections, photorealistic. Across the upper third, set directly on the photo, a large two-style title: "DARK ACADEMIA" in a bold high-contrast serif in capitals, with "Fall Edit" beneath it in a thick flowing brush script, both in white, perfectly spelled, sharp edges, filling about two thirds of the width. No logos, no brand names, no labels on products, no watermark, no person, no other text.
```

Checks: every bracket filled, every other word kept, no color codes, no brand, 6 extras (rule 4 to 8), books have "plain unmarked spines" so R5 and "no other text" hold.

### Pin 2: persona lifestyle, Gemini, attach (1) persona.jpg, (2) the product sheet

Format: over-the-shoulder walking away (P4; first person shot of the week, so a visible face is allowed, but this format keeps it partial). Scene: PERSONA WORLD "the leafy tree-lined street she walks to class".

```
Photograph of this exact woman from the attached reference image (the first image). Identity is taken only from the reference. Please make me one single very realistic lifestyle photo, not a collage or grid. I can't use the exact Amazon images, so this is a new photo. She is wearing every item in the second image, matching each one in color and detail: the cream ribbed turtleneck sweater tucked into the brown, camel and cream plaid pleated midi skirt, the brown cable knit knee-high socks, the dark brown chunky penny loafers with the lug sole, the cognac faux leather satchel with the front flap and two buckles on her left shoulder, the gold oval locket on a fine chain over the turtleneck, the round tortoiseshell glasses with thin gold temples, her hair in a low twisted bun held with a tortoiseshell claw clip. Nails: deep burgundy. Format: over-the-shoulder walking away. Scene: the leafy tree-lined street she walks to class, on a bright Sunday morning in October, fallen orange leaves on the sidewalk, glancing back over her left shoulder mid-step. Make it look like a good-quality photo taken on a phone: 26mm phone lens, natural light, realistic camera angle, real skin and fabric texture, small real-life imperfections, nothing glossy. Portrait 2:3. No lettering, no signs, no logos, no text anywhere in the frame.
```

Checks: nothing about face, hair color, skin, body or age (P1); hair described only as "how it is worn today" (P2); scene from PERSONA WORLD (P3); no text (P6).

Capture: each finished image is shown full size in its own tab and screenshotted (Part 4 capture method). **Gap:** a 1000 by 1500 image does not fit in a typical 1280 by 800 browser viewport at 100 percent, and on a Retina screen a screenshot is 2x. "Show it at an exact size and screenshot it" cannot produce 1000 by 1500 without scaling the page. (FINDINGS F-11)

## 4. Pin copy (Part 5), counted

Board: Dark Academia Outfits. Link (both pins): https://www.amazon.com/shop/priyaplans/list/SIMULATED0001

Order used in the description: search phrase, pieces, one line of voice, "Every piece is linked in my Idea List.", hashtags, then the DISCLOSURE LINE last. Part 5 lists the disclosure BEFORE the hashtags; R3 says every description ENDS with the disclosure. I followed R3 because Part 1 rules "never move". (FINDINGS F-02)

**Pin 1 title** (82 characters, rule 60 to 100):
Dark Academia Fall Outfit Ideas: The Plaid Skirt and Loafers Look for Library Days

**Pin 1 description** (489 characters including the disclosure, rule 450 to 500):
This dark academia fall outfit is the one I'd wear to the library on a crisp October afternoon. A cream ribbed turtleneck, a brown plaid pleated midi skirt, dark brown penny loafers, brown knee-high socks, a cognac satchel, a gold oval locket and round tortoiseshell glasses. Tweed energy, zero costume, and I'd wear it all week. Every piece is linked in my Idea List. #darkacademia #falloutfits #darkacademiaoutfit #plaidskirt #ad As an Amazon Influencer I earn from qualifying purchases.

**Pin 1 alt text** (187 characters, rule 150 to 200):
Overhead flat lay on warm wood floorboards of a cream turtleneck, brown plaid pleated skirt, dark brown penny loafers, a cognac satchel, a gold locket, round glasses and brown knee socks.

**Pin 2 title** (88 characters):
Dark Academia Outfit for Class: Cream Turtleneck, Plaid Midi Skirt and a Leather Satchel

**Pin 2 description** (496 characters including the disclosure):
A dark academia outfit for class that works on a Tuesday. A cream ribbed turtleneck tucked into a brown plaid pleated midi skirt, knee-high socks, penny loafers, a cognac satchel on one shoulder, a gold oval locket and round tortoiseshell glasses. Walk-to-class cozy, the kind of outfit that makes you want a notebook and a latte. Every piece is linked in my Idea List. #darkacademiastyle #falloutfitideas #collegeoutfits #preppystyle #ad As an Amazon Influencer I earn from qualifying purchases.

**Pin 2 alt text** (180 characters):
A woman on a leafy fall street glancing back over her shoulder in a cream turtleneck, brown plaid pleated midi skirt, knee socks and loafers, a cognac satchel on her left shoulder.

Checks: no price, no brand, no em dash, no promise of result or speed, 4 keyword hashtags each (rule 3 to 5; #ad inside the disclosure not counted, which the kit does not say). The disclosure starts at character 429 of 489 in pin 1: Pinterest shows roughly the first line of a description in the closeup, so "#ad" is not visible without expanding. (FINDINGS F-03)

Pin 1 alt text does not mention the "DARK ACADEMIA Fall Edit" words that are on the image. The kit says "what's literally in the image" but never says whether overlay text counts.

## 5. Schedule (Part 6)

| Pin | Board | Publish at (PT) | Rule check |
|---|---|---|---|
| Pin 1, flat lay | Dark Academia Outfits | **Sun 4 Oct 2026, 1:30 pm** | look's date, flat lay slot, 1 day ahead (max 14) |
| Pin 2, persona | Dark Academia Outfits | **Wed 7 Oct 2026, 8:30 pm** | exactly 3 days later, second slot (R7), 4 days ahead |

Neighbors this week: pin 1 of the Wed 7 Oct look posts at 1:30 pm, 7 hours before this look's pin 2 (1-hour gap holds). Every day from Wed 7 Oct carries exactly one 1:30 pm and one 8:30 pm pin: at pace 7 there is no free slot left for any leftover (FINDINGS F-07).

AI label (R13): toggled on in the Create Pin form. The kit gives no instruction if the toggle is not in the form. (FINDINGS F-16)

Verify: scheduled pins page, both pins found by title and time; image, board, link confirmed. Status: verified.

## 6. Log rows as written (Part 7)

storefront-log.md:

| date | window or line | look name | kind | items (short name + ASIN) | list or page link | pin 1 title | pin 2 title | scheduled times | status | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10-04 | Window 1: Early fall and Halloween | Plaid pleated skirt and cream turtleneck with penny loafers | outfit | Cream ribbed turtleneck sweater B0SIMTNK01; Brown plaid pleated midi skirt B0SIMSKT02; Dark brown chunky penny loafers B0SIMLOF03; Brown cable knit knee-high socks B0SIMSOK04; Cognac faux leather satchel B0SIMBAG05; Gold oval locket necklace B0SIMLKT06; Round tortoiseshell glasses with clear lenses B0SIMGLS07 | https://www.amazon.com/shop/priyaplans/list/SIMULATED0001 | Dark Academia Fall Outfit Ideas: The Plaid Skirt and Loafers Look for Library Days | Dark Academia Outfit for Class: Cream Turtleneck, Plaid Midi Skirt and a Leather Satchel | 2026-10-04 1:30 pm; 2026-10-07 8:30 pm | verified | Format A pin 1; persona over-the-shoulder pin 2; page live https://priyaplans.com/lifestyle/dark-academia-fall-outfit-plaid-skirt-loafers |

pin-tab.md:

| posting date | time | board | kind | look | pin title | link | status | PULL |
|---|---|---|---|---|---|---|---|---|
| 2026-10-04 | 1:30 pm | Dark Academia Outfits | outfit | Plaid pleated skirt and cream turtleneck with penny loafers | Dark Academia Fall Outfit Ideas: The Plaid Skirt and Loafers Look for Library Days | https://www.amazon.com/shop/priyaplans/list/SIMULATED0001 | scheduled | |
| 2026-10-07 | 8:30 pm | Dark Academia Outfits | outfit | Plaid pleated skirt and cream turtleneck with penny loafers | Dark Academia Outfit for Class: Cream Turtleneck, Plaid Midi Skirt and a Leather Satchel | https://www.amazon.com/shop/priyaplans/list/SIMULATED0001 | scheduled | |

Note: the log keeps titles only. If either pin had been left "built", the next run or the pull sweep would need the description, alt text and the image itself to schedule it, and none of those are stored anywhere. (FINDINGS F-05)

## 7. Blog half (09 STEP 3)

Slug: `dark-academia-fall-outfit-plaid-skirt-loafers` (09 never says how to make a slug; I used the page title, lowercased and hyphenated, trimmed to the key words).
Category: `outfits`. **Guess.** The categories were invented by the one-off site chat in 09 STEP 1 and live only in the site's code. MY_RECIPE.txt does not carry them and the weekly task cannot read the repo. (FINDINGS F-10)
Season: `Fall` (window 1 is "Early fall and Halloween"; the kit does not say how to turn a window name into a season name).
Date: the look's date (pin 1 date). 09 does not say which date.
Intro (274 characters, 2 sentences, no price). Meta description the site would generate (cut to 155 at a word boundary, 148 characters): "The dark academia fall outfit I'd wear to the library on a crisp October afternoon: a cream turtleneck, a brown plaid pleated skirt and chunky penny"

### The JSON exactly as it would be uploaded

File name: `dark-academia-fall-outfit-plaid-skirt-loafers.json` (validated with a JSON parser)

```json
{
  "slug": "dark-academia-fall-outfit-plaid-skirt-loafers",
  "title": "Dark Academia Fall Outfit: Plaid Skirt, Turtleneck and Loafers",
  "date": "2026-10-04",
  "category": "outfits",
  "season": "Fall",
  "intro": "The dark academia fall outfit I'd wear to the library on a crisp October afternoon: a cream turtleneck, a brown plaid pleated skirt and chunky penny loafers. A cognac satchel, a gold locket and round tortoiseshell glasses finish it, so it reads like a choice, not a costume.",
  "images": [
    {
      "file": "dark-academia-fall-outfit-plaid-skirt-loafers-pin1.jpg",
      "alt": "Overhead flat lay on warm wood floorboards of a cream turtleneck, brown plaid pleated skirt, dark brown penny loafers, a cognac satchel, a gold locket, round glasses and brown knee socks."
    },
    {
      "file": "dark-academia-fall-outfit-plaid-skirt-loafers-pin2.jpg",
      "alt": "A woman on a leafy fall street glancing back over her shoulder in a cream turtleneck, brown plaid pleated midi skirt, knee socks and loafers, a cognac satchel on her left shoulder."
    }
  ],
  "link": "https://www.amazon.com/shop/priyaplans/list/SIMULATED0001",
  "items": [
    {
      "name": "Cream ribbed turtleneck sweater",
      "link": "https://amzn.to/SIM0001"
    },
    {
      "name": "Brown plaid pleated midi skirt",
      "link": "https://amzn.to/SIM0002"
    },
    {
      "name": "Dark brown chunky penny loafers",
      "link": "https://amzn.to/SIM0003"
    },
    {
      "name": "Brown cable knit knee-high socks",
      "link": "https://amzn.to/SIM0004"
    },
    {
      "name": "Cognac faux leather satchel",
      "link": "https://amzn.to/SIM0005"
    },
    {
      "name": "Gold oval locket necklace",
      "link": "https://amzn.to/SIM0006"
    },
    {
      "name": "Round tortoiseshell glasses with clear lenses",
      "link": "https://amzn.to/SIM0007"
    }
  ]
}
```

### Upload and publish

| Step | Time (PT, estimate) | Action |
|---|---|---|
| 1 | Sat 3 Oct, about 2:10 pm | Fresh tab: https://github.com/priyaplans/site/upload/main/src/lifestyle (needs Priya signed in to GitHub in Chrome; not in 01 REQUIREMENTS) |
| 2 | | Attach `...-pin1.jpg` and `...-pin2.jpg` from the screenshots through the file input. |
| 3 | | Attach `...json`. **Blocked:** the JSON is text the task wrote, not a screenshot, and the browser tools can only hand an image they captured to a file input. Workaround the kit does not give: https://github.com/priyaplans/site/new/main/src/lifestyle?filename=dark-academia-fall-outfit-plaid-skirt-loafers.json and paste, as a second commit AFTER the images. (FINDINGS F-12) |
| 4 | | Commit message "Add look: Dark Academia Fall Outfit: Plaid Skirt, Turtleneck and Loafers", Commit changes (direct to main). |
| 5 | about 2:12 pm | Vercel builds from main. |
| 6 | about 2:14 pm | Open https://priyaplans.com/lifestyle/dark-academia-fall-outfit-plaid-skirt-loafers. If it 404s (build still running, or build failed on a bad JSON or unknown category), 09 gives no next step. (FINDINGS F-13) |

Timing reality for the whole run: this one look is roughly 45 to 70 minutes of browser work (tester estimate: about 7 product pages with SiteStripe captures, one Idea List, two generations with up to two correction rounds each, two Pinterest pins, one verify, two GitHub commits). Seven looks is 5 to 8 hours from 1:05 pm, so the run ends between about 6 pm and 9 pm. The 6:00 pm pull sweep will find a lock older than 2 hours and take it mid-run (FINDINGS F-01).

## 8. One-line report the task would give

Built 1 look, 2 pins scheduled and verified, page live. (A full run: "Built 7 looks, 14 pins scheduled and verified.")
