#encoding=utf8

m = {}
# m = dict() #两种创建方式
m['1101']='zhangsan'
m['1102']='lisi'
m['1103']='wangwu'

print m

#循环

for (k,v) in  m.items():
    print k,v
    
s = '	R44261ba8a77b4379aee63b01d55025a'
print s.replace('	','')