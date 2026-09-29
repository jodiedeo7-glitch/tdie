import { legacy, callLegacy } from "./legacy.js";
import { handle as moduleHandler } from "./api/module.js";
import { handle as sneakPeekHandler } from "./api/sneak-peek.js";

const PATH_REDIRECTS = new Map([
  ["/weekend-ecosystem/module-17-one-article-thirty-assets","/weekend-ecosystem/module-17-one-article-twenty-four-assets"],
  ["/resources/shopify-store-kit","/resources/shopify-starter-kit"],
  ["/go/8-claude-prompts-that-save-me-12-hours-a-week","/go/the-operating-prompts"],
]);

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (url.pathname.startsWith("/api/")) {
      try {
        if (url.pathname === "/api/module") return await moduleHandler(request, env);
        if (url.pathname === "/api/sneak-peek") return await sneakPeekHandler(request, env);
        const handler = legacy[url.pathname];
        if (handler) return await callLegacy(handler, request);
        return new Response("Not found", { status: 404 });
      } catch (error) {
        console.error("API error", url.pathname, error);
        return Response.json({ error: "Internal server error" }, { status: 500 });
      }
    }

    const redirect = PATH_REDIRECTS.get(url.pathname);
    if (redirect) {
      const target = new URL(redirect, url.origin);
      target.search = url.search;
      return Response.redirect(target.toString(), 301);
    }

    return env.ASSETS.fetch(request);
  },
};
