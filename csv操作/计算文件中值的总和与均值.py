'''
import csv,glob,os
BASE = os.path.dirname(os.path.abspath(__file__))
input_path = BASE
output_file = ''.join(BASE+'\\'+'output'+'\\'+'duqu.csv')
out_head_list = ['file_name','total_sales','average_sales']
b = open(output_file,'a',newline='')
writefile = csv.writer(b)
writefile.writerow(out_head_list)
for input_file in glob.glob(os.path.join(input_path,'test*')):
    with open(input_file,'r',newline='') as f:
        readfile = csv.reader(f)
        total = 0.0   #记录总值
        sales_number_count = 0.0 #统计值的个数
        output_list = []
        header = next(readfile)  #去掉没用的头部

        #统计每个文件的值
        for row in readfile:
            sales = row[3]
            total += float(str(sales).strip('$').replace(',',''))
            sales_number_count += 1

        avg_value = '{0:.2f}'.format(total/ sales_number_count)
        output_list.append(total)
        output_list.append(sales_number_count)
        output_list.append(avg_value)
        writefile.writerow(output_list)
b.close()
'''


import pandas as pd
import glob,os
BASE = os.path.dirname(os.path.abspath(__file__))
input_path = BASE
output_file = ''.join(BASE+'\\'+'output'+'\\'+'duqu.csv')
out_head_list = ['file_name','total_sales','average_sales']
result = []
for input_file in glob.glob(os.path.join(input_path,'test*')):
    data = pd.read_csv(input_file,index_col=None)

    #通过列表生成式将数值转换为float，再将浮点数转换成dataframe计算总和和均值
    total = pd.DataFrame([float(str(value).strip('$').replace(',','')) for value in data.loc[:,'Sale Amount']]).sum()
    avg = pd.DataFrame([float(str(value).strip('$').replace(',','')) for value in data.loc[:,'Sale Amount']]).mean()
    res = {'file_name':os.path.basename(input_file),
           'total_sales':total,
           'avg_sales':avg}
    result.append(pd.DataFrame(res,columns=['file_name','total_sales','avg_sales']))
#因为都有标题行，需要垂直连接组成一个文本，保留一个标题
data_conn = pd.concat(result,axis=0,ignore_index=True)
data_conn.to_csv(output_file,index=False)