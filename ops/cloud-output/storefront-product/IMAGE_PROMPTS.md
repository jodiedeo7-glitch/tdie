# Image prompts: cover and 4 launch graphics

Written 27 Sep 2026 per `ops/cloud-kit/TDIE_IMAGE_GENERATION_MASTER.md` and `TDIE_DESIGN_RULES.md`. The cloud session cannot run Gemini or Higgsfield, so every photo is prompted here in full and generated at the desktop finish (queue section 4, step 2). Until then each graphic and the PDF cover render with a clean placeholder box.

Tool routing: every photo with Tommy Kate goes to **Google Gemini** first with the seed attached (`public/images/library/avatar-seed-omni-reference.png`), then Nano Banana Pro at 2K on Higgsfield if Gemini is out of credits or the face drifts. Every photo without her goes to **Seedream 4.5 on Higgsfield with Unlimited on**. Garbled or unsatisfactory results re-run on Nano Banana Pro at 2K. Never Canva. No text is generated in any of these photos: the words are set in code by `render.mjs`.

After generating: save each photo under the file name given, in `ops/cloud-output/storefront-product/graphics/photos/`, then run `node ops/cloud-output/storefront-product/render.mjs` from the repo root and check every output at feed and thumbnail size (face, hands, the pink object, no stray lettering).

| # | File name | Used in | Size rendered | Person | Tool |
|---|---|---|---|---|---|
| Cover | `cover-sofa-dusk.jpg` | Setup Guide PDF cover, presale PDF | photo fills right 58% of an A4-ratio page | Tommy Kate | Gemini |
| 1 | `g1-porch-morning.jpg` | Skool 2 (presale open) header, Beacons product image | 1600 × 900 | Tommy Kate | Gemini |
| 2 | `g2-loft-night-desk.jpg` | Skool 1 (tease) header | 1600 × 900 | none | Seedream 4.5 |
| 3 | `g3-kitchen-late.jpg` | Facebook 1 and 2 image, Skool 4 (last call) header | 1080 × 1350 | Tommy Kate | Gemini |
| 4 | `g4-nightstand-phone.jpg` | Sales page share image (OG), Skool 5 (launch) header | 1200 × 630 | none | Seedream 4.5 |

---

## Cover · `cover-sofa-dusk.jpg` · Gemini (seed attached)

**Why it exists:** the product's promise in one picture: the work happens while she rests.
**Composition for the page:** she is in the right third; the left 40% is calm cream wall and window for the HTML title.

> Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference. She is curled up asleep on the white slipcovered sofa in her farmhouse living room at dusk, lying on her side under a chunky cream knit throw, one arm tucked under a gingham cushion, eyes closed, completely relaxed. Her hair is loose and a little messy against the cushion. She wears an oversized saturated candy-pink knit sweater, never pale, and soft grey sweatpants, with fuzzy cream socks. On the low wooden coffee table in front of her sits her glitter-flecked pink iced coffee tumbler with a lavender straw, saturated candy pink, never pale, beside a closed laptop and a small jar of lilacs. Her golden retriever sleeps on the braided rug below the sofa. Quiet wealth, lived in: a real farmhouse room, wide plank floors, a window with the last blue light of evening and one warm table lamp on. She fills the right third of the frame; the left side is calm, open cream wall and window with nothing important in it. Soft practical lamplight mixed with fading blue-hour window light, gentle real shadows. Photorealistic real-world photography, 35mm lens, natural depth of field, true-to-life fabric and wood textures, natural imperfections, lifelike details. Landscape 3:2. No text, no lettering, no logos, no screens showing anything, no watermark, no generic luxury setting.

---

## Graphic 1 · `g1-porch-morning.jpg` · Gemini (seed attached)

**Why it exists:** the morning after: she checks her phone with coffee, and the work is already done.
**Composition:** she is in the right third; the left half is porch rail, lilacs and soft morning sky, calm for the headline card.

> Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference. Early morning on her farmhouse front porch. She sits in a white wooden rocking chair with her knees pulled up, looking down at her phone with a small, pleased half-smile, as if she has just seen something good. Her hair is up in a loose gold claw clip. She wears an oversized saturated candy-pink hoodie, never pale, soft cream leggings and fuzzy socks. In her other hand, her glitter-flecked pink iced coffee tumbler with a lavender straw, saturated candy pink, never pale. A folded gingham blanket over the chair arm, a big pot of lilacs on the porch boards, and the red barn and pasture soft in the background with morning mist. Quiet wealth, lived in. She sits in the right third of the frame; the left half is open porch rail, lilacs and pale morning sky, with nothing important in it. Soft golden early-morning sunlight from the side, real shadows on the porch boards. Photorealistic real-world photography, 50mm lens, natural depth of field, realistic wood grain, true-to-life textures, natural imperfections. Landscape 16:9. The phone screen faces away from the camera. No text, no lettering, no logos, no watermark.

---

## Graphic 2 · `g2-loft-night-desk.jpg` · Seedream 4.5, Unlimited on (no person)

**Why it exists:** the tease: the desk is empty, the lamp is on, the work is happening without her.
**Pink object (exactly one):** candy-pink over-ear headphones.
**Composition:** the desk sits in the right half; the left half is the dark window and sloped attic ceiling, calm for the headline.

> Real-world photograph of a cozy attic gaming loft in a farmhouse at night, nobody in the room. A white wooden desk under the sloped ceiling holds an open laptop with its screen turned away from the camera, casting a soft glow on the desk, a stack of two linen notebooks, a small jar of dried lilacs, and a pair of saturated candy-pink over-ear headphones, never pale, resting beside the laptop. That pair of headphones is the only pink object in the frame. A knitted cream throw over the back of an empty desk chair, warm string lights along a wooden beam, a round window showing a dark blue night sky with a few stars and the faint outline of a red barn. Quiet wealth, lived in: real, tidy, not staged. The desk sits in the right half of the frame; the left half is the calm dark window and sloped ceiling with nothing important in it. Warm practical lamplight and the soft laptop glow, deep natural shadows. Photorealistic, 35mm lens, natural depth of field, realistic wood and fabric textures, natural imperfections, lifelike details. Landscape 16:9. No other pink objects, no text, no lettering, no logos, no readable screen, no people, no watermark.

---

## Graphic 3 · `g3-kitchen-late.jpg` · Gemini (seed attached)

**Why it exists:** last call: she closes the laptop at night and goes to bed, the machine keeps going.
**Composition:** vertical 4:5; she stands in the lower right; the upper 45% is calm kitchen wall, open shelves and window, for the headline card.

> Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference. Late evening in her farmhouse kitchen. She stands at the butcher block island, gently closing her laptop with one hand, turning away toward the stairs as if heading to bed, relaxed and unhurried. Her hair is in a loose low braid. She wears a soft oversized saturated candy-pink knit cardigan, never pale, over a white tee and grey sweatpants. On the island beside the laptop, her glitter-flecked pink iced coffee tumbler with a lavender straw, saturated candy pink, never pale, and a small bowl of lemons. Open wooden shelves with stacked white dishes, a window over the farmhouse sink showing a dark night, one warm pendant light on above the island. Her golden retriever waits by the doorway. Quiet wealth, lived in. She stands in the lower right of a vertical frame; the upper part is calm kitchen wall, shelves and window with nothing important in it. Warm practical pendant light, soft real shadows. Photorealistic real-world photography, 50mm lens, natural depth of field, realistic butcher block and fabric textures, natural imperfections. Portrait 4:5. No text, no lettering, no logos, no screens showing anything, no watermark.

---

## Graphic 4 · `g4-nightstand-phone.jpg` · Seedream 4.5, Unlimited on (no person)

**Why it exists:** the share image: the phone lights up on the nightstand at night; something happened while she slept.
**Pink object (exactly one):** the glitter-flecked pink tumbler.
**Composition:** wide 1.91:1; the nightstand sits in the right third; the left two thirds are soft dark bedroom, calm for the headline.

> Real-world photograph of a farmhouse bedroom nightstand at night, nobody in the frame. A white painted wooden nightstand beside a bed with rumpled white linen sheets and a chunky cream knit throw. On the nightstand: a phone lying face down with a faint glow at its edges, a small ceramic dish with a gold claw clip, a paperback book, a small jar of lilacs, and a glitter-flecked pink iced coffee tumbler with a lavender straw, saturated candy pink, never pale. The tumbler is the only pink object in the frame. A small bedside lamp turned low, a window with soft blue moonlight through linen curtains. Quiet wealth, lived in: real, calm, lightly lived in. The nightstand sits in the right third; the left two thirds are the softly lit bed and dark wall, calm and uncluttered. Low warm lamplight and cool moonlight, natural shadows. Photorealistic, 50mm lens, shallow natural depth of field, true-to-life linen and wood textures, natural imperfections. Landscape, very wide, about 1.91 to 1. No other pink objects, no text, no lettering, no logos, no readable screen, no people, no watermark.

---

## Pre-generation check (all five)

- Tommy Kate frames open with the reference line, describe no locked feature, and carry her glitter tumbler plus other pink (her knit, hoodie or cardigan). Never "the only pink item".
- Person-free frames carry exactly one saturated candy-pink object (headphones in 2, the tumbler in 4), each different.
- Her world only: living room sofa, porch, kitchen island, attic loft, bedroom. No two graphics share a room.
- Real light, real lens, photorealism language, no text, no logos, no hex codes.
- Wardrobe from the locked list: oversized knits, hoodie, cardigan over a tee, sweatpants, leggings.
