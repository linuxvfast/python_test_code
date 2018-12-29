'''
import os
from datetime import date
from xlrd import open_workbook,xldate_as_tuple
from xlwt import Workbook

BASE = os.path.dirname(os.path.abspath(__file__))
input_file = ''.join(BASE+'\\'+'sales_2013.xlsx')
out_file = ''.join(BASE+'\\'+'output'+'\\'+'test10.xls')
out_workbook = Workbook()
out_worksheet = out_workbook.add_sheet('all_data')
first_file = True
grep_col = 3
with open_workbook(input_file) as workbook:
    worksheet_list = workbook.sheet_names()
    data = []
    for work in worksheet_list: #遍历表格中的所有工作簿
        worksheet = workbook.sheet_by_name(work)
        if first_file: #取标题
            head = worksheet.row_values(0)
            data.append(head)
            first_file = False
        for row_index in range(1,worksheet.nrows):#取值
            cell_data = worksheet.cell_value(row_index,grep_col) #获取价格
            # print(cell_data)
            row_list = []
            if cell_data > 2000.0:  #匹配价格大于2000的行
                for col_index in range(worksheet.ncols):
                    data_cell =  worksheet.cell_value(row_index,col_index)
                    data_type =  worksheet.cell_type(row_index,col_index)
                    if data_type == 3:#转换日期类型
                        cell_value = xldate_as_tuple(data_cell,workbook.datemode)
                        cell_value = date(*cell_value[0:3]).strftime('%Y/%m/%d')
                        row_list.append(cell_value)
                    else:
                        row_list.append(data_cell)
            # print(row_list)
            if row_list:
                data.append(row_list)
    # print(data)
    for list_index,out_list in enumerate(data):
        for e_index,value in enumerate(out_list):
            out_worksheet.write(list_index,e_index,value)
out_workbook.save(out_file)



import pandas as pd
import os

BASE = os.path.dirname(os.path.abspath(__file__))
input_file = ''.join(BASE+'\\'+'sales_2013.xlsx')
out_file = ''.join(BASE+'\\'+'output'+'\\'+'test11.xls')
result = []
data_res = pd.read_excel(input_file,sheet_name=None)
for title,data in data_res.items():
    result.append(data[data['Sale Amount'].astype(float) > 2000.0])

rows = pd.concat(result,axis=0,ignore_index=True)  #垂直连接
writer = pd.ExcelWriter(out_file)
rows.to_excel(writer,sheet_name='2018_res',index=False)
writer.save()






#选择部分工作簿的行
import os
from datetime import date
from xlwt import Workbook
from xlrd import open_workbook,xldate_as_tuple

BASE = os.path.dirname(os.path.abspath(__file__))
input_file = ''.join(BASE+'\\'+'sales_2013.xlsx')
out_file = ''.join(BASE+'\\'+'output'+'\\'+'test.xls')

out_workbook = Workbook()
out_worksheet = out_workbook.add_sheet('2018_mach')
save_data = [0,1]  #表示获取第一和第二个工作簿
first_file =True    #第一个文件获取标题
sales_value = 1900.0  #需要价格大于1900的
sale_index = 3           #价格所在列的索引
with open_workbook(input_file) as workbook:
    worksheet_list = workbook.sheet_names()
    # print(worksheet_list)
    data = []
    for index in range(len(worksheet_list)):
        # print(index)
        if index in save_data:
            worksheet = workbook.sheet_by_index(index)
            if first_file: #获取文件标题
                head = worksheet.row_values(0)
                print(head)
                data.append(head)
                first_file = False
            for row_index in range(1,worksheet.nrows):
                row_list = []
                sale_value = worksheet.cell_value(row_index,sale_index)
                if sale_value > sales_value:
                    for col_index in range(worksheet.ncols):
                        cell_data = worksheet.cell_value(row_index,col_index)
                        cell_type = worksheet.cell_type(row_index,col_index)
                        if cell_type == 3:
                            data_cell = xldate_as_tuple(cell_data,workbook.datemode)
                            data_cell = date(*data_cell[0:3]).strftime('%Y/%m/%d')
                            row_list.append(data_cell)
                        else:
                            row_list.append(cell_data)
                # print(row_list)
                if row_list:
                    data.append(row_list)
        print(data)
    for list_index,out_list in enumerate(data):
        for e_index,value in enumerate(out_list):
            out_worksheet.write(list_index,e_index,value)
out_workbook.save(out_file)

'''

import os
import pandas as pd

BASE = os.path.dirname(os.path.abspath(__file__))
input_file = ''.join(BASE+'\\'+'sales_2013.xlsx')
out_file = ''.join(BASE+'\\'+'output'+'\\'+'test.xls')
save_file = [0,1]
sales = 1900.0
data = pd.read_excel(input_file,sheet_name=save_file)
row_list = []
for work_name,value in data.items():
    row_list.append(value[value['Sale Amount'].astype(float) > sales])
result = pd.concat(row_list,axis=0,ignore_index=False)
writer = pd.ExcelWriter(out_file)
result.to_excel(writer,sheet_name='2015_test',index=False)
writer.save()


