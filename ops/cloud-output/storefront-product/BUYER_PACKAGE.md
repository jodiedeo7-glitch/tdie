# Buyer delivery

The customer ZIP contains exactly two documents: the 19-page Buyer Guide and the 15-page Prompts and Editable Workbook with 36 editable PDF fields. The kit directory contains internal reference inputs, not customer download files.

Rebuild with build_buyer_package.py (Python, reportlab and pypdf). render.mjs calls that builder. Do not use the earlier build_guide.py to assemble customer delivery. Rebuild the separate public presale note with build_presale_note.py.

Member attachment replacement and configured download integrity were verified after old file removal. See BUYER_DELIVERY_VERIFICATION_2026-09-30.md for evidence and remaining checks.
