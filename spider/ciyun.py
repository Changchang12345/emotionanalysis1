#-*- codeing = utf-8 -*-
#@Time :2021/4/23 10:53
#@Author : cty
#@File :ciyun.py.py
#@Software: PyCharm

#添加自定义分词

import jieba
from os import path  #用来获取文档的路径

#词云
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
#词云生成工具
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
#需要对中文进行处理
import matplotlib.font_manager as fm

#背景图



def wordyun():

    f = open("weibo.txt", "r")  # 设置文件对象
    str = f.read()
    # 导入背景图‪C:\\Users\\16123\Desktop\素材被\壁纸\mask.jpg
    backgrim = np.array(Image.open("mask.jpg"))
    # 导入文本文件   text=open("C:\\Users\SAMSUNG\PycharmProjects\practice0829\qqzon\\1154540719worldcloud.txt",encoding='utf-8').read()
    # jieba分词
    wordlist = jieba.cut(str, cut_all=True)
    wl = " ".join(wordlist)
    # 设置参数
    wordcloud = WordCloud(
        background_color='white',  # 背景颜色
        mask=backgrim,  # 背景图片
        max_words=300,  # 设置最多现实的词数
        stopwords=STOPWORDS,  # 设置停用词
        max_font_size=200,  # 设置字体最大值
        font_path='C:/Users/Windows/fonts/STXINGKA.TTF',  # 设置字体，路径在电脑内
        width=1600,
        height=1000,
        random_state=30,  # 设置有多少种随机生成状态，即有多少种配色方案
        # scale=.5
    ).generate(wl)
    # 改变字体颜色
    image_colors = ImageColorGenerator(backgrim)
    # 展示词云
    plt.imshow(wordcloud)
    # 是否显示想x，y坐标
    plt.axis("off")
    plt.show()
    # 写入文件
    wordcloud.to_file('词云.png')  # 把词云保存下

if __name__ == '__main__':
    wordyun()
