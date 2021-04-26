__author__ = 'wangchao'

import sqlite3

cx = sqlite3.connect("ziru.db")

cu = cx.cursor()

# cu.execute("create table catalog (id integer primary key,pid integer,name varchar(10) UNIQUE,nickname text '')")


for t in[(0,10,'abc','Yu'),(1,20,'cba','Xu')]:
    cx.execute("insert into catalog values (?,?,?,?)", t)
cx.commit()

for t in [(100,0),(200,1)]:
    cx.execute('update catalog set pid=? where id =?',t)
cx.commit()



# sql = 'create table ziru_house(room_id,room_name,price,mianji,chaoxiang,huxing,louceng,jiaotong,url,quyu,shangquan,create_date)'
# cx.execute(sql)
# cx.commit()

cu.execute("select * from catalog") 
print cu.fetchall()