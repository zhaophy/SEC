# -*- coding: utf-8 -*-
from urllib2 import urlopen
from bs4 import BeautifulSoup
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
s = [] #扫苗当前URL所得的所有URL
already = set() #已扫苗过的URL
urls = {} #上海电气URL和该URL含有非上海电气域名的URL组成的字典


def getLinks(articleUrl):
    if articleUrl not in already:   #如果该URL已经扫描过
        already.add(articleUrl)    #
        try:
            html = urlopen(articleUrl)
            bsObj = BeautifulSoup(html, "html.parser")
            alls = []

            for i in bsObj.find_all('a'):
                try:
                    alls.append(i['href'])

                except:
                    pass
            all = list(set(alls))   #去重

            for j in all[:]:

                for k in ['jpg', 'JPG', 'pdf', 'bmp', 'mailto', 'gov.cn', '#','javascript']:
                    if k in j:
                        all.remove(j)  #####过滤掉静态文件，政府网站，邮箱等

            for m in range(len(all)):
                if 'shanghai-electric.com' not in str(all[m]) and 'http://' not in str(all[m]):
                    all[m] = 'http://www.shanghai-electric.com/' + all[m]  #如果有的URL采用的是相对路径，则补全
            out = []
            for n in all[:]:
                if 'shanghai-electric.com' not in str(n):  #过滤外部URL
                    out.append(n)
                    all.remove(n)
            if len(out) > 0: #当前页面如果含有外部URL则更新至原字典
                urls.update({articleUrl: out})

            if articleUrl in all:
                all.remove(articleUrl)
                global s
                s = list(set(s + list(set(all))))  #当前页面如果含有外部URL则更新至原列表
            if articleUrl in s:
                s.remove(articleUrl)

            return s
        except Exception, e:
            print e
            if articleUrl in s:
                s.remove(articleUrl)

            return s
    else:
        if articleUrl in s:
            s.remove(articleUrl)
        return s

links = getLinks('http://www.shanghai-electric.com/Pages/Companys.aspx')


n = 0
while len(links) > 0:
    for u in links:
        getLinks(u)
        n = n + 1
        print links
        print already
        print len(already)

        links = getLinks(u)

print urls
