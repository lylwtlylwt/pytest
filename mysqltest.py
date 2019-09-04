import pymysql
#创建数据库连接
db = pymysql.connect('127.0.0.1','pymysql','Py_123','pymysql')
#定义游标
cursor = db.cursor()
#定义查询sql
sql = 'select * from t_stock'
#查询数据
cursor.execute(sql)
#获取所有查询结果集，获取一条fetchone()
s_data = cursor.fetchall()
#打印结果,数据是一个数组，第1个下标表示行，第2个下标表示列。如s_data[0][1]表示第一行记录的第2个字段
print(s_data[0],[1])
#定义插入sql
sql1 = "insert into l_stock(tcode,tname,tdate)values('300399','京天利','2014-10-01')"
#捕捉异常
try:
    #执行sql
    cursor.execute(sql1)
    #提交数据
    db.commit();
    print("插入成功！")
except:
    #回滚数据
    db.rollback()
    print("插入失败！")
#关闭游标
cursor.close()
#关闭数据库连接
db.close()
