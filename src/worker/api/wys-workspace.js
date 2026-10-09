// Private WYS customer workspace endpoint. Not registered for production.
export async function handle(request, env) {
  if (!env.WYS_DB) return Response.json({error: 'Not configured'}, {status: 503});
  return Response.json({error: 'Purchase verification required'}, {status: 403});
}
