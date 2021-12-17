# -*- codeing = utf-8 -*-
# @Time :2021/1/14 10:35
# @Author : cty
# @File :demo.py
# @Software: PyCharm
# 这是我的第一个python程序
import json
import re
import urllib.request
from turtle import pd

import bs4
import pandas
import xlwt
from pip._vendor import requests
import time

import random

def main(topic):
    baseurl = "https://s.weibo.com/weibo?q="+urllib.parse.quote(topic)+"&Refer=SWeibo_box?page="
    dataResult = getData(baseurl)
    savepath = ".\\微博疫情.xls"
    # 保存数据
    saveData(dataResult, savepath)
    #askUrl(baseurl)

cookie_str = "login_sid_t=7cc7fb52f3b85b443d200494cb240462; cross_origin_proto=SSL; _s_tentry=passport.weibo.com; Apache=4974278680632.5.1617504807851; SINAGLOBAL=4974278680632.5.1617504807851; ULV=1617504807856:1:1:1:4974278680632.5.1617504807851:; wb_view_log_7527183843=1280*7201.5; WBtopGlobal_register_version=2021040610; UOR=,,login.sina.com.cn; wb_view_log=1280*7201.5; SUB=_2AkMXN1WidcPxrARUmv8UxGjqaI5H-jyk4jxUAn7uJhMyAxh87m41qSVutBF-XDvClx0uYD_SFUW_BozTmEvb-3z2; SUBP=0033WrSXqPxfM72wWs9jqgMF55529P9D9WW72mA7MbUWrzT31qGacsn8; WBStorage=202104061150|undefined; webim_unReadCount=%7B%22time%22%3A1617681301925%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D"
findInfoUrl=re.compile(r'<a href="(.*?)".*?><img src=".*?"/></a>', re.S)
findPreUid=re.compile(r'//weibo.com/(.*?)\?.*?')

findUserPersonalInfo=re.compile(r'.*?基本信息(.*?)简介', re.S)
#name
findLink = re.compile(r'<a class="name" href="(.*?)">.*</a>', re.S)
# content
findContent = re.compile(r'<p class="txt" nick-name=".*" node-type="feed_list_content">(.*?)</p>', re.S)
findAddress = re.compile(r'.*?所在地(.*?)性别.*?')
findSex = re.compile(r'.*?性别(.*?)12.*?')
findAge = re.compile(r'.*?生日(.*?)年.*?')
findZuo = re.compile(r'.*?生日(.*?)座.*?')
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
}
cookie = {
    "cookie":cookie_str
}
def get_cookie(cookie_str):
    cookies = {}
    lines = cookie_str.split(';')
    for line in lines:
        key, value = line.strip().split('=', 1)
        cookies[key] = value
    return cookies

def word_messy(word):
    """词语提炼"""
    res = re.sub(u"([^\u4e00-\u9fa5])", "", word)

    return res

def random_sleep(mu=1, sigma=0.4):
    '''正态分布随机睡眠
    :param mu: 平均值
    :param sigma: 标准差，决定波动范围
    '''
    secs = random.normalvariate(mu, sigma)
    if secs <= 0:
        secs = mu # 太小则重置为平均值
        time.sleep(secs)


def getData(baseurl):

    datalist = [] #保存所有信息
    for i in range(3,10):
        random_sleep()
        url = baseurl + str(i)
        print(url)
        html = askUrl(url)
        # 解析数据
        soup = bs4.BeautifulSoup(html, "html.parser")
        a = soup.find_all('div', class_="card-feed")
        b = soup.find_all('div', class_="avator")
        for item1,item2 in zip(a,b):  # 查找符合要求的字符串，形成列表
            data=[]
            item1 = str(item1)
            link = re.findall(findLink, item1)[0]
            data.append(word_messy(link))
            content = re.findall(findContent, item1)[0]
            data.append(word_messy(content))

            item2 = str(item2)  # item2是avator模块的全部内容
            uidUrl = re.findall(findInfoUrl, item2)[0]
            preUid = re.findall(findPreUid, uidUrl)
            uid = str(test('http:' + uidUrl))
            flag = 'personal'  # 开头为5、6、7是个人
            info = str(user_info(uid, flag, preUid))
            address = re.findall(findAddress,info)
            data.append(re.sub(u"([^\u4e00-\u9fa5])", "", str(address)))#地址
            sex = re.findall(findSex,info)
            data.append(sex)#性别
            age = re.findall(findAge,info)
            zuo = re.findall(findZuo,info)
            if age!=[]:
                age1 = int(str(age).replace('[','').replace(']','').replace('\'',''))
                data.append(2021-age1)#年龄
            else:
                data.append(None)
            if zuo !=[]:
                data.append(zuo)#星座
            else:
                data.append(None)
            datalist.append(data)
    b1=[]
    for it in datalist:
        if it not in b1:
            b1.append(it)
    #print(b1)
    return b1

def user_info(uid,flag,preUid):
    if(flag=='personal'):
        url = 'https://weibo.com/p/' + uid + '/info?mod=pedit_more'
    html = requests.get(url, headers=head,cookies=cookie)
    if html.status_code ==200:
        soup = bs4.BeautifulSoup(html.text,'html.parser')
        res = soup.find_all('script')#基本信息212昵称锁骨姐宋文婷12所在地上海12性别女12生日1985年11月10日
        if(flag=='personal'):
            res1 = re.sub(u"([^\u4e00-\u9fa5^0-9])", "", str(res))
            info1 = re.findall(findUserPersonalInfo, str(res1))
    return info1

def askUrl(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    }
    request = urllib.request.Request(url, headers=head)
    try:
        response = urllib.request.urlopen(request)
        # 加上decode('utf-8', 'ignore')，防止有非法字符。
        html1 = response.read().decode('utf-8', 'ignore')
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html1

def test(url):
    html = requests.get(url, headers=head, cookies=cookie)
    if html.status_code == 200:
        soup = bs4.BeautifulSoup(html.text, 'html.parser')
        res = soup.select('script[type="text/javascript"]')[2]
        if(len(re.split(';',str(res)))>=4):

            temp = re.split(';',str(res))[3]
            tmp1 = re.sub(u"([^0-9])", "", str(temp))
        else:
            tmp1 = None
    return str(tmp1)

def saveData(datal, savepath):
    #print(datal)
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet('微博疫情讨论', cell_overwrite_ok=True)
    col = ("用户名", "用户微博内容","用户所在地","用户性别","用户年龄","用户星座")
    for i in range(0, 6):
        sheet.write(0, i, col[i])  # 列名
        i=0
    for i in range(0, len(datal)):
        #print("第%d条" % (i+1))
        data = datal[i]
        #print(data)
        for j in range(0, 6):
            if  data[j]!=[]:
                sheet.write(i + 1, j, data[j])
            else:
                sheet.write(i+1, j ,None)
    #print(datal)
    book.save(savepath)

if __name__ == "__main__":  # 程序入口
    tp="华晨宇"
    main(tp)
