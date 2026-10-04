#!/usr/bin/env python3
"""Offline handoff gate. Never creates or verifies a platform object."""
import argparse, datetime as dt, hashlib, json, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
FIELDS={'task_id','workflow_id','account','packet','approval','content_hash','status','dependencies','requested_local_time','timezone','observed_state','platform_id','evidence','exception'}
STATES={'DRAFT','QA_PASSED','APPROVED','READY','RUNNING','APPLIED','VERIFIED','COMPLETE','BLOCKED','FAILED','UNKNOWN','CANCELLED','SUPERSEDED'}
def validate(data,root=ROOT):
    errors=[]
    if not isinstance(data,dict) or data.get('schema_version')!=1 or not isinstance(data.get('operations'),list):return ['schema_version=1 and operations array required']
    workflows={r['id'] for r in json.loads((root/'ops/ai-router/WORKFLOW_REGISTRY.json').read_text(encoding='utf-8'))['workflows']}
    seen=set();allids=set();children={}
    for n,r in enumerate(data['operations'],1):
        label=f'operation {n}'
        if not isinstance(r,dict):errors.append(label+': object required');continue
        if FIELDS-r.keys():errors.append(label+': missing fields '+', '.join(sorted(FIELDS-r.keys())));continue
        if not all(isinstance(r[k],str) for k in FIELDS-{'dependencies','evidence'}):errors.append(label+': scalar fields must be strings');continue
        if not isinstance(r['dependencies'],list) or not all(isinstance(x,str) for x in r['dependencies']):errors.append(label+': dependencies must be ID array');continue
        if not isinstance(r['evidence'],list) or not all(isinstance(x,str) and x.strip() for x in r['evidence']):errors.append(label+': evidence must be nonempty references array');continue
        tid=r['task_id'];state=r['status']
        if not tid.strip() or tid in allids:errors.append(label+': blank or duplicate task_id')
        allids.add(tid);children[tid]=r['dependencies']
        if r['workflow_id'] not in workflows:errors.append(label+': invalid workflow_id')
        if state not in STATES:errors.append(label+': invalid status')
        if r['timezone']!='America/New_York':errors.append(label+': wrong timezone')
        try:dt.datetime.fromisoformat(r['requested_local_time'])
        except ValueError:errors.append(label+': local ISO datetime required')
        if not r['account'].strip():errors.append(label+': missing account')
        if r['approval'] not in {'PENDING','APPROVED','REJECTED'}:errors.append(label+': invalid approval')
        if state in {'APPROVED','READY','RUNNING','APPLIED','VERIFIED','COMPLETE'} and r['approval']!='APPROVED':errors.append(label+': action status without approval')
        if not re.fullmatch(r'[0-9a-f]{64}',r['content_hash']):errors.append(label+': SHA-256 content_hash required')
        path=(root/r['packet']).resolve()
        if not r['packet'] or not path.is_relative_to(root.resolve()) or not path.is_file():errors.append(label+': packet missing or outside repo')
        elif hashlib.sha256(path.read_bytes()).hexdigest()!=r['content_hash']:errors.append(label+': packet hash mismatch')
        key=(r['workflow_id'],r['account'],r['requested_local_time'],r['content_hash'])
        if key in seen:errors.append(label+': duplicate operation fingerprint')
        seen.add(key)
        if state in {'VERIFIED','COMPLETE'} and (not r['evidence'] or not r['platform_id'].strip() or not r['observed_state'].strip()):errors.append(label+': completion lacks independent evidence/ID/observed state')
        if state in {'BLOCKED','FAILED','UNKNOWN','CANCELLED','SUPERSEDED'} and not r['exception'].strip():errors.append(label+': exception reason required')
        if tid in r['dependencies']:errors.append(label+': self dependency')
    for tid,deps in children.items():
        if any(dep not in allids for dep in deps):errors.append(tid+': missing dependency ID')
    active=set();visited=set()
    def cycle(tid):
        if tid in active:return True
        if tid in visited:return False
        active.add(tid)
        for dep in children.get(tid,[]):
            if cycle(dep):return True
        active.remove(tid);visited.add(tid);return False
    if any(cycle(tid) for tid in children):errors.append('dependency cycle')
    return errors
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('manifest');args=ap.parse_args()
    try:errors=validate(json.loads(Path(args.manifest).read_text(encoding='utf-8')))
    except (OSError,ValueError) as e:ap.exit(2,str(e)+'\n')
    for e in errors:print('ERROR:',e)
    print(f'{len(errors)} errors; offline contract only. Live evidence is not authenticated here.')
    raise SystemExit(bool(errors))
