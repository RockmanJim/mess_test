from PIL import Image
import numpy as np

im = np.array(Image.open('cl.jpg'))

im_R = im.copy()
im_R[:, :, (1, 2)] = 0
im_G = im.copy()
im_G[:, :, (0, 2)] = 0
im_B = im.copy()
im_B[:, :, (0, 1)] = 0

# 向的图片拼接
# im_RGB = np.concatenate((im_R, im_G, im_B), axis=1)
# n_b = np.pad(im_B, (0, 150), 'constant')
# y = np.concatenate((im_RGB, n_b), axis=0)
# Image.fromarray(y).save('./a.jpg')

y2 = np.concatenate((im_R, im),  axis=0)
Image.fromarray(y2).save('./y2.jpg')
