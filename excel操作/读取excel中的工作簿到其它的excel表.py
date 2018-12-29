'''
import os
from xlrd import open_workbook
from xlwt import Workbook

BASE = os.path.dirname(os.path.abspath(__file__))
input_file = ''.join(BASE+'\\'+'sales_2013.xlsx')
output_file = ''.join(BASE+'\\'+'output'+'\\'+'test.xls')

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('2013_out')  #添加excel工作簿
with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    for row_index in range(worksheet.nrows):
        print('row_index',row_index)
        for col_index in range(worksheet.ncols):
            print('col_index',col_index)
            output_worksheet.write(row_index,col_index,worksheet.cell_value(row_index,col_index))
output_workbook.save(output_file)
 '''

'''
#修正上面的日期显示数据问题
import os
from datetime import date
from xlrd import open_workbook,xldate_as_tuple
from xlwt import Workbook

BASE = os.path.dirname(os.path.abspath(__file__))
input_file = ''.join(BASE+'\\'+'sales_2013.xlsx')
output_file = ''.join(BASE+'\\'+'output'+'\\'+'test2.xls')

out_workbook =Workbook()
out_worksheet = out_workbook.add_sheet('out_2013_2')
with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    for row_index in range(worksheet.nrows):
        row_list = []
        for col_index in range(worksheet.ncols):
            if worksheet.cell_type(row_index,col_index) == 3: #单元格类型为3表示这个单元格包含日期数据
                date_cell = xldate_as_tuple(worksheet.cell_value(row_index,col_index),workbook.datemode)
                date_cell = date(*date_cell[0:3]).strftime('%Y/%m/%d')#取前三个元素传递给date函数
                row_list.append(date_cell)
                # print(row_list)
                out_worksheet.write(row_index,col_index,date_cell)
            else:
                non_cell = worksheet.cell_value(row_index,col_index)
                # print('non_cell',non_cell)
                row_list.append(non_cell)
                out_worksheet.write(row_index,col_index,non_cell)
        # print(row_list)
out_workbook.save(output_file)
'''

#使用pandas读取excel
import  pandas as pd
import os

BASE = os.path.dirname(os.path.abspath(__file__))
input_file = ''.join(BASE+'\\'+'sales_2013.xlsx')
output_file = ''.join(BASE+'\\'+'output'+'\\'+'test3.xls')

data = pd.read_excel(input_file,sheet_name='january_2013')
writer = pd.ExcelWriter(output_file)
data.to_excel(writer,sheet_name='out_2013',index=False)
writer.save()