import os,csv
import pymysql
BASE = os.path.dirname(os.path.abspath(__file__))
output_file = ''.join(BASE+'\\'+'output'+'\\'+'select.csv')

#conn mysql database
conn = pymysql.connect(host='192.168.10.67',port=3306,db='code',user='supp',passwd='sup123456')
cursor = conn.cursor()

#将标题写入文件
writers = csv.writer(open(output_file,'w'))
header = ['supp_name','invoice_num','part_num','cost','pur_date']
writers.writerow(header)

#查询数据写入csv
cursor.execute("select * from supps where cost > 700.0;")
rows = cursor.fetchall()

for row in rows:
    writers.writerow(row)