f = open('test','r')
for l in f:
    if l.replace('\n','')=='': # 跳过空行
        continue
    print(l)