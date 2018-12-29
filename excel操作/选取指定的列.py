'''
#使用列索引获取指定的列
import os
from datetime import date
from xlrd import open_workbook,xldate_as_tuple
from xlwt import Workbook

BASE = os.path.dirname(os.path.abspath(__file__))
input_file = ''.join(BASE+'\\'+'sales_2013.xlsx')
out_file = ''.join(BASE+'\\'+'output'+'\\'+'test8.xls')

grep_data = [1,4]  #指定获取的列
out_workbook = Workbook()
out_worksheet = out_workbook.add_sheet('grep_2018')
with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    data = []
    for row_index in range(worksheet.nrows):
        row_list = [] #保存处理完的列
        for col_index in grep_data: #通过指定的列索引获取列
            cell_value = xldate_as_tuple(row_index,col_index)
            cell_type = worksheet.cell_type(row_index,col_index)
            if cell_type == 3:
                date_cell = xldate_as_tuple(cell_value,workbook.datemode)
                date_cell = date(*date_cell[0:3]).strftime('%Y/%m/%d')
                row_list.append(cell_value)
            else:
                row_list.append(cell_value)
        data.append(row_list)
    for list_index,out_list in enumerate(data):
        for e_index,value in enumerate(out_list):
            out_worksheet.write(list_index,e_index,value)
out_workbook.save(out_file)


import pandas as pd
import os
BASE = os.path.dirname(os.path.abspath(__file__))
input_file = ''.join(BASE+'\\'+'sales_2013.xlsx')
out_file = ''.join(BASE+'\\'+'output'+'\\'+'test8.xls')

data = pd.read_excel(input_file,'january_2013')
result = data.iloc[:,[1,4]]
writer = pd.ExcelWriter(out_file)
result.to_excel(writer,sheet_name='2014_grep',index=False)
writer.save()





#通过列标题获取列

import pandas as pd
import  os
BASE = os.path.dirname(os.path.abspath(__file__))
input_file = ''.join(BASE+'\\'+'sales_2013.xlsx')
out_file = ''.join(BASE+'\\'+'output'+'\\'+'test8.xls')

data = pd.read_excel(input_file,'march_2013')
result = data.loc[:,['Customer Name','Sale Amount']]
writer = pd.ExcelWriter(out_file)
result.to_excel(writer,sheet_name='pd_2018',index=False)
writer.save()
'''

import os
from datetime import date
from xlwt import Workbook
from xlrd import open_workbook,xldate_as_tuple

BASE = os.path.dirname(os.path.abspath(__file__))
input_file = ''.join(BASE+'\\'+'sales_2013.xlsx')
out_file = ''.join(BASE+'\\'+'output'+'\\'+'test9.xls')
mach_title = ['Customer Name','Sale Amount']
out_workbook = Workbook()
out_worksheet = out_workbook.add_sheet('grep_2018')
with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('march_2013')
    header = worksheet.row_values(0)
    head_index = []
    data = [mach_title]
    for index in range(len(header)): #获取标题的序列号
        if header[index] in mach_title:
            head_index.append(index)
    # print(head_index)
    for row_index in range(1,worksheet.nrows):#通过标题的序列号获取指定的列
        row_list = []
        for col_index in head_index:
            cell_value = worksheet.cell_value(row_index,col_index)
            row_list.append(cell_value)
        data.append(row_list)
    for list_index,out_list in enumerate(data):
        for e_index,value in enumerate(out_list):
            out_worksheet.write(list_index,e_index,value)
out_workbook.save(out_file)

