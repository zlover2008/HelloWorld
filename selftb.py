# response = urllib.request.urlopen("https://detail.tmall.com/item.htm?id=558659358821")
# request =urllib.request.Request("https://www.baidu.com")
# request.add_header('User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36')
# response = urllib.request.urlopen(request)
# print(response.read().decode("utf-8"))

import urllib.request
import re
import os
import urllib
import socket
#根据给定的网址来获取网页详细信息，得到的html就是网页的源代码  
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html.decode('gbk')

def getImg(html):
    reg = r'//(.*?)_60x60q90'
    imgre = re.compile(reg)
    imglist = imgre.findall(html)#表示在整个网页中过滤出所有图片的地址，放在imglist中
    x = 0
    path = 'D:\\test'  
   # 将图片保存到D:\\test文件夹中，如果没有test文件夹则创建
    if not os.path.isdir(path):  
        os.makedirs(path)  
    paths = path+'\\'      #保存在test路径下  

    for imgurl in imglist:  
        urllib.request.urlretrieve('http://'+imgurl,'{}{}.jpg'.format(paths,x))  #打开imglist中保存的图片网址，并下载图片保存在本地，format格式化字符串 
        x = x + 1  
    return imglist

urladdress = input("请输入宝贝地址：")

html = getHtml(urladdress)#获取该网址网页详细信息，得到的html就是网页的源代码  
print (getImg(html)) #从网页源代码中分析并下载保存图片


