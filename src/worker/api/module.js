import fs from "node:fs";
import path from "node:path";
import { check } from "../../api/verify.js";
import { jsonResponse, methodNotAllowed } from "../http.js";

export async function handle(request, env) {
  if (request.method !== "POST") return methodNotAllowed();
  let body={}; try { body=await request.json(); } catch {}
  const token=body.token||"";
  const slug=String(body.slug||"");
  if(!check(token)) return jsonResponse({error:"unauthorized"},401);
  if(!/^[a-z0-9-]+$/.test(slug)) return jsonResponse({error:"bad slug"},400);

  const file=path.join("/bundle","api","_content",`${slug}.html`);
  if(!fs.existsSync(file)) return jsonResponse({error:"not found"},404);
  return jsonResponse({html:fs.readFileSync(file,"utf8")});
}
