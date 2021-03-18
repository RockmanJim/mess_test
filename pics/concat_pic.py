from PIL import Image

pic_path = 'C:\\Users\\xushu\\Pictures\\cl_20201221.jpg'
img = Image.open(pic_path)
print(img.size)

target = Image.new('RGB', (300, 300))
target.paste(img, (0, 0, 150, 150))  # 左上右下
target.paste(img, (150, 0, 300, 150))
target.paste(img, (0, 150, 150, 300))
target.paste(img, (150, 150, 300, 300))
target.save('cl4.jpg')
