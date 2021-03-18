import requests
from PIL import Image
import io
import numpy as np


class Serial(object):
    pic: Image.Image = None
    pic_list = []

    def __init__(self):
        self.base_url = 'https://media.st.dl.pinyuncloud.com/steam/apps/1033450/ss_%s.600x338.jpg'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
        self.addr_list = ['131fd8ee1ef30ad2f1e5f2c7f1cfea3e9429307d',
                         '108458739ddda898456c1a48a3b346854e392e45',
                         'b57b65b533487c2259649c59ea4be44ad35bc8cd',
                         'a03ff4bd0439bdc5d5f0bbb5907b4f22fd09797e',
                         '080ab52c3e008211ce33724fb8a2de6c6987f70a',
                         '2247a9a3310de3db442bd5e37614d3fe185ffe01']
        self.param = {'t': '1559288448'}

    def get_pic(self):
        for i in self.addr_list:
            print(i)
            response = requests.get(url=self.base_url % i, headers=self.headers, params=self.param)
            self.pic_list.append(Image.open(io.BytesIO(response.content)))

    def concat_pic(self):
        pic: np.array = None
        for j in self.pic_list:
            if pic is None:
                pic = np.array(j)
            else:
                pic = np.concatenate((pic, np.array(j)), axis=0)
        Image.fromarray(pic).save('./steam.jpg')

    def run(self):
        self.get_pic()
        self.concat_pic()


if __name__ == '__main__':
    Serial().run()
