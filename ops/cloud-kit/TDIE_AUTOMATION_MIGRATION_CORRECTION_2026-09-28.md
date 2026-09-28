# TDIE Automation Migration — Critical Correction
## 28 September 2026

This correction supersedes any implication in earlier migration material that the While-You-Sleep local scheduled tasks should be recreated as ChatGPT Scheduled Tasks.

### Verified constraint

OpenAI's current Scheduled Tasks documentation states that if a scheduled task is created in a ChatGPT Project, it cannot access files uploaded to that project or files stored in that project. The TDIE While-You-Sleep tasks depend on the customer's local Storefront folder, local state files, and signed-in browser session.

Therefore:

- Keep the **While-You-Sleep local execution scheduler in Claude Desktop**.
- Do not create duplicate ChatGPT scheduled tasks for the four Storefront jobs.
- Use ChatGPT for separable research, creative generation, analysis and QA where a clean handoff is possible.
- Test ChatGPT + Higgsfield as a creative-production component, not as a replacement for the local/browser scheduler.
- Test Metricool as the Pinterest publishing layer separately. The currently connected Metricool account has no social network connected, so Pinterest cannot yet be tested through the Metricool connector.
- Use ChatGPT Scheduled Tasks for cloud-accessible recurring work only when the required connected app/state is actually available.

### Why this matters

The right architecture is not "move every Claude task to ChatGPT." It is:

**Claude Desktop = local/browser execution**

**ChatGPT = research, reasoning, creative production, QA and repo work**

**Higgsfield = image/video generation when its specific capabilities are required**

**Metricool/API = deterministic publishing/data operations where verified**

**Structured state/scripts = dates, IDs, deduplication, retries and reconciliation**

No production task should be duplicated or deleted until the replacement path has passed an end-to-end test.
