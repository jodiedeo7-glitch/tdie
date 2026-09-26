# TDIE DFY Services (copy for cloud sessions)

Copy of the project doc `claude/TDIE_DFY_SERVICES.md` (25 Sep 2026), placed here 26 Sep 2026. The live Skool course is the source of truth. Prices and checkout links also live in `ops/canon/canon.json` products[] (Decisions 116 and 118).

**Founder instruction (25 Sep 2026):** turn every fast automation Jodie already runs for TDIE into a DFY service, easy to tweak per client, doubling as proof of concept. Do not touch the spicy services.

**Course:** 📌DFY Services, Skool slug `c83b49d5`, course id `6b03dd5e159b4a3d92e09c46b71b37a9`, Open (public). Public URL: https://www.skool.com/thedigitalincomeedit/classroom/c83b49d5 . Ordering is by DM keyword, then intake form, then a payment link; most services also have a Beacons checkout.

**Discounts (every service):** Membership Premium members 15% off. A service's first 2 clients get 25% off in exchange for a testimonial. The two do not stack.

## The services

| Lesson | Lesson id | Prices | Order word | Built on |
|---|---|---|---|---|
| ⚙️ Run It Like Mine: DFY Automation Setup | 8ab40eaa185d4f58923a53d41b812396 | One Automation $297 · The Engine (any 3) $697 · The Full Machine (up to 6) $1,297 · Care Plan $197/month | ONE AUTOMATION / THE ENGINE / FULL MACHINE / CARE PLAN | Jodie's scheduled tasks: 8 AM publisher, weekly SkoolKit load, pin factory, Threads Sunday write + nightly load, FB group mirror, lapsed-member list, Etsy builder, Friday readout. Set up on the client's own Claude account, in her voice, with test run and instruction sheet. DM only, no Beacons product. |
| 🏫 DFY Skool Autopilot | c28d7087b60f47efb1e148354f30012d | Setup month $497 · $297/month after · Facebook group mirror +$97/month | SKOOL AUTOPILOT / AUTOPILOT MONTHLY / MIRROR | A month of 4-slot community posts written and scheduled in the client's SkoolKit, daily post auto-publish, weekly quiet-member DM list. |
| 📅 DFY Viral Instagram Content Calendar | e48d0013432c48b0b5787c8194028a42 | $297 one month · $247/month ongoing (2-month minimum) | VIRAL CALENDAR / CALENDAR MONTHLY | A custom month of Instagram content built on SOP 15, starting with viral research (40+ outlier posts from 25+ similar accounts). Distinct from the Premium calendar. 7 to 10 business days. |
| 🧵 DFY 30-Day Threads Calendar | ba015faf8a814dc6a5cbee70c7fc56e6 | $197 | THREADS CALENDAR | 30 days of Threads posts in the client's voice, daily slot plan, one offer a day with link-in-reply, hook bank. 3 to 5 business days. |
| 📌 30 Days of Pinterest, Done & Scheduled | 91a2c86e739a44e58d15505aadab1f51 | $247 (30 pins, one a day) · $597 (150 pins, five a day) | 30 DAYS OF PINS / 150 PINS | Pins designed, written (title, 450 to 500 character description, alt text) and scheduled into the client's Pinterest. |
| ♻️ DFY Repurposing Pack | 50a82ec38df941a581e7bb4b0865048d | $197 per article | REPURPOSE | One article into 24 finished assets: 10 Pinterest pins, 1 carousel, 8 Threads posts, 2 reels, 1 Facebook post, 1 email, 1 community post. 3 to 5 business days. |
| 📧 DFY 6-Email Sales Series | 5f809aa8e50f48e1b49026165fa1793c | $197 | EMAIL SERIES | Six objection emails for one offer (one objection each: can't do the tech, no time, price, no refunds / what if it isn't what I think, not enough content, I'll do it later), written and scheduled in the client's MailerLite with buyers excluded. One ask per email, linked twice, no guarantees, no income claims. 3 to 5 business days. |
| 🛍️ DFY Etsy Listing Pack | c1eea7188a34452599f0ac10eb9f2343 | $197 (5 listings) · $347 (10) | ETSY 5 / ETSY 10 | Title, 13 tags, description, 8 mockups and publishing per listing, from the client's own original designs only (no PLR, prompt packs, affiliate or third-party IP). |
| 🛒 DFY Amazon Storefront Launch | 8ec7129809ce4a85a7e0607b8105deec | $297 (10 looks) | STOREFRONT | 10 themed looks, each an Idea List in the client's storefront plus 2 pins with #ad disclosure. Method: `TDIE_LEGALLY_BLONDE_PIN_FACTORY.md` in this folder. |
| 📸 30 Days of AI Persona Photo Prompts | 97d70a3685ab4113b455961e106b870e | $197 | PERSONA PROMPTS | 30 copy-paste persona photo prompts plus 30 finished photos and the persona's written world. Method: `TDIE_IMAGE_GENERATION_MASTER.md` in this folder. |
| 📊 DFY Custom Business Dashboard | d95e61de09e8476ebcb146b34cac4557 | $97 | DASHBOARD | Custom one-page business dashboard in the client's colours with the numbers she tracks. 48 to 72 hours. |

Beacons checkout URLs for each service are in `ops/canon/canon.json` on the matching product row (`beacons_checkout_url` / `beacons_checkout_urls`).

## Untouched, never edited
🌶️ DFY AI Spicy Content Packages (Jodie handles it). AVAILABLE AI INFLUENCERS, AI Influencer Builds, Provider lesson, Brand Identity, Pinterest Growth Package, Instagram Audit. Two drafts stay drafts: 📱 DFY Social Media Content Packages, 📧 DFY Digital Marketing Packages.

## Skool writing mechanics (for whoever uploads)
Lesson edits: `PUT /courses/{id}` on api2.skool.com with a flat body `{title, desc, group_id}`. Body format is `[v2]` plus a JSON array of paragraph nodes. Filter out every empty paragraph node before writing; one empty node blanks the whole lesson. Reload and confirm after every write, because Skool drops writes silently.
