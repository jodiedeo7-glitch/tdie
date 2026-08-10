// /api/pinterest-callback
// Receives the OAuth redirect from Pinterest after the user authorizes the app,
// exchanges the returned authorization code for an access token, and stores it.
//
// Required environment variables (set in Vercel project settings):
//   PINTEREST_APP_ID
//   PINTEREST_APP_SECRET
//   PINTEREST_REDIRECT_URI   (must exactly match what's registered in the Pinterest app, e.g.
//                              https://www.thedigitalincomeedit.com/api/pinterest-callback)

import type { APIRoute } from 'astro';

export const GET: APIRoute = async ({ url, redirect }) => {
  const code = url.searchParams.get('code');
  const error = url.searchParams.get('error');

  if (error) {
    return new Response(
      `Pinterest authorization failed: ${error}`,
      { status: 400 }
    );
  }

  if (!code) {
    return new Response('Missing authorization code from Pinterest.', { status: 400 });
  }

  const appId = import.meta.env.PINTEREST_APP_ID;
  const appSecret = import.meta.env.PINTEREST_APP_SECRET;
  const redirectUri = import.meta.env.PINTEREST_REDIRECT_URI;

  if (!appId || !appSecret || !redirectUri) {
    return new Response(
      'Server is missing Pinterest API credentials. Set PINTEREST_APP_ID, PINTEREST_APP_SECRET, and PINTEREST_REDIRECT_URI in Vercel environment variables.',
      { status: 500 }
    );
  }

  const basicAuth = Buffer.from(`${appId}:${appSecret}`).toString('base64');

  try {
    const tokenResponse = await fetch('https://api.pinterest.com/v5/oauth/token', {
      method: 'POST',
      headers: {
        'Authorization': `Basic ${basicAuth}`,
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: new URLSearchParams({
        grant_type: 'authorization_code',
        code,
        redirect_uri: redirectUri,
      }),
    });

    const tokenData = await tokenResponse.json();

    if (!tokenResponse.ok) {
      return new Response(
        `Pinterest token exchange failed: ${JSON.stringify(tokenData)}`,
        { status: tokenResponse.status }
      );
    }

    // tokenData contains: access_token, refresh_token, expires_in, scope, token_type
    // TODO: persist tokenData securely (e.g. encrypted in your database or secrets store).
    // Never log or expose access_token / refresh_token in a public response.

    return new Response(
      `Pinterest connected successfully. You can close this tab.`,
      { status: 200, headers: { 'Content-Type': 'text/plain' } }
    );
  } catch (err) {
    return new Response(
      `Unexpected error during Pinterest token exchange: ${err instanceof Error ? err.message : String(err)}`,
      { status: 500 }
    );
  }
};
