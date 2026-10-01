# Storefront release checks

Verified September 30, 2026. Times are America/New_York.

## Buyer files passed

- Member listing 36b6f2a8-d26b-4e03-9fa5-b4b698fcf84f has one 44.76 KB ZIP. Its actual configured download matches the finished buyer package.
- Public listing a2e4f613-9431-4fd0-ad76-84415e14aa39 has one corrected 3.15 KB presale PDF. The old 417.88 KB PDF is absent after reload.
- Downloaded presale SHA-256: F302FABCB866FA7FA9BE1185A68DBD18C988C479ACB760EB8F2E221E16EA4480, matching the approved local file.

## Release timing remains a failure

- Public listing says presale opens October 5 at 7 pm and ends October 8 at 11:59 pm. Full delivery is planned October 9 at 9 am.
- On September 30 the direct public link already opens a live $10 card checkout. The written opening date is not an enforced gate.
- Inspected controls: Coming soon is a manual waitlist switch; fixed pricing has no date fields. No automatic open/close or future file replacement was verified.
- Do not claim an automated release is configured. No future automation was created.

## Concrete release actions

1. Before October 5: decide whether direct-link early purchasing is intentional. If it is not, enable Coming soon for the public product and verify the checkout is replaced by the waitlist. This needs an explicit launch-state decision because it affects existing direct links.
2. October 5 at 7 pm: turn Coming soon off if used, confirm the current $10 presale price, one-page note and working checkout, then expose the intended sales link.
3. October 8 at 11:59 pm: close the presale window as intended and verify the change. Do not guess the next public price; recheck current TDIE canon and approved offer.
4. October 9 at 9 am: replace the public product's presale attachment with the finished two-PDF ZIP, then verify both new and existing buyer receipt/customer-portal access. Keep the product identity and customer access route intact.

## End-to-end order remains unverified

Checkout, file endpoints and receipt previews were inspected; no order or email was submitted. Actual payment, receipt delivery and customer portal access need a test order. Use a specifically authorized spending limit or a one-use free test route and a user-designated recipient. Beacons help states content-access links are active for 7 days after purchase; verify the actual receipt and resend path rather than promising permanent receipt URLs.

Official delivery reference: https://help.beacons.ai/en/articles/4699713

Other open audit items: Cloudflare deployment, withdrawn October 7 Metricool date (automatic publishing off), scheduled-runtime state persistence and complete approved production run. These are separate from passed buyer-file integrity checks.
