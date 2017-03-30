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