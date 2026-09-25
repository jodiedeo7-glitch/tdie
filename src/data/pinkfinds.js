// ─────────────────────────────────────────────────────────────
// PINK FINDS signup campaign (Jodie, 25 Sep 2026).
// One MailerLite form feeds the "Lifestyle Pink Finds" group.
// The Prime Big Deal Days copy (Amazon's sale, 6 and 7 Oct 2026)
// shows until PRIME_END, then every form falls back to the
// evergreen Friday copy on its own (switched in the browser, so it
// flips on time even if the site is not rebuilt).
// Sends promised by this copy, both scheduled:
//   Fri 2 Oct 2026 5 pm ET  Pink Finds, Prime Big Deal Days edition
//   Tue 6 Oct 2026 9 am ET  "The sale is live" picks email
// ─────────────────────────────────────────────────────────────
export const PF_ACTION = "https://assets.mailerlite.com/jsonp/2532349/forms/199525394616943647/subscribe";
export const PRIME_END = "2026-10-06T13:00:00Z";
export const PF = {
  prime: {
    heading: "Get my pink Prime Day picks",
    sub: "Prime Big Deal Days runs October 6 and 7. My pink picks land in your inbox for it, then new finds every Friday. Unsubscribe anytime.",
  },
  evergreen: {
    heading: "New pink finds, every Friday",
    sub: "The week's new looks in one email, every piece linked. Unsubscribe anytime.",
  },
  button: "Send Me the Finds",
  done: "You're in. Your first pink finds land in your inbox this Friday.",
};
