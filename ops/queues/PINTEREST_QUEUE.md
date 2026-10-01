# PINTEREST EXECUTION QUEUE

This queue contains browser-only Pinterest work.

## Entry template

### Batch: <batch-id>
- Packet: `<path>`
- Created by: ChatGPT
- Contact sheet approved: YES / NO / NOT REQUIRED
- Pins READY: <count>
- Persona images still required: <count>
- Earliest proposed slot: <date time ET>
- Status: WAITING / RUNNING / PARTIAL / VERIFIED / BLOCKED

### Claude execution
1. Read `ops/ai-router/TDIE_PINTEREST_ROUTER.md`.
2. Open Pinterest scheduled pins and count the next 7 days.
3. Reconcile proposed slots against what is actually scheduled.
4. Schedule only rows marked `READY`.
5. Use one fresh composer tab per pin.
6. Verify every scheduled pin from the scheduled-pins view.
7. Update the packet CSV statuses to `VERIFIED` or `FAILED`.
8. Report only exceptions plus verified count.

### Never do in this queue
- topic research
- copy rewrites
- image generation
- layout design
- new product claims
- pricing decisions
