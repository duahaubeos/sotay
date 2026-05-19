import os
import re
import json
import sys
from unidecode import unidecode

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"c:\Users\asus\OneDrive - Trường Ngôi Sao Hoàng Mai\Desktop\phiếu nhận xét học sinh cuối năm\web_so_lo_xo"
parent_dir = r"c:\Users\asus\OneDrive - Trường Ngôi Sao Hoàng Mai\Desktop\phiếu nhận xét học sinh cuối năm"
html_path = os.path.join(base_dir, 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

results_match = re.search(r'let academicResults = (\[.*?\]);', html_content, re.DOTALL)
if not results_match:
    print("Could not find academicResults!")
    sys.exit(1)

students = json.loads(results_match.group(1))
student_names = [s["name"] for s in students]

print(f"Total students in DB: {len(student_names)}")
for idx, name in enumerate(student_names):
    print(f"  {idx+1}. {name}")

parent_pngs = [f for f in os.listdir(parent_dir) if f.lower().endswith('.png') and not f.startswith('tải xuống') and f != 'back.png' and f != 'mẫu.png']
print(f"\nTotal PNG files in parent directory: {len(parent_pngs)}")
for f in sorted(parent_pngs):
    print(f"  - {f}")

# Try matching them
matched = {}
unmatched_students = []
for name in student_names:
    norm_name = unidecode(name).lower().replace(" ", "")
    found = None
    for png in parent_pngs:
        png_name = os.path.splitext(png)[0]
        norm_png = unidecode(png_name).lower().replace(" ", "")
        
        # Match sub-parts or direct matches
        if norm_name in norm_png or norm_png in norm_name:
            found = png
            break
            
    if found:
        matched[name] = found
    else:
        unmatched_students.append(name)

print("\nMATCHED SUMMARY:")
print(f"Matched: {len(matched)}")
for k, v in matched.items():
    print(f"  - {k} -> {v}")

print(f"\nUNMATCHED STUDENTS ({len(unmatched_students)}):")
for u in unmatched_students:
    print(f"  - {u}")
