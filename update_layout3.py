import os
import shutil
import json

base_dir = r"c:\Users\asus\OneDrive - Trường Ngôi Sao Hoàng Mai\Desktop\phiếu nhận xét học sinh cuối năm\web_so_lo_xo"
# copy images
shutil.copy2(r"c:\Users\asus\OneDrive - Trường Ngôi Sao Hoàng Mai\Desktop\phiếu nhận xét học sinh cuối năm\mẫu.png", os.path.join(base_dir, 'assets', 'mau.png'))
shutil.copy2(r"c:\Users\asus\OneDrive - Trường Ngôi Sao Hoàng Mai\Desktop\phiếu nhận xét học sinh cuối năm\mẫu 2.jpg", os.path.join(base_dir, 'assets', 'mau2.jpg'))

# Load students
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

# get images
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

cards_str = '\n'.join(cards_html)

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
            <!-- Top part of the open notebook -->
            <div class="content-area-2-top">
                <button class="flip-btn-back" onclick="goToPage1()">🡄 Quay lại</button>
                <h2 class="class-title">Danh sách lớp 4C</h2>
            </div>
            
            <!-- Bottom part of the open notebook -->
            <div class="content-area-2-bottom">
                <div class="student-grid">
{cards_str}
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
    width: 100%;
    max-width: 500px;
    height: 100vh;
    max-height: 900px;
    position: relative;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
}

.page-view {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.6s;
    background-size: cover;
    background-position: center;
}

/* Page 1: mau.png */
#page1 {
    background-image: url('assets/mau.png');
    transform: translateX(0);
    opacity: 1;
    z-index: 2;
}

/* Page 2: mau2.jpg */
#page2 {
    background-image: url('assets/mau2.jpg');
    transform: translateX(100%);
    opacity: 0;
    z-index: 1;
}

#page1.hidden {
    transform: translateX(-100%);
    opacity: 0;
}

#page2.active {
    transform: translateX(0);
    opacity: 1;
}

/* Content Area for Page 1 */
.content-area-1 {
    position: absolute;
    top: 25%;
    bottom: 25%;
    left: 12%;
    right: 20%; 
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
}

/* Content Area for Page 2 */
.content-area-2-top {
    position: absolute;
    top: 15%;
    bottom: 53%; 
    left: 10%;
    right: 10%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.content-area-2-bottom {
    position: absolute;
    top: 53%; 
    bottom: 15%;
    left: 10%;
    right: 10%;
    overflow-y: auto;
    padding-top: 10px;
}

.content-area-2-bottom::-webkit-scrollbar { width: 5px; }
.content-area-2-bottom::-webkit-scrollbar-thumb { background: rgba(255,107,129,0.5); border-radius: 5px; }

h1 {
    color: #ff4757;
    font-size: 2rem;
    margin-bottom: 20px;
    text-shadow: 1px 1px 0 #fff;
}

.teacher-box {
    margin-bottom: 30px;
    background: rgba(255,255,255,0.6);
    padding: 10px;
    border-radius: 10px;
}

h2 {
    font-size: 1.4rem;
    color: #2f3542;
    margin: 0;
}

p {
    font-size: 1.1rem;
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
    font-size: 1.8rem;
    border-bottom: 2px dashed #ff4757;
    padding-bottom: 5px;
}

.student-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
    padding-bottom: 20px;
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
    font-size: 0.8rem;
    color: #2d3436;
}
'''

script_js = '''
function goToPage2() {
    document.getElementById('page1').classList.add('hidden');
    document.getElementById('page1').classList.remove('active');
    
    document.getElementById('page2').classList.add('active');
}

function goToPage1() {
    document.getElementById('page2').classList.remove('active');
    
    document.getElementById('page1').classList.add('active');
    document.getElementById('page1').classList.remove('hidden');
}
'''

with open(os.path.join(base_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(index_html)
with open(os.path.join(base_dir, 'style.css'), 'w', encoding='utf-8') as f:
    f.write(style_css)
with open(os.path.join(base_dir, 'script.js'), 'w', encoding='utf-8') as f:
    f.write(script_js)

print("Update to Layout 3 (Page Flip) complete")
