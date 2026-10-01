# TDIE website / repo router V2

The uploaded snapshot records Astro on Vercel. Confirm the current host and deployment configuration before any release; do not overwrite a newer migration. No browser task should be used for bulk code or content edits that belong in the repo.

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
