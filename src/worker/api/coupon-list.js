// 18 Nov 2026: coupon signup from the Skool post. Adds the email to the one
// main MailerLite list (no separate group). Single opt-in, like the other forms.
import { json, jsonResponse, methodNotAllowed } from "../http.js";
export async function handle(request, env) {
  if (request.method === "GET") return jsonResponse({ live: Boolean(env.MAILERLITE_API_KEY) });
  if (request.method !== "POST") return methodNotAllowed();
  const fail = (s) => jsonResponse({ error: "Couldn't add you just now. Try again in a moment." }, s);
  if (!env.MAILERLITE_API_KEY) return fail(503);
  let b = {};
  const ct = request.headers.get("content-type") || "";
  if (ct.includes("application/json")) b = (await json(request)) || {};
  else { const f = await request.formData(); b = { email: f.get("fields[email]") || f.get("email"), hp: f.get("hp") }; }
  if (b.hp) return jsonResponse({ ok: true });
  const email = String(b.email || "").trim().toLowerCase().slice(0, 200);
  if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) return jsonResponse({ error: "Enter a valid email address." }, 400);
  const r = await fetch("https://connect.mailerlite.com/api/subscribers", {
    method: "POST",
    headers: { Authorization: `Bearer ${env.MAILERLITE_API_KEY}`, "Content-Type": "application/json", Accept: "application/json" },
    body: JSON.stringify({ email }),
  }).catch(() => null);
  if (!r || !r.ok) return fail(500);
  return jsonResponse({ ok: true });
}
