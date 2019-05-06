#coding=utf-8
from fenzhuang import MysqlHelper

#修改数据库

# name = raw_input("请输入学生姓名")
# id1 = raw_input("请输入学生编号")

# sql ='update students set name=%s where id=%s'
# params=[name, id1]
#
# sqlhelper = MysqlHelper('192.168.1.104',3306,'python1','root','mysql')
# sqlhelper.cud(sql,params)

sql = 'select id,name from students where id<6'
sqlhelper = MysqlHelper('192.168.1.104',3306,'python1','root','mysql')
result = sqlhelper.all(sql)
print result