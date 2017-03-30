#encoding=GBK


def main():
    cardid_map = {}
    file = open('d:/result.csv')
    i = 0
    for line in file:
        i+=1
        idcard = line[0:18]
        if idcard in cardid_map:
            cardid_map[idcard] += 1
        else:
            cardid_map[idcard] = 1
            
    file.close()
    
    for o in cardid_map:
        print o.value
    print i

if '__main__'==__name__:
    # main()
    print 1
    l = []
    l.append(1)
    l.append(1)
    l.append('s')
    
    ll = list()
    ll.append(22)
    ll.append(22)
    ll.append(list())
    print l
    print ll
    
    
    print '============='
    d = dict()
    d['name']='wangchao'
    d['age']=26
    
    d = {12:'bj'}
    d['name']='wangchao2'
    d['age']=262
    
    print d
    for dd in d:
        print d[dd]
    
    print '============='
    
    s = set()
    ss = {'sdf','sdf',12}
    print ss
    s.add('as')
    s.add(1)
    s.add(1)
    
    for a in s:
        print a
    
    print s

    print '============='
    
    t = tuple('a')
    t = ('a','a',1)
    print t[0]
    
    aa = ''
    print type(aa)
    
