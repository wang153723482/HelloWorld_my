# encoding=utf8
import datetime
import time
import random


print(random.randint(0,9))


#休眠3秒
time.sleep(3)

t = 12
t = 1 - 12860

print(datetime.datetime.now())

t = datetime.datetime.now()

print(t.strftime('%Y-%m-%d %H:%M:%S'))

print(time.time())

print('时间戳')
print("%d" % (time.time() * 1000))
# 字符串转时间
s = '2016-11-29 18:17:26 398'
dd = datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S %f')  # %f 微秒
print(11111111)
print(dd)
print(type(dd))

# 时间计算
s = '2016-11-29 23:59:59 001'
s2 = '2016-11-29 23:59:59 200'
dd = datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S %f')
dd2 = datetime.datetime.strptime(s2, '%Y-%m-%d %H:%M:%S %f')

print((dd2 - dd).days * (24 * 60 * 60 * 1000))  # 根据day算毫秒
print((dd2 - dd).seconds * 1000)  # 根据分钟算毫秒
print((dd2 - dd).microseconds)  # 根据微秒算毫秒


def calc_time(start, end):
    return (end - start).days * (24 * 60 * 60 * 1000) + (end - start).seconds * 1000 + (end - start).microseconds / 1000


print(calc_time(dd, dd2))


start = datetime.datetime.now()
print(datetime.datetime.now())
# time.sleep(1)
print(datetime.datetime.now())
end = datetime.datetime.now()

print((end - start).seconds * 1000)

print('=======================================')

t_time = '2015-10-31 12:25:35'
t = datetime.datetime.strptime(t_time, '%Y-%m-%d %H:%M:%S')

t2 = t + datetime.timedelta(seconds=10)  # 增加10秒 
print(t)
print(t2)

s = '9:2:4'
s2 = datetime.datetime.strptime(s, '%H:%M:%S').strftime('%H:%M:%S')
print type(s2)
print s2

