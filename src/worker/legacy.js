import bami from "../../api/bami-waitlist.js";
import complete from "../../api/complete.js";
import dashboard from "../../api/dashboard-stats.js";
import quiz from "../../api/quiz-result.js";
import verify from "../../api/verify.js";
import waitlist from "../../api/waitlist.js";

function makeRes(resolve) {
  const headers = {};
  const res = {
    statusCode: 200,
    status(code){ this.statusCode=code; return this; },
    setHeader(name,value){ headers[name]=value; },
    json(body){ resolve(Response.json(body,{status:this.statusCode,headers})); },
    send(body){ resolve(new Response(body,{status:this.statusCode,headers})); },
    end(body=""){ resolve(new Response(body,{status:this.statusCode,headers})); }
  };
  return res;
}

export async function callLegacy(handler, request) {
  const url = new URL(request.url);
  let body = {};
  if (request.method !== "GET" && request.method !== "HEAD") {
    try { body = await request.json(); } catch {}
  }
  const req = {
    method: request.method,
    body,
    query: Object.fromEntries(url.searchParams.entries()),
    headers: Object.fromEntries(request.headers.entries()),
  };
  return new Promise(async (resolve,reject)=>{
    const res=makeRes(resolve);
    try {
      const out=await handler(req,res);
      if(out instanceof Response) resolve(out);
    } catch(err) { reject(err); }
  });
}

export const legacy = {
  "/api/bami-waitlist": bami,
  "/api/complete": complete,
  "/api/dashboard-stats": dashboard,
  "/api/quiz-result": quiz,
  "/api/verify": verify,
  "/api/waitlist": waitlist,
};
