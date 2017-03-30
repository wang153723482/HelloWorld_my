#encoding=utf8

'''

元组
使用(o1,o2)或tuple()创建元组,print以后大概是这个样子  ('a',1)  【如果元组中只有一个元素，且用()创建时，一定要加一个逗号】
元组与列表类似，但没有append()、insert()等方法，因为元组一旦创建便无法修改。
相对来说元组占用空间小
函数的参数其实就是元组形式
有序，元素可重复
'''

t = ('asd','dd')
print t[0]



s  = "a,b"
ss = tuple(s.split(','))
print type(ss)
print ss
