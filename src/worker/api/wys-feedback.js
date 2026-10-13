// Feedback box on the private While-You-Sleep Storefront™ buyer website.
// Two kinds: "feedback" (something looks weird) and "love" (a set the buyer loves, optionally
// shared with permission for Jodie's real-results proof). Saves every message and up to 3 photos
// to the tdie-site-data database, then forwards it to Jodie's inbox through her Google Apps Script
// mailer. The mailer's address and passcode live in the database's config table, never in this public code.
import { json, jsonResponse, methodNotAllowed } from "../http.js";

const clean = (v, max) => String(v ?? "").replace(/\r/g, "").trim().slice(0, max);
const MAX_PHOTO_B64 = 1_800_000; // about 1.3 MB of picture after the page shrinks it
const MAX_PHOTOS = 3;

async function config(env) {
  const { results } = await env.DB.prepare("SELECT key, value FROM config WHERE key IN ('feedback_mailer_url','feedback_mailer_secret')").all();
  return Object.fromEntries((results || []).map(r => [r.key, r.value]));
}

function photosFrom(b) {
  const list = Array.isArray(b.photos) ? b.photos : (b.photo ? [{ data: b.photo, type: b.photoType, name: b.photoName }] : []);
  const out = [];
  for (const p of list.slice(0, MAX_PHOTOS)) {
    const data = typeof p?.data === "string" ? p.data.replace(/^data:[^,]*,/, "") : "";
    if (!data || data.length > MAX_PHOTO_B64 || /[^A-Za-z0-9+/=]/.test(data)) continue;
    const type = /^image\/(jpeg|png|webp)$/.test(String(p.type || "")) ? p.type : "image/jpeg";
    out.push({ data, type, name: clean(p.name, 120) || `photo-${out.length + 1}.jpg` });
  }
  return out;
}

export async function handle(request, env) {
  if (request.method !== "POST") return methodNotAllowed();
  if (!env.DB) return jsonResponse({ error: "The box isn't connected yet. Email hello@thedigitalincomeedit.com instead." }, 503);
  const b = await json(request);
  if (b.hp) return jsonResponse({ ok: true });
  const kind = b.kind === "love" ? "love" : "feedback";
  const message = clean(b.message, 5000);
  const email = clean(b.email, 200).toLowerCase();
  const name = clean(b.name, 80);
  const page = clean(b.page, 120);
  const credit = clean(b.credit, 200);
  const consent = kind === "love" && b.consent === true ? 1 : 0;
  const photos = photosFrom(b);
  if (kind === "love" && !photos.length) return jsonResponse({ error: "Add at least one photo from the set you love." }, 400);
  if (!message && !photos.length) return jsonResponse({ error: "Type a message or add a photo first." }, 400);
  if (email && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) return jsonResponse({ error: "That email address doesn't look right." }, 400);

  const created = new Date().toISOString();
  const ins = await env.DB.prepare(
    "INSERT INTO wys_feedback (created_at,name,email,page,message,kind,consent,credit) VALUES (?,?,?,?,?,?,?,?)"
  ).bind(created, name, email, page, message, kind, consent, credit).run();
  const id = ins.meta?.last_row_id;
  if (id && photos.length) {
    await env.DB.batch(photos.map((p, i) =>
      env.DB.prepare("INSERT INTO wys_feedback_photos (feedback_id,idx,name,type,b64) VALUES (?,?,?,?,?)").bind(id, i, p.name, p.type, p.data)));
  }

  let emailed = false;
  try {
    const c = await config(env);
    if (c.feedback_mailer_url && c.feedback_mailer_secret) {
      const r = await fetch(c.feedback_mailer_url, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ secret: c.feedback_mailer_secret, id, kind, consent: !!consent, credit, created, name, email, page, message, photos }),
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
