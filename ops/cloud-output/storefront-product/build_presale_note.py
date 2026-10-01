from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from pypdf import PdfReader
root=Path(__file__).resolve().parent
out=root/'pdf'/'While-You-Sleep-Storefront-Presale.pdf'
pink=HexColor('#B52964');ink=HexColor('#282126')
title=ParagraphStyle('title',fontName='Times-Roman',fontSize=30,leading=34,textColor=ink,spaceAfter=22)
head=ParagraphStyle('head',fontName='Helvetica-Bold',fontSize=11,leading=15,textColor=pink,spaceAfter=6)
body=ParagraphStyle('body',fontName='Helvetica',fontSize=11,leading=16,textColor=ink,spaceAfter=18)
story=[Paragraph('Your Storefront presale',title),Paragraph('You are in',head),Paragraph('Thank you for joining the While-You-Sleep Storefront presale. This is your presale note. The full buyer kit is planned for Friday, October 9, 2026 at 9 am Eastern.',body),Paragraph('Keep this download access',head),Paragraph('Return through your Beacons receipt or customer portal at release to access the kit. Keep your receipt so you can find your order and download access again.',body),Paragraph('Get ready without buying extra tools',head),Paragraph('Choose a theme, check your Amazon Associates and Influencer status and the Storefront or Idea List features actually available to you, and prepare a Pinterest business account with a public board. Select your own products and affiliate links. Use your own or licensed images, or an original layout.',body),Paragraph('Choose the path that fits you',head),Paragraph('Use your existing Claude or ChatGPT plan for short planning and copy requests within your account limits, or complete the steps manually. A paid scheduler, developer application, image subscription, Claude in Chrome, Gemini or Higgsfield is not required for the manual path. Optional connected tools need testing on your own account.',body),Paragraph('What the kit will help you do',head),Paragraph('Prepare original styling Pins linked to your eligible public Idea List or published look page, review each finished Pin, and schedule it using your chosen supported route. The buyer guide includes low-cost and manual alternatives, with a separate prompt workbook and editable worksheets. No sales or unattended result is promised.',body),Paragraph('xoxo, Jodie',body)]
def decor(c,d):
 c.setFillColor(HexColor('#FCF9F7'));c.rect(0,0,612,792,fill=1,stroke=0)
 c.setFillColor(pink);c.rect(0,782,612,10,fill=1,stroke=0)
 c.setFillColor(ink);c.setFont('Helvetica-Bold',9);c.drawString(48,751,'THE DIGITAL INCOME EDIT')
 c.setStrokeColor(HexColor('#CEBBA5'));c.line(48,48,564,48)
 c.setFont('Helvetica',8);c.drawString(48,33,'WHILE-YOU-SLEEP STOREFRONT | PRESALE NOTE | REVISED SEPTEMBER 2026')
SimpleDocTemplate(str(out),pagesize=letter,leftMargin=48,rightMargin=48,topMargin=82,bottomMargin=66,title='While You Sleep Storefront Presale',author='The Digital Income Edit').build(story,onFirstPage=decor,onLaterPages=decor)
assert len(PdfReader(out).pages)==1
print('One-page corrected presale PDF saved.')
