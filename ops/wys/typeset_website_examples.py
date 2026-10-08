from pathlib import Path
import base64,json,html,hashlib
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'src/assets/wys/examples';OUT.mkdir(parents=True,exist_ok=True)
def data(path,mime):return 'data:'+mime+';base64,'+base64.b64encode(path.read_bytes()).decode()
news=data(ROOT/'node_modules/@fontsource/newsreader/files/newsreader-latin-600-normal.woff2','font/woff2');inter=data(ROOT/'node_modules/@fontsource/inter/files/inter-latin-600-normal.woff2','font/woff2')
roles=['basic','styled','lifestyle'];receipts=[]
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 for slug,name,theme in [('pretty-wicked-entryway','Pretty Wicked','Pink Halloween entryway'),('ghoul-fuel-coffee-bar','Ghoul Fuel','Pink Halloween coffee bar')]:
  phrases=['The little pink pieces','Style a cute little haunt','A little everyday magic'] if slug.startswith('pretty') else ['Coffee with a little haunt','A pink coffee corner','Your cutest coffee moment']
  for channel,w,h in [('pin',1000,1500),('instagram',1080,1350)]:
   for n,role in enumerate(roles):
    source=ROOT/'src/lifestyle'/f'{slug}-{role}.png';photo=data(source,'image/png');bg=['#FFE3EF','#F1EAFB','#FFD0E3'][n];rim=['#E891B6','#BCA1DE','#D62E73'][n]
    markup=f'''<!doctype html><html><style>@font-face{{font-family:Newsreader;src:url({news});font-weight:600}}@font-face{{font-family:Inter;src:url({inter});font-weight:600}}*{{box-sizing:border-box}}body{{margin:0;width:{w}px;height:{h}px;background:{bg};padding:40px 48px;color:#1A1417;font-family:Inter;display:flex;flex-direction:column;align-items:center;gap:20px}}.brand{{font-size:19px;letter-spacing:4px;text-transform:uppercase}}.mat{{flex:1;min-height:0;align-self:stretch;display:flex;justify-content:center;align-items:center;border:3px double {rim};border-radius:{'110px 110px 16px 16px' if n==1 else '16px'};padding:20px;background:#FFFCFE;box-shadow:0 12px 30px #B8245F22}}img{{width:100%;height:100%;object-fit:contain}}h1{{font:600 {70 if channel=='pin' else 64}px/1.04 Newsreader;margin:0;text-align:center;color:#B8245F}}.topic{{font-size:21px;letter-spacing:2px;text-align:center}}.foot{{width:100%;display:flex;justify-content:space-between;font-size:17px;padding-top:14px;border-top:1px solid {rim}}}</style><body><div class="brand">The Digital Income Edit™</div><h1>{html.escape(phrases[n])}</h1><div class="topic">{html.escape(theme)}</div><div class="mat"><img src="{photo}"/></div><div class="foot"><span>{html.escape(name)} · {role.capitalize()} view</span><span>{'Styling inspiration' if channel=='pin' else f'{n+1} / 3'}</span></div></body></html>'''
    page=browser.new_page(viewport={'width':w,'height':h},device_scale_factor=1);page.set_content(markup);page.evaluate('document.fonts.ready');page.locator('img').evaluate('(i)=>i.decode()');path=OUT/f'{slug}-{channel}-{n+1}.png';page.screenshot(path=str(path));page.close();receipts.append({'file':path.name,'source':source.name,'sourceSHA256':hashlib.sha256(source.read_bytes()).hexdigest(),'width':w,'height':h,'method':'Deterministic HTML typesetting from approved, unchanged photograph; new website worked-example graphic, not an original archive graphic','photoRole':role,'overlay':phrases[n]})
 browser.close()
(ROOT/'docs/design/WYS_EXAMPLE_GRAPHICS_2026-10-08.json').write_text(json.dumps(receipts,indent=2))
print('Built',len(receipts),'finished example graphics')
