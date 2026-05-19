import os
import json

base_dir = r"c:\Users\asus\OneDrive - Trường Ngôi Sao Hoàng Mai\Desktop\phiếu nhận xét học sinh cuối năm\web_so_lo_xo"

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

img_dir = os.path.join(base_dir, 'assets', 'students')
student_images = sorted([f"assets/students/{img}" for img in os.listdir(img_dir) if img.endswith(('.jpeg', '.png', '.jpg'))])

cards_html = []
tapes = ['bg-primary-container', 'bg-secondary-container', 'bg-tertiary-container']
rotations_tape = ['-rotate-3', 'rotate-6', '-rotate-2', 'rotate-4', '-rotate-5', 'rotate-2', '-rotate-4']
rotations_card = ['rotate-2', '-rotate-1', 'rotate-1', '-rotate-3', 'rotate-4', '-rotate-2', 'rotate-3']

for i, name in enumerate(students):
    img = student_images[i % len(student_images)] if student_images else 'assets/boy.png'
    tape_color = tapes[i % len(tapes)]
    r_tape = rotations_tape[i % len(rotations_tape)]
    r_card = rotations_card[i % len(rotations_card)]
    
    card = f'''
            <div class="relative group">
                <div class="absolute -top-4 left-1/2 -translate-x-1/2 z-10 w-16 h-4 {tape_color} opacity-70 washi-tape {r_tape} group-hover:rotate-0 transition-transform"></div>
                <div class="bg-white p-2 pb-4 polaroid-shadow border border-outline-variant {r_card} group-hover:rotate-0 transition-transform">
                    <img alt="Student" class="w-full aspect-square object-cover mb-2" src="{img}"/>
                    <p class="text-center font-headline-md text-sm text-on-surface-variant">{name}</p>
                </div>
            </div>
    '''
    cards_html.append(card)

students_grid = '\n'.join(cards_html)

# The base HTML from the zip
base_html = f'''<!DOCTYPE html>
<html class="light" lang="vi"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Kỷ Yếu Lớp 4C - Trường Tiểu học Mỹ Thuận 1</title>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=Be+Vietnam+Pro:wght@400;600;700&family=Gochi+Hand&display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<script id="tailwind-config">
      tailwind.config = {{
        darkMode: "class",
        theme: {{
          extend: {{
            "colors": {{
                    "on-tertiary-fixed-variant": "#4a4737",
                    "primary-fixed-dim": "#fab3ca",
                    "primary-container": "#ffb7ce",
                    "secondary-fixed": "#cde5ff",
                    "on-tertiary-container": "#595645",
                    "on-surface-variant": "#514347",
                    "on-primary": "#ffffff",
                    "secondary-fixed-dim": "#9bcbf8",
                    "on-error": "#ffffff",
                    "primary": "#864d61",
                    "on-secondary-container": "#265a81",
                    "on-primary-fixed": "#360b1e",
                    "outline": "#837377",
                    "inverse-primary": "#fab3ca",
                    "surface-container": "#e7eefe",
                    "outline-variant": "#d5c2c6",
                    "surface-container-highest": "#dce2f3",
                    "inverse-on-surface": "#ebf1ff",
                    "on-secondary": "#ffffff",
                    "secondary": "#30628a",
                    "secondary-container": "#a1d1fe",
                    "surface": "#f9f9ff",
                    "inverse-surface": "#2a313d",
                    "background": "#f9f9ff",
                    "on-background": "#151c27",
                    "on-tertiary-fixed": "#1e1c0f",
                    "error-container": "#ffdad6",
                    "surface-bright": "#f9f9ff",
                    "error": "#ba1a1a",
                    "surface-dim": "#d3daea",
                    "on-tertiary": "#ffffff",
                    "surface-container-lowest": "#ffffff",
                    "surface-container-low": "#f0f3ff",
                    "on-background": "#151c27",
                    "surface-tint": "#864d61",
                    "on-secondary-fixed": "#001d32",
                    "surface-variant": "#dce2f3",
                    "on-primary-fixed-variant": "#6a364a",
                    "tertiary": "#625e4e",
                    "on-secondary-fixed-variant": "#104a70",
                    "tertiary-fixed": "#e9e2cd",
                    "on-error-container": "#93000a",
                    "primary-fixed": "#ffd9e3",
                    "tertiary-fixed-dim": "#cdc6b2",
                    "on-primary-container": "#7b4458",
                    "surface-container-high": "#e2e8f8",
                    "tertiary-container": "#d1cbb6"
            }},
            "borderRadius": {{
                    "DEFAULT": "0.25rem",
                    "lg": "0.5rem",
                    "xl": "0.75rem",
                    "full": "9999px"
            }},
            "spacing": {{
                    "page-margin": "2rem",
                    "gutter": "1rem",
                    "notebook-padding": "1.5rem",
                    "line-height-grid": "24px"
            }},
            "fontFamily": {{
                    "headline-lg": ["Plus Jakarta Sans"],
                    "headline-md": ["Plus Jakarta Sans"],
                    "body-md": ["Be Vietnam Pro"],
                    "headline-lg-mobile": ["Plus Jakarta Sans"],
                    "label-sm": ["Be Vietnam Pro"],
                    "body-lg": ["Be Vietnam Pro"],
                    "handwritten": ["'Gochi Hand'", "cursive"]
            }},
            "fontSize": {{
                    "headline-lg": ["36px", {{"lineHeight": "1.2", "letterSpacing": "-0.02em", "fontWeight": "700"}}],
                    "headline-md": ["24px", {{"lineHeight": "1.3", "fontWeight": "600"}}],
                    "body-md": ["16px", {{"lineHeight": "1.5", "fontWeight": "400"}}],
                    "headline-lg-mobile": ["28px", {{"lineHeight": "1.2", "fontWeight": "700"}}],
                    "label-sm": ["12px", {{"lineHeight": "1.0", "fontWeight": "600"}}],
                    "body-lg": ["18px", {{"lineHeight": "1.6", "fontWeight": "400"}}]
            }}
          }},
        }},
      }}
    </script>
<style>
        body {{
            background-color: #f0f0f0;
            background-image: radial-gradient(#d1d1d1 1px, transparent 1px);
            background-size: 20px 20px;
            min-height: max(884px, 100dvh);
            overflow-x: hidden;
        }}
        .notebook-container {{
            max-width: 1000px;
            min-height: 100vh;
            background-color: #fffdfa;
            background-image: linear-gradient(#e5e7eb 1px, transparent 1px);
            background-size: 100% 24px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1), 5px 0 0 #f3f4f6, 10px 0 0 #e5e7eb;
            position: relative;
        }}
        .spiral-binding {{
            position: absolute;
            left: -20px;
            top: 20px;
            bottom: 20px;
            width: 40px;
            display: flex;
            flex-direction: column;
            justify-content: space-around;
            z-index: 10;
        }}
        .spiral-ring {{
            width: 30px;
            height: 10px;
            background: linear-gradient(to bottom, #d1d5db, #9ca3af, #d1d5db);
            border-radius: 5px;
            box-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }}
        .washi-tape {{
            mask-image: url('data:image/svg+xml;utf8,<svg viewBox="0 0 100 20" xmlns="http://www.w3.org/2000/svg"><path d="M0 0 L5 2 L10 0 L15 3 L20 1 L25 4 L30 0 L35 2 L40 0 L45 3 L50 1 L55 4 L60 0 L65 2 L70 0 L75 3 L80 1 L85 4 L90 0 L95 2 L100 0 V20 L95 18 L90 20 L85 17 L80 19 L75 16 L70 20 L65 18 L60 20 L55 17 L50 19 L45 16 L40 20 L35 18 L30 20 L25 17 L20 19 L15 16 L10 20 L5 18 L0 20 Z" fill="black"/></svg>');
            -webkit-mask-image: url('data:image/svg+xml;utf8,<svg viewBox="0 0 100 20" xmlns="http://www.w3.org/2000/svg"><path d="M0 0 L5 2 L10 0 L15 3 L20 1 L25 4 L30 0 L35 2 L40 0 L45 3 L50 1 L55 4 L60 0 L65 2 L70 0 L75 3 L80 1 L85 4 L90 0 L95 2 L100 0 V20 L95 18 L90 20 L85 17 L80 19 L75 16 L70 20 L65 18 L60 20 L55 17 L50 19 L45 16 L40 20 L35 18 L30 20 L25 17 L20 19 L15 16 L10 20 L5 18 L0 20 Z" fill="black"/></svg>');
        }}
        .decoration-washi-tape {{
            text-decoration-line: underline;
            text-decoration-style: solid;
            text-decoration-thickness: 8px;
            text-underline-offset: -2px;
            text-decoration-color: rgba(255, 183, 206, 0.5);
        }}
        .polaroid-shadow {{
            box-shadow: 2px 4px 8px rgba(0,0,0,0.1);
        }}
        .washi-tape-pink {{
            background: #ffb7ce;
            mask-image: url("data:image/svg+xml,%3Csvg width='100' height='20' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 0 l5 2 l5 -2 l5 2 l5 -2 l5 2 l5 -2 l5 2 l5 -2 l5 2 l5 -2 l5 2 l5 -2 l5 2 l5 -2 l5 2 l5 -2 l5 2 l5 -2 l5 2 l5 -2 v20 l-5 -2 l-5 2 l-5 -2 l-5 2 l-5 -2 l-5 2 l-5 -2 l-5 2 l-5 -2 l-5 2 l-5 -2 l-5 2 l-5 -2 l-5 2 l-5 -2 l-5 2 l-5 -2 l-5 2 l-5 -2 l-5 2 z' fill='black'/%3E%3C/svg%3E");
            -webkit-mask-image: url("data:image/svg+xml,%3Csvg width='100' height='20' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 0 l5 2 l5 -2 l5 2 l5 -2 l5 2 l5 -2 l5 2 l5 -2 l5 2 l5 -2 l5 2 l5 -2 l5 2 l5 -2 l5 2 l5 -2 l5 2 l5 -2 l5 2 l5 -2 v20 l-5 -2 l-5 2 l-5 -2 l-5 2 l-5 -2 l-5 2 l-5 -2 l-5 2 l-5 -2 l-5 2 l-5 -2 l-5 2 l-5 -2 l-5 2 l-5 -2 l-5 2 l-5 -2 l-5 2 l-5 -2 l-5 2 z' fill='black'/%3E%3C/svg%3E");
            mask-size: cover;
            opacity: 0.8;
        }}
    </style>
  </head>
<body class="font-body-md text-on-surface selection:bg-primary-container">

<!-- Sidebar Navigation Shell -->
<nav class="fixed left-0 top-1/2 -translate-y-1/2 rounded-r-xl border-y border-r border-outline-variant bg-surface-container shadow-md flex flex-col w-16 md:w-32 z-50">
<div class="p-2 text-center border-b border-outline-variant mb-2">
<span class="font-headline-md text-headline-md text-primary">4C</span>
</div>
<a class="bg-secondary-container text-on-secondary-container font-bold translate-x-2 rounded-r-lg py-3 px-4 mb-1 hover:translate-x-1 transition-all duration-200 flex flex-col items-center gap-1" href="#intro">
<span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">auto_stories</span>
<span class="font-label-sm text-label-sm uppercase tracking-wider hidden md:block">Intro</span>
</a>
<a class="bg-tertiary-fixed text-on-tertiary-fixed py-3 px-4 mb-1 rounded-r-md hover:translate-x-1 transition-all duration-200 flex flex-col items-center gap-1" href="#students">
<span class="material-symbols-outlined">group</span>
<span class="font-label-sm text-label-sm uppercase tracking-wider hidden md:block">Members</span>
</a>
</nav>

<!-- Main Notebook Layout -->
<main class="notebook-container mx-auto my-8 px-8 md:px-notebook-padding py-8 relative overflow-hidden ml-16 md:mx-auto">
    <!-- Spiral Binding Mockup -->
    <div class="spiral-binding md:flex hidden">
        <div class="spiral-ring"></div><div class="spiral-ring"></div><div class="spiral-ring"></div>
        <div class="spiral-ring"></div><div class="spiral-ring"></div><div class="spiral-ring"></div>
        <div class="spiral-ring"></div><div class="spiral-ring"></div><div class="spiral-ring"></div>
        <div class="spiral-ring"></div><div class="spiral-ring"></div><div class="spiral-ring"></div>
        <div class="spiral-ring"></div><div class="spiral-ring"></div><div class="spiral-ring"></div>
        <div class="spiral-ring"></div><div class="spiral-ring"></div><div class="spiral-ring"></div>
        <div class="spiral-ring"></div><div class="spiral-ring"></div>
    </div>

    <!-- Top App Bar Content -->
    <header class="flex justify-between items-center max-w-notebook mx-auto mb-12 px-4" id="intro">
        <div class="flex items-center gap-3">
            <span class="material-symbols-outlined text-primary text-4xl">menu_book</span>
            <h1 class="font-headline-lg-mobile md:font-headline-lg text-primary drop-shadow-sm">Year 4C Keepsake</h1>
        </div>
        <div class="hidden md:flex gap-6">
            <span class="text-on-primary-fixed-variant font-bold underline decoration-washi-tape cursor-pointer">Sổ liên lạc</span>
            <span class="text-on-surface-variant hover:scale-105 transition-transform cursor-pointer">Hoạt động</span>
            <span class="text-on-surface-variant hover:scale-105 transition-transform cursor-pointer">Kỷ niệm</span>
        </div>
    </header>

    <!-- Hero Section: Welcome -->
    <section class="relative mb-16">
        <div class="absolute -top-4 -left-4 washi-tape-pink w-32 h-8 -rotate-12 z-20"></div>
        <div class="relative bg-white p-4 shadow-md rotate-1 inline-block border border-outline-variant max-w-sm">
            <img alt="School" class="w-full h-auto" src="assets/mau2.jpg"/>
        </div>
        <h2 class="font-handwritten text-5xl text-primary mt-8 mb-4">Chào mừng đến với Tiểu học Mỹ Thuận 1!</h2>
        <p class="font-body-lg text-body-lg text-on-surface-variant max-w-2xl">Nơi ươm mầm những tài năng nhí, nơi mỗi ngày đến trường là một niềm vui và mỗi kỷ niệm đều được nâng niu như những trang sổ tay quý giá.</p>
    </section>

    <!-- Teacher Section -->
    <section class="mb-16 relative">
        <div class="absolute -top-6 left-1/2 -translate-x-1/2 z-20 w-32 h-8 bg-primary-container opacity-60 washi-tape rotate-1"></div>
        <div class="bg-surface-container-lowest p-8 rounded-xl polaroid-shadow border border-outline-variant max-w-2xl mx-auto flex flex-col md:flex-row items-center gap-8 -rotate-1">
            <div class="relative">
                <div class="w-48 h-48 rounded-lg overflow-hidden border-8 border-white shadow-inner">
                    <img alt="Cô giáo" class="w-full h-full object-cover" src="assets/teacher.png"/>
                </div>
                <div class="absolute -top-4 -right-4 w-12 h-12 bg-secondary-container rounded-full flex items-center justify-center shadow-md rotate-12">
                    <span class="material-symbols-outlined text-on-secondary-container" style="font-variation-settings: 'FILL' 1;">star</span>
                </div>
            </div>
            <div class="text-center md:text-left flex-1">
                <h2 class="font-headline-md text-headline-md text-primary mb-2">Cô Nguyễn Thị Thu Cúc</h2>
                <p class="text-on-surface-variant font-body-lg mb-4 italic">"Mỗi học sinh là một bông hoa rực rỡ, và cô rất vinh dự khi được là người chăm sóc khu vườn 4C này."</p>
                <div class="flex flex-wrap justify-center md:justify-start gap-3">
                    <span class="px-3 py-1 bg-tertiary-container text-on-tertiary-container rounded-full text-label-sm font-label-sm uppercase tracking-wider">Chủ nhiệm lớp 4C</span>
                    <span class="px-3 py-1 bg-secondary-container text-on-secondary-container rounded-full text-label-sm font-label-sm uppercase tracking-wider">Niên khóa 2023-2024</span>
                </div>
            </div>
        </div>
    </section>

    <!-- Students Grid Section -->
    <section class="px-4" id="students">
        <div class="flex items-center gap-4 mb-10">
            <div class="h-px flex-1 bg-outline-variant"></div>
            <h3 class="font-headline-md text-primary flex items-center gap-2">
                <span class="material-symbols-outlined">group</span>
                Thành viên lớp 4C
            </h3>
            <div class="h-px flex-1 bg-outline-variant"></div>
        </div>
        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-y-12 gap-x-8">
            {students_grid}
        </div>
    </section>

    <!-- Page Footer Decor -->
    <footer class="mt-20 pt-10 border-t-2 border-dashed border-outline-variant flex flex-col items-center gap-4 text-on-surface-variant">
        <div class="flex gap-4">
            <span class="material-symbols-outlined text-primary">edit</span>
            <span class="material-symbols-outlined text-secondary">brush</span>
            <span class="material-symbols-outlined text-tertiary">palette</span>
        </div>
        <p class="font-label-sm uppercase tracking-widest opacity-60">Sổ lưu bút lớp 4C - Niên khóa 2023-2024</p>
        <div class="flex gap-2 pb-10">
            <div class="w-4 h-4 rounded-full bg-primary-fixed"></div>
            <div class="w-4 h-4 rounded-full bg-secondary-fixed"></div>
            <div class="w-4 h-4 rounded-full bg-tertiary-fixed"></div>
        </div>
    </footer>
</main>

</body></html>
'''

with open(os.path.join(base_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(base_html)

print("Zip UI applied")
