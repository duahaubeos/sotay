from PIL import Image
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

workspace_dir = r"c:\Users\asus\OneDrive - Trường Ngôi Sao Hoàng Mai\Desktop\phiếu nhận xét học sinh cuối năm"

for name in ["mẫu.png", "mẫu 2.jpg", "back.png"]:
    p = os.path.join(workspace_dir, name)
    if os.path.exists(p):
        img = Image.open(p)
        print(f"File {name}: Width={img.width}, Height={img.height}, Format={img.format}")
    else:
        print(f"File {name} not found!")
