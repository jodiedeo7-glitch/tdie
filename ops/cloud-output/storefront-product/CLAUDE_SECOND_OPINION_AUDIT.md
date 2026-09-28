# Claude Second-Opinion Audit Prompt

You are the independent second auditor for The While-You-Sleep Storefront™.

You have access to the repository and the duplicate branch/product created for this audit. Do not assume the existing architecture is correct. Do not merely summarize the files. Perform an independent pre-launch audit and then optimize your own duplicate copy.

## Your job

1. Read the entire product, not just the README.
2. Trace the actual customer workflow from setup through production.
3. Identify the exact prompt/instruction responsible for each major step.
4. Independently verify current 2026 platform policies, procedures, API capabilities, connector capabilities, plan requirements, pricing and limits using official sources.
5. For every finding in the Master Audit Record, classify it:
   - AGREE
   - DISAGREE
   - PARTIALLY AGREE
   - UNVERIFIED
6. For every disagreement, explain why and cite current evidence.
7. Find issues the first audit missed.
8. Find opportunities the first audit missed.
9. Audit every user recommendation in the Master Audit Record.
10. Do not treat the user's current personal image workflow as the recommended architecture. Benchmark it against current alternatives.
11. Do not assume a connector is better because it exists.
12. Do not assume an expensive Claude plan is required when a lower-priced paid plan can accomplish the same result.
13. For every feasible workflow step, design both:
   - SAVE TIME: automated path
   - SAVE CREDITS: manual/lower-cost paid-plan path
14. Preserve the human review/pull queue before Pinterest scheduling.
15. Audit the Pinterest API approval/demo-video workflow and incorporate it into the product architecture if it genuinely improves the product.
16. Audit the Amazon Program Content/image-generation issue carefully.
17. Audit the actual lifestyle-blog/product-page experience instead of treating the product as a generic affiliate-pin workflow.
18. Preserve the original product and make optimization changes only to the duplicate.
19. Optimize the duplicate only after the audit establishes what should change.
20. Record every change and why it was made.
21. Build a launch gate. Do not call the product ready merely because the code builds.

## Critical user requirements

The customer should be able to choose between saving time and saving credits throughout the guide. Manual alternatives must be precise and usable.

The user's current personal image routing is:
- Claude-connected Gemini: 10 free generations/day.
- Then Nano Banana Pro via Higgsfield.
- Seedream 4.5 for non-avatar images because it is currently free/unlimited for the user.
This is baseline data only. Determine whether better/cheaper/faster routing exists today.

Pinterest:
- Pins are AI-generated.
- Turn Pinterest's AI-generated/AI-Modified control ON for every applicable Pin.
- Content is not generic; it creates a lifestyle-blog/product-page experience around the linked product.
- The actual workflow is generate -> review queue -> user pulls unwanted Pins -> remaining Pins proceed to scheduling/posting.
- User has been approved for Pinterest API access and needs to complete the approval/demo video.
- Do not remove the human review/selection step.
- Determine exactly where the API should replace browser work and where it should not.

## Required deliverables

Return:
1. Complete independent audit.
2. Agreement/disagreement matrix against the Master Audit Record.
3. New findings.
4. Connector/integration matrix.
5. Platform policy matrix.
6. Exact customer workflow.
7. Exact Claude workflow.
8. Exact prompt map.
9. Save-time/save-credits matrix.
10. Cost/plan comparison.
11. Missing pieces.
12. Redundant work.
13. Reliability/recovery/security audit.
14. Amazon compliance audit.
15. Pinterest/API/OAuth/approval audit.
16. Image-generation architecture audit.
17. Product-page/lifestyle-blog/SEO audit.
18. Customer usability audit.
19. Architecture-from-scratch redesign.
20. Launch blockers.
21. Optimized duplicate product.
22. Full change log.
23. “Things You Didn’t Know You Needed.”
24. Final launch checklist.

Do not hide uncertainty. Mark unresolved items as REQUIRES LIVE TEST and give the exact test.

The goal is not to prove the first audit right. The goal is to find the best launchable version of the product.
