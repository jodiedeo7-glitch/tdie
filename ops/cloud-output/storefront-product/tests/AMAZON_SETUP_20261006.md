# Amazon setup capability test — 6 October 2026

Scope: Step 3 and capability checks in 02_SETUP_PROMPT.txt, after verified board completion. This is not a complete sourcing, publishing or unattended test. Account evidence remains local outside the customer kit.

## Verified tests

- Current official storefront and one existing six-product test Idea List loaded while signed out. Exact destination and displayed contents were read; this proves existing destination readback only.
- After customer sign-in, the matching storefront exposed Create content, Manage content and SiteStripe. The owner Idea List form and Add products dialog were accessible. The form requires at least two products. No new list was submitted.
- SiteStripe displayed the account's selected Store ID and Tracking ID, but its Copy affiliate link action returned empty through the supported browser clipboard reader. That route remains unverified.
- Supported alternative: the official storefront Share Popup exposed Amazon-generated sharing hrefs containing its actual tagged destination URL. Read and decoded that supplied destination without clicking a social/email submission. Storefront link capture passed in this bounded interactive route.
- Owner-view Idea List links showed an onsite tag different from the offsite tag supplied by the sharing UI. No tag was guessed or constructed. Storefront-link capture is separate from Idea List/product-link generation.
- The settled Creators API Applications page displayed no existing applications and offered Create App. The older Product Advertising API menu redirected to that same page. Prepared an unsaved application-name form, then requested explicit approval for application and credential creation. No application or credential was created.

## Pending tests and concrete continuation

- New API access decision: customer may approve browser creation of the specifically named test application and credentials, choose manual instructions or leave API setup pending. Credential creation grants new programmatic access and requires explicit confirmation under the browser action rules.
- Catalog eligibility and usable configured API access remain unverified. The official account page and documentation require ten qualifying sales in the trailing thirty days for catalog access; application creation alone does not prove eligibility. Record the actual supported API result after any authorized connection.
- Product discovery, variant qualification, Idea List/product link capture and Idea List create/update still require their own permitted tests and readbacks. An accessible unsaved form does not pass a write, and catalog API access does not pass Idea List writes.
- Recurring/cloud use remains a separate capability. Customer-directed interactive reads do not establish unattended permission or runtime availability.

## Flow defect repaired

The browser copy action provided no readable clipboard result, while another supported visible sharing route did expose the generated link. Step 3 now requires exact link capture and account/tag verification, tests alternate visible output before a manual handoff and distinguishes scope. It forbids guessing tags/links or taking the signed-in owner URL as an offsite Special Link.

No scheduled Pins were mutated. No API credentials, external shares or Idea Lists were created. Source changes do not certify delivery ZIP/PDF contents or release readiness.

## Official sources checked

- [Creators API introduction](https://affiliate-program.amazon.com/creatorsapi/docs/en-us/introduction): documented catalog operations and eligibility prerequisites.
- [Amazon Associates program policies](https://affiliate-program.amazon.com/help/operating/policies): program-content license and applicable access limitations.
- Authenticated official Amazon storefront, SiteStripe, Idea List creation form and Associates Central Tools pages; exact account observations saved locally.
