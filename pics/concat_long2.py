from PIL import Image
import numpy as np


pic_base_path = 'C:\\Users\\xushu\\Pictures\\鸭兔的！新艺术诞生记！\\88053791_p%d.jpg'
img_list = [np.array(Image.open(pic_base_path % i)) for i in range(0, 24)]
print(img_list)

# 横向axis=1
# 纵向axis=0

yt1 = np.concatenate(img_list[:15],  axis=0)
Image.fromarray(yt1).save('./yt1.jpg')

yt1 = np.concatenate(img_list[15:],  axis=0)
Image.fromarray(yt1).save('./yt2.jpg')
