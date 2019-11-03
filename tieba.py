#coding:utf-8
import urllib.request

page = urllib.request.urlopen('http://tieba.baidu.com/p/1753935195')
htmlcode = page.read()
#print(htmlcode)

pageFile = open('D:\python\pageCode.txt','wb+')#以写的方式打开pageCode.txt
pageFile.write(htmlcode)#写入
pageFile.close()#开了记得关
