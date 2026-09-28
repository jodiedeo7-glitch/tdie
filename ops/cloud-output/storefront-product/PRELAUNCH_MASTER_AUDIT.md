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

