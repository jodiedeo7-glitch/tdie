import {jsonResponse,methodNotAllowed} from "../http.js";
const STAGES=new Set(["No business yet","An idea, nothing built","Something built that isn't selling","Something selling that won't scale"]);
export async function handle(request,env){
 if(request.method!=="POST")return methodNotAllowed();
 let b={};try{b=await request.json()}catch{}
 const email=String(b.email||"").trim().toLowerCase(),name=String(b.name||"").trim().slice(0,80),stageRaw=String(b.stage||"").trim();
 const stage=STAGES.has(stageRaw)?stageRaw:"";
 if(!email||!email.includes("@")||email.length>200)return jsonResponse({error:"Enter a valid email address."},400);
 try{
  const r=await fetch("https://connect.mailerlite.com/api/subscribers",{method:"POST",headers:{Authorization:`Bearer ${env.MAILERLITE_API_KEY}`,"Content-Type":"application/json",Accept:"application/json"},body:JSON.stringify({email,fields:{name,bami_stage:stage},groups:env.MAILERLITE_BAMI_WAITLIST_GROUP_ID?[env.MAILERLITE_BAMI_WAITLIST_GROUP_ID]:undefined})});
  if(!r.ok)return jsonResponse({error:"Couldn't add you just now. Try again in a moment."},500);
  return jsonResponse({ok:true});
 }catch{return jsonResponse({error:"Couldn't add you just now. Try again in a moment."},500);}
}
