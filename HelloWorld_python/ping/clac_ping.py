#encoding=utf8

total = 0.0
total2 = 0.0
num = 0
f = open('ping.201701061025.log','r')
for a in f:
    num = num + 1
    if num==1:
        continue
    
    a = a[a.index('time=')+5:len(a)-3]
    total += float(a)
    total2 += float(a)**2
mean = total/num
var = total2/num - mean**2

print( '平均：'+str(total / num))
print( '平均差：'+str(var))