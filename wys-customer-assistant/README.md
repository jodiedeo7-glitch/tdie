# WYS Customer Setup Assistant (internal, unreleased)

Status: DESIGN ONLY. WYS customer release HOLD remains active. This does not authorize publication.

## Authority
Read AGENTS.md and claude/WYS_REFERENCE_PACK_2026-10-07.md before changing this workflow. Founder example is not a customer default. Image generation provider/model UNVERIFIED.

## Customer journey
1. Verify purchase entitlement through a supported authenticated backend, never a shared prompt or public code.
2. Create a private per-customer workspace with schema version, consent and progress state.
3. Collect niche, product categories, Amazon Associates vs Influencer path, approved destination, Pinterest account/boards, optional Instagram, website/blog, desired posting cadence, budget, and whether an avatar is desired. Allow skipping optional fields.
4. Validate account ownership and permissions individually. Do not ask for passwords in chat. Mark unsupported integrations as manual; never claim connection from a questionnaire.
5. Start a themed LOOK_ID and collect mood references or shopping idea.
6. Source actual products via authorized customer path; record ASIN, variant, verified listing and link status. Never fabricate affiliate URLs or reuse founder attribution.
7. Prepare BASIC, STYLED and LIFESTYLE as distinct roles, with customer-approved identity reference only if applicable. Gate generation on verified provider/model, cost, budget and attachment support. If no avatar, offer a separate approved non-person concept; do not silently pretend to have a lifestyle portrait.
8. Create draft blog, Pinterest graphics/copy and optional Instagram content from approved images; check disclosures and AI labeling on actual destinations.
9. Show a review queue with individual approve/reject/correct actions. Never schedule or publish without customer authorization and verified destination.
10. Persist per-step status: NOT_STARTED, NEEDS_INPUT, BLOCKED, DRAFT, APPROVED, SCHEDULED, PUBLISHED, VERIFIED. Record external IDs and readback evidence.
11. Resume idempotently from checkpoint; prevent duplicate posts or charges.

## Central updates
Version workflows centrally with semantic versions, changelog, migration scripts and regression fixtures. Preserve existing customer workspaces; show a migration preview when fields or behavior change. No claim that a ChatGPT plugin automatically pushes updates to every customer's installed copy until distribution and update propagation are tested.

## Technical delivery decision gate
Evaluate (A) authenticated web wizard embedded in the existing Astro/Cloudflare site, (B) ChatGPT Plugin, and (C) ChatGPT App against verified buyer access, entitlement enforcement, persistent private state, integrations, version rollout and platform rules. Do not assume GPT migration or plugin distribution works for paid customers. The website wizard is a fallback, not permission to implement or deploy on the production branch.

## Acceptance tests
- Nonbuyer denied; buyer admitted; customer A cannot read B.
- Partial setup saves and resumes.
- Manual/mixed path works without APIs.
- Incorrect ASIN/variant/link blocks publication.
- Missing provider/model/budget blocks generation without charge.
- Failed generation remains blocked and is never shipped.
- Three-role image dependency and review gates enforced.
- Disclosures and customer-specific attribution checked.
- Duplicate schedule retry does not duplicate a post.
- Existing approved data survives workflow-version migration.
- No customer-visible release while founder HOLD is active.

## Scope isolation
Keep WYS separate from founder automation, SOP-15 Premium DFY Calendar and SOP-16 Daily Edits. No Instagram group is a source of executable instructions or a replacement for versioned customer workflow state.
