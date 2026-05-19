from PIL import Image
import numpy as np
import sys

sys.stdout.reconfigure(encoding='utf-8')

report_path = r"c:\Users\asus\OneDrive - Trường Ngôi Sao Hoàng Mai\Desktop\phiếu nhận xét học sinh cuối năm\web_so_lo_xo\assets\reports\report_0.png"
avatar_path = r"c:\Users\asus\OneDrive - Trường Ngôi Sao Hoàng Mai\Desktop\phiếu nhận xét học sinh cuối năm\web_so_lo_xo\assets\students\student_0.jpg"

try:
    report = Image.open(report_path).convert('RGB')
    avatar = Image.open(avatar_path).convert('RGB')
    
    print(f"Report: {report.size}, Avatar: {avatar.size}")
    
    # We expect the avatar to be located somewhere in the top-left area
    # Let's crop the search region: x: 50 to 500, y: 350 to 850
    search_box = (50, 350, 500, 850)
    search_area = report.crop(search_box)
    
    # We will search for a scaled version of the avatar in the search area
    # Let's try scaling the avatar from width 100px to 300px
    search_arr = np.array(search_area, dtype=np.float32)
    
    best_ssd = float('inf')
    best_rect = None # (x, y, w, h) in search area coords
    best_scale = None
    
    # Let's try avatar width from 100 to 250 with step of 5
    for target_w in range(100, 250, 5):
        scale = target_w / avatar.width
        target_h = int(avatar.height * scale)
        
        resized_avatar = avatar.resize((target_w, target_h), Image.Resampling.BILINEAR)
        av_arr = np.array(resized_avatar, dtype=np.float32)
        
        # Calculate SSD (Sum of Squared Differences) on downsampled grayscale for speed
        gray_search = 0.2989 * search_arr[:,:,0] + 0.5870 * search_arr[:,:,1] + 0.1140 * search_arr[:,:,2]
        gray_av = 0.2989 * av_arr[:,:,0] + 0.5870 * av_arr[:,:,1] + 0.1140 * av_arr[:,:,2]
        
        # Slide gray_av over gray_search
        H_s, W_s = gray_search.shape
        H_a, W_a = gray_av.shape
        
        # To make it super fast, let's step by 2 pixels
        for y in range(0, H_s - H_a, 2):
            for x in range(0, W_s - W_a, 2):
                sub = gray_search[y:y+H_a, x:x+W_a]
                # Calculate mean squared error
                diff = sub - gray_av
                mse = np.mean(diff ** 2)
                if mse < best_ssd:
                    best_ssd = mse
                    best_rect = (x, y, W_a, H_a)
                    best_scale = scale
                    
    x_s, y_s, w, h = best_rect
    final_x = search_box[0] + x_s
    final_y = search_box[1] + y_s
    print(f"Best match found:")
    print(f"  MSE: {best_ssd}")
    print(f"  Coordinates in report_0.png: x={final_x}, y={final_y}, width={w}, height={h}")
    
except Exception as e:
    print(f"Error: {e}")
