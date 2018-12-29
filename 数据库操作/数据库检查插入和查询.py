import sqlite3

#创建sqlite3内存数据库
#创建带有4个属性的sales表
conn = sqlite3.connect(':memory:') #在内存创建数据库不持久化
query = '''create table sales
            (customer VARCHAR(20),
            product VARCHAR(40),
            amount FLOAT,
            date DATE);'''
conn.execute(query)
conn.commit()

#在表中插入数据
data = [('Richard Lucas','Notepad',2.50,'2014-01-02'),
        ('Jenny Kim','Binder',4.15,'2014-01-15'),
        ('Svetlana Crow','Printer',155.75,'2014-02-03'),
        ('Stephen Randolph','Computer',679.40,'2014-02-20')]
statement = "INSERT INTO sales VALUES(?,?,?,?)"  #问号是占位符，避免sql注入攻击
conn.executemany(statement,data)
conn.commit()

#查询sales表
cursor = conn.execute("SELECT * FROM sales")
rows = cursor.fetchall() #取出所有的行
# print(rows)

#计算行的数量
row_cont = 0
for row in rows:
    print(rows)
    row_cont += 1
print('number_rows:%d'%(row_cont))
