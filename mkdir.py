#coding:utf-8
import re
from geturl import get_url,urls
import os
import time
import datetime

print time.time()
time = datetime.datetime.now().strftime('%Y%m%d')

#print get_url
#i = r'<a href="http://cyecomarine.com/cn/">上海船研环保技术有限公司</a>'
#print i.split( '>')[1].split('<')[0]

def mkdir():
    for i in get_url:
        # print type(i)
        com = str(i).split('>')[1].split('<')[0].decode('utf-8')
        #print com
        dir= "E:\\SEC\\%s\\IMG\\%s" % (com, time)
        os.makedirs(dir)# 按照时间创建文件夹

mkdir()

md = "E:\\SEC\\%s\\IMG\\%s" % (com, time)
print md