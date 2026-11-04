import { sign } from "../auth.js";
import { json, jsonResponse, methodNotAllowed } from "../http.js";

export async function handle(request, env) {
  if (request.method !== "POST") return methodNotAllowed();

  const body = await json(request);
  const email = String(body.email || "").trim().toLowerCase();

  if (!email || !email.includes("@")) {
    return jsonResponse({ error: "Enter a valid email address." }, 400);
  }

  if (!env.MAILERLITE_API_KEY || !env.MAILERLITE_GROUP_ID || !env.ACCESS_SECRET) {
    return jsonResponse({ error: "Verification is temporarily unavailable." }, 500);
  }

  try {
    const r = await fetch(
      `https://connect.mailerlite.com/api/subscribers/${encodeURIComponent(email)}`,
      {
        headers: {
          Authorization: `Bearer ${env.MAILERLITE_API_KEY}`,
          Accept: "application/json",
        },
      }
    );

    if (r.status === 404) {
      return jsonResponse({ error: "We can't find that email. Use the address you purchased with." }, 403);
    }

    if (!r.ok) {
      return jsonResponse({ error: "Verification is temporarily unavailable." }, 500);
    }

    const data = await r.json();
    const groups = data?.data?.groups || [];
    const ok = groups.some((g) => String(g.id) === String(env.MAILERLITE_GROUP_ID));

    if (!ok) {
      return jsonResponse({
        error: "That email isn't registered for this course. Use the address you purchased with.",
      }, 403);
    }

    return jsonResponse({ token: await sign(email, env.ACCESS_SECRET) });
  } catch {
    return jsonResponse({ error: "Verification is temporarily unavailable." }, 500);
  }
}
