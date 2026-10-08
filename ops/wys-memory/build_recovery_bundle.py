from pathlib import Path
import json, shutil, hashlib, html, re, zipfile
from PIL import Image

REPO = Path(__file__).resolve().parents[2]
ROOT = REPO.parent
DEST = REPO / 'ops/wys-memory/2026-10-07-recovered-spec'
PRIVATE = REPO / 'ops/private/wys-board-test-2026-10-06'
SPRINT = PRIVATE / 'halloween-sprint-restart-20261007'
manifest = []

def copy_file(src, dst, role):
    assert src.is_file(), str(src)
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        assert dst.read_bytes() == src.read_bytes(), f'Never overwrite differing source: {dst}'
    else:
        shutil.copyfile(src, dst)
    sha = hashlib.sha256(src.read_bytes()).hexdigest()
    assert hashlib.sha256(dst.read_bytes()).hexdigest() == sha
    item = {'file': dst.relative_to(DEST).as_posix(), 'original_filename': src.name,
            'source': str(src), 'sha256': sha, 'bytes': src.stat().st_size, 'role': role}
    if src.suffix.lower() in ['.png','.webp','.jpg','.jpeg']:
        with Image.open(src) as im: item['dimensions'] = list(im.size)
        item['usage'] = 'Private repair reference; not blanket authorization for public promotion or retailer-photo republication.'
    manifest.append(item)

refs = ['ee6d299b-10e8-4392-a9ff-29cb6d4f1d57','d6d6aae2-c4fb-4646-b94f-6892d26d7c50','e0532571-f859-47aa-8606-8f0eb27574a9','1299ee19-12a1-4d9d-92a0-9b965b78e951','157bf723-6690-4e48-8b9f-4f2d835a56a8','3292b521-5fa2-4c7f-b4f0-9eca3a21a0ad','dc27bf2c-79c6-4492-998a-17ee8ab0d88d','7d303a5c-cb4c-4e6a-8c3d-7c48657c1173','70943d3a-0b40-4542-8d69-0c8a1eacb5ba','391058be-f698-48a8-9c1c-07a75338e836','725dcdda-d206-4185-89f1-546ff7a99c24','16b648b4-bf3f-4138-a806-3ea0d6b0ac3d','20874868-358f-4300-b65b-c769b4d3df81']
for n, ref in enumerate(refs, 1):
    src = Path('C:/Users/Jodie/AppData/Local/Temp') / f'codex-clipboard-{ref}.png'
    copy_file(src, DEST/'original-clothing-references'/src.name, f'Original clothing reference {n}; style evidence, not product inventory; last duplicates reference 6')
nonfashion_refs = ['a68ea6de-072c-4051-b1de-bdcd2e64c591','278f1be0-27b0-45d9-b2f3-fa9da2611528','3d31acd2-3779-4bf1-82bc-3eb3f658a3ae','50eb5c72-bca1-4bdb-a470-46180c71fa85','6e372a35-20cb-4716-a4c2-27fd7aab2bc1','1e72dda1-e4ba-420f-8b7b-e414927d95ed','2ffe63a8-a78b-4208-b754-f685cc6383d3']
for ref in nonfashion_refs:
    src = Path('C:/Users/Jodie/AppData/Local/Temp') / f'codex-clipboard-{ref}.png'
    copy_file(src, DEST/'original-nonfashion-references'/src.name, 'Original workspace/atmosphere reference; category-scoped vibe evidence, NOT clothing-role authority')
for f in ['basic.webp','styled.webp','lifestyle.png','acceptance-and-qa.json']:
    copy_file(PRIVATE/'approved-cardigan-benchmark'/f, DEST/'approved-cardigan'/f, 'Approved mock visual direction with scoped defects; not production certification')
for f in ['mock-five-basic.txt','mock-five-basic-v02.txt','cardigan-final-styled.txt','cardigan-final-lifestyle.txt','cardigan-final-preflight.json','styled-accessory-rejection.json','styled-headset-rejection.json','desk-outfit-rejection.json','six-panel-treatment-audit.json','porch-personalization-audit.json','final-style-and-handoff-audit.json','category-prompt-validation.json','tommy-kate-review-package.json','contents-and-scene-audit.json','maximalist-pair-review.json']:
    copy_file(PRIVATE/f, DEST/'historical-prompts'/f, 'Historical prompt or QA evidence; latest scoped user directions govern')
for folder in ['v1','v2','v3','v4','v5','v6']:
    source = SPRINT/folder
    if source.exists():
        for src in source.rglob('*'):
            if src.is_file() and src.suffix.lower() in ['.txt','.json','.html']:
                copy_file(src, DEST/'sprint-history'/folder/src.relative_to(source), 'Historical rejected/proposed packet evidence; not current approval')
source = SPRINT/'v8-visual-reference-repair'
for src in source.rglob('*'):
    if src.is_file(): copy_file(src, DEST/'sprint-current-source'/src.relative_to(source), 'V8 source records/references only; image instructions require repair')

archive = json.loads((DEST/'USER-INSTRUCTION-ARCHIVE.json').read_text(encoding='utf-8'))
rows = []
for r in archive['records']:
    rows.append('<article id="'+html.escape(r['message_id'])+'"><h3>'+html.escape(r['message_id'])+'</h3><pre>'+html.escape(r['text'])+'</pre><p>'+html.escape(', '.join(r['images']))+'</p></article>')
(DEST/'USER-INSTRUCTION-ARCHIVE.html').write_text('<!doctype html><html><meta charset="utf-8"><title>Verbatim user instruction archive</title><style>body{max-width:1000px;margin:30px auto;padding:20px;font:16px system-ui}pre{white-space:pre-wrap;overflow-wrap:anywhere}article{border-bottom:1px solid #bbb;margin-bottom:30px}</style><h1>Verbatim user instruction archive</h1><p>Pasted assistant claims are evidence to investigate, not human approval. All returned non-heartbeat user messages are preserved.</p>'+''.join(rows)+'</html>',encoding='utf-8')

ledger = json.loads((DEST/'REQUIREMENTS-LEDGER.json').read_text(encoding='utf-8'))
assert len(ledger['rules']) == 66
assert all(r['evidence'] for r in ledger['rules'])
matrix = [{'id':r['id'],'scope':r['scope'],'requirement':r['requirement'],'evidence_ids':[x['message_id'] for x in r['evidence']],'repair_status':'TO_BE_MAPPED_TO_EACH_APPLICABLE_LOOK_AND_ROLE','visual_status':'NOT_TESTED_IN_RECOVERY'} for r in ledger['rules']]
(DEST/'REPAIR-COVERAGE-MATRIX.json').write_text(json.dumps(matrix,indent=2,ensure_ascii=False),encoding='utf-8')

packet = json.loads((DEST/'sprint-current-source/packet-1.json').read_text(encoding='utf-8'))
source_html = (DEST/'sprint-current-source/FULL-PACKET-1.html').read_text(encoding='utf-8')
idea_urls = re.findall(r'https://www\.amazon\.com/shop/[^"\s<>]+/list/[^"\s<>]+', source_html)
product_rows = []
for look in packet['looks']:
    products = []
    for p in look.get('products',[]):
        ref = 'sprint-current-source/'+p['reference']
        assert (DEST/ref).is_file(), ref
        products.append('<li>'+html.escape(p['name'])+' — '+html.escape(str(p.get('variant','')))+' · <a href="'+html.escape(p['url'],quote=True)+'">Product page</a> · '+ ('<a href="'+html.escape(p['affiliate_link'],quote=True)+'">Existing affiliate link</a> · ' if p.get('affiliate_link') else 'Affiliate capture pending · ')+'<a href="'+html.escape(ref,quote=True)+'">Open product photo</a></li>')
    idea_url = next((u for u in idea_urls if look.get('idea') and u.endswith('/'+look['idea'])), None)
    idea_link = '<a href="'+html.escape(idea_url,quote=True)+'">Historical Idea List</a>' if idea_url else 'Idea List destination not present; preserve recorded ID without inventing a URL'
    product_rows.append('<section><h3>'+html.escape(str(look['number'])+' · '+look['name'])+'</h3><p>Source inventory, NOT approved prompt direction. '+idea_link+'</p><ul>'+''.join(products)+'</ul></section>')

thumbs = ''.join('<figure><a href="approved-cardigan/'+f+'"><img src="approved-cardigan/'+f+'" alt="Approved cardigan '+label+'"></a><figcaption>'+label+' — historical accepted mock, scoped defects retained</figcaption></figure>' for f,label in [('basic.webp','BASIC'),('styled.webp','STYLED'),('lifestyle.png','LIFESTYLE')])
reference_links = ''.join('<li><a href="'+x['file']+'">'+html.escape(x['role'])+' · '+html.escape(x['original_filename'])+'</a></li>' for x in manifest if x['file'].startswith(('original-clothing-references/','original-nonfashion-references/')))
prompt = (DEST/'REPAIR-PROMPT.txt').read_text(encoding='utf-8')
page = '<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>WYS source-backed sprint repair handoff</title><style>body{max-width:1100px;margin:auto;padding:24px;font:16px/1.55 system-ui;color:#202020}h1,h2{line-height:1.2}a{color:#a31655}pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#f5f5f5;padding:20px}.trio{display:flex;gap:16px}.trio figure{margin:0;flex:1;min-width:0}.trio img{width:100%;height:auto}section{border-top:1px solid #ddd;padding:12px 0}button{font:inherit;padding:12px} @media(max-width:600px){.trio{display:block}.trio figure{margin-bottom:20px}}</style></head><body><h1>WYS · Legally Blonde sprint repair handoff</h1><p><strong>This is the recovered specification and source pack. V8 is not cleared to run. No new images were generated.</strong></p><p>Attach this whole ZIP to the receiving coding chat and paste the repair prompt below. All local links work after extraction.</p><p><a href="GOVERNING-SPEC.md">Governing specification</a> · <a href="USER-INSTRUCTION-ARCHIVE.html">Verbatim instructions</a> · <a href="REQUIREMENTS-LEDGER.json">66 source-backed requirements</a> · <a href="HANDOFF.md">Handoff / coverage limits</a></p><h2>Approved cardigan visual benchmark</h2><div class="trio">'+thumbs+'</div><p>The photos are preserved unchanged. This approves one mock look; it is not retail-fidelity or client-release certification. Bedding is not a universal series template.</p><h2>Original references: clothing plus separately scoped workspace/atmosphere</h2><ul>'+reference_links+'</ul><h2>Copy this repair prompt</h2><p><a href="REPAIR-PROMPT.txt">Open plain text prompt</a></p><button onclick="navigator.clipboard.writeText(document.getElementById(\'prompt\').textContent).then(()=>this.textContent=\'Copied\').catch(()=>this.textContent=\'Select and copy the text below\')">Copy repair prompt</button><pre id="prompt">'+html.escape(prompt)+'</pre><h2>Existing sprint products and photo links</h2><p>Dated records from October 7. Availability/reviews/affiliate destinations were not refreshed in this source recovery. Idea List IDs are retained; the canonical source record controls any existing full URL.</p>'+''.join(product_rows)+'<h2>Historical evidence</h2><p><a href="sprint-current-source/packet-1.json">V8 structured source inventory (NOT approved prompts)</a> · <a href="FILE-MANIFEST.json">Original filenames, hashes and dimensions</a> · <a href="historical-prompts/cardigan-final-styled.txt">Historical final styled prompt</a> · <a href="historical-prompts/cardigan-final-lifestyle.txt">Historical final lifestyle prompt</a> · <a href="historical-prompts/mock-five-basic-v02.txt">Saved BASIC variant</a></p></body></html>'
(DEST/'START-HERE.html').write_text(page,encoding='utf-8')
(DEST/'FILE-MANIFEST.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False),encoding='utf-8')

# Add exactly one discovery pointer to existing repository instructions.
agents = REPO/'AGENTS.md'
txt = agents.read_text(encoding='utf-8')
heading = '## WYS recovered instruction memory — read before WYS work'
parts = txt.split(heading)
if len(parts)>2:
    first_block, tail = parts[-1].split('When starting the dev server',1)
    txt = parts[0]+heading+first_block+'When starting the dev server'+tail
    agents.write_text(txt,encoding='utf-8')

links = re.findall(r'(?:href|src)="([^"]+)"',page)
missing = [x for x in links if not x.startswith(('https:','http:','#')) and not (DEST/html.unescape(x)).is_file()]
assert not missing, missing
checks = {'history_turns_read':archive['turns_read'],'non_heartbeat_user_messages':len(archive['records']), 'source_backed_rules':len(ledger['rules']), 'original_clothing_screenshots':len(refs),'original_nonfashion_screenshots':len(nonfashion_refs),'approved_images':3,'active_packet_looks':len(packet['looks']),'included_source_files':len(manifest),'local_html_link_targets_verified':len([x for x in links if not x.startswith(('https:','http:','#'))]),'missing_local_targets':missing,'copied_files_hash_verified':True,'status':'STATIC_SOURCE_HANDOFF_CHECKS_ONLY','images_generated':0,'image_prompt_repair':'NEXT_TASK_NOT_COMPLETED_BY_RECOVERY','new_visual_passes':0,'global_account_memory_write':'UNAVAILABLE','root_project_AGENTS_write':'READ_ONLY_WRITE_FAILED_UNCHANGED; repo AGENTS updated','prior_chat_history':'5 available turns; no older cursor; one assistant text truncated; not whole earlier history'}
(DEST/'VERIFICATION.json').write_text(json.dumps(checks,indent=2),encoding='utf-8')
output = ROOT/'WYS-Sprint-Repair-Handoff'
output.mkdir(exist_ok=True)
archive_path = output/'ATTACH-THIS-WYS-REPAIR-PACK.zip'
with zipfile.ZipFile(archive_path,'w',zipfile.ZIP_DEFLATED) as z:
    for f in DEST.rglob('*'):
        if f.is_file(): z.write(f,f.relative_to(DEST).as_posix())
with zipfile.ZipFile(archive_path) as z:
    assert z.testzip() is None
    assert 'START-HERE.html' in z.namelist()
shutil.copyfile(DEST/'REPAIR-PROMPT.txt',output/'PASTE-THIS-REPAIR-PROMPT.txt')
print(json.dumps({'checks':checks,'zip':str(archive_path),'zip_bytes':archive_path.stat().st_size,'prompt':str(output/'PASTE-THIS-REPAIR-PROMPT.txt')},indent=2))
