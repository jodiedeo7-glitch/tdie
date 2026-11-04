// The While-You-Sleep Storefront™ free guide. Handed out only after someone joins the WYS Waitlist
// (the page shows this link after signup, and the MailerLite "WYS Waitlist — Free Guide" email carries it).
// To swap in a new guide: replace api/_content/wys-free-guide.pdf on the cloudflare-migration branch. Nothing else changes.
export const WYS_GUIDE_KEY="VOk-I7sWghoIWzYBxc6wLgYw";
export const WYS_GUIDE_PATH="/api/wys-guide?k="+WYS_GUIDE_KEY;
const PDF_URL="https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/cloudflare-migration/api/_content/wys-free-guide.pdf";
export async function handle(request){
 const url=new URL(request.url);
 if(request.method!=="GET")return new Response("Method not allowed",{status:405});
 if(url.searchParams.get("k")!==WYS_GUIDE_KEY)return Response.redirect(new URL("/shop/while-you-sleep-storefront/waitlist",url.origin).toString(),302);
 const pdf=await fetch(PDF_URL,{cf:{cacheTtl:300,cacheEverything:true}});
 if(!pdf.ok)return new Response("The guide is temporarily unavailable. Try again in a minute.",{status:503});
 return new Response(pdf.body,{status:200,headers:{"Content-Type":"application/pdf","Content-Disposition":'inline; filename="The-While-You-Sleep-Storefront-Free-Guide.pdf"',"Cache-Control":"private, max-age=300","X-Robots-Tag":"noindex, nofollow"}});
}
