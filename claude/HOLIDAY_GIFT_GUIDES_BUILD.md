# TDIE HOLIDAY GIFT GUIDES BUILD

### Built 26 September 2026 in a cloud session. Branch `claude/tdie-holiday-gift-guides-y2c7l4`. 25 looks, 50 images, 50 pins, 25 Instagram posts.

**Sources read before writing:** `claude/CLAUDE_SOURCE_CHECK_RULE.md`, `claude/TDIE_IMAGE_GENERATION_MASTER.md`, `claude/TDIE_DESIGN_RULES.md`, `claude/TDIE_LEGALLY_BLONDE_PIN_FACTORY.md`, `claude/LB_PIN_LOG.md`, `ops/canon/canon.json`, `ops/canon/TDIE_CANON.md`, `src/lifestyle/README.md`, the tdie-image-prompt skill.

**Not read, because they were not available to this session:** `claude/TDIE_TOMMY_KATE_VOICE.md` (the Instagram captions follow factory section 8d but are unverified against the voice file), `claude/TDIE_CHATGPT_IMAGE_BRIEF.md` (the prompts use only the named props the Master file itself spells out: the glitter tumbler, candy pink headphones, candy pink garden gloves), `claude/TDIE_LIFESTYLE_LIST_MAP.md` and `claude/TDIE_BROWSER_LOCK.md`.

**Status:** everything that does not need Jodie's signed-in accounts is done. The 25 look files are committed with `"draft": true`, so none of them shows on the site until its links and images are in. What is still open is the Amazon sourcing, the Idea Lists, the SiteStripe links and the 50 images (section 6), then the finish and live check (section 7).

---

## 1. What is in the repo now

- `src/lifestyle/<slug>.json` for all 25 looks. Each has the page title, intro, the items in order (with empty `link` fields), empty `ideaList`, both image file names and alt text, `"giftGuide": true`, `"guide": <1 to 25>`, a short `"label"` for the hub, and `"draft": true`.
- `src/data/lifestyle.js`: looks with `"draft": true` are skipped by the build (a second lock on top of the existing "no images or no links, no page" rule). New export `GIFT_GUIDES`: live looks with `giftGuide`, in `guide` order.
- `/lifestyle` hub: a **Holiday Gift Guides** block under the intro. It has a blush-to-cream panel, the kicker "The Holiday Edit · 2026", a row of chips (For Her, For Mom, For Teen Girls...) jumping to each guide, and a numbered grid (No. 01 to No. 25) using each look's lifestyle photo. It only appears once at least one guide is live, and it grows as each one goes live.
- Look pages: a gift guide's "More" row shows other holiday gift guides instead of the same category.
- **No prices on gift guides:** the Membership card at the bottom of every Lifestyle page shows the monthly price after "Start with Membership Standard". On gift guide pages and on the Gift Guides category page it now reads "Start with Membership Standard", with the price left off. Every other Lifestyle page is unchanged.
- `claude/HOLIDAY_GIFT_GUIDES_LINKS.md`: the empty table the sourcing run fills (item, ASIN, SiteStripe short link, Idea List URL). I apply it to the JSON files afterwards.
- This file.

## 2. Calls made on your behalf (must-know)

1. **The pink rule follows `TDIE_IMAGE_GENERATION_MASTER.md` section 4 (your 26 Sep correction), not the build brief's "exactly one pink object in every photograph."** The brief says to follow the Master file exactly, and the Master file's newer rule covers every image here. Lifestyle images with Tommy Kate carry her glitter tumbler plus other pink pieces. The flat lays and collages are person-free product pins, so they follow factory section 4 and are as pink as the look. None of the 50 images is a person-free, non-product frame, so the one-object limit applies to none of them.
2. **Flat lay pins keep their generated title on the image.** This is Decision 109 in canon, and it is a scoped exception to the brief's "no text in images". The 25 lifestyle photos carry no text at all.
3. **Two images per look, and both do double duty:** each is one of the look's two pins and one of the two photos on its page. Factory section 2 treats theme lists as flat lay only, but the brief asks for two pins per look, so every look gets a lifestyle pin too. Section 2 allows this ("Tommy Kate in that space using the items").
4. **Pin dates follow factory section 10.** Hostess Gifts goes on 12 Nov inside the Thanksgiving window, where "hostess gift list" is already in the idea bank. The other 24 run from 20 Nov to 17 Dec in the Christmas and gift guide window, one look a day. The top-demand lists land before Black Friday (27 Nov) and Cyber Monday (30 Nov). Five days stay free for the evergreen looks section 10b requires every week. The pages go live by 31 Oct, so Google has them weeks before the pins start.
5. **The books look names no titles.** Its two book slots say "pick a current bestseller she hasn't read" and are chosen when sourcing, because this session cannot check what is in stock. Book covers are unprinted in both image prompts.
6. **Item names are shopping briefs.** When the real product is chosen, its short name replaces the brief's wording in the JSON. I do this from the links table.
7. **Instagram:** one feed post per look, as the brief asked. No Stories are written, because the brief says no links anywhere on Instagram. Factory section 8d still allows Story link stickers (Decision 117), so say if you want Stories added.
8. **Site-wide, not changed here:** the site's heading font token (`--display`) is still Fraunces. `TDIE_DESIGN_RULES.md` retires Fraunces for headings. The new hub block uses the site's own heading token so it matches the rest of the page. The canon edits the Design Rules list as still owed are still owed.

## 2a. How the last six looks were chosen

Amazon's own search autocomplete and Google Trends are both blocked from this cloud container (network policy), so no Amazon-side search volume was read. **That part is unverified.** The six were picked from the published search data below, all from the 2025 season, to fill gaps the first 19 leave. Before sourcing, type "gifts for" into Amazon's search bar on your desktop. If a pick below does not show up in the suggestions, say so and I will swap it.

| # | Look | Why | Source |
|---|---|---|---|
| 20 | Gifts for Mom | Relationship searches ("presents for mom", "gifts for best friends") are named among the highest-intent gift keywords. The first 19 had no mom list, only new moms. | [V9 Digital, gift keywords](https://www.v9digital.com/insights/gift-related-keywords-for-your-ecommerce-holiday-campaign/), [Fire&Spark](https://www.fireandspark.com/blog/seo-for-gift-products/) |
| 21 | Gifts for Your Best Friend | Same source, "gifts for best friends". A buy-two list fits the pink girls'-girl voice. | [V9 Digital](https://www.v9digital.com/insights/gift-related-keywords-for-your-ecommerce-holiday-campaign/) |
| 22 | Teacher Christmas Gifts | Pinterest reported "teacher Christmas gift ideas" searches up 1,890% for holiday 2025. | [ListenFirst, Pinterest holiday 2025](https://www.listenfirstmedia.com/a-pinterest-holiday-strategy-2025/) |
| 23 | Pink Travel Gifts | Pinterest reported "traveler's journals" up 610% and "mini travel essentials" up 80% for holiday 2025. | [ListenFirst](https://www.listenfirstmedia.com/a-pinterest-holiday-strategy-2025/) |
| 24 | Bag Charms and Accessory Gifts | Google's Holiday 100 (search trends, May to Sep 2025) named backpack charms and crescent bags among the top trending gifts. The same list says stacking ring searches doubled, which is used in Jewelry, and home projector searches rose, which is used in White Elephant. | [CNN on Google Holiday 100](https://www.cnn.com/cnn-underscored/gifts/google-holiday-100-gifts-2025), [WISN](https://www.wisn.com/article/trending-gifts-2025-google-holiday-100/69239844) |
| 25 | Snail Mail and Stationery Gifts | Pinterest Predicts 2026: "snail mail gifts" up 110%, "cute stamps" up 105%, "handwritten letters" up 45%. | [Pinterest Newsroom](https://newsroom.pinterest.com/news/pinterest-predicts-nonconformity-self-preservation-and-escapism-drive-21-trends-for-2026/), [Pinterest Predicts](https://business.pinterest.com/pinterest-predicts/) |

Also checked and left out: "wellness gifts" (Pinterest, up 54%) is already covered by Self-Care Night In; "gifts for men" and "budget gifts for boyfriend" are off-audience for a pink women's storefront; toys are Amazon's own Top 100 territory.


## 3. The 25 looks at a glance

| # | Look | Page slug | Category | Board | Flat lay pin | Lifestyle pin | Instagram |
|---|---|---|---|---|---|---|---|
| 1 | For Her | `pink-gifts-for-her` | gifts | LB > Christmas and Gift Guides | Fri 20 Nov 2026 13:30 | Mon 23 Nov 2026 20:30 | Fri 20 Nov 2026 19:00 |
| 2 | For Teen Girls | `gifts-for-teen-girls-who-love-pink` | gifts | LB > Christmas and Gift Guides | Sun 22 Nov 2026 13:30 | Wed 25 Nov 2026 20:30 | Sun 22 Nov 2026 19:00 |
| 3 | For College Girls | `pink-dorm-gifts-for-college-girls` | dorm | Home > Christmas and Gift Guides | Tue 1 Dec 2026 13:30 | Fri 4 Dec 2026 20:30 | Tue 1 Dec 2026 19:00 |
| 4 | For Coworkers | `cute-coworker-christmas-gifts` | gifts | LB > Christmas and Gift Guides | Thu 3 Dec 2026 13:30 | Sun 6 Dec 2026 20:30 | Thu 3 Dec 2026 19:00 |
| 5 | Stocking Stuffers | `pink-stocking-stuffers-for-women` | gifts | LB > Christmas and Gift Guides | Tue 24 Nov 2026 13:30 | Fri 27 Nov 2026 20:30 | Tue 24 Nov 2026 19:00 |
| 6 | Pink Christmas Decor | `pink-christmas-home-decor` | home-decor | Home > Christmas and Gift Guides | Sat 28 Nov 2026 13:30 | Tue 1 Dec 2026 20:30 | Sat 28 Nov 2026 19:00 |
| 7 | Cozy Pajamas | `cozy-pink-christmas-pajamas` | clothing | LB > Christmas and Gift Guides | Mon 30 Nov 2026 13:30 | Thu 3 Dec 2026 20:30 | Mon 30 Nov 2026 19:00 |
| 8 | Beauty and Perfume | `beauty-and-perfume-gift-sets` | perfume | LB > Christmas and Gift Guides | Thu 26 Nov 2026 13:30 | Sun 29 Nov 2026 20:30 | Thu 26 Nov 2026 19:00 |
| 9 | Car Accessories | `pink-car-accessories-gifts` | car | Home > Christmas and Gift Guides | Tue 8 Dec 2026 13:30 | Fri 11 Dec 2026 20:30 | Tue 8 Dec 2026 19:00 |
| 10 | Jewelry | `pink-jewelry-gifts-for-her` | jewelry | LB > Christmas and Gift Guides | Fri 27 Nov 2026 13:30 | Mon 30 Nov 2026 20:30 | Fri 27 Nov 2026 19:00 |
| 11 | Books | `books-to-gift-this-christmas` | books | Home > Christmas and Gift Guides | Mon 7 Dec 2026 13:30 | Thu 10 Dec 2026 20:30 | Mon 7 Dec 2026 19:00 |
| 12 | Hostess Gifts | `pretty-hostess-gifts` | gifts | LB > Thanksgiving | Thu 12 Nov 2026 13:30 | Sun 15 Nov 2026 20:30 | Thu 12 Nov 2026 19:00 |
| 13 | New Moms | `gifts-for-new-moms` | gifts | LB > Christmas and Gift Guides | Sat 12 Dec 2026 13:30 | Tue 15 Dec 2026 20:30 | Sat 12 Dec 2026 19:00 |
| 14 | Dog Lovers | `gifts-for-dog-moms` | gifts | LB > Christmas and Gift Guides | Sat 5 Dec 2026 13:30 | Tue 8 Dec 2026 20:30 | Sat 5 Dec 2026 19:00 |
| 15 | Gamer Girls | `pink-gaming-gifts-for-girl-gamers` | gifts | LB > Christmas and Gift Guides | Sun 29 Nov 2026 13:30 | Wed 2 Dec 2026 20:30 | Sun 29 Nov 2026 19:00 |
| 16 | Self-Care Night In | `self-care-night-in-gift-ideas` | beauty | LB > Christmas and Gift Guides | Tue 15 Dec 2026 13:30 | Fri 18 Dec 2026 20:30 | Tue 15 Dec 2026 19:00 |
| 17 | Party Outfits | `pink-holiday-party-outfits` | clothing | LB > Christmas and Gift Guides | Thu 10 Dec 2026 13:30 | Sun 13 Dec 2026 20:30 | Thu 10 Dec 2026 19:00 |
| 18 | Pink Holiday Table | `pink-christmas-table-decor` | home-decor | Home > Christmas and Gift Guides | Thu 17 Dec 2026 13:30 | Sun 20 Dec 2026 20:30 | Thu 17 Dec 2026 19:00 |
| 19 | White Elephant | `cute-white-elephant-gifts` | gifts | LB > Christmas and Gift Guides | Fri 11 Dec 2026 13:30 | Mon 14 Dec 2026 20:30 | Fri 11 Dec 2026 19:00 |
| 20 | For Mom | `pink-gifts-for-mom` | gifts | LB > Christmas and Gift Guides | Sat 21 Nov 2026 13:30 | Tue 24 Nov 2026 20:30 | Sat 21 Nov 2026 19:00 |
| 21 | Best Friend | `gifts-for-best-friend` | gifts | LB > Christmas and Gift Guides | Mon 23 Nov 2026 13:30 | Thu 26 Nov 2026 20:30 | Mon 23 Nov 2026 19:00 |
| 22 | Teachers | `teacher-christmas-gifts` | gifts | LB > Christmas and Gift Guides | Fri 4 Dec 2026 13:30 | Mon 7 Dec 2026 20:30 | Fri 4 Dec 2026 19:00 |
| 23 | Travel Gifts | `pink-travel-gifts-for-her` | accessories | LB > Christmas and Gift Guides | Sun 13 Dec 2026 13:30 | Wed 16 Dec 2026 20:30 | Sun 13 Dec 2026 19:00 |
| 24 | Bag Charms | `trendy-bag-charms-and-accessory-gifts` | accessories | LB > Christmas and Gift Guides | Sun 6 Dec 2026 13:30 | Wed 9 Dec 2026 20:30 | Sun 6 Dec 2026 19:00 |
| 25 | Snail Mail | `snail-mail-stationery-gifts` | gifts | LB > Christmas and Gift Guides | Mon 14 Dec 2026 13:30 | Thu 17 Dec 2026 20:30 | Mon 14 Dec 2026 19:00 |

LB = `Legally Blonde Outfits | Pink Amazon Fashion`. Home = `Pink Home, Dorm and Car Finds | Amazon`. All times Eastern. Evergreen days left open for recipe section 10b: Wed 25 Nov, Wed 2 Dec, Wed 9 Dec, Wed 16 Dec and Fri 18 Dec.


## 4. Every look in full


---

### 1. For Her

**Page:** `/lifestyle/pink-gifts-for-her` · category `gifts` · season `Holiday` · file `src/lifestyle/pink-gifts-for-her.json` (committed, `draft: true`)

**Page title (H1):** Pink Gifts for Her (Even If She Has Everything)

**Intro:** She says she doesn't need anything. She is lying, and she would love a faux fur throw she didn't have to buy for herself. Every pick here is something she would use daily and never splurge on, which is the whole trick to shopping for the woman who has everything.

**Items to source (the page lists them in this order):**

1. Blush pink faux fur throw blanket · note on page: "The one she steals back from the dog."
2. Pink mulberry silk pillowcase · note on page: "Better hair mornings, zero effort."
3. Scented candle in a ceramic vessel · note on page: "Cozy, not sugary."
4. Cashmere blend lounge socks · note on page: "For cold kitchen floors in December."
5. Gold initial pendant necklace · note on page: "Dainty enough to never take off."
6. Glitter pink insulated tumbler with straw · note on page: "Iced coffee in December is a personality."
7. Pink velvet travel jewelry case · note on page: "Where the necklace lives when she travels."

**Idea List:** title `Pink Gifts for Her (Even If She Has Everything)` · description: She says she doesn't need anything. Every piece is linked here.

**Image 1, `pink-gifts-for-her-flatlay.jpg` (no person, Format A):** Seedream 4.5 on Higgsfield, Unlimited ON, 4K, portrait 2:3. Attach (1) Command Centre `stylerefs` doc `sr-pink-dress-flatlay`, (2) this look's product sheet. Garbled or soft title letters: re-run on Nano Banana Pro 2K. Colour follows factory section 4 (as pink as the look).

```
Using the first image as a style reference for the styling, the fullness and the title lettering, not an exact copy, please make me a very realistic overhead flat lay photo of the products in the second image. I can't use the exact Amazon images outside of Amazon, so this needs to be a new photo. Shot straight down, portrait 2:3, like a good-quality photo taken on a phone. The gifts are arranged as one abundant styled group, pieces overlapping and touching, on a chunky cream knit throw: blush pink faux fur throw blanket, pink mulberry silk pillowcase, scented candle in a ceramic vessel, cashmere blend lounge socks, gold initial pendant necklace, glitter pink insulated tumbler with straw, pink velvet travel jewelry case. Each item matches its screenshot in colour, shape and detail. Tucked in around them, filling the frame edge to edge with almost no empty background: a small bunch of pink tulips, an iced latte in a clear glass, a satin hair bow, a sprig of fresh pine and a small gift box wrapped in cream paper. Every product sits fully inside the frame. Soft natural window light, gentle real shadows, visible fabric texture, true-to-life materials, small real-life imperfections, photorealistic real-world photography. Across the upper third, set directly on the photo, a large two-style title: "GIFTS FOR HER" in a bold high-contrast serif in capitals, with "cozy pink" beneath it in a thick flowing brush script, both in near-black, perfectly spelled, sharp edges, high contrast, filling about two thirds of the width. No logos, no brand names, no labels or printing on products or packaging, no watermark, no person, no other text.
```

**Image 2, `pink-gifts-for-her-lifestyle.jpg` (Tommy Kate, candid full shot):** Google Gemini first; Nano Banana Pro 2K on Higgsfield if Gemini is out or the result fails. Attach (1) style reference `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/src/lifestyle/pink-cat-halloween-costume-lifestyle.jpg`, (2) the Omni seed `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/public/images/library/avatar-seed-omni-reference.png` as a JPEG under 400 KB, (3) this look's product sheet.

```
Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference. The reference sheet is the second image. Using the first image as a style reference, not an exact copy, please make me one single very realistic lifestyle photo, not a collage or grid. I can't use the exact Amazon images, so this is a new photo of the products in the third image, each matching its screenshot in colour and detail. Setting: the white slipcovered sofa in her farmhouse living room on a December morning, the Christmas tree with warm white lights and wooden ornaments behind her, her golden retriever asleep on the rug. She is curled into the corner of the sofa, pulling the blush faux fur throw over her knees and laughing softly as she lifts the lid of the pink velvet jewelry case to find the gold initial necklace. She is wearing an oversized cream cable knit sweater, candy pink lounge pants and cashmere lounge socks. Her hair is twisted up loosely in a claw clip. Nails: soft pink. Her glitter-flecked pink iced coffee tumbler with a lavender straw, saturated candy pink, never pale, is on the side table at her elbow. Other pink in the frame: the candy pink lounge pants and a pink silk pillowcase on a sofa cushion; pink clothes and other pink pieces are welcome alongside the tumbler. The register is quiet wealth, lived in: a real farmhouse that is nice but never showy, clean but not sterile, with small signs of a real life. Format: candid full shot. Her face is visible in a candid, natural moment, not posed to the camera. The main subject sits in the right third of the frame with calmer negative space on the left, natural perspective and believable scale. Portrait 2:3. Light: soft morning window light from a tall farmhouse window on the left. Shot on a mirrorless camera with a 50mm lens at f/2, natural depth of field and soft natural bokeh, photorealistic, real-world photography, true-to-life textures, real skin and fabric texture, natural imperfections, nothing glossy. No lettering, no signs, no logos, no text anywhere in the frame, no brand marks on any product. Not a Paris apartment, cafe, marble room, mansion or influencer studio.
```

**Site alt text:** flat lay: Overhead flat lay on a cream knit of a blush faux fur throw, pink silk pillowcase, candle, lounge socks, gold initial necklace, pink glitter tumbler and a velvet jewelry case. · lifestyle: Woman curled on a white farmhouse sofa by a Christmas tree under a blush faux fur throw, opening a pink velvet jewelry case, golden retriever asleep on the rug.

**Pin 1, flat lay** · Fri 20 Nov 2026 13:30 ET · board `Legally Blonde Outfits | Pink Amazon Fashion` > section `Christmas and Gift Guides` · link: this look's Idea List (`https://www.amazon.com/shop/thedigitalincomeedit/list/<id>`) · AI label ON

- Overlay (on the image): GIFTS FOR HER / cozy pink
- Title: Gifts for Her That She'll Actually Use: Cozy Pink Finds for the Woman Who Has Everything
- Description: Gifts for her that she will actually use, even if she swears she has everything: a blush faux fur throw, a pink silk pillowcase, a cozy candle, cashmere lounge socks, a gold initial necklace, a glitter pink tumbler and a velvet jewelry case. The rule is simple. Buy the nice version of something she uses daily and would never buy herself. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #giftsforher #christmasgiftideas #pinkaesthetic
- Alt text: Overhead flat lay on a cream knit of a blush faux fur throw, pink silk pillowcase, candle, lounge socks, gold initial necklace, pink glitter tumbler and a velvet jewelry case.

**Pin 2, lifestyle** · Mon 23 Nov 2026 20:30 ET · same board and section · same Idea List link · AI label ON, "includes an AI-generated person" ticked

- Title: Cozy Christmas Gift Ideas for Women: Faux Fur Throw, Initial Necklace and Silk Pillowcase
- Description: Cozy Christmas gift ideas for women who love a slow morning: a blush faux fur throw, a gold initial necklace in a velvet case, a pink silk pillowcase and lounge socks for cold farmhouse floors. Tree lights on, dog asleep, iced coffee in hand, obviously. Save this for the person who is impossible to shop for. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #giftsforwomen #cozygifts #christmasgifts #giftsforher
- Alt text: Woman curled on a white farmhouse sofa by a Christmas tree under a blush faux fur throw, opening a pink velvet jewelry case, golden retriever asleep on the rug.

**Instagram @itstommykate feed post** · Fri 20 Nov 2026 19:00 ET · carousel: lifestyle photo first, flat lay second · AI label ON · check the caption panel says `itstommykate` before Share

```
told everyone I didn't need anything this year. then I opened a faux fur throw and a little velvet box with my initial in it and immediately changed my mind 🎀 the whole cozy list is linked in my Amazon storefront (link in bio) #ad #giftsforher #giftideas
```


---

### 2. For Teen Girls

**Page:** `/lifestyle/gifts-for-teen-girls-who-love-pink` · category `gifts` · season `Holiday` · file `src/lifestyle/gifts-for-teen-girls-who-love-pink.json` (committed, `draft: true`)

**Page title (H1):** Gifts for Teen Girls Who Love Pink

**Intro:** Teen girls can smell a gift picked by an adult from across the room. This list is the stuff she is already screenshotting: lip oil, a claw clip set, a bow bag charm, a quilted puffer tote and the fuzzy slides she will wear to school if you let her. Cool aunt status, secured.

**Items to source (the page lists them in this order):**

1. Pink tinted lip oil set · note on page: "The one she keeps in every bag."
2. Claw clip set in pinks and cream
3. Pink quilted puffer tote bag · note on page: "Fits the laptop, the snacks and the drama."
4. Beaded bow bag charm
5. Fuzzy pink slide slippers
6. Photo clip string lights · note on page: "For the wall of pictures she keeps adding to."
7. Satin scrunchie set

**Idea List:** title `Gifts for Teen Girls Who Love Pink` · description: Teen girls can smell a gift picked by an adult from across the room. Every piece is linked here.

**Image 1, `gifts-for-teen-girls-who-love-pink-flatlay.jpg` (no person, Format B):** Seedream 4.5 on Higgsfield, Unlimited ON, 4K, portrait 2:3. Attach (1) Command Centre `stylerefs` doc `sr-that-girl-amazon-finds-blush`, (2) this look's product sheet. Garbled or soft title letters: re-run on Nano Banana Pro 2K. Colour follows factory section 4 (as pink as the look).

```
Using the first image as a style reference for the layout, the fullness and the title lettering, not an exact copy, please make me a "that girl" shoppable Amazon finds collage for Pinterest, portrait 2:3, on a soft pale lilac background with a faint paper texture. I can't use the exact Amazon images outside of Amazon, so please create a new clean cut-out product photo of each item in the second image, each with a soft drop shadow: pink tinted lip oil set, claw clip set in pinks and cream, pink quilted puffer tote bag, beaded bow bag charm, fuzzy pink slide slippers, photo clip string lights, satin scrunchie set. Add heart shaped sunglasses, a small plush bunny, stacked gold rings and a satin hair bow. Pack them around a central title so the whole canvas is full edge to edge, items overlapping slightly, every product fully inside the frame. Add a few tiny accents: small hearts, little sparkles and one small bow. In the middle, set directly on the background, a large two-style title: "TEEN GIRL" in a bold high-contrast serif with "gift list" in a thick flowing brush script, deep plum, perfectly spelled, crisp and fully legible, filling about half the width. Each item matches its screenshot in colour, shape and detail and looks like a real photo, not a render, with true-to-life materials. No logos, no brand names, no labels or printing on products or packaging, no prices, no person, no other text.
```

**Image 2, `gifts-for-teen-girls-who-love-pink-lifestyle.jpg` (Tommy Kate, mirror selfie):** Google Gemini first; Nano Banana Pro 2K on Higgsfield if Gemini is out or the result fails. Attach (1) style reference `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/src/lifestyle/pink-suit-law-student-halloween-costume-lifestyle.jpg`, (2) the Omni seed `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/public/images/library/avatar-seed-omni-reference.png` as a JPEG under 400 KB, (3) this look's product sheet.

```
Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference. The reference sheet is the second image. Using the first image as a style reference, not an exact copy, please make me one single very realistic lifestyle photo, not a collage or grid. I can't use the exact Amazon images, so this is a new photo of the products in the third image, each matching its screenshot in colour and detail. Setting: the full-length mirror in the upstairs farmhouse guest bedroom, a white iron bed with a pink gingham quilt behind her and photo clip string lights glowing on the wall, in December. She takes a mirror selfie with a plain phone case held up so the phone covers her face, the pink quilted puffer tote on her shoulder with the beaded bow charm hanging from the strap. She is wearing an oversized candy pink hoodie, cream wide leg sweatpants and fuzzy pink slide slippers. Her hair is twisted up in a cream claw clip. Nails: short glossy pink. Her glitter-flecked pink iced coffee tumbler with a lavender straw, saturated candy pink, never pale, is in her free hand. Other pink in the frame: the candy pink hoodie, the pink puffer tote and the pink gingham quilt; pink clothes and other pink pieces are welcome alongside the tumbler. The register is quiet wealth, lived in: a real farmhouse that is nice but never showy, clean but not sterile, with small signs of a real life. Format: mirror selfie. Her phone, in a plain case with no logo, covers her face. The main subject sits in the right third of the frame with calmer negative space on the left, natural perspective and believable scale. Portrait 2:3. Light: soft overcast daylight from the window plus the warm glow of the string lights. Make it look like a good-quality photo taken on a phone in a mirror: phone camera seen in the mirror, 26mm phone lens, photorealistic, real-world photography, true-to-life textures, real skin and fabric texture, natural imperfections, nothing glossy. No lettering, no signs, no logos, no text anywhere in the frame, no brand marks on any product. Not a Paris apartment, cafe, marble room, mansion or influencer studio.
```

**Site alt text:** flat lay: Shoppable collage on pale lilac of a pink lip oil set, claw clips, pink quilted puffer tote, beaded bow bag charm, fuzzy pink slides, photo clip lights and satin scrunchies. · lifestyle: Mirror selfie in a farmhouse bedroom of a woman in a candy pink hoodie and fuzzy pink slides, pink puffer tote with a bow charm on her shoulder, phone covering her face.

**Pin 1, flat lay** · Sun 22 Nov 2026 13:30 ET · board `Legally Blonde Outfits | Pink Amazon Fashion` > section `Christmas and Gift Guides` · link: this look's Idea List (`https://www.amazon.com/shop/thedigitalincomeedit/list/<id>`) · AI label ON

- Overlay (on the image): TEEN GIRL / gift list
- Title: Gifts for Teen Girls Who Love Pink: Lip Oil, Claw Clips, Bag Charms and a Puffer Tote
- Description: Gifts for teen girls who love pink and have strong opinions about everything: a lip oil set, claw clips in pinks and cream, a quilted puffer tote, a bow bag charm, fuzzy slides, photo clip lights and satin scrunchies. Nothing on this list looks like a grown-up picked it, which is the highest compliment a teenager can give you. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #giftsforteens #teengirlgifts #pinkaesthetic #christmasgifts
- Alt text: Shoppable collage on pale lilac of a pink lip oil set, claw clips, pink quilted puffer tote, beaded bow bag charm, fuzzy pink slides, photo clip lights and satin scrunchies.

**Pin 2, lifestyle** · Wed 25 Nov 2026 20:30 ET · same board and section · same Idea List link · AI label ON, "includes an AI-generated person" ticked

- Title: Christmas Gift Ideas for Teen Girls: The Pink Puffer Tote, Bag Charm and Fuzzy Slides Look
- Description: Christmas gift ideas for teen girls, styled the way she would actually wear them: a candy pink hoodie, fuzzy slides, a quilted puffer tote with a bow charm and a claw clip holding it all together. Mirror selfie is mandatory. Save this list now, before the group chat starts asking you what she wants for Christmas. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #teengirlgifts #giftsforteens #christmasgifts #pinkoutfit
- Alt text: Mirror selfie in a farmhouse bedroom of a woman in a candy pink hoodie and fuzzy pink slides, pink puffer tote with a bow charm on her shoulder, phone covering her face.

**Instagram @itstommykate feed post** · Sun 22 Nov 2026 19:00 ET · carousel: lifestyle photo first, flat lay second · AI label ON · check the caption panel says `itstommykate` before Share

```
if a 15 year old would steal it from me, it's on the list. puffer tote, bow charm, fuzzy slides, the lip oil everyone keeps asking about 🎀 teen gift list is linked in my Amazon storefront (link in bio) #ad #giftsforteens #teengirlgifts
```


---

### 3. For College Girls

**Page:** `/lifestyle/pink-dorm-gifts-for-college-girls` · category `dorm` · season `Holiday` · file `src/lifestyle/pink-dorm-gifts-for-college-girls.json` (committed, `draft: true`)

**Page title (H1):** Pink Dorm Room Gifts for College Girls

**Intro:** Dorm gifts should solve a real problem, and the real problem is a cinderblock room with one overhead light. A heated throw, a cordless lamp, a shower caddy she won't be embarrassed to carry and a clip-on bedside shelf fix most of it. Pink makes the rest bearable.

**Items to source (the page lists them in this order):**

1. Blush heated throw blanket · note on page: "For the radiator that never works."
2. Cordless rechargeable table lamp · note on page: "No outlet fights with the roommate."
3. Pink mesh shower caddy tote
4. Bed wedge reading pillow
5. Satin pillowcase set
6. Pink acrylic desk organizer set
7. Clip-on bedside shelf · note on page: "The lofted bed's missing nightstand."

**Idea List:** title `Pink Dorm Room Gifts for College Girls` · description: Dorm gifts should solve a real problem, and the real problem is a cinderblock room with one overhead light. Every piece is linked here.

**Image 1, `pink-dorm-gifts-for-college-girls-flatlay.jpg` (no person, Format A):** Seedream 4.5 on Higgsfield, Unlimited ON, 4K, portrait 2:3. Attach (1) Command Centre `stylerefs` doc `sr-flatlay-grid`, (2) this look's product sheet. Garbled or soft title letters: re-run on Nano Banana Pro 2K. Colour follows factory section 4 (as pink as the look).

```
Using the first image as a style reference for the styling, the fullness and the title lettering, not an exact copy, please make me a very realistic overhead flat lay photo of the products in the second image. I can't use the exact Amazon images outside of Amazon, so this needs to be a new photo. Shot straight down, portrait 2:3, like a good-quality photo taken on a phone. The gifts are arranged as one abundant styled group, pieces overlapping and touching, on warm wood floorboards: blush heated throw blanket, cordless rechargeable table lamp, pink mesh shower caddy tote, bed wedge reading pillow, satin pillowcase set, pink acrylic desk organizer set, clip-on bedside shelf. Each item matches its screenshot in colour, shape and detail. Tucked in around them, filling the frame edge to edge with almost no empty background: a loose coil of fairy lights, an iced latte in a clear cup, a spiral notebook with a blank cover, a small bunch of pink carnations and two highlighters. Every product sits fully inside the frame. Soft natural window light, gentle real shadows, visible fabric texture, true-to-life materials, small real-life imperfections, photorealistic real-world photography. Across the upper third, set directly on the photo, a large two-style title: "DORM GIFTS" in a bold high-contrast serif in capitals, with "she'll use daily" beneath it in a thick flowing brush script, both in near-black, perfectly spelled, sharp edges, high contrast, filling about two thirds of the width. No logos, no brand names, no labels or printing on products or packaging, no watermark, no person, no other text.
```

**Image 2, `pink-dorm-gifts-for-college-girls-lifestyle.jpg` (Tommy Kate, detail shot of hands and products):** Google Gemini first; Nano Banana Pro 2K on Higgsfield if Gemini is out or the result fails. Attach (1) style reference `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/src/lifestyle/pink-workwear-freezing-office-lifestyle.jpg`, (2) the Omni seed `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/public/images/library/avatar-seed-omni-reference.png` as a JPEG under 400 KB, (3) this look's product sheet.

```
Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference. The reference sheet is the second image. Using the first image as a style reference, not an exact copy, please make me one single very realistic lifestyle photo, not a collage or grid. I can't use the exact Amazon images, so this is a new photo of the products in the third image, each matching its screenshot in colour and detail. Setting: the spare room of her farmhouse, a twin bed made up with a pink gingham duvet, an open kraft care box on the bed, in December. Close detail of her hands tucking the rolled blush heated throw and the cordless lamp into the care box, the pink mesh shower caddy and satin pillowcases waiting beside it. She is wearing the cuffs of a soft pink waffle knit henley and a thin gold bangle. Nails: pale pink. Her glitter-flecked pink iced coffee tumbler with a lavender straw, saturated candy pink, never pale, is on the bed beside the box. Other pink in the frame: the pink shower caddy, the blush throw and the pink gingham duvet; pink clothes and other pink pieces are welcome alongside the tumbler. The register is quiet wealth, lived in: a real farmhouse that is nice but never showy, clean but not sterile, with small signs of a real life. Format: detail shot of hands and products. Her face is not in the frame. The main subject sits in the right third of the frame with calmer negative space on the left, natural perspective and believable scale. Portrait 2:3. Light: late afternoon window light with long soft shadows. Shot on a mirrorless camera with a 35mm lens at f/2.8, natural depth of field and soft natural bokeh, photorealistic, real-world photography, true-to-life textures, real skin and fabric texture, natural imperfections, nothing glossy. No lettering, no signs, no logos, no text anywhere in the frame, no brand marks on any product. Not a Paris apartment, cafe, marble room, mansion or influencer studio.
```

**Site alt text:** flat lay: Overhead flat lay on wood floorboards of a blush heated throw, cordless lamp, pink shower caddy, reading pillow, satin pillowcases, pink desk organizer and a clip-on shelf. · lifestyle: Hands packing a college care box on a pink gingham bed with a blush heated throw, cordless lamp, pink shower caddy and satin pillowcases, pink glitter tumbler beside it.

**Pin 1, flat lay** · Tue 1 Dec 2026 13:30 ET · board `Pink Home, Dorm and Car Finds | Amazon` > section `Christmas and Gift Guides` · link: this look's Idea List (`https://www.amazon.com/shop/thedigitalincomeedit/list/<id>`) · AI label ON

- Overlay (on the image): DORM GIFTS / she'll use daily
- Title: Pink Dorm Room Gifts for College Girls: Heated Throw, Cordless Lamp and a Cute Shower Caddy
- Description: Pink dorm room gifts for college girls that fix the real problems of dorm life: a heated throw for the radiator that never works, a cordless lamp for the missing outlet, a shower caddy she won't hide, a reading pillow, satin pillowcases, a desk organizer and a clip-on bedside shelf. Care package energy with grown-up taste. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #dormgifts #collegegifts #pinkdorm #dormroomideas
- Alt text: Overhead flat lay on wood floorboards of a blush heated throw, cordless lamp, pink shower caddy, reading pillow, satin pillowcases, pink desk organizer and a clip-on shelf.

**Pin 2, lifestyle** · Fri 4 Dec 2026 20:30 ET · same board and section · same Idea List link · AI label ON, "includes an AI-generated person" ticked

- Title: College Care Package Ideas for Her: Pink Dorm Essentials That Make Winter Break Better
- Description: College care package ideas for the girl coming home for winter break or heading back in January: a blush heated throw, a cordless lamp, a pink shower caddy and satin pillowcases, packed in one box with a handwritten note on top. Dorm life is hard enough without a sad room. Save this for finals week, when she needs it most. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #carepackage #collegegifts #dormessentials #pinkdorm
- Alt text: Hands packing a college care box on a pink gingham bed with a blush heated throw, cordless lamp, pink shower caddy and satin pillowcases, pink glitter tumbler beside it.

**Instagram @itstommykate feed post** · Tue 1 Dec 2026 19:00 ET · carousel: lifestyle photo first, flat lay second · AI label ON · check the caption panel says `itstommykate` before Share

```
packing a dorm care box like it's my job. heated throw, cordless lamp, a shower caddy that doesn't look like it came from a hospital 🎀 whole list is linked in my Amazon storefront (link in bio) #ad #dormgifts #collegegifts
```


---

### 4. For Coworkers

**Page:** `/lifestyle/cute-coworker-christmas-gifts` · category `gifts` · season `Holiday` · file `src/lifestyle/cute-coworker-christmas-gifts.json` (committed, `draft: true`)

**Page title (H1):** Cute Coworker Christmas Gifts That Aren't a Mug

**Intro:** The coworker gift has one job: be nice without being weird. Skip the mug, they own eleven. A desk plant that can't die, pretty pens, hand cream for dry office air and a tiny candle land every time, and three of them fit in one gift bag.

**Items to source (the page lists them in this order):**

1. Faux succulent in a ceramic pot · note on page: "Cannot die. Believe me, people have tried."
2. Pastel pink gel pen set
3. Mini hand cream trio · note on page: "Dry office air is a crime."
4. Small candle in a glass jar
5. Pink sticky note set
6. Tinted lip balm set
7. Blush acrylic desk organizer

**Idea List:** title `Cute Coworker Christmas Gifts That Aren't a Mug` · description: The coworker gift has one job: be nice without being weird. Every piece is linked here.

**Image 1, `cute-coworker-christmas-gifts-flatlay.jpg` (no person, Format B):** Seedream 4.5 on Higgsfield, Unlimited ON, 4K, portrait 2:3. Attach (1) Command Centre `stylerefs` doc `sr-that-girl-amazon-finds-script`, (2) this look's product sheet. Garbled or soft title letters: re-run on Nano Banana Pro 2K. Colour follows factory section 4 (as pink as the look).

```
Using the first image as a style reference for the layout, the fullness and the title lettering, not an exact copy, please make me a "that girl" shoppable Amazon finds collage for Pinterest, portrait 2:3, on a soft cream background with a faint paper texture. I can't use the exact Amazon images outside of Amazon, so please create a new clean cut-out product photo of each item in the second image, each with a soft drop shadow: faux succulent in a ceramic pot, pastel pink gel pen set, mini hand cream trio, small candle in a glass jar, pink sticky note set, tinted lip balm set, blush acrylic desk organizer. Add small gifts wrapped in pink tissue, a satin ribbon spool, a gold paper clip and a sprig of pine. Pack them around a central title so the whole canvas is full edge to edge, items overlapping slightly, every product fully inside the frame. Add a few tiny accents: small hearts, little sparkles and one small bow. In the middle, set directly on the background, a large two-style title: "COWORKER GIFTS" in a bold high-contrast serif with "not a mug" in a thick flowing brush script, near-black, perfectly spelled, crisp and fully legible, filling about half the width. Each item matches its screenshot in colour, shape and detail and looks like a real photo, not a render, with true-to-life materials. No logos, no brand names, no labels or printing on products or packaging, no prices, no person, no other text.
```

**Image 2, `cute-coworker-christmas-gifts-lifestyle.jpg` (Tommy Kate, chin-down outfit crop):** Google Gemini first; Nano Banana Pro 2K on Higgsfield if Gemini is out or the result fails. Attach (1) style reference `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/src/lifestyle/pink-workwear-freezing-office-lifestyle.jpg`, (2) the Omni seed `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/public/images/library/avatar-seed-omni-reference.png` as a JPEG under 400 KB, (3) this look's product sheet.

```
Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference. The reference sheet is the second image. Using the first image as a style reference, not an exact copy, please make me one single very realistic lifestyle photo, not a collage or grid. I can't use the exact Amazon images, so this is a new photo of the products in the third image, each matching its screenshot in colour and detail. Setting: the butcher block island in her farmhouse kitchen early in the morning, a row of little kraft gift bags lined up with pink tissue, in December. A chin-down crop from her collarbone to her hips as she tucks the faux succulent and a pen set into a pink tissue-lined gift bag, blank gift tags on the counter. She is wearing a soft cream turtleneck sweater under a candy pink quilted vest, dark straight jeans. Her hair is in a low sleek ponytail. Nails: nude pink. Her glitter-flecked pink iced coffee tumbler with a lavender straw, saturated candy pink, never pale, is on the island by her hand. Other pink in the frame: the candy pink quilted vest and the pink tissue paper; pink clothes and other pink pieces are welcome alongside the tumbler. The register is quiet wealth, lived in: a real farmhouse that is nice but never showy, clean but not sterile, with small signs of a real life. Format: chin-down outfit crop. The frame is cropped just below her chin, so her face is not in the frame. The main subject sits in the right third of the frame with calmer negative space on the left, natural perspective and believable scale. Portrait 2:3. Light: soft overcast morning light from the kitchen window. Shot on a mirrorless camera with a 35mm lens at f/2.8, natural depth of field and soft natural bokeh, photorealistic, real-world photography, true-to-life textures, real skin and fabric texture, natural imperfections, nothing glossy. No lettering, no signs, no logos, no text anywhere in the frame, no brand marks on any product. Not a Paris apartment, cafe, marble room, mansion or influencer studio.
```

**Site alt text:** flat lay: Shoppable collage on cream of a faux succulent, pastel gel pens, hand cream trio, small candle, pink sticky notes, tinted lip balms and a blush acrylic desk organizer. · lifestyle: Chin-down crop of a woman in a candy pink quilted vest at a farmhouse kitchen island, tucking a faux succulent and pens into small kraft gift bags with pink tissue.

**Pin 1, flat lay** · Thu 3 Dec 2026 13:30 ET · board `Legally Blonde Outfits | Pink Amazon Fashion` > section `Christmas and Gift Guides` · link: this look's Idea List (`https://www.amazon.com/shop/thedigitalincomeedit/list/<id>`) · AI label ON

- Overlay (on the image): COWORKER GIFTS / not a mug
- Title: Cute Coworker Christmas Gifts That Aren't a Mug: Desk Finds They'll Actually Keep
- Description: Cute coworker Christmas gifts that are not another mug: a faux succulent that cannot die, pastel gel pens, a hand cream trio for dry office air, a small candle, pretty sticky notes, lip balm and a blush desk organizer. Mix three into one bag and you look thoughtful without spending your whole lunch break at the store. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #coworkergifts #officegifts #christmasgifts #giftideas
- Alt text: Shoppable collage on cream of a faux succulent, pastel gel pens, hand cream trio, small candle, pink sticky notes, tinted lip balms and a blush acrylic desk organizer.

**Pin 2, lifestyle** · Sun 6 Dec 2026 20:30 ET · same board and section · same Idea List link · AI label ON, "includes an AI-generated person" ticked

- Title: Office Christmas Gift Ideas for Coworkers: Little Pink Gift Bags Everyone Will Keep
- Description: Office Christmas gift ideas for coworkers, wrapped at the kitchen island before the first coffee: a faux succulent, gel pens, hand cream and a tiny candle tucked into pink tissue. Easy, cute, and nobody has to pretend to love a novelty mug again this year. Save it for the Friday before the office party, when you remember. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #officegifts #coworkergifts #secretsanta #giftwrapping
- Alt text: Chin-down crop of a woman in a candy pink quilted vest at a farmhouse kitchen island, tucking a faux succulent and pens into small kraft gift bags with pink tissue.

**Instagram @itstommykate feed post** · Thu 3 Dec 2026 19:00 ET · carousel: lifestyle photo first, flat lay second · AI label ON · check the caption panel says `itstommykate` before Share

```
coworker gifts wrapped before my first coffee was cold. zero mugs were involved 🎀 plant that can't die, pretty pens, hand cream, tiny candle. all linked in my Amazon storefront (link in bio) #ad #coworkergifts #officegifts
```


---

### 5. Stocking Stuffers

**Page:** `/lifestyle/pink-stocking-stuffers-for-women` · category `gifts` · season `Holiday` · file `src/lifestyle/pink-stocking-stuffers-for-women.json` (committed, `draft: true`)

**Page title (H1):** Pink Stocking Stuffers for Women

**Intro:** The stocking is where the best gifts hide, because nobody expects anything good in there. Lip oil, a silk scrunchie set, a mini perfume atomizer, fuzzy socks and a rechargeable hand warmer punch well above their size. Fill it with things she will use by New Year's.

**Items to source (the page lists them in this order):**

1. Plumping lip oil
2. Mulberry silk scrunchie set
3. Refillable mini perfume atomizer · note on page: "Her favorite scent, purse sized."
4. Fuzzy cozy socks
5. Rechargeable hand warmer · note on page: "For barn chores and football games."
6. Pearl claw clip
7. Mini nail polish set in pinks

**Idea List:** title `Pink Stocking Stuffers for Women` · description: The stocking is where the best gifts hide, because nobody expects anything good in there. Every piece is linked here.

**Image 1, `pink-stocking-stuffers-for-women-flatlay.jpg` (no person, Format A):** Seedream 4.5 on Higgsfield, Unlimited ON, 4K, portrait 2:3. Attach (1) Command Centre `stylerefs` doc `sr-pink-dress-flatlay`, (2) this look's product sheet. Garbled or soft title letters: re-run on Nano Banana Pro 2K. Colour follows factory section 4 (as pink as the look).

```
Using the first image as a style reference for the styling, the fullness and the title lettering, not an exact copy, please make me a very realistic overhead flat lay photo of the products in the second image. I can't use the exact Amazon images outside of Amazon, so this needs to be a new photo. Shot straight down, portrait 2:3, like a good-quality photo taken on a phone. The gifts are arranged as one abundant styled group, pieces overlapping and touching, on fluffy pink faux fur: plumping lip oil, mulberry silk scrunchie set, refillable mini perfume atomizer, fuzzy cozy socks, rechargeable hand warmer, pearl claw clip, mini nail polish set in pinks. Each item matches its screenshot in colour, shape and detail. Tucked in around them, filling the frame edge to edge with almost no empty background: a pink gingham stocking the finds spill out of, a sprig of fresh pine, a satin hair bow and a sugar cookie on a small linen napkin. Every product sits fully inside the frame. Soft natural window light, gentle real shadows, visible fabric texture, true-to-life materials, small real-life imperfections, photorealistic real-world photography. Across the upper third, set directly on the photo, a large two-style title: "STOCKING STUFFERS" in a bold high-contrast serif in capitals, with "for her" beneath it in a thick flowing brush script, both in deep plum, perfectly spelled, sharp edges, high contrast, filling about two thirds of the width. No logos, no brand names, no labels or printing on products or packaging, no watermark, no person, no other text.
```

**Image 2, `pink-stocking-stuffers-for-women-lifestyle.jpg` (Tommy Kate, over-the-shoulder walk-away):** Google Gemini first; Nano Banana Pro 2K on Higgsfield if Gemini is out or the result fails. Attach (1) style reference `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/src/lifestyle/pink-graduation-gown-halloween-costume-lifestyle.jpg`, (2) the Omni seed `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/public/images/library/avatar-seed-omni-reference.png` as a JPEG under 400 KB, (3) this look's product sheet.

```
Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference. The reference sheet is the second image. Using the first image as a style reference, not an exact copy, please make me one single very realistic lifestyle photo, not a collage or grid. I can't use the exact Amazon images, so this is a new photo of the products in the third image, each matching its screenshot in colour and detail. Setting: the stone fireplace in her farmhouse living room in the evening, pink gingham stockings hung from the mantel on brass hooks under a garland of fresh greenery, in December. Seen from behind over her shoulder as she reaches up to tuck the silk scrunchies and lip oil into a stocking, the rest of the finds waiting in a small woven basket on the hearth. She is wearing a long oversized candy pink cardigan over a cream tee, black leggings and fuzzy socks. Her hair is worn down and loose. Nails: sheer pink. Her glitter-flecked pink iced coffee tumbler with a lavender straw, saturated candy pink, never pale, is on the mantel beside the garland. Other pink in the frame: the candy pink cardigan and the pink gingham stockings; pink clothes and other pink pieces are welcome alongside the tumbler. The register is quiet wealth, lived in: a real farmhouse that is nice but never showy, clean but not sterile, with small signs of a real life. Format: over-the-shoulder walk-away. Her face is turned away from the camera. The main subject sits in the right third of the frame with calmer negative space on the left, natural perspective and believable scale. Portrait 2:3. Light: warm firelight plus one practical table lamp. Shot on a mirrorless camera with a 50mm lens at f/2, natural depth of field and soft natural bokeh, photorealistic, real-world photography, true-to-life textures, real skin and fabric texture, natural imperfections, nothing glossy. No lettering, no signs, no logos, no text anywhere in the frame, no brand marks on any product. Not a Paris apartment, cafe, marble room, mansion or influencer studio.
```

**Site alt text:** flat lay: Overhead flat lay on pink faux fur of a gingham stocking spilling lip oil, silk scrunchies, a mini perfume atomizer, fuzzy socks, a hand warmer, pearl claw clip and nail polish. · lifestyle: Woman in a candy pink cardigan seen from behind tucking small gifts into pink gingham stockings on a stone farmhouse fireplace mantel with fresh garland at night.

**Pin 1, flat lay** · Tue 24 Nov 2026 13:30 ET · board `Legally Blonde Outfits | Pink Amazon Fashion` > section `Christmas and Gift Guides` · link: this look's Idea List (`https://www.amazon.com/shop/thedigitalincomeedit/list/<id>`) · AI label ON

- Overlay (on the image): STOCKING STUFFERS / for her
- Title: Pink Stocking Stuffers for Women: Lip Oil, Silk Scrunchies, Mini Perfume and Cozy Socks
- Description: Pink stocking stuffers for women that she will use before New Year's: lip oil, silk scrunchies, a refillable mini perfume atomizer, fuzzy socks, a rechargeable hand warmer, a pearl claw clip and mini nail polish. The stocking is the sneaky best part of Christmas morning, so fill it with good small things, not candy she didn't ask for. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #stockingstuffers #giftsforher #christmasgifts
- Alt text: Overhead flat lay on pink faux fur of a gingham stocking spilling lip oil, silk scrunchies, a mini perfume atomizer, fuzzy socks, a hand warmer, pearl claw clip and nail polish.

**Pin 2, lifestyle** · Fri 27 Nov 2026 20:30 ET · same board and section · same Idea List link · AI label ON, "includes an AI-generated person" ticked

- Title: Stocking Stuffer Ideas for Her: Little Pink Things That Make Christmas Morning Better
- Description: Stocking stuffer ideas for her, tucked into pink gingham stockings by the fireplace the night before: lip oil, silk scrunchies, a mini perfume atomizer, cozy socks and a hand warmer for the morning barn chores. Small, pretty, useful. Save this for Christmas Eve, when you suddenly realise the stockings are still empty. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #stockingstuffers #stockingstufferideas #christmasmorning
- Alt text: Woman in a candy pink cardigan seen from behind tucking small gifts into pink gingham stockings on a stone farmhouse fireplace mantel with fresh garland at night.

**Instagram @itstommykate feed post** · Tue 24 Nov 2026 19:00 ET · carousel: lifestyle photo first, flat lay second · AI label ON · check the caption panel says `itstommykate` before Share

```
stockings hung, gingham obviously. lip oil, silk scrunchies, mini perfume, fuzzy socks and a hand warmer for barn chores 🎀 every little thing is linked in my Amazon storefront (link in bio) #ad #stockingstuffers #christmasgifts
```


---

### 6. Pink Christmas Decor

**Page:** `/lifestyle/pink-christmas-home-decor` · category `home-decor` · season `Holiday` · file `src/lifestyle/pink-christmas-home-decor.json` (committed, `draft: true`)

**Page title (H1):** Pink Christmas Decor That Still Looks Grown Up

**Intro:** Pink Christmas decor goes wrong fast. One glittery flamingo and suddenly it's a theme party. The fix is soft pink against real greenery, wood and cream: velvet ribbon, blush glass ornaments, one big wreath bow and candlelight. Grown-up girly, not the toy aisle.

**Items to source (the page lists them in this order):**

1. Blush pink velvet ribbon roll
2. Pink glass ball ornament set
3. Faux cedar garland
4. Oversized pink velvet wreath bow · note on page: "One bow does more than twenty ornaments."
5. Blush flameless taper candles
6. Pink gingham tree skirt
7. Brass star tree topper

**Idea List:** title `Pink Christmas Decor That Still Looks Grown Up` · description: Pink Christmas decor goes wrong fast. Every piece is linked here.

**Image 1, `pink-christmas-home-decor-flatlay.jpg` (no person, Format B):** Seedream 4.5 on Higgsfield, Unlimited ON, 4K, portrait 2:3. Attach (1) Command Centre `stylerefs` doc `sr-amazon-fashion-looks-expensive`, (2) this look's product sheet. Garbled or soft title letters: re-run on Nano Banana Pro 2K. Colour follows factory section 4 (as pink as the look).

```
Using the first image as a style reference for the layout, the fullness and the title lettering, not an exact copy, please make me a "that girl" shoppable Amazon finds collage for Pinterest, portrait 2:3, on a soft blush pink background with a faint paper texture. I can't use the exact Amazon images outside of Amazon, so please create a new clean cut-out product photo of each item in the second image, each with a soft drop shadow: blush pink velvet ribbon roll, pink glass ball ornament set, faux cedar garland, oversized pink velvet wreath bow, blush flameless taper candles, pink gingham tree skirt, brass star tree topper. Add sprigs of fresh pine, a small bunch of pink roses, a small brass bell and cinnamon sticks tied with twine. Pack them around a central title so the whole canvas is full edge to edge, items overlapping slightly, every product fully inside the frame. Add a few tiny accents: small hearts, little sparkles and one small bow. In the middle, set directly on the background, a large two-style title: "PINK CHRISTMAS" in a bold high-contrast serif with "decor" in a thick flowing brush script, deep plum, perfectly spelled, crisp and fully legible, filling about half the width. Each item matches its screenshot in colour, shape and detail and looks like a real photo, not a render, with true-to-life materials. No logos, no brand names, no labels or printing on products or packaging, no prices, no person, no other text.
```

**Image 2, `pink-christmas-home-decor-lifestyle.jpg` (Tommy Kate, over-the-shoulder walk-away):** Google Gemini first; Nano Banana Pro 2K on Higgsfield if Gemini is out or the result fails. Attach (1) style reference `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/src/lifestyle/pink-graduation-gown-halloween-costume-lifestyle.jpg`, (2) the Omni seed `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/public/images/library/avatar-seed-omni-reference.png` as a JPEG under 400 KB, (3) this look's product sheet.

```
Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference. The reference sheet is the second image. Using the first image as a style reference, not an exact copy, please make me one single very realistic lifestyle photo, not a collage or grid. I can't use the exact Amazon images, so this is a new photo of the products in the third image, each matching its screenshot in colour and detail. Setting: the farmhouse front porch at blue hour, a white painted front door, real snow dusting the porch rail and steps, lanterns lit, in December. Seen from behind over her shoulder as she hangs a fresh evergreen wreath tied with the oversized pink velvet bow on the front door, faux cedar garland already draped over the doorframe. She is wearing a cream puffer jacket, a candy pink knit beanie, jeans and brown lace-up boots. Her hair is worn down under the beanie. Nails: soft pink. Her glitter-flecked pink iced coffee tumbler with a lavender straw, saturated candy pink, never pale, is on the porch rail beside her. Other pink in the frame: the candy pink beanie and the pink velvet wreath bow; pink clothes and other pink pieces are welcome alongside the tumbler. The register is quiet wealth, lived in: a real farmhouse that is nice but never showy, clean but not sterile, with small signs of a real life. Format: over-the-shoulder walk-away. Her face is turned away from the camera. The main subject sits in the right third of the frame with calmer negative space on the left, natural perspective and believable scale. Portrait 2:3. Light: warm porch lantern light against the last blue light of dusk. Shot on a mirrorless camera with a 35mm lens at f/2, natural depth of field and soft natural bokeh, photorealistic, real-world photography, true-to-life textures, real skin and fabric texture, natural imperfections, nothing glossy. No lettering, no signs, no logos, no text anywhere in the frame, no brand marks on any product. Not a Paris apartment, cafe, marble room, mansion or influencer studio.
```

**Site alt text:** flat lay: Shoppable collage on blush pink of velvet ribbon, pink glass ornaments, faux cedar garland, a big pink velvet wreath bow, blush taper candles, a gingham tree skirt and a brass star. · lifestyle: Woman in a cream puffer and candy pink beanie seen from behind hanging a wreath with a big pink velvet bow on a white farmhouse door, snow on the porch rail at dusk.

**Pin 1, flat lay** · Sat 28 Nov 2026 13:30 ET · board `Pink Home, Dorm and Car Finds | Amazon` > section `Christmas and Gift Guides` · link: this look's Idea List (`https://www.amazon.com/shop/thedigitalincomeedit/list/<id>`) · AI label ON

- Overlay (on the image): PINK CHRISTMAS / decor
- Title: Pink Christmas Decor Ideas That Still Look Grown Up: Velvet Bows, Blush Ornaments and Cedar
- Description: Pink Christmas decor ideas that look grown up instead of glitter overload: blush velvet ribbon, pink glass ball ornaments, faux cedar garland, a big pink velvet wreath bow, blush flameless tapers, a pink gingham tree skirt and a brass star topper. Keep the pink soft and put it right next to real green and wood. That is the whole secret. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #pinkchristmas #christmasdecor #pinkchristmasdecor
- Alt text: Shoppable collage on blush pink of velvet ribbon, pink glass ornaments, faux cedar garland, a big pink velvet wreath bow, blush taper candles, a gingham tree skirt and a brass star.

**Pin 2, lifestyle** · Tue 1 Dec 2026 20:30 ET · same board and section · same Idea List link · AI label ON, "includes an AI-generated person" ticked

- Title: Pink Christmas Porch Decor: A Fresh Wreath, Cedar Garland and One Big Pink Velvet Bow
- Description: Pink Christmas porch decor for a farmhouse front door: a fresh wreath with one oversized pink velvet bow, cedar garland over the frame and lantern light on the snow. It is the first thing anyone sees when they pull up the drive, so let it be pretty. Save this for the weekend you finally drag the ladder out of the barn. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #christmasporch #pinkchristmas #frontdoordecor #farmhousechristmas
- Alt text: Woman in a cream puffer and candy pink beanie seen from behind hanging a wreath with a big pink velvet bow on a white farmhouse door, snow on the porch rail at dusk.

**Instagram @itstommykate feed post** · Sat 28 Nov 2026 19:00 ET · carousel: lifestyle photo first, flat lay second · AI label ON · check the caption panel says `itstommykate` before Share

```
the big pink bow went up and now the whole porch makes sense 🎀 velvet ribbon, blush ornaments, cedar garland, all linked in my Amazon storefront (link in bio) #ad #pinkchristmas #christmasdecor
```


---

### 7. Cozy Pajamas

**Page:** `/lifestyle/cozy-pink-christmas-pajamas` · category `clothing` · season `Holiday` · file `src/lifestyle/cozy-pink-christmas-pajamas.json` (committed, `draft: true`)

**Page title (H1):** Cozy Pink Christmas Pajamas and Loungewear

**Intro:** Christmas pajamas are the one outfit everybody actually wears on the day, so they deserve effort. Brushed flannel in pink gingham, a waffle robe, faux fur slippers and a satin sleep mask make a set she will live in until February. The photos by the tree look better too.

**Items to source (the page lists them in this order):**

1. Pink gingham flannel pajama set
2. Blush waffle knit robe
3. Faux fur lined moccasin slippers in pink
4. Satin sleep mask
5. Ribbed knit lounge set in cream · note on page: "For the days after Christmas."
6. Knit covered hot water bottle in pink

**Idea List:** title `Cozy Pink Christmas Pajamas and Loungewear` · description: Christmas pajamas are the one outfit everybody actually wears on the day, so they deserve effort. Every piece is linked here.

**Image 1, `cozy-pink-christmas-pajamas-flatlay.jpg` (no person, Format A):** Seedream 4.5 on Higgsfield, Unlimited ON, 4K, portrait 2:3. Attach (1) Command Centre `stylerefs` doc `sr-flatlay-grid`, (2) this look's product sheet. Garbled or soft title letters: re-run on Nano Banana Pro 2K. Colour follows factory section 4 (as pink as the look).

```
Using the first image as a style reference for the styling, the fullness and the title lettering, not an exact copy, please make me a very realistic overhead flat lay photo of the products in the second image. I can't use the exact Amazon images outside of Amazon, so this needs to be a new photo. Shot straight down, portrait 2:3, like a good-quality photo taken on a phone. The outfit is laid out as if worn, top above bottom, shoes at the hem, bag at the hip, jewellery at the neckline, pieces overlapping and touching, on crumpled white linen: pink gingham flannel pajama set, blush waffle knit robe, faux fur lined moccasin slippers in pink, satin sleep mask, ribbed knit lounge set in cream, knit covered hot water bottle in pink. Each item matches its screenshot in colour, shape and detail. Tucked in around them, filling the frame edge to edge with almost no empty background: a sprig of pine, an iced latte in a clear glass, an open paperback with plain pages, a small candle and a satin hair bow. Every product sits fully inside the frame. Soft natural window light, gentle real shadows, visible fabric texture, true-to-life materials, small real-life imperfections, photorealistic real-world photography. Across the upper third, set directly on the photo, a large two-style title: "COZY PAJAMAS" in a bold high-contrast serif in capitals, with "christmas morning" beneath it in a thick flowing brush script, both in near-black, perfectly spelled, sharp edges, high contrast, filling about two thirds of the width. No logos, no brand names, no labels or printing on products or packaging, no watermark, no person, no other text.
```

**Image 2, `cozy-pink-christmas-pajamas-lifestyle.jpg` (Tommy Kate, mirror selfie):** Google Gemini first; Nano Banana Pro 2K on Higgsfield if Gemini is out or the result fails. Attach (1) style reference `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/src/lifestyle/pink-suit-law-student-halloween-costume-lifestyle.jpg`, (2) the Omni seed `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/public/images/library/avatar-seed-omni-reference.png` as a JPEG under 400 KB, (3) this look's product sheet.

```
Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference. The reference sheet is the second image. Using the first image as a style reference, not an exact copy, please make me one single very realistic lifestyle photo, not a collage or grid. I can't use the exact Amazon images, so this is a new photo of the products in the third image, each matching its screenshot in colour and detail. Setting: the antique standing mirror in the corner of her farmhouse bedroom on Christmas morning, an unmade white bed with a pink gingham quilt behind her, frost on the window panes. She takes a mirror selfie with a plain phone case covering her face, one slipper toe pointed, the blush waffle robe falling open over the pajamas. She is wearing the pink gingham flannel pajama set, the blush waffle robe worn open and the pink faux fur moccasin slippers. Her hair is in a messy low bun. Nails: cherry pink. Her glitter-flecked pink iced coffee tumbler with a lavender straw, saturated candy pink, never pale, is in her free hand. Other pink in the frame: the pink gingham pajamas, the blush robe and the pink slippers; pink clothes and other pink pieces are welcome alongside the tumbler. The register is quiet wealth, lived in: a real farmhouse that is nice but never showy, clean but not sterile, with small signs of a real life. Format: mirror selfie. Her phone, in a plain case with no logo, covers her face. The main subject sits in the right third of the frame with calmer negative space on the left, natural perspective and believable scale. Portrait 2:3. Light: cool soft winter daylight through frosted windows. Make it look like a good-quality photo taken on a phone in a mirror: phone camera seen in the mirror, 26mm phone lens, photorealistic, real-world photography, true-to-life textures, real skin and fabric texture, natural imperfections, nothing glossy. No lettering, no signs, no logos, no text anywhere in the frame, no brand marks on any product. Not a Paris apartment, cafe, marble room, mansion or influencer studio.
```

**Site alt text:** flat lay: Overhead flat lay on white linen of pink gingham flannel pajamas, a blush waffle robe, pink faux fur slippers, a satin sleep mask, a cream knit lounge set and a pink hot water bottle. · lifestyle: Mirror selfie in a farmhouse bedroom of a woman in pink gingham flannel pajamas, an open blush waffle robe and pink faux fur slippers, phone covering her face.

**Pin 1, flat lay** · Mon 30 Nov 2026 13:30 ET · board `Legally Blonde Outfits | Pink Amazon Fashion` > section `Christmas and Gift Guides` · link: this look's Idea List (`https://www.amazon.com/shop/thedigitalincomeedit/list/<id>`) · AI label ON

- Overlay (on the image): COZY PAJAMAS / christmas morning
- Title: Cozy Pink Christmas Pajamas for Women: Gingham Flannel, Waffle Robe and Fuzzy Slippers
- Description: Cozy pink Christmas pajamas for women who plan to stay in them until noon: a pink gingham flannel pajama set, a blush waffle robe, faux fur moccasin slippers, a satin sleep mask, a ribbed knit lounge set and a knit hot water bottle. It is the one outfit you are guaranteed to be photographed in on the day, so make it cute. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #christmaspajamas #cozyseason #pinkpajamas #loungewear
- Alt text: Overhead flat lay on white linen of pink gingham flannel pajamas, a blush waffle robe, pink faux fur slippers, a satin sleep mask, a cream knit lounge set and a pink hot water bottle.

**Pin 2, lifestyle** · Thu 3 Dec 2026 20:30 ET · same board and section · same Idea List link · AI label ON, "includes an AI-generated person" ticked

- Title: Christmas Morning Pajamas Outfit: Pink Gingham Flannel, Blush Robe and Faux Fur Slippers
- Description: Christmas morning pajamas outfit, snapped in the bedroom mirror before anyone else is up: pink gingham flannel, a blush waffle robe left open, faux fur moccasin slippers and iced coffee already in hand. Frost on the window, zero plans for the day. Save this for the family photo you are definitely going to end up in this year. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #christmaspajamas #christmasmorning #cozyoutfit #pinkoutfit
- Alt text: Mirror selfie in a farmhouse bedroom of a woman in pink gingham flannel pajamas, an open blush waffle robe and pink faux fur slippers, phone covering her face.

**Instagram @itstommykate feed post** · Mon 30 Nov 2026 19:00 ET · carousel: lifestyle photo first, flat lay second · AI label ON · check the caption panel says `itstommykate` before Share

```
christmas morning uniform: pink gingham flannel, waffle robe, slippers that could double as a small pet 🎀 the set is linked in my Amazon storefront (link in bio) #ad #christmaspajamas #cozyseason
```


---

### 8. Beauty and Perfume

**Page:** `/lifestyle/beauty-and-perfume-gift-sets` · category `perfume` · season `Holiday` · file `src/lifestyle/beauty-and-perfume-gift-sets.json` (committed, `draft: true`)

**Page title (H1):** Beauty and Perfume Gift Sets She'll Actually Use

**Intro:** Beauty gift sets are either the best present under the tree or a box of minis nobody opens. The difference is picking sets built around things she already uses: a lip set, a body care trio, a perfume discovery set and a heated eyelash curler. No mystery serums.

**Items to source (the page lists them in this order):**

1. Perfume discovery sample set · note on page: "She picks her own signature scent. You get the credit."
2. Pink lip gloss and liner set
3. Body wash, scrub and lotion trio
4. Heated eyelash curler
5. Pink quilted makeup bag
6. Gold mirrored vanity tray
7. Pink spa headband and wristband set

**Idea List:** title `Beauty and Perfume Gift Sets She'll Actually Use` · description: Beauty gift sets are either the best present under the tree or a box of minis nobody opens. Every piece is linked here.

**Image 1, `beauty-and-perfume-gift-sets-flatlay.jpg` (no person, Format B):** Seedream 4.5 on Higgsfield, Unlimited ON, 4K, portrait 2:3. Attach (1) Command Centre `stylerefs` doc `sr-soft-pink-collage`, (2) this look's product sheet. Garbled or soft title letters: re-run on Nano Banana Pro 2K. Colour follows factory section 4 (as pink as the look).

```
Using the first image as a style reference for the layout, the fullness and the title lettering, not an exact copy, please make me a "that girl" shoppable Amazon finds collage for Pinterest, portrait 2:3, on a soft pale lilac background with a faint paper texture. I can't use the exact Amazon images outside of Amazon, so please create a new clean cut-out product photo of each item in the second image, each with a soft drop shadow: perfume discovery sample set, pink lip gloss and liner set, body wash, scrub and lotion trio, heated eyelash curler, pink quilted makeup bag, gold mirrored vanity tray, pink spa headband and wristband set. Add stacked gold rings, a small bunch of pink tulips and a satin hair bow. Pack them around a central title so the whole canvas is full edge to edge, items overlapping slightly, every product fully inside the frame. Add a few tiny accents: small hearts, little sparkles and one small bow. In the middle, set directly on the background, a large two-style title: "BEAUTY GIFTS" in a bold high-contrast serif with "she'll use" in a thick flowing brush script, deep plum, perfectly spelled, crisp and fully legible, filling about half the width. Each item matches its screenshot in colour, shape and detail and looks like a real photo, not a render, with true-to-life materials. No logos, no brand names, no labels or printing on products or packaging, no prices, no person, no other text.
```

**Image 2, `beauty-and-perfume-gift-sets-lifestyle.jpg` (Tommy Kate, detail shot of hands and products):** Google Gemini first; Nano Banana Pro 2K on Higgsfield if Gemini is out or the result fails. Attach (1) style reference `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/src/lifestyle/pink-workwear-freezing-office-lifestyle.jpg`, (2) the Omni seed `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/public/images/library/avatar-seed-omni-reference.png` as a JPEG under 400 KB, (3) this look's product sheet.

```
Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference. The reference sheet is the second image. Using the first image as a style reference, not an exact copy, please make me one single very realistic lifestyle photo, not a collage or grid. I can't use the exact Amazon images, so this is a new photo of the products in the third image, each matching its screenshot in colour and detail. Setting: the painted wooden dresser in her farmhouse bedroom used as a vanity, a round mirror above it and a small vase of dried lilacs, in December. Close detail of her hands spritzing a perfume sample onto her wrist over the gold mirrored tray, the lip set and the pink quilted makeup bag laid out beside it. She is wearing the cuff of a candy pink ribbed knit sweater. Nails: glossy ballet pink. Her glitter-flecked pink iced coffee tumbler with a lavender straw, saturated candy pink, never pale, is at the back corner of the dresser. Other pink in the frame: the candy pink sweater cuff and the pink quilted makeup bag; pink clothes and other pink pieces are welcome alongside the tumbler. The register is quiet wealth, lived in: a real farmhouse that is nice but never showy, clean but not sterile, with small signs of a real life. Format: detail shot of hands and products. Her face is not in the frame. The main subject sits in the right third of the frame with calmer negative space on the left, natural perspective and believable scale. Portrait 2:3. Light: soft morning window light from the side. Shot on a mirrorless camera with a 50mm lens at f/2.2, natural depth of field and soft natural bokeh, photorealistic, real-world photography, true-to-life textures, real skin and fabric texture, natural imperfections, nothing glossy. No lettering, no signs, no logos, no text anywhere in the frame, no brand marks on any product. Not a Paris apartment, cafe, marble room, mansion or influencer studio.
```

**Site alt text:** flat lay: Shoppable collage on pale lilac of a perfume sample set, pink lip gloss and liner set, body care trio, heated lash curler, pink quilted makeup bag, gold vanity tray and spa headband. · lifestyle: Hands spritzing perfume onto a wrist over a gold mirrored tray on a painted farmhouse dresser, with a pink lip set, pink quilted makeup bag and dried lilacs.

**Pin 1, flat lay** · Thu 26 Nov 2026 13:30 ET · board `Legally Blonde Outfits | Pink Amazon Fashion` > section `Christmas and Gift Guides` · link: this look's Idea List (`https://www.amazon.com/shop/thedigitalincomeedit/list/<id>`) · AI label ON

- Overlay (on the image): BEAUTY GIFTS / she'll use
- Title: Beauty and Perfume Gift Sets She'll Actually Use: Lip Sets, Body Care and a Scent Sampler
- Description: Beauty and perfume gift sets she will actually use instead of shoving in a drawer: a perfume discovery set so she finds her own signature scent, a pink lip gloss and liner set, a body care trio, a heated eyelash curler, a quilted makeup bag, a gold vanity tray and a spa headband. Pick sets built around things she already reaches for. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #beautygifts #perfumegifts #giftsforher #giftsets
- Alt text: Shoppable collage on pale lilac of a perfume sample set, pink lip gloss and liner set, body care trio, heated lash curler, pink quilted makeup bag, gold vanity tray and spa headband.

**Pin 2, lifestyle** · Sun 29 Nov 2026 20:30 ET · same board and section · same Idea List link · AI label ON, "includes an AI-generated person" ticked

- Title: Perfume Gift Ideas for Her: A Scent Discovery Set, Pink Lip Kit and Gold Vanity Tray
- Description: Perfume gift ideas for her when you honestly have no idea what she wears: a discovery set of samples lets her pick her own, and it looks gorgeous next to a pink lip kit on a gold vanity tray. Tested on the wrist at the bedroom dresser, obviously. Save this one for the friend who smells amazing and still will not tell you why. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #perfumegifts #beautygifts #vanitydecor #giftsforher
- Alt text: Hands spritzing perfume onto a wrist over a gold mirrored tray on a painted farmhouse dresser, with a pink lip set, pink quilted makeup bag and dried lilacs.

**Instagram @itstommykate feed post** · Thu 26 Nov 2026 19:00 ET · carousel: lifestyle photo first, flat lay second · AI label ON · check the caption panel says `itstommykate` before Share

```
a perfume sampler is the gift for people who don't know her scent. she picks, you get credit 🎀 lip kit, body trio and the gold tray are linked in my Amazon storefront (link in bio) #ad #beautygifts #perfumegifts
```


---

### 9. Car Accessories

**Page:** `/lifestyle/pink-car-accessories-gifts` · category `car` · season `Holiday` · file `src/lifestyle/pink-car-accessories-gifts.json` (committed, `draft: true`)

**Page title (H1):** Pink Car Accessories That Make Great Gifts

**Intro:** Car gifts are criminally underrated. She is in that car every single day, and most of what is in there is ugly. A pink steering wheel cover, a seat gap filler, cute cupholder coasters and a heated seat cushion for January fix her whole commute.

**Items to source (the page lists them in this order):**

1. Pink steering wheel cover
2. Heated seat cushion · note on page: "For frosty mornings before the heater kicks in."
3. Car seat gap filler organizer · note on page: "Saves the phone from the abyss."
4. Pink cupholder coaster set
5. Mini car trash can in pink
6. Vent clip diffuser
7. Magnetic phone mount in pink

**Idea List:** title `Pink Car Accessories That Make Great Gifts` · description: Car gifts are criminally underrated. Every piece is linked here.

**Image 1, `pink-car-accessories-gifts-flatlay.jpg` (no person, Format A):** Seedream 4.5 on Higgsfield, Unlimited ON, 4K, portrait 2:3. Attach (1) Command Centre `stylerefs` doc `sr-pink-dress-flatlay`, (2) this look's product sheet. Garbled or soft title letters: re-run on Nano Banana Pro 2K. Colour follows factory section 4 (as pink as the look).

```
Using the first image as a style reference for the styling, the fullness and the title lettering, not an exact copy, please make me a very realistic overhead flat lay photo of the products in the second image. I can't use the exact Amazon images outside of Amazon, so this needs to be a new photo. Shot straight down, portrait 2:3, like a good-quality photo taken on a phone. The gifts are arranged as one abundant styled group, pieces overlapping and touching, on a chunky cream knit throw: pink steering wheel cover, heated seat cushion, car seat gap filler organizer, pink cupholder coaster set, mini car trash can in pink, vent clip diffuser, magnetic phone mount in pink. Each item matches its screenshot in colour, shape and detail. Tucked in around them, filling the frame edge to edge with almost no empty background: a set of car keys, heart shaped sunglasses, an iced coffee in a clear cup, a lip balm and a small bunch of dried flowers. Every product sits fully inside the frame. Soft natural window light, gentle real shadows, visible fabric texture, true-to-life materials, small real-life imperfections, photorealistic real-world photography. Across the upper third, set directly on the photo, a large two-style title: "PINK CAR" in a bold high-contrast serif in capitals, with "finds" beneath it in a thick flowing brush script, both in near-black, perfectly spelled, sharp edges, high contrast, filling about two thirds of the width. No logos, no brand names, no labels or printing on products or packaging, no watermark, no person, no other text.
```

**Image 2, `pink-car-accessories-gifts-lifestyle.jpg` (Tommy Kate, detail shot of hands and products):** Google Gemini first; Nano Banana Pro 2K on Higgsfield if Gemini is out or the result fails. Attach (1) style reference `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/src/lifestyle/pink-workwear-freezing-office-lifestyle.jpg`, (2) the Omni seed `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/public/images/library/avatar-seed-omni-reference.png` as a JPEG under 400 KB, (3) this look's product sheet.

```
Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference. The reference sheet is the second image. Using the first image as a style reference, not an exact copy, please make me one single very realistic lifestyle photo, not a collage or grid. I can't use the exact Amazon images, so this is a new photo of the products in the third image, each matching its screenshot in colour and detail. Setting: the driver's seat of her car parked on the gravel drive by the red barn on a frosty morning, the barn visible through the windshield, in December. Close detail of her hands resting on the pink steering wheel cover, the seat gap organizer holding her phone and lip balm, pink coasters in the cupholders. She is wearing the cuffs of a cream chunky knit sweater and a stack of thin gold rings. Nails: milky pink. Her glitter-flecked pink iced coffee tumbler with a lavender straw, saturated candy pink, never pale, is in the cupholder. Other pink in the frame: the pink steering wheel cover and the pink cupholder coasters; pink clothes and other pink pieces are welcome alongside the tumbler. The register is quiet wealth, lived in: a real farmhouse that is nice but never showy, clean but not sterile, with small signs of a real life. Format: detail shot of hands and products. Her face is not in the frame. The main subject sits in the right third of the frame with calmer negative space on the left, natural perspective and believable scale. Portrait 2:3. Light: soft overcast daylight through the windshield. Shot on a mirrorless camera with a 35mm lens at f/2.8, natural depth of field and soft natural bokeh, photorealistic, real-world photography, true-to-life textures, real skin and fabric texture, natural imperfections, nothing glossy. No lettering, no signs, no logos, no text anywhere in the frame, no brand marks on any product. Not a Paris apartment, cafe, marble room, mansion or influencer studio.
```

**Site alt text:** flat lay: Overhead flat lay on a cream knit of a pink steering wheel cover, heated seat cushion, seat gap organizer, pink cupholder coasters, small trash can, vent diffuser and phone mount. · lifestyle: Hands on a pink steering wheel cover in a car parked by a red barn on a frosty morning, pink glitter tumbler in the cupholder and a seat gap organizer holding a phone.

**Pin 1, flat lay** · Tue 8 Dec 2026 13:30 ET · board `Pink Home, Dorm and Car Finds | Amazon` > section `Christmas and Gift Guides` · link: this look's Idea List (`https://www.amazon.com/shop/thedigitalincomeedit/list/<id>`) · AI label ON

- Overlay (on the image): PINK CAR / finds
- Title: Pink Car Accessories That Make Great Gifts: Steering Wheel Cover, Heated Seat and More
- Description: Pink car accessories that make great gifts for the girl who basically lives in her car: a pink steering wheel cover, a heated seat cushion for cold mornings, a seat gap filler for the phone that keeps falling, cupholder coasters, a tiny car trash can, a vent clip diffuser and a magnetic phone mount. Every red light, a photo shoot. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #caraccessories #pinkcar #giftsforher #caressentials
- Alt text: Overhead flat lay on a cream knit of a pink steering wheel cover, heated seat cushion, seat gap organizer, pink cupholder coasters, small trash can, vent diffuser and phone mount.

**Pin 2, lifestyle** · Fri 11 Dec 2026 20:30 ET · same board and section · same Idea List link · AI label ON, "includes an AI-generated person" ticked

- Title: Cute Car Accessories for Women: A Pink Steering Wheel Cover and a Cozier Winter Commute
- Description: Cute car accessories for women who spend more time in the driver's seat than on the couch: a pink steering wheel cover, a seat gap organizer, cupholder coasters and a heated seat cushion for frosty farm mornings. Iced coffee in the cupholder, red barn in the windshield. Save this one for the commuter on your Christmas list. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #caraccessories #cutecaraccessories #pinkcar #cardecor
- Alt text: Hands on a pink steering wheel cover in a car parked by a red barn on a frosty morning, pink glitter tumbler in the cupholder and a seat gap organizer holding a phone.

**Instagram @itstommykate feed post** · Tue 8 Dec 2026 19:00 ET · carousel: lifestyle photo first, flat lay second · AI label ON · check the caption panel says `itstommykate` before Share

```
my car is basically my second office and now it's a pink one. steering wheel cover, heated seat cushion, the gap filler that saves my phone daily 🎀 linked in my Amazon storefront (link in bio) #ad #caraccessories #pinkcar
```


---

### 10. Jewelry

**Page:** `/lifestyle/pink-jewelry-gifts-for-her` · category `jewelry` · season `Holiday` · file `src/lifestyle/pink-jewelry-gifts-for-her.json` (committed, `draft: true`)

**Page title (H1):** Jewelry Gifts for Her: Stacking Rings, Pearls and Gold

**Intro:** Jewelry is the easiest gift to get right if you stay dainty. Stacking ring sets were one of last season's most searched gifts, and a set means you don't have to guess her size perfectly. Add pearl drops, a paperclip chain and a tiny pink enamel heart and you have covered every kind of girl.

**Items to source (the page lists them in this order):**

1. Gold stacking ring set
2. Pearl drop earrings
3. Gold paperclip chain necklace
4. Pink enamel heart pendant necklace · note on page: "The tiny pink detail that makes the whole stack."
5. Gold huggie hoop earrings
6. Pink crystal tennis bracelet
7. Ceramic heart ring dish

**Idea List:** title `Jewelry Gifts for Her: Stacking Rings, Pearls and Gold` · description: Jewelry is the easiest gift to get right if you stay dainty. Every piece is linked here.

**Image 1, `pink-jewelry-gifts-for-her-flatlay.jpg` (no person, Format B):** Seedream 4.5 on Higgsfield, Unlimited ON, 4K, portrait 2:3. Attach (1) Command Centre `stylerefs` doc `sr-that-girl-amazon-finds-blush`, (2) this look's product sheet. Garbled or soft title letters: re-run on Nano Banana Pro 2K. Colour follows factory section 4 (as pink as the look).

```
Using the first image as a style reference for the layout, the fullness and the title lettering, not an exact copy, please make me a "that girl" shoppable Amazon finds collage for Pinterest, portrait 2:3, on a soft blush pink background with a faint paper texture. I can't use the exact Amazon images outside of Amazon, so please create a new clean cut-out product photo of each item in the second image, each with a soft drop shadow: gold stacking ring set, pearl drop earrings, gold paperclip chain necklace, pink enamel heart pendant necklace, gold huggie hoop earrings, pink crystal tennis bracelet, ceramic heart ring dish. Add a satin hair bow, a small gift box with a ribbon and a few loose pink rose petals. Pack them around a central title so the whole canvas is full edge to edge, items overlapping slightly, every product fully inside the frame. Add a few tiny accents: small hearts, little sparkles and one small bow. In the middle, set directly on the background, a large two-style title: "JEWELRY GIFTS" in a bold high-contrast serif with "dainty gold" in a thick flowing brush script, deep plum, perfectly spelled, crisp and fully legible, filling about half the width. Each item matches its screenshot in colour, shape and detail and looks like a real photo, not a render, with true-to-life materials. No logos, no brand names, no labels or printing on products or packaging, no prices, no person, no other text.
```

**Image 2, `pink-jewelry-gifts-for-her-lifestyle.jpg` (Tommy Kate, chin-down outfit crop):** Google Gemini first; Nano Banana Pro 2K on Higgsfield if Gemini is out or the result fails. Attach (1) style reference `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/src/lifestyle/pink-workwear-freezing-office-lifestyle.jpg`, (2) the Omni seed `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/public/images/library/avatar-seed-omni-reference.png` as a JPEG under 400 KB, (3) this look's product sheet.

```
Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference. The reference sheet is the second image. Using the first image as a style reference, not an exact copy, please make me one single very realistic lifestyle photo, not a collage or grid. I can't use the exact Amazon images, so this is a new photo of the products in the third image, each matching its screenshot in colour and detail. Setting: the white porch railing of her farmhouse on a bright cold afternoon, the pasture and red barn soft in the background, in December. A chin-down crop from her collarbone to her waist as she fastens the pink enamel heart pendant at her neck, the stacking rings and pink tennis bracelet on show. She is wearing a candy pink crewneck sweater under a cream quilted vest. Her hair is tucked behind her ears. Nails: milky pink. Her glitter-flecked pink iced coffee tumbler with a lavender straw, saturated candy pink, never pale, is resting on the porch railing. Other pink in the frame: the candy pink sweater and the pink enamel heart; pink clothes and other pink pieces are welcome alongside the tumbler. The register is quiet wealth, lived in: a real farmhouse that is nice but never showy, clean but not sterile, with small signs of a real life. Format: chin-down outfit crop. The frame is cropped just below her chin, so her face is not in the frame. The main subject sits in the right third of the frame with calmer negative space on the left, natural perspective and believable scale. Portrait 2:3. Light: low golden hour sunlight from the side. Shot on a mirrorless camera with a 85mm lens at f/2, natural depth of field and soft natural bokeh, photorealistic, real-world photography, true-to-life textures, real skin and fabric texture, natural imperfections, nothing glossy. No lettering, no signs, no logos, no text anywhere in the frame, no brand marks on any product. Not a Paris apartment, cafe, marble room, mansion or influencer studio.
```

**Site alt text:** flat lay: Shoppable collage on blush pink of gold stacking rings, pearl drop earrings, a paperclip chain, pink enamel heart pendant, gold huggies, a pink tennis bracelet and a heart ring dish. · lifestyle: Chin-down crop of a woman in a candy pink sweater fastening a pink enamel heart necklace on a farmhouse porch, gold stacking rings and a pink tennis bracelet on show.

**Pin 1, flat lay** · Fri 27 Nov 2026 13:30 ET · board `Legally Blonde Outfits | Pink Amazon Fashion` > section `Christmas and Gift Guides` · link: this look's Idea List (`https://www.amazon.com/shop/thedigitalincomeedit/list/<id>`) · AI label ON

- Overlay (on the image): JEWELRY GIFTS / dainty gold
- Title: Jewelry Gifts for Her: Gold Stacking Rings, Pearl Drops and a Tiny Pink Heart Necklace
- Description: Jewelry gifts for her that are hard to get wrong: a gold stacking ring set, pearl drop earrings, a paperclip chain, a pink enamel heart pendant, gold huggie hoops, a pink crystal tennis bracelet and a heart ring dish to keep them in. Dainty gold works on everyone, and a ring set means you do not have to guess her size perfectly. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #jewelrygifts #goldjewelry #stackingrings #giftsforher
- Alt text: Shoppable collage on blush pink of gold stacking rings, pearl drop earrings, a paperclip chain, pink enamel heart pendant, gold huggies, a pink tennis bracelet and a heart ring dish.

**Pin 2, lifestyle** · Mon 30 Nov 2026 20:30 ET · same board and section · same Idea List link · AI label ON, "includes an AI-generated person" ticked

- Title: Dainty Gold Jewelry Gift Ideas: Stacking Rings, Tennis Bracelet and a Pink Heart Pendant
- Description: Dainty gold jewelry gift ideas, worn the way she would really wear them: stacking rings, a pink crystal tennis bracelet and a pink enamel heart pendant with a candy pink sweater on a cold bright afternoon. Layered, never loud. Save this for the girl who wears the same three pieces every single day and would secretly love one more. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #daintyjewelry #jewelrygifts #goldjewelry #christmasgifts
- Alt text: Chin-down crop of a woman in a candy pink sweater fastening a pink enamel heart necklace on a farmhouse porch, gold stacking rings and a pink tennis bracelet on show.

**Instagram @itstommykate feed post** · Fri 27 Nov 2026 19:00 ET · carousel: lifestyle photo first, flat lay second · AI label ON · check the caption panel says `itstommykate` before Share

```
the stacking rings never come off. then I added a tiny pink heart and a tennis bracelet and honestly it's a whole personality now 🎀 linked in my Amazon storefront (link in bio) #ad #jewelrygifts #goldjewelry
```


---

### 11. Books

**Page:** `/lifestyle/books-to-gift-this-christmas` · category `books` · season `Holiday` · file `src/lifestyle/books-to-gift-this-christmas.json` (committed, `draft: true`)

**Page title (H1):** Books as Gifts: The Pink Reading Nook Bundle

**Intro:** A book is a great gift and a slightly sad one if it arrives alone. Pair one cozy winter romance and one can't-sleep thriller with a rechargeable book light, a quilted book sleeve and a reading journal, and it turns into a whole night in. She will think you planned it for weeks.

**Items to source (the page lists them in this order):**

1. A cozy winter romance novel · note on page: "Pick a current bestseller she hasn't read."
2. A page-turning thriller · note on page: "Also a current bestseller."
3. Rechargeable clip-on book light
4. Quilted pink book sleeve
5. Reading journal
6. Tassel bookmark set
7. Wooden thumb page holder

**Idea List:** title `Books as Gifts: The Pink Reading Nook Bundle` · description: A book is a great gift and a slightly sad one if it arrives alone. Every piece is linked here.

**Image 1, `books-to-gift-this-christmas-flatlay.jpg` (no person, Format A):** Seedream 4.5 on Higgsfield, Unlimited ON, 4K, portrait 2:3. Attach (1) Command Centre `stylerefs` doc `sr-flatlay-grid`, (2) this look's product sheet. Garbled or soft title letters: re-run on Nano Banana Pro 2K. Colour follows factory section 4 (as pink as the look).

```
Using the first image as a style reference for the styling, the fullness and the title lettering, not an exact copy, please make me a very realistic overhead flat lay photo of the products in the second image. I can't use the exact Amazon images outside of Amazon, so this needs to be a new photo. Shot straight down, portrait 2:3, like a good-quality photo taken on a phone. The gifts are arranged as one abundant styled group, pieces overlapping and touching, on a chunky cream knit throw: a cozy winter romance novel, a page-turning thriller, rechargeable clip-on book light, quilted pink book sleeve, reading journal, tassel bookmark set, wooden thumb page holder. Each item matches its screenshot in colour, shape and detail. Tucked in around them, filling the frame edge to edge with almost no empty background: an iced latte in a clear glass, a small bunch of pink tulips, a pair of reading glasses, a sugar cookie on a gingham napkin and a small candle. Every product sits fully inside the frame. Soft natural window light, gentle real shadows, visible fabric texture, true-to-life materials, small real-life imperfections, photorealistic real-world photography. Across the upper third, set directly on the photo, a large two-style title: "BOOK LOVER" in a bold high-contrast serif in capitals, with "gift bundle" beneath it in a thick flowing brush script, both in near-black, perfectly spelled, sharp edges, high contrast, filling about two thirds of the width. No logos, no brand names, no labels or printing on products or packaging, no watermark, no person, no other text.
```

**Image 2, `books-to-gift-this-christmas-lifestyle.jpg` (Tommy Kate, candid full shot):** Google Gemini first; Nano Banana Pro 2K on Higgsfield if Gemini is out or the result fails. Attach (1) style reference `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/src/lifestyle/pink-cat-halloween-costume-lifestyle.jpg`, (2) the Omni seed `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/public/images/library/avatar-seed-omni-reference.png` as a JPEG under 400 KB, (3) this look's product sheet.

```
Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference. The reference sheet is the second image. Using the first image as a style reference, not an exact copy, please make me one single very realistic lifestyle photo, not a collage or grid. I can't use the exact Amazon images, so this is a new photo of the products in the third image, each matching its screenshot in colour and detail. Setting: the window seat in her farmhouse living room on a snowy afternoon, pink gingham cushions, a stack of books with plain unprinted covers, her golden retriever resting its head on the cushion, in December. She is curled into the window seat reading by the clip-on book light, the quilted pink book sleeve beside her, looking up from the page with a small candid smile. She is wearing an oversized candy pink turtleneck sweater and cream knit leggings. Her hair is in a loose braid over one shoulder. Nails: pale pink. Her glitter-flecked pink iced coffee tumbler with a lavender straw, saturated candy pink, never pale, is on the window ledge. Other pink in the frame: the candy pink sweater, the quilted pink book sleeve and the pink gingham cushions; pink clothes and other pink pieces are welcome alongside the tumbler. The register is quiet wealth, lived in: a real farmhouse that is nice but never showy, clean but not sterile, with small signs of a real life. Format: candid full shot. Her face is visible in a candid, natural moment, not posed to the camera. The main subject sits in the right third of the frame with calmer negative space on the left, natural perspective and believable scale. Portrait 2:3. Light: soft snowy daylight from the window. Shot on a mirrorless camera with a 50mm lens at f/2, natural depth of field and soft natural bokeh, photorealistic, real-world photography, true-to-life textures, real skin and fabric texture, natural imperfections, nothing glossy. No lettering, no signs, no logos, no text anywhere in the frame, no brand marks on any product. Not a Paris apartment, cafe, marble room, mansion or influencer studio.
```

**Site alt text:** flat lay: Overhead flat lay on a cream knit of two books with plain covers, a clip-on book light, quilted pink book sleeve, reading journal, tassel bookmarks and a wooden page holder. · lifestyle: Woman in a candy pink turtleneck reading in a farmhouse window seat with pink gingham cushions on a snowy day, clip-on book light, golden retriever resting beside her.

**Pin 1, flat lay** · Mon 7 Dec 2026 13:30 ET · board `Pink Home, Dorm and Car Finds | Amazon` > section `Christmas and Gift Guides` · link: this look's Idea List (`https://www.amazon.com/shop/thedigitalincomeedit/list/<id>`) · AI label ON

- Overlay (on the image): BOOK LOVER / gift bundle
- Title: Books as Gifts: A Cozy Book Lover Gift Bundle With a Book Light, Sleeve and Reading Journal
- Description: Books as gifts, done properly: one cozy winter romance, one page-turning thriller, a rechargeable clip-on book light, a quilted pink book sleeve, a reading journal, tassel bookmarks and a wooden page holder. A book alone can feel like homework. A book with the whole reading setup feels like a night off, which is what she wants. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #bookgifts #booklover #bookishgifts #readingnook
- Alt text: Overhead flat lay on a cream knit of two books with plain covers, a clip-on book light, quilted pink book sleeve, reading journal, tassel bookmarks and a wooden page holder.

**Pin 2, lifestyle** · Thu 10 Dec 2026 20:30 ET · same board and section · same Idea List link · AI label ON, "includes an AI-generated person" ticked

- Title: Book Lover Gift Ideas for Her: The Snowy Window Seat Reading Nook in Pink and Gingham
- Description: Book lover gift ideas for the girl who reads by the window when it snows: a clip-on book light, a quilted pink book sleeve, a reading journal and two new books with nothing else on the calendar. Dog on the cushion, iced coffee slowly going warm. Save this for the friend whose to-be-read pile is taller than her Christmas tree. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #booklover #bookgifts #readingnook #cozyreading
- Alt text: Woman in a candy pink turtleneck reading in a farmhouse window seat with pink gingham cushions on a snowy day, clip-on book light, golden retriever resting beside her.

**Instagram @itstommykate feed post** · Mon 7 Dec 2026 19:00 ET · carousel: lifestyle photo first, flat lay second · AI label ON · check the caption panel says `itstommykate` before Share

```
snow day, window seat, dog on the cushion, new book. the only thing missing was a book light and now I have one 🎀 whole reading bundle is linked in my Amazon storefront (link in bio) #ad #bookgifts #booklover
```


---

### 12. Hostess Gifts

**Page:** `/lifestyle/pretty-hostess-gifts` · category `gifts` · season `Holiday` · file `src/lifestyle/pretty-hostess-gifts.json` (committed, `draft: true`)

**Page title (H1):** Pretty Hostess Gifts for Thanksgiving and Christmas

**Intro:** Showing up empty-handed is not an option, and neither are the sad flowers from the checkout lane. A good hostess gift is something she can use after everyone leaves: a nice candle, linen tea towels, a small olive wood board, a jar of honey. Tie it with ribbon and walk in like a grown-up.

**Items to source (the page lists them in this order):**

1. Linen tea towel set
2. Olive wood serving board
3. Candle in a ceramic vessel
4. Raw honey jar with wooden dipper
5. Scalloped linen cocktail napkins
6. Gold cheese knife set
7. Pink taper candles

**Idea List:** title `Pretty Hostess Gifts for Thanksgiving and Christmas` · description: Showing up empty-handed is not an option, and neither are the sad flowers from the checkout lane. Every piece is linked here.

**Image 1, `pretty-hostess-gifts-flatlay.jpg` (no person, Format B):** Seedream 4.5 on Higgsfield, Unlimited ON, 4K, portrait 2:3. Attach (1) Command Centre `stylerefs` doc `sr-that-girl-amazon-finds-script`, (2) this look's product sheet. Garbled or soft title letters: re-run on Nano Banana Pro 2K. Colour follows factory section 4 (as pink as the look).

```
Using the first image as a style reference for the layout, the fullness and the title lettering, not an exact copy, please make me a "that girl" shoppable Amazon finds collage for Pinterest, portrait 2:3, on a soft cream with a faint linen texture background with a faint paper texture. I can't use the exact Amazon images outside of Amazon, so please create a new clean cut-out product photo of each item in the second image, each with a soft drop shadow: linen tea towel set, olive wood serving board, candle in a ceramic vessel, raw honey jar with wooden dipper, scalloped linen cocktail napkins, gold cheese knife set, pink taper candles. Add a sprig of rosemary, a small pear and a satin ribbon bow. Pack them around a central title so the whole canvas is full edge to edge, items overlapping slightly, every product fully inside the frame. Add a few tiny accents: small hearts, little sparkles and one small bow. In the middle, set directly on the background, a large two-style title: "HOSTESS GIFTS" in a bold high-contrast serif with "thank you" in a thick flowing brush script, deep plum, perfectly spelled, crisp and fully legible, filling about half the width. Each item matches its screenshot in colour, shape and detail and looks like a real photo, not a render, with true-to-life materials. No logos, no brand names, no labels or printing on products or packaging, no prices, no person, no other text.
```

**Image 2, `pretty-hostess-gifts-lifestyle.jpg` (Tommy Kate, over-the-shoulder walk-away):** Google Gemini first; Nano Banana Pro 2K on Higgsfield if Gemini is out or the result fails. Attach (1) style reference `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/src/lifestyle/pink-graduation-gown-halloween-costume-lifestyle.jpg`, (2) the Omni seed `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/public/images/library/avatar-seed-omni-reference.png` as a JPEG under 400 KB, (3) this look's product sheet.

```
Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference. The reference sheet is the second image. Using the first image as a style reference, not an exact copy, please make me one single very realistic lifestyle photo, not a collage or grid. I can't use the exact Amazon images, so this is a new photo of the products in the third image, each matching its screenshot in colour and detail. Setting: a gravel farm lane lined with split rail fence in the early evening, the pasture lightly frosted and the farmhouse windows glowing behind her, in late November. Seen from behind over her shoulder as she walks down the lane carrying a woven basket holding the olive wood board, linen tea towels, candle and honey, tied with a pink satin ribbon. She is wearing a long cream puffer coat, a candy pink knit scarf, jeans and brown leather boots. Her hair is in a low ponytail. Nails: soft pink. Her glitter-flecked pink iced coffee tumbler with a lavender straw, saturated candy pink, never pale, is in her free hand. Other pink in the frame: the candy pink scarf and the pink ribbon on the basket; pink clothes and other pink pieces are welcome alongside the tumbler. The register is quiet wealth, lived in: a real farmhouse that is nice but never showy, clean but not sterile, with small signs of a real life. Format: over-the-shoulder walk-away. Her face is turned away from the camera. The main subject sits in the right third of the frame with calmer negative space on the left, natural perspective and believable scale. Portrait 2:3. Light: golden hour, low warm sun. Shot on a mirrorless camera with a 50mm lens at f/2, natural depth of field and soft natural bokeh, photorealistic, real-world photography, true-to-life textures, real skin and fabric texture, natural imperfections, nothing glossy. No lettering, no signs, no logos, no text anywhere in the frame, no brand marks on any product. Not a Paris apartment, cafe, marble room, mansion or influencer studio.
```

**Site alt text:** flat lay: Shoppable collage on cream of linen tea towels, an olive wood board, a ceramic candle, honey with a dipper, scalloped cocktail napkins, a gold cheese knife set and pink taper candles. · lifestyle: Woman in a cream puffer coat and candy pink scarf seen from behind on a frosty farm lane, carrying a hostess basket with an olive wood board, tea towels and pink ribbon.

**Pin 1, flat lay** · Thu 12 Nov 2026 13:30 ET · board `Legally Blonde Outfits | Pink Amazon Fashion` > section `Thanksgiving` · link: this look's Idea List (`https://www.amazon.com/shop/thedigitalincomeedit/list/<id>`) · AI label ON

- Overlay (on the image): HOSTESS GIFTS / thank you
- Title: Pretty Hostess Gifts for Thanksgiving and Christmas: Tea Towels, Olive Wood and Honey
- Description: Pretty hostess gifts for Thanksgiving, Friendsgiving and every Christmas party after: linen tea towels, an olive wood serving board, a ceramic candle, honey with a wooden dipper, scalloped cocktail napkins, a gold cheese knife set and pink taper candles. Pick two, tie them with ribbon, and give her something she can use when the dishes are done. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #hostessgifts #thanksgiving #friendsgiving
- Alt text: Shoppable collage on cream of linen tea towels, an olive wood board, a ceramic candle, honey with a dipper, scalloped cocktail napkins, a gold cheese knife set and pink taper candles.

**Pin 2, lifestyle** · Sun 15 Nov 2026 20:30 ET · same board and section · same Idea List link · AI label ON, "includes an AI-generated person" ticked

- Title: Hostess Gift Basket Ideas: What to Bring to Thanksgiving Dinner That She'll Keep Using
- Description: Hostess gift basket ideas for the dinner you were invited to and definitely did not cook for: an olive wood board, linen tea towels, a candle and a jar of honey tucked into a woven basket and tied with a pink ribbon. Walked over at golden hour, obviously. Save this before you get invited anywhere this holiday season and panic. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #hostessgifts #giftbasketideas #thanksgivingdinner
- Alt text: Woman in a cream puffer coat and candy pink scarf seen from behind on a frosty farm lane, carrying a hostess basket with an olive wood board, tea towels and pink ribbon.

**Instagram @itstommykate feed post** · Thu 12 Nov 2026 19:00 ET · carousel: lifestyle photo first, flat lay second · AI label ON · check the caption panel says `itstommykate` before Share

```
rule: never show up empty handed. olive wood board, linen tea towels, candle, honey, pink ribbon, done 🎀 hostess basket is linked in my Amazon storefront (link in bio) #ad #hostessgifts #thanksgiving
```


---

### 13. New Moms

**Page:** `/lifestyle/gifts-for-new-moms` · category `gifts` · season `Holiday` · file `src/lifestyle/gifts-for-new-moms.json` (committed, `draft: true`)

**Page title (H1):** Gifts for New Moms (That Are Actually for Her)

**Intro:** Everybody shops for the baby. The new mom gets a pile of onesies and a cold cup of coffee. This list is only for her: a nursing-friendly robe, a giant water bottle, dry shampoo, a silk eye mask for stolen naps and a neck massager for the shoulders that carry everything.

**Items to source (the page lists them in this order):**

1. Nursing-friendly waffle robe
2. Large water bottle with handle and straw · note on page: "Hydration, one-handed."
3. Dry shampoo
4. Silk eye mask
5. Cordless neck and shoulder massager
6. Snack caddy organizer
7. Soft pink knit baby blanket · note on page: "Okay, one thing for the baby."

**Idea List:** title `Gifts for New Moms (That Are Actually for Her)` · description: Everybody shops for the baby. Every piece is linked here.

**Image 1, `gifts-for-new-moms-flatlay.jpg` (no person, Format A):** Seedream 4.5 on Higgsfield, Unlimited ON, 4K, portrait 2:3. Attach (1) Command Centre `stylerefs` doc `sr-pink-dress-flatlay`, (2) this look's product sheet. Garbled or soft title letters: re-run on Nano Banana Pro 2K. Colour follows factory section 4 (as pink as the look).

```
Using the first image as a style reference for the styling, the fullness and the title lettering, not an exact copy, please make me a very realistic overhead flat lay photo of the products in the second image. I can't use the exact Amazon images outside of Amazon, so this needs to be a new photo. Shot straight down, portrait 2:3, like a good-quality photo taken on a phone. The gifts are arranged as one abundant styled group, pieces overlapping and touching, on rumpled pink satin: nursing-friendly waffle robe, large water bottle with handle and straw, dry shampoo, silk eye mask, cordless neck and shoulder massager, snack caddy organizer, soft pink knit baby blanket. Each item matches its screenshot in colour, shape and detail. Tucked in around them, filling the frame edge to edge with almost no empty background: a small bunch of pink peonies, an iced latte in a clear glass, a tiny knit baby bonnet and a hair claw clip. Every product sits fully inside the frame. Soft natural window light, gentle real shadows, visible fabric texture, true-to-life materials, small real-life imperfections, photorealistic real-world photography. Across the upper third, set directly on the photo, a large two-style title: "NEW MOM" in a bold high-contrast serif in capitals, with "gifts for her" beneath it in a thick flowing brush script, both in near-black, perfectly spelled, sharp edges, high contrast, filling about two thirds of the width. No logos, no brand names, no labels or printing on products or packaging, no watermark, no person, no other text.
```

**Image 2, `gifts-for-new-moms-lifestyle.jpg` (Tommy Kate, candid full shot):** Google Gemini first; Nano Banana Pro 2K on Higgsfield if Gemini is out or the result fails. Attach (1) style reference `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/src/lifestyle/pink-cat-halloween-costume-lifestyle.jpg`, (2) the Omni seed `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/public/images/library/avatar-seed-omni-reference.png` as a JPEG under 400 KB, (3) this look's product sheet.

```
Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference. The reference sheet is the second image. Using the first image as a style reference, not an exact copy, please make me one single very realistic lifestyle photo, not a collage or grid. I can't use the exact Amazon images, so this is a new photo of the products in the third image, each matching its screenshot in colour and detail. Setting: the upstairs nursery of her farmhouse, a white spindle crib, a gingham upholstered glider by the window and a small lamp on the dresser, in December. She sits in the glider folding the soft pink knit baby blanket into a gift basket that already holds the water bottle and silk eye mask, smiling down at the basket. She is wearing a candy pink knit cardigan over a cream tee and soft grey joggers. Her hair is in a relaxed half-up twist. Nails: bare and natural. Her glitter-flecked pink iced coffee tumbler with a lavender straw, saturated candy pink, never pale, is on the windowsill beside the glider. Other pink in the frame: the candy pink cardigan and the pink knit baby blanket; pink clothes and other pink pieces are welcome alongside the tumbler. The register is quiet wealth, lived in: a real farmhouse that is nice but never showy, clean but not sterile, with small signs of a real life. Format: candid full shot. Her face is visible in a candid, natural moment, not posed to the camera. The main subject sits in the right third of the frame with calmer negative space on the left, natural perspective and believable scale. Portrait 2:3. Light: soft north window light. Shot on a mirrorless camera with a 50mm lens at f/2, natural depth of field and soft natural bokeh, photorealistic, real-world photography, true-to-life textures, real skin and fabric texture, natural imperfections, nothing glossy. No lettering, no signs, no logos, no text anywhere in the frame, no brand marks on any product. Not a Paris apartment, cafe, marble room, mansion or influencer studio.
```

**Site alt text:** flat lay: Overhead flat lay on pink satin of a waffle robe, a large water bottle, dry shampoo, a silk eye mask, a neck massager, a snack caddy and a soft pink knit baby blanket. · lifestyle: Woman in a candy pink cardigan sitting in a gingham glider in a farmhouse nursery, folding a pink knit baby blanket into a new mom gift basket with a water bottle.

**Pin 1, flat lay** · Sat 12 Dec 2026 13:30 ET · board `Legally Blonde Outfits | Pink Amazon Fashion` > section `Christmas and Gift Guides` · link: this look's Idea List (`https://www.amazon.com/shop/thedigitalincomeedit/list/<id>`) · AI label ON

- Overlay (on the image): NEW MOM / gifts for her
- Title: Gifts for New Moms That Are Actually for Her: Waffle Robe, Eye Mask and a Giant Water Bottle
- Description: Gifts for new moms that are actually for her and not the baby: a nursing-friendly waffle robe, a giant water bottle with a straw, dry shampoo for day three of no shower, a silk eye mask for stolen naps, a cordless neck massager, a snack caddy and one soft pink baby blanket because you could not resist. She will remember who remembered her. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #newmomgifts #giftsfornewmom #giftsformom
- Alt text: Overhead flat lay on pink satin of a waffle robe, a large water bottle, dry shampoo, a silk eye mask, a neck massager, a snack caddy and a soft pink knit baby blanket.

**Pin 2, lifestyle** · Tue 15 Dec 2026 20:30 ET · same board and section · same Idea List link · AI label ON, "includes an AI-generated person" ticked

- Title: New Mom Gift Basket Ideas: Cozy Things for Her, Packed in the Nursery Glider
- Description: New mom gift basket ideas for the friend who just came home with a baby and has not sat down since: a waffle robe, a giant water bottle, a silk eye mask and a neck massager, with a soft pink knit blanket folded on top. Packed in the glider chair by the nursery window. Save it for the next baby shower on your calendar. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #newmomgifts #giftbasketideas #postpartumgifts #babyshowergift
- Alt text: Woman in a candy pink cardigan sitting in a gingham glider in a farmhouse nursery, folding a pink knit baby blanket into a new mom gift basket with a water bottle.

**Instagram @itstommykate feed post** · Sat 12 Dec 2026 19:00 ET · carousel: lifestyle photo first, flat lay second · AI label ON · check the caption panel says `itstommykate` before Share

```
packing a basket for a brand new mama and not one thing in it is for the baby. ok, one blanket. robe, eye mask, giant water bottle 🎀 linked in my Amazon storefront (link in bio) #ad #newmomgifts #giftsformom
```


---

### 14. Dog Lovers

**Page:** `/lifestyle/gifts-for-dog-moms` · category `gifts` · season `Holiday` · file `src/lifestyle/gifts-for-dog-moms.json` (committed, `draft: true`)

**Page title (H1):** Gifts for Dog Moms (and Their Very Spoiled Dogs)

**Intro:** Dog moms are the easiest people on earth to shop for, because the answer is always the dog. A pink gingham bandana, a treat pouch that doesn't look like hiking gear, a lint roller that works and a couch cover for muddy paws. She will cry a little. So will you.

**Items to source (the page lists them in this order):**

1. Pink gingham dog bandana
2. Blush leash and collar set
3. Silicone treat pouch in pink
4. Reusable pet hair remover roller · note on page: "The only one that actually works."
5. Paw cleaner cup
6. Slow feeder bowl in pink
7. Waterproof couch cover in cream

**Idea List:** title `Gifts for Dog Moms (and Their Very Spoiled Dogs)` · description: Dog moms are the easiest people on earth to shop for, because the answer is always the dog. Every piece is linked here.

**Image 1, `gifts-for-dog-moms-flatlay.jpg` (no person, Format B):** Seedream 4.5 on Higgsfield, Unlimited ON, 4K, portrait 2:3. Attach (1) Command Centre `stylerefs` doc `sr-amazon-fashion-looks-expensive`, (2) this look's product sheet. Garbled or soft title letters: re-run on Nano Banana Pro 2K. Colour follows factory section 4 (as pink as the look).

```
Using the first image as a style reference for the layout, the fullness and the title lettering, not an exact copy, please make me a "that girl" shoppable Amazon finds collage for Pinterest, portrait 2:3, on a soft dusty blue background with a faint paper texture. I can't use the exact Amazon images outside of Amazon, so please create a new clean cut-out product photo of each item in the second image, each with a soft drop shadow: pink gingham dog bandana, blush leash and collar set, silicone treat pouch in pink, reusable pet hair remover roller, paw cleaner cup, slow feeder bowl in pink, waterproof couch cover in cream. Add a tennis ball, a bone shaped biscuit and a small sprig of dried wildflowers. Pack them around a central title so the whole canvas is full edge to edge, items overlapping slightly, every product fully inside the frame. Add a few tiny accents: small hearts, little sparkles and one small bow. In the middle, set directly on the background, a large two-style title: "DOG MOM" in a bold high-contrast serif with "gift list" in a thick flowing brush script, near-black, perfectly spelled, crisp and fully legible, filling about half the width. Each item matches its screenshot in colour, shape and detail and looks like a real photo, not a render, with true-to-life materials. No logos, no brand names, no labels or printing on products or packaging, no prices, no person, no other text.
```

**Image 2, `gifts-for-dog-moms-lifestyle.jpg` (Tommy Kate, over-the-shoulder walk-away):** Google Gemini first; Nano Banana Pro 2K on Higgsfield if Gemini is out or the result fails. Attach (1) style reference `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/src/lifestyle/pink-graduation-gown-halloween-costume-lifestyle.jpg`, (2) the Omni seed `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/public/images/library/avatar-seed-omni-reference.png` as a JPEG under 400 KB, (3) this look's product sheet.

```
Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference. The reference sheet is the second image. Using the first image as a style reference, not an exact copy, please make me one single very realistic lifestyle photo, not a collage or grid. I can't use the exact Amazon images, so this is a new photo of the products in the third image, each matching its screenshot in colour and detail. Setting: the frosty pasture fence line on a bright winter morning, the red barn in the distance, in December. Seen from behind over her shoulder as she walks along the fence with her golden retriever on the blush leash, the dog wearing the pink gingham bandana, the treat pouch clipped at her hip. She is wearing a candy pink puffer vest over a cream sherpa pullover, leggings and muck boots. Her hair is in a high ponytail. Nails: short and bare. Her glitter-flecked pink iced coffee tumbler with a lavender straw, saturated candy pink, never pale, is in her free hand. Other pink in the frame: the candy pink puffer vest, the pink gingham bandana and the pink treat pouch; pink clothes and other pink pieces are welcome alongside the tumbler. The register is quiet wealth, lived in: a real farmhouse that is nice but never showy, clean but not sterile, with small signs of a real life. Format: over-the-shoulder walk-away. Her face is turned away from the camera. The main subject sits in the right third of the frame with calmer negative space on the left, natural perspective and believable scale. Portrait 2:3. Light: clear low winter sunlight. Shot on a mirrorless camera with a 85mm lens at f/2.8, natural depth of field and soft natural bokeh, photorealistic, real-world photography, true-to-life textures, real skin and fabric texture, natural imperfections, nothing glossy. No lettering, no signs, no logos, no text anywhere in the frame, no brand marks on any product. Not a Paris apartment, cafe, marble room, mansion or influencer studio.
```

**Site alt text:** flat lay: Shoppable collage on dusty blue of a pink gingham dog bandana, blush leash and collar, pink treat pouch, pet hair roller, paw cleaner cup, pink slow feeder bowl and a couch cover. · lifestyle: Woman in a candy pink puffer vest seen from behind walking a golden retriever in a pink gingham bandana along a frosty pasture fence, red barn in the distance.

**Pin 1, flat lay** · Sat 5 Dec 2026 13:30 ET · board `Legally Blonde Outfits | Pink Amazon Fashion` > section `Christmas and Gift Guides` · link: this look's Idea List (`https://www.amazon.com/shop/thedigitalincomeedit/list/<id>`) · AI label ON

- Overlay (on the image): DOG MOM / gift list
- Title: Gifts for Dog Moms: Gingham Bandana, Blush Leash, Treat Pouch and a Couch-Saving Cover
- Description: Gifts for dog moms who say the dog is the favourite child and mean it: a pink gingham bandana, a blush leash and collar set, a silicone treat pouch, a pet hair remover roller that actually works, a paw cleaner cup, a slow feeder bowl and a waterproof couch cover. Shopping for her means shopping for the dog. She will not mind at all. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #dogmom #doggifts #giftsfordoglovers #dogmomgifts
- Alt text: Shoppable collage on dusty blue of a pink gingham dog bandana, blush leash and collar, pink treat pouch, pet hair roller, paw cleaner cup, pink slow feeder bowl and a couch cover.

**Pin 2, lifestyle** · Tue 8 Dec 2026 20:30 ET · same board and section · same Idea List link · AI label ON, "includes an AI-generated person" ticked

- Title: Dog Mom Gift Ideas: A Pink Gingham Bandana Walk With a Golden Retriever on the Farm
- Description: Dog mom gift ideas for a frosty pasture walk: a pink gingham bandana on the golden retriever, a blush leash, a treat pouch clipped at the hip and a paw cleaner waiting by the back door. The dog is wearing gingham and has never been happier about anything. Save this for the friend whose camera roll is ninety percent dog. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #dogmom #goldenretriever #doggifts #dogmomgifts
- Alt text: Woman in a candy pink puffer vest seen from behind walking a golden retriever in a pink gingham bandana along a frosty pasture fence, red barn in the distance.

**Instagram @itstommykate feed post** · Sat 5 Dec 2026 19:00 ET · carousel: lifestyle photo first, flat lay second · AI label ON · check the caption panel says `itstommykate` before Share

```
the dog got a gingham bandana and now refuses to be photographed without it 🎀 leash, treat pouch, paw cleaner, all linked in my Amazon storefront (link in bio) #ad #dogmom #doggifts
```


---

### 15. Gamer Girls

**Page:** `/lifestyle/pink-gaming-gifts-for-girl-gamers` · category `gifts` · season `Holiday` · file `src/lifestyle/pink-gaming-gifts-for-girl-gamers.json` (committed, `draft: true`)

**Page title (H1):** Pink Gaming Gifts for Girl Gamers

**Intro:** Gamer girls do not need another thing with a skull on it. They want the setup to look as good as it plays: candy pink headphones, a pastel keycap set, a desk mat big enough for the whole mouse arc, a controller charging dock and lights that don't scream gamer bro.

**Items to source (the page lists them in this order):**

1. Candy pink wireless over-ear headphones
2. Pink wireless gaming mouse
3. Extended desk mat in pink
4. Pastel pink keycap set
5. Controller charging dock · note on page: "Check it fits her console."
6. Soft LED light bar
7. Keyboard wrist rest cushion

**Idea List:** title `Pink Gaming Gifts for Girl Gamers` · description: Gamer girls do not need another thing with a skull on it. Every piece is linked here.

**Image 1, `pink-gaming-gifts-for-girl-gamers-flatlay.jpg` (no person, Format A):** Seedream 4.5 on Higgsfield, Unlimited ON, 4K, portrait 2:3. Attach (1) Command Centre `stylerefs` doc `sr-flatlay-grid`, (2) this look's product sheet. Garbled or soft title letters: re-run on Nano Banana Pro 2K. Colour follows factory section 4 (as pink as the look).

```
Using the first image as a style reference for the styling, the fullness and the title lettering, not an exact copy, please make me a very realistic overhead flat lay photo of the products in the second image. I can't use the exact Amazon images outside of Amazon, so this needs to be a new photo. Shot straight down, portrait 2:3, like a good-quality photo taken on a phone. The gifts are arranged as one abundant styled group, pieces overlapping and touching, on fluffy pink faux fur: candy pink wireless over-ear headphones, pink wireless gaming mouse, extended desk mat in pink, pastel pink keycap set, controller charging dock, soft LED light bar, keyboard wrist rest cushion. Each item matches its screenshot in colour, shape and detail. Tucked in around them, filling the frame edge to edge with almost no empty background: an iced latte in a clear cup, a claw clip, a small succulent and a few pink cable ties. Every product sits fully inside the frame. Soft natural window light, gentle real shadows, visible fabric texture, true-to-life materials, small real-life imperfections, photorealistic real-world photography. Across the upper third, set directly on the photo, a large two-style title: "GAMER GIRL" in a bold high-contrast serif in capitals, with "gift list" beneath it in a thick flowing brush script, both in near-black, perfectly spelled, sharp edges, high contrast, filling about two thirds of the width. No logos, no brand names, no labels or printing on products or packaging, no watermark, no person, no other text.
```

**Image 2, `pink-gaming-gifts-for-girl-gamers-lifestyle.jpg` (Tommy Kate, over-the-shoulder walk-away):** Google Gemini first; Nano Banana Pro 2K on Higgsfield if Gemini is out or the result fails. Attach (1) style reference `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/src/lifestyle/pink-graduation-gown-halloween-costume-lifestyle.jpg`, (2) the Omni seed `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/public/images/library/avatar-seed-omni-reference.png` as a JPEG under 400 KB, (3) this look's product sheet.

```
Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference. The reference sheet is the second image. Using the first image as a style reference, not an exact copy, please make me one single very realistic lifestyle photo, not a collage or grid. I can't use the exact Amazon images, so this is a new photo of the products in the third image, each matching its screenshot in colour and detail. Setting: the pink attic gaming loft at night, sloped ceiling beams, a low table with the pink desk mat and pastel keyboard, a screen showing only a soft abstract colour glow with no game imagery, in December. Seen from behind and slightly to the side as she sits cross-legged on a big floor cushion with a controller in her hands and the candy pink headphones on, her golden retriever sprawled on the cushion beside her. She is wearing an oversized cream hoodie, candy pink sweatpants and fuzzy socks. Her hair is in a loose high bun. Nails: pastel pink. Her glitter-flecked pink iced coffee tumbler with a lavender straw, saturated candy pink, never pale, is on the low table beside the keyboard. Other pink in the frame: the candy pink headphones, the candy pink sweatpants and the pink desk mat; pink clothes and other pink pieces are welcome alongside the tumbler. The register is quiet wealth, lived in: a real farmhouse that is nice but never showy, clean but not sterile, with small signs of a real life. Format: over-the-shoulder walk-away. Her face is turned away from the camera. The main subject sits in the right third of the frame with calmer negative space on the left, natural perspective and believable scale. Portrait 2:3. Light: warm practical lamps with a soft pink and violet LED glow. Shot on a mirrorless camera with a 35mm lens at f/2, natural depth of field and soft natural bokeh, photorealistic, real-world photography, true-to-life textures, real skin and fabric texture, natural imperfections, nothing glossy. No lettering, no signs, no logos, no text anywhere in the frame, no brand marks on any product. Not a Paris apartment, cafe, marble room, mansion or influencer studio.
```

**Site alt text:** flat lay: Overhead flat lay on pink faux fur of candy pink headphones, a pink wireless mouse, a pink desk mat, pastel keycaps, a controller charging dock, a light bar and a wrist rest. · lifestyle: Woman in candy pink headphones seen from behind playing on a floor cushion in a pink attic gaming loft at night, golden retriever beside her, pink desk mat and soft LED glow.

**Pin 1, flat lay** · Sun 29 Nov 2026 13:30 ET · board `Legally Blonde Outfits | Pink Amazon Fashion` > section `Christmas and Gift Guides` · link: this look's Idea List (`https://www.amazon.com/shop/thedigitalincomeedit/list/<id>`) · AI label ON

- Overlay (on the image): GAMER GIRL / gift list
- Title: Pink Gaming Gifts for Girl Gamers: Candy Pink Headphones, Keycaps and a Cute Desk Setup
- Description: Pink gaming gifts for girl gamers who want the setup to look as good as it plays: candy pink wireless headphones, a pink wireless mouse, an extended desk mat, a pastel keycap set, a controller charging dock, a soft LED light bar and a wrist rest. Nothing with a skull on it. Just a pretty pink corner she never wants to leave. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #gamergirl #gaminggifts #pinkgamingsetup #giftsforgamers
- Alt text: Overhead flat lay on pink faux fur of candy pink headphones, a pink wireless mouse, a pink desk mat, pastel keycaps, a controller charging dock, a light bar and a wrist rest.

**Pin 2, lifestyle** · Wed 2 Dec 2026 20:30 ET · same board and section · same Idea List link · AI label ON, "includes an AI-generated person" ticked

- Title: Cute Gaming Setup Gift Ideas: A Pink Attic Gaming Loft With Candy Pink Headphones
- Description: Cute gaming setup gift ideas from the pink attic loft: candy pink headphones, a pink desk mat, a pastel keyboard and soft LED light, with the dog asleep on the floor cushion like a very large support animal. Late night, one more round, no regrets. Save this for the girl on your list who always says she is almost done playing. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #gamingsetup #gamergirl #pinkaesthetic #gaminggifts
- Alt text: Woman in candy pink headphones seen from behind playing on a floor cushion in a pink attic gaming loft at night, golden retriever beside her, pink desk mat and soft LED glow.

**Instagram @itstommykate feed post** · Sun 29 Nov 2026 19:00 ET · carousel: lifestyle photo first, flat lay second · AI label ON · check the caption panel says `itstommykate` before Share

```
player two has entered the loft 🎮 candy pink headphones, pastel keycaps, desk mat, soft LED glow, dog on the cushion as always 🎀 linked in my Amazon storefront (link in bio) #ad #gamergirl #gaminggifts
```


---

### 16. Self-Care Night In

**Page:** `/lifestyle/self-care-night-in-gift-ideas` · category `beauty` · season `Holiday` · file `src/lifestyle/self-care-night-in-gift-ideas.json` (committed, `draft: true`)

**Page title (H1):** Self-Care Night In Gift Ideas for Women

**Intro:** The best self-care gift is permission to do nothing for one night. Put it in a basket: a bath soak, a bamboo tub tray, a satin robe, a cooling eye mask, a sheet mask set and a bath pillow. She will say it is too much. She will use every piece by Sunday.

**Items to source (the page lists them in this order):**

1. Bamboo bathtub caddy tray
2. Bath soak salts
3. Pink satin robe
4. Cooling gel eye mask
5. Hydrating sheet mask set
6. Silicone face scrubber
7. Pink bath pillow

**Idea List:** title `Self-Care Night In Gift Ideas for Women` · description: The best self-care gift is permission to do nothing for one night. Every piece is linked here.

**Image 1, `self-care-night-in-gift-ideas-flatlay.jpg` (no person, Format B):** Seedream 4.5 on Higgsfield, Unlimited ON, 4K, portrait 2:3. Attach (1) Command Centre `stylerefs` doc `sr-soft-pink-collage`, (2) this look's product sheet. Garbled or soft title letters: re-run on Nano Banana Pro 2K. Colour follows factory section 4 (as pink as the look).

```
Using the first image as a style reference for the layout, the fullness and the title lettering, not an exact copy, please make me a "that girl" shoppable Amazon finds collage for Pinterest, portrait 2:3, on a soft cream background with a faint paper texture. I can't use the exact Amazon images outside of Amazon, so please create a new clean cut-out product photo of each item in the second image, each with a soft drop shadow: bamboo bathtub caddy tray, bath soak salts, pink satin robe, cooling gel eye mask, hydrating sheet mask set, silicone face scrubber, pink bath pillow. Add a small bunch of pink tulips, a satin hair bow and a lip gloss. Pack them around a central title so the whole canvas is full edge to edge, items overlapping slightly, every product fully inside the frame. Add a few tiny accents: small hearts, little sparkles and one small bow. In the middle, set directly on the background, a large two-style title: "NIGHT IN" in a bold high-contrast serif with "self-care" in a thick flowing brush script, deep plum, perfectly spelled, crisp and fully legible, filling about half the width. Each item matches its screenshot in colour, shape and detail and looks like a real photo, not a render, with true-to-life materials. No logos, no brand names, no labels or printing on products or packaging, no prices, no person, no other text.
```

**Image 2, `self-care-night-in-gift-ideas-lifestyle.jpg` (Tommy Kate, chin-down outfit crop):** Google Gemini first; Nano Banana Pro 2K on Higgsfield if Gemini is out or the result fails. Attach (1) style reference `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/src/lifestyle/pink-workwear-freezing-office-lifestyle.jpg`, (2) the Omni seed `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/public/images/library/avatar-seed-omni-reference.png` as a JPEG under 400 KB, (3) this look's product sheet.

```
Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference. The reference sheet is the second image. Using the first image as a style reference, not an exact copy, please make me one single very realistic lifestyle photo, not a collage or grid. I can't use the exact Amazon images, so this is a new photo of the products in the third image, each matching its screenshot in colour and detail. Setting: the edge of the clawfoot tub in her farmhouse bathroom in the evening, white beadboard walls, candles and a small lamp glowing, the bamboo tray across the tub holding a book and a sheet mask packet, in December. A chin-down crop from her collarbone to her knees as she sits on the tub edge and swirls bath soak into the water with one hand. She is wearing the pink satin robe tied at the waist and plush spa socks. Her hair is twisted up in a claw clip. Nails: sheer pink. Her glitter-flecked pink iced coffee tumbler with a lavender straw, saturated candy pink, never pale, is on the bamboo tray. Other pink in the frame: the pink satin robe and the pink bath pillow; pink clothes and other pink pieces are welcome alongside the tumbler. The register is quiet wealth, lived in: a real farmhouse that is nice but never showy, clean but not sterile, with small signs of a real life. Format: chin-down outfit crop. The frame is cropped just below her chin, so her face is not in the frame. The main subject sits in the right third of the frame with calmer negative space on the left, natural perspective and believable scale. Portrait 2:3. Light: warm candlelight and one small practical lamp. Shot on a mirrorless camera with a 35mm lens at f/1.8, natural depth of field and soft natural bokeh, photorealistic, real-world photography, true-to-life textures, real skin and fabric texture, natural imperfections, nothing glossy. No lettering, no signs, no logos, no text anywhere in the frame, no brand marks on any product. Not a Paris apartment, cafe, marble room, mansion or influencer studio.
```

**Site alt text:** flat lay: Shoppable collage on cream of a bamboo bathtub tray, bath soak, pink satin robe, cooling eye mask, sheet masks, a silicone face scrubber and a pink bath pillow. · lifestyle: Chin-down crop of a woman in a pink satin robe on the edge of a clawfoot tub in a farmhouse bathroom, swirling bath soak, bamboo tray, candles and a pink bath pillow.

**Pin 1, flat lay** · Tue 15 Dec 2026 13:30 ET · board `Legally Blonde Outfits | Pink Amazon Fashion` > section `Christmas and Gift Guides` · link: this look's Idea List (`https://www.amazon.com/shop/thedigitalincomeedit/list/<id>`) · AI label ON

- Overlay (on the image): NIGHT IN / self-care
- Title: Self-Care Night In Gift Ideas for Women: Bath Tray, Satin Robe, Eye Mask and Bath Soak
- Description: Self-care night in gift ideas for women who never sit down: a bamboo bathtub tray, a bath soak, a pink satin robe, a cooling gel eye mask, a sheet mask set, a silicone face scrubber and a bath pillow. Put it all in one basket with a note that says the dishes can wait. That note is the real gift, and she will read it twice. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #selfcare #selfcaregifts #spanight #giftsforher
- Alt text: Shoppable collage on cream of a bamboo bathtub tray, bath soak, pink satin robe, cooling eye mask, sheet masks, a silicone face scrubber and a pink bath pillow.

**Pin 2, lifestyle** · Fri 18 Dec 2026 20:30 ET · same board and section · same Idea List link · AI label ON, "includes an AI-generated person" ticked

- Title: At Home Spa Night Ideas: A Clawfoot Tub, Pink Satin Robe and a Bamboo Bath Tray
- Description: At home spa night ideas for the woman who deserves one evening off: a pink satin robe, a bamboo tray across the clawfoot tub, bath soak swirling in the water and candles lit in the farmhouse bathroom. Phone on silent, iced coffee on the tray, which is very much allowed. Save this for the tired friend who never asks for anything. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #spanight #selfcarenight #athomespa #selfcaregifts
- Alt text: Chin-down crop of a woman in a pink satin robe on the edge of a clawfoot tub in a farmhouse bathroom, swirling bath soak, bamboo tray, candles and a pink bath pillow.

**Instagram @itstommykate feed post** · Tue 15 Dec 2026 19:00 ET · carousel: lifestyle photo first, flat lay second · AI label ON · check the caption panel says `itstommykate` before Share

```
phone on silent. tub running. satin robe on. nobody is allowed to need me for one hour 🎀 bath tray, soak, eye mask, all linked in my Amazon storefront (link in bio) #ad #selfcare #selfcaregifts
```


---

### 17. Party Outfits

**Page:** `/lifestyle/pink-holiday-party-outfits` · category `clothing` · season `Holiday` · file `src/lifestyle/pink-holiday-party-outfits.json` (committed, `draft: true`)

**Page title (H1):** Pink Holiday Party Outfits

**Intro:** Holiday party outfits should work for three parties in a row, not one. A pink velvet mini dress does the office party with black tights and the friend party with bare legs and a bow. Add crystal drops, sparkly Mary Janes, a beaded bag and a faux fur jacket for the walk to the car.

**Items to source (the page lists them in this order):**

1. Pink velvet long sleeve mini dress
2. Sheer black tights
3. Glitter Mary Jane heels
4. Satin bow hair clip
5. Crystal drop earrings
6. Beaded top handle mini bag in cream
7. Cropped faux fur jacket in cream

**Idea List:** title `Pink Holiday Party Outfits` · description: Holiday party outfits should work for three parties in a row, not one. Every piece is linked here.

**Image 1, `pink-holiday-party-outfits-flatlay.jpg` (no person, Format A):** Seedream 4.5 on Higgsfield, Unlimited ON, 4K, portrait 2:3. Attach (1) Command Centre `stylerefs` doc `sr-pink-dress-flatlay`, (2) this look's product sheet. Garbled or soft title letters: re-run on Nano Banana Pro 2K. Colour follows factory section 4 (as pink as the look).

```
Using the first image as a style reference for the styling, the fullness and the title lettering, not an exact copy, please make me a very realistic overhead flat lay photo of the products in the second image. I can't use the exact Amazon images outside of Amazon, so this needs to be a new photo. Shot straight down, portrait 2:3, like a good-quality photo taken on a phone. The outfit is laid out as if worn, top above bottom, shoes at the hem, bag at the hip, jewellery at the neckline, pieces overlapping and touching, on rumpled pink satin: pink velvet long sleeve mini dress, sheer black tights, glitter Mary Jane heels, satin bow hair clip, crystal drop earrings, beaded top handle mini bag in cream, cropped faux fur jacket in cream. Each item matches its screenshot in colour, shape and detail. Tucked in around them, filling the frame edge to edge with almost no empty background: an empty champagne coupe, a small bunch of pink roses, a lipstick, a blank party invitation card and a strand of gold tinsel. Every product sits fully inside the frame. Soft natural window light, gentle real shadows, visible fabric texture, true-to-life materials, small real-life imperfections, photorealistic real-world photography. Across the upper third, set directly on the photo, a large two-style title: "PARTY OUTFIT" in a bold high-contrast serif in capitals, with "pink velvet" beneath it in a thick flowing brush script, both in near-black, perfectly spelled, sharp edges, high contrast, filling about two thirds of the width. No logos, no brand names, no labels or printing on products or packaging, no watermark, no person, no other text.
```

**Image 2, `pink-holiday-party-outfits-lifestyle.jpg` (Tommy Kate, mirror selfie):** Google Gemini first; Nano Banana Pro 2K on Higgsfield if Gemini is out or the result fails. Attach (1) style reference `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/src/lifestyle/pink-suit-law-student-halloween-costume-lifestyle.jpg`, (2) the Omni seed `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/public/images/library/avatar-seed-omni-reference.png` as a JPEG under 400 KB, (3) this look's product sheet.

```
Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference. The reference sheet is the second image. Using the first image as a style reference, not an exact copy, please make me one single very realistic lifestyle photo, not a collage or grid. I can't use the exact Amazon images, so this is a new photo of the products in the third image, each matching its screenshot in colour and detail. Setting: the full-length mirror on the upstairs landing of her farmhouse in the evening, the banister wrapped in fresh garland and warm white lights, in December. She takes a mirror selfie with a plain phone case covering her face, the cream faux fur jacket over one arm and the beaded bag hanging from her wrist, ready to leave. She is wearing the pink velvet long sleeve mini dress, sheer black tights, glitter Mary Jane heels and crystal drop earrings. Her hair is half up with the satin bow clip. Nails: glossy candy pink. Her glitter-flecked pink iced coffee tumbler with a lavender straw, saturated candy pink, never pale, is on the banister ledge beside her. Other pink in the frame: the pink velvet dress; pink clothes and other pink pieces are welcome alongside the tumbler. The register is quiet wealth, lived in: a real farmhouse that is nice but never showy, clean but not sterile, with small signs of a real life. Format: mirror selfie. Her phone, in a plain case with no logo, covers her face. The main subject sits in the right third of the frame with calmer negative space on the left, natural perspective and believable scale. Portrait 2:3. Light: warm garland lights and a hallway sconce. Make it look like a good-quality photo taken on a phone in a mirror: phone camera seen in the mirror, 26mm phone lens, photorealistic, real-world photography, true-to-life textures, real skin and fabric texture, natural imperfections, nothing glossy. No lettering, no signs, no logos, no text anywhere in the frame, no brand marks on any product. Not a Paris apartment, cafe, marble room, mansion or influencer studio.
```

**Site alt text:** flat lay: Overhead flat lay on pink satin of a pink velvet mini dress, black tights, glitter Mary Janes, a satin bow clip, crystal drop earrings, a cream beaded bag and a faux fur jacket. · lifestyle: Mirror selfie on a farmhouse landing with garland of a woman in a pink velvet mini dress, black tights and glitter Mary Janes, faux fur jacket over her arm, phone covering face.

**Pin 1, flat lay** · Thu 10 Dec 2026 13:30 ET · board `Legally Blonde Outfits | Pink Amazon Fashion` > section `Christmas and Gift Guides` · link: this look's Idea List (`https://www.amazon.com/shop/thedigitalincomeedit/list/<id>`) · AI label ON

- Overlay (on the image): PARTY OUTFIT / pink velvet
- Title: Pink Holiday Party Outfits: A Velvet Mini Dress, Satin Bow and Sparkly Mary Janes
- Description: Pink holiday party outfits that work three parties in a row: a pink velvet long sleeve mini dress, sheer black tights for the office party, sparkly Mary Jane heels, a satin bow hair clip, crystal drop earrings, a beaded top handle bag and a cropped faux fur jacket. Swap the tights for bare legs on Saturday and nobody will clock the repeat. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #holidayoutfit #partyoutfit #pinkdress
- Alt text: Overhead flat lay on pink satin of a pink velvet mini dress, black tights, glitter Mary Janes, a satin bow clip, crystal drop earrings, a cream beaded bag and a faux fur jacket.

**Pin 2, lifestyle** · Sun 13 Dec 2026 20:30 ET · same board and section · same Idea List link · AI label ON, "includes an AI-generated person" ticked

- Title: Christmas Party Outfit Idea: Pink Velvet Mini Dress, Black Tights and a Faux Fur Jacket
- Description: Christmas party outfit idea, checked in the landing mirror on the way out the door: a pink velvet mini dress, sheer black tights, sparkly Mary Janes, a satin bow in half-up hair and a cream faux fur jacket over the arm. Garland on the banister, ride waiting in the drive. Save this for the holiday party you almost said no to. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #christmaspartyoutfit #holidayoutfit #velvetdress #pinkoutfit
- Alt text: Mirror selfie on a farmhouse landing with garland of a woman in a pink velvet mini dress, black tights and glitter Mary Janes, faux fur jacket over her arm, phone covering face.

**Instagram @itstommykate feed post** · Thu 10 Dec 2026 19:00 ET · carousel: lifestyle photo first, flat lay second · AI label ON · check the caption panel says `itstommykate` before Share

```
outfit check before the party: pink velvet, black tights, bow in the hair, sparkly shoes I will regret by 10pm 🎀 every piece is linked in my Amazon storefront (link in bio) #ad #holidayoutfit #partyoutfit
```


---

### 18. Pink Holiday Table

**Page:** `/lifestyle/pink-christmas-table-decor` · category `home-decor` · season `Holiday` · file `src/lifestyle/pink-christmas-table-decor.json` (committed, `draft: true`)

**Page title (H1):** A Pink Christmas Table That Looks Expensive

**Intro:** A pink Christmas table looks expensive when the pink is in the details and everything else is linen, wood and gold. Blush linen napkins, pink tapers in brass holders, scalloped plates and a runner of greenery do all the work. Nobody will guess it came in two boxes.

**Items to source (the page lists them in this order):**

1. Blush linen napkins
2. Pink taper candles
3. Brass taper candle holders
4. Scalloped white dinner plate set
5. Gold flatware set
6. Faux eucalyptus garland runner
7. Gold napkin rings

**Idea List:** title `A Pink Christmas Table That Looks Expensive` · description: A pink Christmas table looks expensive when the pink is in the details and everything else is linen, wood and gold. Every piece is linked here.

**Image 1, `pink-christmas-table-decor-flatlay.jpg` (no person, Format B):** Seedream 4.5 on Higgsfield, Unlimited ON, 4K, portrait 2:3. Attach (1) Command Centre `stylerefs` doc `sr-that-girl-amazon-finds-blush`, (2) this look's product sheet. Garbled or soft title letters: re-run on Nano Banana Pro 2K. Colour follows factory section 4 (as pink as the look).

```
Using the first image as a style reference for the layout, the fullness and the title lettering, not an exact copy, please make me a "that girl" shoppable Amazon finds collage for Pinterest, portrait 2:3, on a soft cream with a faint linen texture background with a faint paper texture. I can't use the exact Amazon images outside of Amazon, so please create a new clean cut-out product photo of each item in the second image, each with a soft drop shadow: blush linen napkins, pink taper candles, brass taper candle holders, scalloped white dinner plate set, gold flatware set, faux eucalyptus garland runner, gold napkin rings. Add sprigs of fresh pine, a clementine, a small pear and a little satin bow. Pack them around a central title so the whole canvas is full edge to edge, items overlapping slightly, every product fully inside the frame. Add a few tiny accents: small hearts, little sparkles and one small bow. In the middle, set directly on the background, a large two-style title: "PINK TABLE" in a bold high-contrast serif with "christmas dinner" in a thick flowing brush script, deep plum, perfectly spelled, crisp and fully legible, filling about half the width. Each item matches its screenshot in colour, shape and detail and looks like a real photo, not a render, with true-to-life materials. No logos, no brand names, no labels or printing on products or packaging, no prices, no person, no other text.
```

**Image 2, `pink-christmas-table-decor-lifestyle.jpg` (Tommy Kate, candid full shot):** Google Gemini first; Nano Banana Pro 2K on Higgsfield if Gemini is out or the result fails. Attach (1) style reference `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/src/lifestyle/pink-cat-halloween-costume-lifestyle.jpg`, (2) the Omni seed `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/public/images/library/avatar-seed-omni-reference.png` as a JPEG under 400 KB, (3) this look's product sheet.

```
Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference. The reference sheet is the second image. Using the first image as a style reference, not an exact copy, please make me one single very realistic lifestyle photo, not a collage or grid. I can't use the exact Amazon images, so this is a new photo of the products in the third image, each matching its screenshot in colour and detail. Setting: the long farmhouse dining table at dusk, a wide plank wood top with the eucalyptus runner down the middle and the kitchen in soft focus behind, in December. She leans over the table lighting the pink taper candles in their brass holders, the scalloped plates and blush napkins already set, glancing up with a small laugh. She is wearing a soft candy pink mohair sweater and a cream satin midi skirt. Her hair is in a low bun with loose face-framing pieces. Nails: glossy pink. Her glitter-flecked pink iced coffee tumbler with a lavender straw, saturated candy pink, never pale, is at the end of the table. Other pink in the frame: the candy pink sweater, the blush napkins and the pink tapers; pink clothes and other pink pieces are welcome alongside the tumbler. The register is quiet wealth, lived in: a real farmhouse that is nice but never showy, clean but not sterile, with small signs of a real life. Format: candid full shot. Her face is visible in a candid, natural moment, not posed to the camera. The main subject sits in the right third of the frame with calmer negative space on the left, natural perspective and believable scale. Portrait 2:3. Light: candlelight plus the last blue dusk light from the windows. Shot on a mirrorless camera with a 50mm lens at f/1.8, natural depth of field and soft natural bokeh, photorealistic, real-world photography, true-to-life textures, real skin and fabric texture, natural imperfections, nothing glossy. No lettering, no signs, no logos, no text anywhere in the frame, no brand marks on any product. Not a Paris apartment, cafe, marble room, mansion or influencer studio.
```

**Site alt text:** flat lay: Shoppable collage on cream of blush linen napkins, pink taper candles, brass candlesticks, scalloped white plates, gold flatware, a eucalyptus garland runner and gold napkin rings. · lifestyle: Woman in a candy pink mohair sweater lighting pink taper candles in brass holders on a long farmhouse table set with scalloped plates and blush linen napkins at dusk.

**Pin 1, flat lay** · Thu 17 Dec 2026 13:30 ET · board `Pink Home, Dorm and Car Finds | Amazon` > section `Christmas and Gift Guides` · link: this look's Idea List (`https://www.amazon.com/shop/thedigitalincomeedit/list/<id>`) · AI label ON

- Overlay (on the image): PINK TABLE / christmas dinner
- Title: Pink Christmas Table Decor That Looks Expensive: Blush Linen, Brass Candlesticks and Tapers
- Description: Pink Christmas table decor that looks expensive without trying too hard: blush linen napkins, pink taper candles, brass candlestick holders, scalloped white plates, gold flatware, a faux eucalyptus garland runner and gold napkin rings. Keep the pink in the details and let linen, wood and gold do the rest. Your family will think you hired someone. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #christmastable #tablescape #pinkchristmas
- Alt text: Shoppable collage on cream of blush linen napkins, pink taper candles, brass candlesticks, scalloped white plates, gold flatware, a eucalyptus garland runner and gold napkin rings.

**Pin 2, lifestyle** · Sun 20 Dec 2026 20:30 ET · same board and section · same Idea List link · AI label ON, "includes an AI-generated person" ticked

- Title: Pink Christmas Tablescape Ideas: Lighting the Tapers on a Farmhouse Dining Table
- Description: Pink Christmas tablescape ideas for a long farmhouse table: pink tapers in brass holders, scalloped plates, blush linen napkins and a eucalyptus runner, candles lit just before everyone sits down to eat. Warm, pretty and a little bit fancy. Save this for Christmas Eve dinner or the year you are finally the one hosting everybody. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #christmastablescape #pinkchristmas #farmhousetable
- Alt text: Woman in a candy pink mohair sweater lighting pink taper candles in brass holders on a long farmhouse table set with scalloped plates and blush linen napkins at dusk.

**Instagram @itstommykate feed post** · Thu 17 Dec 2026 19:00 ET · carousel: lifestyle photo first, flat lay second · AI label ON · check the caption panel says `itstommykate` before Share

```
lighting the tapers is my favourite 30 seconds of the whole holiday. pink candles, brass holders, scalloped plates, blush napkins 🎀 linked in my Amazon storefront (link in bio) #ad #christmastable #tablescape
```


---

### 19. White Elephant

**Page:** `/lifestyle/cute-white-elephant-gifts` · category `gifts` · season `Holiday` · file `src/lifestyle/cute-white-elephant-gifts.json` (committed, `draft: true`)

**Page title (H1):** White Elephant Gifts People Actually Fight Over

**Intro:** A great white elephant gift gets stolen three times. The trick is something everyone secretly wants but would never buy: a mini waffle maker, a massage gun, a tiny projector, a karaoke mic. Wrap it in pink paper so the whole room knows which one to steal.

**Items to source (the page lists them in this order):**

1. Mini waffle maker in pink
2. Mini massage gun
3. Portable mini projector · note on page: "Home projectors were one of last season's most searched gifts."
4. Cordless milk frother
5. Bluetooth karaoke microphone
6. Candle warmer lamp
7. Pink and gold wrapping paper rolls · note on page: "For the steal-me wrapping job."

**Idea List:** title `White Elephant Gifts People Actually Fight Over` · description: A great white elephant gift gets stolen three times. Every piece is linked here.

**Image 1, `cute-white-elephant-gifts-flatlay.jpg` (no person, Format A):** Seedream 4.5 on Higgsfield, Unlimited ON, 4K, portrait 2:3. Attach (1) Command Centre `stylerefs` doc `sr-flatlay-grid`, (2) this look's product sheet. Garbled or soft title letters: re-run on Nano Banana Pro 2K. Colour follows factory section 4 (as pink as the look).

```
Using the first image as a style reference for the styling, the fullness and the title lettering, not an exact copy, please make me a very realistic overhead flat lay photo of the products in the second image. I can't use the exact Amazon images outside of Amazon, so this needs to be a new photo. Shot straight down, portrait 2:3, like a good-quality photo taken on a phone. The gifts are arranged as one abundant styled group, pieces overlapping and touching, on warm wood floorboards: mini waffle maker in pink, mini massage gun, portable mini projector, cordless milk frother, bluetooth karaoke microphone, candle warmer lamp, pink and gold wrapping paper rolls. Each item matches its screenshot in colour, shape and detail. Tucked in around them, filling the frame edge to edge with almost no empty background: a spool of pink ribbon, a pair of scissors, blank gift tags, a sprig of pine and a loose string of fairy lights. Every product sits fully inside the frame. Soft natural window light, gentle real shadows, visible fabric texture, true-to-life materials, small real-life imperfections, photorealistic real-world photography. Across the upper third, set directly on the photo, a large two-style title: "WHITE ELEPHANT" in a bold high-contrast serif in capitals, with "steal-worthy" beneath it in a thick flowing brush script, both in near-black, perfectly spelled, sharp edges, high contrast, filling about two thirds of the width. No logos, no brand names, no labels or printing on products or packaging, no watermark, no person, no other text.
```

**Image 2, `cute-white-elephant-gifts-lifestyle.jpg` (Tommy Kate, chin-down outfit crop):** Google Gemini first; Nano Banana Pro 2K on Higgsfield if Gemini is out or the result fails. Attach (1) style reference `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/src/lifestyle/pink-workwear-freezing-office-lifestyle.jpg`, (2) the Omni seed `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/public/images/library/avatar-seed-omni-reference.png` as a JPEG under 400 KB, (3) this look's product sheet.

```
Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference. The reference sheet is the second image. Using the first image as a style reference, not an exact copy, please make me one single very realistic lifestyle photo, not a collage or grid. I can't use the exact Amazon images, so this is a new photo of the products in the third image, each matching its screenshot in colour and detail. Setting: inside the red barn decorated for a holiday party, string lights across the beams, hay bales with plaid blankets and a table of gifts wrapped in pink and gold paper behind her, in December. A chin-down crop from her collarbone to her waist as she hugs a gift wrapped in pink and gold paper to her chest like she has no intention of giving it back. She is wearing an oversized cream fair isle sweater with candy pink pattern details and light wash jeans. Her hair is in two loose low braids. Nails: candy pink. Her glitter-flecked pink iced coffee tumbler with a lavender straw, saturated candy pink, never pale, is in her other hand. Other pink in the frame: the pink and gold wrapped gift and the candy pink pattern in the sweater; pink clothes and other pink pieces are welcome alongside the tumbler. The register is quiet wealth, lived in: a real farmhouse that is nice but never showy, clean but not sterile, with small signs of a real life. Format: chin-down outfit crop. The frame is cropped just below her chin, so her face is not in the frame. The main subject sits in the right third of the frame with calmer negative space on the left, natural perspective and believable scale. Portrait 2:3. Light: warm string lights and practical lanterns inside the barn. Shot on a mirrorless camera with a 35mm lens at f/2, natural depth of field and soft natural bokeh, photorealistic, real-world photography, true-to-life textures, real skin and fabric texture, natural imperfections, nothing glossy. No lettering, no signs, no logos, no text anywhere in the frame, no brand marks on any product. Not a Paris apartment, cafe, marble room, mansion or influencer studio.
```

**Site alt text:** flat lay: Overhead flat lay on wood floorboards of a pink mini waffle maker, mini massage gun, portable projector, milk frother, karaoke mic, candle warmer lamp and pink and gold wrapping paper. · lifestyle: Chin-down crop of a woman in a cream fair isle sweater hugging a pink and gold wrapped gift inside a red barn lit with string lights for a white elephant party.

**Pin 1, flat lay** · Fri 11 Dec 2026 13:30 ET · board `Legally Blonde Outfits | Pink Amazon Fashion` > section `Christmas and Gift Guides` · link: this look's Idea List (`https://www.amazon.com/shop/thedigitalincomeedit/list/<id>`) · AI label ON

- Overlay (on the image): WHITE ELEPHANT / steal-worthy
- Title: White Elephant Gifts People Actually Fight Over: Mini Projector, Waffle Maker and More
- Description: White elephant gifts people actually fight over: a mini waffle maker, a mini massage gun, a portable projector, a cordless milk frother, a karaoke microphone, a candle warmer lamp and pink and gold wrapping paper so everyone spots the good one. The winner is what everybody wants and nobody buys. Expect it to get stolen three times. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #whiteelephant #whiteelephantgifts #giftexchange
- Alt text: Overhead flat lay on wood floorboards of a pink mini waffle maker, mini massage gun, portable projector, milk frother, karaoke mic, candle warmer lamp and pink and gold wrapping paper.

**Pin 2, lifestyle** · Mon 14 Dec 2026 20:30 ET · same board and section · same Idea List link · AI label ON, "includes an AI-generated person" ticked

- Title: Best White Elephant Gift Ideas for the Barn Christmas Party: Wrapped in Pink and Gold
- Description: Best white elephant gift ideas for a barn Christmas party under string lights: a mini projector, a waffle maker or a massage gun, wrapped in pink and gold so the whole room knows exactly which one to steal. Hold on tight when your number comes up. Save this for the gift swap where you refuse to go home with another candle. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #whiteelephant #giftexchange #christmasparty #whiteelephantideas
- Alt text: Chin-down crop of a woman in a cream fair isle sweater hugging a pink and gold wrapped gift inside a red barn lit with string lights for a white elephant party.

**Instagram @itstommykate feed post** · Fri 11 Dec 2026 19:00 ET · carousel: lifestyle photo first, flat lay second · AI label ON · check the caption panel says `itstommykate` before Share

```
white elephant strategy: wrap the good one in pink so everyone knows which one to steal. then steal it back 🎀 projector, waffle maker, massage gun, all linked in my Amazon storefront (link in bio) #ad #whiteelephant #giftexchange
```


---

### 20. For Mom

**Page:** `/lifestyle/pink-gifts-for-mom` · category `gifts` · season `Holiday` · file `src/lifestyle/pink-gifts-for-mom.json` (committed, `draft: true`)

**Page title (H1):** Gifts for Mom She Won't Return

**Intro:** Moms return gifts. It is a whole sport. The way around it is buying the upgraded version of something she already uses: a plush robe, a heated neck wrap, a digital photo frame you load before you wrap it and pink garden gloves for the beds she won't stop talking about. Returns department, defeated.

**Items to source (the page lists them in this order):**

1. Plush robe
2. Heated neck and shoulder wrap
3. Digital photo frame · note on page: "Load the photos before you wrap it."
4. Recipe box with cards
5. Soft wrap scarf
6. Birth flower necklace
7. Pink garden gloves and tool set

**Idea List:** title `Gifts for Mom She Won't Return` · description: Moms return gifts. Every piece is linked here.

**Image 1, `pink-gifts-for-mom-flatlay.jpg` (no person, Format A):** Seedream 4.5 on Higgsfield, Unlimited ON, 4K, portrait 2:3. Attach (1) Command Centre `stylerefs` doc `sr-pink-dress-flatlay`, (2) this look's product sheet. Garbled or soft title letters: re-run on Nano Banana Pro 2K. Colour follows factory section 4 (as pink as the look).

```
Using the first image as a style reference for the styling, the fullness and the title lettering, not an exact copy, please make me a very realistic overhead flat lay photo of the products in the second image. I can't use the exact Amazon images outside of Amazon, so this needs to be a new photo. Shot straight down, portrait 2:3, like a good-quality photo taken on a phone. The gifts are arranged as one abundant styled group, pieces overlapping and touching, on crumpled white linen: plush robe, heated neck and shoulder wrap, digital photo frame, recipe box with cards, soft wrap scarf, birth flower necklace, pink garden gloves and tool set. Each item matches its screenshot in colour, shape and detail. Tucked in around them, filling the frame edge to edge with almost no empty background: a small bunch of pink roses, a pair of reading glasses, a blank recipe card, an iced latte in a clear glass and a sprig of rosemary. Every product sits fully inside the frame. Soft natural window light, gentle real shadows, visible fabric texture, true-to-life materials, small real-life imperfections, photorealistic real-world photography. Across the upper third, set directly on the photo, a large two-style title: "GIFTS FOR MOM" in a bold high-contrast serif in capitals, with "she'll keep" beneath it in a thick flowing brush script, both in near-black, perfectly spelled, sharp edges, high contrast, filling about two thirds of the width. No logos, no brand names, no labels or printing on products or packaging, no watermark, no person, no other text.
```

**Image 2, `pink-gifts-for-mom-lifestyle.jpg` (Tommy Kate, chin-down outfit crop):** Google Gemini first; Nano Banana Pro 2K on Higgsfield if Gemini is out or the result fails. Attach (1) style reference `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/src/lifestyle/pink-workwear-freezing-office-lifestyle.jpg`, (2) the Omni seed `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/public/images/library/avatar-seed-omni-reference.png` as a JPEG under 400 KB, (3) this look's product sheet.

```
Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference. The reference sheet is the second image. Using the first image as a style reference, not an exact copy, please make me one single very realistic lifestyle photo, not a collage or grid. I can't use the exact Amazon images, so this is a new photo of the products in the third image, each matching its screenshot in colour and detail. Setting: the raised garden beds by the red barn on a cold sunny morning, frost on the soil, a gift basket set on the wooden edge of a bed, in December. A chin-down crop from her collarbone to her hips as she ties a pink ribbon bow on the basket holding the pink garden gloves, the tool set and the folded wrap scarf. She is wearing a quilted cream barn jacket over a candy pink knit sweater, jeans. Her hair is tucked into her collar. Nails: short and natural. Her glitter-flecked pink iced coffee tumbler with a lavender straw, saturated candy pink, never pale, is on the edge of the raised bed. Other pink in the frame: the candy pink sweater and the pink garden gloves; pink clothes and other pink pieces are welcome alongside the tumbler. The register is quiet wealth, lived in: a real farmhouse that is nice but never showy, clean but not sterile, with small signs of a real life. Format: chin-down outfit crop. The frame is cropped just below her chin, so her face is not in the frame. The main subject sits in the right third of the frame with calmer negative space on the left, natural perspective and believable scale. Portrait 2:3. Light: bright low winter morning sun. Shot on a mirrorless camera with a 50mm lens at f/2.8, natural depth of field and soft natural bokeh, photorealistic, real-world photography, true-to-life textures, real skin and fabric texture, natural imperfections, nothing glossy. No lettering, no signs, no logos, no text anywhere in the frame, no brand marks on any product. Not a Paris apartment, cafe, marble room, mansion or influencer studio.
```

**Site alt text:** flat lay: Overhead flat lay on white linen of a plush robe, heated neck wrap, digital photo frame, recipe box, wrap scarf, birth flower necklace and pink garden gloves with a tool set. · lifestyle: Chin-down crop of a woman in a cream barn jacket tying a pink bow on a gift basket with pink garden gloves and a scarf on the edge of a frosty raised garden bed.

**Pin 1, flat lay** · Sat 21 Nov 2026 13:30 ET · board `Legally Blonde Outfits | Pink Amazon Fashion` > section `Christmas and Gift Guides` · link: this look's Idea List (`https://www.amazon.com/shop/thedigitalincomeedit/list/<id>`) · AI label ON

- Overlay (on the image): GIFTS FOR MOM / she'll keep
- Title: Gifts for Mom She Won't Return: A Plush Robe, Heated Neck Wrap and Digital Photo Frame
- Description: Gifts for mom she will not return, and you know she returns everything: a plush robe, a heated neck and shoulder wrap, a digital photo frame you load up before wrapping, a pretty recipe box, a soft wrap scarf, a birth flower necklace and pink garden gloves with a tool set. Buy the nicer version of what she already uses. She keeps those. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #giftsformom #christmasgiftsformom #momgifts
- Alt text: Overhead flat lay on white linen of a plush robe, heated neck wrap, digital photo frame, recipe box, wrap scarf, birth flower necklace and pink garden gloves with a tool set.

**Pin 2, lifestyle** · Tue 24 Nov 2026 20:30 ET · same board and section · same Idea List link · AI label ON, "includes an AI-generated person" ticked

- Title: Christmas Gifts for Mom Who Loves Her Garden: Pink Gloves, Tool Set and a Cozy Wrap
- Description: Christmas gifts for mom who lives in her garden, even in December: pink garden gloves and a tool set, a soft wrap scarf and a heated neck wrap for afterwards, packed in a basket on the edge of the raised beds. Frost on the soil, sun on the red barn. Save this for the mom who says she wants nothing for Christmas and means seeds. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #giftsformom #gardeninggifts #christmasgifts #momgifts
- Alt text: Chin-down crop of a woman in a cream barn jacket tying a pink bow on a gift basket with pink garden gloves and a scarf on the edge of a frosty raised garden bed.

**Instagram @itstommykate feed post** · Sat 21 Nov 2026 19:00 ET · carousel: lifestyle photo first, flat lay second · AI label ON · check the caption panel says `itstommykate` before Share

```
mom gift rule: buy the nicer version of something she uses every day. she keeps those 🎀 pink garden gloves, heated neck wrap, a photo frame I loaded myself. linked in my Amazon storefront (link in bio) #ad #giftsformom #christmasgifts
```


---

### 21. Best Friend

**Page:** `/lifestyle/gifts-for-best-friend` · category `gifts` · season `Holiday` · file `src/lifestyle/gifts-for-best-friend.json` (committed, `draft: true`)

**Page title (H1):** Gifts for Your Best Friend (Buy Two, Keep One)

**Intro:** Best friend gifts are the only gifts where buying two is the point. Matching charm bracelets, a pair of heart frames for the same photo, a pink instant camera for the next girls night and a question card game for the sleepover. Keep one set for yourself. That is the tradition now.

**Items to source (the page lists them in this order):**

1. Matching heart charm bracelet set
2. Heart shaped photo frames, set of two
3. Question card game for friends
4. Pink instant camera
5. Instant film pack
6. Matching silk eye masks
7. Pink linen photo album

**Idea List:** title `Gifts for Your Best Friend (Buy Two, Keep One)` · description: Best friend gifts are the only gifts where buying two is the point. Every piece is linked here.

**Image 1, `gifts-for-best-friend-flatlay.jpg` (no person, Format B):** Seedream 4.5 on Higgsfield, Unlimited ON, 4K, portrait 2:3. Attach (1) Command Centre `stylerefs` doc `sr-that-girl-amazon-finds-script`, (2) this look's product sheet. Garbled or soft title letters: re-run on Nano Banana Pro 2K. Colour follows factory section 4 (as pink as the look).

```
Using the first image as a style reference for the layout, the fullness and the title lettering, not an exact copy, please make me a "that girl" shoppable Amazon finds collage for Pinterest, portrait 2:3, on a soft blush pink background with a faint paper texture. I can't use the exact Amazon images outside of Amazon, so please create a new clean cut-out product photo of each item in the second image, each with a soft drop shadow: matching heart charm bracelet set, heart shaped photo frames, set of two, question card game for friends, pink instant camera, instant film pack, matching silk eye masks, pink linen photo album. Add two iced lattes in clear cups, two lip glosses and a satin hair bow. Pack them around a central title so the whole canvas is full edge to edge, items overlapping slightly, every product fully inside the frame. Add a few tiny accents: small hearts, little sparkles and one small bow. In the middle, set directly on the background, a large two-style title: "BEST FRIEND" in a bold high-contrast serif with "buy two" in a thick flowing brush script, deep plum, perfectly spelled, crisp and fully legible, filling about half the width. Each item matches its screenshot in colour, shape and detail and looks like a real photo, not a render, with true-to-life materials. No logos, no brand names, no labels or printing on products or packaging, no prices, no person, no other text.
```

**Image 2, `gifts-for-best-friend-lifestyle.jpg` (Tommy Kate, detail shot of hands and products):** Google Gemini first; Nano Banana Pro 2K on Higgsfield if Gemini is out or the result fails. Attach (1) style reference `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/src/lifestyle/pink-workwear-freezing-office-lifestyle.jpg`, (2) the Omni seed `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/public/images/library/avatar-seed-omni-reference.png` as a JPEG under 400 KB, (3) this look's product sheet.

```
Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference. The reference sheet is the second image. Using the first image as a style reference, not an exact copy, please make me one single very realistic lifestyle photo, not a collage or grid. I can't use the exact Amazon images, so this is a new photo of the products in the third image, each matching its screenshot in colour and detail. Setting: the farmhouse porch steps dusted with light snow, white railings and a wreath on the door behind, in December. Close detail of her hands holding up two matching small gift bags tied with pink ribbon, one wrist wearing the heart charm bracelet, the pink instant camera on the step below. She is wearing the cuffs of a cream puffer jacket over a candy pink knit. Nails: candy pink. Her glitter-flecked pink iced coffee tumbler with a lavender straw, saturated candy pink, never pale, is on the step beside the camera. Other pink in the frame: the candy pink knit cuffs, the pink ribbon and the pink instant camera; pink clothes and other pink pieces are welcome alongside the tumbler. The register is quiet wealth, lived in: a real farmhouse that is nice but never showy, clean but not sterile, with small signs of a real life. Format: detail shot of hands and products. Her face is not in the frame. The main subject sits in the right third of the frame with calmer negative space on the left, natural perspective and believable scale. Portrait 2:3. Light: soft overcast snowy daylight. Shot on a mirrorless camera with a 50mm lens at f/2, natural depth of field and soft natural bokeh, photorealistic, real-world photography, true-to-life textures, real skin and fabric texture, natural imperfections, nothing glossy. No lettering, no signs, no logos, no text anywhere in the frame, no brand marks on any product. Not a Paris apartment, cafe, marble room, mansion or influencer studio.
```

**Site alt text:** flat lay: Shoppable collage on blush pink of matching heart charm bracelets, two heart photo frames, a card game, a pink instant camera, film, silk eye masks and a pink linen photo album. · lifestyle: Hands holding two matching gift bags with pink ribbon on snowy farmhouse porch steps, heart charm bracelet on one wrist, a pink instant camera and glitter tumbler below.

**Pin 1, flat lay** · Mon 23 Nov 2026 13:30 ET · board `Legally Blonde Outfits | Pink Amazon Fashion` > section `Christmas and Gift Guides` · link: this look's Idea List (`https://www.amazon.com/shop/thedigitalincomeedit/list/<id>`) · AI label ON

- Overlay (on the image): BEST FRIEND / buy two
- Title: Gifts for Your Best Friend: Matching Bracelets, Heart Frames and a Pink Instant Camera
- Description: Gifts for your best friend, where buying two is the whole point: a matching heart charm bracelet set, a pair of heart photo frames, a question card game for the next sleepover, a pink instant camera with a film pack, matching silk eye masks and a photo album to fill. Give one set, keep one set, and call it a tradition from now on. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #bestfriendgifts #giftsforbestfriend #giftsforher
- Alt text: Shoppable collage on blush pink of matching heart charm bracelets, two heart photo frames, a card game, a pink instant camera, film, silk eye masks and a pink linen photo album.

**Pin 2, lifestyle** · Thu 26 Nov 2026 20:30 ET · same board and section · same Idea List link · AI label ON, "includes an AI-generated person" ticked

- Title: Best Friend Christmas Gift Ideas: Two Little Pink Gift Bags and a Matching Bracelet
- Description: Best friend Christmas gift ideas, wrapped in two matching bags on the snowy porch steps: heart charm bracelets, a pink instant camera for the next girls night and heart frames for the photo you already know you will print. One for her, one for you. Save this for the friend who has seen you at your absolute worst and stayed anyway. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #bestfriendgifts #bff #girlsnight #christmasgifts
- Alt text: Hands holding two matching gift bags with pink ribbon on snowy farmhouse porch steps, heart charm bracelet on one wrist, a pink instant camera and glitter tumbler below.

**Instagram @itstommykate feed post** · Mon 23 Nov 2026 19:00 ET · carousel: lifestyle photo first, flat lay second · AI label ON · check the caption panel says `itstommykate` before Share

```
bestie gifts where you buy two and keep one. matching bracelets, heart frames, a pink instant camera for our next girls night 🎀 linked in my Amazon storefront (link in bio) #ad #bestfriendgifts #giftsforher
```


---

### 22. Teachers

**Page:** `/lifestyle/teacher-christmas-gifts` · category `gifts` · season `Holiday` · file `src/lifestyle/teacher-christmas-gifts.json` (committed, `draft: true`)

**Page title (H1):** Teacher Christmas Gifts They'll Actually Want

**Intro:** Teachers get forty candles and an apple mug every December. Be the family that sends something useful: a good insulated tumbler, a pretty beaded lanyard, hand sanitizer that smells nice, fine tip pens and a stapler that isn't beige. Candles are fine. Forty candles are a fire hazard.

**Items to source (the page lists them in this order):**

1. Insulated tumbler with lid and straw
2. Beaded lanyard
3. Scented hand sanitizer set
4. Fine tip pen set
5. Pink stapler and tape dispenser set
6. Dry erase marker set · note on page: "Teachers buy these with their own money."
7. Pink gift card holder

**Idea List:** title `Teacher Christmas Gifts They'll Actually Want` · description: Teachers get forty candles and an apple mug every December. Every piece is linked here.

**Image 1, `teacher-christmas-gifts-flatlay.jpg` (no person, Format A):** Seedream 4.5 on Higgsfield, Unlimited ON, 4K, portrait 2:3. Attach (1) Command Centre `stylerefs` doc `sr-flatlay-grid`, (2) this look's product sheet. Garbled or soft title letters: re-run on Nano Banana Pro 2K. Colour follows factory section 4 (as pink as the look).

```
Using the first image as a style reference for the styling, the fullness and the title lettering, not an exact copy, please make me a very realistic overhead flat lay photo of the products in the second image. I can't use the exact Amazon images outside of Amazon, so this needs to be a new photo. Shot straight down, portrait 2:3, like a good-quality photo taken on a phone. The gifts are arranged as one abundant styled group, pieces overlapping and touching, on warm wood floorboards: insulated tumbler with lid and straw, beaded lanyard, scented hand sanitizer set, fine tip pen set, pink stapler and tape dispenser set, dry erase marker set, pink gift card holder. Each item matches its screenshot in colour, shape and detail. Tucked in around them, filling the frame edge to edge with almost no empty background: a clementine, a small pencil cup, a satin bow, a pad of plain sticky notes and a sprig of pine. Every product sits fully inside the frame. Soft natural window light, gentle real shadows, visible fabric texture, true-to-life materials, small real-life imperfections, photorealistic real-world photography. Across the upper third, set directly on the photo, a large two-style title: "TEACHER GIFTS" in a bold high-contrast serif in capitals, with "not a candle" beneath it in a thick flowing brush script, both in near-black, perfectly spelled, sharp edges, high contrast, filling about two thirds of the width. No logos, no brand names, no labels or printing on products or packaging, no watermark, no person, no other text.
```

**Image 2, `teacher-christmas-gifts-lifestyle.jpg` (Tommy Kate, detail shot of hands and products):** Google Gemini first; Nano Banana Pro 2K on Higgsfield if Gemini is out or the result fails. Attach (1) style reference `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/src/lifestyle/pink-workwear-freezing-office-lifestyle.jpg`, (2) the Omni seed `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/public/images/library/avatar-seed-omni-reference.png` as a JPEG under 400 KB, (3) this look's product sheet.

```
Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference. The reference sheet is the second image. Using the first image as a style reference, not an exact copy, please make me one single very realistic lifestyle photo, not a collage or grid. I can't use the exact Amazon images, so this is a new photo of the products in the third image, each matching its screenshot in colour and detail. Setting: the mudroom bench by the farmhouse back door during the morning rush, small backpacks on hooks and boots lined up underneath, in December. Close detail of her hands tucking the fine tip pens, the beaded lanyard and the hand sanitizer into a gift bag lined with pink tissue, a blank folded card on the bench beside it. She is wearing the cuffs of a candy pink fleece half-zip. Nails: nude pink. Her glitter-flecked pink iced coffee tumbler with a lavender straw, saturated candy pink, never pale, is on the bench beside the gift bag. Other pink in the frame: the candy pink fleece cuffs, the pink tissue and the pink stapler; pink clothes and other pink pieces are welcome alongside the tumbler. The register is quiet wealth, lived in: a real farmhouse that is nice but never showy, clean but not sterile, with small signs of a real life. Format: detail shot of hands and products. Her face is not in the frame. The main subject sits in the right third of the frame with calmer negative space on the left, natural perspective and believable scale. Portrait 2:3. Light: soft morning light through the mudroom window. Shot on a mirrorless camera with a 35mm lens at f/2.8, natural depth of field and soft natural bokeh, photorealistic, real-world photography, true-to-life textures, real skin and fabric texture, natural imperfections, nothing glossy. No lettering, no signs, no logos, no text anywhere in the frame, no brand marks on any product. Not a Paris apartment, cafe, marble room, mansion or influencer studio.
```

**Site alt text:** flat lay: Overhead flat lay on wood floorboards of an insulated tumbler, beaded lanyard, hand sanitizer set, fine tip pens, a pink stapler and tape set, dry erase markers and a pink card holder. · lifestyle: Hands packing pens, a beaded lanyard and hand sanitizer into a pink tissue gift bag on a farmhouse mudroom bench, small backpacks on hooks and a pink glitter tumbler.

**Pin 1, flat lay** · Fri 4 Dec 2026 13:30 ET · board `Legally Blonde Outfits | Pink Amazon Fashion` > section `Christmas and Gift Guides` · link: this look's Idea List (`https://www.amazon.com/shop/thedigitalincomeedit/list/<id>`) · AI label ON

- Overlay (on the image): TEACHER GIFTS / not a candle
- Title: Teacher Christmas Gifts They'll Actually Want: Tumbler, Beaded Lanyard and Nice Pens
- Description: Teacher Christmas gifts they will actually want, instead of another apple mug: an insulated tumbler with a straw, a beaded lanyard, nice smelling hand sanitizer, fine tip pens, a pink stapler and tape set, dry erase markers and a gift card holder. Teachers buy half their supplies themselves. Stock the desk, be the favourite family. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #teachergifts #teacherchristmasgifts #christmasgifts
- Alt text: Overhead flat lay on wood floorboards of an insulated tumbler, beaded lanyard, hand sanitizer set, fine tip pens, a pink stapler and tape set, dry erase markers and a pink card holder.

**Pin 2, lifestyle** · Mon 7 Dec 2026 20:30 ET · same board and section · same Idea List link · AI label ON, "includes an AI-generated person" ticked

- Title: Teacher Gift Ideas From Kids: A Little Pink Gift Bag Packed on the Mudroom Bench
- Description: Teacher gift ideas from the kids, packed on the mudroom bench during the morning rush: fine tip pens, a beaded lanyard, hand sanitizer that smells good and a handwritten card from the kids tucked in on top. Backpacks on the hooks, boots by the door, somebody missing a mitten. Save this for the last week before winter break. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #teachergifts #teachergiftideas #christmasgifts #winterbreak
- Alt text: Hands packing pens, a beaded lanyard and hand sanitizer into a pink tissue gift bag on a farmhouse mudroom bench, small backpacks on hooks and a pink glitter tumbler.

**Instagram @itstommykate feed post** · Fri 4 Dec 2026 19:00 ET · carousel: lifestyle photo first, flat lay second · AI label ON · check the caption panel says `itstommykate` before Share

```
teacher gifts packed in the mudroom at 7am because that's when mornings happen. pens, beaded lanyard, fancy sanitizer, zero apple mugs 🎀 linked in my Amazon storefront (link in bio) #ad #teachergifts #christmasgifts
```


---

### 23. Travel Gifts

**Page:** `/lifestyle/pink-travel-gifts-for-her` · category `accessories` · season `Holiday` · file `src/lifestyle/pink-travel-gifts-for-her.json` (committed, `draft: true`)

**Page title (H1):** Pink Travel Gifts for Her

**Intro:** Travel gifts are for the friend who is always somewhere else. A pink carry-on, packing cubes, a travel jewelry case, a clear toiletry bag and a journal for the window seat make every trip feel organized, even the red-eye. She will stop living out of a tote bag, and her camera roll will thank you.

**Items to source (the page lists them in this order):**

1. Pink hardside carry-on suitcase
2. Packing cube set
3. Travel jewelry case
4. Clear toiletry bag
5. Blush travel journal · note on page: "For the window seat."
6. Pink memory foam neck pillow
7. Pink passport cover

**Idea List:** title `Pink Travel Gifts for Her` · description: Travel gifts are for the friend who is always somewhere else. Every piece is linked here.

**Image 1, `pink-travel-gifts-for-her-flatlay.jpg` (no person, Format B):** Seedream 4.5 on Higgsfield, Unlimited ON, 4K, portrait 2:3. Attach (1) Command Centre `stylerefs` doc `sr-amazon-fashion-looks-expensive`, (2) this look's product sheet. Garbled or soft title letters: re-run on Nano Banana Pro 2K. Colour follows factory section 4 (as pink as the look).

```
Using the first image as a style reference for the layout, the fullness and the title lettering, not an exact copy, please make me a "that girl" shoppable Amazon finds collage for Pinterest, portrait 2:3, on a soft dusty blue background with a faint paper texture. I can't use the exact Amazon images outside of Amazon, so please create a new clean cut-out product photo of each item in the second image, each with a soft drop shadow: pink hardside carry-on suitcase, packing cube set, travel jewelry case, clear toiletry bag, blush travel journal, pink memory foam neck pillow, pink passport cover. Add heart shaped sunglasses, a lip balm and a small silk scarf. Pack them around a central title so the whole canvas is full edge to edge, items overlapping slightly, every product fully inside the frame. Add a few tiny accents: small hearts, little sparkles and one small bow. In the middle, set directly on the background, a large two-style title: "TRAVEL GIFTS" in a bold high-contrast serif with "for her" in a thick flowing brush script, near-black, perfectly spelled, crisp and fully legible, filling about half the width. Each item matches its screenshot in colour, shape and detail and looks like a real photo, not a render, with true-to-life materials. No logos, no brand names, no labels or printing on products or packaging, no prices, no person, no other text.
```

**Image 2, `pink-travel-gifts-for-her-lifestyle.jpg` (Tommy Kate, over-the-shoulder walk-away):** Google Gemini first; Nano Banana Pro 2K on Higgsfield if Gemini is out or the result fails. Attach (1) style reference `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/src/lifestyle/pink-graduation-gown-halloween-costume-lifestyle.jpg`, (2) the Omni seed `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/public/images/library/avatar-seed-omni-reference.png` as a JPEG under 400 KB, (3) this look's product sheet.

```
Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference. The reference sheet is the second image. Using the first image as a style reference, not an exact copy, please make me one single very realistic lifestyle photo, not a collage or grid. I can't use the exact Amazon images, so this is a new photo of the products in the third image, each matching its screenshot in colour and detail. Setting: the stone path from the farmhouse front door to the gravel drive at dawn, frost on the grass and the red barn in the distance, in December. Seen from behind over her shoulder as she rolls the pink hardside carry-on toward the car, the blush travel journal tucked under her arm. She is wearing a long camel wool coat over a cream knit set, white sneakers and a small candy pink crossbody bag. Her hair is in a sleek low bun. Nails: soft pink. Her glitter-flecked pink iced coffee tumbler with a lavender straw, saturated candy pink, never pale, is in her free hand. Other pink in the frame: the pink carry-on and the candy pink crossbody bag; pink clothes and other pink pieces are welcome alongside the tumbler. The register is quiet wealth, lived in: a real farmhouse that is nice but never showy, clean but not sterile, with small signs of a real life. Format: over-the-shoulder walk-away. Her face is turned away from the camera. The main subject sits in the right third of the frame with calmer negative space on the left, natural perspective and believable scale. Portrait 2:3. Light: soft pink-grey dawn light. Shot on a mirrorless camera with a 50mm lens at f/2, natural depth of field and soft natural bokeh, photorealistic, real-world photography, true-to-life textures, real skin and fabric texture, natural imperfections, nothing glossy. No lettering, no signs, no logos, no text anywhere in the frame, no brand marks on any product. Not a Paris apartment, cafe, marble room, mansion or influencer studio.
```

**Site alt text:** flat lay: Shoppable collage on dusty blue of a pink hardside carry-on, packing cubes, a travel jewelry case, a clear toiletry bag, a blush journal, a pink neck pillow and a passport cover. · lifestyle: Woman in a camel coat seen from behind rolling a pink hardside carry-on down a frosty farmhouse path at dawn, candy pink crossbody bag, red barn in the distance.

**Pin 1, flat lay** · Sun 13 Dec 2026 13:30 ET · board `Legally Blonde Outfits | Pink Amazon Fashion` > section `Christmas and Gift Guides` · link: this look's Idea List (`https://www.amazon.com/shop/thedigitalincomeedit/list/<id>`) · AI label ON

- Overlay (on the image): TRAVEL GIFTS / for her
- Title: Pink Travel Gifts for Her: A Carry-On, Packing Cubes, Travel Journal and Jewelry Case
- Description: Pink travel gifts for her, for the friend who is always somewhere else: a pink hardside carry-on, a packing cube set, a travel jewelry case, a clear toiletry bag, a blush travel journal, a pink neck pillow and a passport cover. Every trip feels calmer when everything has a place, even the six am flight she swore she would never book again. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #travelgifts #travelessentials #giftsforher
- Alt text: Shoppable collage on dusty blue of a pink hardside carry-on, packing cubes, a travel jewelry case, a clear toiletry bag, a blush journal, a pink neck pillow and a passport cover.

**Pin 2, lifestyle** · Wed 16 Dec 2026 20:30 ET · same board and section · same Idea List link · AI label ON, "includes an AI-generated person" ticked

- Title: Travel Gift Ideas for Women: Rolling a Pink Carry-On Out the Farmhouse Door at Dawn
- Description: Travel gift ideas for women who leave before the sun is up: a pink hardside carry-on, a travel journal for the window seat, packing cubes that actually keep things folded and a passport cover she will not lose. Frost on the path, car warming up in the drive, coffee in hand. Save this for the friend who already has a trip booked for January. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #travelgifts #carryon #travelessentials
- Alt text: Woman in a camel coat seen from behind rolling a pink hardside carry-on down a frosty farmhouse path at dawn, candy pink crossbody bag, red barn in the distance.

**Instagram @itstommykate feed post** · Sun 13 Dec 2026 19:00 ET · carousel: lifestyle photo first, flat lay second · AI label ON · check the caption panel says `itstommykate` before Share

```
5am, frost on the path, pink carry-on rolling. packing cubes are the reason I own shoes on the other end 🎀 travel list is linked in my Amazon storefront (link in bio) #ad #travelgifts #travelessentials
```


---

### 24. Bag Charms

**Page:** `/lifestyle/trendy-bag-charms-and-accessory-gifts` · category `accessories` · season `Holiday` · file `src/lifestyle/trendy-bag-charms-and-accessory-gifts.json` (committed, `draft: true`)

**Page title (H1):** Bag Charms and the Accessory Gifts Everyone Wants Right Now

**Intro:** Bag charms went from niche to everywhere in a year, and they make a perfect gift because they are nearly impossible to get wrong. Pair a beaded bow charm and a tiny plush with a cream crescent bag, a silk scarf for the strap and a pink heart coin purse, and a plain tote suddenly has a personality.

**Items to source (the page lists them in this order):**

1. Beaded bow bag charm
2. Mini plush bag charm
3. Cream crescent shoulder bag · note on page: "The shape that let charms become the point."
4. Silk skinny scarf for the bag strap
5. Gold chain keyring
6. Pink heart coin purse
7. Tortoise cat eye sunglasses

**Idea List:** title `Bag Charms and the Accessory Gifts Everyone Wants Right Now` · description: Bag charms went from niche to everywhere in a year, and they make a perfect gift because they are nearly impossible to get wrong. Every piece is linked here.

**Image 1, `trendy-bag-charms-and-accessory-gifts-flatlay.jpg` (no person, Format A):** Seedream 4.5 on Higgsfield, Unlimited ON, 4K, portrait 2:3. Attach (1) Command Centre `stylerefs` doc `sr-pink-dress-flatlay`, (2) this look's product sheet. Garbled or soft title letters: re-run on Nano Banana Pro 2K. Colour follows factory section 4 (as pink as the look).

```
Using the first image as a style reference for the styling, the fullness and the title lettering, not an exact copy, please make me a very realistic overhead flat lay photo of the products in the second image. I can't use the exact Amazon images outside of Amazon, so this needs to be a new photo. Shot straight down, portrait 2:3, like a good-quality photo taken on a phone. The gifts are arranged as one abundant styled group, pieces overlapping and touching, on a chunky cream knit throw: beaded bow bag charm, mini plush bag charm, cream crescent shoulder bag, silk skinny scarf for the bag strap, gold chain keyring, pink heart coin purse, tortoise cat eye sunglasses. Each item matches its screenshot in colour, shape and detail. Tucked in around them, filling the frame edge to edge with almost no empty background: an iced latte in a clear glass, stacked gold rings, a small bunch of pink tulips and a lip gloss. Every product sits fully inside the frame. Soft natural window light, gentle real shadows, visible fabric texture, true-to-life materials, small real-life imperfections, photorealistic real-world photography. Across the upper third, set directly on the photo, a large two-style title: "BAG CHARMS" in a bold high-contrast serif in capitals, with "it girl" beneath it in a thick flowing brush script, both in near-black, perfectly spelled, sharp edges, high contrast, filling about two thirds of the width. No logos, no brand names, no labels or printing on products or packaging, no watermark, no person, no other text.
```

**Image 2, `trendy-bag-charms-and-accessory-gifts-lifestyle.jpg` (Tommy Kate, detail shot of hands and products):** Google Gemini first; Nano Banana Pro 2K on Higgsfield if Gemini is out or the result fails. Attach (1) style reference `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/src/lifestyle/pink-workwear-freezing-office-lifestyle.jpg`, (2) the Omni seed `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/public/images/library/avatar-seed-omni-reference.png` as a JPEG under 400 KB, (3) this look's product sheet.

```
Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference. The reference sheet is the second image. Using the first image as a style reference, not an exact copy, please make me one single very realistic lifestyle photo, not a collage or grid. I can't use the exact Amazon images, so this is a new photo of the products in the third image, each matching its screenshot in colour and detail. Setting: the weathered red doors of her barn on a grey winter morning, a hay bale to one side, in December. Close detail of the cream crescent bag on her shoulder with the beaded bow charm and the plush charm swinging from the strap, the silk scarf knotted on the handle. She is wearing a cream cable cardigan over a candy pink turtleneck. Nails: milky pink. Her glitter-flecked pink iced coffee tumbler with a lavender straw, saturated candy pink, never pale, is in her hand beside the bag. Other pink in the frame: the candy pink turtleneck and the pink heart coin purse peeking out of the bag; pink clothes and other pink pieces are welcome alongside the tumbler. The register is quiet wealth, lived in: a real farmhouse that is nice but never showy, clean but not sterile, with small signs of a real life. Format: detail shot of hands and products. Her face is not in the frame. The main subject sits in the right third of the frame with calmer negative space on the left, natural perspective and believable scale. Portrait 2:3. Light: soft overcast daylight. Shot on a mirrorless camera with a 50mm lens at f/2, natural depth of field and soft natural bokeh, photorealistic, real-world photography, true-to-life textures, real skin and fabric texture, natural imperfections, nothing glossy. No lettering, no signs, no logos, no text anywhere in the frame, no brand marks on any product. Not a Paris apartment, cafe, marble room, mansion or influencer studio.
```

**Site alt text:** flat lay: Overhead flat lay on a cream knit of a cream crescent bag with a beaded bow charm and a plush charm, a silk scarf, a gold keyring, a pink heart coin purse and tortoise sunglasses. · lifestyle: Detail of a cream crescent bag with a beaded bow charm, plush charm and silk scarf on a woman's shoulder in front of weathered red barn doors, pink glitter tumbler in hand.

**Pin 1, flat lay** · Sun 6 Dec 2026 13:30 ET · board `Legally Blonde Outfits | Pink Amazon Fashion` > section `Christmas and Gift Guides` · link: this look's Idea List (`https://www.amazon.com/shop/thedigitalincomeedit/list/<id>`) · AI label ON

- Overlay (on the image): BAG CHARMS / it girl
- Title: Bag Charms and Trendy Accessory Gifts: Beaded Bows, a Crescent Bag and a Silk Scarf
- Description: Bag charms and trendy accessory gifts she will clip on the second she unwraps them: a beaded bow bag charm, a mini plush charm, a cream crescent shoulder bag, a silk skinny scarf for the handle, a gold chain keyring, a pink heart coin purse and tortoise cat eye sunglasses. It is the fastest way to make a plain bag feel brand new again. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #bagcharms #accessories #giftsforher #crescentbag
- Alt text: Overhead flat lay on a cream knit of a cream crescent bag with a beaded bow charm and a plush charm, a silk scarf, a gold keyring, a pink heart coin purse and tortoise sunglasses.

**Pin 2, lifestyle** · Wed 9 Dec 2026 20:30 ET · same board and section · same Idea List link · AI label ON, "includes an AI-generated person" ticked

- Title: How to Style Bag Charms: A Cream Crescent Bag, Beaded Bow Charm and Silk Scarf
- Description: How to style bag charms without looking like a keychain display: one beaded bow charm, one small plush, a silk scarf knotted on the strap and a cream crescent bag that lets them be the whole point. Styled by the red barn doors on a grey winter morning. Save this for the girl who already owns every bag and still wants something new. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #bagcharms #howtostyle #accessorytrends #crescentbag
- Alt text: Detail of a cream crescent bag with a beaded bow charm, plush charm and silk scarf on a woman's shoulder in front of weathered red barn doors, pink glitter tumbler in hand.

**Instagram @itstommykate feed post** · Sun 6 Dec 2026 19:00 ET · carousel: lifestyle photo first, flat lay second · AI label ON · check the caption panel says `itstommykate` before Share

```
the bag charm situation got out of hand in the best way. bow charm, tiny plush, silk scarf on the strap 🎀 all linked in my Amazon storefront (link in bio) #ad #bagcharms #accessories
```


---

### 25. Snail Mail

**Page:** `/lifestyle/snail-mail-stationery-gifts` · category `gifts` · season `Holiday` · file `src/lifestyle/snail-mail-stationery-gifts.json` (committed, `draft: true`)

**Page title (H1):** Snail Mail and Pretty Stationery Gifts

**Intro:** Handwritten letters are having a real comeback, and the stationery girls were right all along. A wax seal kit, a box of cream notecards, a fountain pen that writes like butter and pink washi tape turn into a gift that keeps giving every time she mails something. Old-fashioned, in the best way.

**Items to source (the page lists them in this order):**

1. Wax seal stamp kit
2. Cream notecards and envelopes box
3. Fountain pen with ink cartridges
4. Pink washi tape set
5. Linen address book
6. Pink stationery set
7. Brass letter tray

**Idea List:** title `Snail Mail and Pretty Stationery Gifts` · description: Handwritten letters are having a real comeback, and the stationery girls were right all along. Every piece is linked here.

**Image 1, `snail-mail-stationery-gifts-flatlay.jpg` (no person, Format B):** Seedream 4.5 on Higgsfield, Unlimited ON, 4K, portrait 2:3. Attach (1) Command Centre `stylerefs` doc `sr-soft-pink-collage`, (2) this look's product sheet. Garbled or soft title letters: re-run on Nano Banana Pro 2K. Colour follows factory section 4 (as pink as the look).

```
Using the first image as a style reference for the layout, the fullness and the title lettering, not an exact copy, please make me a "that girl" shoppable Amazon finds collage for Pinterest, portrait 2:3, on a soft cream with a faint paper texture background with a faint paper texture. I can't use the exact Amazon images outside of Amazon, so please create a new clean cut-out product photo of each item in the second image, each with a soft drop shadow: wax seal stamp kit, cream notecards and envelopes box, fountain pen with ink cartridges, pink washi tape set, linen address book, pink stationery set, brass letter tray. Add dried lavender sprigs, a satin ribbon and a small bunch of pink roses. Pack them around a central title so the whole canvas is full edge to edge, items overlapping slightly, every product fully inside the frame. Add a few tiny accents: small hearts, little sparkles and one small bow. In the middle, set directly on the background, a large two-style title: "SNAIL MAIL" in a bold high-contrast serif with "gift set" in a thick flowing brush script, deep plum, perfectly spelled, crisp and fully legible, filling about half the width. Each item matches its screenshot in colour, shape and detail and looks like a real photo, not a render, with true-to-life materials. No logos, no brand names, no labels or printing on products or packaging, no prices, no person, no other text.
```

**Image 2, `snail-mail-stationery-gifts-lifestyle.jpg` (Tommy Kate, detail shot of hands and products):** Google Gemini first; Nano Banana Pro 2K on Higgsfield if Gemini is out or the result fails. Attach (1) style reference `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/src/lifestyle/pink-workwear-freezing-office-lifestyle.jpg`, (2) the Omni seed `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/public/images/library/avatar-seed-omni-reference.png` as a JPEG under 400 KB, (3) this look's product sheet.

```
Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference. The reference sheet is the second image. Using the first image as a style reference, not an exact copy, please make me one single very realistic lifestyle photo, not a collage or grid. I can't use the exact Amazon images, so this is a new photo of the products in the third image, each matching its screenshot in colour and detail. Setting: the writing desk in the corner of her farmhouse living room by the window on a quiet afternoon, a small vase of dried wildflowers, in December. Close detail of her hands pressing the wax seal onto a blank cream envelope, a stack of blank envelopes, the pink washi tape and the fountain pen beside it. She is wearing the sleeves of a candy pink cardigan. Nails: soft pink. Her glitter-flecked pink iced coffee tumbler with a lavender straw, saturated candy pink, never pale, is at the back of the desk. Other pink in the frame: the candy pink cardigan sleeves and the pink washi tape; pink clothes and other pink pieces are welcome alongside the tumbler. The register is quiet wealth, lived in: a real farmhouse that is nice but never showy, clean but not sterile, with small signs of a real life. Format: detail shot of hands and products. Her face is not in the frame. The main subject sits in the right third of the frame with calmer negative space on the left, natural perspective and believable scale. Portrait 2:3. Light: soft afternoon window light. Shot on a mirrorless camera with a 50mm lens at f/2.2, natural depth of field and soft natural bokeh, photorealistic, real-world photography, true-to-life textures, real skin and fabric texture, natural imperfections, nothing glossy. No lettering, no signs, no logos, no text anywhere in the frame, no brand marks on any product. Not a Paris apartment, cafe, marble room, mansion or influencer studio.
```

**Site alt text:** flat lay: Shoppable collage on cream of a wax seal kit, cream notecards and envelopes, a fountain pen, pink washi tape, a linen address book, a pink stationery set and a brass letter tray. · lifestyle: Hands pressing a wax seal onto a blank cream envelope at a farmhouse writing desk with pink washi tape, a fountain pen, dried wildflowers and a pink glitter tumbler.

**Pin 1, flat lay** · Mon 14 Dec 2026 13:30 ET · board `Legally Blonde Outfits | Pink Amazon Fashion` > section `Christmas and Gift Guides` · link: this look's Idea List (`https://www.amazon.com/shop/thedigitalincomeedit/list/<id>`) · AI label ON

- Overlay (on the image): SNAIL MAIL / gift set
- Title: Snail Mail Stationery Gifts: Wax Seal Kit, Cream Notecards, Washi Tape and a Fountain Pen
- Description: Snail mail stationery gifts for the girl who still writes real letters: a wax seal stamp kit, a box of cream notecards and envelopes, a smooth fountain pen, pink washi tape, a linen address book, a pink stationery set and a brass letter tray. Handwritten letters are coming back, and nothing in a mailbox beats an envelope with a wax seal. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #snailmail #stationery #stationerygifts #penpal
- Alt text: Shoppable collage on cream of a wax seal kit, cream notecards and envelopes, a fountain pen, pink washi tape, a linen address book, a pink stationery set and a brass letter tray.

**Pin 2, lifestyle** · Thu 17 Dec 2026 20:30 ET · same board and section · same Idea List link · AI label ON, "includes an AI-generated person" ticked

- Title: Snail Mail Gift Ideas: Pressing a Wax Seal at a Farmhouse Writing Desk
- Description: Snail mail gift ideas for the pen pal, the long-distance best friend or the grandma who still sends birthday cards: a wax seal kit, cream notecards and a fountain pen, sealed at the farmhouse writing desk on a quiet afternoon. Slow, pretty and very analog. Save this one for the friend who deserves a real letter in the mail this year. Every piece is linked in my Amazon storefront. #ad As an Amazon Influencer I earn from qualifying purchases. #snailmail #waxseal #letterwriting #stationerygifts
- Alt text: Hands pressing a wax seal onto a blank cream envelope at a farmhouse writing desk with pink washi tape, a fountain pen, dried wildflowers and a pink glitter tumbler.

**Instagram @itstommykate feed post** · Mon 14 Dec 2026 19:00 ET · carousel: lifestyle photo first, flat lay second · AI label ON · check the caption panel says `itstommykate` before Share

```
wrote four real letters today and sealed every one with wax because I am that girl now 🎀 wax seal kit, cream cards, fountain pen, washi. linked in my Amazon storefront (link in bio) #ad #snailmail #stationery
```


---

## 5. LB_PIN_LOG.md rows (append to the project copy of `claude/LB_PIN_LOG.md` once the Idea Lists and images exist)

All 50 pins are listed here as built-but-not-scheduled, so the weekly factory schedules them before building new looks for these dates. Pinterest will not take anything more than 14 days ahead, so these go in week by week. Fill the ASINs and Idea List ids from the sourcing run.

| Date | Window | Look | Type | Items (name, ASIN) | Idea List URL | Flat lay title | Lifestyle title | Times ET | Verified |
|---|---|---|---|---|---|---|---|---|---|
| 2026-11-12 | 4 holiday gift guide | Hostess Gifts | theme list, 2 pins | Linen tea towel set (ASIN tbc); Olive wood serving board (ASIN tbc); Candle in a ceramic vessel (ASIN tbc); Raw honey jar with wooden dipper (ASIN tbc); Scalloped linen cocktail napkins (ASIN tbc); Gold cheese knife set (ASIN tbc); Pink taper candles (ASIN tbc) | tbc | Pretty Hostess Gifts for Thanksgiving and Christmas: Tea Towels, Olive Wood and Honey | Hostess Gift Basket Ideas: What to Bring to Thanksgiving Dinner That She'll Keep Using | 12 Nov 13:30, 15 Nov 20:30 (planned, NOT scheduled) | no |
| 2026-11-20 | 5 holiday gift guide | For Her | theme list, 2 pins | Blush pink faux fur throw blanket (ASIN tbc); Pink mulberry silk pillowcase (ASIN tbc); Scented candle in a ceramic vessel (ASIN tbc); Cashmere blend lounge socks (ASIN tbc); Gold initial pendant necklace (ASIN tbc); Glitter pink insulated tumbler with straw (ASIN tbc); Pink velvet travel jewelry case (ASIN tbc) | tbc | Gifts for Her That She'll Actually Use: Cozy Pink Finds for the Woman Who Has Everything | Cozy Christmas Gift Ideas for Women: Faux Fur Throw, Initial Necklace and Silk Pillowcase | 20 Nov 13:30, 23 Nov 20:30 (planned, NOT scheduled) | no |
| 2026-11-21 | 5 holiday gift guide | For Mom | theme list, 2 pins | Plush robe (ASIN tbc); Heated neck and shoulder wrap (ASIN tbc); Digital photo frame (ASIN tbc); Recipe box with cards (ASIN tbc); Soft wrap scarf (ASIN tbc); Birth flower necklace (ASIN tbc); Pink garden gloves and tool set (ASIN tbc) | tbc | Gifts for Mom She Won't Return: A Plush Robe, Heated Neck Wrap and Digital Photo Frame | Christmas Gifts for Mom Who Loves Her Garden: Pink Gloves, Tool Set and a Cozy Wrap | 21 Nov 13:30, 24 Nov 20:30 (planned, NOT scheduled) | no |
| 2026-11-22 | 5 holiday gift guide | For Teen Girls | theme list, 2 pins | Pink tinted lip oil set (ASIN tbc); Claw clip set in pinks and cream (ASIN tbc); Pink quilted puffer tote bag (ASIN tbc); Beaded bow bag charm (ASIN tbc); Fuzzy pink slide slippers (ASIN tbc); Photo clip string lights (ASIN tbc); Satin scrunchie set (ASIN tbc) | tbc | Gifts for Teen Girls Who Love Pink: Lip Oil, Claw Clips, Bag Charms and a Puffer Tote | Christmas Gift Ideas for Teen Girls: The Pink Puffer Tote, Bag Charm and Fuzzy Slides Look | 22 Nov 13:30, 25 Nov 20:30 (planned, NOT scheduled) | no |
| 2026-11-23 | 5 holiday gift guide | Best Friend | theme list, 2 pins | Matching heart charm bracelet set (ASIN tbc); Heart shaped photo frames, set of two (ASIN tbc); Question card game for friends (ASIN tbc); Pink instant camera (ASIN tbc); Instant film pack (ASIN tbc); Matching silk eye masks (ASIN tbc); Pink linen photo album (ASIN tbc) | tbc | Gifts for Your Best Friend: Matching Bracelets, Heart Frames and a Pink Instant Camera | Best Friend Christmas Gift Ideas: Two Little Pink Gift Bags and a Matching Bracelet | 23 Nov 13:30, 26 Nov 20:30 (planned, NOT scheduled) | no |
| 2026-11-24 | 5 holiday gift guide | Stocking Stuffers | theme list, 2 pins | Plumping lip oil (ASIN tbc); Mulberry silk scrunchie set (ASIN tbc); Refillable mini perfume atomizer (ASIN tbc); Fuzzy cozy socks (ASIN tbc); Rechargeable hand warmer (ASIN tbc); Pearl claw clip (ASIN tbc); Mini nail polish set in pinks (ASIN tbc) | tbc | Pink Stocking Stuffers for Women: Lip Oil, Silk Scrunchies, Mini Perfume and Cozy Socks | Stocking Stuffer Ideas for Her: Little Pink Things That Make Christmas Morning Better | 24 Nov 13:30, 27 Nov 20:30 (planned, NOT scheduled) | no |
| 2026-11-26 | 5 holiday gift guide | Beauty and Perfume | theme list, 2 pins | Perfume discovery sample set (ASIN tbc); Pink lip gloss and liner set (ASIN tbc); Body wash, scrub and lotion trio (ASIN tbc); Heated eyelash curler (ASIN tbc); Pink quilted makeup bag (ASIN tbc); Gold mirrored vanity tray (ASIN tbc); Pink spa headband and wristband set (ASIN tbc) | tbc | Beauty and Perfume Gift Sets She'll Actually Use: Lip Sets, Body Care and a Scent Sampler | Perfume Gift Ideas for Her: A Scent Discovery Set, Pink Lip Kit and Gold Vanity Tray | 26 Nov 13:30, 29 Nov 20:30 (planned, NOT scheduled) | no |
| 2026-11-27 | 5 holiday gift guide | Jewelry | theme list, 2 pins | Gold stacking ring set (ASIN tbc); Pearl drop earrings (ASIN tbc); Gold paperclip chain necklace (ASIN tbc); Pink enamel heart pendant necklace (ASIN tbc); Gold huggie hoop earrings (ASIN tbc); Pink crystal tennis bracelet (ASIN tbc); Ceramic heart ring dish (ASIN tbc) | tbc | Jewelry Gifts for Her: Gold Stacking Rings, Pearl Drops and a Tiny Pink Heart Necklace | Dainty Gold Jewelry Gift Ideas: Stacking Rings, Tennis Bracelet and a Pink Heart Pendant | 27 Nov 13:30, 30 Nov 20:30 (planned, NOT scheduled) | no |
| 2026-11-28 | 5 holiday gift guide | Pink Christmas Decor | theme list, 2 pins | Blush pink velvet ribbon roll (ASIN tbc); Pink glass ball ornament set (ASIN tbc); Faux cedar garland (ASIN tbc); Oversized pink velvet wreath bow (ASIN tbc); Blush flameless taper candles (ASIN tbc); Pink gingham tree skirt (ASIN tbc); Brass star tree topper (ASIN tbc) | tbc | Pink Christmas Decor Ideas That Still Look Grown Up: Velvet Bows, Blush Ornaments and Cedar | Pink Christmas Porch Decor: A Fresh Wreath, Cedar Garland and One Big Pink Velvet Bow | 28 Nov 13:30, 1 Dec 20:30 (planned, NOT scheduled) | no |
| 2026-11-29 | 5 holiday gift guide | Gamer Girls | theme list, 2 pins | Candy pink wireless over-ear headphones (ASIN tbc); Pink wireless gaming mouse (ASIN tbc); Extended desk mat in pink (ASIN tbc); Pastel pink keycap set (ASIN tbc); Controller charging dock (ASIN tbc); Soft LED light bar (ASIN tbc); Keyboard wrist rest cushion (ASIN tbc) | tbc | Pink Gaming Gifts for Girl Gamers: Candy Pink Headphones, Keycaps and a Cute Desk Setup | Cute Gaming Setup Gift Ideas: A Pink Attic Gaming Loft With Candy Pink Headphones | 29 Nov 13:30, 2 Dec 20:30 (planned, NOT scheduled) | no |
| 2026-11-30 | 5 holiday gift guide | Cozy Pajamas | theme list, 2 pins | Pink gingham flannel pajama set (ASIN tbc); Blush waffle knit robe (ASIN tbc); Faux fur lined moccasin slippers in pink (ASIN tbc); Satin sleep mask (ASIN tbc); Ribbed knit lounge set in cream (ASIN tbc); Knit covered hot water bottle in pink (ASIN tbc) | tbc | Cozy Pink Christmas Pajamas for Women: Gingham Flannel, Waffle Robe and Fuzzy Slippers | Christmas Morning Pajamas Outfit: Pink Gingham Flannel, Blush Robe and Faux Fur Slippers | 30 Nov 13:30, 3 Dec 20:30 (planned, NOT scheduled) | no |
| 2026-12-01 | 5 holiday gift guide | For College Girls | theme list, 2 pins | Blush heated throw blanket (ASIN tbc); Cordless rechargeable table lamp (ASIN tbc); Pink mesh shower caddy tote (ASIN tbc); Bed wedge reading pillow (ASIN tbc); Satin pillowcase set (ASIN tbc); Pink acrylic desk organizer set (ASIN tbc); Clip-on bedside shelf (ASIN tbc) | tbc | Pink Dorm Room Gifts for College Girls: Heated Throw, Cordless Lamp and a Cute Shower Caddy | College Care Package Ideas for Her: Pink Dorm Essentials That Make Winter Break Better | 1 Dec 13:30, 4 Dec 20:30 (planned, NOT scheduled) | no |
| 2026-12-03 | 5 holiday gift guide | For Coworkers | theme list, 2 pins | Faux succulent in a ceramic pot (ASIN tbc); Pastel pink gel pen set (ASIN tbc); Mini hand cream trio (ASIN tbc); Small candle in a glass jar (ASIN tbc); Pink sticky note set (ASIN tbc); Tinted lip balm set (ASIN tbc); Blush acrylic desk organizer (ASIN tbc) | tbc | Cute Coworker Christmas Gifts That Aren't a Mug: Desk Finds They'll Actually Keep | Office Christmas Gift Ideas for Coworkers: Little Pink Gift Bags Everyone Will Keep | 3 Dec 13:30, 6 Dec 20:30 (planned, NOT scheduled) | no |
| 2026-12-04 | 5 holiday gift guide | Teachers | theme list, 2 pins | Insulated tumbler with lid and straw (ASIN tbc); Beaded lanyard (ASIN tbc); Scented hand sanitizer set (ASIN tbc); Fine tip pen set (ASIN tbc); Pink stapler and tape dispenser set (ASIN tbc); Dry erase marker set (ASIN tbc); Pink gift card holder (ASIN tbc) | tbc | Teacher Christmas Gifts They'll Actually Want: Tumbler, Beaded Lanyard and Nice Pens | Teacher Gift Ideas From Kids: A Little Pink Gift Bag Packed on the Mudroom Bench | 4 Dec 13:30, 7 Dec 20:30 (planned, NOT scheduled) | no |
| 2026-12-05 | 5 holiday gift guide | Dog Lovers | theme list, 2 pins | Pink gingham dog bandana (ASIN tbc); Blush leash and collar set (ASIN tbc); Silicone treat pouch in pink (ASIN tbc); Reusable pet hair remover roller (ASIN tbc); Paw cleaner cup (ASIN tbc); Slow feeder bowl in pink (ASIN tbc); Waterproof couch cover in cream (ASIN tbc) | tbc | Gifts for Dog Moms: Gingham Bandana, Blush Leash, Treat Pouch and a Couch-Saving Cover | Dog Mom Gift Ideas: A Pink Gingham Bandana Walk With a Golden Retriever on the Farm | 5 Dec 13:30, 8 Dec 20:30 (planned, NOT scheduled) | no |
| 2026-12-06 | 5 holiday gift guide | Bag Charms | theme list, 2 pins | Beaded bow bag charm (ASIN tbc); Mini plush bag charm (ASIN tbc); Cream crescent shoulder bag (ASIN tbc); Silk skinny scarf for the bag strap (ASIN tbc); Gold chain keyring (ASIN tbc); Pink heart coin purse (ASIN tbc); Tortoise cat eye sunglasses (ASIN tbc) | tbc | Bag Charms and Trendy Accessory Gifts: Beaded Bows, a Crescent Bag and a Silk Scarf | How to Style Bag Charms: A Cream Crescent Bag, Beaded Bow Charm and Silk Scarf | 6 Dec 13:30, 9 Dec 20:30 (planned, NOT scheduled) | no |
| 2026-12-07 | 5 holiday gift guide | Books | theme list, 2 pins | A cozy winter romance novel (ASIN tbc); A page-turning thriller (ASIN tbc); Rechargeable clip-on book light (ASIN tbc); Quilted pink book sleeve (ASIN tbc); Reading journal (ASIN tbc); Tassel bookmark set (ASIN tbc); Wooden thumb page holder (ASIN tbc) | tbc | Books as Gifts: A Cozy Book Lover Gift Bundle With a Book Light, Sleeve and Reading Journal | Book Lover Gift Ideas for Her: The Snowy Window Seat Reading Nook in Pink and Gingham | 7 Dec 13:30, 10 Dec 20:30 (planned, NOT scheduled) | no |
| 2026-12-08 | 5 holiday gift guide | Car Accessories | theme list, 2 pins | Pink steering wheel cover (ASIN tbc); Heated seat cushion (ASIN tbc); Car seat gap filler organizer (ASIN tbc); Pink cupholder coaster set (ASIN tbc); Mini car trash can in pink (ASIN tbc); Vent clip diffuser (ASIN tbc); Magnetic phone mount in pink (ASIN tbc) | tbc | Pink Car Accessories That Make Great Gifts: Steering Wheel Cover, Heated Seat and More | Cute Car Accessories for Women: A Pink Steering Wheel Cover and a Cozier Winter Commute | 8 Dec 13:30, 11 Dec 20:30 (planned, NOT scheduled) | no |
| 2026-12-10 | 5 holiday gift guide | Party Outfits | theme list, 2 pins | Pink velvet long sleeve mini dress (ASIN tbc); Sheer black tights (ASIN tbc); Glitter Mary Jane heels (ASIN tbc); Satin bow hair clip (ASIN tbc); Crystal drop earrings (ASIN tbc); Beaded top handle mini bag in cream (ASIN tbc); Cropped faux fur jacket in cream (ASIN tbc) | tbc | Pink Holiday Party Outfits: A Velvet Mini Dress, Satin Bow and Sparkly Mary Janes | Christmas Party Outfit Idea: Pink Velvet Mini Dress, Black Tights and a Faux Fur Jacket | 10 Dec 13:30, 13 Dec 20:30 (planned, NOT scheduled) | no |
| 2026-12-11 | 5 holiday gift guide | White Elephant | theme list, 2 pins | Mini waffle maker in pink (ASIN tbc); Mini massage gun (ASIN tbc); Portable mini projector (ASIN tbc); Cordless milk frother (ASIN tbc); Bluetooth karaoke microphone (ASIN tbc); Candle warmer lamp (ASIN tbc); Pink and gold wrapping paper rolls (ASIN tbc) | tbc | White Elephant Gifts People Actually Fight Over: Mini Projector, Waffle Maker and More | Best White Elephant Gift Ideas for the Barn Christmas Party: Wrapped in Pink and Gold | 11 Dec 13:30, 14 Dec 20:30 (planned, NOT scheduled) | no |
| 2026-12-12 | 5 holiday gift guide | New Moms | theme list, 2 pins | Nursing-friendly waffle robe (ASIN tbc); Large water bottle with handle and straw (ASIN tbc); Dry shampoo (ASIN tbc); Silk eye mask (ASIN tbc); Cordless neck and shoulder massager (ASIN tbc); Snack caddy organizer (ASIN tbc); Soft pink knit baby blanket (ASIN tbc) | tbc | Gifts for New Moms That Are Actually for Her: Waffle Robe, Eye Mask and a Giant Water Bottle | New Mom Gift Basket Ideas: Cozy Things for Her, Packed in the Nursery Glider | 12 Dec 13:30, 15 Dec 20:30 (planned, NOT scheduled) | no |
| 2026-12-13 | 5 holiday gift guide | Travel Gifts | theme list, 2 pins | Pink hardside carry-on suitcase (ASIN tbc); Packing cube set (ASIN tbc); Travel jewelry case (ASIN tbc); Clear toiletry bag (ASIN tbc); Blush travel journal (ASIN tbc); Pink memory foam neck pillow (ASIN tbc); Pink passport cover (ASIN tbc) | tbc | Pink Travel Gifts for Her: A Carry-On, Packing Cubes, Travel Journal and Jewelry Case | Travel Gift Ideas for Women: Rolling a Pink Carry-On Out the Farmhouse Door at Dawn | 13 Dec 13:30, 16 Dec 20:30 (planned, NOT scheduled) | no |
| 2026-12-14 | 5 holiday gift guide | Snail Mail | theme list, 2 pins | Wax seal stamp kit (ASIN tbc); Cream notecards and envelopes box (ASIN tbc); Fountain pen with ink cartridges (ASIN tbc); Pink washi tape set (ASIN tbc); Linen address book (ASIN tbc); Pink stationery set (ASIN tbc); Brass letter tray (ASIN tbc) | tbc | Snail Mail Stationery Gifts: Wax Seal Kit, Cream Notecards, Washi Tape and a Fountain Pen | Snail Mail Gift Ideas: Pressing a Wax Seal at a Farmhouse Writing Desk | 14 Dec 13:30, 17 Dec 20:30 (planned, NOT scheduled) | no |
| 2026-12-15 | 5 holiday gift guide | Self-Care Night In | theme list, 2 pins | Bamboo bathtub caddy tray (ASIN tbc); Bath soak salts (ASIN tbc); Pink satin robe (ASIN tbc); Cooling gel eye mask (ASIN tbc); Hydrating sheet mask set (ASIN tbc); Silicone face scrubber (ASIN tbc); Pink bath pillow (ASIN tbc) | tbc | Self-Care Night In Gift Ideas for Women: Bath Tray, Satin Robe, Eye Mask and Bath Soak | At Home Spa Night Ideas: A Clawfoot Tub, Pink Satin Robe and a Bamboo Bath Tray | 15 Dec 13:30, 18 Dec 20:30 (planned, NOT scheduled) | no |
| 2026-12-17 | 5 holiday gift guide | Pink Holiday Table | theme list, 2 pins | Blush linen napkins (ASIN tbc); Pink taper candles (ASIN tbc); Brass taper candle holders (ASIN tbc); Scalloped white dinner plate set (ASIN tbc); Gold flatware set (ASIN tbc); Faux eucalyptus garland runner (ASIN tbc); Gold napkin rings (ASIN tbc) | tbc | Pink Christmas Table Decor That Looks Expensive: Blush Linen, Brass Candlesticks and Tapers | Pink Christmas Tablescape Ideas: Lighting the Tapers on a Farmhouse Dining Table | 17 Dec 13:30, 20 Dec 20:30 (planned, NOT scheduled) | no |


---

## 6. Jodie's steps: Idea Lists, SiteStripe links and images

Run these on your desktop with your computer linked, in your own signed-in Chrome. The recipe behind every step is `claude/TDIE_LEGALLY_BLONDE_PIN_FACTORY.md` sections 3, 3b, 3c, 4 and 5. Work one look at a time, in the order of the table in section 3, so the earliest pin dates are ready first.

**Before you start**
1. Take the Command Centre browser lock (`claude/TDIE_BROWSER_LOCK.md`) so no scheduled task uses Chrome at the same time.
2. Confirm you are signed in to Amazon with your Associates and Influencer account: open any product page and check the SiteStripe bar is across the top. If it is missing, sign in before going on. A link without your tag pays nothing.
3. Open this file and `claude/HOLIDAY_GIFT_GUIDES_LINKS.md` on GitHub, branch `claude/tdie-holiday-gift-guides-y2c7l4`.

**A. Sourcing and the Idea List (repeat for each of the 25 looks)**

4. For each item in the look's "Items to source" list, search amazon.com. Pick a product that is in stock (not "only a few left"), Prime where possible, 4.0 stars or better with at least 100 ratings, and clearly photographed. Skip any listing whose name uses Barbie or another name on canon's IP list, and prefer products with no printed words or logos on them.
5. In the links file, write the product's short name and its ASIN on that item's row.
6. Go to your storefront (https://www.amazon.com/shop/thedigitalincomeedit) > Create content > Idea List.
7. Title: the look's page title from section 4. Description: the Idea List description from section 4.
8. Click Add products > Browse history tab > search one ASIN > tick it > Done. Repeat for every item. If an ASIN does not come back in the search, swap that product for one that does, then update step 5.
9. Dismiss the AI description suggestion (its X). Save > Submit.
10. On the storefront page, open the new list and copy its public address. It must read `https://www.amazon.com/shop/thedigitalincomeedit/list/<id>`. It must never contain `influencer-adc3fcaa`. Paste it into the look's Idea List row in the links file.

**B. SiteStripe short links (every item, every look)**

11. Open each chosen product's page, click "Get Link" in the SiteStripe bar, choose Short Link, and copy it.
12. Check it starts with `https://link.amazon/`. If you got the long link, click Short Link again and re-copy.
13. Paste it into that item's row in the links file.

**C. Product sheet (one per look, for the image generators only)**

14. Make one screenshot of the look's main product images side by side (the factory's section 3c overlay method). Never download Amazon's images and never post them. The sheet is only a reference for the generators.

**D. The two images (repeat for each look)**

15. Flat lay: open Higgsfield Seedream 4.5 (`https://higgsfield.ai/ai/image?model=seedream_v4_5`). Clear old references. Attach the `stylerefs` image named in section 4, then the product sheet. Set 4K and portrait 2:3, and check the Unlimited switch is ON. Paste the look's flat lay prompt exactly as written and generate.
16. Check it at feed size: every item is there and fully inside the frame, the title is spelled right, crisp and sits on the image, and there are no logos or brand names. Fix anything wrong in the same thread, telling it exactly what to change, at most two rounds. Garbled or soft letters go to Nano Banana Pro 2K on Higgsfield with the same prompt.
17. Lifestyle: open Google Gemini. Attach, in this order, the style reference named in section 4, the Omni seed as a JPEG under 400 KB, then the product sheet. Paste the look's lifestyle prompt exactly as written.
18. Check it at feed size. The face follows the reference, or is hidden the way the format says. Hands have five natural fingers. The glitter pink tumbler with the lavender straw is there. Every product matches its screenshot. There is no text or logo anywhere. It is one photo, not a grid. Fix in the same chat, at most two rounds. If Gemini is out of images or keeps failing, run the same prompt and attachments on Nano Banana Pro 2K on Higgsfield.
19. If an image looks glossy, add light grain by hand (noise, sigma about 5) rather than generating again.
20. Save each image at exactly 1000 by 1500, JPEG quality 82, named `<slug>-flatlay.jpg` and `<slug>-lifestyle.jpg` with the slug from section 4.

**E. Upload and hand back**

21. Upload all the images to `src/lifestyle` on the branch through https://github.com/jodiedeo7-glitch/tdie/upload/claude/tdie-holiday-gift-guides-y2c7l4/src/lifestyle. Do it in one go if you can. Commit message: "Lifestyle: holiday gift guide images".
22. Commit the filled-in `claude/HOLIDAY_GIFT_GUIDES_LINKS.md` to the same branch.
23. Append the section 5 rows to the project copy of `claude/LB_PIN_LOG.md`, with the ASINs and Idea List addresses filled in. From there the weekly Legally Blonde factory schedules the pins week by week. It schedules built-but-not-scheduled pins before building new looks, and never more than 14 days ahead. The igqueue picks up the Instagram posts the same way.
24. Release the browser lock.
25. Come back to this session and say "links and images are in".

**Paste-ready prompt for the desktop session** (copy everything inside the box):

```
Holiday Gift Guides sourcing and image run for The Digital Income Edit. Start your reply with "Sources checked:" and the files you actually opened.

Read first, from the TDIE project: claude/CLAUDE_SOURCE_CHECK_RULE.md, claude/TDIE_IMAGE_GENERATION_MASTER.md, claude/TDIE_LEGALLY_BLONDE_PIN_FACTORY.md (sections 3, 3b, 3c, 4, 5), claude/TDIE_BROWSER_LOCK.md, claude/LB_PIN_LOG.md. Load the tdie-image-prompt skill. Then read claude/HOLIDAY_GIFT_GUIDES_BUILD.md and claude/HOLIDAY_GIFT_GUIDES_LINKS.md from GitHub repo jodiedeo7-glitch/tdie, branch claude/tdie-holiday-gift-guides-y2c7l4 (not main).

Work through the 25 looks in the date order of section 3 of the build file. For each look: take the browser lock; source every item on Amazon with factory section 3 rules; record short name, ASIN and SiteStripe short link (must start https://link.amazon/) in the links file; build the Idea List under https://www.amazon.com/shop/thedigitalincomeedit with the title and description given in section 4 and copy its public /list/<id> address (never influencer-adc3fcaa); make one product sheet screenshot; generate the flat lay on Seedream 4.5 on Higgsfield (Unlimited ON, 4K, 2:3) with the named stylerefs image and the product sheet, pasting that look's flat lay prompt exactly; generate the lifestyle photo in Google Gemini with the named style reference, the Omni seed and the product sheet, pasting that look's lifestyle prompt exactly, falling back to Nano Banana Pro 2K on Higgsfield. Check every image at feed size against section 18 of the steps, at most two correction rounds per image. Never Canva. Nothing saved to Jodie's Downloads.

Save images as 1000 by 1500 JPEG quality 82 named <slug>-flatlay.jpg and <slug>-lifestyle.jpg and upload them to src/lifestyle on branch claude/tdie-holiday-gift-guides-y2c7l4 (https://github.com/jodiedeo7-glitch/tdie/upload/claude/tdie-holiday-gift-guides-y2c7l4/src/lifestyle). Commit the filled links file to the same branch. Do not edit the look JSON files, do not remove any draft flag and do not touch main. Append the section 5 rows of the build file to the project copy of claude/LB_PIN_LOG.md with ASINs and Idea List addresses filled in, in full with project_write. Release the browser lock.

No prices, no em dashes, no links on Instagram. If the SiteStripe bar is missing, stop and tell Jodie in one line. Report in one line when all 25 looks have links, lists and both images, or name exactly which look and item did not finish.
```

---

## 7. What I do when you say "links and images are in"

1. Re-read canon.json and this file. Read the links file and write every `link`, every `ideaList` and the sourced item names into the 25 JSON files.
2. Look at all 50 images myself: size, name, the pink rule, no logos, no text on the lifestyle photos, title spelling on the flat lays. Then correct any alt text that no longer matches the picture.
3. Remove `"draft": true` and set `date` to the day the pages go live.
4. Run `npm run build` and confirm it passes with all 25 pages built.
5. Push to the branch, then ask you before merging to `main`. `main` is what goes live, and I don't push there without your yes.
6. After the deploy, open all 25 live URLs and /lifestyle and check:
   - every page loads and every image displays;
   - both disclosures are on every page;
   - every Amazon link resolves to Amazon, carries `rel="sponsored nofollow"`, and is a SiteStripe short link or a `/shop/thedigitalincomeedit/list/` Idea List;
   - all 25 are in the Holiday Gift Guides block;
   - no price and no em dash on any page.
7. Check the log in the project file: all 50 pins logged, every destination is that look's Idea List, and there is no thedigitalincomeedit.com link on any pin. Check the Instagram captions: no link anywhere.
8. Re-read the live result against the source files and report in one line with the hub link.

**The Digital Income Edit, Holiday Gift Guides Build, 26 September 2026**
