import json
import os
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

index_html = f'''<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kỷ Yếu Cuối Năm - Lớp 4C</title>
    <link rel="stylesheet" href="style.css">
    <link href="https://fonts.googleapis.com/css2?family=Edu+VIC+WA+NT+Beginner:wght@400..700&display=swap" rel="stylesheet">
</head>
<body>
    <div class="notebook-wrapper">
        <div class="notebook">
            <!-- Left Page -->
            <div class="page left-page">
                <div class="page-content">
                    <h1>Trường Tiểu học Mỹ Thuận 1</h1>
                    <div class="hero-image-container">
                        <img src="assets/school.png" alt="Trường Tiểu học Mỹ Thuận 1" class="photo">
                    </div>
                    
                    <div class="teacher-box">
                        <img src="assets/teacher.png" alt="GVCN" class="teacher-photo">
                        <div class="teacher-text">
                            <h2>GVCN: Cô Nguyễn Thị Thu Cúc</h2>
                            <p>"Chúc các con lớp 4C một mùa hè vui vẻ và chuẩn bị tinh thần thật tốt cho năm học mới nhé!"</p>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Center Spiral -->
            <div class="spiral-container">
            </div>
            
            <!-- Right Page -->
            <div class="page right-page">
                <div class="page-content">
                    <div style="text-align: center;">
                        <h2 class="class-title">Danh sách lớp 4C</h2>
                    </div>
                    <div class="student-grid">
{cards_html}
                    </div>
                </div>
            </div>
            
            <!-- Tabs -->
            <div class="tabs">
                <div class="tab tab-1">Lớp 4C</div>
                <div class="tab tab-2">2023-2024</div>
            </div>
        </div>
    </div>
    <script src="script.js"></script>
</body>
</html>
'''

with open(os.path.join(base_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(index_html)

style_css = '''
:root {
    --bg-color: #f0e6d2; 
    --notebook-bg: #fff;
    --text-color: #2c3e50;
    --primary: #ff7675;
    --secondary: #74b9ff;
    --accent: #ffeaa7;
    --font-main: 'Edu VIC WA NT Beginner', cursive;
}

body {
    background-color: var(--bg-color);
    background-image: url('https://www.transparenttextures.com/patterns/wood-pattern.png');
    font-family: var(--font-main);
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    color: var(--text-color);
}

.notebook-wrapper {
    width: 95%;
    max-width: 1200px;
    height: 85vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

.notebook {
    display: flex;
    width: 100%;
    height: 100%;
    background: transparent;
    position: relative;
    box-shadow: 0 20px 50px rgba(0,0,0,0.3);
    border-radius: 10px;
}

.page {
    flex: 1;
    background: var(--notebook-bg);
    position: relative;
    overflow-y: auto;
    /* Lined paper effect */
    background-image: repeating-linear-gradient(transparent, transparent 29px, #74b9ff44 30px);
    background-position: 0 40px;
}

.left-page {
    border-radius: 15px 0 0 15px;
    box-shadow: inset -10px 0 20px rgba(0,0,0,0.05);
    padding: 40px 30px;
}

.right-page {
    border-radius: 0 15px 15px 0;
    box-shadow: inset 10px 0 20px rgba(0,0,0,0.05);
    padding: 40px 30px;
}

.page::-webkit-scrollbar { width: 8px; }
.page::-webkit-scrollbar-thumb { background: #dfe6e9; border-radius: 4px; }

/* Center spiral */
.spiral-container {
    width: 40px;
    background: linear-gradient(to right, #e0e0e0, #f5f5f5, #e0e0e0);
    position: relative;
    z-index: 10;
    box-shadow: inset 5px 0 10px rgba(0,0,0,0.1), inset -5px 0 10px rgba(0,0,0,0.1);
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    align-items: center;
}

.ring {
    width: 60px;
    height: 15px;
    background: linear-gradient(to bottom, #bdc3c7, #fff, #7f8c8d);
    border-radius: 10px;
    box-shadow: 2px 3px 5px rgba(0,0,0,0.4);
    position: relative;
    left: 0;
}

/* Content Styles */
h1 {
    color: var(--primary);
    font-size: 3.5rem;
    text-align: center;
    margin-top: 0;
    text-shadow: 2px 2px 0px #ffeaa7;
}

.hero-image-container {
    text-align: center;
    position: relative;
    margin: 20px 0;
}

.photo {
    width: 80%;
    max-width: 400px;
    border: 10px solid white;
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    transform: rotate(-2deg);
}

.teacher-box {
    display: flex;
    align-items: center;
    background: #fff9e6;
    padding: 20px;
    border-radius: 15px;
    border: 2px dashed #f1c40f;
    margin-top: 40px;
}

.teacher-photo {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    object-fit: cover;
    border: 4px solid var(--primary);
    margin-right: 20px;
}

.teacher-text h2 {
    color: var(--primary);
    margin: 0 0 10px 0;
    font-size: 1.8rem;
}
.teacher-text p {
    margin: 0;
    font-size: 1.3rem;
    line-height: 1.5;
}

.class-title {
    color: var(--secondary);
    font-size: 2.8rem;
    text-align: center;
    margin-top: 0;
    margin-bottom: 30px;
    border-bottom: 3px dashed var(--secondary);
    display: inline-block;
    padding-bottom: 10px;
}

.student-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(110px, 1fr));
    gap: 20px;
}

.student-card {
    text-align: center;
    background: #fff;
    padding: 10px;
    border-radius: 8px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    border: 1px solid #eee;
    transition: transform 0.2s;
    position: relative;
}

.student-card::before {
    content: '';
    position: absolute;
    top: -10px;
    left: 50%;
    transform: translateX(-50%) rotate(-3deg);
    width: 40px;
    height: 15px;
    background: rgba(255,255,255,0.7);
    border: 1px solid #ddd;
    z-index: 2;
}

.student-card:hover {
    transform: scale(1.05) rotate(2deg);
}

.student-card img {
    width: 80px;
    height: 80px;
    border-radius: 50%;
    object-fit: cover;
    border: 3px solid #dfe6e9;
    margin-bottom: 10px;
}

.student-card h4 {
    margin: 0;
    font-size: 1.3rem;
    color: #2d3436;
    font-weight: bold;
}

.tabs {
    position: absolute;
    right: -40px;
    top: 50px;
    display: flex;
    flex-direction: column;
    gap: 20px;
}
.tab {
    background: var(--primary);
    color: white;
    padding: 15px 10px;
    writing-mode: vertical-rl;
    text-orientation: mixed;
    border-radius: 0 10px 10px 0;
    font-size: 1.2rem;
    box-shadow: 4px 4px 10px rgba(0,0,0,0.2);
    cursor: pointer;
}
.tab-2 {
    background: var(--secondary);
}

@media (max-width: 800px) {
    .notebook {
        flex-direction: column;
        height: 90vh;
    }
    .spiral-container {
        width: 100%;
        height: 40px;
        flex-direction: row;
    }
    .ring {
        width: 15px;
        height: 60px;
    }
    .left-page, .right-page {
        border-radius: 15px;
        width: 100%;
        box-sizing: border-box;
    }
    .tabs { display: none; }
}
'''

with open(os.path.join(base_dir, 'style.css'), 'w', encoding='utf-8') as f:
    f.write(style_css)

script_js = '''
document.addEventListener('DOMContentLoaded', () => {
    const spiralContainer = document.querySelector('.spiral-container');
    const isMobile = window.innerWidth <= 800;
    const ringCount = isMobile ? 15 : 20;
    
    for (let i = 0; i < ringCount; i++) {
        const ring = document.createElement('div');
        ring.classList.add('ring');
        spiralContainer.appendChild(ring);
    }
    
    window.addEventListener('resize', () => {
        const newIsMobile = window.innerWidth <= 800;
        if (newIsMobile !== isMobile) {
            location.reload();
        }
    });
});
'''

with open(os.path.join(base_dir, 'script.js'), 'w', encoding='utf-8') as f:
    f.write(script_js)

print("UI rewrite complete")
