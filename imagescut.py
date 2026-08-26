from PIL import Image
import os

folder_path = './images'
for filename in os.listdir(folder_path):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        img_path = os.path.join(folder_path, filename)
        img = Image.open(img_path)
        
        # 가로 500 픽셀로 설정 (적당한 크기와 화질 타협점)
        width = 500
        ratio = (width / float(img.size[0]))
        height = int((float(img.size[1]) * float(ratio)))
        
        # LANCZOS 필터 적용해서 초고화질로 리사이징!
        resized_img = img.resize((width, height), Image.Resampling.LANCZOS)
        
        # PNG 퀄리티 손실 없이 덮어쓰기
        resized_img.save(img_path, quality=95)