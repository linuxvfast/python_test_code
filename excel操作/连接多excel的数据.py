'''
import glob,os
from datetime import date
from xlrd import open_workbook,xldate_as_tuple
from xlwt import Workbook

BASE = os.path.dirname(os.path.abspath(__file__))
input_dir = ''.join(BASE)
out_file = ''.join(BASE+'\\'+'output'+'\\'+'test.xls')
out_workbook = Workbook()
out_worksheet = out_workbook.add_sheet('all_data')
first_file = True
data = []
for input_file in glob.glob(os.path.join(input_dir,'*.xlsx')): #遍历所有的文件
    print(os.path.basename(input_file))
    with open_workbook(input_file) as workbook:
        for worksheet in workbook.sheets():#遍历excel中所有的工作簿
            # print(worksheet)
            if first_file:
                head = worksheet.row_values(0)
                data.append(head)
                first_file = False
            for row_index in range(1,worksheet.nrows):
                row_list = []
                for col_index in range(worksheet.ncols):
                    cell_value = worksheet.cell_value(row_index,col_index)
                    cell_type = worksheet.cell_type(row_index,col_index)
                    if cell_type == 3:
                        data_cell = xldate_as_tuple(cell_value,workbook.datemode)
                        data_cell = date(*data_cell[0:3]).strftime('%Y/%m/%d')
                        row_list.append(data_cell)
                    else:
                        row_list.append(cell_value)
                if row_list:
                    data.append(row_list)
for list_index,out_list in enumerate(data):
    for e_index,value in enumerate(out_list):
        out_worksheet.write(list_index,e_index,value)
out_workbook.save(out_file)
'''

import pandas as pd
import os,glob

BASE = os.path.dirname(os.path.abspath(__file__))
input_dir = ''.join(BASE)
out_file = ''.join(BASE+'\\'+'output'+'\\'+'test15.xls')
all_workbooks = glob.glob(os.path.join(input_dir,'*.xlsx'))
data = []
for workbook in all_workbooks:
    worksheet_list = pd.read_excel(workbook,sheet_name=None)
    for worksheet_name,value in worksheet_list.items():
        data.append(value)
        # print(title)
result = pd.concat(data,axis=0,ignore_index=True)
writer = pd.ExcelWriter(out_file)
result.to_excel(writer,sheet_name='all_work',index=False)
writer.save()

