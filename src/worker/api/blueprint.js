import {jsonResponse,methodNotAllowed} from "../http.js";
// Free downloads delivered on the site. Adds the email to that freebie's
// MailerLite group and hands the file over on screen straight away, so
// delivery never depends on an email arriving. Served at /api/blueprint.
const FREEBIES={
 "blueprint":{group:"200887878817940879",file:"/downloads/the-faceless-income-blueprint.pdf"},
 "ai-starter-kit":{group:"200894937733006762",file:"/downloads/the-ai-starter-kit.pdf"},
 "automation-kit":{group:"200894939716912725",file:"/downloads/the-automation-kit.pdf"},
 "branding-kit":{group:"200894941608543725",file:"/downloads/the-branding-kit.pdf"},
 "content-creation-kit":{group:"200894943533729602",file:"/downloads/the-content-creation-kit.pdf"},
 "mindset-kit":{group:"200894945530218312",file:"/downloads/the-mindset-kit.pdf"},
 "email-starter-kit":{group:"200894947585427047",file:"/downloads/the-email-starter-kit.pdf"},
 "blogging-kit":{group:"200894949355422909",file:"/downloads/the-blogging-kit.pdf"},
 "digital-products-kit":{group:"200894951401195204",file:"/downloads/the-digital-products-kit.pdf"},
 "affiliate-starter-kit":{group:"200894953378808915",file:"/downloads/the-affiliate-starter-kit.pdf"},
 "passive-income-kit":{group:"200894955250517958",file:"/downloads/the-passive-income-kit.pdf"},
 "pinterest-traffic-kit":{group:"200894957651756422",file:"/downloads/the-pinterest-traffic-kit.pdf"},
 "business-systems-kit":{group:"200894959714305898",file:"/downloads/the-business-systems-kit.pdf"},
 "wys-waitlist":{group:"200719389134161712",file:null},
};
export async function handle(request,env){
 if(request.method!=="POST")return methodNotAllowed();
 let b={};try{b=await request.json()}catch{}
 const email=String(b.email||"").trim().toLowerCase();
 const f=FREEBIES[String(b.kit||"blueprint")]||FREEBIES.blueprint;
 if(!email||!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)||email.length>200)return jsonResponse({error:"Enter a valid email address."},400);
 let saved=false;
 try{
  const r=await fetch("https://connect.mailerlite.com/api/subscribers",{method:"POST",headers:{Authorization:`Bearer ${env.MAILERLITE_API_KEY}`,"Content-Type":"application/json",Accept:"application/json"},body:JSON.stringify({email,groups:[f.group]})});
  saved=r.ok;
 }catch{}
 return jsonResponse({ok:true,saved,file:f.file});
}
