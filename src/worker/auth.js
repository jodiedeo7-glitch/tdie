const TTL_DAYS=30;
function enc(bytes){let s="";for(const b of bytes)s+=String.fromCharCode(b);return btoa(s).replace(/\+/g,"-").replace(/\//g,"_").replace(/=+$/g,"");}
function dec(value){const b=value.replace(/-/g,"+").replace(/_/g,"/")+"=".repeat((4-value.length%4)%4);const s=atob(b);return Uint8Array.from(s,c=>c.charCodeAt(0));}
async function hkey(secret){return crypto.subtle.importKey("raw",new TextEncoder().encode(secret||""),{name:"HMAC",hash:"SHA-256"},false,["sign","verify"]);}
export async function sign(email,secret){
 const exp=Date.now()+TTL_DAYS*86400000;
 const payload=`${String(email).toLowerCase()}|${exp}`;
 const sig=new Uint8Array(await crypto.subtle.sign("HMAC",await hkey(secret),new TextEncoder().encode(payload)));
 return enc(new TextEncoder().encode(`${payload}|${enc(sig)}`));
}
export async function check(token,secret){
 try{
  const raw=new TextDecoder().decode(dec(String(token)));
  const [email,exp,sig]=raw.split("|");
  if(!email||!exp||!sig||Date.now()>Number(exp))return null;
  const valid=await crypto.subtle.verify("HMAC",await hkey(secret),dec(sig),new TextEncoder().encode(`${email}|${exp}`));
  return valid?email:null;
 }catch{return null;}
}
