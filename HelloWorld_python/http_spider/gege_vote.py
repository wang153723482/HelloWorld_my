# encoding=utf8
__author__ = 'wangchao'

import json
import urllib2
import sys
from pyquery import PyQuery as pq


def main():
    'this is test'
    # urlTarget = 'http://u.interlib.cn:81/onecard/vote/index/atbuwb1448435157?aid=3'
    urlTarget = 'http://10.7.13.154/demo/vote.html'
    urlItem = urllib2.urlopen(urlTarget)
    htmlSource = urlItem.read()
    urlItem.close()
    # html = htmlSource.decode('utf-8','replace').encode(sys.getfilesystemencoding())
    # print html
    html = htmlSource
    d = pq( unicode(html,'utf-8') )
    
    l = {}
    for div in d('.per-con'):
        name = div.find('p').find('span').getnext().text
        piaoshu = div.find('p').getnext().getnext().getnext().find('span').find('span').text
        # print name 
        # print piaoshu
        l[name]=int(piaoshu)
        
    dict= sorted(l.iteritems(), key=lambda d:d[1], reverse = True)
    
    for a in dict :
        print type(a)


    



if __name__ == '__main__':
    print main
    main()
