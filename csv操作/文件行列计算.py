import os,csv
import glob
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
input_path = BASE_DIR

count = 0
for input_file in glob.glob(os.path.join(input_path,'test*')):
    row_count = 1
    with open(input_file,'r',newline='') as f: #去除换行符newline
        readfile = csv.reader(f)
        header = next(readfile)
        for row in readfile:
            row_count += 1
    print('{0!s}:\t{1:d} row \t {2:d} col'.format(os.path.basename(input_file),row_count,len(header)))
    count += 1
print('Number of files:{0:d}'.format(count))