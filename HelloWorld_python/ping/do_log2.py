# encoding=utf8
import numpy as np

f = open('ping.new.log', 'r')

sum = 0.0
pro = 1.0
num = 0
t_list = []
for a in f:
    num = num + 1
    this_n = float(a[a.index('time=') + 5:a.index(' ms')])
    t_list.append(this_n)
    sum = sum + this_n
    # pro = pro * this_n    # 可能是超出最大范围无法计算
    # if num == 300:
    #     break

t_list.sort()
print (t_list[int(num * 0.7)])

print(sum)
print(pro)
print(num)

print(sum / num)
# print(pro ** (1.0/num))


print 69*7.5+10*15.5