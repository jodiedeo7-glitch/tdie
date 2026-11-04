> **WYS authority, 7 October 2026:** [Read the complete WYS master](https://github.com/jodiedeo7-glitch/tdie/blob/main/claude/WYS_REFERENCE_PACK_2026-10-07.md). It is the sole active WYS workflow. This shared document cannot supply WYS generation defaults or override its current three-image prompts, pause or release hold. SOP-15/SOP-16 and unrelated systems retain their own authority.

# TDIE website / repo router V2

Hosting is Cloudflare (worker `tdie-site`), deployed from the `cloudflare-migration` branch. Vercel is retired (ChatGPT migrated the site after the Vercel free tier ran out of space). Do not overwrite the Cloudflare setup. No browser task should be used for bulk code or content edits that belong in the repo.

## ChatGPT
CRO, information architecture, copy, QA criteria, release packet.

## Codex
Implement approved changes on a feature branch, run build/tests, inspect diff, and prepare review. Never push to main or alter pricing/launch gating without approval.

## Claude
Read-only live checks for checkout buttons, logged-out site, mobile layout, live offers and Skool/Beacons destination verification. Browser edits are only for external account settings that cannot be implemented in the repo.

## Safety
- Source of truth: current live site and current GitHub main override the September 28 uploaded ZIP.
- Check `ops/canon/canon.json` for approved offer metadata and launch gates.
- Never open Storefront presale before its release gate; do not replace approved live checkout URLs with placeholders.
- Do not alter newsletter/RSS routing without verifying the article-index and date-map dependencies documented in README.md.
- Never claim a deployed change without live read-back.
