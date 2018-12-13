'''
import csv,sys
input_file = sys.argv[1]
output_file = sys.argv[2]
count = 0
#newline='' 去除文件中的换行符
with open(input_file,'r',newline='') as f,open(output_file,'w',newline='') as b:
    readfile = csv.reader(f)
    writefile = csv.writer(b)
    for row in readfile:
        if count >=3 and count <= 15:
            writefile.writerow([value.strip() for value in row],)
        count += 1
'''

import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
input_file = ''.join(BASE_DIR + '\\' + 'supplier_data.csv')
output_file = ''.join(BASE_DIR + '\\' + 'output' + '\\' + 'duqu.csv')

data = pd.read_csv(input_file,header=None)
#丢弃不需要的行
data = data.drop([0,1,2,16,17,18])

#选取第0行作为列索引
data.columns = data.iloc[0]
#重新生成索引
data = data.reindex(data.index.drop(3))
data.to_csv(output_file,index=False)

