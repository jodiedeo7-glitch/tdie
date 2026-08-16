#!/usr/bin/env python3
"""
TDIE AUDIT — The Digital Income Edit™
Runs the greppable half of the canon against the repo and the live site.

Replaces, by machine:
  SOP 12 Phase B  (content audit, steps 5–12)
  SOP 8  step 9   (placeholder search) and step 14 (verify live, not preview)
  SOP 6  step 3   (inbound links — the orphan check)
  SOP 7  steps 3–5 (affiliate link + rel=sponsored + disclosure, presence AND absence)
  Standing Rule 32 (every price checked against the collision table)

Usage
  export GH_TOKEN=ghp_...                 # repo mode only; unset when done
  python3 tdie_audit.py --repo
  python3 tdie_audit.py --live
  python3 tdie_audit.py --repo --live --report audit.md

Exit code 1 if any FAIL finding. REVIEW findings do not fail the run.
Stdlib only. No install step.
"""

import argparse
import base64
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from collections import defaultdict
from html.parser import HTMLParser

CANON_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "canon", "canon.json")
UA = "tdie-audit/1.0"

TEXT_EXT = (
    ".astro", ".md", ".mdx", ".html", ".ts", ".tsx", ".js", ".jsx",
    ".json", ".txt", ".yml", ".yaml", ".css", ".xml",
)
SKIP_DIRS = ("node_modules/", ".git/", "dist/", ".vercel/", ".astro/", "public/images/")
SKIP_FILES = ("canon.json", "package-lock.json", "pnpm-lock.yaml", "yarn.lock")


# ─────────────────────────────────────────────────────────────── helpers

def load_canon():
    with open(CANON_PATH, encoding="utf-8") as f:
        return json.load(f)


def get(url, token=None, raw=False, timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    if token:
        req.add_header("Authorization", f"Bearer {token}")
        req.add_header("Accept", "application/vnd.github.raw" if raw else "application/vnd.github+json")
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def line_of(text, idx):
    return text.count("\n", 0, idx) + 1


def excerpt(text, idx, span=60):
    s = max(0, idx - span // 2)
    return re.sub(r"\s+", " ", text[s:idx + span]).strip()


class Findings:
    def __init__(self):
        self.rows = []

    def add(self, level, check, where, line, detail, why=""):
        self.rows.append(
            {"level": level, "check": check, "where": where, "line": line, "detail": detail, "why": why}
        )

    @property
    def fails(self):
        return [r for r in self.rows if r["level"] == "FAIL"]

    @property
    def reviews(self):
        return [r for r in self.rows if r["level"] == "REVIEW"]


# ─────────────────────────────────────────────────────── the scanner core

def scan_text(canon, findings, where, text, published=False):
    """Every string check in one pass over one file or page."""

    for rule in canon["checks"]["fail"]:
        if rule.get("scope") == "published" and not published:
            continue
        for pat in rule["patterns"]:
            for m in re.finditer(pat, text, re.IGNORECASE):
                findings.add("FAIL", rule["id"], where, line_of(text, m.start()),
                             excerpt(text, m.start()), rule["why"])

    for rule in canon["checks"]["review"]:
        prox = rule.get("proximity_to")
        anchors = []
        if prox:
            for a in prox:
                anchors += [m.start() for m in re.finditer(re.escape(a), text)]
            if not anchors:
                continue
        window = rule.get("window", 400)
        for pat in rule["patterns"]:
            for m in re.finditer(pat, text, re.IGNORECASE):
                if prox and not any(abs(m.start() - a) <= window for a in anchors):
                    continue
                findings.add("REVIEW", rule["id"], where, line_of(text, m.start()),
                             excerpt(text, m.start()), rule["why"])

    check_prices(canon, findings, where, text)
    check_affiliates(canon, findings, where, text)


def check_prices(canon, findings, where, text):
    """Standing Rule 32 — every price string checked against the collision table."""
    table = price_table(canon)
    known = set(table.keys())
    for m in re.finditer(r"\$(\d[\d,]*)(?:\.(\d{2}))?", text):
        val = int(m.group(1).replace(",", ""))
        if m.group(2) and m.group(2) != "00":
            findings.add("REVIEW", "price_not_in_register", where, line_of(text, m.start()),
                         f"${m.group(1)}.{m.group(2)} — no product carries this price",
                         "No asset ships a price that is not a Register row.")
            continue
        if val not in known:
            findings.add("REVIEW", "price_not_in_register", where, line_of(text, m.start()),
                         f"${val} — no product in the Register carries this price",
                         "No asset ships a price that is not a Register row.")
            continue
        shared = table[val]
        if len(shared) > 1:
            findings.add("REVIEW", "price_collision", where, line_of(text, m.start()),
                         f"${val} is shared by {len(shared)}: " + " · ".join(shared),
                         "Name what this price buys before the reader has to work it out.")


def price_table(canon):
    t = defaultdict(list)
    for p in canon["ladder"] + canon["products"]:
        if p.get("price") is None:
            continue
        label = p["name"]
        if p.get("recurring"):
            label += " (recurring)"
        t[p["price"]].append(label)
    return t


def check_affiliates(canon, findings, where, text):
    """Standing Rule 18 — link, rel=sponsored, and disclosure ship as a set or not at all."""
    rule = canon["affiliate_rule"]
    has_disclosure = any(k.lower() in text.lower() for k in rule["disclosure_markers"])
    for p in canon["products"]:
        if p.get("owned", True) or not p.get("url"):
            continue
        for m in re.finditer(re.escape(p["url"]), text):
            ln = line_of(text, m.start())
            ctx = text[max(0, m.start() - 400): m.start() + 400]
            if "sponsored" not in ctx.lower():
                findings.add("FAIL", "affiliate_missing_rel", where, ln,
                             f'{p["name"]} — no rel="sponsored" within 400 chars', rule["requirement"])
            if not has_disclosure:
                findings.add("FAIL", "affiliate_missing_disclosure", where, ln,
                             f'{p["name"]} — no disclosure anywhere on this page', rule["requirement"])


# ────────────────────────────────────────────────────────────── repo mode

def audit_repo(canon, findings, token, branch="main"):
    repo = canon["meta"]["repo"]
    ref = json.loads(get(f"https://api.github.com/repos/{repo}/git/ref/heads/{branch}", token))
    sha = ref["object"]["sha"]
    tree = json.loads(get(f"https://api.github.com/repos/{repo}/git/trees/{sha}?recursive=1", token))

    if tree.get("truncated"):
        print("  ! tree truncated — some files not scanned", file=sys.stderr)

    paths = [
        n["path"] for n in tree["tree"]
        if n["type"] == "blob"
        and n["path"].endswith(TEXT_EXT)
        and not any(n["path"].startswith(d) or f"/{d}" in n["path"] for d in SKIP_DIRS)
        and os.path.basename(n["path"]) not in SKIP_FILES
    ]
    print(f"  repo {repo}@{branch}  {len(paths)} text files")

    blobs = {n["path"]: n["sha"] for n in tree["tree"] if n["type"] == "blob"}
    for i, path in enumerate(paths, 1):
        try:
            data = json.loads(get(f"https://api.github.com/repos/{repo}/git/blobs/{blobs[path]}", token))
            text = base64.b64decode(data["content"]).decode("utf-8", "replace")
        except Exception as e:
            findings.add("REVIEW", "unreadable", path, 0, str(e), "")
            continue
        scan_text(canon, findings, f"repo:{path}", text, published=True)
        if i % 25 == 0:
            print(f"    {i}/{len(paths)}")
    return paths


# ────────────────────────────────────────────────────────────── live mode

class LinkGrab(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.title = ""
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == "a" and d.get("href"):
            self.links.append((d["href"], d.get("rel", "")))
        if tag == "title":
            self._in_title = True

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data


def audit_live(canon, findings, limit=None):
    host = canon["meta"]["canonical_host"]
    try:
        sm = get(f"{host}/sitemap-index.xml").decode("utf-8", "replace")
        subs = re.findall(r"<loc>(.*?)</loc>", sm)
        urls = []
        for s in subs:
            urls += re.findall(r"<loc>(.*?)</loc>", get(s).decode("utf-8", "replace"))
    except Exception:
        sm = get(f"{host}/sitemap.xml").decode("utf-8", "replace")
        urls = re.findall(r"<loc>(.*?)</loc>", sm)

    urls = sorted(set(u for u in urls if u.startswith(host)))
    if limit:
        urls = urls[:limit]
    print(f"  live {host}  {len(urls)} pages in sitemap")

    inbound = defaultdict(set)
    outbound = defaultdict(set)
    external = set()

    for i, url in enumerate(urls, 1):
        try:
            html = get(url).decode("utf-8", "replace")
        except Exception as e:
            findings.add("FAIL", "page_unreachable", url, 0, str(e), "In the sitemap and not serving.")
            continue
        scan_text(canon, findings, url, html, published=True)

        g = LinkGrab()
        g.feed(html)
        path = url[len(host):] or "/"
        for href, rel in g.links:
            if href.startswith("/"):
                tgt = href.split("#")[0].split("?")[0].rstrip("/") or "/"
                outbound[path].add(tgt)
                inbound[tgt].add(path)
            elif href.startswith("http") and host not in href:
                external.add(href.split("#")[0])
        if i % 20 == 0:
            print(f"    {i}/{len(urls)}")

    # SOP 6 — the orphan check. Outbound always gets done; inbound never does.
    for p in canon["pillars"]:
        slug = p["slug"].rstrip("/")
        if slug not in inbound or not inbound[slug]:
            findings.add("FAIL", "orphan_no_inbound", host + slug, 0,
                         f'Pillar {p["n"]} — {p["name"]}: nothing on the site links to it',
                         "SOP 6 step 3. An orphan with good manners.")
    for path in outbound:
        if path in ("/",):
            continue
        if not inbound.get(path):
            findings.add("REVIEW", "orphan_no_inbound", host + path, 0,
                         "No internal page links to this page",
                         "Reachable only from the sitemap.")

    # every external link resolves — money links first
    money = [u for u in external if "links.thedigitalincomeedit.com" in u or "skool.com" in u]
    other = [u for u in sorted(external) if u not in money]
    for u in money:
        findings.add("REVIEW", "link_unverifiable", u, 0,
                     "Beacons/Skool link — not fetchable by tooling, verify by hand",
                     "links.* is not indexed and does not resolve via fetch.")
    for u in other:
        code = head(u)
        if code is None or code >= 400:
            findings.add("FAIL", "link_dead", u, 0, f"HTTP {code}", "Outbound link does not resolve.")
        time.sleep(0.15)

    return urls


def head(url):
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA}, method=method)
            with urllib.request.urlopen(req, timeout=15) as r:
                return r.status
        except urllib.error.HTTPError as e:
            if method == "GET" or e.code != 405:
                return e.code
        except Exception:
            return None
    return None


# ───────────────────────────────────────────────────────────────── report

def report(canon, findings, path=None):
    by_check = defaultdict(list)
    for r in findings.rows:
        by_check[(r["level"], r["check"])].append(r)

    out = ["# TDIE audit", "", f'Canon v{canon["meta"]["canon_version"]} · {time.strftime("%Y-%m-%d %H:%M")}', "",
           f"**{len(findings.fails)} FAIL · {len(findings.reviews)} REVIEW**", ""]

    for level in ("FAIL", "REVIEW"):
        groups = [(k, v) for k, v in by_check.items() if k[0] == level]
        if not groups:
            continue
        out.append(f"## {level}")
        out.append("")
        for (_, check), rows in sorted(groups, key=lambda x: -len(x[1])):
            out.append(f"### {check} — {len(rows)}")
            if rows[0]["why"]:
                out.append(f"*{rows[0]['why']}*")
            out.append("")
            for r in rows[:40]:
                loc = f'{r["where"]}:{r["line"]}' if r["line"] else r["where"]
                out.append(f'- `{loc}` — {r["detail"]}')
            if len(rows) > 40:
                out.append(f"- …and {len(rows) - 40} more")
            out.append("")

    if not findings.rows:
        out.append("Clean.")

    text = "\n".join(out)
    if path:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"\n  report → {path}")
    else:
        print("\n" + text)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", action="store_true")
    ap.add_argument("--live", action="store_true")
    ap.add_argument("--branch", default="main")
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--report", default=None)
    a = ap.parse_args()

    if not (a.repo or a.live):
        ap.error("pick --repo, --live, or both")

    canon = load_canon()
    findings = Findings()

    if a.repo:
        token = os.environ.get("GH_TOKEN") or os.environ.get("GH")
        if not token:
            sys.exit("GH_TOKEN not set. Generate a fine-grained read-only token, run, then revoke it.")
        audit_repo(canon, findings, token, a.branch)

    if a.live:
        audit_live(canon, findings, a.limit)

    report(canon, findings, a.report)
    print(f"\n  {len(findings.fails)} FAIL · {len(findings.reviews)} REVIEW")
    sys.exit(1 if findings.fails else 0)


if __name__ == "__main__":
    main()
