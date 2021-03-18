from PIL import Image

pic_path = 'C:\\Users\\xushu\\Pictures\\cl_20201221.jpg'
img = Image.open(pic_path)
print(img.size)

crop_1 = img.crop((0, 0, 74, 74))
crop_1.save('1.jpg')  # 左上右下
crop_2 = img.crop((75, 0, 150, 74))
crop_2.save('2.jpg')  # 左上右下
crop_3 = img.crop((0, 75, 74, 150))
crop_3.save('3.jpg')  # 左上右下
crop_4 = img.crop((75, 75, 150, 150))
crop_4.save('4.jpg')  # 左上右下
