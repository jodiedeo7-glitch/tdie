# WYS reference pack: Tommy Kate Halloween (approved styling examples, 7 Oct 2026)

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

### avatar-lifestyle-prompt.txt (superseded by the porch-door lifestyle)

```text
Use the avatar reference image only for the person. Use the entryway reference only for the room, selected decor and colour palette. Create a NEW photorealistic vertical 2:3 LIFESTYLE photograph of Tommy Kate actively decorating that entryway; not a person-free scene or a posed portrait.
Preserve the black console, oval black mirror, warm ivory wall, pink open-weave gauze, three plain matte hot-pink ribbed pumpkins with dark gold-flecked stems, small pink jack-o-lantern string lights with crisp black faces, pink miniature plastic LED tea lights with white flame tips, black PVC bat silhouettes, black urn of pink roses and lavender asters, ghost painting, checker cotton blanket basket and silver lantern. Keep the plain large pumpkins without faces; the faces are on small light bulbs. Props and room remain believable at human scale.
Tommy Kate stands to the LEFT of the console in a three-quarter side view, pressing one black PVC bat onto the ivory wall at comfortable shoulder height. Her right hand makes light fingertip contact with the bat centre; her left holds one spare bat at waist level. Natural slightly bent elbow, relaxed shoulders, attention on what she is placing, no looking at the camera. Make hands anatomically plausible and wings visibly supported against the wall. Her body does not block the pumpkin cluster or pink lights. Camera steps back enough to show her from head to shoes plus the complete console, with a clear walking path.
Scene-appropriate attire: open cropped bubblegum-pink knit cardigan, white ribbed tank, medium-blue straight wide-leg jeans with plain pockets, pink low-top sneakers with plain dark side panels and gum soles, small gold stud earrings. No bag or tumbler because she is decorating at home; no costume. Her hair is loosely clipped back with a simple pink claw clip. Do not add bows or ribbons to her clothing or decor. Do not carry over the outside garden, dog, gate or text from the avatar reference. Use the avatar reference as identity authority without inventing facial traits.
Soft neutral window fill from the doorway at left, cozy warm local lights, real skin and knit textures, crisp black bat silhouettes and true saturated hot-pink pumpkins. Rich collected cottage atmosphere, engaging candid action, no pink colour wash, shag/fur, hydrangeas, logos, text overlays, watermark, extra people or copied layout. Preserve the selected decor's identity while reframing the scene naturally around the action.
```

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

Copied from: Claude Project document claude/WYS_REFERENCE_PACK_2026-10-07.md (sections 1 to 8, unchanged). That document was checked word for word on 7 Oct 2026 against the pack's pack-manifest.json, prompts/REFERENCE-MAP.txt and all 12 prompt files.

Pack files whose full text is NOT reproduced here because the original zip was not reachable in this session: START-HERE.txt, pack-manifest.json (full), sourcing-evidence.json (full), pretty-wicked-entryway/blog-source-staged.json and the matching Ghoul Fuel record (full), the two blog drafts, and the text on the Pinterest graphics and carousel slides. Their recorded values used above are in sections 1, 6 and 7.
