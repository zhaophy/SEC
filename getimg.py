#coding:utf-8
from geturl import urls,
import datetime

companylist =
path = "E:\\SEC\\IMG\\"

def get_html(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


#html = get_html(url)

def get_img(html):
    reg = r'src="(.+?\.(png|jpg))"'
    imgre = re.compile(reg)
    imglist = list(set(re.findall(imgre, get_html(url))))
    imglist_re = []
    for i in imglist:
        imglist_re.append(i[0])
    imglists = list(set(get_imgs(imglist_re)))

    x = 0
    for imgurl in imglists:


        urllib.urlretrieve(imgurl, 'd:\\sec\\sec\\img\\%s.jpg' % x)
        x += 1
