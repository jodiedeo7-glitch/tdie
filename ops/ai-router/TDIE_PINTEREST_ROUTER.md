> **Current core Pinterest reconciliation (4 October 2026):** Read `ops/ai-router/CORE_PINTEREST_RECONCILIATION_2026-10-04.md` first. It supersedes conflicting legacy browser, ownership-fallback, missing-source and vocabulary instructions below. This repository edit does not change live tasks or prove a publishing cutover.

# TDIE PINTEREST ROUTER

> **MIDJOURNEY, STANDING RULE (Jodie, 3 October 2026).** Jodie has an active Midjourney subscription, signed in in her browser, with far more free generations than Higgsfield. Whenever an image would come out better in Midjourney, use Midjourney, with or without a person. This amends every tool-order line in this file that says no other image generator is used. Canva is still never an image generator. Full rule: section M of claude/TDIE_IMAGE_GENERATION_MASTER.md.


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
ChatGPT produces the finished, Metricool-ready batch:
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

Publishing ownership is established by the reconciliation's live owner check, not by the creative role.

### Gemini/Higgsfield owns person photography
Only when a selected layout genuinely requires Tommy Kate. Follow the standing image rules and tool order. The image tool returns only the source photo. It does not create Pinterest text or layout.

### Verified operator owns Metricool execution
The verified publisher receives finished PNGs and a complete manifest, reconciles live Metricool state, schedules, reads back each result and logs discrepancies. Follow the reconciliation's execution procedure. No research, copy rewriting or creative generation during scheduling.

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
- No banned vocabulary list; verify claims and facts.
- First run of a new visual system requires Jodie to see the contact sheet before scheduling

## Execution and recovery
Use Metricool only for scheduling, editing, deleting and scheduled-state verification. Follow the reconciliation for ownership, concurrency, partial results and unsupported AI-label behavior. Never retry ambiguous writes blindly.

## Final manifest gate
Run `ops/scripts/validate_pins_manifest.py` on pins.csv before handing it to the operator. Use America/New_York, approval=PENDING/APPROVED/REJECTED, persona_required=YES/NO, ai_label=ON, and exact SHA-256 of the PNG. READY requires approved finished assets. A 1000x1500 header/hash check is not decoding or visual QA; inspect the image, overlay, claims, board rotation, lockup and approved fonts separately. Never use a core manifest to operate Amazon pins.
