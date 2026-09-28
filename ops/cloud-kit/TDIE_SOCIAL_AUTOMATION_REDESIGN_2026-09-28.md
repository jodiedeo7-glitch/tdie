# TDIE Social Automation Redesign — 2026-09-28

## Core decision
Do not move the 33 scheduled jobs wholesale to ChatGPT.
Use the existing Claude scheduler as the coordinator, but route social operations through Metricool MCP wherever Metricool supports the exact operation. This removes browser work without creating a second scheduling system.

## Reply checks
Current: Claude opens each platform in the browser three times per day.
Target: keep Skool in Claude browser because no verified Metricool equivalent was established; route supported Facebook, Instagram and Threads inbox/comments through Metricool MCP; keep one human approval queue; post approved replies through Metricool for supported networks.

## Pinterest factories
Keep creative/build phase initially. Replace browser scheduling with Metricool MCP after a controlled test. For large batches, Metricool CSV import can schedule Pinterest posts; its current guidance recommends up to 50 posts per file. Keep Pinterest-native/browser deletion for pulled live Pins unless a tested action actually removes the live Pinterest object.

## Threads top-up
Current reason: native Threads scheduler capacity forces nightly loading. Target: keep the weekly writer but have Claude schedule the next 18 individual posts through Metricool MCP instead of browser loading. Do not create one 126-post Thread. After one full successful week, evaluate whether the nightly task can be eliminated by scheduling the whole week in advance.

## Instagram feed
Move feed scheduling to Metricool after the target Instagram account is connected. Stories containing link stickers remain manual/notification based because the third-party Instagram API does not support those interactive story elements.

## Facebook group mirror
Keep Claude. Metricool Page-post support does not establish support for the specific Facebook Group mirror.

## Skool
Keep Claude browser execution. No verified current connector replacement for the TDIE Skool operations was established.

## Etsy
Keep Claude execution. No verified current Metricool or ChatGPT write connector for the TDIE Etsy operations was established.

## Amazon
Use Amazon Creators API for product-data retrieval only after eligibility is confirmed. Keep SiteStripe short-link and Influencer Idea List operations in the existing browser path until separately verified.

## ChatGPT role
Because the current account is ChatGPT Go, do not design production around ChatGPT Work. OpenAI documents Work as unavailable on Go. Go supports scheduled tasks but only three active tasks, and scheduled tasks created inside a project cannot access uploaded/project files. Therefore ChatGPT is best used as a research/creative/analysis worker here, not as the scheduler for the 33-job system.
ChatGPT Images is available on all tiers. Current ChatGPT environment has Higgsfield, Metricool, GitHub and Canva integrations available. Google Drive is disabled in this environment. No verified native ChatGPT connector was established for Pinterest, Amazon Associates, Gemini, Skool or Etsy.

## Higgsfield cost caution
Higgsfield officially connects to ChatGPT and Claude. Connected-agent generations use Higgsfield credits, while website-specific free/Unlimited allowances do not automatically transfer to the agent path. Do not migrate the TDIE Seedream/Gemini production path until credit economics are tested.

## Google Drive
Do not add Google Drive as a general TDIE state store. GitHub/canon is already the source of truth. A second repository creates synchronization risk.

## Canva
Do not insert Canva into the Amazon/Pinterest image factory. TDIE canon excludes Canva as the image generator. Use Canva only for workflows that actually require editable Canva designs.

## Model strategy
Claude Sonnet 5.5 is the current cheaper model for well-scoped everyday work. Opus 5.5 is the current strong writing/design/judgment model and is cheaper than Fable 5.1 in token pricing.
Benchmark before downgrading Fable assignments: monthly DFY calendar, Friday Skool week build, Friday numbers/member read.
Use Sonnet 5.5 first for routine execution: 8am publisher, Threads top-up, approved-reply posting, missed-run, Pinterest state operations and inactive-member sweep.

## Timing fix already made on migration branch
GitHub Actions now uses timezone-aware scheduling for the Friday audit at 8:00 am America/New_York. This corrects the previous UTC drift.

## Migration safety
Connect one platform, run one test, verify the platform result and state, test a duplicate/retry scenario, keep the old browser path active until it passes, then remove only the redundant step. Never run two publishers for the same content.