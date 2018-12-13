
'''
#通过列索引值取指定的列
import csv,sys

input_file = sys.argv[1]
output_file = sys.argv[2]
keep_col = [0,3]
with open(input_file,'r') as f,open(output_file,'w') as b:
    read_file = csv.reader(f)
    write_file = csv.writer(b)
    for row_list in read_file:
        list_keep = []
        for index in keep_col:
            list_keep.append(row_list[index])
        write_file.writerow(list_keep)


import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
data = pd.read_csv(input_file)
result = data.iloc[:,[0,3]]
result.to_csv(output_file,index=False) #索引为False表示不写入索引值
'''


''' 
#通过列标题取指定的列
import csv,sys
input_file = sys.argv[1]
output_file = sys.argv[2]
title_col = ['Supplier Name','Purchase Date']

with open(input_file,'r') as f,open(output_file,'w') as b:
    read_file = csv.reader(f)
    write_file = csv.writer(b)
    reader = next(read_file)
    title_col_index = []
    for index in range(len(reader)):
        if reader[index] in title_col:
            title_col_index.append(index)
    write_file.writerow(title_col)
    for row_list  in read_file:
        # print(row_list)
        out_list = []
        for index in title_col_index:
            out_list.append(row_list[index])
        write_file.writerow(out_list)
'''

#使用pandas通过标题获取指定的列
import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

data = pd.read_csv(input_file)
result = data.loc[['Supplier Name','Purchase Date'],:]
result.to_csv(output_file,index=False)
