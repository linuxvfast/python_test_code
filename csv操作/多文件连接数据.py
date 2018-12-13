import csv,glob,os

BASE = os.path.dirname(os.path.abspath(__file__))
input_path = BASE
output_file = ''.join(BASE+'\\'+'output'+'\\'+'duqu.csv')
''' 
first_file = True
for input_file in glob.glob(os.path.join(input_path,'test*')):
    print(os.path.basename(input_file))
    with open(input_file,'r',newline='') as f,open(output_file,'a',newline='') as b:
        readfile = csv.reader(f)
        writefile = csv.writer(b)
        if first_file:
            for row in readfile:
                writefile.writerow(row)
            first_file = False
        else:
            header = next(readfile)
            for row in readfile:
                writefile.writerow(row)
'''

import pandas as pd
all_file = glob.glob(os.path.join(input_path,'test*'))
result_data = []
for file in all_file:
    date = pd.read_csv(file,index_col=None)
    result_data.append(date)

#axis控制连接的方向，垂直连接用0，平行连接用1
data_conn = pd.concat(result_data,axis=0,ignore_index=True)
data_conn.to_csv(output_file,index=False)




