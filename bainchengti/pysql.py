import pymysql

db = pymysql.connect(host="127.0.0.1",user="root",db="school")

#指定游标   所有要进行执行的事务都是通过游标来进行传输，对数据库的操作
cursor = db.cursor()

#使用ececute输入需要进行数据库的操作

# cursor.execute("select * from t_students")
#调用了一次之后就不能进行二次调用了，因为之前已经创建表成功，不能进行创建多次
# cursor.execute("create table t_teacher(name char(20),t_id varchar(5),s_salary varchar(50))")
cursor.execute("insert into t_teacher values('w','5','12000')")

cursor.execute("select * from  t_teacher")
#获取查询之后的数据，用一个变量存着，传递所有已经记录好的数据库操作，记录在游标里，进行提交
date=cursor.fetchall()      
#打印输出获取的数据
print(date)
print(type(date))

for i in date:
    name=i[0]
    t_id=i[1]
    t_salary=i[2]
    #获取到每个变量中的值，打印
    print("name=%s,t_id=%s,t_salary=%s"%(name,t_id,t_salary))
#关闭游标
cursor.close()
#关闭数据库
db.close()