"""Run after astro build. Verify the generated Lifestyle pages and legacy preservation."""
import json,re,subprocess
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse,unquote
ROOT=Path(__file__).resolve().parents[2];DIST=ROOT/'dist'
class Page(HTMLParser):
 def __init__(self,text):
  super().__init__();self.links=[];self.linkAttrs=[];self.images=[];self.ids=[];self.canonical=[];self.titles=0;self.headings=0;self.forms=[];self.ld=[];self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if a.get('id'):self.ids.append(a['id'])
  if tag=='a':self.links.append(a.get('href',''));self.linkAttrs.append(a)
  if tag=='img':self.images.append(a)
  if tag=='link' and a.get('rel')=='canonical':self.canonical.append(a['href'])
  if tag=='title':self.titles+=1
  if tag=='h1':self.headings+=1
  if tag=='form' and 'data-pf' in a:self.forms.append(a)
  if tag=='script' and a.get('type')=='application/ld+json':self.ld.append(True)
records=[json.loads(p.read_text()) for p in (ROOT/'src/lifestyle').glob('*.json')]
public=[r for r in records if r.get('status') not in ['draft','STAGED_NOT_PUBLIC'] and not r.get('draft')]
drafts=[r for r in records if r not in public]
pages=list((DIST/'lifestyle').rglob('index.html'))
assert len(pages)==len(public)+12,(len(pages),len(public))
checks=0
for file in pages:
 text=file.read_text();page=Page(text);path='/' + str(file.parent.relative_to(DIST))
 assert page.canonical==['https://www.thedigitalincomeedit.com'+path],file
 assert page.titles==page.headings==1,file
 assert len(page.forms)==1,file
 assert len(page.ids)==len(set(page.ids)),file
 assert page.ld,file
 for block in re.findall(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',text,re.S):json.loads(block)
 assert 'As an Amazon Associate I earn from qualifying purchases.' in text,file
 assert 'Retail products may differ' in text,file
 assert 'Every link on this page is an affiliate link' not in text,file
 for img in page.images:
  if img.get('width')=='1' and img.get('height')=='1' and 'display:none' in img.get('style',''):continue
  assert img.get('alt') and int(img.get('width','0'))>0 and int(img.get('height','0'))>0,file
  if img['src'].startswith('/') and not img['src'].startswith('/@'): assert (DIST/unquote(urlparse(img['src']).path.lstrip('/'))).is_file(),(file,img['src'])
 for href in page.links:
  if href.startswith('/'):
   target=urlparse(href);pathname=target.path.rstrip('/') or '/';base=DIST/pathname.lstrip('/')
   assert pathname.startswith('/api/') or base.is_file() or base.with_suffix('.html').is_file() or (base/'index.html').is_file(),(file,href)
   if target.fragment and pathname==path:assert target.fragment in page.ids,(file,href)
 assert not re.search(r'ops/private|C:[/\\]|sourcing-evidence\.json|STAGED_NOT_PUBLIC|REJECTED_STALE_LINK',text),file
 checks+=1
for record in public:
 file=DIST/'lifestyle'/record['slug']/'index.html';text=file.read_text();page=Page(text)
 if record.get('shoppingStatus')=='pending':
  assert len([im for im in page.images if record['slug'] in unquote(im['src'])])==3,record['slug']
  assert 'Product links are still being verified.' in text,record['slug']
  assert not any('amazon.com' in a.get('href','') or 'amzn.to' in a.get('href','') for a in page.linkAttrs),record['slug']
  assert '/lifestyle/'+record['slug'] in (DIST/'sitemap-0.xml').read_text(),record['slug']
  continue
 original=json.loads(subprocess.check_output(['git','show','HEAD:src/lifestyle/'+record['slug']+'.json'],cwd=ROOT,text=True))
 assert record==original,record['slug']
 for item in record['items']:
  assert item['link'].replace('&','&amp;') in text,(record['slug'],item['name'])
  destination=next(a for a in page.linkAttrs if a.get('href')==item['link'])
  assert 'sponsored' in destination.get('rel','').split() and destination.get('target')=='_blank',(record['slug'],item['name'])
 assert record['ideaList'] in text,record['slug']
 assert len([im for im in page.images if record['slug'] in unquote(im['src'])])>=len(record['images']),record['slug']
sitemap=(DIST/'sitemap-0.xml').read_text()
for draft in drafts:
 assert not (DIST/'lifestyle'/draft['slug']/'index.html').exists(),draft['slug']
 assert '/lifestyle/'+draft['slug'] not in sitemap,draft['slug']
 for file in pages:assert '/lifestyle/'+draft['slug'] not in file.read_text(),(file,draft['slug'])
print(json.dumps({'generatedLifestylePages':checks,'legacyRecordsUnchanged':len([r for r in public if r.get('shoppingStatus')!='pending']), 'publishedPendingShoppingArticles':len([r for r in public if r.get('shoppingStatus')=='pending']),'draftRoutesExcluded':len(drafts),'canonicalLinksImagesFormsSitemap':'PASS'},indent=2))

for draft in drafts:
 for image in draft.get('images', []):
  stem=Path(image['file']).stem
  assert not any(stem in asset.name for asset in DIST.rglob('*') if asset.is_file()), ('Private draft asset emitted', stem)
print('Private draft photographs excluded from production assets: PASS')
