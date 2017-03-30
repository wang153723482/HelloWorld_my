import cx_Oracle

db=cx_Oracle.connect('wang','123456','192.168.1.50:1521/mydb')

print db.version


cr=db.cursor()

sql = 'xxxxxxxxxxxx'
cr.execute(sql)

cr.close()

db.commit()

db.close()