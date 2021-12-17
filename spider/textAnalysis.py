#-*- coding: utf-8 -*-
#@Time :2021/2/19 12:18
#@Author : cty
#@File :textAnalysis.py
#@Software: PyCharm
import math
import re

import jieba
import xlrd
from datetime import date,datetime
import xdrlib,sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import xlwt
import jieba.posseg as psg
from snownlp import SnowNLP, normal
from snownlp import sentiment
from snownlp.seg import seg
savepath = ".\\weibo.txt"

def barchartemo(em0,em1,em2):
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
    plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号
    ans = em0+em1+em2
    x = np.array(['消极情感','中性情感','积极情感'])  # x值取默认值
    y = np.array([em0 / ans, em1 / ans, em2 / ans])
    # print(a2,ans,a2/ans)
    sortIndex = np.argsort(-y)  # 倒序，返回排序后各数据的原始下标
    x_sort = x[sortIndex]  # 重新进行排序，与y保持初始顺序一致
    y_sort = y[sortIndex]  # 重新进行排序，倒序

    # 定义函数来显示柱状上的数值

    plt.xticks(np.arange(len(x_sort)), x_sort)
    a = plt.bar(np.arange(len(x_sort)), y_sort, color=['r', 'g', 'b', 'c'], alpha=0.8)
    # autolabel(a)

    plt.title('情感分布')
    plt.ylabel('人数占比(%)', fontsize=12)
    plt.xlabel('情感倾向', fontsize=12)
    plt.savefig('./情感柱状图.png')
    plt.show()

def piechartage0(a1,a2,a3,a4):

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
    plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号
    ans=a1+a2+a3+a4
    x = np.array(['小于20','20-40','40-60','大于60'])  # x值取默认值
    y = np.array([a1/ans,a2/ans,a3/ans,a4/ans])
    #print(a2,ans,a2/ans)
    sortIndex = np.argsort(-y)  # 倒序，返回排序后各数据的原始下标
    x_sort = x[sortIndex]  # 重新进行排序，与y保持初始顺序一致
    y_sort = y[sortIndex]  # 重新进行排序，倒序

    # 定义函数来显示柱状上的数值

    plt.xticks(np.arange(len(x_sort)), x_sort)
    a = plt.bar(np.arange(len(x_sort)), y_sort, color=['r', 'g', 'b', 'c'],alpha=0.8)
    #autolabel(a)
    plt.title('消极年龄柱状图')
    plt.ylabel('人数占比(%)', fontsize=12)
    plt.xlabel('年龄段', fontsize=12)
    plt.savefig('./消极年龄柱状图.png')
    plt.show()

def piechartage1(a1,a2,a3,a4):

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
    plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号
    ans=a1+a2+a3+a4
    x = np.array(['小于20','20-40','40-60','大于60'])  # x值取默认值
    y = np.array([a1/ans,a2/ans,a3/ans,a4/ans])
    #print(a2,ans,a2/ans)
    sortIndex = np.argsort(-y)  # 倒序，返回排序后各数据的原始下标
    x_sort = x[sortIndex]  # 重新进行排序，与y保持初始顺序一致
    y_sort = y[sortIndex]  # 重新进行排序，倒序

    # 定义函数来显示柱状上的数值

    plt.xticks(np.arange(len(x_sort)), x_sort)
    a = plt.bar(np.arange(len(x_sort)), y_sort, color=['r', 'g', 'b', 'c'],alpha=0.8)
    #autolabel(a)

    plt.title('中性年龄柱状图')
    plt.ylabel('人数占比(%)', fontsize=12)
    plt.xlabel('年龄段', fontsize=12)
    plt.savefig('./中性年龄柱状图.png')
    plt.show()

def piechartage2(a1,a2,a3,a4):

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
    plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号
    ans=a1+a2+a3+a4
    x = np.array(['小于20','20-40','40-60','大于60'])  # x值取默认值
    y = np.array([a1/ans,a2/ans,a3/ans,a4/ans])
    #print(a2,ans,a2/ans)
    sortIndex = np.argsort(-y)  # 倒序，返回排序后各数据的原始下标
    x_sort = x[sortIndex]  # 重新进行排序，与y保持初始顺序一致
    y_sort = y[sortIndex]  # 重新进行排序，倒序

    # 定义函数来显示柱状上的数值

    plt.xticks(np.arange(len(x_sort)), x_sort)
    a = plt.bar(np.arange(len(x_sort)), y_sort, color=['r', 'g', 'b', 'c'],alpha=0.8)
    #autolabel(a)

    plt.title('积极年龄柱状图')
    plt.ylabel('人数占比(%)', fontsize=12)
    plt.xlabel('年龄段', fontsize=12)
    plt.savefig('./积极年龄柱状图.png')
    plt.show()

def piechartxz0(xz):
    labels = list(xz.keys())
    fraces = list(xz.values())

    matplotlib.rcParams['font.sans-serif'] = ['SimHei']

    plt.pie(fraces, labels=labels, autopct='%2.2f%%', shadow=True)
    # 设置x,y的刻度一样，使其饼图为正圆
    plt.axis('equal')
    plt.title('消极星座饼图')
    plt.savefig('./消极星座饼图.png')
    plt.show()

def piechartxz1(xz):
    labels = list(xz.keys())
    fraces = list(xz.values())

    matplotlib.rcParams['font.sans-serif'] = ['SimHei']

    plt.pie(fraces, labels=labels, autopct='%2.2f%%', shadow=True)
    # 设置x,y的刻度一样，使其饼图为正圆
    plt.axis('equal')
    plt.title('中性星座饼图')
    plt.savefig('./中性星座饼图.png')
    plt.show()

def piechartxz2(xz):
    labels = list(xz.keys())
    fraces = list(xz.values())

    matplotlib.rcParams['font.sans-serif'] = ['SimHei']

    plt.pie(fraces, labels=labels, autopct='%2.2f%%', shadow=True)
    # 设置x,y的刻度一样，使其饼图为正圆
    plt.axis('equal')
    plt.title('积极星座饼图')
    plt.savefig('./积极星座饼图.png')
    plt.show()

def piechartad0(ad):
    ad.pop('')
    labels = list(ad.keys())
    fraces = list(ad.values())

    matplotlib.rcParams['font.sans-serif'] = ['SimHei']

    plt.pie(fraces, labels=labels, autopct='%2.2f%%', shadow=True)
    # 设置x,y的刻度一样，使其饼图为正圆
    plt.axis('equal')
    plt.title('消极所在地饼图')
    plt.savefig('./消极所在地饼图.png')
    plt.show()

def piechartad1(ad):
    ad.pop('')
    labels = list(ad.keys())
    fraces = list(ad.values())

    matplotlib.rcParams['font.sans-serif'] = ['SimHei']

    plt.pie(fraces, labels=labels, autopct='%2.2f%%', shadow=True)
    # 设置x,y的刻度一样，使其饼图为正圆
    plt.axis('equal')
    plt.title('中性所在地饼图')
    plt.savefig('./中性所在地饼图.png')
    plt.show()

def piechartad2(ad):
    ad.pop('')
    labels = list(ad.keys())
    fraces = list(ad.values())

    matplotlib.rcParams['font.sans-serif'] = ['SimHei']

    plt.pie(fraces, labels=labels, autopct='%2.2f%%', shadow=True)
    # 设置x,y的刻度一样，使其饼图为正圆
    plt.axis('equal')
    plt.title('积极所在地饼图')
    plt.savefig('./积极所在地饼图.png')
    plt.show()

def piechartsex0(sexnv,sexnan):
    labels = ['female', 'male']
    fraces = [sexnv,sexnan]
    plt.pie(fraces,labels=labels,autopct='%3.2f%%',shadow=True)
    # 设置x,y的刻度一样，使其饼图为正圆
    plt.axis('equal')
    plt.title('消极性别饼图')
    plt.savefig('./消极性别饼图.png')
    plt.show()

def piechartsex1(sexnv,sexnan):
    labels = ['female', 'male']
    fraces = [sexnv,sexnan]
    plt.pie(fraces,labels=labels,autopct='%3.2f%%',shadow=True)
    # 设置x,y的刻度一样，使其饼图为正圆
    plt.axis('equal')
    plt.title('中性性别饼图')
    plt.savefig('./中性性别饼图.png')
    plt.show()

def piechartsex2(sexnv,sexnan):
    labels = ['female', 'male']
    fraces = [sexnv,sexnan]
    plt.pie(fraces,labels=labels,autopct='%3.2f%%',shadow=True)
    # 设置x,y的刻度一样，使其饼图为正圆
    plt.axis('equal')
    plt.title('积极性别饼图')
    plt.savefig('./积极性别饼图.png')
    plt.show()

def stopwordslist():

    stopwords = [line.strip() for line in open('chineseStopTxt.txt', encoding='UTF-8').readlines()]
    return stopwords

#定义TF-IDF的计算过程
def D_con(word, count_list):  #计算 所有文档中 这个word的词频
    D_con = 0
    for count in count_list:
        if word in count:
            D_con += 1
    return D_con
def tf(word,doc):#单个词此文档的频率
    wCount = 0
    tCount = 0
    for item in doc:
        if word == item:
            wCount +=1
    tCount +=1
    return wCount/tCount

def idf(word, count_list): #计算逆文档频率
    return math.log(len(count_list)) / (1 + D_con(word, count_list))

def tfidf(word, count, count_list):
    return tf(word, count) * idf(word, count_list)

def countTf():
    count_list = dataWash()
    ci_list = ['b','ns','nt','nr','m','nz','d','p','nrt','t','n']
    for i in range(len(count_list)):
        print('For document {}'.format(i + 1))
        tf_idf = {}
        for word in count_list[i]:
            if ciXing(word).split('/')[1] not in ci_list:
                #print(ciXing(word))
                tf_idf[word] = tfidf(word, count_list[i], count_list)#计算出tfidf值了

        sort = sorted(tf_idf.items(), key=lambda x: x[1], reverse=True)  # 将集合按照TF-IDF值从大到小排列
        score = 0
        for word, tf_idf in sort[:10]:
            #print("\tWord: {} : {}".format(word, round(tf_idf, 6)))
            score += test(word)
    return score/10


def test(data):
    s1 = SnowNLP(data)
    #print(data, s1.sentiments)  # 这部电影真心棒，全程无尿点 0.9842572323704297
    return s1.sentiments

def dataWash():

    data =xlrd.open_workbook(r"C:\Users\16123\PycharmProjects\first\test\微博疫情.xls")

    file = xlwt.Workbook()
    table_w = file.add_sheet('fc',cell_overwrite_ok=True)
    table = data.sheet_by_index(0)
    nrows = table.nrows
    count_list = []
    for i in range(1,nrows):
        seg_list = jieba.cut(str(table.row(i)[1].value))
        # 创建一个停用词列表
        stopwords = stopwordslist()
        # 输出结果为outstr
        outstr = []
        # 去停用词
        for word in seg_list:
            if word not in stopwords:
                if word != '\t':
                    outstr.append(word)
        count_list.append(outstr)

    #print(count_list)
    return count_list

def ciXing(word):
    posseg = re.sub(r'[ ]', "", word)
    value = psg.cut(posseg)
    value = ' '.join('%s' % (tag) for (tag) in value)
    return value
def save():

    data =xlrd.open_workbook(r"C:\Users\16123\PycharmProjects\first\test\微博疫情.xls")
    sexnv0 = 0
    sexnv1 =0
    sexnv2 = 0
    sexnan0 = 0
    sexnan1 =0
    sexnan2 = 0
    address0= {}
    address0.update({'':89})
    address1= {}
    address1.update({'':89})
    address2= {}
    address2.update({'':89})
    xingzuo0={}
    xingzuo1 = {}
    xingzuo2 = {}
    emo0=0
    emo1=0
    emo2=0
    a10=0
    a20=0
    a30=0
    a40=0
    a11=0
    a21=0
    a31=0
    a41=0
    a12=0
    a22=0
    a32=0
    a42=0
    file = xlwt.Workbook()
    table_w = file.add_sheet('fc',cell_overwrite_ok=True)

    table = data.sheet_by_index(0)
    nrows = table.nrows

    count_list = dataWash()
    #print(nrows, len(count_list))
    ci_list = ['b', 'ns', 'nt', 'nr', 'm', 'nz', 'd', 'p', 'nrt', 't', 'n']
    p=0
    for i in range(1,nrows):
        print('For document {}'.format(i + 1))
        tf_idf = {}
        for word in count_list[i-1]:
            if ciXing(word).split('/')[1] not in ci_list:
                #print(ciXing(word))
                tf_idf[word] = tfidf(word, count_list[i-1], count_list)#计算出tfidf值了

        sort = sorted(tf_idf.items(), key=lambda x: x[1], reverse=True)  # 将集合按照TF-IDF值从大到小排列
        score = 0
        for word, tf_idf in sort[:10]:
            #print("\tWord: {} : {}".format(word, round(tf_idf, 6)))
            with open(savepath, "a") as f:
                f.write(word)
            score += test(word)

            table_w.write(i, 0, table.row_values(i)[0])
            table_w.write(i, 1, table.row_values(i)[1])
            table_w.write(i, 2, table.row_values(i)[2])
            table_w.write(i, 3, table.row_values(i)[3])
            table_w.write(i, 4, table.row_values(i)[4])
            table_w.write(i, 5, table.row_values(i)[5])
            table_w.write(i, 6, score/10)
            if(score/10<0.45):
                emo0 += 1
                if (table.row_values(i)[3]) == '女':
                    sexnv0 +=1
                if (table.row_values(i)[3]) == '男':
                    sexnan0 +=1
                if (table.row_values(i)[2] not in address0.keys()):
                    address0.update({table.row_values(i)[2]: 1})
                else:
                    address0[table.row_values(i)[2]] += 1
                if (table.row_values(i)[5] not in xingzuo0.keys()):
                    xingzuo0.update({table.row_values(i)[5]: 1})
                else:
                    xingzuo0[table.row_values(i)[5]] += 1
                # table.row_values(i)[4].replace(" ","");
                if (table.row_values(i)[4] != ''):
                    if (float(table.row_values(i)[4]) <= 20.0):
                        a10 += 1
                    if (float(table.row_values(i)[4]) > 20.0 and float(table.row_values(i)[4]) <= 40):
                        a20 += 1
                    if (float(table.row_values(i)[4]) > 40 and float(table.row_values(i)[4]) <= 60):
                        a30 += 1
                    if (float(table.row_values(i)[4]) > 60):
                        a40 += 1
            if(score/10<=0.6 and score/10 >=0.45):
                emo1+=1
                if (table.row_values(i)[3]) == '女':
                    sexnv1 +=1
                if (table.row_values(i)[3]) == '男':
                    sexnan1 +=1
                if (table.row_values(i)[2] not in address1.keys()):
                    address1.update({table.row_values(i)[2]: 1})
                else:
                    address1[table.row_values(i)[2]] += 1
                if (table.row_values(i)[5] not in xingzuo1.keys()):
                    xingzuo1.update({table.row_values(i)[5]: 1})
                else:
                    xingzuo1[table.row_values(i)[5]] += 1
                # table.row_values(i)[4].replace(" ","");
                if (table.row_values(i)[4] != ''):
                    if (float(table.row_values(i)[4]) <= 20.0):
                        a11 += 1
                    if (float(table.row_values(i)[4]) > 20.0 and float(table.row_values(i)[4]) <= 40):
                        a21 += 1
                    if (float(table.row_values(i)[4]) > 40 and float(table.row_values(i)[4]) <= 60):
                        a31 += 1
                    if (float(table.row_values(i)[4]) > 60):
                        a41 += 1

            if(score/10>0.6 ):
                emo2+=1
                if (table.row_values(i)[3]) == '女':
                    sexnv2 +=1
                if (table.row_values(i)[3]) == '男':
                    sexnan2 +=1
                if (table.row_values(i)[2] not in address2.keys()):
                    address2.update({table.row_values(i)[2]: 1})
                else:
                    address2[table.row_values(i)[2]] += 1
                if (table.row_values(i)[5] not in xingzuo2.keys()):
                    xingzuo2.update({table.row_values(i)[5]: 1})
                else:
                    xingzuo2[table.row_values(i)[5]] += 1
                # table.row_values(i)[4].replace(" ","");
                if (table.row_values(i)[4] != ''):
                    if (float(table.row_values(i)[4]) <= 20.0):
                        a12 += 1
                    if (float(table.row_values(i)[4]) > 20.0 and float(table.row_values(i)[4]) <= 40):
                        a22 += 1
                    if (float(table.row_values(i)[4]) > 40 and float(table.row_values(i)[4]) <= 60):
                        a32 += 1
                    if (float(table.row_values(i)[4]) > 60):
                        a42 += 1
    barchartemo(emo0,emo1,emo2)
    piechartage0(a10,a20,a30,a40)
    piechartage1(a11,a21,a31,a41)
    piechartage2(a12, a22, a32, a42)
    piechartxz0(xingzuo0)
    piechartxz1(xingzuo1)
    piechartxz2(xingzuo2)
    piechartad0(address0)
    piechartad1(address1)
    piechartad2(address2)
    piechartsex0(sexnv0,sexnan0)
    piechartsex1(sexnv1,sexnan1)
    piechartsex2(sexnv2,sexnan2)
    table_w.write(0, 0, "用户名")
    table_w.write(0, 1, "微博内容原词")
    table_w.write(0, 2, "所在地")
    table_w.write(0, 3, "性别")
    table_w.write(0, 4, "年龄")
    table_w.write(0, 5, "星座")
    table_w.write(0, 6,"情感倾向")


    file.save(r"C:\Users\16123\PycharmProjects\first\test\微博疫情分词.xls")

if __name__ == '__main__':
    save()
