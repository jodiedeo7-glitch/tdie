import {jsonResponse,methodNotAllowed} from "../http.js";
// The While-You-Sleep Storefront™ waitlist. MailerLite group "WYS Waitlist".
const WYS_WAITLIST_GROUP_ID="200719389134161712";
export async function handle(request,env){
 if(request.method!=="POST")return methodNotAllowed();
 let email="";
 const type=request.headers.get("content-type")||"";
 try{
  if(type.includes("application/json")){const b=await request.json();email=b.email||b["fields[email]"]||"";}
  else{const f=await request.formData();email=f.get("fields[email]")||f.get("email")||"";}
 }catch{}
 email=String(email).trim().toLowerCase();
 if(!email||!email.includes("@")||email.length>200)return jsonResponse({error:"Enter a valid email address."},400);
 try{
  const r=await fetch("https://connect.mailerlite.com/api/subscribers",{method:"POST",headers:{Authorization:`Bearer ${env.MAILERLITE_API_KEY}`,"Content-Type":"application/json",Accept:"application/json"},body:JSON.stringify({email,groups:[WYS_WAITLIST_GROUP_ID]})});
  if(!r.ok)return jsonResponse({error:"Couldn't add you just now. Try again in a moment."},500);
  return jsonResponse({ok:true});
 }catch{return jsonResponse({error:"Couldn't add you just now. Try again in a moment."},500);}
}
