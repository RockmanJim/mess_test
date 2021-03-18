from PIL import Image
import numpy as np

im = np.array(Image.open('cl.jpg'))

im_R = im.copy()
im_R[:, :, (1, 2)] = 0
im_G = im.copy()
im_G[:, :, (0, 2)] = 0
im_B = im.copy()
im_B[:, :, (0, 1)] = 0

# 横向的图片拼接
im_RGB = np.concatenate((im_R, im_G, im_B), axis=1)
# im_RGB = np.hstack((im_R, im_G, im_B))
# im_RGB = np.c_['1', im_R, im_G, im_B]

pil_img = Image.fromarray(im_RGB)
pil_img.save('./lena_numpy_split_color.jpg')

y = np.concatenate((im_RGB, im_RGB, im_RGB), axis=0)
Image.fromarray(y).save('./y.jpg')
# ————————————————
# 版权声明：本文为CSDN博主「饺子大人」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/qq_18351157/article/details/103730014