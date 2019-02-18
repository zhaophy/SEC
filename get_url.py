#coding:utf-8
import requests
from bs4 import BeautifulSoup
import urllib
import re

def get_url(url):  #获取集团下公司官网名称与其URL组成的列表
    r = requests.get(url).content
    soup = BeautifulSoup(r, 'lxml')
    find = soup.find('p')
    urls = soup.find_all('a')
    outurl = []
    for i in urls:
        if 'http' in str(i) and 'shanghai-electric' not in str(i) and 'gov.cn' not in str(i):
            outurl.append(i)
    return outurl
get_url = get_url('http://www.shanghai-electric.com/Pages/Companys.aspx')


def urls(): ##获取仅含集团下公司官网URL的列表
    urls = []
    for i in get_url:
        # print i
        #print  i['href']
        urls.append(i['href'])
    return urls
print urls()
print len(urls())




#由于图片的链接可能有的为相对路径有的为绝对路径，故需统一全部为绝对路径的URL，即重新组合图片链接，使列表中的图片链接均为完整链接
def get_imgs(list):#重新组合图片链接，使列表中的图片链接均为完整链接
    new_list = []
    for i in list:
        if 'http:'  in i:
            new_list.append(i)
        else:
           new_list.append( '{}{}'.format(url,i))

            #print list

    return new_list





url = 'https://www.smec-cn.com/cn/'
def get_html(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

html = get_html(url)
def get_img(html):
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    print reg
    print imgre
    print imglist
    imglists = get_imgs(imglist)
    imgurls = []
    x = 0
    for imgurl in imglists:
        print imgurl

        urllib.urlretrieve(imgurl, '%s.jpg' % x)
        x += 1


get_img(html)



