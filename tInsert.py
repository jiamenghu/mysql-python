#coding=utf-8

#非封装的简单对数据库操作

from MySQLdb import *

try:
    #name=raw_input("input name:")
    conn = connect(host='192.168.1.104',port=3306,user='root',passwd='mysql',db='python1',charset='utf8')
    cursors1 = conn.cursor()

    #sql='insert into students(name) values("大乔")'
    #sql = 'update students set age=18 where name="大乔"'
    #sql='insert into students(name) values(%s)'
    #cursors1.execute(sql,[name])

    #cursors1.execute('select * from students where id=6')
    #result=cursors1.fetchone()
    #for data in result:
    #    print data

    print result
    cursors1.close()
    conn.close()
    print("OK")
except Exception,e:
    print(e.message)


