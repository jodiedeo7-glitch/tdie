from pathlib import Path
import json,hashlib,shutil,zipfile
root=Path(__file__).resolve().parent.parent;out=root/'outputs/Packet-1-V10';repo=root/'work/tdie'
rel=Path('ops/private/wys-board-test-2026-10-06/halloween-sprint-restart-20261007/v10-complete-looks-creative-repair')
p=json.loads((out/'packet-1.json').read_text());old=json.loads((root/'outputs/Packet-1-V9/packet-1.json').read_text())
assert [l['number'] for l in p['looks']]==[1,2,3,5,6,7,8,9,10]
for l in p['looks']:
 assert 5<=len(l['products'])<=8
 assert len(set(x['asin'] for x in l['products']))==len(l['products'])
 assert l['shopping_record_count']==len(l['products'])
 assert 'one pair of one pair' not in json.dumps(l)
 assert 'No connected body outline' in l['prompts']['STYLED']
 assert l['scene_camera_plan']['basic'] != l['scene_camera_plan']['styled']
 if l['number']==5:
  assert 'B0DQ6YTL7R' not in [x['asin'] for x in l['products']]
  assert 'satin bow clips' not in l['blog_copy']['body']
 for role,t in l['prompts'].items():
  assert len(t)<3000 and len(t.encode('utf-16-le'))//2<3000
  assert t==(out/f'prompts/{l["number"]:02}-{role.lower()}.txt').read_text()
  assert t != next(x for x in old['looks'] if x['number']==l['number'])['prompts'][role]
  for a in l['attachments'][role]:assert (out/a['file']).is_file()
 for x in l['products']:assert hashlib.sha256((out/x['reference']).read_bytes()).hexdigest()==x['reference_sha256']
qa=json.loads((out/'document-qa/RENDER-CHECKS.json').read_text());assert qa['downloadByteMatch'] and qa['copyButtonsTested']==27
v=json.loads((out/'VALIDATION.json').read_text());v.update(rendered_document_QA=qa,shopping_range_check='ALL_9_LOOKS_HAVE_5_TO_8_DISTINCT_PURCHASES',creative_revision_check='27_OF_27_PROMPTS_CHANGED_FROM_REJECTED_V9',ghost_correction='Separate garment positions, local fabric depth and no connected body outline in all STYLED prompts; generated results not tested.')
(out/'VALIDATION.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
(out/'.gitattributes').write_text('* -text\n',encoding='utf-8',newline='\n')
corrections='''LATEST DIRECT CORRECTIONS — 8 October 2026

User rejected V9: Look 2 has only three shopping products; result is too plain; STYLED looks like a ghost laid out. User also requested no further explanations. Screenshot preserved unchanged in rejection-evidence, never used as a positive generation reference.

Implementation: every active look now has five or six distinct shopping purchases. Short looks gain individually sourced jewellery or a previously sourced headband. Jewellery pairs and garment sets remain one purchase each. Graduation bows replaced by selected bracelet under the existing no-bows direction; removed product/link preserved historically. Richer close compositions, broad lavender/cream contrasts, unequal group sizes, personal accessory clusters, independent garment positions and local fabric depth replace sparse grids and assembled invisible bodies. Lifestyle actions and props are look-specific.

This correction supplements the recovered governing record and takes precedence over conflicting V9 choices. It does not redefine clothing STYLED as a flat unfilled BASIC. No generated V10 images, visual approval or release claim.
'''
(out/'LATEST-DIRECT-CORRECTIONS.txt').write_text(corrections,encoding='utf-8',newline='\n')
audit={'document_checks':qa,'original_source_hashes_verified':292,'selected_product_hashes_verified':True,'all_prompt_attachment_files_present':True,'all_27_saved_prompts_under_3000':True,'all_27_prompts_differ_from_v9':True,'all_nine_looks_5_to_8_purchases':True,'new_sources':'Official Amazon cached listings retrieved 8 Oct; selected variants, photos and displayed aggregate ratings captured. Current stock/price and individual review text not established. Brand material/size crosscheck retained in SOURCING-ADDITIONS.json.','generated_v10_images_reviewed':0,'rejected_user_screenshot_preserved':True,'recovered_history_read_scope':'Governing record, 66-rule ledger, recovered archive/approval evidence and supplied historical prompts; original clothing references and cardigan trio inspected. No unavailable history claim.'}
(out/'SOURCE-READ-AND-DOCUMENT-AUDIT.json').write_text(json.dumps(audit,indent=2)+'\n',encoding='utf-8',newline='\n')
agents=repo/'AGENTS.md';s=agents.read_text(encoding='utf-8');marker='Packet 1 V10 corrective repair'
if marker not in s:agents.write_text(s+'\n'+marker+': read `'+rel.as_posix()+'/LATEST-DIRECT-CORRECTIONS.txt` alongside the governing record. V9 was rejected for three-item lists, sparse styling and ghost-body composition. Latest packet completes 5–8 shopping selections, removes conflicting bows and uses separate dimensional garments. No new visual approval.\n',encoding='utf-8',newline='\n')
shutil.copytree('\\\\?\\'+str(out),'\\\\?\\'+str(repo/rel),dirs_exist_ok=True)
scripts=repo/rel/'validation-scripts';scripts.mkdir(exist_ok=True)
for name in ['build_v10.py','v10_creative.py','verify_v10.cjs','finish_v10.py','source_additions.py']:
 Path('\\\\?\\'+str(scripts/name)).write_text((root/'work'/name).read_text(encoding='utf-8-sig').rstrip()+'\n',encoding='utf-8',newline='\n')
zpath=root/'outputs/WYS-PACKET-1-V10.zip';files=sorted(f for f in out.rglob('*') if f.is_file())
with zipfile.ZipFile(zpath,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for f in files:z.write(f,f.relative_to(out).as_posix())
with zipfile.ZipFile(zpath) as z:
 assert z.testzip() is None
 for f in files:assert z.read(f.relative_to(out).as_posix())==f.read_bytes()
print(json.dumps({'shopping_counts':{l['number']:l['shopping_record_count'] for l in p['looks']},'prompts':27,'max_characters':v['prompt_max_characters'],'zip_bytes':zpath.stat().st_size,'validation':'DOCUMENT_CHECKS_PASS_ONLY'},indent=2))
