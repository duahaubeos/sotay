import os
import json

base_dir = r"c:\Users\asus\OneDrive - Trường Ngôi Sao Hoàng Mai\Desktop\phiếu nhận xét học sinh cuối năm\web_so_lo_xo"

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

img_dir = os.path.join(base_dir, 'assets', 'students')
student_images = sorted([f"assets/students/{img}" for img in os.listdir(img_dir) if img.endswith(('.jpeg', '.png', '.jpg'))])

cards_html = []
for i, name in enumerate(students):
    img = student_images[i % len(student_images)] if student_images else 'assets/boy.png'
    card = f'''
        <div class="student-card">
            <img src="{img}" alt="Học sinh">
            <h4>{name}</h4>
        </div>'''
    cards_html.append(card)

# Split students into left and right page for mau2_h.jpg
mid = len(cards_html) // 2 + 1
cards_left = '\n'.join(cards_html[:mid])
cards_right = '\n'.join(cards_html[mid:])

index_html = f'''<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kỷ Yếu Lớp 4C</title>
    <link rel="stylesheet" href="style.css">
    <link href="https://fonts.googleapis.com/css2?family=Edu+VIC+WA+NT+Beginner:wght@400..700&display=swap" rel="stylesheet">
</head>
<body>
    <div class="app-container">
        
        <!-- PAGE 1: Giới thiệu -->
        <div id="page1" class="page-view active">
            <div class="content-area-1">
                <h1>Trường Tiểu học Mỹ Thuận 1</h1>
                <div class="teacher-box">
                    <h2>GVCN: Cô Nguyễn Thị Thu Cúc</h2>
                    <p>Kỷ yếu cuối năm học 2023-2024</p>
                </div>
                <button class="flip-btn" onclick="goToPage2()">Mở Sổ ➔</button>
            </div>
        </div>
        
        <!-- PAGE 2: Danh sách học sinh -->
        <div id="page2" class="page-view">
            <!-- Left part of the open notebook -->
            <div class="content-area-2-left">
                <button class="flip-btn-back" onclick="goToPage1()">🡄 Đóng sổ</button>
                <h2 class="class-title">Danh sách lớp 4C (1)</h2>
                <div class="student-grid">
{cards_left}
                </div>
            </div>
            
            <!-- Right part of the open notebook -->
            <div class="content-area-2-right">
                <h2 class="class-title">Danh sách lớp 4C (2)</h2>
                <div class="student-grid">
{cards_right}
                </div>
            </div>
        </div>

    </div>
    <script src="script.js"></script>
</body>
</html>
'''

style_css = '''
:root {
    --font-main: 'Edu VIC WA NT Beginner', cursive;
}

body {
    margin: 0;
    padding: 0;
    background-color: #ff9fb2;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    font-family: var(--font-main);
}

.app-container {
    width: 95%;
    max-width: 900px;
    height: 75vh;
    max-height: 600px;
    position: relative;
    perspective: 2000px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
}

.page-view {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    transition: transform 0.8s cubic-bezier(0.645, 0.045, 0.355, 1);
    transform-style: preserve-3d;
    backface-visibility: hidden;
    background-size: cover;
    background-position: center;
    border-radius: 10px;
}

/* Page 1: mau_h.jpg (Spiral on top) */
#page1 {
    background-image: url('assets/mau_h.jpg');
    transform: rotateX(0deg); /* Flip upwards like a calendar */
    transform-origin: top center;
    z-index: 2;
}

/* Page 2: mau2_h.jpg (Spiral vertical in middle) */
#page2 {
    background-image: url('assets/mau2_h.jpg');
    transform: rotateX(-180deg);
    transform-origin: top center;
    z-index: 1;
}

#page1.hidden {
    transform: rotateX(180deg);
}

#page2.active {
    transform: rotateX(0deg);
    z-index: 2;
}

/* Content Area for Page 1 */
/* Spiral is on top, space is below */
.content-area-1 {
    position: absolute;
    top: 25%;
    bottom: 10%;
    left: 10%;
    right: 10%; 
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
}

/* Content Area for Page 2 */
/* Spiral is in the middle vertical. We have a left page and right page. */
.content-area-2-left {
    position: absolute;
    top: 10%;
    bottom: 10%; 
    left: 7%;
    right: 52%;
    display: flex;
    flex-direction: column;
    align-items: center;
    overflow-y: auto;
    padding-right: 10px;
}

.content-area-2-right {
    position: absolute;
    top: 10%; 
    bottom: 10%;
    left: 52%;
    right: 7%;
    display: flex;
    flex-direction: column;
    align-items: center;
    overflow-y: auto;
    padding-left: 10px;
}

.content-area-2-left::-webkit-scrollbar, .content-area-2-right::-webkit-scrollbar { width: 5px; }
.content-area-2-left::-webkit-scrollbar-thumb, .content-area-2-right::-webkit-scrollbar-thumb { background: rgba(255,107,129,0.5); border-radius: 5px; }

h1 {
    color: #ff4757;
    font-size: 2.5rem;
    margin-bottom: 20px;
    text-shadow: 1px 1px 0 #fff;
}

.teacher-box {
    margin-bottom: 30px;
    background: rgba(255,255,255,0.6);
    padding: 15px 30px;
    border-radius: 10px;
}

h2 {
    font-size: 1.5rem;
    color: #2f3542;
    margin: 0;
}

p {
    font-size: 1.2rem;
    color: #57606f;
}

.flip-btn, .flip-btn-back {
    background: #ff4757;
    color: white;
    border: none;
    padding: 10px 25px;
    border-radius: 20px;
    font-family: var(--font-main);
    font-size: 1.2rem;
    font-weight: bold;
    cursor: pointer;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    transition: transform 0.2s;
}

.flip-btn:hover { transform: scale(1.05); }

.flip-btn-back {
    background: #747d8c;
    padding: 5px 15px;
    font-size: 1rem;
    margin-bottom: 10px;
}

.class-title {
    color: #ff4757;
    font-size: 1.3rem;
    border-bottom: 2px dashed #ff4757;
    padding-bottom: 5px;
    margin-bottom: 15px;
}

.student-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 15px;
    width: 100%;
}

.student-card {
    text-align: center;
    background: rgba(255, 255, 255, 0.7);
    padding: 5px;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.student-card img {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    object-fit: cover;
    border: 2px solid #ff4757;
    margin-bottom: 5px;
}

.student-card h4 {
    margin: 0;
    font-size: 0.9rem;
    color: #2d3436;
}
'''

with open(os.path.join(base_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(index_html)
with open(os.path.join(base_dir, 'style.css'), 'w', encoding='utf-8') as f:
    f.write(style_css)

print("Landscape layout updated")
