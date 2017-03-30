import uuid

print uuid.uuid1()
print str(uuid.uuid1()).replace('-','')

f = open('d://xx.csv','w')
for i in range(1000):
    f.write( str(uuid.uuid1()).replace('-','')+',\n' )
    
f.close()