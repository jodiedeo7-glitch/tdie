# PINK FINDS GROWTH PLAN (copy for cloud sessions)

Copy of the project doc `claude/TDIE_PINK_FINDS_GROWTH_PLAN.md` (25 Sep 2026), placed here 26 Sep 2026.

## Where it stands (25 Sep 2026)
- MailerLite group "Lifestyle Pink Finds" (form 199525394616943647): 0 subscribers. Whole MailerLite account: 70 active subscribers. Free plan, all 3 automation slots used, so there is no welcome email; the Friday email is a regular campaign.
- Storefront traffic: 2 clicks, no earnings (24 Sep). Pinterest's Legally Blonde board is the one channel with reach (15.42k of 23k monthly impressions) but pins can't link to the site (domain block).
- Target reader: women who already shop a lot on Amazon and buy by the look: costume and party shoppers, dorm and apartment decorators, gift buyers. Not business builders.

## The offer
- Evergreen: "New pink finds, every Friday." One email, Friday, unsubscribe any time.
- Pushes, same shape: Prime Big Deal Days (6 and 7 Oct 2026, live now), Halloween last call (week of 19 Oct), Black Friday and Cyber Monday gift guides (27 and 30 Nov), Christmas gift guide. Each push gets its own form headline, a real date, and the send that keeps the promise. No invented deadlines or discounts, ever.
- Emails link only to thedigitalincomeedit.com/lifestyle pages, never to Amazon (Amazon Associates rules ban affiliate links in email).

## What's live in the repo
- Signup page: `src/pages/lifestyle/pink-finds.astro` (https://www.thedigitalincomeedit.com/lifestyle/pink-finds). Headline "Your cart is already pink. Let's make it good."
- Forms: `src/components/PinkFindsSignup.astro`, placed under the intro on the hub and category pages, under "Shop every piece on Amazon" on every look page, and at the bottom.
- Copy and push dates: `src/data/pinkfinds.js` (`PRIME_END` switches the Prime copy back to evergreen at 6 Oct 2026, 9 am ET). To run a new push, change the copy and the end date there; every form updates.
- Thank-you line: "You're in. Your first pink finds land in your inbox this Friday."
- Meta Pixel fires a Lead event "Pink Finds" on every signup.

## Channels
Lifestyle pages (forms) · @itstommykate Instagram (captions point to the link in bio, one extra daily story with a link sticker to /lifestyle/pink-finds) · existing 70 subscribers (invite on 1 Oct) · TDIE Facebook group, 4.6K (posts 1 and 4 Oct, link in first comment) · Friday email forward-to-a-friend line · Pinterest reach only.

## Goals (targets, not forecasts)
50 subscribers by 7 Oct 2026; 250 by 30 Nov 2026 (Cyber Monday); open rate 35%+; click rate 5%+.

## Rules
No em dashes. No invented discounts, prices or deadlines; deal claims only when Amazon shows the deal at send time. Emails never link to Amazon. Pages carry the Amazon disclosure. Instagram: no links except story stickers. Facebook: link only in the first comment. Every send's footer says the looks are styled on an AI model. Sign off "Jodie"; never "Warmly". Paid Meta ads only with Jodie's go.
