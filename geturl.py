#coding:utf-8
import requests
from bs4 import BeautifulSoup
import urllib
import re
import datetime


def get_url(url):  #获取集团下公司官网名称与其URL组成的列表
    r = requests.get(url).content
    soup = BeautifulSoup(r, 'lxml')
    find = soup.find('p')
    urls = soup.find_all('a')
    outurl = []
    for i in urls:
        if 'http' in str(i) and 'shanghai-electric' not in str(i) and 'gov.cn' not in str(i):
            outurl.append(i)
    return sorted(outurl)
get_url = get_url('http://www.shanghai-electric.com/Pages/Companys.aspx')



def urls(): ##获取仅含集团下公司官网URL的列表
    urls = []
    for i in get_url:
        # print i
        #print  i['href']
        urls.append(i['href'])
    return urls




def com_list(): ###获取公司名称的列表
    com = []
    for i in get_url:
        com.append(str(i).split('>')[1].split('<')[0].decode('utf-8'))
    return  com
print get_url
print urls()
print com_list()
len = len(com_list())



def com_url():
    com_urls = []
    for i in range(len):
        com_urls.append({com_list()[i]:urls()[i]})
    return com_urls
print com_url()



