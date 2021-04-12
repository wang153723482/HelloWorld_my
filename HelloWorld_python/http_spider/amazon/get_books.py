# encoding=utf8
import requests
from pyquery import PyQuery as pq

# 获取亚马逊的所有书名
# python3


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


# 获取分类
def get_classification():
    requests.DEFAULT_RETRIES = 2  # 增加重试连接次数
    s = requests.session()
    s.keep_alive = False  # 关闭多余连接
    url = 'https://www.amazon.cn/Kindle%E7%94%B5%E5%AD%90%E4%B9%A6/b?ie=UTF8&node=116169071&ref_=nav_topnav_giftcert'
    s.get(url)  # 你需要的网址
    response = s.get(url, headers=headers)
    resp_obj = pq(response.text)
    classification_xpath = '//*[@id="s-refinements"]/div'
    divs = resp_obj('#s-refinements').children('div')
    # for div in divs:
    #     print('=================')
    #     print(div)
    print()
    cf_ul = pq(divs[2]).find('ul li').eq(2)
    for ul in cf_ul:
        print(pq(ul).html())



def main():
    get_classification()
    pass


if __name__ == '__main__':
    main()
