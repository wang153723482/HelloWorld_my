# encoding=gbk
__author__ = 'wangchao'

import MySQLdb

conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='test')

cur = conn.cursor()

# �������ݱ�
cur.execute("create table students(id int ,name varchar(20),class varchar(30),age varchar(10))")

# ����һ������
# cur.execute("insert into students values('2','Tom','3 year 2 class','9')")

# cur.execute("insert into students(age) values (?)", ('a2',))

# �޸Ĳ�ѯ����������
# cur.execute("update students set class='3 year 1 class' where name = 'Tom'")

# ɾ����ѯ����������
# cur.execute("delete from students where age='9'")


cur.execute('select * from students')

# print cur.fetchall()


for i in cur.fetchall():
    print '==========='
    print i[0]

cur.close()
conn.commit()
conn.close()
