// Feedback box on the private While-You-Sleep Storefront™ buyer website.
// Saves every message (and optional photo) to the tdie-site-data database,
// then forwards it to Jodie's inbox through her Google Apps Script mailer.
// The mailer's address and passcode live in the database's config table, never in this public code.
import { json, jsonResponse, methodNotAllowed } from "../http.js";

const clean = (v, max) => String(v ?? "").replace(/\r/g, "").trim().slice(0, max);
const MAX_PHOTO_B64 = 1_800_000; // about 1.3 MB of picture after the page shrinks it

async function config(env) {
  const { results } = await env.DB.prepare("SELECT key, value FROM config WHERE key IN ('feedback_mailer_url','feedback_mailer_secret')").all();
  return Object.fromEntries((results || []).map(r => [r.key, r.value]));
}

export async function handle(request, env) {
  if (request.method !== "POST") return methodNotAllowed();
  if (!env.DB) return jsonResponse({ error: "The feedback box isn't connected yet. Email hello@thedigitalincomeedit.com instead." }, 503);
  const b = await json(request);
  if (b.hp) return jsonResponse({ ok: true });
  const message = clean(b.message, 5000);
  const email = clean(b.email, 200).toLowerCase();
  const name = clean(b.name, 80);
  const page = clean(b.page, 120);
  let photo = typeof b.photo === "string" ? b.photo.replace(/^data:[^,]*,/, "") : "";
  const photoType = /^image\/(jpeg|png|webp)$/.test(String(b.photoType || "")) ? b.photoType : "image/jpeg";
  const photoName = clean(b.photoName, 120) || "screenshot.jpg";
  if (!message && !photo) return jsonResponse({ error: "Type a message or add a photo first." }, 400);
  if (email && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) return jsonResponse({ error: "That email address doesn't look right." }, 400);
  if (photo.length > MAX_PHOTO_B64 || /[^A-Za-z0-9+/=]/.test(photo)) photo = "";

  const created = new Date().toISOString();
  const ins = await env.DB.prepare(
    "INSERT INTO wys_feedback (created_at,name,email,page,message,photo_name,photo_type,photo_b64) VALUES (?,?,?,?,?,?,?,?)"
  ).bind(created, name, email, page, message, photo ? photoName : null, photo ? photoType : null, photo || null).run();
  const id = ins.meta?.last_row_id;

  let emailed = false;
  try {
    const c = await config(env);
    if (c.feedback_mailer_url && c.feedback_mailer_secret) {
      const r = await fetch(c.feedback_mailer_url, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ secret: c.feedback_mailer_secret, id, created, name, email, page, message, photo, photoType, photoName }),
        redirect: "follow",
      });
      emailed = r.ok && (await r.text()).trim().startsWith("ok");
      if (emailed && id) await env.DB.prepare("UPDATE wys_feedback SET emailed=1 WHERE id=?").bind(id).run();
    }
  } catch (e) {
    console.error("feedback mailer failed", e);
  }
  return jsonResponse({ ok: true, emailed });
}
