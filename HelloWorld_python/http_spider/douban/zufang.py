# encoding=utf-8
__author__ = 'wangchao'

import urllib2
import sqlite3
from pyquery import PyQuery as pq
import jieba

# 租房小组，获取所有的标题，并进行分词，存入数据库



cx = sqlite3.connect("sqlite_zufang.db")

cu = cx.cursor()


def main(page):
    # page = 0
    url = 'https://www.douban.com/group/beijingzufang/discussion?start=' + str(page)
    url_handle = urllib2.urlopen(url, 'utf-8')
    html_source = url_handle.read()

    # html_source = open('test.txt', 'r').read()

    pq_obj = pq(html_source)

    i = 0
    for tr in pq_obj('#content').find('table').find('tr'):
        i += 1
        if i < 3:
            continue
        tr_obj = pq(tr)
        # $("ul li:eq(3)")
        td_title = tr_obj('td:eq(0)')
        td_author = tr_obj('td:eq(1)')
        td_time = tr_obj('td:eq(3)')

        c_url = td_title('a').attr('href')
        c_title = td_title('a').attr('title')
        c_title_show = td_title.text()
        a_url = td_author('a').attr('href')
        a_name = td_author.text()
        t_time = td_time.text()

        seg_list = jieba.cut_for_search(c_title_show)  # 搜索引擎模式
        c_title_words = ",".join(seg_list)

        for t in [(c_url, c_title, c_title_show, a_url, a_name, t_time, c_title_words)]:
            cx.execute(
                "INSERT INTO zufang1('c_url','c_title','c_title_show','a_url','a_name','t_time','c_title_words') "
                "VALUES (?,?,?,?,?,?,?)", t)
            cx.commit()

        


if __name__ == '__main__':
    for i in range(4469):
        main(i * 25)
        print('page ' + str(i) + ' is over =======================')

        # main()
        # test()
