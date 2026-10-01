from pathlib import Path
import json, re, zipfile, hashlib
from xml.sax.saxutils import escape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether, Flowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.pagesizes import letter
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'pdf'
OUT.mkdir(exist_ok=True)
PINK = HexColor('#B52964')
INK = HexColor('#282126')
styles = {
 'k': ParagraphStyle('k', fontName='Helvetica-Bold',fontSize=9,leading=13,textColor=PINK,spaceAfter=10),
 't': ParagraphStyle('t',fontName='Times-Roman',fontSize=29,leading=32,textColor=INK,spaceAfter=18),
 'h': ParagraphStyle('h',fontName='Helvetica-Bold',fontSize=11,leading=15,textColor=PINK,spaceAfter=5,keepWithNext=True),
 'b': ParagraphStyle('b',fontName='Helvetica',fontSize=10.5,leading=15,textColor=INK,spaceAfter=12),
 'prompt': ParagraphStyle('prompt',fontName='Helvetica',fontSize=10,leading=14,textColor=INK,spaceAfter=8),
}

def clean(s):
 return s.replace('\u2014', ' - ').replace('\u2013','-').replace('\u2011','-').replace('\u2605','').replace('\u2122','').strip()

def para(s,style='b'):
 s=escape(clean(s)).replace('\n','<br/>')
 # Official reference URLs are clickable and wrap at word boundaries.
 s=re.sub(r'(https://[^<\s]+)', lambda m:'<link href="'+m.group(1)+'" color="#B52964">'+m.group(1)+'</link>',s)
 return Paragraph(s,styles[style])

def decor(c,d):
 c.setFillColor(HexColor('#FCF9F7'));c.rect(0,0,612,792,fill=1,stroke=0)
 c.setFillColor(PINK);c.rect(0,782,612,10,fill=1,stroke=0)
 c.setFillColor(INK);c.setFont('Helvetica-Bold',9);c.drawString(48,751,'THE DIGITAL INCOME EDIT')
 c.setStrokeColor(HexColor('#CEBBA5'));c.line(48,48,564,48)
 c.setFont('Helvetica',8);c.drawString(48,33,'WHILE-YOU-SLEEP STOREFRONT | BUYER EDITION | SEPTEMBER 2026')
 c.drawRightString(564,33,str(d.page))

def page(story,k,title,sections):
 if story:story.append(PageBreak())
 story.extend([para(k.upper(),'k'),para(title,'t')])
 for label,body in sections:
  story.extend([para(label,'h'),para(body)])

pages=json.loads((ROOT/'guide-content.json').read_text(encoding='utf-8'))
replace={
 'Read 01_REQUIREMENTS.txt.':'Use the account checklist in the workbook.',
 'This guide replaces the older hands-off setup PDF. Historical examples are not current tests.':'This guide and the workbook contain everything in the buyer package.',
 'Paste the setup prompt in 02_SETUP_PROMPT.txt':'Copy the setup prompt from the workbook',
 '06_SCHEDULED_TASK_PROMPTS.txt supplies':'The workbook supplies',
 'Every automated step has the low-cost and manual paths in 12_OPERATION_MODES.txt.':'Each core step includes a low-cost chat route and a fully manual route.',
 'See SOURCES.md;':'Use the official links on this page;',
}
story=[]
page(story,'Begin here','Your Storefront buyer guide',[
 ('What you will make','A complete Pinterest Pin from your selected products: an original or rights-cleared image, accurate copy, a working destination and a posting time you approve. Optional connected tools can prepare the work. You remain in control of each publication.'),
 ('Two documents, one clear path','Read this guide first. Use the companion workbook to copy the setup and recipe prompts, fill your account settings, record products, review Pins and track results. The workbook is an editable PDF: open it in a PDF reader that supports forms, save a copy, then type in the response fields. Print it if you prefer handwriting.'),
 ('Start without extra subscriptions','For the simplest route, select one look yourself, use your own or licensed photo or original layout, write the copy and schedule in Pinterest. Your existing Claude or ChatGPT plan can help with small requests within its limits. AI, paid schedulers and developer applications are optional.'),
 ('Your first session','1. Choose your operating mode. 2. Check your account and public destination. 3. Complete one product intake. 4. Make one finished Pin. 5. Review and schedule it. 6. Reopen the saved record and log the result.'),
 ('Where to find things','Guide pages 3-9: the seven setup steps. Pages 10-11: optional paths and references. The remaining pages explain a complete themed look, image choices, recovery and optional additions. Workbook: setup prompt, recipe prompt, task prompts and editable worksheets.')])
for k,title,sections in pages:
 updated=[]
 for label,body in sections:
  for a,b in replace.items():body=body.replace(a,b)
  if title=='Create persistent working state' and label=='One production workspace':
   body='Manual mode: the workbook can hold your settings, intake, queue and log. Save a private copy and a backup. Connected automation may need separate working files; the setup prompt creates them from your answers. Those files are working state, not extra buyer instructions. Keep this project separate from other TDIE automation.'
  if title=='Prepare a ready product intake' and label=='One look, one destination':
   body='Start with one coherent selection. Complete the product worksheet in the workbook for each item: ASIN, your description, color/material, your Special Link, destination URL and image rights. Connected automation uses the same information in its product intake file.'
  updated.append((label,body))
 page(story,k,title,updated)

extra=[
 ('Make your first look','Build one look from beginning to end',[
 ('Choose a useful theme','Pick one specific situation, such as pink workwear for a cold office. Select the products yourself and create or confirm the eligible public Idea List or your own published look page. Put one item on each product worksheet. Never mark an example or missing link ready.'),
 ('Make one image first','Use a flat lay, person-free collage, your own photograph or a licensed asset. Two variations are optional: one flat lay and one different layout or a rights-cleared persona scene. Start with one valid Pin when you want to save credits.'),
 ('Inspect before writing','Confirm item count, colors, silhouettes, fabric, hands where applicable, portrait framing and readable overlay text. Remove unintended logos or decorative third-party characters. An AI styling image is inspiration; similar products in a list are not the exact items photographed.'),
 ('Finish all fields','Write the title, caption and alt text using the rules in Step 5. Confirm the image, destination, board, section and date. Put the complete record on the Pin review worksheet. An unfinished record stays HOLD.'),
 ('Approve and read back','Choose each exact Pin yourself before publishing. Schedule in Pinterest or a tested supported publisher. Reopen the external record and compare all fields. Copy its external ID to the log. Check native Pinterest and Metricool separately before making another Pin.')]),
 ('Your routes','Save time or save credits at every stage',[
 ('Planning and product choices','Time-saving: a tested runtime organizes your approved intake. Low-cost chat: give one short request using your own notes. Manual: choose a look, find the products and create your own links and destination in Amazon.'),
 ('Images and corrections','Time-saving: a verified image connector uses the chosen model within your budget. Low-cost chat: request one image only if your account supports it and its commercial terms fit. Manual: use an original layout, your own photo or a licensed asset. Correct only the failed image; keep valid work.'),
 ('Copy and destination','Time-saving: supported tools prepare fields or an authorized website page. Low-cost chat: ask for one title/caption/alt-text set or one page from verified facts. Manual: write the fields and create your Idea List or paste a page into your site editor.'),
 ('Queue and scheduling','Time-saving: tested tools save the complete record and publish only after the required individual approval. Low-cost chat: prepare and check fields, then schedule yourself. Manual: review every field in Pinterest and set your chosen posting time.'),
 ('Readback and changes','Time-saving: supported tools inspect existing records and update the log. Low-cost chat: paste statuses for one comparison. Manual: open each owning service and match the exact external ID. A timeout is a reason to check first, not create a duplicate.')]),
 ('Image choices','Choose a provider you can actually use',[
 ('Use your own account evidence','Record provider, model, interface, allowance, commercial rights and maximum spend in the workbook. A website allowance can differ from a connector or API allowance. Another person\'s subscription does not transfer to your account.'),
 ('With a persona','Use a reference only with consent and rights covering transformation and commercial use. Check likeness, hands, fabric and framing. Keep the persona optional; a person-free layout is a complete path.'),
 ('Without image generation','Use your own photograph, a licensed image or a layout you create in your usual editor. The workflow does not require a paid image provider. Choose the applicable AI-content and AI-person labels based on the actual finished image.'),
 ('Limits before spending','Set your maximum cost before generation. Use no more than the first attempt and two correction rounds per Pin, within that budget. If the asset still fails, hold it. Do not switch plans or models silently.'),
 ('A short image brief','Use the recipe prompt in the workbook. Describe verified colors, fabrics, shapes and arrangement in your own words. Supply no copied marketplace image unless you have the necessary rights. Review the exported asset before it enters the queue.')]),
 ('Keep work recoverable','Track results without duplicating Pins',[
 ('One record for each Pin','Use a stable ID made from the look, Pin number and chosen date/time with timezone. Save that ID, the owning service and its external ID. If the date changes by your instruction, retain the old ID and mark it withdrawn; create a new record only after checking the old external record.'),
 ('When a run stops','Save completed assets and fields. Mark the unfinished step and the exact reason. Read the external scheduler before retrying. Resume only after the missing capability is restored and the required approval is still valid.'),
 ('If authorization expires','Stop connected publication, mark waiting for Pinterest authorization and reconnect through the normal service flow. Use the manual route if you choose. Never invent a hidden browser or private-request workaround.'),
 ('If a product or link fails','Mark blocked product or blocked destination. Choose a replacement yourself and verify it. Do not let chat invent a link, ASIN or substitute posting date.'),
 ('HOLD and PULL','HOLD means do not publish. PULL records your requested change or removal of the exact existing item; it does not itself prove the external change happened. Read the record back and log the observed result. Missing approval always stays HOLD.')]),
 ('Optional publishing','Use connected scheduling only after a test',[
 ('Choose the simple path first','Native Pinterest scheduling needs no developer application. Metricool is optional and requires its own account test. A developer app is a separate route; check current approval, authorization scopes and supported operations in the official portal.'),
 ('A useful draft-only test','Use one prepared image and complete fields. Confirm the chosen account, public board, destination, alt text, approval and intended date. Save as a draft with automatic publishing disabled, then read it back. Do not call publication or scheduling passed based on a draft-only test.'),
 ('For a developer application','Prepare a demo of the real workflow: connect, select the exact board, prepare a finished Pin, have the customer choose each Pin, submit only a supported request and read the result back. Keep credentials out of prompts, logs and public files. Test access is not proof of production capability.'),
 ('Low-cost and manual routes','Ask your existing chat to organize application notes if you need them. Otherwise skip the application and schedule each Pin yourself. While a required capability remains unknown, use build/queue only.'),
 ('For scheduled work','Copy the relevant task prompt from the workbook. Supply a confirmed timezone, schedule, accessible state and supported tools. A template is not an installed task. Test the actual environment before enabling recurring work.')]),
 ('Optional additions','Add a website or another channel',[
 ('Your look page','Publish an original title, introduction, rights-cleared styling image, your own Special Links, affiliate disclosure and an accurate AI-image disclosure. Check the live page before linking a Pin. Do not include prices in this kit\'s Pin or image copy.'),
 ('Low-cost website path','Ask your existing chat for one page draft from the verified product intake. Read it, check every link, and paste it into your site editor.'),
 ('Manual website path','Write the same page yourself and publish through your usual editor. A supported site connector is an optional time-saving route; it still needs live readback.'),
 ('Instagram','Treat Instagram as a separate optional workflow. Check current account features, disclosures and publishing rules. Low-cost chat can draft one caption; manually create the post in the app or your normal publishing interface. Do not put earnings claims on Facebook or Instagram.'),
 ('Keep the core simple','Your first complete Pinterest workflow does not need a website if your eligible public Idea List works. It does not need Instagram, a persona, developer approval or a paid scheduler.')]),
 ('Optional styling source','Keep paid community material separate',[
 ('Brand Closet OOTD','This optional route stays disabled until you have written permission covering the intended commercial derivative and automated use of paid material. Membership or referral access is not evidence of that permission.'),
 ('Permission to record','Confirm permitted access, extraction of product attributes, prompt transformation, derivative styling images, commercial publication, affiliate use, automated processing, customer use and the permission\'s duration and revocation conditions. Keep the actual permission privately.'),
 ('Low-cost alternative','Give chat your own original styling brief and verified product facts. Use a small request on your existing plan. Skip paid content when rights are uncertain.'),
 ('Manual alternative','Create an original look from your own notes, select your own products and links, make a rights-cleared asset and schedule in Pinterest. Do not copy paid lesson text, reuse paid images or assume a community instruction grants a commercial license.'),
 ('Optional referral card','Only use a program you personally have access to under its current terms. Verify membership information and referral conditions before publishing. A manual website card is sufficient. Referral permission does not activate the OOTD automation.')]),
 ('Finish your first test','Know what passed and what is still unknown',[
 ('Ready for one approved Pin','Your intake is complete; rights and budget are recorded; the public destination works; the exact public board is chosen; image and copy pass review; date/time is yours; the finished Pin has your individual approval.'),
 ('Pass only what you observed','Owner-visible lists are not the same as signed-out public access. A saved draft does not prove scheduling. A scheduled Pin does not prove it published at the right time. A document on your computer does not prove a cloud run can read it.'),
 ('Record the next action','Use the test log in the workbook: expected result, observed result, pass or unverified, evidence and next action. Keep historical tests separate from current ones.'),
 ('Start again from a saved record','Before the next look, check the current queue, external schedules and unresolved holds. Reuse valid work. Add automation only where a repeated task justifies it.'),
 ('You have the complete buyer package','Keep the guide for instructions and a private saved workbook for your settings, prompts, products and Pin records. Working state files are needed only if your chosen automation uses them; the setup prompt will prepare those from your answers.')])]
for args in extra:page(story,*args)
guide=OUT/'While-You-Sleep-Storefront-Buyer-Guide.pdf'
SimpleDocTemplate(str(guide),pagesize=letter,leftMargin=48,rightMargin=48,topMargin=82,bottomMargin=67,title='While You Sleep Storefront Buyer Guide',author='The Digital Income Edit').build(story,onFirstPage=decor,onLaterPages=decor)

class Field(Flowable):
 def __init__(self,name,height=30):
  Flowable.__init__(self); self.name=name;self.width=504;self.height=height+10
 def draw(self):
  self.canv.acroForm.textfield(name=self.name,tooltip=self.name.replace('_',' '),x=self.canv._currentMatrix[4],y=self.canv._currentMatrix[5]+5,width=504,height=self.height-10,fontName='Helvetica',fontSize=10,borderWidth=.5,borderColor=HexColor('#D4BDC7'),fillColor=white,textColor=black,forceBorder=True,fieldFlags='multiline' if self.height>45 else '',maxlen=12000)

work=[]
page(work,'Use this workbook','Storefront prompts and workbook',[
 ('Save your own copy','Open this PDF in a reader that supports forms. Save a private copy with your name or project theme. Fill the response boxes and save again. If your browser does not keep typed answers, use a PDF reader or print it. Keep passwords, tokens and private credentials out of every field.'),
 ('Copy prompts when useful','Select the text under each prompt and paste it into your existing Claude or ChatGPT chat. Prompt text runs across clearly numbered pages. Copy all setup prompt parts together for the complete interview. If you prefer fully manual work, skip the prompts and complete the worksheets.'),
 ('What is editable','The settings, product, image/budget, Pin review and test log pages have response fields. Duplicate the blank worksheets in your PDF reader for additional products and Pins, or print extra copies.'),
 ('Working files are optional','Manual mode can use this workbook alone. Connected automation may require a private settings file, product intake, queue and log. The setup prompt creates those from your answers, then reads them back; those working files do not replace this guide.'),
 ('Prompt order','1. Setup interview. 2. One themed look. 3. Optional task prompts after testing. Then use the worksheets for the actual records. Every finished Pin needs its own approval.')])
setup_parts=[
 ('Setup prompt 1 of 3','You are helping me set up While-You-Sleep Storefront. Use plain words. Ask one question at a time with a short example. Never ask for passwords, invent products or links, spend money, install recurring tasks or publish without the required specific authorization.\n\nFirst ask whether I want manual, mixed or time-saving mode. Manual uses this workbook and native Pinterest. Mixed uses chat or supported tools for preparation with manual publication. Time-saving uses a supported tested runtime and accessible private state.\n\nAsk my theme, clothing/home mix, voice, timezone and desired posting windows. Ask my Associates and Influencer status separately. Record actual Storefront, Idea List and onsite capabilities as separate verified or UNKNOWN fields. Use my eligible existing public Idea List, or require my compliant published website destination. Never promise application approval.\n\nAsk my exact public Pinterest board and section and verify the selected destination. Record my publishing method: native manual, supported connected publisher, or independently eligible developer API. Missing verified access means build/queue only. Each finished Pin requires my approval of its exact image, copy, link, board and date/time.'),
 ('Setup prompt 2 of 3','Ask my image route: own/licensed asset or original layout, optional image generation, and optional rights-cleared persona reference. Record provider, model, plan, website/connector/API interface, current allowance, commercial-use evidence and maximum spend. Never assume website Unlimited applies to a connector or someone else\'s subscription transfers to me.\n\nAsk where my private working records will live. For a scheduled runtime, record local/cloud environment and prove the actual runtime can read and write that state. A local folder is not automatically available in the cloud. Keep this Storefront project separate from other business automation.\n\nIf I already have state, ask whether to update an answer, renew planning, switch modes or start a new project. Preserve history. Record UNKNOWN where evidence is missing.\n\nManual mode: help me complete the workbook. No tasks or code files are required. Optional automation: prepare MY_RECIPE.txt settings, PRODUCT_SOURCES.md intake, pin-tab.md queue, pin-drafts.md draft details and storefront-log.md evidence. Use browser-lock.txt only for a workflow sharing a browser. Never store credentials in these records.'),
 ('Setup prompt 3 of 3','Settings must include mode, theme, mix, voice, timezone, boards/sections, Associates status, Influencer status, actual Storefront/Idea List capabilities, destination/site and publishing access, persona/rights, image provider/model/interface/plan/budget, runtime/state location, Pinterest method/access/approval, shutdown/HOLD, pace/look days, optional blog, Brand Closet permission gate and optional Instagram.\n\nEvery product row needs look, ASIN, my written product attributes, my own Special Link, destination and any reference-image rights. Examples and missing fields stay not ready. Queue records need stable ID, owning service/external ID when present, image, title, caption, alt text, destination, board/section, chosen date/time/timezone, status, APPROVE and PULL.\n\nUse the buyer guide\'s copy rules: title 60-100 characters; caption 450-500; no prices or product-brand/film/character names. Begin caption #ad and end As an Amazon Associate I earn from qualifying purchases. Describe AI styling and similar-product destinations accurately.\n\nRead back the saved settings and intake. Verify exact fields, public board, destination, rights, budget and current approval status. Stop missing items as HOLD with the next action. Keep Brand Closet disabled until written permission passes. Draft task prompts only after I choose real schedules. A template or old test is not proof of a run. Do not create new dates for withdrawn Pins or publish unapproved work.')]
for title,body in setup_parts:page(work,'Copy together',title,[('Copy this prompt text',body)])
page(work,'Copy and paste','One themed look prompt',[
 ('Before you paste','Complete one product worksheet for every item. Attach only rights-cleared references. Supply the exact public destination and public board. This request prepares a draft; it does not authorize publication.'),
 ('Copy this prompt text','Prepare one themed-look Pin from the verified product facts I supply below. Do not research Amazon autonomously, invent an ASIN, create affiliate links or change a destination. Mark missing facts HOLD.\n\nUse my selected image route, rights and budget. Offer both a short low-cost Claude/ChatGPT route and a fully manual own-photo/licensed-asset/original-layout route. Do not generate or spend until the exact image operation is authorized. Inspect the actual image before claiming it passed.\n\nGive me a 60-100 character accurate generic title, a 450-500 character caption and truthful alt text. Caption begins #ad and ends As an Amazon Associate I earn from qualifying purchases. No prices or product-brand/film/character names. If AI styling, call it inspiration; if the destination has similar items, do not call them the exact products photographed.\n\nReturn image reference, title, caption, alt text, exact destination, board/section and my chosen date/time with timezone as one draft record. Count characters. Check for existing records before making another. Save HOLD until I approve this individual finished Pin. Do not publish, choose a substitute date or install tasks.\n\nMy settings and product facts follow:'),
 ('Manual alternative','Follow the same field checklist yourself. An AI prompt is optional; your workbook record and native Pinterest composer are enough.')])
tasks=(ROOT/'kit'/'06_SCHEDULED_TASK_PROMPTS.txt').read_text(encoding='utf-8')
blocks=re.split(r'(?=TASK [123]:)',tasks)
page(work,'Optional tasks','Before you schedule any work',[
 ('Confirm the actual schedule','These are templates, not installed tasks. Record timezone, schedule, local/cloud runtime, accessible private state, tool capabilities and budget. Test a draft-only run and read it back before recurring production.'),
 ('Add this to each task','Use only the verified runtime and state location I supply. Read my current settings, product intake, queue and log first. Do not invent unknowns. Stop publication without approval of the exact finished Pin. Report the observed result and next action. No catch-up, spend increase or automatic replacement date is authorized.'),
 ('Low-cost route','Run one short request yourself when you need it. No recurring task or paid scheduler is required.'),
 ('Manual route','Choose the look, make the asset, write fields, schedule yourself and log the observed result. Skip the task templates entirely if this is your selected mode.')])
for b in blocks[1:]:
 lines=b.strip().splitlines(); title=lines[0].split(':',1)[1].strip().capitalize()
 page(work,'Optional task prompt',title,[('Copy this prompt text', '\n'.join(lines[1:]).strip().replace('03_THEMED_LOOK_RECIPE.txt','the themed-look section of the buyer guide'))])

def formpage(title,intro,fields):
 global work
 if work:work.append(PageBreak())
 work.extend([para('EDITABLE WORKSHEET','k'),para(title,'t'),para(intro)])
 for key,label,height in fields:
  work.extend([para(label,'h'),Field(key,height*.80),Spacer(1,2)])

formpage('Your account and settings','Record what you have actually verified. Use UNKNOWN for anything not checked.',[
 ('mode_theme','Operating mode, theme and voice',42),('amazon_status','Associates status, Influencer status and actual Storefront / Idea List capabilities',54),('destination','Exact public destination URL and public visibility evidence',54),('pinterest_board','Pinterest account, exact public board / section and IDs if known',54),('time_schedule','Timezone and your chosen posting windows',36),('publication','Publishing method, access status and individual approval process',54)])
formpage('Your runtime and budget','Manual mode may use this workbook alone. Fill the runtime fields only if you use connected or scheduled work.',[
 ('image_model','Image route, provider / model / interface and current allowance',54),('rights_budget','Commercial rights evidence and maximum spend before generation',54),('persona','Persona reference and consent / rights, or person-free route',42),('state_runtime','Private state location, backup and local / cloud runtime',54),('test_runtime','Actual state read / write test, date and evidence',54),('optional','Optional blog / Instagram; Brand Closet permission or disabled',42)])
formpage('One product intake','Use one page per product. Complete every item in a look before marking the look ready. No sample ASIN or guessed link is ready.',[
 ('product_look','Look name, product number and customer-selected ASIN',36),('product_desc','Your written description, color, material, shape and visual details',66),('special_link','Your own verified Amazon Special Link',54),('product_destination','Published Idea List or look-page URL for this look',54),('product_image_rights','Reference image and commercial / transformation rights, or none',54),('intake_status','Ready / HOLD and any missing information or next action',36)])
formpage('Review one finished Pin','Fill the full record before approval. Count title and caption characters using your editor or a short chat request.',[
 ('pin_id','Stable ID, look and image file reference',36),('pin_title','Title and character count',42),('pin_caption','Caption and character count',96),('pin_alt','Alt text describing the actual image',54),('pin_link_board','Exact destination URL, public board and section',54),('pin_time','Your chosen date, time and timezone; AI-content / AI-person labels',36)])
formpage('Approval and external record','Approval applies to this exact finished Pin. A withdrawn date stays HOLD; it is not replaced automatically.',[
 ('approved_record','Stable ID and final image / copy version reviewed',42),('checks','Rights, image, disclosures, link and board checks; evidence',66),('approval','APPROVE or HOLD, your name and approval date / time',42),('owning_service','Owning service and exact external record ID / URL',54),('external_status','Observed draft / scheduled / published status and exact date / time',54),('pull','PULL / withdrawal request and observed external change, or none',54)])
formpage('Test and recovery log','Pass only the behavior you observed. Native Pinterest and Metricool have separate records.',[
 ('log_date','Test date, stable ID and owning service',36),('log_expected','Expected behavior and fields',54),('log_observed','Observed result and evidence / screenshot reference',78),('log_result','PASS / UNVERIFIED / FAILED and the exact reason',54),('log_next','Next action, owner and required approval if any',54),('log_resume','Work preserved, duplicate check and resume condition',54)])
workbook=OUT/'While-You-Sleep-Storefront-Prompts-and-Workbook.pdf'
SimpleDocTemplate(str(workbook),pagesize=letter,leftMargin=48,rightMargin=48,topMargin=82,bottomMargin=67,title='While You Sleep Storefront Prompts and Workbook',author='The Digital Income Edit').build(work,onFirstPage=decor,onLaterPages=decor)
package=ROOT/'While-You-Sleep-Storefront-Kit.zip'
with zipfile.ZipFile(package,'w',zipfile.ZIP_DEFLATED) as z:
 z.write(guide,'1 START HERE - Storefront Buyer Guide.pdf')
 z.write(workbook,'2 Storefront Prompts and Editable Workbook.pdf')
with zipfile.ZipFile(package) as z:
 assert z.testzip() is None
 assert len(z.namelist())==2 and all(n.endswith('.pdf') for n in z.namelist())
g=PdfReader(guide);w=PdfReader(workbook)
fields=w.get_fields() or {}
assert len(fields)==36, len(fields)
assert all('/V' in v for v in fields.values())
widgets=[a.get_object() for p in w.pages for a in p.get('/Annots',[]) if a.get_object().get('/Subtype')=='/Widget']
assert len(widgets)==36 and all(a.get('/AP',{}).get('/N') for a in widgets)
text='\n'.join(p.extract_text() for p in g.pages)
assert not re.search(r'\b\d{2}_[A-Z_]+\.txt',text)
result={'guide_pages':len(g.pages),'workbook_pages':len(w.pages),'editable_fields':len(fields),'package_contents':zipfile.ZipFile(package).namelist(),'package_sha256':hashlib.sha256(package.read_bytes()).hexdigest()}
(ROOT/'buyer-package-validation.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result))
