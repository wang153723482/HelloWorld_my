# encoding=utf8
from time import time



aa = 'a..a.a.aa.tx.t'

print aa.rfind('.')
print aa[aa.rfind('.'):] #获取文件扩展名

print aa.index('tx')
if aa.find('tx')>-1:
    print 1
else:
    print 2
print 22222222

a = 'a'
if a :
    print 11
else:
    print 22


table_name = 'ss'
sql_create_table = 'create table ' + table_name + '  (' \
                                                  'time_ varchar(500) default null,' \
                                                  'scp varchar(500) default null,' \
                                                  'result varchar(500) default null,' \
                                                  'trans_type varchar(500) default null,' \
                                                  'req_no varchar(500) default null,' \
                                                  'cost varchar(500) default null,' \
                                                  'mark varchar(500) default null' \
                                                  ') ENGINE=InnoDB DEFAULT CHARSET=latin1;'

print sql_create_table

s = '[lo[g4j]'
print s.find('[')

pass

s = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><response><certificates><certificate><amount>100.00</amount><certificateId>g3VGvCB/yczklst97WzChYzNkCSlz8O6MHvqU0Lx7Oc=</certificateId><datePurchased>1481163455000</datePurchased><ephemeralPublicKey>MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE43IDxnPVaNVL/4PnSzoExG2LTJ3s1EbHLzBvCMnL2ASBXSwpZkHbGe6Zswd10JSxGR2iNtEfGSUsT7LDzU0mWQ==</ephemeralPublicKey><refId>PNCZ20161208H00EBF55</refId><scn>TCA90966819121</scn><status>2</status></certificate></certificates></response>'

print s[s.index('<refId>') + 7:s.index('</refId>')]

s = '[log4j] 2016-12-07 15:38:45,422 - com.zihexin.web.controller.CommunicationController_getMessage INFO   - |SCP|SUCCESS|CreateCertificate|077f0f2bbe3ea8801c300b14c0acc86c|486|完成业务操作|'

print s[s.index('|SCP|'):]

print s[8:31]

print ''.join(['aa', 'bb'])

t = time()
for i in range(1000000):
    s = ''.join(['aa', 'bab', 'bab'])
print time() - t

t = time()
for i in range(1000000):
    s = 'aa' + 'bb' + 'byb'
print time() - t


def method1():
    t = time()
    for i in xrange(1000000):
        s = 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab' + 'pythontab'
    print time() - t


def method2():
    t = time()
    for i in xrange(1000000):
        s = ''.join(
            ['pythontab', 'pythontab', 'pythontab', 'pythontab', 'pythontab', 'pythontab', 'pythontab', 'pythontab',
             'pythontab', 'pythontab', 'pythontab', 'pythontab', 'pythontab', 'pythontab', 'pythontab', 'pythontab',
             'pythontab', 'pythontab', 'pythontab', 'pythontab', 'pythontab', 'pythontab', 'pythontab', 'pythontab',
             'pythontab', 'pythontab', 'pythontab', 'pythontab', 'pythontab', 'pythontab', 'pythontab', 'pythontab',
             'pythontab', 'pythontab', 'pythontab', 'pythontab', 'pythontab', 'pythontab', 'pythontab', 'pythontab',
             'pythontab', 'pythontab', 'pythontab', 'pythontab', 'pythontab', 'pythontab'])
    print time() - t


method1()
method2()
