from PIL import Image
import os

folder_path = './images' # 네 이미지 폴더 경로
for filename in os.listdir(folder_path):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        img_path = os.path.join(folder_path, filename)
        img = Image.open(img_path)
        
        # 가로 400 기준으로 비율 맞춰서 줄이기
        width = 400
        ratio = (width / float(img.size[0]))
        height = int((float(img.size[1]) * float(ratio)))
        
        resized_img = img.resize((width, height))
        resized_img.save(img_path) # 원본 덮어쓰기