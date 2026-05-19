import os
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"c:\Users\asus\OneDrive - Trường Ngôi Sao Hoàng Mai\Desktop\phiếu nhận xét học sinh cuối năm\web_so_lo_xo"
html_path = os.path.join(base_dir, 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

results_match = re.search(r'let academicResults = (\[.*?\]);', html_content, re.DOTALL)
if not results_match:
    print("Could not find academicResults!")
    sys.exit(1)

students = json.loads(results_match.group(1))
print("First student keys & sample values:")
for k, v in students[0].items():
    if k != 'grades':
        print(f"  - {k}: {v}")
    else:
        print(f"  - {k}: (dict with {len(v)} keys)")
