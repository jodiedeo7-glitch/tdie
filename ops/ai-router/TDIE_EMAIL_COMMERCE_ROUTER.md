# TDIE Email + Commerce Router V2

## Founder correction — 30 September 2026

**Find Your Door is no longer automated.** It must not be counted as a MailerLite automation, given a scheduled task, or assigned an automated follow-up sequence. Keep the free on-site routing resource distinct from email automations. Any optional email form or site API integration is a separate technical feature and is not evidence that a quiz email automation is active.

## Source-of-truth rule

The repository documents MailerLite's active/inactive automation configuration as of 19 September 2026. That is historical evidence, **not live account verification**. Before any migration, Claude must read back the current MailerLite account and Beacons configuration. Never disable, pause, or replace an active delivery automation based solely on the repo.

## ChatGPT owns
- offer-to-email mapping and funnel design
- subject lines, campaign copy, and exclusion rules
- buyer delivery requirements
- automation inventory analysis and capacity planning
- QA packet and approval checklist

## Claude owns
- live MailerLite inventory and status read-back
- Beacons product/checkout inventory read-back
- configuring approved campaigns and automations
- test purchases or test subscriber flows only with founder authorization
- verifying that buyers receive promised access
- recording actual platform state

## Codex owns
- website email capture and API integration code
- deterministic tests
- non-secret configuration templates

## Required gates
1. Export/read current live MailerLite automation list, statuses, triggers and audiences.
2. Verify live Beacons checkout products, access/delivery and discount settings.
3. Crosswalk each purchase or signup event to its existing email/delivery action.
4. Flag missing delivery, duplicated sends, unwanted promotions to buyers and unapproved automation.
5. Propose changes for approval before making them.
6. Run controlled verification and log results.

## Explicit exclusions
- No Find Your Door email automation.
- No resurrecting the previous five-workflow proposal.
- No assumption that a form/API endpoint means a scheduled campaign or automation exists.
- No modification of Daily Prompts, Premium DFY Content Calendar or customer Storefront automation from this queue.
