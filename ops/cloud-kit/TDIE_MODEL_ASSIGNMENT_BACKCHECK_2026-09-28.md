# TDIE Model Assignment Back-Check — 2026-09-28

## Current verified Claude model landscape

Anthropic released Claude Sonnet 5.5 on September 28, 2026. Anthropic describes it as a faster, lower-cost complement to Opus 5.5, strongest for well-scoped everyday tasks, bug fixes, and polished documents/slides/spreadsheets.

Claude Opus 5.5 was released September 22, 2026 and is positioned by Anthropic as the leading Opus model, performing at the level of Fable 5.1 on most work at substantially lower token cost than Opus 5.

Claude Fable 5.1 remains Anthropic's most capable generally available model for demanding reasoning and long-horizon agentic work.

## Consequence for TDIE

The September 25 model-switch table is no longer the final model table.

Replace:
- routine Sonnet 5 assignments with Sonnet 5.5 where the task is well-scoped and does not require Fable-level judgment;
- routine Opus 5.5 assignments only after testing whether Sonnet 5.5 produces equivalent TDIE output;
- expensive Fable 5.1 assignments only where the task genuinely benefits from long-horizon reasoning/research/judgment.

Do not downgrade voice-sensitive or business-critical work merely to save tokens. Use a representative-output test before moving a task down a model tier.

## Current target categories

### Fable 5.1
Use for:
- monthly DFY calendar research/build
- Friday Skool week build if member evidence + 21-post voice work remains complex
- Friday numbers/member read if it must synthesize multiple business streams and decide next-week priorities
- Sunday Threads research/write if its current 126-post research workload remains genuinely long-horizon
- any new deep research or architecture task where failure is expensive

### Opus 5.5
Use for:
- nuanced writing that needs strong judgment but is more bounded than the Fable tasks
- complex creative production
- difficult browser workflows where Sonnet 5.5 testing does not pass
- image/design/copy workflows where the visual/copy quality bar requires the additional capability

### Sonnet 5.5
First candidate for:
- 8am Daily Prompt publishing
- loading already-written Threads posts
- Pinterest pull/removal execution
- inactive-member sweep
- approved-reply posting
- missed-run sweep
- other bounded browser/posting/checking tasks
- routine document production after a quality test

### Haiku 5.5
Do not assign yet. Anthropic's September 28 announcement says it is coming in the coming weeks.

## Important

Model selection is separate from platform ownership. A Sonnet 5.5 task can still belong in Claude because Claude has the required local/browser execution environment. Moving a task to ChatGPT merely because GPT is capable of the reasoning is not a valid architecture decision if the execution environment is missing.
