import json
import os
import re
import glob
import shutil

base_dir = r'c:\Users\asus\OneDrive - Trường Ngôi Sao Hoàng Mai\Desktop\phiếu nhận xét học sinh cuối năm\web_so_lo_xo'

# Load names
with open(os.path.join(base_dir, 'names.json'), 'r', encoding='utf-8') as f:
    data = json.load(f)

students = []
for row in data:
    try:
        stt = row.get("Unnamed: 0")
        name = row.get("Unnamed: 1")
        if isinstance(stt, (int, float)) and name and isinstance(name, str) and not "HỌ VÀ TÊN" in name.upper():
            students.append(name)
    except:
        pass

# Collect images
media_dir = os.path.join(base_dir, 'pptx_media', 'ppt', 'media')
images = glob.glob(os.path.join(media_dir, '*.*'))

# Filter images > 50KB to avoid small icons
valid_images = []
for img in images:
    if img.endswith(('.jpeg', '.png', '.jpg')):
        if os.path.getsize(img) > 50000:
            valid_images.append(os.path.basename(img))
valid_images.sort()

# Generate student cards HTML
html_cards = []
for i, name in enumerate(students):
    img = valid_images[i % len(valid_images)] if valid_images else 'boy.png'
    src_img = os.path.join(media_dir, img)
    dest_img = os.path.join(base_dir, 'assets', img)
    if os.path.exists(src_img) and not os.path.exists(dest_img):
        shutil.copy2(src_img, dest_img)
            
    card = f'''
                            <div class="student-card">
                                <img src="assets/{img}" alt="Học sinh">
                                <h4>{name}</h4>
                            </div>'''
    html_cards.append(card)

cards_html = '\n'.join(html_cards)

# Update index.html
html_path = os.path.join(base_dir, 'index.html')
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Replace student grid
pattern = r'<div class="student-grid">.*?</div>\s*</div>\s*</div>'
replacement = f'<div class="student-grid">\n{cards_html}\n                        </div>\n                    </div>\n                </div>'
html_content = re.sub(pattern, replacement, html_content, flags=re.DOTALL)

# Update Teacher name
html_content = html_content.replace('Cô Nguyễn Thị Hương', 'Cô Nguyễn Thị Thu Cúc')

# Update font in HTML
font_link = '<link href="https://fonts.googleapis.com/css2?family=Edu+VIC+WA+NT+Beginner:wght@400..700&display=swap" rel="stylesheet">'
html_content = html_content.replace('<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;700;900&family=Patrick+Hand&display=swap" rel="stylesheet">', font_link)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

# Update style.css
css_path = os.path.join(base_dir, 'style.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

css_content = css_content.replace("'Nunito', sans-serif", "'Edu VIC WA NT Beginner', cursive")
css_content = css_content.replace("'Patrick Hand', cursive", "'Edu VIC WA NT Beginner', cursive")

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_content)

print(f"Updated {len(students)} students.")
