# JOB D1 REPORT: VIRAL PRODUCT BANK, SUPPLIERS AND MARGIN MODEL

27 September 2026. Sources checked: `ops/cloud-kit/README_START_HERE.md`, `ops/canon/canon.json`, `ops/canon/TDIE_CANON.md`, `ops/cloud-kit/TDIE_LEGALLY_BLONDE_PIN_FACTORY.md`, `ops/cloud-kit/TDIE_LIFESTYLE_LIST_MAP.md`, `ops/cloud-kit/TDIE_PINK_FINDS_GROWTH_PLAN.md`, `ops/cloud-kit/TDIE_IMAGE_GENERATION_MASTER.md`, `ops/cloud-kit/TDIE_SIX_M_FRAMEWORK.md`, `ops/cloud-kit/CLOUD_CREDIT_JOBS_ROUND_2.md` (Job 3 recipe), `src/lifestyle/README.md`, `src/lifestyle/pink-workwear-freezing-office.json`, `src/lifestyle/pink-halloween-porch-decor.json`, `src/lifestyle/pink-witch-halloween-costume.json`, `src/data/pinkfinds.js`, `ops/cloud-output/DESKTOP_FINISH_QUEUE.md`.

**One line:** bank of 40 products, 40 of 40 on a US-warehouse winner supplier (all of them, by rule; each one still has to be confirmed in stock on the supplier site), recommended platform Shopify Basic plus the free CJ Dropshipping app (Zendrop as the paid fallback), earliest Christmas order-by date in the bank **Fri 11 Dec 2026**.

## What this session could and could not reach

- This container's network policy blocks every supplier, trend and pricing site (TikTok, Pinterest Trends, Google Trends, Amazon, Etsy, Temu, AliExpress, CJ, Zendrop, Spocket, AutoDS, USADrop, Printful, Printify, Shopify, Stripe, USPS, UPS, FedEx, dor.georgia.gov, ftc.gov). Only web search worked. **Every number in this job comes from a search-result snippet, never from the page itself.** Each figure carries "seen in snippet" or "unverified: reason", and every supplier cost is an estimate unless the row says a price was seen. The desktop queue (section 4 of `DESKTOP_FINISH_QUEUE.md`) is where the figures get confirmed, signed in.
- The research agents also shared one search budget of 200 calls, which ran out part way through; the lead session filled the gaps with its own searches. Categories with the thinnest evidence: Halloween decor (listings exist, counts not visible), NYE party decor, dog accessories, the coffee bar. Those items are in the Candidates sheet with the reason they were not banked.
- Job 3's recipe was followed for the look drafts. Nothing was written into `src/lifestyle/`, canon or the live site. Nothing was built.

## Flags for Jodie (three, each once)

1. **Price bands.** The growth plan copy in the repo names no dollar bands, so the bank uses the factory's rule (section 3: mostly under $50, one splurge per look; window 5: "under 25" gift guides). Bands in the model: core up to $50, splurge up to $79, one splurge per look. If she meant different numbers, change cells B12 and B13 on the Margins sheet and the Band OK? column re-checks itself.
2. **Halloween is honest, not optimistic.** The Halloween order-by date is Fri 16 Oct 2026 for every US-warehouse product. No store exists today, D2 has not run, and the platform is unpicked, so the five Halloween products only earn this year if the store is live by about 12 October. They are kept because velvet pumpkins, the throw, the pillow covers and the party cups all carry into Thanksgiving and Christmas; only the bunny ears are Halloween-only.
3. **Sized apparel is out except two soft pieces.** The pink cardigan (40.8K sold on TikTok Shop) and the cropped blazer were the two strongest workwear signals, and both were cut: sized clothing returns run far above the 8% allowance and blazers cannot be worn by Tommy Kate in lifestyle photos. The bank keeps one pajama set (S to XL) and one one-size robe, both flagged. "Pink workwear most weeks" is met by the desk-and-bag look (desk mat, tote, sleeve, stationery), which is the workwear line the brief itself names.

## The worked margin example (Q01, fluffy pink bunny ears headband)

Every column on the Margins sheet, one product, so the maths can be checked by hand. Inputs in blue on the sheet.

| Line | Value | Where it comes from |
|---|---|---|
| Sale price | $32.99 | The lowest x.99 that clears both floors (below) |
| Product cost | $7.70 | Estimate: 40% of the $19.28 TikTok Shop retail seen (Zendrop guide ratio: $8 to $12 product on a $25 retail). Confirm on cjdropshipping.com |
| Inbound shipping | $4.50 | Small parcel from a US warehouse, estimate (Zendrop guide: $4 to $6; CJ: "about $5") |
| Packaging | $0.50 | Insert card or tissue; CJ ships in its own unbranded mailer |
| Payment processing | $1.26 | 2.9% of $32.99 plus $0.30 |
| App fee share | $1.30 | (Shopify Basic $39 + CJ app $0) / 30 orders a month |
| Return allowance | $2.64 | 8% of the sale price |
| Ad or creator cost, scenario 1 | $0.00 | Pinterest and email traffic |
| Sales tax | not a cost | Collected from the buyer at checkout and remitted; Georgia nexus from day one |
| **Total cost at $0 CAC** | **$17.90** | sum of the lines above |
| **Gross margin $ at $0 CAC** | **$15.09** | price minus total cost |
| **Gross margin % at $0 CAC** | **45.8%** | floor is 45% |
| Gross margin $ at $5 CAC | $10.09 | scenario 2 subtracts $5 |
| Gross margin % at $5 CAC | 30.6% | floor is 25% |
| Break-even units a month | 3 | $39 fixed cost / (price minus product, shipping, packaging, processing and return allowance) = 39 / 16.39 |

Pricing rule, written out: with the costs above, the 45% floor needs price x to satisfy x minus (2.9% of x + 8% of x) minus fixed costs of $14.30 to be at least 45% of x, so x is at least $32.43; the $5 CAC floor needs x of at least $30.11. The higher of the two, rounded up to the next .99, is $32.99. Shipping is shown as free at checkout because it is inside the price. The same rule prices all 40; every one passes both floors and sits inside its band (Margins sheet, columns T and W).

## Top 10 by margin (gross margin % at $0 CAC)

| # | ID | Product | Price | Margin % at $0 CAC | Margin % at $5 CAC | Break-even units/month |
|---|---|---|---|---|---|---|
| 1 | E17 | Pink bow spa headband and wristband set | $20.99 | 50.5% | 26.7% | 4 |
| 2 | Q14 | Pink satin sleep bonnet, adjustable | $22.99 | 49.5% | 27.8% | 4 |
| 3 | E04 | Pink aesthetic sticky notes and tabs set | $22.99 | 49.5% | 27.8% | 4 |
| 4 | E10 | Bling rhinestone car cup coasters, pink, 2 pack | $22.99 | 49.5% | 27.8% | 4 |
| 5 | E11 | Plush pink seat belt covers with bow, pair | $23.99 | 47.0% | 26.2% | 4 |
| 6 | E20 | Pink satin sleep mask with bow | $24.99 | 46.7% | 26.7% | 4 |
| 7 | E22 | Pink satin heatless curling rod set | $24.99 | 46.7% | 26.7% | 4 |
| 8 | E12 | Pink magnetic suction car phone holder, no electronics | $25.99 | 46.4% | 27.2% | 3 |
| 9 | E16 | Hot pink multi-compartment desk and vanity organiser | $27.99 | 46.2% | 28.4% | 3 |
| 10 | Q06 | Pink velvet Christmas tree bows, 24 pack | $33.99 | 46.1% | 31.4% | 3 |

The margins cluster at 45 to 47% because the price rule sets every product at the lowest price that clears the floor; the real spread is in the $5 CAC column, where the pricier items hold up better.

## Top 10 by viral signal (largest number seen in a snippet)

| # | ID | Product | Signal |
|---|---|---|---|
| 1 | Q14 | Pink satin sleep bonnet, adjustable | 351.2K sold (TikTok Shop keyword page 'hair bonnets') |
| 2 | E08 | Fluffy pink steering wheel cover, universal 15 inch | 57.0K total sold (TikTok Shop 'fluffy pink steering wheel cover'), Amazon 200+ to 400+ bought in past month |
| 3 | E17 | Pink bow spa headband and wristband set | 13.7K sold at $2.11 (TikTok Shop) |
| 4 | E01 | Pink PU leather desk mat, large | 10,000 est. monthly sales for the #1 ASIN (ASINsight, Jun 2026) |
| 5 | Q11 | Pink 40 oz insulated tumbler with handle and straw | 10K monthly sales for the #1 ASIN, #2 8K (+20% MoM) (ASINsight, mid-2026) |
| 6 | E16 | Hot pink multi-compartment desk and vanity organiser | 7.7K sold at $10.99 (TikTok Shop) |
| 7 | E07 | Pink quilted puffer laptop tote | 7K monthly sales for the #1 ASIN (ASINsight) |
| 8 | E19 | Puffy pink slippers | 5.7K sold at $17.28 and 3.6K at $30.98 (TikTok Shop) |
| 9 | Q01 | Fluffy pink bunny ears headband | 4.8K sold at $19.28 (TikTok Shop) |
| 10 | E20 | Pink satin sleep mask with bow | 4.2K sold at $39.00 (TikTok Shop) |

Not banked despite big numbers: pink cardigan (40.8K sold, sized apparel), floral quilted foldable basket (20.0K sold as a laundry basket, too bulky), pink reusable party cups are banked but the 1.9K figure sits on a trademark keyword ("pink solo cups"), pink dog beds (5K+ bought, too bulky to ship inside the band).

## The 40, by look (see Bank40 sheet for suppliers, and `looks/` for every draft)


**Pink Halloween Party at Home, Last Call** (Halloween, `pink-halloween-party-at-home-last-call`)
- Q01 Fluffy pink bunny ears headband: $32.99, 46% / 31%. Christmas order by Fri 11 Dec 2026.
- Q02 Pink velvet pumpkins, set of 12: $35.99, 46% / 32%. Christmas order by Fri 11 Dec 2026.
- Q03 Pink faux fur throw blanket, 50 by 60: $50.99, 45% / 36%. Christmas order by Fri 11 Dec 2026.
- Q04 Pink velvet throw pillow covers, pair: $28.99, 46% / 28%. Christmas order by Fri 11 Dec 2026.
- Q05 Pink reusable party cups, 16 oz pack: $40.99, 45% / 33%. Christmas order by Fri 11 Dec 2026. Flag: Never use the word 'Solo' in copy.

**The Pink Christmas Tree Edit** (Christmas, `the-pink-christmas-tree-edit`)
- Q06 Pink velvet Christmas tree bows, 24 pack: $33.99, 46% / 31%. Christmas order by Fri 11 Dec 2026.
- Q07 Pink velvet bow garland, 6 ft: $35.99, 46% / 32%. Christmas order by Fri 11 Dec 2026.
- Q08 Pink shatterproof ornament set, 45 pieces: $43.99, 45% / 34%. Christmas order by Fri 11 Dec 2026. Flag: Weak signal: rank not visible. Confirm demand on Amazon Best Sellers before ordering a sample.
- Q09 Pink velvet Christmas stocking with bow: $26.99, 46% / 28%. Christmas order by Fri 11 Dec 2026.
- Q10 Pink flocked tabletop Christmas tree, 2 ft, unlit: $50.99, 45% / 36%. Christmas order by Fri 11 Dec 2026. Flag: Unlit only. Pre-lit versions have batteries or plugs and are out.

**The Pink Gift Guide, Stocking to New Year's Eve** (Christmas, `pink-gift-guide-stocking-to-new-years-eve`)
- Q11 Pink 40 oz insulated tumbler with handle and straw: $43.99, 45% / 34%. Christmas order by Fri 11 Dec 2026. Flag: Generic only. Never 'Stanley' in the title, copy or tags.
- Q12 Pink velvet jewelry box with lock: $39.99, 45% / 33%. Christmas order by Fri 11 Dec 2026.
- Q13 Blush pink packing cubes, 8 piece set: $35.99, 46% / 32%. Christmas order by Fri 11 Dec 2026.
- Q14 Pink satin sleep bonnet, adjustable: $22.99, 50% / 28%. Christmas order by Fri 11 Dec 2026.
- Q15 Pink bow champagne flutes, set of 2: $39.99, 45% / 33%. Christmas order by Fri 11 Dec 2026. Flag: Fragile: $1.50 packaging line, and confirm the supplier double-boxes glass.
- Q16 Pink 2027 weekly and monthly planner, hardcover: $33.99, 46% / 31%. Christmas order by Fri 11 Dec 2026.

**The Law School Desk and Bag Setup, All Pink** (Evergreen, `the-law-school-desk-and-bag-setup-all-pink`)
- E01 Pink PU leather desk mat, large: $30.99, 45% / 29%. Christmas order by Fri 11 Dec 2026.
- E02 Pink acrylic desk organizer with pen cup: $30.99, 45% / 29%. Christmas order by Fri 11 Dec 2026.
- E03 Pink desk stationery set (stapler, tape dispenser, scissors, clips): $33.99, 46% / 31%. Christmas order by Fri 11 Dec 2026.
- E04 Pink aesthetic sticky notes and tabs set: $22.99, 50% / 28%. Christmas order by Fri 11 Dec 2026.
- E05 Pink wooden monitor riser with drawer: $54.99, 45% / 36%. Christmas order by Fri 11 Dec 2026. Flag: Splurge candidate for this look. AliExpress $30.50 seen; if CJ US cost is above $16 the price leaves the splurge band and the riser is cut.
- E06 Cream laptop sleeve with pink bow, 13 to 14 inch: $28.99, 46% / 28%. Christmas order by Fri 11 Dec 2026. Flag: List as 'fits 13 to 14 inch laptops'. Never 'MacBook' in the title.
- E07 Pink quilted puffer laptop tote: $44.99, 46% / 34%. Christmas order by Fri 11 Dec 2026.

**Pink Car Accessories That Make Every Red Light Feel Like a Photo Shoot** (Evergreen, `pink-car-accessories-that-make-every-red-light-feel-like-a-photo-shoot`)
- E08 Fluffy pink steering wheel cover, universal 15 inch: $30.99, 45% / 29%. Christmas order by Fri 11 Dec 2026. Flag: Plain plush only. No Kuromi, Hello Kitty or Barbie variants.
- E09 Pink leak-proof car trash can with lid: $30.99, 45% / 29%. Christmas order by Fri 11 Dec 2026.
- E10 Bling rhinestone car cup coasters, pink, 2 pack: $22.99, 50% / 28%. Christmas order by Fri 11 Dec 2026.
- E11 Plush pink seat belt covers with bow, pair: $23.99, 47% / 26%. Christmas order by Fri 11 Dec 2026. Flag: Never 'Jellycat' in copy (a seat belt cover keyword on TikTok Shop).
- E12 Pink magnetic suction car phone holder, no electronics: $25.99, 46% / 27%. Christmas order by Fri 11 Dec 2026. Flag: Weak signal (27 sold). Passive magnet and suction only; the 'aromatherapy' and LED versions are out.

**The Pink Vanity Organisation List** (Evergreen, `the-pink-vanity-organisation-list`)
- E13 Pink large-capacity travel vanity bag: $35.99, 46% / 32%. Christmas order by Fri 11 Dec 2026.
- E14 Pink glitter makeup brush holder cup: $26.99, 46% / 28%. Christmas order by Fri 11 Dec 2026. Flag: AliExpress pearl version $11.50 seen; plain glitter cup cost estimated at $5. Confirm on CJ.
- E15 Clear acrylic 2-tier perfume and vanity tray: $33.99, 46% / 31%. Christmas order by Fri 11 Dec 2026.
- E16 Hot pink multi-compartment desk and vanity organiser: $27.99, 46% / 28%. Christmas order by Fri 11 Dec 2026.
- E17 Pink bow spa headband and wristband set: $20.99, 51% / 27%. Christmas order by Fri 11 Dec 2026. Flag: TikTok Shop sells this at $2.11. The model prices it at $18.99 because shipping and fees are fixed, so it is an add-on to the vanity look, never a hero.
- E18 Covered acrylic makeup organiser with pink lid: $41.99, 46% / 34%. Christmas order by Fri 11 Dec 2026. Flag: Weak signal (45 sold). Kept to complete the look; confirm demand before a sample.

**Pink Self-Care Sunday: The Night Routine** (Evergreen, `pink-self-care-sunday-the-night-routine`)
- E19 Puffy pink slippers: $33.99, 46% / 31%. Christmas order by Fri 11 Dec 2026. Flag: Never 'Pluffi' in copy.
- E20 Pink satin sleep mask with bow: $24.99, 47% / 27%. Christmas order by Fri 11 Dec 2026.
- E21 Pink feather-trim pajama set: $37.99, 45% / 32%. Christmas order by Fri 11 Dec 2026. Flag: Sized S to XL: expect apparel returns above the 8% allowance. Textile flammability rule 16 CFR 1610 applies; ask the supplier for the test report.
- E22 Pink satin heatless curling rod set: $24.99, 47% / 27%. Christmas order by Fri 11 Dec 2026. Flag: Weak per-SKU numbers. Never 'Kitsch' in copy.
- E23 Pink robe with feather trim, one size: $59.99, 45% / 37%. Christmas order by Fri 11 Dec 2026. Flag: Splurge for this look. Never 'Viral Robe' in copy.
- E24 Cream hooded wearable blanket: $43.99, 45% / 34%. Christmas order by Fri 11 Dec 2026. Flag: Never 'Snuggie' in copy. TikTok deal price $4.65 is far under our floor; sell it as the cozy layer of the set.

## Order-by dates (OrderByDates sheet)

Formula: holiday date minus (supplier maximum quoted days + 2 handling + 3 buffer), moved back to the previous business day. CJ US warehouse quotes 1 to 3 days processing plus 3 to 6 days transit, so 9 days; the lead time is 14 calendar days for every product on the winner supplier. Results for all 40: Halloween **Fri 16 Oct 2026**, Christmas **Fri 11 Dec 2026**, New Year's Eve **Thu 17 Dec 2026**. No product's Christmas order-by date falls before 5 December, so nothing had to be moved out of the Christmas looks. The Zendrop backup (up to 11 days) would move Christmas to Wed 9 Dec; the AliExpress Choice last resort (15 days) is excluded from Q4 outright.

Carrier cutoffs for delivery by 25 December, from search snippets: USPS Ground Advantage Thu 17 Dec, Priority Mail Fri 18 Dec, Priority Mail Express Sat 19 Dec (USPS release of 22 Sep 2026, seen in snippet); FedEx Ground and Home Delivery 15 to 19 Dec by lane, Express Saver 21 Dec, 2Day 22 Dec, Overnight 23 Dec (fedex.com 2026 PDF, seen in snippet); UPS 2026 not published as of 22 Sep 2026, 2025 proxy Ground 16 to 18 Dec, 2nd Day Air 22 Dec, Next Day Air 23 Dec (unverified for 2026). The store's own order-by date (11 Dec) is earlier than every carrier cutoff, so the carrier dates never bind. These drive the D2 email calendar.

## Rejected candidates, one line each

123 candidates were gathered (Candidates sheet). 82 were not banked:

- Jewelry box / bracelet organiser (pink velvet or felt): Numeric signal exists but weaker than the 40 kept, or it duplicates a kept product in the same look.
- Silicone makeup sponge holder (pink): Numeric signal exists but weaker than the 40 kept, or it duplicates a kept product in the same look.
- Claw clip (pearl / rhinestone / jelly pink): Numeric signal exists but weaker than the 40 kept, or it duplicates a kept product in the same look.
- Satin hair bow clip (oversized, pink): Numeric signal exists but weaker than the 40 kept, or it duplicates a kept product in the same look.
- Satin pillowcase (blush / hot pink, ruffle edge): No numeric signal found (listings exist, counts not visible in snippets).
- Padded / preppy headband (pink, bow or pearl): No numeric signal found (listings exist, counts not visible in snippets).
- Microfiber hair towel wrap (pink): No numeric signal found (listings exist, counts not visible in snippets).
- Reusable satin-lined shower cap (pink): No numeric signal found (listings exist, counts not visible in snippets).
- Satin scrunchie set (pink, oversized): No numeric signal found (listings exist, counts not visible in snippets).
- Travel jewelry case (pink, small zip): No numeric signal found (listings exist, counts not visible in snippets).
- Hanging toiletry bag (pink): No numeric signal found (listings exist, counts not visible in snippets).
- Bath caddy tray: No numeric signal found (listings exist, counts not visible in snippets).
- Nail care kit without glue (files, buffers, cuticle tools, pink case): No numeric signal found (listings exist, counts not visible in snippets).
- Pink calming donut / raised dog bed: Bulky or heavy: inbound shipping pushes the price out of the Pink Finds band.
- Pink travel jewelry case (small zip organizer): Numeric signal exists but weaker than the 40 kept, or it duplicates a kept product in the same look.
- Pink paper heart garland (6 ft): Numeric signal exists but weaker than the 40 kept, or it duplicates a kept product in the same look.
- Galentine's party kit (pink plates, napkins, banner, straws): Numeric signal exists but weaker than the 40 kept, or it duplicates a kept product in the same look.
- Pink heart-shaped decor: heart pillow and heart-shaped tray: Numeric signal exists but weaker than the 40 kept, or it duplicates a kept product in the same look.
- Pink ruffle dog bandana with matching bow: Numeric signal exists but weaker than the 40 kept, or it duplicates a kept product in the same look.
- Pink plastic champagne flutes 5.5 oz, non-skid base (party pack): No numeric signal found (listings exist, counts not visible in snippets).
- Pink bow dog harness, collar and leash set: No numeric signal found (listings exist, counts not visible in snippets).
- Pink poop bag holder (velvet / strawberry / PU leather): No numeric signal found (listings exist, counts not visible in snippets).
- Pink pet carrier bag / bubble-window backpack: No numeric signal found (listings exist, counts not visible in snippets).
- Pink insulated wine tumbler 12 oz with lid: No numeric signal found (listings exist, counts not visible in snippets).
- Pink robe + slippers + headband spa gift set (no cosmetics): No numeric signal found (listings exist, counts not visible in snippets).
- Pink NYE decor: balloon garland, sequin table runner, disco ball ornaments, pink party hats: No numeric signal found (listings exist, counts not visible in snippets).
- Pink satin pajama set: Sized apparel: returns run well above the 8% allowance and Tommy Kate cannot wear blazers; kept for the Amazon pipeline, not the store.
- Pink luggage tag + passport holder set: No numeric signal found (listings exist, counts not visible in snippets).
- Pink stationery gift set, pink 1000-piece puzzle / game-night set, dog mom gift box: No numeric signal found before the search budget ran out (no signal, no product).
- Pink cow-print steering wheel cover: Numeric signal exists but weaker than the 40 kept, or it duplicates a kept product in the same look.
- Pink PU-leather full-set car seat covers (5 or 7 seat, airbag compatible): Bulky or heavy: inbound shipping pushes the price out of the Pink Finds band.
- Bling rhinestone pink car seat covers (full set): Bulky or heavy: inbound shipping pushes the price out of the Pink Finds band.
- 43-piece fuzzy pink car interior set (seat covers + steering + belt + handbrake covers): Bulky or heavy: inbound shipping pushes the price out of the Pink Finds band.
- Pink floral quilted car storage basket / back-seat organizer: Numeric signal exists but weaker than the 40 kept, or it duplicates a kept product in the same look.
- Pink car floor mats (polka-dot bow print or bling leather 4-5 pc set): Numeric signal exists but weaker than the 40 kept, or it duplicates a kept product in the same look.
- Pink snow brush + ice scraper (car winter kit): Numeric signal exists but weaker than the 40 kept, or it duplicates a kept product in the same look.
- Wavy / wave-shaped wall mirror (no lights): Bulky or heavy: inbound shipping pushes the price out of the Pink Finds band.
- Pink laundry basket / hamper (large woven or on wheels): Bulky or heavy: inbound shipping pushes the price out of the Pink Finds band.
- Coffee syrup pump dispensers (pink, fits 750ml bottles): Numeric signal exists but weaker than the 40 kept, or it duplicates a kept product in the same look.
- Bow glass cup 16oz with bamboo lid and glass straw (pink, set of 2): Numeric signal exists but weaker than the 40 kept, or it duplicates a kept product in the same look.
- Pink stick-on bathroom caddy set (5-pack, stainless, toothbrush + soap holder): Numeric signal exists but weaker than the 40 kept, or it duplicates a kept product in the same look.
- Pink bow bedding / duvet set: Bulky or heavy: inbound shipping pushes the price out of the Pink Finds band.
- Small fluffy pink bedroom / bedside rug: Bulky or heavy: inbound shipping pushes the price out of the Pink Finds band.
- 12-in-1 pink silicone kitchen utensil set: Numeric signal exists but weaker than the 40 kept, or it duplicates a kept product in the same look.
- Pastel pink wall shelf (dorm / vanity): Bulky or heavy: inbound shipping pushes the price out of the Pink Finds band.
- Pink car tissue box holder (visor / armrest): No numeric signal found (listings exist, counts not visible in snippets).
- Flower / daisy car vent clips (decorative, unscented holder, set of 4): No numeric signal found (listings exist, counts not visible in snippets).
- Pink bow car headrest neck pillows (2-pack): No numeric signal found (listings exist, counts not visible in snippets).
- Pink bow throw pillow / bow-shaped cushion: No numeric signal found (listings exist, counts not visible in snippets).
- Pink bow flannel throw blanket (coquette print): No numeric signal found (listings exist, counts not visible in snippets).
- Pink bow and hearts ceramic mug (11/15oz): No numeric signal found (listings exist, counts not visible in snippets).
- Pink bows & hearts soap dispenser / pink glass 16oz soap dispenser: No numeric signal found (listings exist, counts not visible in snippets).
- Bow-shaped pink wax melts / pink bow candle: No numeric signal found (listings exist, counts not visible in snippets).
- Pink apron + oven mitt set: No numeric signal found (listings exist, counts not visible in snippets).
- Pink checkerboard rug: Bulky or heavy: inbound shipping pushes the price out of the Pink Finds band.
- Pink entryway tray and wall hooks; pink car emergency kit; velvet/boucle pink cushions; pink diffuser: No numeric signal found before the search budget ran out (no signal, no product).
- Pink desk mat + keyboard wrist rest + mouse wrist rest 3-piece set: Numeric signal exists but weaker than the 40 kept, or it duplicates a kept product in the same look.
- Pink 40 oz tumbler accessories kit (bow straw topper, letter charms, silicone boot): Numeric signal exists but weaker than the 40 kept, or it duplicates a kept product in the same look.
- Pink knit cardigan (office layer, oversized or wrap style): Sized apparel: returns run well above the 8% allowance and Tommy Kate cannot wear blazers; kept for the Amazon pipeline, not the store.
- Pink cropped blazer: Sized apparel: returns run well above the 8% allowance and Tommy Kate cannot wear blazers; kept for the Amazon pipeline, not the store.
- Pink 2026 planner / mini weekly planner with PU leather cover: Numeric signal exists but weaker than the 40 kept, or it duplicates a kept product in the same look.
- Pink leopard / pink glitter retractable badge reel with card holder: No numeric signal found (listings exist, counts not visible in snippets).
- Pink laptop stand (aluminium or acrylic riser, no electronics): Numeric signal exists but weaker than the 40 kept, or it duplicates a kept product in the same look.
- Pink office / pink desk aesthetic (category-level demand signal, use for list titles): Category signal only, used for look titles, not a product.
- NO-SIGNAL SECTION: pink loafers; satin padded pink headband; pearl hair claw / pearl bow clip; pink wide-leg work trousers; pink insulated bottle (non-40oz); pink acrylic file holder / magazine rack; pink highlighter set; pink hardcover notebook / journal; pink pen cup alone; certified pink keyboard/mouse; certified plug-in pink desk lamp: No numeric signal found before the search budget ran out (no signal, no product).
- Pink matching Christmas pajamas (women's / family sets, plain pink or pink candy-stripe): Sized apparel: returns run well above the 8% allowance and Tommy Kate cannot wear blazers; kept for the Amazon pipeline, not the store.
- Pink bow pumpkin (resin or foam pumpkin with oversized satin bow): No numeric signal in any source (listings exist, counts not visible); Halloween order-by dates also fall before a store can be live.
- Pink ghost hanging decor set (6-pack pastel ghosts / garland): No numeric signal in any source (listings exist, counts not visible); Halloween order-by dates also fall before a store can be live.
- Pink Halloween ghost doormat (coir, 'boo' or pink bow ghost): No numeric signal in any source (listings exist, counts not visible); Halloween order-by dates also fall before a store can be live.
- Pink ruffle / pastel ghost trick-or-treat bucket (adult 'candy bucket' or party bowl): No numeric signal in any source (listings exist, counts not visible); Halloween order-by dates also fall before a store can be live.
- Pink cat ears headband (fluffy or satin, with optional tail clip): No numeric signal in any source (listings exist, counts not visible); Halloween order-by dates also fall before a store can be live.
- Pink cowgirl hat (felt or sequin, adult): No numeric signal in any source (listings exist, counts not visible); Halloween order-by dates also fall before a store can be live.
- Pink sequin mini dress (Halloween / NYE party): Sized apparel: returns run well above the 8% allowance and Tommy Kate cannot wear blazers; kept for the Amazon pipeline, not the store.
- Pink witch hat (satin/velvet, adult): No numeric signal in any source (listings exist, counts not visible); Halloween order-by dates also fall before a store can be live.
- Pink skeleton garland / pink spiderweb (tabletop or mantel): No numeric signal in any source (listings exist, counts not visible); Halloween order-by dates also fall before a store can be live.
- Pink Halloween pillow covers / tablecloth (retro ghost and pumpkin print): No numeric signal in any source (listings exist, counts not visible); Halloween order-by dates also fall before a store can be live.
- Pink Halloween car hanging ghost charms (rear-view mirror set): Bulky or heavy: inbound shipping pushes the price out of the Pink Finds band.
- Pink pumpkin ceramic mug (11 oz, pink pumpkin / pink ghost print or 3D pumpkin shape): No numeric signal in any source (listings exist, counts not visible); Halloween order-by dates also fall before a store can be live.
- Pink plaid / checkered throw blanket (fall cozy): No numeric signal found (listings exist, counts not visible in snippets).
- Pink nutcracker figurine (pastel, ballet-inspired, 12-14 in): No numeric signal found (listings exist, counts not visible in snippets).
- Pink Christmas wreath / pink tree skirt / pink wrapping paper and ribbon: No numeric signal found (listings exist, counts not visible in snippets).
- Pink Christmas mug / pink candy cane decor / pink advent calendar (non-cosmetic) / pink Christmas car bow: No numeric signal found (listings exist, counts not visible in snippets).

## Every figure not confirmed (and where to confirm it)

- Every supplier product cost and shipping cost (Suppliers sheet, columns F to J): estimates from the retail price seen, the Zendrop and CJ shipping bands, and the USPS 2026 rate file. Confirm each on cjdropshipping.com (US warehouse filter) or app.zendrop.com (Ships From: US), signed in. Four rows have a seen supplier price: AliExpress $6.79 (desk organizer), $11.50 (pearl brush holder), $30.50 (monitor riser, likely including shipping); CJ listing prices were not visible in any snippet.
- Every supplier's warehouse country, stock, MOQ, packaging and return terms (Suppliers sheet, columns L to O): stated from the supplier's published policy, not from the listing. Confirm per listing.
- Retail prices "seen": TikTok Shop deal prices and Amazon "bought in past month" bands come from search snippets and change daily.
- ASINsight monthly sales estimates (desk mat, tumbler, tote, laptop sleeve) are a third-party estimate of Amazon sales, not Amazon data.
- Pinterest and Etsy trend percentages for bows (+200%, +120%) were quoted by trend press; the original article could not be opened.
- Google Trends "vanity bag" 206K a month, +66% YoY: quoted by CJ's blog, not read on trends.google.com.
- Shopify Basic $39/$29, the $1-for-3-months offer, Shopify Payments 2.9% + 30c, Shopify Tax 0.35% and the $75/$150 filing fees, Zendrop, Spocket, AutoDS, DSers and Stripe prices: all from snippets of help pages and 2026 review sites; confirm on each company's pricing page.
- Shopify Tax lifetime threshold for stores created on or after 13 May 2026: not seen.
- UPS 2026 holiday schedule: not published; 2025 used as proxy.
- Georgia "free registration" and "4% state rate": third-party pages only.
- General liability insurance cost, food-contact rules for the tumbler and cups, CPSIA scope: not searched.
- Pinterest: whether a new domain on the same account inherits the block on thedigitalincomeedit.com: not found.

## Platform and legal sources

See `PLATFORM_RECOMMENDATION.md` and `LEGAL_SETUP_CHECKLIST.md`; every fact there carries its URL and date. The raw research notes are in the session scratchpad and were not committed.

## Files

- `PRODUCT_BANK.xlsx`: Candidates, Suppliers, Margins (assumptions in blue at the top; formulas live), Bank40, OrderByDates. Cached values are baked in so it reads on a phone; Excel and Numbers recalculate on open. (LibreOffice in this container could not open files, so the cached values were computed in Python and checked against the sheet's formulas by hand on row Q01.)
- `looks/<slug>.json` (7): lifestyle page drafts in the `src/lifestyle/README.md` format, `link` and `ideaList` set to STORE_PENDING, `season` set. NOT in `src/lifestyle/`.
- `looks/<slug>.copy.md` (7): flat lay or collage prompt, Tommy Kate lifestyle prompt, two pins each (title, description, alt, all inside the limits), @itstommykate caption, cross-link line, and the product page copy for every product in the look (title under 60, 40-word description, three bullets, shipping window, returns line, sold-by line, image alt, tags).
- `PLATFORM_RECOMMENDATION.md`, `LEGAL_SETUP_CHECKLIST.md`, this `REPORT.md`.
- `ops/cloud-output/DESKTOP_FINISH_QUEUE.md`, section 4 (DROPSHIP).

This matches `ops/canon/canon.json` (no product, price or link in canon was touched; the Shopify affiliate link and Decision 83's US-warehouse rule are followed) and `ops/cloud-kit/README_START_HERE.md`. The one line that does not match a source is the price band, flagged above, because the growth plan copy in the repo does not carry one.
