from pathlib import Path
import urllib.request,json,hashlib
from PIL import Image
root=Path(__file__).resolve().parent.parent
out=root/'work/new-sourcing';out.mkdir(exist_ok=True)
products=[dict(asin='B0C8BKT7YZ',name='PAVOI polished teardrop hoop earrings',variant='White Gold / 31 Millimeters',review_rating=4.4,review_count=411,image_url='https://m.media-amazon.com/images/I/61pOv9j0yiL._AC_SL1500_.jpg',quality_note='Smooth substantial-looking teardrops repeat the silver shoes without competing with the square neckline. Manufacturer specifies lightweight construction and sterling-silver posts; plating is not solid gold or solid sterling silver. Fit and long-term finish require care; no wear-test claim.'),dict(asin='B07TBNQYYN',name='PAVOI 3mm cubic-zirconia tennis bracelet',variant='White Gold / 7 Inches',review_rating=4.3,review_count=32114,image_url='https://m.media-amazon.com/images/I/61uQR+29l3L._AC_SL1500_.jpg',quality_note='One slim line of clear stones complements silver footwear and adds a separate wrist detail; not a bundle counted as several products. White-gold-plated brass with cubic zirconia, not diamonds. Wrist measurement matters. Aggregated reviews combine variants; no lifetime durability or wear-test claim.')]
for p in products:
 p.update(url='https://www.amazon.com/dp/'+p['asin'],affiliate_link=None,checked_at='2026-10-08',evidence='Official Amazon listing retrieved through web search on 8 Oct 2026; selected ASIN, variant, product image, displayed aggregate rating/count inspected. Retrieval was a cached crawl about four weeks old; not a live stock or current price verification. Manufacturer material/shape details crosschecked where available.',reference='references/'+p['asin']+'.jpg',reference_usage='Private product-fidelity source reference; no public republication claim.')
 f=out/(p['asin']+'.jpg');f.write_bytes(urllib.request.urlopen(p['image_url'],timeout=40).read())
 p['reference_dimensions']=list(Image.open(f).size);p['reference_sha256']=hashlib.sha256(f.read_bytes()).hexdigest()
(out/'ADDED-PRODUCTS.json').write_text(json.dumps(products,indent=2)+'\n',encoding='utf-8')
print(json.dumps([{'asin':p['asin'],'dimensions':p['reference_dimensions']} for p in products]))
