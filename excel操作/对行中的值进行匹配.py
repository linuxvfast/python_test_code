'''
import re,os
from datetime import date
from xlwt import Workbook
from xlrd import open_workbook,xldate_as_tuple

BASE = os.path.dirname(os.path.abspath(__file__))
input_file = ''.join(BASE+'\\'+'sales_2013.xlsx')
out_file = ''.join(BASE+'\\'+'output'+'\\'+'test6.xls')

out_workbook = Workbook()
out_worksheet = out_workbook.add_sheet('check_2014')
mach = re.compile(r'(?P<my_mach>^J.*)') #正则匹配包含J开头的行
mach_index = 1
with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    data = []
    header = worksheet.row_values(0)
    data.append(header)
    for row_index in range(1,worksheet.nrows):#排除标题的行遍历
        row_list = []
        #匹配字符串
        if mach.search(worksheet.cell_value(row_index,mach_index)):
            for col_index in range(worksheet.ncols):
                cell_value = worksheet.cell_value(row_index,col_index)
                cell_type = worksheet.cell_type(row_index,col_index)
                if cell_type == 3: #处理日期
                    date_cell = xldate_as_tuple(cell_value,workbook.datemode)
                    date_cell = date(*date_cell[0:3]).strftime('%Y/%m/%d')
                    row_list.append(date_cell)
                else:
                    row_list.append(cell_value)
        if row_list:
            data.append(row_list)
    for list_index,out_list in enumerate(data):
        for e_index,value in enumerate(out_list):
            out_worksheet.write(list_index,e_index,value)
out_workbook.save(out_file)
'''


#pandas匹配数据
import pandas as pd
import os

BASE = os.path.dirname(os.path.abspath(__file__))
input_file = ''.join(BASE+'\\'+'sales_2013.xlsx')
out_file = ''.join(BASE+'\\'+'output'+'\\'+'test7.xls')

data = pd.read_excel(input_file,'january_2013',index_col=None)
result = data[data['Customer Name'].str.startswith('J')]
writer = pd.ExcelWriter(out_file)
result.to_excel(writer,sheet_name='2014_res',index=False)
writer.save()