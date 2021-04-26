# encoding=gbk
import urllib2
import gzip
import binascii
from StringIO import StringIO
from pyquery import PyQuery as pq
import json
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import datetime

url1 = 'https://bj.lianjia.com/ershoufang/'
url2 = 'co21ng1hu1nb1l2p1/'
url = url1 + url2

key_words = [u'�Ͽ�', u'����', u'����', u'�ǹ�', u'�����', u'��ƽ����', u'�׶�����', u'��԰', u'���ػ���']

blacklist = ['https://bj.lianjia.com/ershoufang/101102309958.html',
             'https://bj.lianjia.com/ershoufang/101102400383.html',
             'https://bj.lianjia.com/ershoufang/101102287209.html']

result_file_name = 'result2.csv'

page_data = []

page_total = 0

email_body = ''
email_title = ''

my_dict = dict()

headers = {
    'Host': 'bj.lianjia.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,de;q=0.6',
    'Cookie': 'select_city=110000; all-lj=406fadba61ceb7b8160b979dadec8dfa; lianjia_ssid=f6d75b91-c20c-464a-ad8d-215617d14b0a; lianjia_uuid=8f108264-76ff-48f0-b6bf-efcdd49ca780; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1514819141; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1514819141; UM_distinctid=160b241c8d21e9-05c51609a48a928-41554130-144000-160b241c8d33c0; CNZZDATA1253477573=214118895-1514817856-%7C1514817856; CNZZDATA1254525948=1623949242-1514815949-%7C1514815949; CNZZDATA1255633284=666341979-1514814294-%7C1514814294; CNZZDATA1255604082=790662337-1514814374-%7C1514814374; _smt_uid=5a4a4e48.1e6ee96b; _jzqa=1.337153783675248830.1514819146.1514819146.1514819146.1; _jzqb=1.1.10.1514819146.1; _jzqc=1; _jzqckmp=1; _qzja=1.236947836.1514819181560.1514819181560.1514819181560.1514819181560.1514819181560.0.0.0.1.1; _qzjb=1.1514819181560.1.0.1.0; _qzjc=1; _qzjto=1.1.0'
}


def gunziptxt(data):
    buf = StringIO(data)
    of = gzip.GzipFile(fileobj=buf, mode="rb")
    outdata = of.read()
    return outdata


def check(d):
    for k in key_words:
        if d.find(k) >= 0:
            return True  # �������������true
    return False


def send_mail(subject, msg):
    # ������ SMTP ����
    mail_host = "mail.zihexin.com"
    mail_user = "wangchao0048"
    mail_pass = "111111"

    sender = 'wangchao0048@zihexin.com'
    receivers = ['153723482@qq.com']  # �����ʼ���������Ϊ���QQ���������������

    message = MIMEText(msg, 'plain', 'utf-8')
    message['From'] = Header(sender, 'utf-8')
    message['To'] = Header('153723482@qq.com', 'utf-8')
    message['Cc'] = Header('983715180@qq.com', 'utf-8')

    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 Ϊ SMTP �˿ں�
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print u"�ʼ����ͳɹ�"
    except smtplib.SMTPException:
        print u"Error: �޷������ʼ�"


# ��csv�ж�ȡ���е����ݣ����������ǰ��url���򷵻ؿհ��ַ��������򷵻�'new'����д���ļ�
def check_new(url, text):
    i = 1
    with open(result_file_name, 'a+') as lines:
        for line in lines:
            if line.find(url) > -1:
                return ''
            i = int(line[0:line.index(',')]) + 1
        lines.write(str(i) + ',' + url + ',' + str(text.encode('utf-8').strip()) + '\n')


def do_url(url):
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request).read()
    outdata = gunziptxt(response)
    # print outdata

    pq_obj = pq(outdata)
    sellListContent = pq_obj('.sellListContent')
    # print sellListContent

    lis = sellListContent('li')
    for li in lis.items():
        positionInfo = li('.positionInfo')
        if not check(positionInfo.html()):
            h_url = li.find('a').attr('href')
            if not h_url in blacklist:
                check_new(h_url, li.text())
            pass
    return pq_obj


# ��ȡ��һҳ���������ҳurl
def main():
    pq_obj = do_url(url)

    # �����ҳ
    pages = pq_obj('.page-box').filter('.house-lst-page-box')
    # print pages.attr('page-data')
    json_str = json.loads(pages.attr('page-data'))
    # print json_str['totalPage']
    total_page = int(json_str['totalPage'])
    for i in range(2, total_page + 1):
        page_data.append(url1 + 'pg' + str(i) + url2)

    # ����������
    page_total = int(pq_obj('.total').filter('.fl').find('span').html())
    my_dict['page_total'] = page_total


# �������һҳ���������
def main2():
    for url in page_data:
        do_url(url)


if __name__ == '__main__':
    main()
    main2()
    print '========='
    msg = ''
    my_hours = open(result_file_name, 'r')
    my_cou = 0
    for h in my_hours:
        my_cou = my_cou + 1
        msg += (h.replace(',', '\n').replace('-','\n') + '\n' + '\n')
    sub = u'��' + str(my_dict['page_total']) + u'����ɸѡ��' + str(my_cou) + u'��' + datetime.datetime.now().strftime(
        '%Y-%m-%d %H:%M:%S')

    send_mail(sub, msg)
    print sub
    print msg
