# Buyer delivery

The customer ZIP contains exactly two documents: the 19-page Buyer Guide and the 15-page Prompts and Editable Workbook. The workbook has 36 editable PDF fields. The kit directory contains internal reference inputs, not customer download files.

Rebuild with build_buyer_package.py (Python, reportlab and pypdf). render.mjs calls that builder. Do not use the earlier build_guide.py to assemble customer delivery.

Validation: all pages rendered and inspected; all 36 fields populated in a test copy, saved and reopened; every field is inside page margins; ZIP integrity checked with exactly two PDF entries and no raw TXT/Markdown files.

Beacons member product 36b6f2a8-d26b-4e03-9fa5-b4b698fcf84f: new 44.76 KB ZIP uploaded. Old 2.80 MB attachment removal awaits the service deletion confirmation. Customer checkout/receipt delivery is not yet verified. Public presale PDF remains a separate delivery.
