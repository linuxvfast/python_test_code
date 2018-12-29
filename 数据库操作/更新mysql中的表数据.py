import os,csv,pymysql

BASE = os.path.dirname(os.path.abspath(__file__))
input_file = ''.join(BASE+'\\'+'update.csv')

#连接数据库
conn = pymysql.connect(host='192.168.10.67',port=3306,db='code',user='supp',passwd='sup123456')
cursor = conn.cursor()

#从csv读取数据更新mysql表数据
# read_data = csv.reader(open(input_file,'r'))
# header = next(read_data)
# for row in read_data:
#     data = []
#     for index in range(len(header)):
#         data.append(str(row[index]).strip())
#     print(data)
#     cursor.execute("update supps set cost=%s,purchase_data=%s where supplier_name=%s;",data)
# conn.commit()

#查询修改完的数据
cursor.execute("select * from supps")
rows = cursor.fetchall()

for row in rows:
    data = []
    for index in range(len(row)):
        data.append(str(row[index]))
    print(data)