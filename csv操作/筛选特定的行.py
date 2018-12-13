'''
#行中的某个值满足某个条件
import sys,csv

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file,'r') as f,open(output_file,'w') as b:
    read_file = csv.reader(f)
    write_file = csv.writer(b)
    header = next(read_file)#获取文件头
    write_file.writerow(header)#将文件头列表写入文件
    for row_list in read_file:
        match_name = str(row_list[0]).strip()
        replace_str = str(row_list[3]).strip('$').replace(',','')
        #将Supplier Name为Supplier Z或者Cost大于600的写入文件
        if match_name == 'Supplier Z' or float(replace_str) > 600.0:
            write_file.writerow(row_list)
'''

#使用pandans匹配数据
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

read_data = pd.read_csv(input_file)
#转换成字符串替换逗号和钱符号，最后转换成浮点数
read_data['Cost'] = read_data['Cost'].str.replace(',','').str.strip('$').astype(float)
# print(read_data['Cost'])
#获取包含'Z'和Cost值大于600的
result = read_data.loc[(read_data['Supplier Name'].str.contains('Z'))|(read_data['Cost'] > 600.0),:]
result.to_csv(output_file,index=False)