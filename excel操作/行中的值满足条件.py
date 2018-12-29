'''
import os
from datetime import date
from xlrd import open_workbook,xldate_as_tuple
from xlwt import Workbook

BASE = os.path.dirname(os.path.abspath(__file__))
input_file = ''.join(BASE+'\\'+'sales_2013.xlsx')
out_file = ''.join(BASE+'\\'+'output'+'\\'+'test.xls')
out_workbook = Workbook()
out_worksheet = out_workbook.add_sheet('2014_out')
sale_count = 3  #声明日期的类型（表示单元格包含日期）
with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    data = []  #存放整理完的行列表
    header = worksheet.row_values(0)#读取标题
    data.append(header)
    # print(data)
    for row_index in range(1,worksheet.nrows):
        row_list = [] #存放处理格式化日期的列表
        sale_value = worksheet.cell_value(row_index,sale_count) #获取所有的价格
        # print(sale_value)
        if sale_value > 1400.0:
            for col_index in range(worksheet.ncols):
                # print(col_index)
                cell_value = worksheet.cell_value(row_index,col_index) #获取每行的值
                cell_type = worksheet.cell_type(row_index,col_index) #获取值对应的类型
                # print(cell_value,cell_type)
                if cell_type == 3: #处理包含日期的单元格
                    cell_date = xldate_as_tuple(cell_value,workbook.datemode)
                    cell_date = date(*cell_date[0:3]).strftime('%Y/%m/%d')
                    row_list.append(cell_date)
                else:
                    row_list.append(cell_value)
        if row_list:
            data.append(row_list)
            # print(data)
    for list_index,out_list in enumerate(data):
        for el_index,value in enumerate(out_list):
            out_worksheet.write(list_index,el_index,value)
out_workbook.save(out_file)
'''

#pandas获取满足条件的行
import pandas as pd
import os
BASE = os.path.dirname(os.path.abspath(__file__))
input_file = ''.join(BASE+'\\'+'sales_2013.xlsx')
out_file = ''.join(BASE+'\\'+'output'+'\\'+'test.xls')
data = pd.read_excel(input_file,'january_2013',index_col=None)
result = data[data['Sale Amount'].astype(float) < 1400.0]
writer = pd.ExcelWriter(out_file)
result.to_excel(writer,sheet_name='2014_out',index=False)
writer.save()
