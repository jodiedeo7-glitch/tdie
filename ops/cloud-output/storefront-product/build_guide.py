from pathlib import Path
import json, shutil, zipfile
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from xml.sax.saxutils import escape

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'pdf'; OUT.mkdir(exist_ok=True)
PAGES=[
('Start with the path that suits you', 'The While-You-Sleep Storefront', [
('Your product choices. Your approval.', 'Turn your prepared Amazon product selection into original styling images and Pinterest Pins linked to an eligible Idea List or your live shop-the-look page. You review each finished Pin before publication.'),
('Time-saving path', 'Use supported connected tools to prepare images, copy and a queue. Publishing is optional, account-specific and tested. Your exact finished Pin, destination, board and posting time need your approval.'),
('Low-cost Claude or ChatGPT path', 'Use the plan you already have for a short planning or copy request, within your limits. Generate one image only if that feature and commercial use are available. No paid scheduler is required.'),
('Manual alternative', 'Choose products yourself, use your own or licensed asset or original layout, write the fields, and use Pinterest native scheduling. AI and paid automation are optional.'),
('Before you begin', 'Read 01_REQUIREMENTS.txt. This guide replaces the older hands-off setup PDF. Historical examples are not current tests. No sales, account approval or unattended result is promised.')]),
('Step 1', 'Check your Amazon path', [
('Associates and Influencer are distinct', 'Influencer is part of the Associates Program and adds eligibility and storefront/content features. Record your Associates and Influencer status separately. Influencer status does not replace the Associates disclosure.'),
('Check the account you actually have', 'Verify Storefront and Idea List access separately. Amazon changed creator Storefront wording in April 2026, so do not assume a universal Influencer-only rule or promise every Associates account the same features.'),
('Destination', 'Use an existing eligible public Idea List when supported. Otherwise use your compliant live website page and your own Special Links. Test public visibility separately from the owner view.'),
('Low-cost Claude or ChatGPT', 'Give chat your selected product facts and request one list title and description. Do not ask it to invent an ASIN, link or entitlement.'),
('Manual alternative', 'Choose products, capture your own Special Links, create the Idea List and record its exact URL yourself. Keep registered sites and social profiles current, finish the save and read the result back.')]),
('Step 2', 'Create persistent working state', [
('One production workspace', 'Keep MY_RECIPE.txt, PRODUCT_SOURCES.md, storefront-log.md, pin-tab.md and pin-drafts.md together. Keep a local backup. Separate production from test records and from other TDIE automation.'),
('Record what is known', 'Save your theme, timezone, exact public board and section, Amazon destination, image provider/model, rights evidence, maximum image budget, runtime and publishing method. Leave unverified choices UNKNOWN.'),
('Local or cloud', 'A local runtime needs the configured host available. A cloud runtime needs state and connections accessible in that cloud environment. Prove read/write persistence with a draft-only run. A local folder is not automatically cloud state.'),
('Low-cost Claude or ChatGPT', 'Paste the setup prompt in 02_SETUP_PROMPT.txt into a chat. Ask it to format your answers and draft the state files; verify the saved content yourself.'),
('Manual alternative', 'Fill the same settings and queue fields in text files. No scheduled task is required. Browser locking is only relevant where work actually shares a browser.')]),
('Step 3', 'Prepare a ready product intake', [
('One look, one destination', 'Start with one coherent selection. Record the look, proposed date, ASINs, your written product descriptions, color/material details, Special Links, destination URL and reference rights in PRODUCT_SOURCES.md.'),
('Customer-owned Amazon work', 'The default agent reads your prepared intake. It does not create Amazon links or lists, browse as a disguised person, or invent missing product data. An approved integration is optional and requires independent eligibility.'),
('Image rights', 'Use written attributes, customer-owned images or an explicit license covering transformation and commercial use. Public Amazon product photographs and paid classroom access do not automatically supply those rights.'),
('Low-cost Claude or ChatGPT', 'Ask chat to organize one look from facts you supply. Keep requests small and reject any invented link, product detail or rights claim.'),
('Manual alternative', 'Choose the items and write the intake table yourself. Missing information means HOLD. Complete the row before generating images or preparing a publication.')]),
('Step 4', 'Make and inspect your image', [
('Optional time-saving route', 'Use only the provider/model and connector verified on your account. Website Unlimited is not proof of connector or API Unlimited. Set a spend limit before generation.'),
('Inspect the actual asset', 'Check product count, color, fabric, hands, framing, logos and spelling. Persona references need consent and rights. A person-free flat lay or collage is a normal option.'),
('Low-cost Claude or ChatGPT', 'Use one selected generation if available within your plan limits and commercial terms. Fix only the failed asset. Keep a valid companion image.'),
('Manual alternative', 'Use your own photograph, licensed image or original layout. Add readable text in your normal editor. No AI generation, provider subscription or persona is required.'),
('Represent it honestly', 'Describe generated styling as inspiration, not product photography. If the linked list contains similar pieces, say so. Use applicable Pinterest AI-content and AI-person labels.')]),
('Step 5', 'Write a finished Pin record', [
('Required fields', 'Save the image, accurate title, caption, alt text, exact destination, public board/section and intended date/time in the queue. A stable ID ties the look, Pin number and timestamp to its external record.'),
('Kit copy rules', 'Title: 60-100 characters. Caption: 450-500 characters. Use generic item descriptions, no prices, and no product brand, film or character names. Alt text describes what the image actually shows.'),
('Disclosure', 'Begin the caption with #ad. End it with: As an Amazon Associate I earn from qualifying purchases. Place the required statement prominently on the linked social account/profile too. Influencer is your account status; Associate is the required program disclosure.'),
('Low-cost Claude or ChatGPT', 'Request one title, caption and alt text from verified intake and the actual image. Count characters and read every field before approval.'),
('Manual alternative', 'Write the same fields yourself from this checklist. Confirm that the caption explains AI styling and similar-product destinations accurately. Approval of one record does not approve later Pins.')]),
('Step 6', 'Schedule only the approved Pin', [
('Manual is the default fallback', 'In Pinterest native composer, upload the finished image, paste the approved fields, choose the exact public board and set the approved date/time. Review before confirming. Then reopen the saved record.'),
('Optional connected publisher', 'A supported approved connector, Metricool or developer API is a separate account test. Verify access, board resolution, media, link, alt text, approval and schedule. Missing capability means BUILD/QUEUE ONLY.'),
('Individual approval', 'Approve the exact finished image, copy, destination, board and date/time. Missing approval means HOLD. A withdrawn date never becomes a substitute date automatically.'),
('Low-cost Claude or ChatGPT', 'Have chat prepare a compact field checklist. Schedule it yourself in the native interface; no developer application or paid scheduler is needed.'),
('Manual alternative', 'Review and schedule each Pin yourself. Record its exact external ID and service. Native Pinterest and Metricool are separate inventories; check both before creating another record.')]),
('Step 7', 'Reconcile before you retry', [
('Read back first', 'Match the exact external ID, image, title, caption, destination, board and posting time. Mark passed only when observed. Save evidence and the result in storefront-log.md and pin-tab.md.'),
('Failure or timeout', 'Preserve completed work and check the external service before retrying. Do not create a duplicate stable ID, replace a date, change a model or buy credits automatically.'),
('Withdrawal and PULL', 'HOLD stops new publication. PULL is a requested removal/change, not permission to publish. Confirm any change by external readback. Draft status alone is not proof that all automatic publishing settings are disabled.'),
('Low-cost Claude or ChatGPT', 'Give chat the current scheduler statuses for one comparison. Ask it to identify unknowns and the exact next action.'),
('Manual alternative', 'Inspect native Pinterest and Metricool separately and update the log yourself. Verify a public destination while signed out when possible. Owner-session visibility is a separate result.')]),
('Optional additions', 'Add only what you need', [
('Scheduled work', '06_SCHEDULED_TASK_PROMPTS.txt supplies weekly planning, optional permission-gated OOTD and reconciliation templates. They are not installed tasks or proof of a run. Use your confirmed timezone and actual schedule.'),
('Blog half', 'Prepare an original page from verified intake. Low-cost chat can draft one page; manually paste it into your editor. A supported site connector is optional. Confirm the live page before linking a Pin.'),
('Brand Closet OOTD', 'Keep this disabled until paid-content rights, access and the recipe permission gate pass. Low-cost chat can use your own original styling brief. Manual alternative: make your own look and skip paid content.'),
('Instagram and referrals', 'Keep these separate from the core workflow. Verify current program access and disclosure. Do not put earnings claims on Facebook or Instagram. Scheduled affiliate availability is not evidence that it is live.'),
('Upgrade only a real bottleneck', 'Compare actual volume, plan allowance and time saved. Every automated step has the low-cost and manual paths in 12_OPERATION_MODES.txt. Test before claiming it works.')]),
('Verification and references', 'What counts as ready', [
('Account checklist', 'Associates/Influencer capabilities, registered traffic sources, public destination, exact public board, state persistence, image rights and budget, approved Pin fields and publishing method all need evidence.'),
('Historical example', 'The project includes earlier Halloween and OOTD examples. They illustrate styling, not current release readiness. Reverify their account, board, rights, links and schedule before using any result as proof.'),
('Amazon agreement and disclosure', 'https://affiliate-program.amazon.com/help/operating/agreement\nhttps://affiliate-program.amazon.com/help/node/topic/GPXFHVYZMTGPUMPE'),
('Amazon program and change notice', 'https://affiliate-program.amazon.com/help/operating/policies\nhttps://affiliate-program.amazon.com/help/operating/compare'),
('Pinterest requirements', 'https://policy.pinterest.com/en/developer-guidelines\nhttps://policy.pinterest.com/en/terms-of-service'),
('Policy vs account proof', 'References checked September 30, 2026. Official rules explain requirements. Your current account and a read-back test establish capability. See SOURCES.md; record unresolved checks and the next action.')])]

styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='TitleTDIE',fontName='Times-Roman',fontSize=31,leading=34,textColor=HexColor('#1A1417'),spaceAfter=20))
styles.add(ParagraphStyle(name='Kicker',fontName='Helvetica-Bold',fontSize=10,leading=14,textColor=HexColor('#D62E73'),spaceAfter=12))
styles.add(ParagraphStyle(name='Label',fontName='Helvetica-Bold',fontSize=11,leading=15,textColor=HexColor('#A81F57'),spaceAfter=5))
styles.add(ParagraphStyle(name='Copy',fontName='Helvetica',fontSize=10.5,leading=15,textColor=HexColor('#4A3F44'),spaceAfter=14))
def decor(c,d):
 c.setFillColor(HexColor('#FBF8F5'));c.rect(0,0,612,792,fill=1,stroke=0)
 c.setFillColor(HexColor('#D62E73'));c.rect(0,780,612,12,fill=1,stroke=0)
 c.setFont('Helvetica-Bold',9);c.drawString(48,746,'THE DIGITAL INCOME EDIT')
 c.setStrokeColor(HexColor('#C8A96A'));c.line(48,48,564,48)
 c.setFont('Helvetica',8);c.setFillColor(HexColor('#4A3F44'));c.drawString(48,33,'WHILE-YOU-SLEEP STOREFRONT | SETUP GUIDE | REVISED SEP 30, 2026');c.drawRightString(564,33,str(d.page))
story=[]
for idx,(k,title,sections) in enumerate(PAGES):
 if idx:story.append(PageBreak())
 story += [Paragraph(escape(k.upper()),styles['Kicker']),Paragraph(escape(title),styles['TitleTDIE'])]
 for label,body in sections:
  story.append(KeepTogether([Paragraph(escape(label),styles['Label']),Paragraph(escape(body).replace('\n','<br/>'),styles['Copy'])]))
pdf=OUT/'While-You-Sleep-Storefront-Setup-Guide.pdf'
SimpleDocTemplate(str(pdf),pagesize=letter,leftMargin=48,rightMargin=48,topMargin=83,bottomMargin=67,title='While-You-Sleep Storefront Setup Guide',author='The Digital Income Edit').build(story,onFirstPage=decor,onLaterPages=decor)
shutil.copy2(pdf,ROOT/'kit'/pdf.name)
jsonpath=ROOT/'guide-content.json';jsonpath.write_text(json.dumps(PAGES,indent=2),encoding='utf-8')
with zipfile.ZipFile(ROOT/'While-You-Sleep-Storefront-Kit.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in sorted((ROOT/'kit').iterdir()):z.write(p,p.name)
print(json.dumps({'pdf':str(pdf),'pages_expected':len(PAGES),'kit_files':len(list((ROOT/'kit').iterdir()))}))
