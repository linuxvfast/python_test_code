'''
#基本的复制操作
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file,'r') as f,open(output_file,'w') as b:
    header = f.readline()
    header = header.strip()
    header_list = header.split(',')
    print(header_list)
    b.write(','.join(map(str,header_list))+'\n')
    for row in f:
        row = row.strip()
        row_list = row.split(',')
        print(row_list)
        b.write(','.join(map(str,row_list))+'\n')
'''

''' 
#pandas复制文件
import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

read_data = pd.read_csv(input_file)
print(read_data)
read_data.to_csv(output_file,index=False)
'''


#csv复制文件
import csv,sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file,'r') as f,open(output_file,'w') as b:
    read_data = csv.reader(f,delimiter=',')#delimiter默认的分隔符，默认是逗号
    write_file = csv.writer(b,delimiter=',')
    for row_list in read_data:
        print(row_list)
        write_file.writerow(row_list) #writerow将每行的列表值输入文件中

