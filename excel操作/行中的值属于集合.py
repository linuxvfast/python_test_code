'''
import os
from datetime import date
from xlrd import open_workbook,xldate_as_tuple
from xlwt import Workbook

BASE = os.path.dirname(os.path.abspath(__file__))
input_file = ''.join(BASE+'\\'+'sales_2013.xlsx')
out_file = ''.join(BASE+'\\'+'output'+'\\'+'test4.xls')

out_workbook = Workbook()
out_worksheet = out_workbook.add_sheet('grep_2014')
grep_date = ['2013/01/24','2013/01/31']
grep_index = 4
with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    data = []
    header = worksheet.row_values(0)
    data.append(header)
    for row_index in range(1,worksheet.nrows):
        #转换日期格式
        cell_data = xldate_as_tuple(worksheet.cell_value(row_index,grep_index),workbook.datemode)
        cell_data = date(*cell_data[0:3]).strftime('%Y/%m/%d')
        row_list = []
        if cell_data in grep_date:  #匹配日期
            for col_index in range(worksheet.ncols):
                # print(col_index)
                cell_value = worksheet.cell_value(row_index,col_index)
                cell_type = worksheet.cell_type(row_index,col_index)
                if cell_type == 3: #处理日期格式
                    date_cell = xldate_as_tuple(cell_value,workbook.datemode)
                    date_cell =date(*date_cell[0:3]).strftime('%Y/%m/%d')
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

#pandas获取数据
import pandas as pd
import os

BASE = os.path.dirname(os.path.abspath(__file__))
input_file = ''.join(BASE+'\\'+'sales_2013.xlsx')
out_file = ''.join(BASE+'\\'+'output'+'\\'+'test5.xls')
data = pd.read_excel(input_file,'january_2013',index_col=None)
grep_data = ['2013/01/24','2013/01/31']
result = data[data['Purchase Date'].isin(grep_data)] #判断日期是否在grep_data
writer = pd.ExcelWriter(out_file)
result.to_excel(writer,sheet_name='2014_out',index=False)
writer.save()

