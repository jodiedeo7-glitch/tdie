# Amazon setup capability test - 6 October 2026

Scope: Step 3 and capability checks in 02_SETUP_PROMPT.txt, after verified board completion. This is not a complete sourcing, publishing or unattended test. Account evidence remains local outside the customer kit.

## Verified tests

- Current official storefront and one existing six-product test Idea List loaded while signed out. Exact destination and displayed contents were read; this proves existing destination readback only.
- After customer sign-in, the matching storefront exposed Create content, Manage content and SiteStripe. The owner Idea List form and Add products dialog were accessible. The form requires at least two products. No new list was submitted.
- SiteStripe displayed the account's selected Store ID and Tracking ID, but its Copy affiliate link action returned empty through the supported browser clipboard reader. That route remains unverified.
- Supported alternative: the official storefront Share Popup exposed Amazon-generated sharing hrefs containing its actual tagged destination URL. Read and decoded that supplied destination without clicking a social/email submission. Storefront link capture passed in this bounded interactive route.
- Owner-view Idea List links showed an onsite tag different from the offsite tag supplied by the sharing UI. No tag was guessed or constructed. Storefront-link capture is separate from Idea List/product-link generation.
- The settled Creators API Applications page displayed no existing applications and offered Create App. The older Product Advertising API menu redirected to that same page. The customer approved application and credential creation. A name containing spaces was rejected; the valid hyphenated name WYS-Storefront-Capability-Test was accepted and read back.
- Credential incident: the first generated secret was inadvertently exposed once in tool output before any API use. The customer specifically approved permanent revocation and replacement. The exposed credential was deleted, and a fresh page reload showed it absent with the application retained. The replacement was generated, stored using authenticated encryption with a Windows CurrentUser-protected private key and verified ACTIVE after reload. Required fields and encrypted-storage decryption were verified without displaying replacement values. No credentials are included in tracked files.
- Replacement authentication passed against Amazon's documented North America token endpoint (HTTP 200). A controlled two-ASIN GetItems request returned HTTP 403 with AssociateNotEligible and AccessDenied. No catalog products were returned, so catalog sourcing has not passed.
- The existing test Idea List's official Share Popup exposed an Amazon-generated destination with the selected offsite tracking tag. Read the visible href without sending a social/email share, then opened the exact supplied Amazon destination and verified the matching title and six items. Existing Idea List link capture and destination readback passed in this bounded interactive scope. No list was created or changed.

## Pending tests and concrete continuation

- Catalog eligibility remains unverified during the new-credential review window. The live official page permits up to 48 hours for access review and warns of AssociateNotEligible during that period. Replacement creation: 2026-10-06 06:40:53 UTC; review deadline: 2026-10-08 06:40:53 UTC (2:40:53 a.m. America/New_York). Next API action: reuse the encrypted replacement for one catalog request after that window. A later check has not been scheduled. If the error persists then, check the current requirement of ten qualifying sales in the trailing thirty days and the available permitted alternative; do not create another key as an eligibility fix.
- Product discovery, variant qualification, individual-product link generation/capture and Idea List create/update still require their own permitted tests and readbacks. Existing Idea List sharing/readback has passed only the scope recorded above. An accessible unsaved form does not pass a write, and catalog API access does not pass Idea List writes. The customer has been offered a browser test of a specifically named two-product list or exact manual steps to save credits; no list write was performed while awaiting that choice.
- Recurring/cloud use remains a separate capability. Customer-directed interactive reads do not establish unattended permission or runtime availability.

## Flow defect repaired

The browser copy action provided no readable clipboard result, while another supported visible sharing route did expose the generated link. Step 3 now requires exact link capture and account/tag verification, tests alternate visible output before a manual handoff and distinguishes scope. It forbids guessing tags/links or taking the signed-in owner URL as an offsite Special Link.

This continuation exposed application-name validation, secret-bearing browser output and a gap between provisioning/authentication and actual catalog access. Step 3 now validates application names, requires secure capture before credential generation, excludes secret-bearing observations from output/proof, provides incident recovery and handles the provider review window with a precise retry and independent checks. The automatic contract preserves these distinctions. These are source repairs, not additional capability passes.

No scheduled Pins were mutated. The approved test application and replacement credential were created; no external shares or Idea Lists were created. Source changes do not certify delivery ZIP/PDF contents or release readiness.

## Official sources checked

- [Creators API introduction](https://affiliate-program.amazon.com/creatorsapi/docs/en-us/introduction): documented catalog operations and eligibility prerequisites.
- [Using cURL](https://affiliate-program.amazon.com/creatorsapi/docs/en-us/get-started/using-curl): regional authentication, GetItems requests and credential handling.
- [Amazon Associates program policies](https://affiliate-program.amazon.com/help/operating/policies): program-content license and applicable access limitations.
- Authenticated official Amazon storefront, SiteStripe, Idea List creation form and Associates Central Tools pages; exact account observations saved locally.
