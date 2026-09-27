# Canon rows: DRAFT, not registered

Written 27 Sep 2026. **Nothing here is in canon yet.** The desktop finish (queue section 4, step 4) pastes these into `canon.json` and `TDIE_CANON.md`, in both the project and the repo, on the same day, before any Beacons product is created. Steps 5 and 7 then replace each `pending: ...` address with the real one, the same day, in both copies.

## Founder decisions recorded here (27 Sep 2026)

1. **Canon rows first.** Canon's Product Register rule wants a row before any asset. The kit, copy and sales page were written as drafts in a cloud session; the desktop finish adds these rows as its first account step (step 4), before any Beacons product exists and before anything is published, scheduled or merged. The Beacons addresses do not exist yet at that step, so the rows go in with the text `pending: set in finish step 5, same day` in the address fields, and step 5 writes the real addresses into both copies the same day.
2. **The vault question (the numbered decision below, "vault_member_pricing").** Founder call, 27 Sep 2026: The While-You-Sleep Storefront™ is a standalone product, not a vault guide. It appears as one member-pricing lesson in BOTH vaults, so the two vaults still hold identical lessons and only how each tier pays differs. The Value Vault lesson links the private $17 product; The Premium Vault lesson links the same $17 product plus the 50% code. Premium pays half, not nothing: a scoped exception to "every guide already unlocked in The Premium Vault". It is never flagged as a vault defect.

Also noted, not a defect: The Value Vault course is Open by design (Decision 95), so the lesson holding the $17 link is reachable by non-members. The $17 product stays hidden on Beacons (never on the storefront or the link in bio). Decision 95 is not reopened.

---

## `canon.json → products[]` (insert in price order, after the $27 rows)

```json
{
  "name": "The While-You-Sleep Storefront™",
  "price": 27,
  "display": "$27 one-time on Beacons. Presale $10 for everyone (4 days). Membership Standard members $17 through a private Beacons product. Membership Premium members $8.50 with code PREMIUM50 on the member product.",
  "recurring": false,
  "owned": true,
  "platform": "Beacons",
  "url": "pending: set in finish step 5, same day",
  "member_product": {
    "price": 17,
    "url": "pending: set in finish step 5, same day",
    "visibility": "Hidden on Beacons. Never on the storefront or the link in bio. Linked only from the Value Vault lesson and the Premium Vault lesson."
  },
  "premium_code": {
    "code": "PREMIUM50",
    "discount": "50% off the $17 member product ($8.50)",
    "where": "Only in the Premium Vault lesson. Never in public copy, a Skool post, an email or a Beacons description."
  },
  "value_vault_lesson": "pending: set in finish step 7, same day",
  "premium_vault_lesson": "pending: set in finish step 7, same day",
  "presale": "$10 for everyone, Mon 5 Oct 2026 7:00 pm to Thu 8 Oct 2026 11:59 pm Eastern (founder dates, 27 Sep 2026). Public $27 and member $17 from Fri 9 Oct 2026 9:00 am Eastern. The presale product is the public product, repriced at launch; its presale file is a one-page note swapped for the full kit on launch morning.",
  "sales_page": "https://www.thedigitalincomeedit.com/shop/while-you-sleep-storefront",
  "affiliate": "Member affiliate program, 40%, Beacons affiliate product. See own_affiliate_programs.while_you_sleep_storefront.",
  "refunds": "None. Stated once, on the sales page.",
  "upgrade": "DFY Amazon Storefront Launch ($297) is the done-for-you upgrade named at the end of the kit.",
  "note": "Standalone product, never included free in any tier. Working name. A copy-paste kit that turns Jodie's two Amazon pin automations (the themed-look line built on claude/TDIE_LEGALLY_BLONDE_PIN_FACTORY.md and the Brand Closet™ Outfit of the Day line built on claude/TDIE_BRAND_CLOSET_PIN_FACTORY.md) into a buyer's own: setup prompt, two recipes, four scheduled task prompts (including a daily missed-run sweep), persona and storefront paths, the blog half for Weekend Ecosystem™ sites, an optional Instagram add-on and a setup PDF. Proof is the machine: 15 looks, 15 Idea Lists, 15 live /lifestyle pages, 84 tagged links, 26 pins built (27 Sep 2026 log). Never a sales, commission or income claim: the storefront had 2 clicks and no earnings at the 24 Sep 2026 check. Not a vault guide: it appears as one member-pricing lesson in both vaults (see meta vault_member_pricing). Kit files: ops/cloud-output/storefront-product/kit/."
}
```

## `canon.json → own_affiliate_programs` (new key)

```json
"while_you_sleep_storefront": {
  "status": "LIVE from launch (Mon 5 Oct 2026, 9:00 am Eastern) once turned on in Beacons at the desktop finish.",
  "commission_percent": 40,
  "product_price": 27,
  "cap": "none",
  "application": "none",
  "link": "pending: set in finish step 5, same day",
  "mechanic": "Same as own_affiliate_programs.weekend_ecosystem.mechanic: one link, identical for every member, added in her own Beacons account (add a digital product, choose affiliate product, paste the link). Beacons issues her own tracked link. There is no reply-for-a-link step.",
  "meta_rule": "The 40% figure is permitted on Skool, Threads, email and the kit. Never on Facebook or Instagram, and never on the sales page (it carries the Meta Pixel).",
  "not_a_pack_cta": "Member-promotion link. Never fills the affiliate slot in a Repurposing Pack."
}
```

## `canon.json → vault_disambiguation` (new key)

```json
"standalone_member_pricing": "Decision [next number + 1] (meta vault_member_pricing). A standalone product can appear as one member-pricing lesson in BOTH vaults without being a vault guide. The While-You-Sleep Storefront™ is the first: The Value Vault lesson links the private $17 product, The Premium Vault lesson links the same $17 product plus code PREMIUM50 (50% off). The two vaults still hold identical lessons; only how each tier pays differs. Premium pays half, not nothing: a scoped founder exception to 'every guide already unlocked in The Premium Vault'. Never flagged as a vault defect, an audit finding or a pricing conflict."
```

## `canon.json → meta` (new key)

```json
"while_you_sleep_storefront_DATE": "Decision [next number]. Founder instruction, 27 Sep 2026: Jodie's two Amazon pin automations become one standalone product, The While-You-Sleep Storefront™ (working name). Presale $10 for everyone, Mon 5 Oct 7:00 pm to Thu 8 Oct 11:59 pm Eastern, then $27 one-time on Beacons from Fri 9 Oct 9:00 am. Membership Standard $17 through a private Beacons product linked only from a Value Vault lesson. Membership Premium: code PREMIUM50, 50% off the member product ($8.50), shown only in a Premium Vault lesson. Member affiliate 40% via Beacons' affiliate product. Zero refunds, stated once. Never included free in any tier. Upgrade: DFY Amazon Storefront Launch ($297). Registered at the desktop finish."
```

```json
"vault_member_pricing_DATE": "Decision [next number + 1]. Founder call, 27 Sep 2026. The While-You-Sleep Storefront™ is a standalone product, not a vault guide. It appears as one member-pricing lesson in BOTH The Value Vault and The Premium Vault, so the two vaults still hold identical lessons and only how each tier pays differs: The Value Vault lesson links the private $17 Beacons product; The Premium Vault lesson links the same $17 product plus code PREMIUM50 (50% off, $8.50). Premium pays half, not nothing. This is a scoped exception to 'every guide already unlocked in The Premium Vault' and is never re-raised as a vault defect, an audit finding or a pricing conflict. Closed item."
```

When pasting: replace `DATE` in both keys with the finish date (`YYYY_MM_DD`), `[next number]` with the next free decision number in canon.json `meta`, and `[next number + 1]` with the one after it.

---

## `TDIE_CANON.md` (§5 PRODUCTS, new paragraph after The Keep It Running Kit)

**The While-You-Sleep Storefront™ (Decision [next number], founder instruction 27 Sep 2026, working name).** A standalone copy-paste kit that turns Jodie's two Amazon pin automations into a buyer's own: Amazon links to Pinterest pins to an optional shop-the-look section, built and scheduled by the buyer's own Claude scheduled tasks. **$27 one-time on Beacons**, after a **$10 presale** for everyone (Mon 5 Oct 7:00 pm to Thu 8 Oct 11:59 pm Eastern; public price from Fri 9 Oct 9:00 am). Membership Standard members pay **$17** through a private Beacons product linked only from a Value Vault lesson; Membership Premium members use code **PREMIUM50** (50% off, $8.50), shown only in a Premium Vault lesson and never in public copy. It is never included free in any tier, and it is not a vault guide: it appears as one member-pricing lesson in both vaults, so the vaults still hold identical lessons and only how each tier pays differs. Premium pays half, not nothing: a scoped founder exception to "every guide already unlocked in The Premium Vault" (Decision [next number + 1], 27 Sep 2026), never flagged as a vault defect. Member affiliate program **40%** through Beacons' affiliate product (one shared link, no reply step); the rate never appears on Facebook, Instagram or the sales page. Zero refunds, stated once on the sales page. Upgrade: DFY Amazon Storefront Launch ($297). Proof is the machine only, never sales or income. Sales page `/shop/while-you-sleep-storefront`. Row: `canon.json → products[]`.

And in §2 STANDING FACTS, add nothing: the product does not change a standing fact.
