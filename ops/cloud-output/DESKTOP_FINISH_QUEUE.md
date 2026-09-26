# DESKTOP FINISH QUEUE

Account-only steps left by cloud sessions. Each job adds one numbered section with every file path, piece of copy and exact step written in. The DESKTOP FINISH prompt in `ops/cloud-kit/CLOUD_CREDIT_JOBS.md` works through this file on Jodie's computer and marks each section DONE with the date.

## 1. DFY proof samples: photos, re-render, Skool attach (queued 26 Sep 2026, cloud session)

Cloud sessions cannot reach Skool, Gemini or Higgsfield, so the eleven PDFs were finished in the cloud with designed photo placeholders. Everything below is ready to run. Files: `ops/cloud-output/dfy-samples/`. Doc of record: `ops/cloud-kit/TDIE_DFY_SERVICES.md` → "Proof samples".

### Step A. Make two persona reference sheets (fictional clients only)
Two samples use a fictional client's own AI persona, so each needs its own reference sheet first. Run this prompt twice in Google Gemini (fresh chat each time), keep one image each, save as `ops/cloud-output/dfy-samples/build/images/REF-marnie.jpg` (Saltbox Cove Candle Co.) and `REF-lilac-lane.jpg` (Lilac Lane Nursery Finds). Never use Tommy Kate's seed image for these.

> Photorealistic character reference sheet of one invented adult woman who does not resemble any real person, celebrity or public figure. Three views side by side on one image: front, three-quarter and profile, head and shoulders, same woman in all three, neutral relaxed expression, natural minimal makeup, hair pulled back so the face is clear, plain soft grey background. Wearing a plain cream crew-neck tee. Soft even studio softbox light from the front, no harsh shadows. Shot on a mirrorless camera, 85mm lens at f/8, everything in sharp focus. Real skin texture, natural imperfections, true-to-life colour. No text, no labels, no logos, no watermarks.

### Step B. Generate every photo
Every prompt is written in full, one per photo id, in these files (tool named on each prompt; people and hands go to Google Gemini first, then Nano Banana Pro 2K on Higgsfield; no person goes to Seedream 4.5 on Higgsfield; garbled results re-run on Nano Banana Pro 2K; never Canva):
- `ops/cloud-output/dfy-samples/DFY-Viral-Instagram-Content-Calendar_Proof-Sample_image-prompts.md` (IG-1 to IG-7, ST-1 to ST-3)
- `ops/cloud-output/dfy-samples/DFY-30-Days-of-Pinterest_Proof-Sample_image-prompts.md` (PIN-1, PIN-5)
- `ops/cloud-output/dfy-samples/DFY-Repurposing-Pack_Proof-Sample_image-prompts.md` (RP-1, RP-2)
- `ops/cloud-output/dfy-samples/DFY-Etsy-Listing-Pack_Proof-Sample_image-prompts.md` (ET-1, ET-2, ET-3, ET-4, ET-7, ET-8; these are blank-card scenes)
- `ops/cloud-output/dfy-samples/DFY-Amazon-Storefront-Launch_Proof-Sample_image-prompts.md` (AZ-1A, AZ-1B, AZ-2A, AZ-2B, AZ-3A, AZ-3B; the B prompts attach `REF-lilac-lane.jpg` as the reference sheet; the A prompts need a style reference from the Command Centre `stylerefs` collection and a product sheet, per `TDIE_LEGALLY_BLONDE_PIN_FACTORY.md` sections 3b and 3c)
- `ops/cloud-output/dfy-samples/30-Days-of-AI-Persona-Photo-Prompts_Proof-Sample_image-prompts.md` (PP-01 to PP-05; attach `REF-marnie.jpg`)
Look at every image at feed size before keeping it (hands, faces, no stray text). Save each as `ops/cloud-output/dfy-samples/build/images/<photo id>.jpg`, for example `IG-1.jpg`. For the Etsy scenes, place a watercolor mushroom card design on each blank card before saving (any original painted placeholder art the session makes itself, never third-party art).

### Step C. Re-render and commit
In the repo: `cd ops/cloud-output/dfy-samples/build && pip install playwright && python3 render.py` (set `CHROME` to a Chromium path if Playwright can't find one). Open every PDF and check every page at thumbnail size. Commit and push the updated PDFs.

### Step D. Attach each PDF to its Skool lesson
Course: 📌DFY Services, slug `c83b49d5`, course id `6b03dd5e159b4a3d92e09c46b71b37a9`. Do not touch 🌶️ DFY AI Spicy Content Packages or anything listed as untouched in `TDIE_DFY_SERVICES.md`.
For each row: open the lesson, attach the PDF as a lesson file, and add exactly this one line as its own paragraph immediately above the existing "Ready to order?" block. Change nothing else in the lesson.

| Lesson | Lesson id | Line to add above "Ready to order?" | PDF to attach |
|---|---|---|---|
| ⚙️ Run It Like Mine: DFY Automation Setup | `8ab40eaa185d4f58923a53d41b812396` | See the whole thing first: The Engine, one-week run log (sample built for a fictional client). | `ops/cloud-output/dfy-samples/Run-It-Like-Mine-DFY-Automation-Setup_The-Engine_Proof-Sample.pdf` |
| 🏫 DFY Skool Autopilot | `c28d7087b60f47efb1e148354f30012d` | See the whole thing first: a full week of Skool Autopilot posts (sample built for a fictional client). | `ops/cloud-output/dfy-samples/DFY-Skool-Autopilot_Proof-Sample.pdf` |
| 📅 DFY Viral Instagram Content Calendar | `e48d0013432c48b0b5787c8194028a42` | See the whole thing first: one week of the Instagram calendar (sample built for a fictional client). | `ops/cloud-output/dfy-samples/DFY-Viral-Instagram-Content-Calendar_Proof-Sample.pdf` |
| 🧵 DFY 30-Day Threads Calendar | `ba015faf8a814dc6a5cbee70c7fc56e6` | See the whole thing first: the full first week of the Threads calendar (sample built for a fictional client). | `ops/cloud-output/dfy-samples/DFY-30-Day-Threads-Calendar_Proof-Sample.pdf` |
| 📌 30 Days of Pinterest, Done & Scheduled | `91a2c86e739a44e58d15505aadab1f51` | See the whole thing first: 5 finished pins (sample built for a fictional client). | `ops/cloud-output/dfy-samples/DFY-30-Days-of-Pinterest_Proof-Sample.pdf` |
| ♻️ DFY Repurposing Pack | `50a82ec38df941a581e7bb4b0865048d` | See the whole thing first: 6 of the 24 finished assets (sample built for a fictional client). | `ops/cloud-output/dfy-samples/DFY-Repurposing-Pack_Proof-Sample.pdf` |
| 📧 DFY 6-Email Sales Series | `5f809aa8e50f48e1b49026165fa1793c` | See the whole thing first: 2 of the 6 emails in full (sample built for a fictional client). | `ops/cloud-output/dfy-samples/DFY-6-Email-Sales-Series_Proof-Sample.pdf` |
| 🛍️ DFY Etsy Listing Pack | `c1eea7188a34452599f0ac10eb9f2343` | See the whole thing first: 1 complete Etsy listing (sample built for a fictional client). | `ops/cloud-output/dfy-samples/DFY-Etsy-Listing-Pack_Proof-Sample.pdf` |
| 🛒 DFY Amazon Storefront Launch | `8ec7129809ce4a85a7e0607b8105deec` | See the whole thing first: 3 complete storefront looks (sample built for a fictional client). | `ops/cloud-output/dfy-samples/DFY-Amazon-Storefront-Launch_Proof-Sample.pdf` |
| 📸 30 Days of AI Persona Photo Prompts | `97d70a3685ab4113b455961e106b870e` | See the whole thing first: 5 finished persona prompts and their photos (sample built for a fictional client). | `ops/cloud-output/dfy-samples/30-Days-of-AI-Persona-Photo-Prompts_Proof-Sample.pdf` |
| 📊 DFY Custom Business Dashboard | `d95e61de09e8476ebcb146b34cac4557` | See the whole thing first: a working one-page dashboard (sample built for a fictional client). | `ops/cloud-output/dfy-samples/DFY-Custom-Business-Dashboard_Proof-Sample.pdf` |

Dashboard lesson only: also attach `ops/cloud-output/dfy-samples/DFY-Custom-Business-Dashboard_Sample_Clementine-Loom.html` so buyers can open the working file.

**Writing mechanics (from `TDIE_DFY_SERVICES.md`):** lesson edits are `PUT /courses/{id}` on api2.skool.com with the flat body `{title, desc, group_id}`. The body format is `[v2]` plus a JSON array of paragraph nodes. Read the current lesson first and build the new desc from it. Filter out every empty paragraph node before writing: one empty node blanks the whole lesson.
**After every write:** reload the lesson and confirm (1) the new line is live, directly above "Ready to order?", (2) the rest of the lesson text is unchanged, (3) the PDF attachment is listed, (4) the attachment opens. A successful response is not proof; Skool drops writes silently. Then add the same Proof samples section to the project copy `claude/TDIE_DFY_SERVICES.md` and mark this section DONE with the date.
