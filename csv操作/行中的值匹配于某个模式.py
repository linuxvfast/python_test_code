'''
import csv,sys,re
input_file = sys.argv[1]
output_file = sys.argv[2]

pattern = re.compile(r'(?P<my_pattern_group>^001-.*)',re.I)
with open(input_file,'r') as f,open(output_file,'w') as b:
    read_file = csv.reader(f)
    write_file = csv.writer(b)
    header = next(read_file)
    write_file.writerow(header)
    for row_list in read_file:
        mach_number = row_list[1]
        if pattern.search(mach_number):
            write_file.writerow(row_list)
'''

import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data = pd.read_csv(input_file)
# result = data.loc[data['Invoice Number'].str.startswith("001-"),:]
result = data.loc[data['Supplier Name'].str.endswith('Z'),:]
result.to_csv(output_file,index=False)