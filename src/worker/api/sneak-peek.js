import fs from "node:fs";
import path from "node:path";
import { check, sign } from "../../api/verify.js";
import { jsonResponse, methodNotAllowed } from "../http.js";

export async function handle(request, env) {
  const url=new URL(request.url);
  const file=path.join("/bundle","api","_content","pretty-and-paid-plr-vault-sneak-peek.pdf");

  if(request.method==="GET"){
    const token=String(url.searchParams.get("t")||"");
    if(!check(token)) return new Response("This link has expired. Enter your email again to get a fresh one.",{status:401});
    if(!fs.existsSync(file)) return new Response("Not found",{status:404});
    return new Response(fs.readFileSync(file),{status:200,headers:{
      "Content-Type":"application/pdf",
      "Content-Disposition":'inline; filename="Pretty-and-Paid-PLR-Vault-Sneak-Peek.pdf"',
      "Cache-Control":"private, no-store",
      "X-Robots-Tag":"noindex, nofollow"
    }});
  }

  if(request.method!=="POST") return methodNotAllowed();
  let body={}; try { body=await request.json(); } catch {}
  const email=String(body.email||"").trim().toLowerCase();
  if(!email||!email.includes("@")||email.length>200)return jsonResponse({error:"Enter a valid email address."},400);

  try{
    const r=await fetch("https://connect.mailerlite.com/api/subscribers",{method:"POST",headers:{
      Authorization:`Bearer ${env.MAILERLITE_API_KEY}`,"Content-Type":"application/json",Accept:"application/json"
    },body:JSON.stringify({email,groups:env.MAILERLITE_SNEAKPEEK_GROUP_ID?[env.MAILERLITE_SNEAKPEEK_GROUP_ID]:undefined})});
    if(!r.ok)return jsonResponse({error:"Couldn't add you just now. Try again in a moment."},500);
    return jsonResponse({url:`/api/sneak-peek?t=${sign(email)}`});
  }catch{return jsonResponse({error:"Couldn't add you just now. Try again in a moment."},500);}
}
