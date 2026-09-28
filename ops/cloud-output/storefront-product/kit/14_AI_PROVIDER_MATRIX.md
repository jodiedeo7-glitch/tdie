# 14. AI PROVIDER MATRIX

Checked against current provider documentation on Sep 28, 2026.

## A. COST / PLAN SNAPSHOT

| Provider / route | Current plan or usage price | Credits / allowance | Commercial rights | Unlimited note | Best use in this product |
|---|---:|---|---|---|---|
| Claude Free | $0 | Usage-limited | Not an image license | No image generation entitlement | Planning, copy, manual path |
| Claude Pro | $20/mo | Usage-limited | Not an image license | No image generation entitlement | Scheduled orchestration |
| ChatGPT Free | $0 | Usage-limited | Image output terms apply to account | No simple universal image-unlimited promise | Manual planning/image path |
| ChatGPT Go | $8/mo US | Higher limits than Free | Image output terms apply to account | Limits vary | Lower-cost manual path |
| ChatGPT Plus | $20/mo | Higher limits than lower tiers | Image output terms apply to account | Not a universal image-unlimited promise | Manual creation + planning |
| OpenArt Plus | $34 list / $27 currently displayed promotion | 12,000 credits/mo | Commercial use rights | Plus itself is credit-based, not universal unlimited | Strong all-around customer stack |
| Higgsfield Plus | $49/mo list benchmark | Plan credits plus model-specific Unlimited windows | Check current plan terms | Specific website models/windows only | High-volume manual browser generation |
| Gemini API - Nano Banana 2 | $0.101 per 2K image standard | Pay per image | Check current Google API terms for your account/use | No unlimited | Lowest-cost API image benchmark |
| Gemini API - Nano Banana Pro | $0.134 per 1K/2K image standard | Pay per image | Check current Google API terms | No unlimited | Higher-control reference/editing benchmark |
| OpenAI GPT Image 2.5 | $8/M image-input tokens + $30/M image-output tokens | Usage-based | Check current OpenAI terms | No unlimited | Targeted edits/generation |

Source notes:
- OpenArt: current Plus pricing shows 12,000 credits/month, OpenArt MCP and commercial-use rights.
- OpenArt MCP: same OpenArt account, credits, projects and generation history; connector generations consume the account's credit pool.
- Higgsfield: website Unlimited is model/surface specific; MCP/CLI and other non-website surfaces consume standard credits.
- Google Gemini API: current Nano Banana 2 2K output is $0.101 standard; Nano Banana Pro 1K/2K is $0.134 standard.
- OpenAI GPT Image 2.5 is token-priced, so there is no honest flat per-image cost without measuring actual usage.
- Claude Scheduled Tasks are on paid plans and run in the cloud.

## B. ILLUSTRATIVE MONTHLY IMAGE COST

Example workload:
4 looks/week
x 2 images/look
x 4 weeks
= 32 generated images/month

Gemini Nano Banana 2 at 2K:
32 x $0.101 = about $3.23 standard usage.

Gemini Nano Banana Pro at 2K:
32 x $0.134 = about $4.29 standard usage.

Batch pricing is lower where the job is eligible for Google's batch mode, but the workflow must tolerate asynchronous processing.

OpenAI GPT Image 2.5:
Do not quote a fixed per-image number. Measure the actual response usage for the chosen size/quality.

OpenArt and Higgsfield:
Do not convert credits into dollars until you have the current model's actual credit cost. Credit costs vary by model and settings.

## C. WHAT MODEL FOR WHICH JOB?

### Faceless product/lifestyle styling
Primary candidates:
- Seedream 4.5
- Seedream 5 Pro
- Nano Banana 2

Choose based on current provider availability, realism, reference fidelity and credit cost.

### Face-forward persona consistency
Primary candidates:
- Nano Banana 2
- Nano Banana Pro

Use the customer's fixed persona reference image.

### Hard edits / targeted changes
Primary candidates:
- Nano Banana Pro
- GPT Image

Use when a specific edit matters more than raw throughput.

### Lowest-cost repeat image generation
Primary candidate:
- Gemini Nano Banana 2 at 2K through the API

Use batch when the workflow can tolerate asynchronous processing.

### High-volume manual browser generation
Potential candidates:
- Higgsfield model-specific Unlimited windows
- OpenArt plans with the model/allowance that matches the job

Always verify the current plan's exact model and Unlimited terms.

## D. UNLIMITED DOES NOT MEAN "UNLIMITED EVERYWHERE"

### Higgsfield
Higgsfield's website may include model-specific Unlimited windows.

That does NOT mean:
- Unlimited MCP
- Unlimited CLI
- Unlimited Canvas
- Unlimited external agent generation

Those non-website surfaces consume credits according to Higgsfield's current rules.

### OpenArt
OpenArt has plan-specific Unlimited creation benefits for particular models/surfaces.

That does NOT mean:
- Unlimited every model
- Unlimited MCP

OpenArt MCP uses the connected OpenArt account and credit balance.

### Gemini API
No unlimited allowance.

### OpenAI API
No unlimited allowance.

### ChatGPT
Do not describe ChatGPT's current image limits as universally unlimited. Account limits vary.

### Claude
Claude is the orchestrator in this product, not the image-generation provider.

## E. MANUAL VS CONNECTOR

| Job | Manual path | Connector/API path |
|---|---|---|
| Write prompt | ChatGPT/Claude manually | Claude task |
| Generate image | Provider website/app | OpenArt MCP, Higgsfield MCP, Gemini API or OpenAI API |
| Reuse persona reference | Upload manually | Connector/API attachment |
| Pinterest Pin creation | Native Pinterest | Pinterest API Standard |
| Pinterest review | Customer | Customer APPROVE in API mode |
| Amazon product intake | Manual | Optional Amazon Creators API if eligible |
| Idea List creation | Manual | Customer-side / eligible Amazon workflow |
| Site page | Manual paste | Authorized site/GitHub workflow |

## F. BUYING RULES

1. Do not buy Higgsfield Unlimited just because a workflow says "MCP."
2. Do not buy OpenArt Plus assuming 12,000 credits means 12,000 premium 2K generations. Model credit costs differ.
3. Do not buy a second image platform until the first one has been tested for the exact job.
4. Do not pay for an image API when the same task can be done manually within an existing lower-cost plan.
5. Do not make customer recommendations from the founder's personal unlimited access.

## CURRENT SOURCE LIST

OpenArt Pricing
OpenArt MCP
Higgsfield pricing/help for Unlimited and MCP/CLI
Google Gemini API Pricing and image-generation documentation
OpenAI Image Generation pricing
Anthropic Claude Help Center: Scheduled Tasks / Cowork


## G. CHATGPT CONNECTED IMAGE APPS

The current ChatGPT connector inventory includes official Higgsfield and OpenArt apps. They can generate images from prompts and reference images inside ChatGPT, subject to the customer's connected account, plan and current app capabilities.

This is a ChatGPT app path, not a Claude MCP path.

Use it in the CREDIT-SAVING or MIXED path when it reduces tool switching:
ChatGPT
-> connected OpenArt or Higgsfield
-> manual review
-> Pinterest native tools

Do not tell customers that:
- a ChatGPT app connector creates unlimited generations
- a ChatGPT subscription grants the provider's website Unlimited allowance
- a ChatGPT connector has the same credit behavior as Claude MCP

Always check the connected app's current model list and account credit behavior before production use.

## H. DECISION TREE

1. I want the fewest subscriptions.
   Start with one manual image provider and native Pinterest.

2. I want the cheapest predictable image spend.
   Benchmark Gemini API Nano Banana 2 at 2K.

3. I want one paid visual platform with many model choices.
   Benchmark OpenArt Plus.

4. I already have Higgsfield and prefer its browser workflow.
   Test Higgsfield manually first. Only use MCP when the customer's plan and credit economics are understood.

5. I want Claude to orchestrate the image generation.
   Use a supported Claude MCP route and treat connector credits separately from website Unlimited.

6. I want ChatGPT to handle image generation interactively.
   Test the current OpenArt or Higgsfield ChatGPT app against the exact Storefront job.

7. I do not want API/developer work.
   Stay on native Pinterest and manual image generation.

No single provider wins every job. The product therefore documents the tradeoffs instead of forcing one vendor.
