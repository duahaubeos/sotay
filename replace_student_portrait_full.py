import os
import shutil
import re
import sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

# Inputs passed as command line arguments or variables
if len(sys.argv) < 3:
    print("Usage: python replace_student_portrait_full.py <src_path> <student_name>")
    sys.exit(1)

src_path = sys.argv[1]
student_name = sys.argv[2]

html_path = r"c:\Users\asus\OneDrive - Trường Ngôi Sao Hoàng Mai\Desktop\phiếu nhận xét học sinh cuối năm\web_so_lo_xo\index.html"
dest_dir = r"c:\Users\asus\OneDrive - Trường Ngôi Sao Hoàng Mai\Desktop\phiếu nhận xét học sinh cuối năm\web_so_lo_xo\assets\students"

# 1. Read index.html to find student details
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's search for the student inside academicResults
array_start = content.find('let academicResults = [')
array_end = content.find('];', array_start)
array_content = content[array_start:array_end]

# Find the student's entry
student_idx = array_content.find(f'"name": "{student_name}"')
if student_idx == -1:
    matches = [m.start() for m in re.finditer(re.escape(student_name), array_content, re.IGNORECASE)]
    if matches:
        student_idx = matches[0]
    else:
        print(f"Error: Could not find student '{student_name}' in academicResults!")
        sys.exit(1)

# Find the portrait property for this student
portrait_match = re.search(r'"portrait":\s*"([^"]+)"', array_content[student_idx:student_idx+500])
if not portrait_match:
    print(f"Error: Could not find portrait property for '{student_name}'!")
    sys.exit(1)

old_portrait_path = portrait_match.group(1) # e.g. "assets/students/student_0.jpg" or "assets/students/student_0_real.jpg"

# Find the report_img property for this student
report_match = re.search(r'"report_img":\s*"([^"]+)"', array_content[student_idx:student_idx+500])
if not report_match:
    print(f"Error: Could not find report_img property for '{student_name}'!")
    sys.exit(1)

report_img_path = report_match.group(1) # e.g. "assets/reports/report_0.png"
print(f"Current portrait path: {old_portrait_path}")
print(f"Current report_img path: {report_img_path}")

# Extract student index from old portrait (e.g. student_0)
student_id_match = re.search(r'student_(\d+)', old_portrait_path)
if not student_id_match:
    print(f"Error: Could not parse student ID from portrait path '{old_portrait_path}'!")
    sys.exit(1)

student_id = student_id_match.group(1)
ext = os.path.splitext(src_path)[1].lower() # e.g. ".jpg" or ".png"

new_portrait_filename = f"student_{student_id}_real{ext}"
new_portrait_path = f"assets/students/{new_portrait_filename}"
dest_portrait_path = os.path.join(dest_dir, new_portrait_filename)

# 2. Copy the real photo to assets/students
shutil.copy2(src_path, dest_portrait_path)
print(f"Successfully copied real portrait of {student_name} to: {dest_portrait_path}")

# 3. Update index.html
# Update the grid HTML image src (both old_portrait_path and potential previous versions like _real)
content = content.replace(f'src="{old_portrait_path}"', f'src="{new_portrait_path}"')
# Also replace inside the array entry
content = content.replace(f'"portrait": "{old_portrait_path}"', f'"portrait": "{new_portrait_path}"')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Successfully updated index.html with new portrait path: {new_portrait_path}")

# 4. Paste real photo over the chibi avatar inside the A4 report card
# Report card path is e.g. assets/reports/report_0.png
web_dir = r"c:\Users\asus\OneDrive - Trường Ngôi Sao Hoàng Mai\Desktop\phiếu nhận xét học sinh cuối năm\web_so_lo_xo"
full_report_path = os.path.join(web_dir, report_img_path.replace('/', '\\'))

if os.path.exists(full_report_path):
    try:
        report_img = Image.open(full_report_path)
        real_photo = Image.open(src_path)
        
        # Center crop real photo to square
        w, h = real_photo.size
        min_dim = min(w, h)
        left = (w - min_dim) // 2
        top = (h - min_dim) // 2
        right = left + min_dim
        bottom = top + min_dim
        
        square_photo = real_photo.crop((left, top, right, bottom))
        
        # Resize to 245x245 (chibi template coordinates)
        resized_photo = square_photo.resize((245, 245), Image.Resampling.LANCZOS)
        
        # Paste onto report
        report_img.paste(resized_photo, (156, 522))
        report_img.save(full_report_path, "PNG")
        print(f"Successfully updated A4 report card image '{report_img_path}' with real photo!")
    except Exception as e:
        print(f"Error updating report card image: {e}")
else:
    print(f"Warning: Report card image file '{full_report_path}' does not exist!")
