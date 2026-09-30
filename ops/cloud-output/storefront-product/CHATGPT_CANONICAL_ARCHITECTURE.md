## Audit update · 30 Sep 2026

The production Pinterest board and its linked Amazon list have now passed read-only checks in the connected account. Board: public, ID 1122311238330934930. Destination: public six-item list. A similar Pin is already scheduled for Oct 2, so the current pink cold-office draft must remain unscheduled as a duplicate risk; Oct 7 remains withdrawn. The end-to-end ChatGPT Work → Drive/Metricool path remains untested. Desktop route: select ChatGPT from the top-left menu, select Work in the switcher above the composer, open the storefront project under Projects, then choose Work. Availability can depend on the account plan and workspace.

# While-You-Sleep Storefront™: Canonical ChatGPT Architecture
## Verification-first source of truth
Date: 2026-09-28

This document is the canonical architecture for the customer-facing While-You-Sleep Storefront™ migration from Claude to ChatGPT.

## 1. SYSTEM OWNERSHIP

### ChatGPT Work
Owns:
- customer setup interview and configuration
- deterministic schedule calculation
- product/ASIN research when the customer supplies a valid Amazon path
- pin title, description and alt-text generation
- image-generation orchestration
- reading and updating structured state
- duplicate prevention and recovery decisions
- preparing publishing records
- verification and reporting

ChatGPT Work can run recurring Scheduled Tasks. Cloud Work runs on a remote computer and can continue after the customer's computer is off. Local Work can access local folders on the customer's computer. Cloud and local capabilities are distinct. [VERIFIED: OpenAI Help Center, 2026-09-28]

### Higgsfield
Owns image generation when selected by the customer.
Higgsfield documents an official ChatGPT integration and an official MCP. [VERIFIED: Higgsfield official documentation, 2026-09-28]

### Metricool
Owns Pinterest publishing/scheduling in the TIME-SAVING path, subject to the customer's connected Metricool/Pinterest account and the exact ChatGPT scheduled-task integration being successfully tested.

Current verified Metricool capabilities include:
- Pinterest scheduling
- Pinterest board selection
- Pinterest Pin title
- Pinterest Pin link
- alt text
- CSV bulk scheduling
- create/update/delete scheduled-post operations through Metricool tooling/API
- connected Google Drive media for direct Metricool posting when the customer's Google Drive connection is linked to Metricool
- CSV media import via publicly accessible direct media URLs

[VERIFIED: Metricool official documentation, 2026-09-28]

IMPORTANT:
The end-to-end combination "ChatGPT Scheduled Task automatically invokes Metricool to publish a Pinterest Pin without a user approval step" is currently UNVERIFIED.
The 2026-09-30 read-only account audit verified production board `Legally Blonde Outfits | Pink Amazon Fashion` as public with ID `1122311238330934930`, matching the Metricool draft's board ID. Its Amazon destination resolved to the public six-item list. This closes the production-board existence/ID check for that board; it does not prove that a connected Work task can create, schedule, and read back a post.
DO NOT publish fully unattended publishing as a guaranteed customer capability until the end-to-end scheduled-task test passes. Production board existence and ID have been verified read-only; actual authorized create/schedule/readback remains untested.

### Pinterest
Owns native Pinterest publishing in the CREDIT-SAVING path.

Pinterest's API supports creating, reading and deleting Pins, but Pinterest's developer policy requires the end user to specifically choose each Pin when an app schedules Pins. Therefore the product must not promise unrestricted autonomous Pinterest API publishing. [VERIFIED: Pinterest official documentation/policy, 2026-09-28]

### Google Drive
Owns cloud-accessible customer state and generated assets for the CLOUD execution path, when the customer chooses this architecture.
ChatGPT's Google Drive app supports reading connected files/folders and, where authorized, creating/updating supported Drive-family files. [VERIFIED: OpenAI Help Center, 2026-09-28]

### Amazon
Amazon remains the customer-controlled product source and affiliate-account layer.

PA-API 5 is deprecated. Amazon says new and existing integrations should move to Creators API. Creators API provides programmatic catalog access but has its own eligibility/onboarding requirements. [VERIFIED: Amazon Associates official documentation, 2026-09-28]

Do not build the customer workflow around PA-API 5.
Do not assume every customer qualifies for Creators API.
Do not scrape Amazon as a substitute for an approved integration.

## 2. CUSTOMER MODES

### TIME-SAVING
Customer connects:
1. Eligible ChatGPT Work
2. Google Drive
3. Higgsfield if selected
4. Metricool + Pinterest
5. Amazon account/path required by the selected storefront path

ChatGPT builds the content and prepares the publishing record.
Metricool is the intended Pinterest scheduling/publishing layer.

End-to-end autonomous ChatGPT Work → Metricool publishing remains UNVERIFIED until tested.

### CREDIT-SAVING
Customer uses:
1. ChatGPT Work
2. selected image provider
3. native Pinterest

ChatGPT prepares the finished Pin package.
Customer performs the final Pinterest scheduling action.

This path must not require Metricool or Pinterest API approval.

### MIXED
Customer can use Metricool for publishing while manually performing any expensive or optional image/research step.

## 3. EXECUTION MODES

### CLOUD
Preferred architecture for a true "while you sleep" experience.
- State lives in Google Drive-supported files/sheets.
- Assets live in Google Drive or another supported connected asset store.
- ChatGPT Work runs remotely.
- Customer computer does not need to stay on.

This is the preferred target architecture, but the exact scheduled-task + connected-app write path must be tested before it is marketed as fully unattended.

### LOCAL
Fallback when the customer needs a local folder or a site/browser that cannot be reached reliably from cloud execution.
- ChatGPT Work runs locally in the desktop app.
- Local files can be used.
- The computer must be available during runs.

The product should not make LOCAL the default merely because the original Claude architecture used a local folder.

## 4. CANONICAL STATE

The old markdown-file state model is retained only as a human-readable export.

The authoritative state should be structured and keyed by stable IDs.

Required entities:
- LOOK_ID
- PIN_ID
- PRODUCT_ID / ASIN
- IMAGE_ID
- PUBLISHER_POST_ID
- BOARD_ID
- DESTINATION_URL
- RUN_ID

Required states:
- intake_needed
- ready
- building
- built
- queued
- scheduled
- published
- verified
- pull_requested
- pulled
- failed
- dropped

A run must be idempotent:
- Before creating a look, check LOOK_ID.
- Before creating a Pin, check PIN_ID.
- Before scheduling, check PUBLISHER_POST_ID or an exact deterministic fingerprint.
- A repeated run must reconcile existing records instead of creating duplicates.

## 5. PUBLISHING RECORD

Every Pin must have one structured record containing:
- pin_id
- look_id
- image_id
- image_location
- title
- description
- alt_text
- destination_url
- board_id
- scheduled_at
- publisher
- publisher_post_id
- status
- last_checked_at
- error_code
- pull_requested

The human-readable pin-tab.md is a view/export, not the authoritative state.

## 6. ERROR MODEL

External operation failures must transition state instead of relying on prose.

Examples:
- image generation failure → image_failed
- destination unavailable → destination_blocked
- publisher rejection → publish_failed
- approval required → awaiting_approval
- duplicate detected → reconciled
- network/browser failure → retry_pending

No silent provider/model substitution after credits are exhausted.

## 7. PINTEREST PULL MODEL

Metricool currently documents deleting scheduled posts in its planner, but its API limitation documentation says editing already-published Pinterest posts is not supported.

Therefore:
- scheduled/unpublished pull = remove/cancel in the publishing layer
- already-published pull = remove from Pinterest itself
- state must distinguish scheduled vs published

Do not promise that deleting a Metricool record automatically deletes an already-published Pinterest Pin.

## 8. IMAGE GENERATION RULE

The canonical customer path is:
1. one image generation
2. deterministic copy/layout work
3. final publishing asset

Do not introduce a second paid image generation merely to place text on an already-approved image unless the selected provider cannot produce the required final asset another way.

## 9. CUSTOMER PROMISE

The product promises a repeatable content-production and publishing system.

It does NOT promise:
- sales
- traffic volume
- affiliate earnings
- Pinterest distribution
- unrestricted autonomous Pinterest actions

## 10. UNVERIFIED ITEMS THAT MUST NOT BECOME CUSTOMER INSTRUCTIONS

1. Fully unattended ChatGPT Scheduled Task → Metricool Pinterest publishing with no intervening approval.
2. Any specific image-provider operation that has not been tested through the actual customer-facing ChatGPT workflow.
3. Any customer plan requirement not verified against current OpenAI availability for the customer's account/region.
4. Any Amazon API capability that is not explicitly supported by the customer's current Creators API access.

## 11. BUILD ORDER

1. Update setup requirements.
2. Update setup prompt.
3. Replace Claude scheduled-task prompts with ChatGPT Work prompts.
4. Replace browser-based Pinterest publishing with the TIME-SAVING Metricool path and CREDIT-SAVING native path.
5. Replace markdown-only state with structured IDs/state.
6. Update pull/recovery logic.
7. Update Amazon intake language to reflect Creators API as the current API path without requiring it.
8. Update customer guide.
9. Regenerate ZIP.
10. Run end-to-end test for both publishing paths.
11. Only after successful tests, mark the corresponding capability VERIFIED in the customer guide.

## 12. SOURCE PRIORITY

When customer files conflict:
1. This canonical architecture
2. Current official provider documentation
3. Current implementation files
4. Human-readable guide

Never silently preserve an older customer instruction when it conflicts with this architecture.
