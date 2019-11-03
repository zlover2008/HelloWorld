import urllib.request
import re
import os
import urllib
import pickle
headers = {
    'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
    'Connection': 'keep-alive'
}

url = r'https://detail.1688.com/offer/552152081737.html'
req = urllib.request.Request(url, headers=headers)
page = urllib.request.urlopen(req)
html = page.read()
jieguo = html.decode('gbk')


reg = r'[a-zA-z]+://[^\s]*rp=\d{1}|[a-zA-z]+://detail[^\s]*html'
urlre = re.compile(reg)
urllist = urlre.findall(jieguo)

print(urllist)

pageFile = open(r'D:\test\urlbak.pkl','w')#以写的方式打开pageCode.txt
pickle.dump(urllist, pageFile)#写入
pageFile.close()#开了记得关