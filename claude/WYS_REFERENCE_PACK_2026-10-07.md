# WYS master: workflow and Tommy Kate Halloween approved reference (7 Oct 2026)

> SINGLE ACTIVE WYS AUTHORITY. Read this entire file before WYS work. Generation is PAUSED; provider/model are unverified. The reference export and complete operating rules are consolidated here.

Source: Jodie's upload Tommy-Kate-Halloween-Cloud-Handoff.zip, prepared 2026-10-07T18:20:03.097205+00:00 (UTC). Two looks: Pretty Wicked entryway (home-decor) and Ghoul Fuel coffee bar. Jodie, 7 Oct 2026: this pack is the current WYS reference example for sourcing, prompts and content preparation. The photos are approved styling examples. Affiliate destinations and publication are still pending. This is not evidence that the whole automated workflow passed. Nothing in the pack is live.

The images stay private. They are not in the public repo and not in this document. Codex handles the /lifestyle website pages; Claude does not independently edit or publish them.

## 1. Generation configuration (exactly as recorded in the pack)

- Image provider and model: NOT RECORDED in the pack. The manifest, prompts, sourcing evidence and image files carry no provider, model or settings field, and the PNGs carry no metadata. UNVERIFIED; do not assume one.
- Output of every approved photograph: PNG, 1024 x 1536 pixels, vertical 2:3, RGB.
- Prompt length: every prompt under 3,000 characters (manifest check: ghoul-fuel-basic.txt 1975, ghoul-fuel-lifestyle.txt 1922, ghoul-fuel-styled.txt 1903, pretty-wicked-basic.txt 1950, pretty-wicked-lifestyle.txt 2721, pretty-wicked-styled.txt 2348).
- Reference attachments by role (REFERENCE-MAP.txt, full text in section 3): BASIC, supplied mood images only if wanted; STYLED, the matching basic.png to hold product shapes; LIFESTYLE, avatar-reference.png (1280 x 1908) as the only identity source plus the matching styled.png as room and decor reference.
- Sourcing method (sourcing-evidence.json): "Human-authorized Amazon browser sourcing; no paid scraping or generation". Intake route: "vibe photos". Reference count: 10.
- Other pack assets, made separately from the photographs: 3 Pinterest graphics per look (PNG 1000 x 1500) and 3 Instagram carousel slides per look (PNG 1080 x 1350). Their text lives on those graphics, never in the photographs.
- Pack checks: six photos present; six Pinterest PNGs; six carousel slides; two blog drafts; retail link ASINs match source. Affiliate destinations PENDING. Live publication NOT_RUN. Blog render audit UNVERIFIED (file: previews blocked). Exact retail product fidelity: APPROXIMATE_STYLING_ONLY.
- Lifestyle revision recorded in the manifest: file pretty-wicked-avatar-lifestyle-v2.png; Jodie's feedback "lifestyle image is much better"; composition: Porch viewpoint through open door, trick-or-treater foreground, console receding diagonally behind Tommy Kate. Rule: Lifestyle must differ from styled in camera angle, framing or POV; natural activity rather than avatar insertion into the same frame.

## 2. Image roles, three per look, all photorealistic vertical 2:3, no text in any photo

1. BASIC: straight-overhead styled flat lay of the selected retail products on a real surface, with named styling extras that are clearly not products. Every retail product distinguishable. No words, no furniture scene.
2. STYLED: a new lived-in room vignette with the products in use; styling extras listed separately from the shopping list; matching basic.png attached. No person.
3. LIFESTYLE: Tommy Kate (identity from avatar-reference.png only) in a separately composed photograph with a different camera angle, framing or viewpoint from STYLED, naturally doing something that fits the scene. Never the avatar pasted into the styled frame.

## Visual direction (from the approved images and prompts)

Cute adult pink maximalism: hot pink with black, cream, lavender and silver, with material contrast (matte, mirror, translucent). True hot pink, never a full-room pink wash. Late-afternoon side light with warm local glows; blue dusk outside with warm lamplight indoors for evening scenes. Tommy Kate's wardrobe in these: soft pink knit cardigan, white tank, straight jeans, pink low-top sneakers, gold studs, pink claw clip. Banned in these prompts: decorative bows or ribbons, hydrangeas, fur, shag or fluffy surfaces, logos, watermarks, text overlays, collages, extra people, copied layouts.

## 3. REFERENCE-MAP.txt (verbatim)

```text
Each prompt is under 3000 characters. For basic: use supplied mood images only if desired. For styled: attach the matching basic.png to preserve product shapes. For lifestyle: attach avatar-reference.png as person identity and the matching styled.png as room/decor reference. Lifestyle must be a separately composed photograph with a different camera angle, framing or POV from styled, plus natural human activity; never simply insert the avatar into the styled frame. Retail product shapes remain approximate in generated images. The stand-only correction used for Ghoul Fuel is retained separately as coffee-styled-prompt.txt at pack root.
```

## 4. The approved prompts (verbatim, from the pack's prompts folder)

### Pretty Wicked entryway: BASIC (prompts/pretty-wicked-basic.txt)

```text
Photorealistic vertical 2:3 image, crisp natural textures and clean black edges, adult playful pink maximalism. Preserve every selected product's real colour, finish, shape and size; no invented product features. No decorative bows, ribbons, hydrangeas, fur, shag or fluffy surfaces. No watermarks, interface, logos added to the scene or price claims. Selected products: Winlyn plain matte hot-pink ribbed foam pumpkins, 2.8–7.3 inches wide, dark gold-flecked stems, NO carved faces or added patterns; Qtisky pink open-weave gauze panels; Glooglitter pink pumpkin LED string lights, black jack-o-lantern faces, two 6.5-foot strands; Coogam black PVC bat silhouettes with folded wings; Homemory pink LED tea lights with white flame tips. Five retail products; display selected members of multipacks. STYLED FLATLAY: straight overhead on a worn black-painted wooden table, deliberately composed like a Halloween decorating afternoon. Pink open-weave gauze runs diagonally and pools at lower right, with black wood visible through the holes. Place three plain hot-pink pumpkins in graduated sizes at upper left, real dark stems clear. One unlit pink jack-o-lantern light strand snakes across the centre; preserve the black faces and visible cable. Five black PVC bat cutouts lie on a pale lavender card at upper right, wings partly folded; three pink LED tea lights sit near lower left. Add styling extras: an ornate empty silver picture frame tilted slightly beneath one gauze edge, a black bowl holding silver mirror spheres, a small sprig of pink roses and purple asters, a vintage key and a loose lavender cotton tassel. Layer black, hot pink, lavender and silver with strong material contrast; the pumpkins are matte, mirror balls reflective, gauze translucent. Leave just enough quiet space to distinguish all five retail products. No added faces on large pumpkins, no artificial flat sticker outlines around objects, no words, no furniture scene.
```

### Pretty Wicked entryway: STYLED (prompts/pretty-wicked-styled.txt)

```text
Create one NEW photorealistic vertical 2:3 lifestyle photograph for a pink Halloween blog. Attached image is mood reference ONLY: use its layered pink-and-black contrast, collected decor density and warm inviting atmosphere. Do not copy its composition, lettering, watermark, interface or patterned pumpkins.
Actual selected products must retain these designs: Winlyn plain matte hot-pink ribbed foam pumpkins, assorted 2.8–7.3 inches wide, dark gold-flecked stems, NO faces or painted patterns; Qtisky pink open-weave gauze; Glooglitter pink pumpkin LED string lights with sharp black jack-o-lantern faces; Coogam black PVC bat silhouettes with folded wings; Homemory smooth pink cylinder LED tea lights with white flame tips. Show selected members of these five multipacks, not every piece.
An inviting lived-in cottage entry vignette. Black console with curved legs and aged brass pulls against warm ivory walls, large oval black mirror above. Pink gauze drapes asymmetrically over the console, falling down its right edge. Three graduated plain hot-pink pumpkins sit at right, one pumpkin light strand loops low around them; another follows just the lower mirror edge. Nine black bats arc up the left wall toward the mirror. Four PINK-bodied LED tea lights glow on the tabletop.
Contextual styling extras, separate from shopping list: ornate silver frame with a wordless botanical ghost painting leaning left, black urn of pink roses and lavender asters with two dark branches, silver tray with keys, small black cauldron of wrapped candy. Under the console, woven basket with neatly folded pink-and-black checker cotton blanket; antique silver lantern with LED candle opposite. At right edge, arm of dusty-lavender upholstered chair and cream cushion with black bat silhouette. Oak floor, flatwoven ivory-and-black patterned rug, no shag.
Console and decor fill middle two-thirds, modest surroundings make it believable. Layer foreground, tabletop and wall without hiding products. Neutral late-afternoon side light with restrained warm local glows, true hot-pink pumpkin colour, readable crisp black faces and silhouettes. Cute adult maximalism, material variety and charming discoveries. No decorative bows or ribbons, hydrangeas, furry/fluffy surfaces, person, text overlay, collage, watermark, copied artwork or full-room pink colour wash.
```

### Pretty Wicked entryway: LIFESTYLE (prompts/pretty-wicked-lifestyle.txt)

```text
Use the avatar reference image only for the person. Create a NEW photorealistic vertical 2:3 lifestyle photograph of this same adult Tommy Kate answering the front door for Halloween trick-or-treaters. The second reference supplies the decor designs and home atmosphere, but rebuild the room from a completely different camera position.

CAMERA AND COMPOSITION: Photographer stands OUTSIDE on the porch, eye level, 35mm lens, looking diagonally through an open black front door into the entryway. The open door panel and white doorway frame occupy the left foreground; Tommy Kate stands full-length at the threshold in the central plane, turned three-quarter toward the porch. The black console is deeper inside on the RIGHT, seen in strong oblique perspective, its tabletop receding toward the back wall. Show the threshold, a little porch floor, and oak hallway floor to establish depth. This must look like a second photograph taken by someone at the door, not the frontal console photograph with a person inserted. Avoid the large centered mirror-and-console composition of the reference.

ACTION: Tommy Kate smiles naturally toward one small trick-or-treater seen only partly from behind in the lower-left foreground, wearing a simple white ghost costume and holding a candy bag. Tommy Kate holds a small black cauldron of wrapped candy at waist height with one hand; her other hand rests naturally on the open door. Clear, anatomically believable hands. Her attire is a soft pink knit cardigan, white tank, straight black jeans and pink low-top sneakers, suitable for a cozy evening at home. Preserve the reference person's identity without copying her original pose.

DECOR CONTINUITY: Same black curved-leg console with brass drawer pulls; hot-pink matte ribbed pumpkins in three graduated sizes with dark gold-flecked stems grouped toward its far end; open-weave pink gauze draped over the tabletop and right edge; pink jack-o-lantern bulb string lights with black faces on dark wire; crisp black folded-wing bat wall decorations; small squat pink LED tea lights with white plastic flame tips; black urn holding pink roses and lavender asters; ornate metallic frame with botanical ghost art, and a black oval mirror above the console, now foreshortened and partly cropped by this new viewpoint. A woven blanket basket below. Keep the purchased decor recognizable while the doorway activity is the story.

Realistic modest house dimensions, soft blue dusk outside and warm indoor lamplight, richly pink but balanced with black and cream, natural shadows, crisp believable textures, editorial Pinterest lifestyle photography. No graphic overlays, lettering, logos, bows, hydrangeas, shag rugs or additional people.
```

### Ghoul Fuel coffee bar: BASIC (prompts/ghoul-fuel-basic.txt)

```text
Create a NEW photorealistic portrait 2:3 BASIC curated editorial flatlay for Ghoul Fuel, a pink Halloween coffee edit. Reference supplies mood and palette only. True overhead photograph on a worn black wooden tabletop, a lavender cotton napkin crossing one edge, a small black-and-cream checker cloth beneath the mug. Five selected products: glossy bubblegum-pink 14 oz sculpted ghost ceramic mug with side arms, normal handle, black oval eyes and small smile; pink ceramic TWO-TIER HEART serving stand with 9-inch bottom HEART and 7-inch top HEART, pierced-heart rim holes, one upright GOLD centre rod and GOLD heart-loop handle; 3-inch velvet pumpkins in blush, coral pink, peach and ivory with short gold stems; miniature pink plastic LED tea lights, squat wider-than-tall cylinders with WHITE flame-shaped plastic tips; tiny silver mirrored tile disco spheres with small top hooks. Preserve geometry: each serving plate has TWO rounded lobes, a visible inward notch and a pointed lower tip; they are NOT circles or ovals. Overhead view can show part of lower plate around the smaller top heart. Place stand upper left with its gold handle readable; mug face-up on its side lower right with handle and face visible; four small velvet pumpkins clustered outside the stand, three tea lights and three silver spheres clearly visible. Add purposeful unlinked styling extras: ornate empty silver frame tucked under a lavender napkin corner, black mini cauldron with coffee pods, teaspoon, two star-shaped cookies on a plain pink saucer, small sprig of lavender asters and pink roses along one outer edge. Rich curated layering, gentle edge overlaps, products still recognizable. Neutral daylight, coherent shadows, realistic ceramic/velvet/metal textures, crisp black eyes. No bows, ribbons, hydrangeas, fur or shag, text, logos, price tags, watercolor, screenshot UI, copied artwork or collage border. This is an actual table photograph with personality, not a catalogue grid.
```

### Ghoul Fuel coffee bar: STYLED (prompts/ghoul-fuel-styled.txt)

```text
Create a NEW photorealistic vertical 2:3 STYLED photograph of a finished pink Halloween coffee nook, with no person. Use the basic flatlay as the product-shape reference. Cream shaker cabinetry with aged brass pulls, honey-oak countertop, warm ivory wall, oak floating shelf and warm under-shelf light balanced by neutral daylight from a nearby window. A cream coffee machine sits left; a glossy pink sculpted ghost mug with side arms, a normal handle, black oval eyes and tiny smile sits on a black-and-cream checker coaster in front. At right, a pink ceramic two-tier HEART stand: 9-inch lower heart, 7-inch upper heart, pierced-heart rim holes, gold center rod and gold heart-loop handle. Both plates have two lobes, a notch and pointed tip; orient the points toward camera so neither plate appears circular. Mini blush, coral, peach and ivory velvet pumpkins with short gold stems sit below, three tiny silver tiled disco spheres above. Three short smooth pink plastic LED tea lights with white plastic flame tips around the base; a gentle warm glow, no real flames. Keep all five selected product types recognizable. Add unlinked styling extras: black mini cauldron of coffee pods, pink ribbed canister, syrup bottle with gold pump, teaspoon holder, black urn of pink roses and lavender asters, black vase with dark branches. Above the shelf, an arched black mirror reflects a believable kitchen window; an ornate gold frame holds an original wordless floral ghost painting. Shelf holds stacked cream scalloped saucers, one vintage floral cup and two pink ribbed votives; trailing greenery at the outer edges. A pink-and-black floral cotton towel hangs from the cabinet rail. Rich adult playful maximalism, coherent proportions, layered textures, crisp black edges, polished ceramics and realistic wood. No bows, ribbons, hydrangeas, fur, shag, people, text, logos, UI, watermark or copied artwork.
```

### Ghoul Fuel coffee bar: LIFESTYLE (prompts/ghoul-fuel-lifestyle.txt)

```text
Use the avatar reference image only for the person. Create a NEW photorealistic 2:3 portrait lifestyle photograph of Tommy Kate naturally stirring her fresh coffee at the pink Halloween coffee nook in image 2. Preserve the same cream cabinetry, oak counter, black arched mirror, original floral ghost picture, black urn of pink roses and lavender asters, shelf, black cauldron of coffee pods and five selected products. Widen the framing to include her standing at the LEFT of the coffee nook, the decorated counter on the RIGHT unobstructed, with believable kitchen floor and cabinet proportions. She wears a soft lavender cardigan open over a plain white ribbed tank, relaxed blue jeans and pink house slippers; a small pink claw clip loosely gathers part of her hair. Candid three-quarter side view, concentrating on the mug rather than posing for camera. She holds the ONE glossy pink ghost mug by its handle in her left hand at waist level, its black oval eyes and smile facing camera, and gently stirs with a teaspoon in her right hand. Mug no longer sits on the counter. Anatomically natural hands and physically plausible contact. Keep pink two-tier ceramic HEART plates with pierced-heart rims, GOLD rod and GOLD heart-loop handle on right counter, both heart points visible; little blush/coral/peach/ivory velvet pumpkins below, three silver mini disco balls above, three squat pink LED tea lights with white plastic flame-shaped tips around stand. Clear product visibility and recognizable actual designs. Add a small black-and-cream checker coaster where mug was, a folded lavender tea towel and one pink saucer with two star cookies. Warm under-shelf light balanced with soft window daylight, cozy richly styled real home, crisp facial detail, sharp ceramics, velvet and wood grain. No bows, ribbons, hydrangeas, fur, shag, live candle flames, duplicates of mug, added text, logos, screenshot UI or watermark.
```

## 5. Other prompt files at the pack root (verbatim)

- generation-prompt.txt is identical to prompts/pretty-wicked-styled.txt. coffee-basic-prompt.txt is identical to prompts/ghoul-fuel-basic.txt. coffee-avatar-prompt.txt is identical to prompts/ghoul-fuel-lifestyle.txt. Not repeated.
- coffee-styled-prompt.txt: the stand-only correction used for Ghoul Fuel, kept separately (REFERENCE-MAP.txt).
- avatar-lifestyle-prompt.txt: the earlier Pretty Wicked lifestyle prompt (Tommy Kate placing a bat on the wall). The manifest's lifestyle revision replaced it with the porch-door version in section 4, which Jodie approved.

### coffee-styled-prompt.txt

```text
Edit image 1, the finished pink Halloween coffee nook. Keep the room, camera, lighting, all five products, flowers, black mirror, framed original floral ghost art, coffee machine, styling and colors unchanged. Correct ONLY the two-tier pink ceramic stand using image 2 as its precise shape reference: both plates are HEART SHAPED, each has two lobes, an inward notch and a distinct pointed tip; 9-inch bottom heart, 7-inch top heart, pierced heart rim holes, gold center rod and gold heart handle. Orient both pointed tips toward camera so their actual hearts are visible despite perspective; no round or oval top tier. Keep small mirrored disco balls on top and tiny blush, coral, peach and ivory velvet pumpkins with gold stems below. The three short pink tea lights are LED, with solid white plastic flame-shaped tips and a gentle warm glow, no live flames. Photorealistic 2:3 portrait, sharp realistic ceramic and metal textures. No people, bows, ribbons, hydrangeas, fur, shag, added text or logos.
```

### Removed superseded prompt

The earlier bat-on-the-wall prompt has been removed from the active document. Use the approved porch-door prompt in section 4. Its original text remains in Git history only.

## 6. Sourcing records

Per product: ASIN, name, variant, visual facts, canonical URL, verified time, stock observed, verification method, affiliate URL (null until verified). Canonical product URLs are sourcing references, not verified affiliate links. Brand names appear in the sourcing records and prompts only; never on the page, pins or titles.

| ASIN | Product | Variant | Visual facts | Stock | Verified (UTC) | Affiliate URL |
|---|---|---|---|---|---|---|
| B0DCW42HGK | Cloverhome pink ghost mug | Pink | 14 oz glossy ceramic sculpted smiling ghost; side arms, handle, black oval eyes and small smile. | In Stock | 2026-10-07T16:00:23Z | not yet |
| B0FD1NKLLZ | Paris Hilton two-tier heart serving tray | Pink | Pink ceramic heart plates, pierced-heart rims, gold centre rod and heart loop handle; 9-inch lower and 7-inch upper plates. | In Stock | 2026-10-07T16:01:28Z | not yet |
| B0C49S7XNR | Winlyn mini velvet pumpkins, set of 12 | Blush Pink and White | 3-inch pumpkins; three each blush, coral pink, peach and ivory; short gold stems. | In Stock | 2026-10-07T16:04:47Z | not yet |
| B0B31KBC6L | Homemory pink LED tea lights, pack of 12 | Pink | Smooth pink cylinders with white LED flame tips. | In Stock | 2026-10-07T16:05:15Z | not yet |
| B09MW87J57 | MTLEE silver mini disco balls, pack of 20 | Silver; 2.4, 2, 1.6, 1.2 inch assortment | Silver mirrored tile spheres with hanging hooks; four-size selected assortment. | In Stock | 2026-10-07T16:06:31Z | not yet |
| B09KL2BP6B | Winlyn hot-pink foam pumpkins, set of 7 | Hot Pink | Plain matte ribbed hot-pink pumpkins; dark gold-flecked stems; assorted sizes 2.8–7.3 inches wide and 3–6.5 inches tall. No faces. | In Stock | 2026-10-07T16:07:02Z | not yet |
| B09LLZ4PG5 | Qtisky pink creepy gauze, set of 5 | pink | Five pink open-weave gauze panels, each 72 x 30 inches. | In Stock | 2026-10-07T16:07:35Z | not yet |
| B0FCM9Y4M8 | Glooglitter pink pumpkin lights, two strands | Pink | Two battery-operated 6.5-foot strands, each 20 pink jack-o-lantern bulbs with black faces. | In Stock | 2026-10-07T16:08:04Z | not yet |
| B07TRCJJS3 | Coogam black 3D bat decals, pack of 60 | Black | Black PVC bat silhouettes, four sizes, foldable wings and supplied adhesive strips. | In Stock | 2026-10-07T16:09:02Z | not yet |

Amazon Idea List drafts (checked 2026-10-07T18:21:26.852280+00:00): "Pretty Wicked: Pink Halloween Entryway" (B09KL2BP6B, B09LLZ4PG5, B0FCM9Y4M8, B07TRCJJS3, B0B31KBC6L) and "Ghoul Fuel: Pink Halloween Coffee Bar" (B0DCW42HGK, B0FD1NKLLZ, B0C49S7XNR, B0B31KBC6L, B09MW87J57), both FIVE_PRODUCT_EDITOR_DRAFT_NOT_SUBMITTED. Submission needs action-time confirmation of Amazon's terms. Selection method: Exact-ASIN search in picker; unrelated history not extracted. Broad history read was rejected; narrower exact-product route succeeded. Clipboard check: REJECTED_STALE_LINK: https://link.amazon/B03gIRvVi resolved to B07TRCJJS3 (correct bats; wrong for mug). Never assigned to mug.

## 7. Website record (staged, per look)

Fields: slug, title, date, category, intro, three images each with role (basic, styled, lifestyle) and alt, ideaList (null until submitted), items with name, ASIN, link, variant, note and affiliate_link_verified, status STAGED_NOT_PUBLIC.

- pretty-wicked-entryway: title "Pretty wicked. Pink Halloween Entryway", category home-decor, status STAGED_NOT_PUBLIC. Intro: "A little glow, a few bats, and the kind of extra that makes coming home feel fun. Start with plain hot-pink pumpkins and crisp black bats. Let pink gauze spill over the console edge, weave in the little jack-o-lantern lights and finish with pink LED tea lights. Add flowers, a framed print and a place to drop your keys from pieces you already own."
- ghoul-fuel-coffee-bar: title "Ghoul fuel. Pink Halloween Coffee Bar", category home-decor, status STAGED_NOT_PUBLIC. Intro: "Coffee first. Cute little haunt immediately after. A smiling pink ghost mug is the starting point. Give the heart stand a little collection of blush and ivory velvet pumpkins below and tiny mirror balls above, then tuck pink LED tea lights around the base. A checker coaster, flowers and a little cauldron for coffee pods make it feel like your own coffee corner."

Page notice used in the blog drafts: "AI-generated styling inspiration. Retail products may differ; check the actual listing photographs, contents and measurements. Flowers, furniture, artwork, clothing and other props are styling extras."

## 8. Publication order

Finish affiliate destinations and Amazon list submission, verify the live blog, then publish Pinterest. Instagram follows confirmed Pinterest publication. No old private test may be restored.

Known limits (manifest): Generated styling is inspiration, not an exact product photograph. Only five product types per look are linked; furniture, clothing, flowers and other props are styling extras. Actual affiliate destinations and Amazon list submission require completion before the pack is published.

## 9. Private reference images (kept out of this public repo)

These files live only in Jodie's private pack, Tommy-Kate-Halloween-Cloud-Handoff.zip. None are committed here. They are named so a generator run knows exactly what to attach.

| File in the pack | Role |
|---|---|
| prompts/avatar-reference.png (1280 x 1908) | Tommy Kate identity reference. The ONLY identity source for every LIFESTYLE photograph. Never used for room, outfit or setting. |
| pretty-wicked-entryway/basic.png | Pretty Wicked BASIC flat lay (approved). Attached to the Pretty Wicked STYLED prompt to hold product shapes. |
| pretty-wicked-entryway/styled.png | Pretty Wicked STYLED room vignette (approved). Attached to the Pretty Wicked LIFESTYLE prompt as room and decor reference. |
| pretty-wicked-entryway/lifestyle.png | Pretty Wicked LIFESTYLE photograph (approved porch-door version). |
| pretty-wicked-avatar-lifestyle-v2.png | The manifest's recorded lifestyle revision file (porch viewpoint through the open door), the version Jodie approved ("lifestyle image is much better"). |
| ghoul-fuel-coffee-bar/basic.png | Ghoul Fuel BASIC flat lay (approved). Attached to the Ghoul Fuel STYLED prompt and used as "image 2" shape reference by coffee-styled-prompt.txt. |
| ghoul-fuel-coffee-bar/styled.png | Ghoul Fuel STYLED coffee nook (approved). Attached to the Ghoul Fuel LIFESTYLE prompt ("image 2") as room reference, and "image 1" in coffee-styled-prompt.txt. |
| ghoul-fuel-coffee-bar/lifestyle.png | Ghoul Fuel LIFESTYLE photograph (approved). Filename follows the pack's per-look pattern; UNVERIFIED in this session. |
| pinterest-visual-audit.jpg | Pack's Pinterest visual audit sheet. Reference only. |
| Supplied mood images ("vibe photos", 10 references per sourcing-evidence.json) | Optional mood reference for BASIC only. |
| 3 Pinterest graphics per look (PNG 1000 x 1500), 3 Instagram carousel slides per look (PNG 1080 x 1350) | Finished graphics made after photography; text lives on these only. Individual filenames not reproduced here. |

## 10. Dependency chain for one look (run order)

1. Source five retail products and record each one (section 6 fields), affiliate_url null.
2. BASIC: run the look's BASIC prompt. Attach supplied mood images only if wanted.
3. STYLED: run the look's STYLED prompt with that look's basic.png attached.
4. Fix only if needed: a single-product shape correction is an edit pass on styled.png with the shape reference attached (coffee-styled-prompt.txt is the worked example).
5. LIFESTYLE: run the look's LIFESTYLE prompt with avatar-reference.png (identity only) and that look's styled.png (room and decor only). Different camera angle, framing or viewpoint from STYLED; Tommy Kate doing something natural. Never paste her into the styled frame.
6. Make the 3 Pinterest graphics and 3 carousel slides from the finished photographs; text goes on those, never in the photographs.
7. Fill the website record (section 7) with status STAGED_NOT_PUBLIC.
8. Publish in the section 8 order.

## 11. Generation status (7 Oct 2026)

WYS image generation is PAUSED. Recorded in the repo's AGENTS.md on branch lifestyle-wys-rebuild-2026-10-07 (commit 4291e1b, 7 Oct 2026): "Until that consolidation is complete and its source coverage is checked, WYS image generation remains PAUSED." The old Legally Blonde / Brand Closet generation recipes, two-image recipes, generated-text instructions and fixed Seedream/Gemini fallback routing are superseded for WYS and must not be run.

Image provider, model and settings: NOT RECORDED in the pack (section 1). Do not assume one. The only generator used on 7 Oct after this pack arrived was Higgsfield Seedream 4.5 (2 credits, 2 images); both failed the pack standard and are not used.

## 12. Source coverage of this document

Source export: Claude Project document claude/WYS_REFERENCE_PACK_2026-10-07.md. The current approved prompts remain unchanged; the superseded bat-placement prompt was removed during consolidation. That document was checked word for word on 7 Oct 2026 against the pack's pack-manifest.json, prompts/REFERENCE-MAP.txt and all 12 prompt files.

Pack files whose full text is NOT reproduced here because the original zip was not reachable in this session: START-HERE.txt, pack-manifest.json (full), sourcing-evidence.json (full), pretty-wicked-entryway/blog-source-staged.json and the matching Ghoul Fuel record (full), the two blog drafts, and the text on the Pinterest graphics and carousel slides. Their recorded values used above are in sections 1, 6 and 7.

## 13. Sole WYS authority and execution status

This file is the single active WYS operating document for founder sourcing, imagery, content preparation, website handoff and workflow design. Read it in full before executing a WYS task. The six prompts in section 4 and the stand correction in section 5 are the current worked examples. The superseded bat-placement prompt is not an executable recipe. Older two-image instructions, generated lettering inside photographs, fixed generator routing and old website writers cannot be revived from Git history, receipts, logs, customer PDFs or scheduled-task snapshots.

The approved examples establish styling and the three-image dependency chain. They do not identify a generator. Provider, model, generation parameters beyond the recorded output, current account capability, budget, live affiliate destinations and publication remain unverified until separately recorded. WYS generation remains PAUSED. Never replace missing configuration with a remembered or older default, use an arbitrary test image as a reference, or spend credits to discover the configuration. Continue independent documentation and code work.

General TDIE rules still govern other systems, including SOP-15 and SOP-16. For WYS the specific approved prompt wins over generic visual defaults: do not insert a mandatory tumbler, change the approved coffee cabinetry, force a generic identity preamble, hide the face by default, or convert this pack into the old two-image format. The Pretty Wicked lifestyle prompt expressly includes one partly visible trick-or-treater; its prohibition on additional people does not remove that approved foreground figure. Wardrobe varies by the exact prompt: Pretty Wicked uses pink cardigan and black jeans; Ghoul Fuel uses lavender cardigan, blue jeans and pink slippers.

Source coverage: sections 1–8 preserve the submitted current reference and approved prompts, with the superseded bat-placement prompt removed; sections 9–12 preserve the additional repo reference details already present. Operating rules below consolidate the founder safeguards, customer setup/state/recovery requirements and website migration requirements. They are instructions, not evidence that their execution or the end-to-end customer product has passed. The original zip and private images have not been independently inspected in this consolidation. Unknowns remain unknown.

## 14. Operators, accounts and founder boundaries

Maintain exactly one writer for each external action. Codex owns repository implementation and /lifestyle publication. Claude prepares sourcing, prompts and staged content; it does not independently upload old-style website files or publish the pages. Use an available supported connector for its exact authorized operation; check capability and readback before claiming it can perform that operation. An installed app does not prove access to the relevant account, board, media field, AI label, schedule, cancellation or live deletion.

Founder Amazon destination of record is https://www.amazon.com/shop/thedigitalincomeedit with tracking tag jodiedeo0c-20. Confirm live destinations before use. Reuse an existing list for the same look rather than creating a duplicate. Never use the retired influencer-adc3fcaa address. Canonical /dp/ASIN URLs are sourcing records only. Do not substitute the storefront home or an unrelated affiliate link for a pending per-look destination just to finish a run.

Founder Pinterest scheduling uses the authorized Metricool route, with recorded account identifier 7142540 and America/New_York timezone. Read the active connector schema: field names and live permissions are not established by this document. Read schedules before writing and read every result back afterward. Do not switch to native Pinterest scheduling or a different board because Metricool rejects an operation. Current founder policy prohibits Pinterest-browser schedule/edit/delete/verification; public-board checks are a separate read-only capability. Missing required section or AI-label support is a visible blocked step, not a successful publication.

Recorded founder boards: outfit looks use Legally Blonde Outfits | Pink Amazon Fashion; home/dorm/car/desk/book looks use Pink Home, Dorm and Car Finds | Amazon. Brand Closet uses Pink Outfit of the Day | Amazon Fashion Finds, numeric ID 1122311238331286804, recorded public on 4 October. Recheck current public visibility and account access. TK Outfits stays private and is never used or changed. Do not infer other board IDs from names or substitute them.

The affiliate Instagram account is @itstommykate. Confirm the actual posting identity in the composer or owning service before sharing. @the.faceless.homestead.mama belongs to the separate TDIE/calendar system. Instagram captions and comments use a verbal link-in-bio CTA, no raw links; approved Story link stickers are a separate operation. Do not change account type, linked Facebook Page, auto-post settings or credentials to repair a missing capability without existing authority. Historical Meta access reports are not current capability checks.

MailerLite operations use Claude's MailerLite connector only, never a browser. This workflow does not create a new welcome automation or send campaigns as a side effect of the website rebuild. Preserve founder publishing/spending restrictions and the customer-product release HOLD. A planned launch date is not clearance. Do not publish a WYS product promotion, checkout, customer delivery or release merely because a staged affiliate look is prepared.

## 15. Intake and sourcing procedure

1. Read the current state and unfinished checkpoint first. Resume completed products, assets and verified destinations; do not rebuild from zero. Assign a stable LOOK_ID and source record. Intake records the theme, date/season, category, authorized mood/reference inputs, desired channel set, destination path and product requirements. These two worked examples contain five product types per look.
2. Use only authorized sources and assets. Read Amazon through the supported authorized account route; no background scraping, broad history extraction or paid scraper substitution. Normal browsing does not by itself establish permission for commercial automation. Do not probe unrelated account history.
3. Match the exact ASIN and selected variant. Record shape, color, materials, measurements and pack count from the listing, plus canonical URL, observed stock, verification method and timestamp. Stock in the table is a historical observation, not a current promise. Recheck changed or stale listings before publication. If an item is unavailable, record the failure; any replacement must update the source record and all affected imagery/copy before it is used.
4. For affiliate capture, confirm the authorized Associates/Influencer identity and SiteStripe/account route. Capture the actual link; resolve it and match the destination ASIN and selected variant plus the expected tracking attribution. A copied link can be stale even when it has the right short-link domain. Leave affiliate_url null and affiliate_link_verified false until checked.
5. Build or reuse the exact look's Idea List using exact-ASIN selection. Confirm its product membership and live URL after submission. Do not treat a five-product editor draft as submitted. Where the service requires action-time terms confirmation, leave submission pending until that requirement is satisfied.
6. Reference product images remain private source material. Do not republish retailer images, paste catalog cutouts into the finished photo, or publish paid member screenshots. Use named styling extras only as extras, never silently add them to the shopping list.
7. Save each verified product and destination immediately. Do not wait until the end of a long run to persist links. Check for repeated hero items in the founder history; avoid repeats within 30 days unless explicitly selected for reuse. Source quality preferences from the earlier founder operation (clear photographs, in-stock listings, Prime when available, normally at least 4 stars/100 ratings) are selection preferences, not evidence or mandatory properties of the approved pack's existing products.

## 16. Generation preflight, dependency chain and acceptance

Before a generation write, the saved configuration must identify provider, exact model/version, supported reference mechanism, output settings, account, cost per attempt, authorized budget and source of authorization. Record prompt version/hash, actual attachments and their roles, request/job ID, timestamp, actual output metadata and debit. No silent provider/model switch, resolution change, subscription purchase or unlimited reruns. Budget includes corrections, failed submissions and uncertain outcomes. Reserve expected cost before submission; reconcile uncertain jobs before retrying. Stop the affected image when configuration, references or budget is missing.

The pack's PNG 1024x1536 output is verified only as a recorded asset format; it does not prove which generation UI setting produced it. Retain the correct source output and make separately named derived graphics. Do not stretch, repaint or overwrite the source photograph to fit social dimensions.

Execute BASIC → inspect → STYLED with matching accepted BASIC → inspect/correct → LIFESTYLE with identity plus matching accepted STYLED → inspect. Verify reference attachments actually reached the selected tool before submission. One look's room reference cannot be used for another look. Attach no reference that changes Tommy Kate's identity. Approved example prompts are verbatim; new looks require prompts derived from their actual source products and scene, with all changes recorded.

Acceptance requires all three roles, no photographic text/logos/watermarks/collages, visible recognizable product types, correct distinguishing geometry/color and physically plausible scale/light/contact. BASIC is truly overhead on a real surface; STYLED has no person; LIFESTYLE shows Tommy Kate performing an appropriate action with a genuinely different viewpoint/framing from STYLED. Review the actual image, not only the prompt or tool response. Check hands, duplicate objects, product placement and room continuity. Inspect full size and phone/feed size. Reject missing products, wrong stand geometry, altered pumpkin faces, hidden reference-dependent shapes, identity drift, or avatar insertion into the styled frame.

Corrections must identify the specific defect and preserve accepted elements. The Ghoul Fuel correction is the worked example. No new open-ended correction allowance is implied by older recipes. Record each attempt against the current budget and stop at its authorized limit. A failing image never ships because time or corrections ran out. Both failed 7 October test images remain excluded.

## 17. Graphics, copy and disclosure

Create exactly three separate Pinterest graphics per look at 1000x1500 and three separate Instagram carousel slides at 1080x1350, from the accepted photographs. Keep role → photograph → graphic/slide associations explicit in state. Photography carries no lettering; add all graphic typography deterministically after generation and inspect every word at phone size. Use the TDIE brand: loud confident pink with a polished luxury feel, Newsreader SemiBold upright for headlines and Inter for other type. Preserve legibility, contrast, safe margins and product visibility. Never render generated text into the source photo.

Founder copy conventions: overlay normally 3–5 words, title 60–100 characters, description 450–500 characters including disclosure, alt text 150–200 characters describing the actual image. These are founder editorial targets, not asserted current platform limits; validate current fields before posting. No prices, earnings promises, em dashes, copied brand/logo cues or unsupported product/performance claims. Brand names in the approved sourcing/prompts do not belong in public titles, pages or pins. Write specific plain copy in the founder's voice. Do not claim generated photos are exact retailer product photographs.

Founder Amazon pin disclosure: "#ad As an Amazon Influencer I earn from qualifying purchases." Customer disclosure must match the customer's actual account/path and current applicable requirements; never copy the founder's account status. Required AI labels and affiliate disclosures must be supported and verified on the exact publication route. Lack of a field does not waive a requirement.

Brand Closet credit remains founder copy: "Outfit inspiration from The Brand Closet™: https://www.skool.com/the-brand-closet/about?ref=97643519c9b448d0a683ab33b6cc68ce" before the Amazon disclosure, within the complete description target. Customer exports use the customer's authorized attribution/destination, not the founder's private configuration.

## 18. Website implementation and full /lifestyle replacement

Codex must implement the new system for the hub, category pages, individual looks and direct legacy URLs. No old two-image generator/template may continue to display old content or recreate it after cutover. Use one reusable template and explicit records with the three roles. Extend section 7 records with a schema version, stable LOOK_ID, role-specific asset IDs/checksums, staging status, source version and verification evidence as needed; adapters must not silently declare an old two-image record complete.

Keep new records STAGED_NOT_PUBLIC while image files, destination verification or approval are missing. Do not manufacture a third image, hotlink private pack assets, publish those private references, replace them with stock imagery or expose a half-migrated look as complete. Public media requires separate authorization. The pack's approved styling status does not make its private files public.

Before cutover inventory all existing look JSON, image references, routes, feeds, sitemap entries, internal links and old writer paths. Preserve rollback in Git. Retire all old look displays; choose explicit tested redirects where a genuine new equivalent exists, otherwise a deliberate retired route. No redirect may lead to a broken product or old template. Separate verified reusable product data from rejected imagery. The reported Pink Angel clutch link is a known issue requiring verification; do not publish it as a verified clutch destination without a new check.

The public deployment is Cloudflare worker tdie-site from cloudflare-migration. main is not proof of deployment; Vercel is retired. Incorporate the parked rebuild only after review against this document. Stop competing /lifestyle writers before cutover. Validate schemas, required three-role images, alt text, links, affiliate verification and stage/public gating. Run the appropriate build and route checks, inspect complete desktop and mobile pages at 320px/390px, then independently inspect the actual custom-domain deployment. No claim of completion from a build alone. Keep h1 30–36px mobile, h2 26–30px, wrapping labels, 48px primary actions and zero overflow. Preserve the Newsreader/Inter brand and site signup integrations without reintroducing old visual layouts.

Show section 7's exact AI styling notice and the appropriate affiliate disclosure. Styling extras stay separate from shoppable items. Make product and Idea List links understandable and accessible; never present an unverified canonical URL as an affiliate destination. Product-release promotions remain held. This documentation change does not itself rebuild or deploy /lifestyle.

## 19. Publication and scheduling

Use section 8's order: verified affiliate destinations and submitted list → Codex implementation and independent live blog verification → Pinterest publication → Instagram after confirmed Pinterest publication. Scheduled Pinterest posts do not count as published. Prepare drafts independently, but do not schedule downstream publication as if an upstream dependency already passed. Record the exact approved assets, copy, destination, board/account, timezone and time for each write.

The reference pack specifies three graphics, but does NOT specify a three-pin timetable. Do not fill the third slot by inventing a default or applying the deleted two-pin timetable. Save an authorized three-role posting plan before scheduling; preserve already-confirmed schedules and resolve collisions against live state. Founder related pins remain separated rather than all posted the same day; respect the saved pacing policy and a maximum 14-day forward planning window unless the founder changes it. Dates, timezone and policy revision belong in state, not inferred from machine local time.

Read existing schedules/publications first. Write one exact payload once, persist its external ID/UUID immediately, and read it back through the owning service. Compare time/timezone, actual board/account, media, title, description, alt, destination, disclosure and required labels. A successful API response is only submitted evidence; scheduled, published and verified are separate states. Instagram uses three finished carousel slides; no old two-photo carousel ordering rule survives. Verify account, asset order, caption, labels and live result. Missing Story support leaves the Story pending and does not cause an unauthorized account-setting change.

## 20. State schema and durable records

Use one durable production truth: an authorized spreadsheet/database or equivalent local JSON store. Markdown logs and Command Centre tabs are views, not independent sources of truth. Founder existing LB_PIN_LOG and Brand Closet history must be reconciled/imported rather than discarded; preserve completed links and external IDs. Read pending pull requests before rebuilding a view so a refresh cannot erase them.

Required tables/collections: AUTOMATION_POLICY, CAPABILITIES, LOOKS, PRODUCTS, IMAGES, PINS, BLOG, INSTAGRAM, LESSONS, RUNS, ERRORS. Stable keys include LOOK_ID, IMAGE_ID, PIN_ID, ASIN, lesson ID, run ID, external post ID/UUID and policy revision. Store timestamps in ISO form with schedule timezone. Record source/asset hashes and payload fingerprint so changed copy, media, time or destination invalidates prior verification/approval.

LOOKS: theme, date, season, category, source, destination, status, next_action, owner, policy_version. PRODUCTS: complete section 6 fields plus affiliate verification evidence. IMAGES: role, prompt version/hash, references, provider/model/configuration, request ID, cost, private/public asset location, dimensions/checksum, QA outcome/reason. PINS/INSTAGRAM: exact copy/alt/disclosure, media IDs, account/board, intended timezone/time, external ID, payload fingerprint, approval evidence, submitted/readback/live timestamps, status. BLOG: section 7 data, schema version, staged/public status, build/deployment ID, public URL and live audit. RUNS: claim/heartbeat/checkpoint, write intents, reservations/debits, start/end, completion evidence. ERRORS: affected ID, operation, exact error, attempts, outcome certainty and next action.

Operational statuses include intake_needed, sourcing, ready, building, built, queued, customer_review_required, awaiting_approval, customer_scheduling_required, scheduled, customer_scheduled, published, verified, missed, write_outcome_unknown, pull_requested, pulled, pull_failed, failed and dropped. STAGED_NOT_PUBLIC is the website publication gate, not an accidental substitute for the operational status. Distinguish omitted steps from completed ones. Persist each actual result immediately and verify the state write.

## 21. Permissions, budgets, claims and recovery

Save an AUTOMATION_POLICY before unattended operation. It records who authorized what and when, selected mode, accounts, boards/destinations, source/asset rights, provider/model/settings, per-run and period budget, cadence, timezone, channel scope, approval boundaries, expiration/revocation and pause controls. AUTOMATIC mode executes within that policy; REVIEW_FIRST requires approval of the exact asset/copy/destination/schedule fingerprint. Changed payloads invalidate the approval. Account consent and platform capability are separately checked. Automation does not invent a spending allowance.

Acquire a run claim before side effects. Use an atomic conditional/versioned write where available, record owner and heartbeat, and release after checkpointing on every exit. A lock's age alone does not prove its holder stopped. Reconcile holder status and uncertain external writes before reclaiming. Keep a pending write_intent with stable write_attempt_id, exact payload fingerprint and expected cost before submitting. If a response is lost, mark write_outcome_unknown, inspect the external service and match payload/IDs before any retry. Never create a second post/list/job merely because the first response was missing.

Resume only the failed or unfinished step. Reuse accepted images, sourced products, verified links and committed state. Complete independent authorized work while a dependency is blocked; keep a precise checkpoint including the next operation and unresolved evidence. Retry transient failures only within the recorded policy, with bounded attempts. Never silently change tools, accounts, boards, prompts, rights, cost or publication route. Save a visible failure when all supported routes are exhausted.

Pull requests are durable state. Cancellation of a scheduled external post and removal of a live platform post are distinct operations. Use the exact supported authorized capability, verify the owning service result and record pulled/pull_failed. Deleting a Metricool record is not proof that a live Pinterest pin disappeared. Do not erase historical evidence or unrelated live posts during documentation cleanup.

## 22. Customer setup and manual/mixed equivalents

This founder reference is NOT a customer delivery package. Before release derive a sanitized buyer edition from this one authority and validate every path. Never copy founder task triggers, account identifiers, board IDs, tracking tags, private lesson URLs, Command Centre IDs/logs, private references or paid member materials into customer output. Customer state and authorization belong to the customer.

Setup captures: actual Amazon account path (Influencer list, Associates-only or owned site), owned destinations and verified links, disclosure, persona/no-persona choice, authorized reference assets, product categories, selected channels, timezone/cadence, provider/model and budget, chosen automation/review mode, connected capabilities and durable state location. Produce the customer's recipe and schedule as parameterized runtime configuration pointing to this workflow, not another freestanding competing instruction manual. Never claim all buyers have the same signed-in accounts or browser runtime.

Time-saving, credit-saving/manual and mixed paths complete the same steps and have the same acceptance criteria. Manual equivalents: buyer supplies products/listing facts and source rights; captures/verifies their own links/list in the native service; generates using their selected provider and correct role references; prepares graphics with deterministic type; creates their own site page or selected destination; uses native publishing/scheduling where permitted; reads back actual results and records state. Mixed mode assigns each operation to either the buyer or agent explicitly. Planning/copy can use the buyer's chosen capable chat tool. Do not require a subscription, paid scraper, persona service or automation tool solely because the founder used one historically.

No-persona buyers must receive a deliberately validated no-persona variant of the third image, not an undisclosed substitution or a claim that the founder's Tommy Kate pack demonstrates that path. Persona buyers need authorized identity inputs. Associates-only buyers do not get a fictitious Influencer Idea List. Own-site buyers need a real authorized page and correct destination verification. Where an automatic capability is missing, block and name that step; do not quietly turn the promised automatic path into customer homework. Manual mode is a buyer choice, not proof that automatic mode works.

## 23. Scheduled jobs and Brand Closet intake

The reusable customer design has three jobs: weekly themed-look build, optional Outfit of the Day intake/build, and daily reconciliation/recovery/pull handling. Save them paused first. Enable only after the first real publication and a separate scheduled execution have been independently verified for the chosen customer path. Manual customers receive the same operations as a checklist, without fictitious trigger IDs. Task payloads identify this canonical file, its reviewed version/hash, the saved policy and state; they must not embed stale generation defaults.

Founder known task times from the prior active override are historical configuration to reconcile before editing runtime: weekly build Saturday 1:05pm Eastern; Brand Closet Sunday–Friday 9:20pm Eastern. The Brand Closet overnight checkpoint stops new items at 6:45am, saves/releases by 7:30am Eastern. Continuation must read the checkpoint and existing schedule, never start the outfit over. A previously saved task or a clock time is not evidence that its embedded prompt now matches this document. Runtime task/skill/project copies must be inspected and updated by an operator with that access before generation resumes.

Brand Closet: read the authorized Outfit of the Day Closet lesson source, state first, latest 14 days oldest unfinished first. Finish partly sourced/built lessons using existing work before starting new ones, ordinarily up to two per run. Mark older unstarted lessons missed/skipped with a reason, rather than silently rescheduling a logged lesson. Paid member photos/prompts are private references only; never publish them or another creator's affiliate links. Source the buyer/founder's own matching products and destinations. Close unrelated source tabs after intake. If no unprocessed lessons or unfinished work exist, end without opening generation or publishing tools. The new three-role image workflow applies to WYS outputs; the removed Brand Closet two-image generator defaults do not.

## 24. Seasonal planning and surrounding integrations

Carry the founder's source calendar forward without its old image/cadence rules: Halloween through 23 October 2026; pink fall 24 October–6 November; Thanksgiving/Friendsgiving 7–19 November; Christmas/gift guides 20 November–18 December; New Year's Eve 19–30 December; winter 31 December–24 January 2027; Valentine/Galentine 25 January–7 February; transition to spring 8 February–6 March; Easter/pink-and-green seasonal looks 7–21 March; spring 22–31 March. Do not schedule past the recorded 31 March end without renewal. Dress evergreen looks for the current season; include at least one a week and normally two where the saved plan allows. Use the separate current lifestyle idea bank as product ideas only, never as a competing image recipe.

Pink Finds signup, membership/Brand Closet cards and Friday newsletter are surrounding integrations, not permission to release WYS. Preserve their verified account/source boundaries while rebuilding the page styling. Any applicable Weekend Ecosystem mention is a soft, authorized next step, not an invented deliverable or activation. Newsletter links go to independently verified owned lifestyle pages, not unverified affiliate destinations. Email send/test/schedule operations require their existing authority and owning-service readback. Do not represent historical subscriber counts, campaign status, price, plan capacity or tier facts as current without checking.

## 25. Validation, release gate and cleanup completion

Documentation checks: six current approved prompts and REFERENCE-MAP match the supplied export word for word; active stand correction matches; three role/reference chains are present; no executable legacy generator/default or two-image recipe remains; all active WYS references point here; old packaged instructions/compiled copies cannot recreate the old recipes. This is a source check, not an image, affiliate, live publication or automation pass.

Image/website checks: inspect actual current private inputs and approved outputs through authorized access; verify links/list; schema and route tests; complete desktop/mobile and actual deployment audits; downstream publication readback. Never restore failed private tests, label a staged page live, or distribute private pack images.

Customer release requires evidence for all six buyer paths: Influencer+persona, Associates-only+no persona, own site, Brand Closet member, manual and mixed. For each verify setup, sourcing/rights, correct destination/disclosure, actual three-image variant, graphics/copy, public board/account, duplicate prevention/locks, budget behavior, uncertain-write recovery, missed-run reconciliation, pull/cancel behavior, first real publication and separate scheduled run. Validate rendered guides, no founder/private leakage, and every manual equivalent. Simulations and documentation edits do not pass live tests. Do not promise guaranteed sales, earnings, universal automation or Pinterest distribution. The founder's explicit release hold remains until she changes it.

Old instructions belong only to Git history for rollback/evidence, not live instruction files. Delete superseded WYS recipes, task prompt files, architecture/release duplicates and old instruction kit/PDF/ZIP builds. Update shared entrypoints to this file without deleting unrelated TDIE systems, production logs, source product data, approved private assets or published posts. Remove obsolete code that regenerates deleted instruction kits. Runtime Claude Project documents, skills and scheduled tasks are separate copies: repository cleanup alone does not prove they were removed. Keep generation paused until their source coverage and migration are checked. Record the exact remaining inaccessible surface rather than claiming global deletion.

## 26. Product campaign facts and release hold

Updated 4 Oct 2026. Read current canon and verify live checkout/listing state before using prices, links, capabilities or release claims in customer-facing material.

## Release hold

Release is on hold. Publish nothing for this product. Dates below are planning facts only and do not authorize posting, launch, checkout activation, delivery release or affiliate activation.

## Campaign structure

- Name The While-You-Sleep Storefront™ in the first Mon 5 Oct announcement. Do not run an unnamed mystery campaign.
- Mon 5 Oct through Thu 8 Oct before 4:00 pm Eastern is the prelaunch desire/demo period.
- WYS prelaunch promotion repeatedly reminds the audience: **Standard presale opens Thu 8 Oct at 4:00 pm Eastern; 20 Standard presale spots.**
- Demonstrations should create desire by showing real verified outputs and workflow behavior, not unsupported promises.

## Pricing and scarcity

- Standard member presale: Thu 8 Oct 4:00 pm to Sat 10 Oct 2:00 pm Eastern. $17. Exactly 20 Standard presale spots.
- Standard spots remaining = 20 minus actual Standard presale purchases. Do not count Premium purchases against this cap.
- No Beacons counter or sales limit (Jodie, 4 Oct 2026). Jodie keeps the Standard spots count herself and updates it by hand in Skool. Never set a Beacons sales limit for this, and never post a spots number she hasn't given.
- Premium member offer: $10 via TDIEPREMIUM in The Premium Vault only. Uncapped.
- Premium purchases may be used in truthful, clearly labeled total-buyer/social-proof counts. They may never be used to create or reduce a Standard spots-remaining number.
- No public presale.
- Public launch: Sat 10 Oct 2:00 pm through Mon 12 Oct 11:59 pm Eastern at $27 against regular $37.
- Regular price: Tue 13 Oct onward, $37. Launch member pricing/code off.
- Member affiliate program: 40% through Beacons no earlier than public launch Sat 10 Oct 2:00 pm. Never state the rate on Facebook, Instagram or the sales page.

## Claims

- No sales, commission or income claims about this storefront.
- Do not claim automatic sourcing, silent fully automatic publishing, or any capability not supported by current live test/release evidence.
- Historical audits are evidence of their date only. Current release status must be reverified.
- Sep 28 founder requirement remains: every automated or credit-heavy customer-guide step must offer both a lower-cost Claude/ChatGPT path and a manual alternative. This requirement does not itself prove the current guide implements it.

## Live-state boundary

Product IDs, checkout links, Vault lessons, affiliate setup, sales-page copy, delivery behavior and scheduled tasks must be checked live before publication or activation. The dated 27 Sep project reference and Sep 30 audits are historical, not current authority.

## 27. Answer persistence and category mini tests (9 October repair)

Founder instruction, 9 October: the questionnaire must actually govern every downstream prompt; the operator runs its own image checks; unnecessary Higgsfield spending is rejected; run a mini test for EVERY category before scaling. This is a repair requirement, not a report that the tests passed. The original completed founder questionnaire has not been recovered in this repair. Incomplete observed settings and isolated no-persona buyer fixtures are not her answers.

Persist each answer when received, not after the interview ends. Preserve the exact value, original source/message evidence and timestamp, all custom question keys, customer identity, revision and prior-answer history. Read the durable record back. Resume the same profile after interruptions. Never overwrite it with a simulated buyer profile, remembered brand context, a suggested default, or a summary labelled as a confirmed answer. Missing, unknown or conflicting answers remain incomplete. Do not require the founder to complete the questionnaire again to conceal a failed handoff. Her later 9 October instruction expressly authorizes focused replacement questions. Record new answers as a new revision; preserve the original questionnaire as unrecovered. Carry forward source-backed direct instructions without fabricating original answer timestamps.

Before each sourcing, BASIC, STYLED, LIFESTYLE, graphics, blog, Pinterest, Instagram and reconciliation operation, reload that profile and bind its revision/hash and this master hash to the exact step input. Record how each answer is applied or why it is genuinely inapplicable. A profile change invalidates earlier prepared inputs and mini-test acceptance. No generation or paid operation proceeds with an incomplete profile or missing answer-application evidence. Input preparation is not proof the image provider accepted it; retain the actual tool request, attachments, result and visual inspection separately.

Mechanical implementation: `ops/wys-runtime/intake.py` provides the ordered, resumable interview and immediately saves each exact answer with component provenance. Business direction/audience precede category curation and price questions. Operator capability checks are not customer preference questions. A partially completed interview cannot pass input preparation. `ops/wys-runtime/profile.py` persists and reads back private answers, prepares step-bound inputs and verifies field coverage. `mini_test.py` checks category coverage and acceptance records. `spend.py` reserves attempts/cost before submission and preserves failed/uncertain attempts. These are local operator components, not installed cloud integrations. A caller that bypasses them is not protected by them. Scheduled agents, project copies and connected production adapters must be independently inspected, wired to these checks and tested before claiming runtime enforcement. Never upload customer/founder answers, identity images, provider credentials or private test assets to this public repository.

### Category-specific roles, with later clothing directions preserved

Source: founder's complete October 8 handoff, SHA256 `00b1b279c9b420987a48744823830976f760b512562c4006ebc5759fe996d9e6`, READ-THIS-PROMPT.txt and recovered-spec/GOVERNING-SPEC.md. Later direct founder instructions override conflicting generic descriptions. Sections 2–10 are worked HOME-DECOR examples; they must not redefine clothing STYLED as an installed room vignette.

Clothing BASIC: beautiful photographic arrangement of only selected shoppable pieces, naturally flat or aesthetically folded. Clothing STYLED: a different person-free outfit flatlay with independent AS-IF-WORN volume, hollow garment openings and grounded fabric, plus relevant personal extras. No connected invisible wearer, mannequin, hanging wardrobe, office desk, default bed or generic repeated prop kit. The distinction must remain visible with background and props ignored. Clothing LIFESTYLE: the authorized persona actually wearing the selected outfit during a plausible activity, with a different composition and adequate product visibility. Do not write identity features in words.

The designated finished clothing BASIC needs its recorded readable label: large hot-pink brush script plus a dark uppercase sans subtitle in the accepted founder manual direction. Do not force the historical "off duty" label onto new looks. Clean-photo plus deterministic typography is allowed only when the operator delivers the complete finished labelled asset. STYLED/LIFESTYLE remain unlabelled except explicitly scoped physical product/prop inscriptions. Do not use extra paid generation just to add lettering.

Objects: BASIC is the category-appropriate overhead contextual product arrangement; STYLED is intended use/installation without a person; LIFESTYLE is meaningful interaction in a separately composed scene. Accessories and jewelry need their own scale, closures, quantities and wearing/use checks; beauty and perfume need exact product/packaging fidelity and no invented effect, scent or performance claims; car needs correct fit/use, support and plausible placement; books need exact edition/product facts with no invented cover/lettering. Gifts, holidays and mixed edits follow the physical products, not a blanket costume or room rule. These are acceptance requirements to test, not verified successful recipes.

### One complete representative look per category, before a batch

Discover ALL categories from the actual selected category source. Current main `src/data/lifestyle.js` registers clothing, accessories, jewelry, beauty, perfume, home-decor, dorm, car, books and gifts. A changed inventory invalidates the coverage record; new categories cannot inherit another category's pass. Also test each selected intake route (detailed mock list, vibe reference, quick start), persona/no-persona and relevant buyer execution paths. An absent third-image variant is BLOCKED, never silently substituted.

For each category: one look, actual sourced product/variant records and private reference images, saved confirmed preferences, complete measured prompts below 3,000 characters, BASIC → inspected STYLED → inspected LIFESTYLE with the right dependencies, final label/graphics, copy/disclosure/destination checks, and a resume test. Inspect full-size and phone-size outputs personally; record concrete defects and acceptance evidence. Do not ask Jodie to run generations as the operator's QA. Preserve failures. One approved home-decor or cardigan example is not an all-category pass. Static prompt/length checks never count as visual acceptance. A miniature visual test is not a live-publication or scheduled-execution pass.

The current founder mini-test route is native in-chat image generation per her direct instruction, not Higgsfield. Its availability, actual reference inputs and output must be checked; this does not select every buyer's provider or assert cost/plan capability. No Higgsfield spending is authorized for this repair. Do not invent replacement preferences. The founder has now explicitly authorized new questions: save her new answers and continue the bounded tests without waiting indefinitely for the old questionnaire. Private visual pilots require their visual inputs; missing publishing or scheduling settings only block the operations that need them. They do not authorize publication. Ordinary generation pause, release hold and publishing boundaries remain in effect outside the explicitly requested bounded mini tests.

Save a finite attempt allowance before each pilot. Generate one role at a time and inspect it before the next role. Corrections count as attempts; failed and uncertain jobs count against reserved spend. Missing outcome blocks a retry until reconciled. Reuse accepted assets. No automatic provider/model switch, open-ended reroll or production-size batch. Only that category with matching profile/master/product versions and actual recorded mini-test acceptance may proceed to scaling within the authorized budget; other categories remain blocked. Operational publication, recurring execution and customer release still require their separate evidence gates.
