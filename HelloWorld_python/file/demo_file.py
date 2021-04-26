#encoding=utf8

f = open('test','r')
for l in f:
    if l.replace('\n','')=='': # 跳过空行
        continue
    print(l)
    
f2 = open('a.log','a')   #r 只读 w 只写 a 追加    wb 二进制写
f2.write('asdf\n')
f2.close()