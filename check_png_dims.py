import os
from PIL import Image
import sys

sys.stdout.reconfigure(encoding='utf-8')

parent_dir = r"c:\Users\asus\OneDrive - Trường Ngôi Sao Hoàng Mai\Desktop\phiếu nhận xét học sinh cuối năm"
parent_pngs = [f for f in os.listdir(parent_dir) if f.lower().endswith('.png') and not f.startswith('tải xuống') and f != 'back.png' and f != 'mẫu.png']

print("Dimensions of parent PNGs:")
for f in parent_pngs[:5]:
    p = os.path.join(parent_dir, f)
    img = Image.open(p)
    print(f"  - {f}: size={img.size}")
