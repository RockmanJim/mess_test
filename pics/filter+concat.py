from PIL import Image
from PIL import ImageFilter


class Trans(object):
    def __init__(self):
        self.source_path = 'cl.jpg'
        self.new_path = 'cl9.jpg'
        self.image_filter_list = ['BLUR', 'DETAIL', 'EDGE_ENHANCE', 'EDGE_ENHANCE_MORE', 'EMBOSS', 'FIND_EDGES',
                                  'SMOOTH', 'SMOOTH_MORE', 'SHARPEN']
        self.pic: Image.Image = Image.open(self.source_path)
        self.weight, self.height = self.pic.size
        self.target = Image.new(self.pic.mode, (self.weight * 3, self.height * 3))

    def run(self):
        for i in range(3):
            for j in range(3):
                t = self.pic.filter(getattr(ImageFilter, self.image_filter_list[i * 3 + j]))
                self.target.paste(t, (j * self.weight, i * self.height, (j + 1) * self.weight, (i + 1) * self.height))
        self.target.save(self.new_path)


if __name__ == '__main__':
    Trans().run()
    # ImageFilter.BLUR  # 图像的模糊效果
    # ImageFilter.CONTOUR  # 图像的轮廓效果
    # ImageFilter.DETAIL  # 图像的细节效果
    # ImageFilter.EDGE_ENHANCE  # 图像的边界加强效果
    # ImageFilter.EDGE_ENHANCE_MORE  # 图像的阈值边界加强效果
    # ImageFilter.EMBOSS  # 图像的浮雕效果
    # ImageFilter.FIND_EDGES  # 图像的边界效果
    # ImageFilter.SMOOTH  # 图像的平滑效果
    # ImageFilter.SMOOTH_MORE  # 图像的阈值平滑效果
    # ImageFilter.SHARPEN  # 图像的锐化效果
