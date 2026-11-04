#!/usr/bin/env python3
"""Validate the core TDIE pin handoff, not Amazon/buyer pipelines."""
import argparse,csv,datetime as dt,hashlib,struct
from pathlib import Path
FIELDS='file,title,description,alt,link,board,date,time,source,topic_family,layout,persona_required,status,overlay,timezone,approval,asset_sha256,ai_label'.split(',')
def validate(path):
    errors=[];seen=set();slots=set();lastboard=None;families={}
    with Path(path).open(encoding='utf-8-sig',newline='') as f:
        reader=csv.DictReader(f)
        if any(x not in (reader.fieldnames or []) for x in FIELDS):return ['Missing required columns']
        records=list(reader)
    if not records:return ['No pin rows: blank template is not an approved packet']
    dated=[]
    for n,r in enumerate(records,2):
        label=f'row {n}';state=r['status']
        if any(r.get(x) is None for x in FIELDS):errors.append(label+': incomplete row');continue
        if state not in {'READY','IMAGE_REQUIRED','HOLD','SCHEDULED','VERIFIED','FAILED'}:errors.append(label+': invalid status')
        if r['approval'] not in {'PENDING','APPROVED','REJECTED'}:errors.append(label+': invalid approval')
        if state in {'READY','SCHEDULED','VERIFIED'} and r['approval']!='APPROVED':errors.append(label+': executable row without approval')
        if r['timezone']!='America/New_York':errors.append(label+': wrong timezone')
        if r['link']!='https://www.skool.com/thedigitalincomeedit/about':errors.append(label+': wrong core destination')
        for field,low,high in [('title',60,100),('description',450,500),('alt',150,200)]:
            if not low<=len(r[field])<=high:errors.append(label+f': {field} length out of range')
        if not 3<=len(r['overlay'].split())<=5:errors.append(label+': overlay must be 3 to 5 words')
        if r['ai_label']!='ON':errors.append(label+': AI label must be ON')
        if r['persona_required'] not in {'YES','NO'}:errors.append(label+': persona_required must be YES/NO')
        if any(not r[x].strip() for x in ['board','source','topic_family','layout']):errors.append(label+': missing production metadata')
        copy=' '.join(r[x] for x in ['title','description','alt','overlay'])
        if '$' in copy or 'make money online' in copy.lower():errors.append(label+': prohibited price/spam-risk copy')
        try:stamp=dt.datetime.strptime(r['date']+' '+r['time'],'%Y-%m-%d %H:%M');dated.append((stamp,r))
        except ValueError:errors.append(label+': invalid local date/time')
        slot=(r['date'],r['time'])
        if slot in slots:errors.append(label+': duplicate slot')
        slots.add(slot)
        if r['file'] in seen:errors.append(label+': duplicate file')
        seen.add(r['file'])
        asset=(Path(path).resolve().parent/r['file']).resolve()
        if not asset.is_relative_to(Path(path).resolve().parent):errors.append(label+': asset path escapes packet');continue
        if state in {'READY','SCHEDULED','VERIFIED'}:
            if not asset.is_file():errors.append(label+': missing finished asset');continue
            b=asset.read_bytes()
            if hashlib.sha256(b).hexdigest()!=r['asset_sha256']:errors.append(label+': asset hash mismatch')
            if len(b)<24 or b[:8]!=b'\x89PNG\r\n\x1a\n' or struct.unpack('>II',b[16:24])!=(1000,1500):errors.append(label+': finished PNG must be 1000x1500')
    for stamp,r in sorted(dated,key=lambda x:x[0]):
        if r['board']==lastboard:errors.append('Consecutive board repeat')
        lastboard=r['board'];family=r['topic_family']
        if family in families and (stamp-families[family]).total_seconds()<3*86400:errors.append('Topic family repeats within 3 days')
        families[family]=stamp
    return errors
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('manifest');a=ap.parse_args()
    try:errors=validate(a.manifest)
    except (OSError,ValueError) as e:ap.exit(2,str(e)+'\n')
    for e in errors:print('ERROR:',e)
    print(f'{len(errors)} errors. Visual quality, claims and live scheduling need separate evidence.')
    raise SystemExit(bool(errors))
