# Skool About gallery: final set (11 October 2026)

This set replaces the whole Skool About gallery. Upload these five files in this order and delete every other image in the gallery.

| Slot | File | What it does |
|---|---|---|
| 1 | `out/01-hero.jpg` | Faceless income, built with AI. Attic loft. |
| 2 | `out/02-same-effort.jpg` | Same effort. Opposite order. Farmhouse kitchen. |
| 3 | `out/03-roadmap.jpg` | Four steps. One build. (Jodie's Roadmap copy, word for word.) Garden beds and red barn. |
| 4 | `out/04-member-wins.jpg` | Real members. Real wins. (Quotes word for word.) Living room sofa. |
| 5 | `out/05-tiers.jpg` | Two ways in. Both free for 7 days. Porch rocking chair. |

**Delete from the gallery:** the "Inside the classroom / Offer first. Audience last." graphic, "Membership Premium / Where the business starts paying", "Choose your membership" (pink wash), the "DFY Content Calendar / Every month, I write your content for you" graphic, the old "Get Your First Online Income in 90 Days" graphic, the video thumbnail if it is the old one, and anything else not in the table.

## Why the four uploaded graphics were rejected

They break standing rules in `ops/cloud-kit/TDIE_DESIGN_RULES.md`:

| Graphic | Broken rules |
|---|---|
| Inside the classroom | Full hot pink wash; blurred background; no photo of her; "25 courses" (canon: 21 published, Roadmap uses "20+"); course mapping does not match Jodie's Roadmap copy (Ads Edit under funnel, both vaults under "Offer") |
| Where the business starts paying | Full hot pink wash; blurred; same photo as the next graphic; lesson counts and "The Operating Prompts™ included" not verifiable in canon |
| Choose your membership | Full hot pink wash; blurred; same photo reused; italic tier lines ("Build it. Then sell it." / "Everything you need to scale.") |
| DFY Content Calendar | Stone background with no world; dark chocolate footer bar; catalogue-style standing pose; no tumbler; em dash |

None of these four files exist in the repo; they were not made from this folder.

## How this set follows the rules (rebuilt 11 October 2026, second pass)

The first pass of this set was rejected by Jodie the same day: hot pink gradient cards, glass and glow effects, and photos that were not Tommy Kate enough (white modern kitchen and living room, a beam down the loft wall, a clean new porch, none of her named props). This pass fixes both.

- **No gradients, no glass, no glow.** Follows the site's own system in `src/styles/edit.css` ("No glass, no glow, no gradients on buttons. Depth comes from scale, crop and contrast."): solid Signature Hot Pink cards and buttons, white paper cards with a Muted Gold hairline and a plain lift shadow, gold-hairline kickers. The only gradient left is the cream fade from the copy into the photo, which is the approved 25 September layout. No fake sparkle in the design; the one sparkle moment is in each photo.
- **Type:** Newsreader SemiBold upright headlines, Inter for everything else, no italics, no brown.
- **Photos copied from her world file** (`ops/cloud-kit/TDIE_DFY_CALENDAR_TOMMY_KATE_WORLD.md` and the 4 Oct handoff rules), Nano Banana Pro 2K on Higgsfield, avatar seed attached, "this exact woman" opening, no locked feature written:
  - **Hero, pink attic loft:** ivy-wrapped ceiling beams, plush pink shag rug, pastel pink gaming desk, glass-panel PC glowing pink, Hello Kitty and Kuromi plushies, the grey British Shorthair cat, lavender controller with the strawberry charm, candy-pink headphones, scrunchie, fuzzy socks.
  - **Same effort, farmhouse kitchen:** blush cabinets, butcher-block island, copper pans with patina, the Player Two? mug, lilacs in a mason jar, gold claw clip, heart necklace, the retriever with his rope toy.
  - **Roadmap, outside:** raised garden beds, split rail fencing, chicken coop with hens, wildflower field, sage barn coat, ribbed tank, vintage denim, worn brown farm boots, candy-pink gardening gloves, the retriever.
  - **Member wins, living room:** candy-pink velvet pillow, a patchwork quilt someone uses, peonies, rhinestone claw clip (the sparkle), hot pink manicure, fuzzy socks, the retriever.
  - **Tiers, porch:** chipped white paint, rocking chair with a patchwork quilt, potted herbs, lilacs, pasture and split rail fence, glitter pink cowboy boots (the sparkle), the retriever.
  - Her glitter-flecked candy-pink tumbler with the lavender straw is in every photo and never hidden by copy. No logos, no text in any photo except Player Two? on the mug.
- **Plushies note:** the world file requires the Hello Kitty and Kuromi plushies whenever the loft is in frame, and allows them as her home plushies; they are background props in the hero, not a product or a subject.
- **Copy:** unchanged from the first pass (audit + Jodie's Roadmap copy word for word).

### Defects found at full size and fixed before sending (second pass)

- Photos rejected and regenerated: pale or see-through tumbler (loft, living room twice), Xbox logo on the controller, Apple logo on the laptop (porch twice), her leg and boots under the tier cards (porch).
- Cream fade had hard vertical edges (gradient stops out of order) → fixed.
- Words alone on a line ("a sale", "Audience / first", "Your / offer", third chip) → fixed.
- Cards touching the Player Two? mug, her basket and gloves, the dog's head → photos repositioned or cards narrowed.

## Skool description (paste into the About text box)

You don't need an audience. You need something to sell. 💗

You've been told to build the audience first and the offer later. That's why you've posted for months with nothing to show for it.

The Digital Income Edit™ runs it backwards. Offer first. Funnel second. Automation third. Audience last.

You walk out with a machine: an offer, a funnel, an email list that's yours, and a persona that fronts it. Not a content habit. A business.

Built faceless, start to finish✨ I built this whole business this way: no face on camera, no audience when I started. 1,200+ women are already inside.

**Standard, $9/month or $99/year.** Everything you need to build the thing and start selling it.
✅ AI Twin Creation - an AI persona fronts your brand, so your face never has to
✅ Pinterest Foundations™ + The Email Edit - traffic and a list you own
✅ The Content Edit + The Monetization Edit - make it, then make it pay

**Premium, $35/month or $297/year.** Everything in Standard, then the full build, and your content written for you.
📅 DFY Content Calendar - 31 days of finished content, every month
✅ The Offer Edit + The Funnel Edit - the offer and the funnel, built first
✅ The Ads Edit™ · Scaling & Systems · The Premium Vault (every guide unlocked)

20+ courses across both.

✨Click the Community & Classroom tabs above for a free look inside!✨

✨ Start your 7 days free. Then $9/month, or pick Premium. Leave from inside the app any time.

## Re-render

`node ops/cloud-output/about-gallery-2026-10/render.mjs` from the repo root. Output is 3200×1800 JPG (1600×900 at 2x), quality 93.
