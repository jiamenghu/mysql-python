#coding=utf-8

#登录数据库
from fenzhuang import MysqlHelper
from hashlib import sha1

name =raw_input("请输入用户名：")
pwd = raw_input("请输入密码：")

s1=sha1()
s1.update(pwd)
pwd2 = s1.hexdigest()

sql = 'select passwd from users where name =%s'
helper = MysqlHelper('192.168.1.104',3306,'python1','root','mysql')
result = helper.all(sql,[name]) #(('123'),)
if len(result) == 0:
    print("用户名错误")
elif result[0][0] == pwd2:
#print(result)

    print("登录成功")
else:
    print("密码错误")