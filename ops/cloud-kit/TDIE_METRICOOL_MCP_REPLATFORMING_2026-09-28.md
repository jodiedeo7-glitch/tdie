# TDIE Metricool MCP Replatforming — 2026-09-28

## Decision

Do not move social publishing tasks to ChatGPT merely because ChatGPT can create or schedule social content.

Metricool now has an official MCP for Claude. It connects to Claude Desktop/Claude.ai/Claude Code and can read analytics, schedule and publish posts, and manage connected networks without opening the Metricool dashboard.

This means the preferred architecture for TDIE social execution is:

**Claude scheduled task -> Metricool MCP -> social platform**

instead of:

**Claude scheduled task -> browser -> social platform**

where Metricool supports the exact operation.

## Highest-value targets

### Threads

Current TDIE architecture writes 126 posts weekly, then a nightly browser task loads the next day's 18 because the native Threads scheduler holds about 25 posts.

Metricool can schedule Threads content and supports Threads up to 80-post threads. Metricool's CSV importer also accepts date/time, Threads, text, image URLs and alt text.

Target:
- Keep the weekly research/writing task in Claude.
- Change its output to a validated schedule package/CSV.
- Use Metricool MCP to schedule the week's individual posts in batches.
- Eliminate the nightly Threads top-up task only after one full week is successfully scheduled and verified in Metricool and on Threads.

Do not combine the 126 posts into one 80-post thread. The current system uses 18 separate posts per day; preserve that.

### Pinterest

Current TDIE Pinterest factories repeatedly use browser scheduling.

Target:
- Keep creative generation/research where it is best.
- Use Metricool MCP for scheduled Pinterest publishing.
- Use Metricool's batch CSV path for large batches where useful.
- Keep Pinterest-native/browser deletion for pulled live Pins unless a tested Metricool/Pinterest delete path actually removes the live Pin.
- Keep the existing Pinterest API as a possible read/state source.

The Pinterest native API is not treated as a future-scheduling replacement. Pinterest's own help documents native scheduling up to 30 days; its current API docs reviewed do not expose the same future-publish operation.

### Instagram

Metricool can auto-publish Instagram posts, Reels and Stories for professional accounts, but Stories with links, mentions or interactive stickers require manual publishing. Therefore:
- move feed-post execution to Metricool when the account connection is available;
- keep Story-with-link execution manual/notification based until the platform path changes;
- do not claim full hands-off Story scheduling for link-sticker stories.

### Facebook

Metricool can publish supported Facebook content, but the current TDIE Facebook group mirror is a Facebook Group workflow. Do not replace the Group mirror unless Metricool explicitly supports the target group action.

## Tasks that should NOT move to ChatGPT

- Skool publishing and member DMs: no verified equivalent current ChatGPT connector/action found.
- Facebook Group mirror: no verified Metricool replacement for the target group action.
- Etsy listing publishing: no verified ChatGPT/Metricool write path established.
- Amazon Idea List management: no verified replacement established.
- Local Storefront scheduled tasks: keep Claude Desktop due local files/browser requirements.

## Model changes that accompany this

Claude Sonnet 5.5 launched 28 Sep 2026 and is 30%+ faster and up to 30% less costly than Sonnet 5 for most work. Claude Opus 5.5 launched 22 Sep 2026, performs at the level of Fable 5.1 on most work and costs 40% less to run than Opus 5.

Therefore:
- routine posting/loading/checking tasks should be tested on Sonnet 5.5;
- complex writing/reasoning can use Opus 5.5;
- Fable 5.1 should be reserved for work where its additional capability is actually needed.

## Account requirement

The current Metricool connection in this ChatGPT environment has no social networks connected, so production migration cannot be tested yet. Connection of Pinterest/Threads/Instagram/Facebook accounts must occur at the user's Metricool account level before live validation.

## Migration safety

Do not delete any existing task until:
1. Metricool is connected to the relevant network;
2. the replacement creates or schedules the correct content;
3. the platform shows the expected result;
4. one retry/duplicate scenario is tested;
5. the old Claude/browser task can be disabled without leaving a gap.

