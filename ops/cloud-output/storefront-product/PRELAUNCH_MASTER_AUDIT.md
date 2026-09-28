# The While-You-Sleep Storefront™ — Master Pre-Launch Audit Record

## Purpose

This is the master audit record for the pre-launch review of The While-You-Sleep Storefront™. The working branch is `overnight-storefront-audit-optimized`. The original product on `main` is preserved.

The audit must establish the actual customer experience first, then compare it against current platform policies, current capabilities, cost, reliability, simplicity, and product value. Do not optimize merely because a newer tool exists.

## Operating rule

For every major step:
1. What does the customer actually do?
2. What does Claude actually do?
3. What exact prompt/instruction causes it?
4. What external service/API/connector is used?
5. What is the input and output?
6. Can the step be simpler?
7. Can a connector/API/script/state file do it instead?
8. Can the step be eliminated?
9. What is missing?
10. What current policy/capability changed since the workflow was built?
11. What is the cheapest reliable way to accomplish it?
12. What is the fastest reliable way to accomplish it?
13. Is the step safe, repeatable, recoverable and customer-proof?

## User requirements and decisions captured in this audit

- Audit the product before launch, not just the implementation.
- Look for what is missing, not only what exists.
- Audit workflow, policies/procedures/guidelines, ease of operation, output quality, cost, reliability, customer effort, and hidden opportunities.
- Search current Claude connectors/integrations for image generation, Higgsfield, Google/Gemini, GitHub, Pinterest, Amazon/Amazon Associates, Canva, Google Drive, and every other service actually used.
- Do not assume a connector is better just because it exists.
- Identify work that should be done by a connector/API/script/stored state/reusable asset/scheduled task rather than Claude.
- Identify every manual customer action that can be eliminated or reduced.
- Identify missing setup, permissions, connectors, account configuration, error handling, validation, safety checks, cost controls, backups, recovery, customer instructions, disclosures, platform requirements and automation.
- Research newer/better capabilities available in 2026.
- Challenge the architecture as if building it from scratch today.
- Find duplicated verification, browser work, sequential work, regenerated assets, repeated setup information and other hidden work.
- Produce an explicit connector matrix.
- Produce a final “Things You Didn’t Know You Needed” section.
- Maintain a cumulative record of findings, corrections, decisions, changes and reasoning.
- After this audit, optimize a duplicate copy of the product. Do not alter the original until the optimized version is reviewed.
- Prepare a complete second-opinion audit package that can be given to Claude. Claude must independently fact-check every finding, agree or disagree with evidence, audit every platform policy/procedure/current capability, incorporate every user recommendation, and add optimizations neither audit found initially.
- The two optimized versions will be compared to create one final master release.

## User-requested dual operating modes

Every feasible major workflow step should have:
- ⚡ SAVE TIME: automated/high-tier paid-plan path.
- ★ SAVE CREDITS: manual/lower-cost paid-plan path.

The manual path must not be treated as a second-class path. It must include exact tool, action, prompt/input, expected output, and next step.

Important: the user means lower-priced PAID Claude plans, not Free. Do not describe the architecture as Free vs paid unless a specific capability truly requires it.

Do not assume every automated step requires a higher plan. Verify the minimum paid plan required for each capability.

## Current personal image workflow: baseline only

The user's current workflow is:
1. Claude connected to Gemini provides 10 free generations/day.
2. After those are used, the user currently switches to Nano Banana Pro through Higgsfield.
3. For non-avatar images, the user currently uses Seedream 4.5 because it is currently free/unlimited for the user.

This is NOT a claim that this is optimal. It is the baseline to benchmark against:
- current Gemini/Nano Banana models and pricing;
- Higgsfield capabilities/pricing/API;
- Seedream 4.5 availability/pricing/limits;
- image quality;
- avatar consistency;
- reference-image capability;
- speed;
- number of Claude turns;
- browser work;
- failure/retry rate;
- customer accessibility;
- actual per-look cost.

The audit must determine whether a significantly cheaper, simpler, faster or higher-quality routing exists.

## Important correction: Pinterest workflow

The current workflow is NOT autonomous publishing without review.

Actual model:
Generate content -> place it in a review queue -> user reviews -> user pulls anything unwanted -> anything remaining proceeds to scheduling/posting.

This human review/pull step is a core product control and must be preserved unless a better compliant workflow is demonstrated.

Pinterest AI label:
- The user's Pins are AI-generated.
- Pinterest currently provides an explicit Mark as AI-Modified toggle.
- The product workflow should turn that toggle ON for every applicable Pin.
- Do not describe the AI label as merely optional or uncertain.

Pinterest content:
- The workflow creates a lifestyle-blog/product-page experience around the product; it is not merely generic affiliate content.
- Audit the actual product page, creative, copy and destination before judging originality/value.
- Do not infer the product is generic from the Pinterest publishing step alone.

## Amazon image/content issue

Do not send Amazon Program Content, including Amazon product images, into a generative AI model unless current Amazon terms explicitly permit that use.

The current Amazon policy updated April 14, 2026 states that Program Content cannot be used to develop or improve LLMs, multimodal models, ML models or related technology, and limits use/storage/redistribution of Program Content. It also restricts use of Program Content outside the licensed Site context. Verify the exact current policy before implementation.

The replacement architecture must preserve accurate product identification without using restricted Amazon Program Content as an AI-generation input.

## Pinterest API

The user has been approved for Pinterest API access and needs to complete the approval/demo video.

This must be incorporated into the audit and optimization.

Audit:
- app configuration;
- OAuth;
- requested scopes;
- approval video;
- privacy policy;
- token handling;
- image Pin creation;
- video Pin creation;
- read/update/delete;
- boards/sections;
- scheduling;
- AI label handling;
- rate limits;
- error handling;
- queue/review/pull workflow;
- whether API can replace browser automation;
- whether API can support both image and video workflows;
- sandbox testing and production testing.

The Pinterest API must NOT be assumed to replace browser automation merely because it exists. Pinterest's current Developer Guidelines say end users must specifically consider each action and, for scheduled Pins, the end user must choose each Pin to be published. Reconcile this with the product's human review queue before changing the architecture.

## Current Pinterest findings to verify continuously

- Native Pinterest publishing supports Publish Later for Business accounts, up to 30 days.
- Pinterest provides a Mark as AI-Modified control.
- Pinterest API supports image/video Pins, boards and Pin CRUD.
- Pinterest provides an API sandbox for testing supported endpoints.
- Pinterest developer policy requires specific user consideration/consent for actions.
- The final architecture must preserve the customer's review/selection step.

## Current Claude capability findings

Current Claude scheduled tasks are available on paid plans and can use connected tools, skills and plugins. Current documentation says scheduled tasks run remotely when possible, but tasks requiring local files/apps run locally.

Remote MCP custom connectors are available across Claude Free, Pro, Max, Team and Enterprise, with Free limited to one custom connector.

Do not assume an expensive plan is required for a connector. Verify capability-by-capability.

## Connector candidates to investigate

| Connector / Integration | Status | Audit question |
|---|---|---|
| GitHub | Connected/used | What can become deterministic/API-based instead of browser work? |
| Pinterest API | Approved by user, video still needed | Can it replace publishing/verification/pulls while preserving review? |
| Amazon Associates / Creators API | Investigate | Can current Creators API replace SiteStripe/browser sourcing? |
| Amazon Selling Partner connector | Investigate | Is it actually relevant to affiliate/creator use, or not? |
| Gemini | Current workflow | Can direct/current Gemini image capability beat browser/connector routing? |
| Higgsfield | Current workflow | Is there an official API/connector and does it reduce work/cost? |
| Seedream 4.5 | Current workflow | Verify current price/limits/API and whether it remains the best non-avatar path. |
| Canva | Investigate | Can it simplify deterministic creative composition/editable assets without replacing image generation? |
| Google Drive | Investigate | Can it replace local state/assets safely? |
| Metricool | Investigate | Can it provide compliant Pinterest scheduling/publishing without unnecessary browser automation? |
| Other services | Discover | Audit every actual service in the product. |

## Architecture principles to test

Preferred order:
1. Native platform/API/official connector.
2. Deterministic script.
3. Stored state/reusable asset.
4. Scheduled task.
5. Browser automation.
6. Manual fallback.

Do not follow this order blindly. Platform policy and actual reliability override convenience.

## Current repo-specific findings already identified

- The buyer kit contains a core setup prompt, themed-look recipe, Brand Closet recipe, scheduled task prompts, storefront paths, blog-half instructions and optional Instagram add-on.
- Existing buyer testing has covered multiple paths but much of the desk testing is simulated/unverified for live Amazon/Pinterest/Claude behavior.
- The existing kit already has browser-lock, leftovers, recovery and Runs-table mechanisms.
- The existing audit identified Amazon background-fetch risk and changed the workflow to read loaded Amazon pages instead of background fetches.
- The Brand Closet backlog logic has been identified as a potential loss point and has explicit recovery changes in the existing audit.
- The existing product has an Associates-only path and an Influencer path, plus an optional blog/site half.
- The existing product uses a human review/pull queue before Pinterest scheduling.
- The current guide includes a 5-minute setup promise; audit whether this is accurate as a total onboarding claim versus a setup-prompt claim.
- The current product contains an optional Instagram add-on; audit whether it should remain separate, be redesigned, or be removed from the core product.
- The current product has an optional Brand Closet line; audit dependencies, cost, permissions and customer value.
- The product currently uses multiple Markdown/text state files; audit whether structured state can simplify recovery and reduce repeated work.
- The blog half relies on GitHub/Vercel-style workflows; audit whether the customer-facing path is still optimal.
- The original product must remain untouched during the audit/optimization.

## Required final audit outputs

1. Executive launch readiness summary.
2. Complete customer journey map.
3. Complete workflow map.
4. Step-by-step AS-IS table.
5. Step-by-step TO-BE table.
6. Exact prompt/instruction map.
7. Customer action inventory.
8. Claude action inventory.
9. External service/API/connector inventory.
10. Connector matrix.
11. Platform policy matrix.
12. Cost/plan matrix.
13. Save-time vs save-credits matrix.
14. Missing capabilities/gaps.
15. Redundant work.
16. Reliability/failure/recovery audit.
17. Security/privacy/credential audit.
18. Affiliate disclosure audit.
19. Amazon compliance audit.
20. Pinterest compliance/API audit.
21. AI/image-generation compliance and provenance audit.
22. SEO/product-page audit.
23. Customer onboarding/usability audit.
24. Product-value/output-quality audit.
25. Architecture-from-scratch challenge.
26. New 2026 capabilities audit.
27. Launch blocker list.
28. Recommended optimizations ranked by impact.
29. “Things You Didn’t Know You Needed.”
30. Complete change log with reason/evidence.
31. Claude second-opinion audit prompt.
32. Final comparison checklist for merging the two optimized versions.

## Evidence standard

Separate:
- VERIFIED CURRENT FACT
- REPO FACT
- USER-PROVIDED FACT
- INFERENCE
- OPEN QUESTION
- REQUIRES LIVE TEST

Never turn an inference into a fact.

For current platform policy/capability claims, use current official documentation whenever possible.

For pricing/limits, record date checked.

For any recommendation that changes architecture, state the reason and what it replaces.

## Second-opinion requirement

Claude must not merely summarize this audit.

Claude must:
- independently inspect the same duplicate product;
- independently inspect the actual files;
- independently research current official policies/capabilities;
- challenge every factual claim;
- mark each finding AGREE / DISAGREE / PARTIALLY AGREE / UNVERIFIED;
- explain disagreements with evidence;
- find missing issues;
- find optimizations neither audit identified;
- audit every user-requested recommendation;
- independently optimize its own duplicate;
- preserve the original product;
- return a complete change log;
- produce a final launch gate.

Neither audit is authoritative by default. The final master is created only after comparing both.



## 2026-09-28 live verification addendum

### Pinterest — verified
- Pinterest Developer Guidelines explicitly list content-marketing tools such as Pin schedulers and dynamic creative tools as acceptable uses.
- The same guidelines prohibit apps from automatically initiating actions without users specifically considering each action; for scheduled Pins, the user must choose each Pin to be published. Therefore the product's existing review queue is an architectural compliance control: the customer reviews the generated queue and removes unwanted Pins before the remaining selected Pins proceed.
- Pinterest API v5 currently supports image/video Pins, product tagging on organic Pins, board/section management, and Pin GET/POST/PATCH/DELETE/SAVE.
- Pinterest Sandbox currently supports image Pin creation and Pin/board CRUD but explicitly does not support creating video Pins. Sandbox documentation was updated September 8, 2026.
- Pinterest Standard-access approval requires a demo video showing the OAuth authentication flow and live Pinterest integration. The user's API approval/video work must remain a pre-launch workstream.
- Pinterest's current help documentation explicitly provides a Mark as AI-Modified toggle for content made completely or partly with AI or containing an AI-generated person. The user's procedure should enable this for every applicable AI-generated Pin.

### Amazon — verified
- Amazon's current Associates policies were updated April 14, 2026.
- Special Links may currently be used in solicited/opted-in email, SMS and social-media direct messages, subject to the agreement, trademark/brand rules and applicable marketing law. Therefore any blanket statement that Amazon categorically prohibits affiliate links in email/SMS/DM is too broad and must be corrected.
- Separately, Amazon's Program Content restrictions remain a distinct issue. The audit must distinguish the permitted use of Special Links from restrictions on Amazon-provided Program Content, including images/data/text.
- Amazon requires Program Content to be used within the license scope and restricts altering Program Content. Do not assume an Amazon product image can be transformed or fed to a generative model merely because it is publicly visible.

### Gemini image architecture — verified
- Current Gemini API documentation identifies Nano Banana 2 Lite, Nano Banana 2, Nano Banana Pro, and legacy Nano Banana.
- Google positions Nano Banana 2 as the general workhorse balancing quality, speed and cost; Nano Banana 2 Lite as the efficiency/low-cost option; Nano Banana Pro as the premium model for complex visual tasks and precise creative control.
- Current Gemini API pricing lists Nano Banana 2 at approximately $0.067 per 1K image, $0.101 per 2K image and $0.151 per 4K image under standard paid pricing; batch pricing is lower. Nano Banana Pro is approximately $0.134 per 1K/2K image and $0.24 per 4K image under standard paid pricing.
- The user's existing Claude-connected Gemini 10-free-generations/day workflow should therefore be benchmarked against direct Gemini API/AI Studio availability, Nano Banana 2/2 Lite, and the current Higgsfield/Nano Banana Pro and Seedream 4.5 options. No replacement should be made without quality/consistency/cost testing.


## 2026-09-28 audit corrections and launch-level findings

### A. Claude scheduled-task architecture — VERIFIED CURRENT
Anthropic's current Cowork documentation materially changes the original product instructions:
- Scheduled tasks can run remotely even when the computer is asleep or the Claude Desktop app is closed.
- However, a scheduled task that requires local files or local apps runs locally.
- A local-folder workflow therefore still requires the Claude Desktop app to be open/connected when the task needs that local folder.
- Browser use through the user's own Chrome and local computer access also require the Claude Desktop app to be open.
- Current Claude scheduled tasks support hourly/daily/weekly/weekdays/manual cadence, and the task can specify a folder.
- Current documentation says scheduled tasks are available on Pro/Max for individual users; Claude in Chrome is available on paid plans.

PRODUCT CHANGE REQUIRED:
The guide must stop saying simply "scheduled tasks run from your own computer" as though all scheduling itself is local. The accurate statement is:
"Your scheduled task can be scheduled in Claude's cloud, but because this workflow uses your local Storefront folder and your signed-in browser, the computer running Claude Desktop must be online with Claude Desktop open when the task runs."

The current "missed-run sweep" may therefore still be useful for local execution failures, but its rationale must be rewritten. Do not describe it as necessary merely because scheduled tasks cannot run while the computer is off.

Sources: Anthropic Claude Cowork scheduled tasks and Cowork architecture documentation, checked 2026-09-28.

### B. Browser architecture — VERIFIED CURRENT
Claude now has a built-in browser in Cowork in addition to Claude in Chrome. The built-in browser does not touch the user's existing Chrome tabs/logins. The Storefront currently depends on the customer's signed-in Amazon/Pinterest/Skool sessions, so the Chrome path remains relevant unless the entire workflow is redesigned around authenticated connectors/API access.

Do not replace Chrome simply because a built-in browser exists. The audit must determine, service by service, whether browser-session dependence can actually be removed.

### C. Amazon Creators API — VERIFIED CURRENT, NOT A UNIVERSAL CUSTOMER DEPENDENCY
Amazon's current Creators API can programmatically search products, retrieve ASIN/product information, variations, browse nodes and image URLs. However, current Amazon documentation says API access requires final Associates acceptance and qualified sales eligibility; the current eligibility criterion documented by Amazon is 10 qualified sales in the trailing 30 days. API access can also be lost after a consecutive 30-day period without qualified referring sales.

PRODUCT CHANGE REQUIRED:
Do not make Creators API a required setup step for ordinary new Storefront customers. It should be treated as an optional advanced optimization for eligible customers.

Potential future optimization:
For eligible customers, Creators API could replace browser-based Amazon search/ASIN retrieval and reduce browser work. It does not automatically solve affiliate-link creation, Program Content licensing, or product-image rights, so those must remain separately audited.

Sources: Amazon Creators API onboarding, API rates, resources and troubleshooting, checked 2026-09-28.

### D. Amazon + Pinterest direct-link architecture — VERIFIED CURRENT, REQUIRES REDESIGN REVIEW
Amazon's current Associates agreement explicitly defines a monetizable "Site" to include social media user-generated content and permits Special Links in qualifying social-media contexts. Pinterest's current affiliate guidelines permit affiliate links when content is original, adds unique value, is transparent, and is used in moderation.

This means the current product statement:
"Associates only and NO website = the machine cannot run"
is not established as a current universal Amazon rule and must be re-audited.

Pinterest itself permits affiliate content and separately offers an Amazon Storefront connection for eligible creators. Pinterest's Amazon Storefront integration currently requires Amazon Influencer participation, but that is separate from the broader Associates social-link permission.

PRODUCT CHANGE REQUIRED:
Re-test an Associates-only/no-website path in which Pins link directly to compliant Amazon Special Links or use Pinterest's supported product-tagging mechanisms where available. Do not retain the website as a mandatory dependency unless the direct-link route fails an actual Amazon/Pinterest policy or technical test.

This could eliminate the largest remaining manual branch for Associates-only customers.

### E. Pinterest native Amazon integration — NEW OPPORTUNITY
Pinterest currently allows eligible creators who connect an Amazon Storefront to use an Amazon filter when tagging products; affiliate links are applied automatically and Pins with those affiliate links automatically receive an affiliate-link disclosure. Pinterest's current Pin design tools also support up to five product stickers per Pin.

PRODUCT CHANGE REQUIRED:
Test whether the Storefront should teach Amazon Influencer customers to connect their Amazon Storefront to Pinterest and tag up to five products directly on the Pin. This may complement or partially replace the Idea List workflow, especially for the first five hero products.

Do not replace Idea Lists until the customer journey, click destination, disclosure behavior, and multi-product shopping experience are tested.

### F. Pinterest affiliate-volume risk — VERIFIED CURRENT
Pinterest's affiliate guidelines state that affiliate content should be original and add unique value, and that affiliate Pins should be used in moderation. They specifically warn against creating affiliate Pins repetitively or in large volumes.

PRODUCT CHANGE REQUIRED:
The product's current "3 / 5 / 7 looks per week" setting and two Pins per look must be tested against Pinterest's current spam/affiliate enforcement guidance. The existing 60-second spacing and 6-pin pause are operational safeguards, but they are not evidence that a given volume is safe.

The product must not imply that the prescribed volume is "Pinterest-safe" merely because it has delays.

### G. Brand Closet™ automation — LAUNCH BLOCKER PENDING RIGHTS VERIFICATION
The current kit uses a paid third-party Skool membership as an input source for a commercial affiliate-content automation. The recipe correctly says not to copy, save, upload, or redistribute the third party's paid images/prompts/lesson text, but it still derives commercial content from that paid material.

Skool's current Transaction Terms state that a member's license to restricted Admin content is revocable, limited, non-transferable, non-sublicensable and for private, personal, non-promotional, non-commercial use.

PRODUCT CHANGE REQUIRED:
Do not ship Automation 2 as a commercial use case unless there is explicit permission/license from the Brand Closet owner covering this use. A rule saying "do not save or repost the paid content" is not enough if the automation is commercially deriving new affiliate content from the paid material.

Until rights are documented, the safest launch architecture is:
- core product: Automation 1 only;
- Brand Closet integration: remove from the core automation or replace with a permissioned/public source;
- if retained, add explicit owner permission and scope to the product's requirements.

This is a launch blocker, not a cosmetic improvement.

### H. Amazon product-image generation — LAUNCH BLOCKER PENDING RIGHTS-SAFE REPLACEMENT
The current image recipe uses screenshots of Amazon product images as reference inputs to an image generator. It then creates a new image and does not publish the Amazon image itself.

That is better than reposting Amazon's image, but the current Amazon Program Content license does not establish permission to feed Program Content into a generative model or create derivative works from it. Amazon also prohibits altering Program Content and limits its use to the licensed scope.

PRODUCT CHANGE REQUIRED:
Replace "attach the Amazon product sheet to the image generator" with a rights-safe product-reference method.

Candidates to test:
1. Text-only product description generated from the Amazon page, with no Amazon image supplied to the model.
2. A customer-owned photograph of the product.
3. A manufacturer/seller image for which the customer has a separate license allowing this use.
4. A rights-cleared product-feed/image source whose terms expressly permit generative transformation.
5. If Amazon explicitly confirms a permitted API/reference workflow for this use, document that permission before adding it.

The product must not tell customers that Amazon images are safe to use as generative references merely because they are not directly published.

### I. Amazon policy wording in the kit is outdated
The current recipe says "Amazon's rules ban affiliate links in email." That is too broad under the April 14, 2026 Associates policy. Amazon now permits Special Links in solicited/opted-in email, SMS and social-media direct messages subject to the agreement and applicable marketing/brand requirements.

PRODUCT CHANGE REQUIRED:
Replace the blanket ban with a precise rule. The core product does not need email affiliate links, so the simplest product wording is:
"Do not add Amazon affiliate links to this workflow's email copy. If you ever use Special Links in email, SMS or social DMs outside this workflow, follow Amazon's current opted-in communication requirements."

### J. Current AI-model architecture — VERIFIED CURRENT
Google currently identifies Nano Banana 2 as its general-purpose image-generation workhorse, Nano Banana 2 Lite as the efficiency specialist, and Nano Banana Pro as the premium complex-asset model. The legacy Nano Banana is being deprecated and is scheduled for shutdown October 2, 2026.

PRODUCT CHANGE REQUIRED:
Do not build a long-lived customer guide around legacy Nano Banana as a required model. Any customer instructions using "Nano Banana" must be clarified as either:
- the current model actually intended by the platform; or
- a specific legacy model that is being phased out.

The audit should test whether Nano Banana 2 can replace the current faceless regular Nano Banana/Seedream routing for customers.

### K. OpenAI current image stack — VERIFIED CURRENT
OpenAI currently offers GPT Image 2.5 Flare for fast everyday image generation and GPT Image 2.5 Sunburst for higher-precision image generation/editing. Both accept text and image inputs and support iterative editing.

PRODUCT CHANGE REQUIRED:
OpenAI remains a benchmark candidate, but no architecture change should be made from model documentation alone. It requires the same controlled Storefront quality test as Gemini/Higgsfield/OpenArt.

### L. Current customer-plan architecture
The customer recommendation must be based on the current plans and actual model access available to a new customer, not the founder's personal unlimited access.

The product should separate:
- "model quality recommendation"
- "platform access recommendation"
- "customer subscription recommendation"

An Unlimited model on the founder's account is not evidence that the same model is unlimited for a customer.

### M. Human review remains mandatory
The existing review/pull queue remains valuable and should be preserved. Pinterest's current developer guidelines explicitly say that if an app schedules Pins, the end user must choose each Pin to be published.

The workflow can automate preparation and scheduling of Pins that the customer has specifically selected, but it should not silently publish an unreviewed generated queue.

### N. Current Pinterest AI transparency requirement
Pinterest currently provides a Mark as AI-Modified control and separately has AI detection/transparency mechanisms. The product should explicitly enable the user-controlled AI label for every applicable generated Pin rather than treating it as optional.

### O. New highest-priority launch blockers
Before release, resolve these in this order:
1. Rights-safe replacement for Amazon product screenshots as AI-generation inputs.
2. Explicit permission/license for Brand Closet commercial derivative workflow, or remove that automation from the launch product.
3. Re-test Associates-only/no-website architecture.
4. Re-test current Pinterest affiliate volume against the moderation requirement.
5. Update Claude scheduling/local-computer instructions to current Cowork behavior.
6. Test current image-model routing and customer plan economics.
7. Then perform the Pinterest API migration test while preserving the human selection/review gate.

