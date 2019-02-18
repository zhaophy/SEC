#coding:utf-8

import urllib
import re
url = 'http://cyecomarine.com/cn/'

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

    imgurls = []
    for i in imglist:

        if 'http' not in i:
            imgurl = '{}{}'.format(url,i)
            imgurls.append(imgurl)
    return imgurls
    #x = 0
    #for imgurl in imglist:
     #   urllib.urlretrieve(imgurl, '%s.jpg' % x)
      #  x += 1

print get_img(html)

