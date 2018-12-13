'''
#使用csv获取指定的值
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

storge_data = ['1/20/14','1/30/14']
with open(input_file,'r') as f,open(output_file,'w') as b:
    read_file = csv.reader(f)
    write_file = csv.writer(b)
    header = next(read_file)
    write_file.writerow(header)
    for row_list in read_file:
        get_date = row_list[4]
        if get_date in storge_data:
            write_file.writerow(row_list)

'''

import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]
data = pd.read_csv(input_file)
storge_data = ['1/20/14','1/30/14']
result = data.loc[data['Purchase Date'].isin(storge_data),:]
result.to_csv(output_file,index=False)