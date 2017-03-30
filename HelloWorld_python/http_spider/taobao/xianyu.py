# encoding=utf8
__author__ = 'wangchao'

import urllib2
import re
import datetime
from pyquery import PyQuery as pq
import sqlite3

# 根据关键字从闲鱼获取商品列表，记录商品url、价格、标题、简介，并对标题和简介进行分词

PROTOCOL = 'https:'


cx = sqlite3.connect('taobao.db')
cur = cx.cursor()


def main():
    
    url = 'https://s.2.taobao.com/list/list.htm?spm=2007.1000337.3.2.ebCToK&catid=50100399&st_trust=1&q=iphone+6s&ist=0'
    page_no = 0
    searchByKeyWord(url,page_no)
    cx.commit()
    cur.close()
    cx.close()


# 根据关键字进行搜索
def searchByKeyWord(url,page_no):
    page_no =page_no+ 1
    f = urllib2.urlopen(
        'https://s.2.taobao.com/list/list.htm?spm=2007.1000337.3.2.ebCToK&catid=50100399&st_trust=1&q=iphone+6s&ist=0')
    # f = open('test.html', 'r')

    pqf = pq(f.read())
    lists = pqf.find('.item-lists').find('.item-info-wrapper.item-idle.clearfix')

    i = 0
    d1 = datetime.datetime.now()
    for list_ in lists:
        # if i == 1:
        #     break
        # i += 1
        obj_this = pq(list_)
        ele_title = obj_this.find('.item-title')
        title_text = ele_title.text()
        title_url = ele_title.find('a').attr('href')
        print title_text
        print title_url

        ele_price = obj_this.find('.price').find('em')
        price = ele_price.text()
        print price

        ele_description = obj_this.find('.item-description')
        desc = ele_description.text()
        print desc

        ele_seller = obj_this.find('.seller-nick a')
        seller_url = ele_seller.attr('href')
        seller_name = ele_seller.text()
        print seller_url
        print seller_name

        ele_location = obj_this.find('.seller-location')
        location = ele_location.text()
        print location

        ele_time = obj_this.find('.item-pub-time')
        time_ = re.findall('^[0-9]{1,2}', ele_time.text())[0]
        d2 = d1 - datetime.timedelta(minutes=int(time_))
        oper_date = d2.strftime("%Y-%m-%d %H:%M:%S")
        print oper_date

        now_ = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        t = (title_text, title_url, price, desc, seller_url, seller_name, location,page_no, oper_date, now_)
        cur.execute(
            'insert into xianyu (title_text,title_url,price,desc,seller_url,seller_name,location,page_no,oper_date,create_date)'
            'values(?,?,?,?,?,?,?,?,?,?);', t)
        cx.commit()
    ele_next = pqf.find('.paginator-next')
    next_url = PROTOCOL + ele_next.attr('href')
    searchByKeyWord(next_url,page_no)
    pass


if __name__ == '__main__':
    main()
