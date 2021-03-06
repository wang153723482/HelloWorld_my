# encoding=utf8
# -*- coding: utf-8 -*-
import requests
from pyquery import PyQuery as pq

# 获取亚马逊的所有书名
# python3


# 访问分类页面的url
clc_url = 'https://www.amazon.cn/Kindle%E7%94%B5%E5%AD%90%E4%B9%A6/b?ie=UTF8&node=116169071&ref_=nav_topnav_giftcert'

'''
访问首页的header

'''

headers = {'Host': 'www.amazon.cn',
           'Connection': 'keep-alive',
           'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
           'sec-ch-ua-mobile': '?0',
           'DNT': '1',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'Sec-Fetch-Site': 'none',
           'Sec-Fetch-Mode': 'navigate',
           'Sec-Fetch-User': '?1',
           'Sec-Fetch-Dest': 'document',
           'Accept-Encoding': 'gzip, deflate, br',
           'Accept-Language': 'zh-CN,zh;q=0.9', }

# 访问某一个分类的header
headers2 = {'Host': 'www.amazon.cn',
            'Connection': 'keep-alive',
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'DNT': '1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': 'https://www.amazon.cn/Kindle%E7%94%B5%E5%AD%90%E4%B9%A6/b?ie=UTF8&node=116169071&ref_=nav_topnav_giftcert',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9', }


# 获取分类
def get_classification():
    requests.DEFAULT_RETRIES = 2  # 增加重试连接次数
    s = requests.session()
    s.keep_alive = False  # 关闭多余连接
    url = clc_url
    # s.get(url)  # 你需要的网址
    response = requests.get(url, headers=headers)
    # print(response.text)
    resp_obj = pq(response.text)
    divs = resp_obj('#s-refinements').children('div')
    # print(divs)
    # if 1==1:
    #     return
    cf_ul = pq(divs[2]).find('ul li')
    i = 0
    file_classfication = open('cfc.csv', 'w')
    for ul in cf_ul:
        i = i + 1

        if i < 3:
            # 前2个不是要抓取的分类名称
            continue
        print('==============')
        ss = pq(ul).find('a').attr('href')
        c_name = pq(ul).text()
        # 分类ID，拼到url中 https://www.amazon.cn/s?rh=n%3A{}&fs=true&ref=lp_{}_sar 请求这个的时候记得refer_url为下面那个长链接
        c_id = ss[56:65]
        c_url = 'https://www.amazon.cn/s?rh=n%3A{}&fs=true&ref=lp_{}_sar'.format(c_id, c_id)
        file_classfication.write((c_id + ',' + c_name + ',' + c_url + '\n'))
        # print(c_id + ',' + c_name + ',' + c_url)


# 根据url获取图书名称写入文件，c_id作为文件名
def get_books_by_url(c_id, c_url):
    response = requests.get(c_url, headers=headers2)
    # print(response.text)
    resp_obj = pq(response.text)
    # 书名
    a = resp_obj('#search > div.s-desktop-width-max.s-opposite-dir > div > div.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16 > div > span:nth-child(4) > div.s-main-slot.s-result-list.s-search-results.sg-row > div:nth-child(1) > div > span > div > div > div:nth-child(2) > div.sg-col.sg-col-4-of-12.sg-col-8-of-16.sg-col-12-of-20 > div > div.a-section.a-spacing-none > h2 > a > span')
    # 第二本书
    b = resp_obj('#search > div.s-desktop-width-max.s-opposite-dir > div > div.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16 > div > span:nth-child(4) > div.s-main-slot.s-result-list.s-search-results.sg-row > div:nth-child(2)')
    # 作者、年份
    a2 = resp_obj('#search > div.s-desktop-width-max.s-opposite-dir > div > div.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16 > div > span:nth-child(4) > div.s-main-slot.s-result-list.s-search-results.sg-row > div:nth-child(1) > div > span > div > div > div:nth-child(2) > div.sg-col.sg-col-4-of-12.sg-col-8-of-16.sg-col-12-of-20 > div > div.a-section.a-spacing-none > div')

    print(a)
    print(a2)
    # print(resp_obj)
    pass


def main():
    # 第一次运行需要先获取所有分类的信息，写入文件
    # get_classification()

    c_id = '143359071'
    c_url = 'https://www.amazon.cn/s?rh=n%3A143359071&fs=true&ref=lp_143359071_sar'
    get_books_by_url(c_id, c_url)

    # a = '123'
    # print ("This website name is %s %s" % (a,a))

    pass


if __name__ == '__main__':
    main()

'''
这是该分类下全部书籍的链接，替换这里的 144154071 即可。上面抓到的链接中，只有这个数字不同，其他都是相同的值
https://www.amazon.cn/s?rh=n%3A144154071&fs=true&ref=lp_144154071_sar
/s?bbn=116169071&amp;rh=n%3A116087071%2Cn%3A116169071%2Cn%3A144154071&amp;dc&amp;qid=1618411517&amp;rnid=116169071&amp;ref=lp_116169071_nr_n_0


/s?bbn=116169071&rh=n%3A116087071%2Cn%3A116169071%2Cn%3A143468071&dc&qid=1618412690&rnid=116169071&ref=lp_116169071_nr_n_27
/s?bbn=116169071&rh=n%3A116087071%2Cn%3A116169071%2Cn%3A143553071&dc&qid=1618413163&rnid=116169071&ref=lp_116169071_nr_n_32
/s?bbn=116169071&rh=n%3A116087071%2Cn%3A116169071%2Cn%3A143579071&dc&qid=1618413163&rnid=116169071&ref=lp_116169071_nr_n_33
/s?bbn=116169071&rh=n%3A116087071%2Cn%3A116169071%2Cn%3A116170071&dc&qid=1618413163&rnid=116169071&ref=lp_116169071_nr_n_34

https://www.amazon.cn/s?rh=n%3A144180071&fs=true&ref=lp_144180071_sar
https://www.amazon.cn/s?i=digital-text&rh=n%3A144180071&fs=true&page=2&qid=1618411782&ref=sr_pg_2
https://www.amazon.cn/s?i=digital-text&rh=n%3A144180071&fs=true&page=3&qid=1618413388&ref=sr_pg_3
https://www.amazon.cn/s?i=digital-text&rh=n%3A144180071&fs=true&page=4&qid=1618413415&ref=sr_pg_3
https://www.amazon.cn/s?i=digital-text&rh=n%3A144180071&fs=true&qid=1618413452&ref=sr_pg_1
https://www.amazon.cn/s?i=digital-text&rh=n%3A144180071&fs=true&page=2&qid=1618413470&ref=sr_pg_2

有一个莫名其妙的qid，貌似是在相应的cookie里的值

'''
