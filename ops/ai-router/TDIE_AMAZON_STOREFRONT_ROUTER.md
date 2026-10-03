# TDIE Amazon + While-You-Sleep Storefront Router

## Purpose

Keep these THREE systems separate:

1. **JODIE_INTERNAL_AMAZON** — Jodie's own themed-look / Amazon / Pinterest production.
2. **BRAND_CLOSET_INTERNAL** — Jodie's own Brand Closet™ Outfit of the Day production.
3. **WYS_CUSTOMER_PRODUCT** — the sellable While-You-Sleep Storefront™ workflow buyers receive.

Never copy internal account state, private logs, private URLs, private task IDs, or Jodie's execution queue into the customer product.

---

## Routing rule

### ChatGPT owns
- product architecture
- buyer-path logic
- setup copy
- scheduled-task prompt design
- creative strategy
- product-selection framework
- Pinterest copy frameworks
- compliance review
- buyer simulation / QA
- documentation
- deciding what should be automated versus manual
- live Google Drive production-state reads and writes when the connected Drive action supports them
- live Metricool reconciliation, draft/schedule writes and read-back when the connected Metricool action supports the exact operation
- Higgsfield generation, cost preflight, deterministic post-processing, media filing and generation read-back
- Canva asset filing and supported design operations
- GitHub runbooks, queues and migration state

### Capability-first live execution
ChatGPT is the preferred operator for every step exposed by a connected, read-back-capable service. Claude is not the default merely because an older recipe named Claude.

Browser-only actions remain with the currently available authorized browser/computer-use operator until ChatGPT has a supported route to that exact account action:
- signed-in Amazon product qualification
- SiteStripe link capture
- Amazon Idea List creation/editing
- native Pinterest composer/scheduled-page read-back when Metricool cannot perform the required operation
- Brand Closet/Skool lesson reads when no connected source exposes the lesson
- browser-lock operations that exist only in the legacy Command Centre

Do not duplicate a writer across ChatGPT and Claude. Reconcile first, then use exactly one operator for each external write.

### Gemini / Higgsfield owns
- product-inspired lifestyle scenes
- persona imagery where the selected path requires it
- final photographic generation only

### Codex owns
- site/blog implementation
- JSON/content-file writes
- repo code changes
- deterministic validation

---

# Internal workflow A — Jodie's themed Amazon looks

## ChatGPT
Produces a run packet:
- theme
- product requirements
- search constraints
- board
- pin concepts
- overlay copy
- title/description/alt text templates
- image-generation prompts
- date/slot plan

Browser execution is used only when the active ChatGPT environment exposes a supported computer-use/browser route. Otherwise the packet stops before the browser-only step without fabricating completion.

## Live operator
ChatGPT executes every connector-supported step directly. The active browser/computer-use operator handles only the browser-only remainder:
1. acquire the legacy browser lock when the browser route requires it
2. verify target boards are public when that cannot be independently read through a connected service
3. browse Amazon normally
4. choose qualifying products
5. obtain affiliate links with SiteStripe
6. create/update the required Amazon list
7. hand the verified product packet back to ChatGPT for generation/copy/QA when possible
8. use Metricool through ChatGPT for Pinterest scheduling when it supports the required board, media, disclosure, approval and read-back behavior; otherwise use native Pinterest
9. verify the owning service
10. update the production run log
11. release the browser lock

The live operator does not redesign strategy during execution.

---

# Internal workflow B — Brand Closet™ OOTD

## ChatGPT
Owns:
- content interpretation rules
- creative angle
- copy framework
- QA rules
- prompt design
- backlog policy

## Live operator
ChatGPT owns generation, copy, QA, reconciliation and any connected-service writes. The browser-only operator owns only the steps not exposed to ChatGPT:
- open the correct Brand Closet lesson
- read the current outfit
- capture only the allowed source material
- create Jodie's own Amazon links

After source capture, ChatGPT should resume the run, generate/finalize imagery through approved connected image services, schedule through Metricool when it satisfies the exact publishing requirements, verify through the owning service, and log the lesson immediately to prevent duplicates.

Important:
- never use Rose's affiliate links
- never post Rose's images
- never treat Benable text or ASINs as Jodie's Amazon source
- public boards only

---

# Customer product — While-You-Sleep Storefront™

This is a PRODUCT, not Jodie's private automation.

## Product design owner
ChatGPT.

## Buyer setup/execution
Claude, ChatGPT Work, or another capable browser/computer-use agent may execute the buyer prompts if the buyer chooses the time-saving path.

The product must remain platform-neutral enough that a buyer can also complete the same steps manually.

## Two paths stay explicit

### TIME-SAVING
AI prepares repetitive downstream work and browser execution handles live account steps.

### CREDIT-SAVING
Buyer completes image generation, link collection, Pinterest creation and scheduling manually.

### MIXED
Automate only the portions the buyer wants.

Never imply that browser automation is mandatory.

---

# Hard boundary

The customer kit MUST NOT contain:

- Jodie's task trigger IDs
- Jodie's board names unless used purely as labeled examples
- Jodie's private browser lock state
- Jodie's Amazon storefront IDs
- Jodie's Idea List IDs
- Jodie's Skool private URLs
- Jodie's command-centre documents
- Jodie's private run logs
- Jodie's private affiliate links
- internal desktop-finish instructions
- instructions that assume Claude specifically unless clearly labeled as a Claude example

The kit may contain generic templates and example values.

---

# QA gate before customer release

Every version must pass:

1. Influencer + persona buyer
2. Associates-only + no persona buyer
3. Own-site buyer
4. Brand Closet™ member buyer
5. manual-path buyer
6. mixed-path buyer

For each:
- setup completes
- destination works
- disclosure is correct for that path
- pin copy fits limits
- no duplicate scheduling
- no browser-lock collision
- no private Jodie data appears
- manual alternative exists wherever browser automation is optional
- the buyer can understand exactly what happens automatically and what does not

---

# Verification ownership

**The owning external service verifies live account actions through independent read-back.**

**ChatGPT executes and verifies logic, documentation, copy, product architecture, consistency, connected-service writes and connected-service read-back. Browser-only actions require a second read-back from the owning service before they are marked complete.**

**Codex/tests verify files, schemas, code and deterministic checks.**

A single tool should never self-approve the same step it both designed and executed when a second verification method is available.


---

## Global operator-fit preflight — founder rule, 2 October 2026

Before starting any TDIE task, first determine which available operator can complete that exact task most accurately and completely using the required sources, accounts, browser/computer-use capabilities, connectors, local files and customer-facing workflow.

- If Claude can complete the task better than ChatGPT, STOP before execution and tell Jodie to use Claude. Provide a complete continuation/handoff prompt containing the relevant verified context so she does not have to reconstruct the task.
- If ChatGPT is the better operator, proceed in ChatGPT.
- If the task genuinely requires both, state the exact operator split before execution and preserve the documented workflow at each handoff.
- For customer-product testing, operator fit does not permit substitution: execute each step on the platform/tool the customer-facing material actually instructs. A successful substitute implementation is not valid end-to-end evidence.
- Never choose an operator from memory or preference when the repo/customer workflow specifies one. Read the governing sources first.

This preflight applies to every TDIE task, not only Amazon/WYS work.
