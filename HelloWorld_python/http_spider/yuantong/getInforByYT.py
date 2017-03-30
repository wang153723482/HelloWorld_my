__author__ = 'wangchao'

import urllib2
import urllib
import sys
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq

url = 'http://trace.yto.net.cn:8022/TraceSimple.aspx'
waybillNo = 'xxxxxxxxx'
data = {'waybillNo': waybillNo}
header = {
    'Host': '127.0.0.1',
    'Connection': 'keep-alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8'
}

def main():
    
    post_data = urllib.urlencode(data)
    req = urllib2.Request(url, post_data, header)
    content = urllib2.urlopen(req)
    html = content.read()
    html = html.decode('utf-8', 'replace').encode(sys.getfilesystemencoding())
    pq_html = pq(html)
    print(pq_html)


    

    # urlItem = urllib2.urlopen(url)
    # htmlSource = urlItem.read()
    # urlItem.close()
    # print(htmlSource)
    # pass
    # html = """ <html><head><title>The Dormouse's story</title><contents>this is contents</contents></head>
    # <body>
    #     <p>a</p><p>b</p>
    #     <p>c</p>
    # </body></html>
    # """
    # soup = BeautifulSoup(html, "lxml")
    # print soup.title
    # 
    # print soup.body.p.next_sibling

# /html/body/div[8]/div[2]/div/div[2]/table/tbody

if __name__=='__main__':
    main()