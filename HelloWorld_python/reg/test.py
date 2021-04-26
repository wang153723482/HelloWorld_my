#encoding=utf8
import re


#正则替换
#1正则，2新的字符串，3需要进行替换的字符串
s = 'sdf34df3k3k3k'
s= re.subn(r'[0-9]','*',s)
print s



s = '23skldjfl12'

print re.findall('^[0-9]{1,2}',s)[0]



st = '12'
st = int(st)
print type(st)

a = 1
a =+ 1 
print a

s = '原始报文日志插入成功，数量为：1,花费时间为：144'
print re.findall('[0-9]*$',s)[0]




# 将正则表达式编译成Pattern对象
pattern = re.compile(r'hello')

# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
match = pattern.match('hello world!')

if match:
    # 使用Match获得分组信息
    print match.group()

    ### 输出 ###
    # hello

import random

s = random.randint(1, 5400)
print s

import time

# time.sleep(3)

import requests

# s  = requests.get('http://192.168.103.72:8080')
# print s.status_code
# print s.content

import urllib2

s = urllib2.urlopen('http://192.168.103.72:8080')
print s.read()
