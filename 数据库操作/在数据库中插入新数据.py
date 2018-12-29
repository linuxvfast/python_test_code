import csv,sqlite3
import os

BASE = os.path.dirname(os.path.abspath(__file__))
# print(BASE)
input_file = ''.join(BASE+'\\'+'first.csv')

#持久化数据库，可以是'my_databse.db'或者'C:\Python36\source\data_analysis\my_database.db'
conn =sqlite3.connect('C:\Python36\source\data_analysis\my_database.db')
c = conn.cursor()  #创建光标
create_table = '''create table if not exists test
                    (test_name varchar(20),
                    invoice_number varchar(20),
                    part_number varchar(20),
                    cost float,
                    puchase_date data);'''
c.execute(create_table)
conn.commit()

#读取csv文件，向表中插入数据
read_data = csv.reader(open(input_file,'r'),delimiter=',')
header = next(read_data)
for row in read_data:
    data = []
    for col_index in range(len(header)):
        data.append(row[col_index])
    # print(data)
    c.execute("insert into test values(?,?,?,?,?);",data)
conn.commit()
print('')


#查询
out = c.execute("select * from test")
rows = out.fetchall()
for row in rows:
    output = []
    for col_index in range(len(row)):
        output.append(str(row[col_index]))
    print(output)
