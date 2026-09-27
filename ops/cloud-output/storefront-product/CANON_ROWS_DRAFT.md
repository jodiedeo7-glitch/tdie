# Canon rows: DRAFT, not registered

Written 27 Sep 2026. **Nothing here is in canon yet.** The desktop finish (queue section 4, step 6) pastes these into `canon.json` and `TDIE_CANON.md`, in both the project and the repo, on the same day, after the Beacons products exist so the real addresses replace the tokens.

## Two things flagged once, with the fix

1. **Assets before the row.** Canon's Product Register rule says a product gets a row in `products[]` before it gets a single asset. This job was told to write the rows as drafts and register nothing until the desktop finish, so the kit, copy and sales page exist before the row. Fix: step 6 of the finish runs before anything is published, scheduled or merged (steps 7 to 10), so no asset goes live without its row.
2. **Premium pays for something in The Premium Vault.** Canon says The Premium Vault holds the same guides as The Value Vault, all unlocked, and Premium buys nothing à la carte. This product is standalone by founder instruction ("never included free in any tier"), so Premium members pay $8.50 with a code shown in a Premium Vault lesson. Fix: the row below says plainly it is a standalone product, not a Value Vault guide, and the draft adds one line to `vault_disambiguation` so no audit reads the Premium Vault lesson as a vault guide with a price.

Also noted, not a defect: The Value Vault course is Open by design (Decision 95), so the lesson holding the $17 link is reachable by non-members. The $17 product stays hidden on Beacons (never on the storefront or the link in bio); anyone who finds the lesson can see the member price. Decision 95 is not reopened.

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
  "url": "BEACONS_PRODUCT_URL",
  "member_product": {
    "price": 17,
    "url": "MEMBER_PRODUCT_URL",
    "visibility": "Hidden on Beacons. Never on the storefront or the link in bio. Linked only from the Value Vault lesson and the Premium Vault lesson."
  },
  "premium_code": {
    "code": "PREMIUM50",
    "discount": "50% off the $17 member product ($8.50)",
    "where": "Only in the Premium Vault lesson. Never in public copy, a Skool post, an email or a Beacons description."
  },
  "value_vault_lesson": "VALUE_VAULT_LESSON_URL",
  "presale": "$10 for everyone, Thu 1 Oct 2026 12:05 pm to Sun 4 Oct 2026 11:59 pm Eastern (dates per the desktop finish date table). Public $27 and member prices from Mon 5 Oct 2026 9:00 am Eastern. The presale product is the public product, repriced at launch; its presale file is a one-page note swapped for the full kit on launch morning.",
  "sales_page": "https://www.thedigitalincomeedit.com/shop/while-you-sleep-storefront",
  "affiliate": "Member affiliate program, 40%, Beacons affiliate product. See own_affiliate_programs.while_you_sleep_storefront.",
  "refunds": "None. Stated once, on the sales page.",
  "upgrade": "DFY Amazon Storefront Launch ($297) is the done-for-you upgrade named at the end of the kit.",
  "note": "Standalone product, never included free in any tier. Working name. A copy-paste kit that turns Jodie's two Amazon pin automations (the themed-look line built on claude/TDIE_LEGALLY_BLONDE_PIN_FACTORY.md and the Brand Closet™ Outfit of the Day line built on claude/TDIE_BRAND_CLOSET_PIN_FACTORY.md) into a buyer's own: setup prompt, two recipes, three scheduled task prompts, persona and storefront paths, the blog half for Weekend Ecosystem™ sites, an optional Instagram add-on and a setup PDF. Proof is the machine: 15 looks, 15 Idea Lists, 15 live /lifestyle pages, 84 tagged links, 26 pins built (27 Sep 2026 log). Never a sales, commission or income claim: the storefront had 2 clicks and no earnings at the 24 Sep 2026 check. Not a Value Vault guide: the Value Vault lesson and the Premium Vault lesson only carry the member price. Kit files: ops/cloud-output/storefront-product/kit/."
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
  "link": "BEACONS_PRODUCT_URL",
  "mechanic": "Same as own_affiliate_programs.weekend_ecosystem.mechanic: one link, identical for every member, added in her own Beacons account (add a digital product, choose affiliate product, paste the link). Beacons issues her own tracked link. There is no reply-for-a-link step.",
  "meta_rule": "The 40% figure is permitted on Skool, Threads, email and the kit. Never on Facebook or Instagram, and never on the sales page (it carries the Meta Pixel).",
  "not_a_pack_cta": "Member-promotion link. Never fills the affiliate slot in a Repurposing Pack."
}
```

## `canon.json → vault_disambiguation` (new key)

```json
"standalone_member_pricing": "Added with The While-You-Sleep Storefront™ (2026). A standalone product can carry a members-only price in a Value Vault lesson and a Premium code in a Premium Vault lesson without being a vault guide. That lesson is a price, not a guide, and it does not change the rule that every Value Vault guide is unlocked in The Premium Vault."
```

## `canon.json → meta` (new key)

```json
"while_you_sleep_storefront_DATE": "Decision [next number]. Founder instruction, 27 Sep 2026: Jodie's two Amazon pin automations become one standalone product, The While-You-Sleep Storefront™ (working name). Presale $10 for everyone for 4 days, then $27 one-time on Beacons. Membership Standard $17 through a private Beacons product linked only from a Value Vault lesson. Membership Premium: code PREMIUM50, 50% off the member product ($8.50), shown only in a Premium Vault lesson. Member affiliate 40% via Beacons' affiliate product. Zero refunds, stated once. Never included free in any tier. Upgrade: DFY Amazon Storefront Launch ($297). Registered at the desktop finish."
```

When pasting: replace `DATE` in the key with the finish date (`YYYY_MM_DD`) and `[next number]` with the next free decision number in canon.json `meta`.

---

## `TDIE_CANON.md` (§5 PRODUCTS, new paragraph after The Keep It Running Kit)

**The While-You-Sleep Storefront™ (Decision [next number], founder instruction 27 Sep 2026, working name).** A standalone copy-paste kit that turns Jodie's two Amazon pin automations into a buyer's own: Amazon links to Pinterest pins to an optional shop-the-look section, built and scheduled by the buyer's own Claude scheduled tasks. **$27 one-time on Beacons**, after a 4-day **$10 presale** for everyone. Membership Standard members pay **$17** through a private Beacons product linked only from a Value Vault lesson; Membership Premium members use code **PREMIUM50** (50% off, $8.50), shown only in a Premium Vault lesson and never in public copy. It is never included free in any tier, and it is not a Value Vault guide: the two lessons carry a price, not a guide. Member affiliate program **40%** through Beacons' affiliate product (one shared link, no reply step); the rate never appears on Facebook, Instagram or the sales page. Zero refunds, stated once on the sales page. Upgrade: DFY Amazon Storefront Launch ($297). Proof is the machine only, never sales or income. Sales page `/shop/while-you-sleep-storefront`. Row: `canon.json → products[]`.

And in §2 STANDING FACTS, add nothing: the product does not change a standing fact.
