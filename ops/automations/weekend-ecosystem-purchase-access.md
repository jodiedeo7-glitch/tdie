# Weekend Ecosystem purchase access

Verified and activated 2026-09-30. Owner-authorized Make integration is a scoped exception to the older tool-stack list.

## Live workflow

Beacons paid-sale notification in the owner's Gmail → Make scenario **TDIE | Weekend Ecosystem purchase access** (6465016, team 3076688) → existing MailerLite Buyers group → existing **Weekend Ecosystem — Access Granted and Completion** automation (196430036792772181) → existing access email and course authorization.

Scenario: https://us2.make.com/3076688/scenarios/6465016/edit

Scheduling is Active, every 60 minutes. Gmail start position was reset to **From now on** after testing. No historical bulk enrollment. Existing course authentication, completion tracking, customer fields and unrelated automations were preserved.

## Source and enrollment checks

Gmail Watch emails uses:
```
from:sup@info.beacons.ai subject:"You made a sale" "The Weekend Ecosystem"
```
Maximum 10 messages per poll; messages are not marked read. HTML body is converted to text because the plain-text alternative omits important order-detail values.

A case-sensitive parser requires exact product **The Weekend Ecosystem™**, type **digital-products**, decimal dollar amount, valid-looking buyer email and UUID order number. No match produces no enrollment. The route additionally requires sender sup@info.beacons.ai, amount greater than zero, and Gmail's Authentication-Results beginning mx.google.com with DKIM pass for @info.beacons.ai and DMARC pass for info.beacons.ai. Receipt-template or authentication changes fail closed and require investigation.

MailerLite POST /subscribers body:
```json
{"email":"<mapped Text parser 3.email>","groups":["195477643940857421"]}
```
The body does not set subscriber status, fields or remove groups. Credentials are stored in Make connections; no key is committed. Existing unsubscribed/bounced subscribers are not forced active.

This is automatic processing of authenticated **paid-sale email notifications**, not a native checkout webhook. Successful paid installments are eligible; repeated installments or replayed notices update the same subscriber. Zero-dollar/coupon orders are excluded. Failed/incomplete checkouts without a paid-sale receipt do not enroll. Refund/revocation handling is outside this scenario. Reliability depends on Beacons notification delivery and its current receipt format.

## Verification performed

- Captured two genuine historical paid Weekend Ecosystem sale receipts; both authenticated and parsed with their actual buyer emails.
- Replayed the full production-mapped flow: both existing buyers returned HTTP 200.
- Safe owner-only controlled tests: new subscriber POST returned 201; repeat returned 200 with the same subscriber ID. No nonpurchaser was enrolled.
- Existing MailerLite automation completed and delivered its access email to the owner's controlled test address.
- Opened the email's course link, authenticated with the test email and opened protected module 22 content.
- Final full receipt replay to a fresh owner test alias created once then updated once; exactly one access email arrived and MailerLite activity showed completion.
- Unrelated-product and malformed-email parser tests produced no bundles/enrollment.
- Restored production buyer-email mapping before activation; reset trigger to From now on; saved; overview showed Active.

No new checkout transaction was made and no payment was incurred. Verification used genuine captured purchase events and safe owner-only replay, not a newly charged checkout.

## Cost and operation

Additional subscription cost: $0/month at current volume. Make Free has 1,000 credits/month. Hourly polling uses up to 744 credits in a 31-day month, plus approximately 3 credits per matching notification (HTML conversion, parser, MailerLite); testing and any other scenarios also consume credits. About 85 eligible notifications fit after baseline polling if there are no other credit uses. Free-plan limits remain a dependency; no paid plan was purchased. Access normally arrives within an hour plus email processing/delivery.

## Troubleshooting and rollback

1. Check Make History and Incomplete executions. Sequential processing and storing incomplete executions are enabled; data-loss/discard is disabled; trigger commits last. Module errors are retained for inspection/retry. After three consecutive errors the scenario can deactivate; check Active status and credit balance. Separate alert delivery was not verified.
2. If a sale is missing, verify that its actual paid-sale receipt reached the connected Gmail. Compare captured receipt count with parser/filter output. No-match and filtered receipts can finish without an error; inspect their execution data.
3. Inspect exact product/type/email/amount/order fields and Authentication-Results. Do not relax authentication or enroll an unrelated product to make a test pass.
4. For MailerLite failures, check connection validity, response status, buyer status and Buyers membership. Retry retained execution after fixing the cause. Idempotent enrollment does not reset completion or repeatedly join an existing group.
5. If membership is correct but delivery fails, inspect the existing MailerLite automation's activity and email delivery; preserve consent/status. If course authorization fails, investigate existing course API/group checks separately.
6. To roll back, switch this Make scenario Off. Keep the existing MailerLite access/completion automation active; already enrolled buyers retain access. Manual verified buyer enrollment remains the emergency procedure.

## Unfinished activation workaround

Rechecked after activation: Beacons **Untitled 9/28/2026** Weekend Ecosystem post-purchase sequence remains in Drafts, with no recipients. It was not activated. MailerLite **Weekend Ecosystem - Activate Access** form remains an unlinked emergency fallback; it is not part of this automatic workflow. No competing purchase-activation email was enabled and no dependent assets were deleted.
