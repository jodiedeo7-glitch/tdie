"""Render every DFY proof sample to PDF.

Usage: python3 render.py [sample_key ...]
Photos: drop a generated image into build/images/<photo id>.jpg (ids are in each *_image-prompts.md)
and re-run; the placeholder is replaced automatically.
"""
import importlib, os, sys, asyncio
from playwright.async_api import async_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
SAMPLES = ["s01_automation", "s02_skool", "s03_instagram", "s04_threads", "s05_pinterest", "s06_repurpose",
           "s07_email", "s08_etsy", "s09_amazon", "s10_persona", "s11_dashboard"]


async def main(keys):
    sys.path.insert(0, HERE)
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=os.environ.get("CHROME", None) or None)
        for k in keys:
            m = importlib.import_module(k)
            html, fname, orient = m.build()
            src = os.path.join(HERE, f"_{k}.html")
            open(src, "w").write(html)
            pg = await b.new_page()
            await pg.goto("file://" + src)
            await pg.evaluate("document.fonts.ready")
            await pg.wait_for_timeout(300)
            await pg.pdf(path=os.path.join(OUT, fname), print_background=True, prefer_css_page_size=True,
                         width="11in" if orient == "landscape" else "8.5in",
                         height="8.5in" if orient == "landscape" else "11in",
                         margin=dict(top="0", right="0", bottom="0", left="0"))
            await pg.close()
            if getattr(m, "PROMPTS", None):
                md = [f"# Image prompts: {fname[:-4]}", "",
                      "Every photo slot in this proof sample, with its complete standalone prompt. "
                      "Generate each image, save it as `build/images/<id>.jpg`, then run `python3 render.py " + k + "` to drop it into the PDF.",
                      "Tool order (TDIE_DESIGN_RULES.md): any image with a person or a persona goes to Google Gemini first with the reference sheet attached, then Nano Banana Pro at 2K on Higgsfield. Any image with no person goes to Seedream 4.5 on Higgsfield. Garbled or unsatisfactory results re-run on Nano Banana Pro at 2K. Never Canva.", ""]
                for pid, title, tool, text in m.PROMPTS:
                    md += [f"## {pid} · {title}", f"Tool: {tool}", "", text, ""]
                open(os.path.join(OUT, fname[:-4] + "_image-prompts.md"), "w").write("\n".join(md))
            print("rendered", fname)
        await b.close()

if __name__ == "__main__":
    asyncio.run(main(sys.argv[1:] or SAMPLES))
