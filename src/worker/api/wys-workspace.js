// Unreleased WYS workspace handler. A trusted purchase service must provision
// the wys_customers entitlement row and issue a WYS-scoped token.
import { check } from "../auth.js";
const reply=(body,status=200)=>Response.json(body,{status,headers:{"Cache-Control":"no-store"}});
const fields=new Set(["niche","categories","idea","amazon","destination","pinterest","boards","instagram","mode","cadence","budget","persona"]);
export async function handle(request,env){
  if(!env.WYS_DB||!env.WYS_ACCESS_SECRET)return reply({error:"Not configured"},503);
  const header=request.headers.get("Authorization")||"";
  if(!header.startsWith("Bearer "))return reply({error:"Unauthorized"},401);
  const email=await check(header.slice(7),env.WYS_ACCESS_SECRET);
  if(!email)return reply({error:"Unauthorized"},401);
  const buyer=await env.WYS_DB.prepare("SELECT id FROM wys_customers WHERE email = ?").bind(email).first();
  if(!buyer)return reply({error:"Purchase not verified"},403);
  if(request.method==="GET"){
    const saved=await env.WYS_DB.prepare("SELECT preferences_json,updated_at FROM wys_preferences WHERE customer_id = ?").bind(buyer.id).first();
    return reply({schemaVersion:1,preferences:saved?JSON.parse(saved.preferences_json):{},updatedAt:saved?.updated_at||null});
  }
  if(request.method!=="PUT")return reply({error:"Method not allowed"},405);
  if(request.headers.get("Content-Type")?.split(";")[0].trim().toLowerCase()!=="application/json")return reply({error:"JSON content type required"},415);
  let data;try{data=await request.json()}catch{return reply({error:"Invalid JSON"},400)}
  if(!data||typeof data!=="object"||Array.isArray(data)||!data.preferences||typeof data.preferences!=="object"||Array.isArray(data.preferences))return reply({error:"Invalid preferences"},400);
  if(Object.keys(data.preferences).length>fields.size)return reply({error:"Too many fields"},400);
  const clean={};
  for(const [name,value] of Object.entries(data.preferences)){
    if(!fields.has(name)||typeof value!=="string"||value.length>2000)return reply({error:"Invalid field"},400);
    clean[name]=value;
  }
  const payload=JSON.stringify(clean);
  if(payload.length>12000)return reply({error:"Payload too large"},413);
  await env.WYS_DB.prepare("INSERT INTO wys_preferences(customer_id,schema_version,preferences_json,updated_at) VALUES (?,1,?,CURRENT_TIMESTAMP) ON CONFLICT(customer_id) DO UPDATE SET preferences_json=excluded.preferences_json,updated_at=CURRENT_TIMESTAMP").bind(buyer.id,payload).run();
  return reply({ok:true,schemaVersion:1});
}
