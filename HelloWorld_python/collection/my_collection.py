# encoding=utf8

from collections import namedtuple
from collections import defaultdict
from collections import OrderedDict
import timeit

# 定义一个有名字的tuple，并且通过属性访问其中的值
Point = namedtuple('point', ['x', 'y'])
p = Point(1, 2)
print p.x
print type(p)

# 定义一个有默认值的dict
d = defaultdict(int)  # 定义一个默认值为0的字典
d['min_m'] = 1

print d['min_m']
print d['max_m']

d2 = defaultdict(lambda: '_')  # 定义一个默认值为_的dict
print d2['sss']

# 定义一个有序的dict

od1 = OrderedDict()
od1['name'] = 'wangc'
od1['age'] = 15
od1['address'] = 'bj'
print od1

od2 = {}
od2['name'] = 'wangc'
od2['age'] = 15
od2['address'] = 'bj'
print od2
