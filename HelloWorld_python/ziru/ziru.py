# encoding=utf8

import datetime
import urllib2
import urllib
import sqlite3
import os
from pyquery import PyQuery as pq
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# sql = 'create table ziru_house(room_id,room_name,price,mianji,chaoxiang,huxing,louceng,jiaotong,url,quyu,shangquan,create_date)'
# sql2 = 'create table ziru_pic(room_id,url,local_path)'

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'll="108288"; bid=-eLVuRym7hk; __utmt=1; dbcl2="154230225:g19PdE0CXtw"; _ga=GA1.2.576788339.1480220093; _gat_UA-7019765-1=1; ck=1y_j; push_noty_num=0; push_doumail_num=0; _pk_id.100001.8cb4=dba2dac045704948.1480220093.1.1480220106.1480220093.; _pk_ses.100001.8cb4=*; __utma=30149280.576788339.1480220093.1480220093.1480220093.1; __utmb=30149280.3.10.1480220093; __utmc=30149280; __utmz=30149280.1480220093.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=30149280.15423; _vwo_uuid_v2=1D944F328C30D183491E7AA72D1EA095|56fea8feb15293b476abd5975eedc829; ap=1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.1.2840.99 Safari/537.36'
}

IMAGES = 'ziru/images/'

con = sqlite3.connect('ziru.db')
cur = con.cursor()

def do_request(_url):
    try:
        # 随机获取一个代理地址
        # proxy_addres = {'http': '127.0.0.1:1080'}
        # proxy_handler = urllib2.ProxyHandler( proxy_addres )
        # opener = urllib2.build_opener(proxy_handler)
        # r = opener.open(_url)
        # return r.read()
        return urllib2.urlopen(_url).read()
    except Exception,e:
        print e
        # do_request(_url)

#单独一张表保存图片信息，room_id、pic_url,同一个url可能对应多个不同的房间
def download_pic(pic_list,room_id):
    for pic in pic_list:
        pic_url = pq(pic).attr('src')
        pic_name = pic_url[pic_url.rindex('/')+1:]
        local_path = IMAGES + room_id +'/'+ pic_name
        print(pic_url)
        sql = 'select count(1),local_path from ziru_pic where url = "'+pic_url+'"' \
                                                                               'group by local_path'
        cur.execute(sql)
        feo = cur.fetchone()
        if feo and feo[0]=='0':
            local_path = feo[1] #把数据库中保存的url拿出来

        sql_insert = 'insert into ziru_pic (room_id,url,local_path)' \
                     'values(?,?,?)'
        cur.execute(sql_insert,[room_id,pic_url,local_path])
        con.commit()

        # 创建子目录 images/[room_id]/[原图片名称]
        new_path = IMAGES+room_id
        if not os.path.exists(new_path):
            os.makedirs(new_path)

        # 下载图片
        pic_file = open(new_path+'/'+pic_name,'wb')
        # pic_file.write( urllib2.urlopen(pic_url).read() )
        pic_file.write( do_request(pic_url) )

    pass

#todo 判断是否已配置、是否预定中
def do_detail(url_list):
    i = 0
    for u in url_list:
        i += 1
        # if i==3:
        #     break
        detail_house = do_request(u)
        py_detail_house = pq(detail_house)
        room_id = py_detail_house('.aboutRoom h3').text().replace('编号：','').replace(' ','')
        print(room_id)
        room_detail_right =py_detail_house('.room_detail_right')
        room_name = room_detail_right('.room_name h2').text()        #标题 room_name
        print( room_name)
        room_local = room_detail_right('.room_name p span').text()
        arry = room_local[1:room_local.index(']')].split(' ')
        quyu = arry[0]
        shangquan = arry[len(arry)-1]
        print(quyu)
        print(shangquan)
        room_price = room_detail_right('.room_price').text().replace('￥','')#价格  room_price
        print(room_price)

        #基本信息
        detail_room = room_detail_right('.detail_room').children()
        mianji = pq(detail_room[0]).text().replace('面积：','').replace(' ','').replace('\n','')
        chaoxiang = pq(detail_room[2]).text().replace('朝向：','').replace(' ','').replace('\n','')
        huxing = pq(detail_room[3]).text().replace('户型：','').replace(' ','').replace('\n','')
        louceng = pq(detail_room[4]).text().replace('楼层：','').replace(' ','').replace('\n','')
        jiaotong = pq(detail_room[5]).text().replace('交通：','').replace(' ','').replace('\n','')

        sql = 'insert into ziru_house(room_id,room_name,price,mianji,quyu,shangquan,chaoxiang,huxing,louceng,jiaotong,url,create_date)' \
              'values(?,?,?,?,?,?,?,?,?,?,?,?)'
        cur.execute(sql,[room_id,room_name,room_price,mianji,quyu,shangquan,chaoxiang,huxing,louceng,jiaotong,u,datetime.datetime.now()])
        con.commit()

        #图片信息
        # room_pic =py_detail_house('#cao ul li a img')
        # download_pic(room_pic,room_id)    #下载图片略烦，先不考虑了


def main(detail_url_list,url_index):
    html_index = do_request(url_index)
    py_index = pq(html_index)
    house_list = py_index('#houseList').children()
    print len(house_list)
    i = 0
    for house in house_list:
        i = i + 1
        try:
            house_url = 'http:'+pq(house).children().children().attr('href')
            detail_url_list.append(house_url)
        except Exception,e:
            print i
            print e

    page_next = py_index('#page .next')
    if page_next:
        main(detail_url_list,'http:'+page_next.attr('href'))

    return detail_url_list


if __name__ == '__main__':
    index_urls = []
    detail_host_list = []

    index_url = 'http://www.ziroom.com/z/nl/z2-r1500TO2600-u3-d23008611.html'
    house_list = main(detail_host_list,index_url)
    do_detail(house_list)




'''
ziru

   
每次查询都随机使用一个代理和请求头信息进行查询

搜索条件：（8次） 链接写死的!!!
友家合租
丰台、昌平、房山、大兴
1500-2600
2居、3居

http://www.ziroom.com/z/nl/z2-r1500TO2600-d23008617-u2.html
http://www.ziroom.com/z/nl/z2-r1500TO2600-d23008617-u3.html

http://www.ziroom.com/z/nl/z2-r1500TO2600-u2-d23008611.html
http://www.ziroom.com/z/nl/z2-r1500TO2600-u3-d23008611.html

http://www.ziroom.com/z/nl/z2-r1500TO2600-u2-d23008616.html
http://www.ziroom.com/z/nl/z2-r1500TO2600-u3-d23008616.html

http://www.ziroom.com/z/nl/z2-r1500TO2600-u2-d23008615.html
http://www.ziroom.com/z/nl/z2-r1500TO2600-u3-d23008615.html


结果：
链接
标题
价格、面积、朝向、户型、楼层
户型图、房间图



配置中 可预定
//img.ziroom.com/pic/static/images/slist_1207/defaultPZZ/other-canbook.jpg_C_264_198_Q80.webp

配置中
//img.ziroom.com/pic/static/images/slist_1207/defaultPZZ/other-loading.jpg_C_264_198_Q80.webp

//img.ziroom.com/pic/static/images/slist_1207/defaultPZZ/other-loading.jpg_C_264_198_Q80.webp


'''