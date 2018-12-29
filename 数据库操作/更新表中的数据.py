import csv,os,sqlite3
BASE = os.path.dirname(os.path.abspath(__file__))
print(BASE)
input_file = ''.join(BASE+'\\'+'two.csv')
# conn = sqlite3.connect('C:\Python36\source\data_analysis\date3.db')
conn = sqlite3.connect(':memory:')

query = '''create table if not exists sales
            (customer varchar(20),
            product varchar(40),
            amount flost,
            date date);'''
conn.execute(query)
conn.commit()

#向表中插入数据
dat = [('Richard Lucas','Notepad',2.50,'2014-01-02'),
       ('Jenny Kim','Binder',4.15,'2014-01-15'),
       ('Svetlana Crow','Prinder',155.75,'2014-02-03'),
       ('Stephen Randolph','Computer',679.40,'2014-02-20')]
# for tuple in dat:
    # print(tuple)
statement = "insert into sales values(?,?,?,?)"
conn.executemany(statement,dat)
conn.commit()


#读取csv更新指定的行
read_data = csv.reader(open(input_file,'r'))
header = next(read_data)

for row in read_data:
    data = []
    for col_index in range(len(header)):
        data.append(row[col_index])
    print(data)
    ##占位符的位置要和input_file文件中的字段位置一致才能替换
    conn.execute("update sales set amount=?,customer=? where date=?;",data)
conn.commit()

#查询
cursor = conn.execute("select * from sales")
rows = cursor.fetchall()
# print(rows)
for row in rows:
    out = []
    for col_index in range(len(row)):
        out.append(str(row[col_index]))
    print(out)