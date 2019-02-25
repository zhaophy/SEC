#coding:utf-8
from geturl import get_url,urls,com_list

list = urls()
path = 'e:\\sec\\%s\\'

def down_img(list,path):
    for i in list:
        page = urllib.urlopen(i)
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
