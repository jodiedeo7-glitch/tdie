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

## How this set follows the rules

- **Approved build (design rules §2):** cream base, Tommy Kate on the right in a different place in her world each time, cream scrim on the left holding the copy, frosted white cards with a thin gold line, one glossy hot pink hero card per graphic, round tilted stickers, hot pink pill CTA.
- **THE LOOK (Decision 128):** Newsreader SemiBold upright headlines, Inter for everything else, no italics, no brown, no full pink wash, sparkle on the hero card and the foil callout only.
- **Photos:** Nano Banana Pro at 2K on Higgsfield, avatar seed attached, "this exact woman" opening, no locked feature written. Every photo has her glitter-flecked candy pink tumbler with the lavender straw, visible and not covered by copy. No logos, no plushies (sales graphic), no text in the photos.
- **Copy:** from `ops/cloud-output/SKOOL_ABOUT_CONVERSION_AUDIT.md`. Pinterest Foundations™ (live course), never The Pinterest Edit (draft). The Ads Edit™ has no price. The Value Vault is "guides à la carte" for Standard. $171 = $37 + $37 + $97. No price-increase line (it ended 30 September).
- **Look-before-you-send:** every graphic was rendered and checked at full size; defects found and fixed are listed below.

### Defects found and fixed before sending

- Headline running over her face (Same effort) → two-line headline.
- Stickers over her body or over copy (Hero, Same effort, Member wins) → moved into clear space.
- Words alone on a line ("alone", "to sell.", "AI / Twin") → wrapping fixed.
- "Start here" tag in the headline font → Inter.
- Photos rejected and re-generated: tumbler clear and pale (hero, kitchen); tumbler hidden under the copy (living room, porch twice, kitchen); brand logo on headphones (hero); logo on laptop (porch). Rejected files are in `rejected/` (not committed).

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
