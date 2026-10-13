// Jodie's private inbox for the buyer-website box. Needs the inbox key (kept in the
// database's config table) in the X-Inbox-Key header. GET lists messages; ?photo=ID returns one photo.
import { jsonResponse, methodNotAllowed } from "../http.js";

export async function handle(request, env) {
  if (request.method !== "GET") return methodNotAllowed();
  if (!env.DB) return jsonResponse({ error: "Not connected." }, 503);
  const key = request.headers.get("X-Inbox-Key") || "";
  const row = await env.DB.prepare("SELECT value FROM config WHERE key='inbox_key'").first();
  if (!row?.value || key !== row.value) return jsonResponse({ error: "That key doesn't match." }, 401);
  const url = new URL(request.url);
  const photo = url.searchParams.get("photo");
  if (photo) {
    const p = await env.DB.prepare("SELECT type, b64 FROM wys_feedback_photos WHERE id=?").bind(Number(photo)).first();
    if (!p) return jsonResponse({ error: "Not found." }, 404);
    const bytes = Uint8Array.from(atob(p.b64), c => c.charCodeAt(0));
    return new Response(bytes, { headers: { "Content-Type": p.type || "image/jpeg", "Cache-Control": "private, max-age=86400" } });
  }
  const { results } = await env.DB.prepare(
    "SELECT f.id, f.created_at, f.kind, f.name, f.email, f.page, f.message, f.consent, f.credit, f.emailed, f.photo_b64 IS NOT NULL AS legacy_photo, " +
    "(SELECT group_concat(p.id) FROM wys_feedback_photos p WHERE p.feedback_id=f.id ORDER BY p.idx) AS photo_ids " +
    "FROM wys_feedback f ORDER BY f.id DESC LIMIT 300"
  ).all();
  return jsonResponse({ items: (results || []).map(r => ({ ...r, photo_ids: r.photo_ids ? String(r.photo_ids).split(",").map(Number) : [] })) });
}
