import { handle as wysWorkspace } from "./api/wys-workspace.js";
import { handle as bamiWaitlist } from "./api/bami-waitlist.js";
import { handle as complete } from "./api/complete.js";
import { handle as dashboardStats } from "./api/dashboard-stats.js";
import { handle as moduleContent } from "./api/module.js";
import { handle as quizResult } from "./api/quiz-result.js";
import { handle as sneakPeek } from "./api/sneak-peek.js";
import { handle as verify } from "./api/verify.js";
import { handle as waitlist } from "./api/waitlist.js";

const API = {
  "/api/wys-workspace": wysWorkspace,
  "/api/bami-waitlist": bamiWaitlist,
  "/api/complete": complete,
  "/api/dashboard-stats": dashboardStats,
  "/api/module": moduleContent,
  "/api/quiz-result": quizResult,
  "/api/sneak-peek": sneakPeek,
  "/api/verify": verify,
  "/api/waitlist": waitlist,
};

const PATH_REDIRECTS = new Map([
  ["/weekend-ecosystem/module-17-one-article-thirty-assets","/weekend-ecosystem/module-17-one-article-twenty-four-assets"],
  ["/resources/shopify-store-kit","/resources/shopify-starter-kit"],
  ["/go/8-claude-prompts-that-save-me-12-hours-a-week","/go/the-operating-prompts"],
]);

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (url.pathname.startsWith("/api/")) {
      const handler = API[url.pathname];
      if (!handler) return new Response("Not found", { status: 404 });
      try {
        return await handler(request, env);
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
