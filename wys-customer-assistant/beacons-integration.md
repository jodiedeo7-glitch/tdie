# Beacons purchase verification evidence (9 October 2026)

Authenticated creator dashboard: @thedigitalincomeedit, inspected read-only via signed-in browser.

WYS products:
- Public product ID: `66271fb0-fc54-4aae-ad9f-c826f4635ee7`
- Member product ID: `36b6f2a8-d26b-4e03-9fa5-b4b698fcf84f`

Recent Sales view showed free downloads, no confirmed WYS purchases among the five inspected rows. This does not establish that there are zero WYS purchases in full history.

Observed: Store Settings supports email/push alerts for new downloads and sales. Email Marketing has a post-purchase sequence. No order webhook, API, or Zapier connector was observed in this account; this does not prove none exists.

**Security:** Never use an email alert, guessed email address, free download, or customer-supplied receipt alone as proof of purchase. The founder's existing release hold stays in force.

**Integration decision pending verification:** Inspect whether the payment processor offers a verified signed order event containing exact Beacons product IDs. If unavailable, use an operator-confirmed entitlement flow with independent transaction verification. Never auto-grant access on unverified input.

**Customer test gate:** Confirm buyer order for the matching WYS product, verify payment status, provision scoped access, complete wizard, resume saved preferences, deny nonbuyers, and validate isolation. No production credentials or customer personal data in repository.
