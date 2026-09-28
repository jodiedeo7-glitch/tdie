# TDIE 33 Scheduled Tasks — Verified Migration Matrix
## 28 September 2026

Source: TDIE AI Operating Manual (25 Sep 2026), current TDIE repo, current platform documentation, and current connector/tool availability.

## Decision key
- KEEP CLAUDE = required platform/local/browser execution; do not duplicate.
- CLAUDE + CHATGPT = split research/creative reasoning from execution.
- METRICOOL CANDIDATE = use Metricool for supported Pinterest publishing/analytics.
- DETERMINISTIC = move date/status/dedupe logic to structured state/code.
- RETIRE = only after replacement is proven.

## Task matrix
| # | Task | Target owner | Model/engine target | Main change |
|---|---|---|---|---|
| 1 | 8am Daily Prompt | Claude | Sonnet 5.5 | Bounded browser execution. |
| 2-4 | Reply checks 8:30 / 1:30 / 7:30 | Claude | Opus 5.5 | Voice-sensitive writing + platform context. |
| 5-7 | Approved-reply posters | Claude | Sonnet 5.5 | Pure execution. |
| 8 | Missed-run sweep | Claude + deterministic state | Sonnet 5.5 | Replace prose/log inference with due-state. |
| 9 | FB daily Skool mirror | Claude | Opus 5.5 | No verified ChatGPT Skool write path. |
| 10 | Skool member watch | Claude | Opus 5.5 | Member judgment + platform execution. |
| 11-13 | Hot-thread checks | Claude | Opus 5.5 | Research + writing + platform context. |
| 14 | Daily DFY calendar post | Claude | Sonnet 5.5 if loading only | Separate creation from posting. |
| 15 | Pinterest pull sweep | Split | Sonnet 5.5 execution | Metricool can manage scheduled content, but current connected tool has no delete action; Pinterest-native/browser remains for pulls and published deletion. |
| 16 | Brand Closet OOTD pins | Claude + ChatGPT candidate | Opus/Sonnet | Test ChatGPT + Higgsfield for creative component; keep local/browser execution. |
| 17 | Inactive-member sweep | Claude | Sonnet 5.5 | Bounded platform check. |
| 18 | Threads top-up | Claude | Sonnet 5.5 | Loads already-written queue. |
| 19 | Monday DFY test readout | Metricool + ChatGPT candidate | — | Metricool analytics + ChatGPT analysis once Instagram is connected. |
| 20 | Etsy listing package | Claude + ChatGPT candidate | Opus 5.5 | ChatGPT can prep creative/research; Etsy execution remains unverified. |
| 21 | Pretty & Paid build | Claude initially | Fable 5.1; test Opus 5.5 | Long-horizon product production. |
| 22 | Friday numbers + member read | ChatGPT candidate + connectors | Fable/Opus | Strong analysis candidate after data sources are connected. |
| 23 | Friday Pink Finds | Split | Opus 5.5 creative | MailerLite execution remains until a direct write path is verified. |
| 24 | Friday Skool week build | Claude + ChatGPT prep candidate | Fable 5.1 | Keep final Skool execution in Claude. |
| 25 | Saturday Legally Blonde Amazon pin factory | Claude + ChatGPT + Metricool candidate | Fable/Opus creative; Sonnet execution | Strong Pinterest migration candidate; Metricool supports Pinterest scheduling and CSV batch import. |
| 26 | Saturday Daily Prompts build | Claude | Opus 5.5 | Local files + downstream Claude execution. |
| 27 | Sunday Threads write | Claude + ChatGPT candidate | Fable 5.1 | ChatGPT can research/brainstorm; no verified Threads write path. |
| 28 | Sunday Pinterest pin factory | Claude + ChatGPT + Metricool candidate | Opus/Sonnet | Move creative where it passes quality test; batch schedule through Metricool. |
| 29 | Monthly DFY Content Calendar | Claude + ChatGPT candidate | Fable 5.1 | ChatGPT is a strong research/analysis candidate; Claude remains upload owner. |
| 30 | Last-Friday Pretty & Paid drop | Claude | Fable/Opus | Platform-specific execution. |
| 31 | Last-Friday scorecard/member pass | ChatGPT candidate + connectors | Fable/Opus | Analysis candidate after data access is established. |
| 32 | Weekly warm-member DFY offers | Claude | Opus 5.5 | Skool/member context + DM drafting. |
| 33 | Premium/flash-sale and other one-off scheduled changes | Claude | Sonnet 5.5 for bounded work | Expire/delete after their dates; do not duplicate. |

## Highest-value architecture change: Pinterest

Creative should be separated from publishing.

ChatGPT: research, angle, Pin copy, image direction, QA, and optionally Higgsfield generation.

Existing deterministic renderer: text/layout rendering.

Metricool: Pinterest scheduling/publishing.

Metricool currently supports Pinterest scheduling and CSV batch import. Its CSV supports Pinterest, board name, Pin title, Pin link, alt text, and public media URLs. Metricool recommends importing up to 50 posts per file, so a 60-Pin batch becomes two imports instead of 60 browser scheduling sessions.

Do not use Metricool as the Pinterest pull/deletion replacement until a delete action is available and tested. Deleting a post in Metricool removes it from Metricool's calendar; published social content still has to be removed on the social platform.

## Critical platform constraint

Do not recreate the four While-You-Sleep local Storefront jobs as ChatGPT Scheduled Tasks. OpenAI's current documentation says scheduled tasks created in a ChatGPT Project cannot access uploaded/project files. These TDIE jobs depend on local Storefront files and signed-in browser execution. Claude Desktop remains the correct execution layer.

ChatGPT can take over separable research, creative generation, analysis, QA, and GitHub work.

## Current connector state

ChatGPT environment: GitHub, Higgsfield and Metricool are available.
Metricool is connected, but the current brand has no social network connected, so Pinterest cannot yet be tested through Metricool.
Claude officially supports GitHub, Google Drive/Google Workspace and Canva, among many other connectors.
No verified first-party TDIE connector was established for Pinterest, Amazon Associates, Gemini, Skool, or Etsy.

## Current Claude model correction

Claude Sonnet 5.5 released September 28, 2026. The old September 25 model map is stale.
Use Fable 5.1 for demanding long-horizon reasoning, Opus 5.5 for complex writing/design/judgment, and Sonnet 5.5 for well-scoped routine execution. Do not assign Haiku 5.5 yet; Anthropic announced it is coming later.

## Non-negotiable migration rule

No existing Claude task is deleted or duplicated until its replacement produces the required output, performs the platform action, is verified on-platform, reconciles state, passes a retry/duplicate test, and has a rollback path.