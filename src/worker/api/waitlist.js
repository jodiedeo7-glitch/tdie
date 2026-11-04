import {jsonResponse,methodNotAllowed} from "../http.js";
export async function handle(request,env){
 if(request.method!=="POST")return methodNotAllowed();
 let b={};try{b=await request.json()}catch{}
 const email=String(b.email||"").trim().toLowerCase();
 if(!email||!email.includes("@")||email.length>200)return jsonResponse({error:"Enter a valid email address."},400);
 try{
  const r=await fetch("https://connect.mailerlite.com/api/subscribers",{method:"POST",headers:{Authorization:`Bearer ${env.MAILERLITE_API_KEY}`,"Content-Type":"application/json",Accept:"application/json"},body:JSON.stringify({email,groups:env.MAILERLITE_WAITLIST_GROUP_ID?[env.MAILERLITE_WAITLIST_GROUP_ID]:undefined})});
  if(!r.ok)return jsonResponse({error:"Couldn't add you just now. Try again in a moment."},500);
  return jsonResponse({ok:true});
 }catch{return jsonResponse({error:"Couldn't add you just now. Try again in a moment."},500);}
}
