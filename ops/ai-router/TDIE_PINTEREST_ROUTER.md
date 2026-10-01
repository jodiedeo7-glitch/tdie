# TDIE PINTEREST ROUTER

## Scope
This router governs only the core TDIE Pinterest line. It does not govern the Legally Blonde Amazon line, Brand Closet Amazon line, or While-You-Sleep Storefront buyer automations.

## Governing sources
Read before every production run:
1. `ops/cloud-kit/README_START_HERE.md`
2. `ops/cloud-kit/TDIE_PIN_RULES.md`
3. `ops/cloud-kit/TDIE_DESIGN_RULES.md`
4. `ops/canon/canon.json` sections `pin_render` and `products[]`
5. Any source material selected for the batch

If these sources conflict, canon and the live business state win.

## Ownership

### ChatGPT owns creation
ChatGPT produces the finished, browser-ready batch:
- source selection
- search-first topic angles
- overlays
- titles
- descriptions
- alt text
- board assignment
- date/time planning
- layout assignment
- all non-person flat-layer creative
- persona image prompts when a persona layout is used
- final compositing after the persona image exists
- contact sheet
- thumbnail QA
- `pins.csv`
- scheduling manifest

ChatGPT must not schedule pins in Pinterest unless explicitly asked to perform the browser execution task.

### Gemini/Higgsfield owns person photography
Only when a selected layout genuinely requires Tommy Kate. Follow the standing image rules and tool order. The image tool returns only the source photo. It does not create Pinterest text or layout.

### Claude owns Pinterest execution
Claude receives finished PNGs and a complete scheduling manifest. Claude only:
1. checks the current scheduled queue
2. confirms the proposed slots remain valid
3. uploads finished PNGs
4. fills metadata
5. schedules
6. verifies from the scheduled-pins view
7. logs discrepancies

Claude does not research topics, rewrite copy, design pins, or generate new layouts during the browser run. If a finished asset is invalid, Claude skips it and reports the exact issue instead of redesigning it in-browser.

## Standard batch contract
Each production packet contains:
- `png/` finished 1000x1500 pins
- `contact-sheet.png`
- `pins.csv`
- `manifest.md`
- `image-prompts.md` only if persona images are required
- `qa.md`

`pins.csv` columns:
`file,title,description,alt,link,board,date,time,source,topic_family,layout,persona_required,status,overlay,timezone,approval,asset_sha256,ai_label`

Valid status values:
`READY`, `IMAGE_REQUIRED`, `HOLD`, `SCHEDULED`, `VERIFIED`, `FAILED`

## Hard production rules
- Destination: `https://www.skool.com/thedigitalincomeedit/about`
- Canvas: 1000x1500
- Fonts: Newsreader and Inter only
- Overlay: 3 to 5 words
- Title: 60 to 100 characters
- Description: 450 to 500 characters
- Alt: 150 to 200 characters
- No prices on pins
- No income claims
- AI-generated label on
- Lockup on every TDIE pin
- Five approved boards rotate with no consecutive repeat
- Close cousins at least 3 days apart
- Never use the phrase `Make Money Online` in pin copy
- First run of a new visual system requires Jodie to see the contact sheet before scheduling

## Browser rule
The browser is for Pinterest state and scheduling only. Creative generation does not happen inside the Pinterest browser session.

## Failure rule
For blank/frozen/session errors, exhaust the browser fallback procedure in the execution job while holding the correct lock. Account warnings, unknown lock ownership and ambiguous write outcomes still hold the operation. Reconcile uncertain saves before retry. Do not change the creative packet. Record unscheduled rows as `READY` with the failure reason.

## Final manifest gate
Run `ops/scripts/validate_pins_manifest.py` on pins.csv before handing it to the operator. Use America/New_York, approval=PENDING/APPROVED/REJECTED, persona_required=YES/NO, ai_label=ON, and exact SHA-256 of the PNG. READY requires approved finished assets. A 1000x1500 header/hash check is not decoding or visual QA; inspect the image, overlay, claims, board rotation, lockup and approved fonts separately. Never use a core manifest to operate Amazon pins.
