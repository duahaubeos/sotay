from PIL import Image
import os

base_dir = r"c:\Users\asus\OneDrive - Trường Ngôi Sao Hoàng Mai\Desktop\phiếu nhận xét học sinh cuối năm\web_so_lo_xo\assets"

img1 = Image.open(os.path.join(base_dir, 'mau.png'))
img1_h = img1.rotate(-90, expand=True) 
img1_h = img1_h.convert("RGB")
img1_h.save(os.path.join(base_dir, 'mau_h.jpg'))

img2 = Image.open(os.path.join(base_dir, 'mau2.jpg'))
img2_h = img2.rotate(-90, expand=True)
img2_h = img2_h.convert("RGB")
img2_h.save(os.path.join(base_dir, 'mau2_h.jpg'))

print("Images rotated")
