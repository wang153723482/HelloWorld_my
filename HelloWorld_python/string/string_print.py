# encoding=utf8
from datetime import datetime

template = 'hello %s' % 'wangc'
print template

template = 'hello %s,today is %s,my age is %d' % ('wangc', '2017-01-01', 15)
print template

template = 'hello %(name)s,today is %(day)s,my age is %(age)d' % {'name': 'zhangsan', 'day': '2011-11-11', 'age': 99}
print template

temp = 'hello {0},my age is {1},now is {2}'.format('wangc', 10, datetime.now())
print temp

temp = 'hello {name},my age is {age},now is {now}'.format(now=datetime.now(), name='wangc', age=111)
print temp

temp = '{now}'.format(now=datetime.now())
print temp


temp = '{0},{1}'
line_null = ('dd','fff',)
print temp.format('x','d')