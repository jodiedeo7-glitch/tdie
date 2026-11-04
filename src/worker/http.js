export async function json(request) {
  try { return await request.json(); } catch { return {}; }
}
export function jsonResponse(body,status=200,headers={}) {
  return Response.json(body,{status,headers:{"Cache-Control":"no-store",...headers}});
}
export function textResponse(body,status=200,headers={}) {
  return new Response(body,{status,headers:{"Cache-Control":"no-store",...headers}});
}
export function methodNotAllowed(){ return jsonResponse({error:"Method not allowed"},405); }
