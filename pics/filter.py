from PIL import Image
from PIL import ImageFilter
pic_path = 'C:\\Users\\xushu\\Pictures\\cl_20201221.jpg'
pic = Image.open(pic_path)
contour_cl = pic.filter(ImageFilter.CONTOUR)  # 轮廓效果
contour_cl.save("contour_cl.jpg")
