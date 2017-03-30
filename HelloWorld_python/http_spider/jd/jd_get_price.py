#encoding=UTF-8
import urllib2
import json

#
# Description: 根据SKU获取京东商品的售卖价格，未持续调用，不知道京东是否会封IP。
# Author:wangc
# Version:0.1
# Date:2016-04-28 13:30
#


def main():
    #获取商品价格url，商品地址为http://item.jd.com/1413825.html，数字为SKU
    urlTarget = 'http://p.3.cn/prices/get?skuid=J_1413825'
    urlTarget = 'http://locate.apple.com/cn/zh/sales/?pt=all&lat=23.125178&lon=113.280637&address=Guangdong'
    urlItem = urllib2.urlopen(urlTarget)
    htmlSource = urlItem.read() #获取价格信息
    print(htmlSource)
    urlItem.close()

    htmlJson = json.loads(htmlSource)
    print(htmlJson[0].get('p')) #获取当前售价


if __name__=='__main__':
    main()