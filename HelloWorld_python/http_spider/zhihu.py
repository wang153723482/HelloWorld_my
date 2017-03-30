#encoding=utf8
# 作者：挖数
# 链接：https://www.zhihu.com/question/28975391/answer/100796070
# 来源：知乎
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

import requests
import urllib2
import re
import random
from time import sleep

def main():
    url='https://www.zhihu.com/question/31106546'
    set_headers = {'Host':'https://www.zhihu.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
        'Accept':'',
        'Connection':'keep-alive'
    }
    req = urllib2.Request(url,headers=set_headers)
    r = urllib2.urlopen(req)
    html = r.read()
    html = html.decode('utf-8','replace').encode(sys.getfilesystemencoding())
    print html


    # sleep(random.uniform(0.5,1))

if __name__=='__main__':
    main()
    print 9999