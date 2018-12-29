import csv,os,pymysql
from datetime import datetime,date

BASE = os.path.dirname(os.path.abspath(__file__))
input_file = ''.join(BASE+'\\'+'supp_data.csv')

#连接数据库
conn = pymysql.connect(host='192.168.10.67', port=3306, user='supp', passwd='sup123456', db='code')
cursor = conn.cursor() #创建游标

#创建表
# cursor.execute("create table if not exists res (supplier_name varchar(20), invoice_num varchar(20), part_num varchar(20), cost float, purchase_data date);")
# conn.commit()



#向表中插入数据
# read_data = csv.reader(open(input_file,'r'))
# header = next(read_data)
#
# for row in read_data:
#     data = []
#     for index in range(len(header)):
#         if index < 4:
#             data.append(str(row[index]).strip('$').replace(',',''))
#         else:
#             get_data = datetime.date(datetime.strptime(str(row[index]),'%m/%d/%y'))
#             get_data = get_data.strftime('%Y-%m-%d')
#             data.append(get_data)
    # print(data)
    # cursor.execute("insert into supps values(%s,%s,%s,%s,%s);",data)
    # conn.execute()
# conn.commit()
# print("")

#c查询数据

cursor.execute("select * from supps")
rows = cursor.fetchall()

for row in rows:
    row_list = []
    for index in range(len(row)):
        row_list.append(str(row[index]))
    print(row_list)
