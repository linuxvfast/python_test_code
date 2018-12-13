import os,csv
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
input_file = ''.join(BASE_DIR + '\\' + 'test.csv')
output_file = ''.join(BASE_DIR + '\\' + 'output' + '\\' + 'duqu.csv')
''' 
with open(input_file,'r')as f,open(output_file,'w',newline='') as b:
    readfile = csv.reader(f)
    writefile = csv.writer(b)
    head_list = ['Supplier Name','Invoice Number','Part Number','Cost','Purchase Date']
    writefile.writerow(head_list)
    for row_list in readfile:
        writefile.writerow(row_list)
'''

import pandas as pd
head_list = ['Supplier Name', 'Invoice Number', 'Part Number', 'Cost', 'Purchase Date']
data = pd.read_csv(input_file,header=None,names=head_list)
data.to_csv(output_file,index=False)