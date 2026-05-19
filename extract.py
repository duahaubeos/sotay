import zipfile
import pandas as pd
import json
import os

base_path = r'c:\Users\asus\OneDrive - Trường Ngôi Sao Hoàng Mai\Desktop\phiếu nhận xét học sinh cuối năm'
xlsx_path = os.path.join(base_path, '4C.xlsx')
pptx_path = os.path.join(base_path, 'Pink and White Playful  Illustrative Back to School Poster (A4).pptx')
dest_dir = os.path.join(base_path, 'web_so_lo_xo')

# Read excel
try:
    df = pd.read_excel(xlsx_path)
    data = df.to_dict(orient='records')
    with open(os.path.join(dest_dir, 'names.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
except Exception as e:
    print(f"Error reading excel: {e}")

# Extract media from pptx
pptx_media_dir = os.path.join(dest_dir, 'pptx_media')
os.makedirs(pptx_media_dir, exist_ok=True)
try:
    with zipfile.ZipFile(pptx_path, 'r') as z:
        for file_info in z.infolist():
            if file_info.filename.startswith('ppt/media/'):
                z.extract(file_info, pptx_media_dir)
except Exception as e:
    print(f"Error extracting pptx: {e}")

# Extract media from xlsx
xlsx_media_dir = os.path.join(dest_dir, 'xlsx_media')
os.makedirs(xlsx_media_dir, exist_ok=True)
try:
    with zipfile.ZipFile(xlsx_path, 'r') as z:
        for file_info in z.infolist():
            if file_info.filename.startswith('xl/media/'):
                z.extract(file_info, xlsx_media_dir)
except Exception as e:
    print(f"Error extracting xlsx: {e}")

print("Extraction complete")
