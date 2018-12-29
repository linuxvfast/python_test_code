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
grep_col = ['Customer Name','Sale Amount']
with open_workbook(input_file) as workbook:
    worksheet_list = workbook.sheet_names()
    data = []
    grep_index = [] #保存指定列的索引
    for work in worksheet_list: #遍历表格中的所有工作簿
        worksheet = workbook.sheet_by_name(work)
        if first_file: #取标题
            head = worksheet.row_values(0)
            data.append(grep_col)
            for index in range(len(head)): #获取列索引
                if head[index] in grep_col:
                    grep_index.append(index)
            first_file = False

        for row_index in range(1,worksheet.nrows):#取值
            row_list = [] #存储指定列的值
            for col_index in grep_index:
                cell_data = worksheet.cell_value(row_index,col_index) #获取价格
                row_list.append(cell_data)
            if row_list:
                data.append(row_list)
    # print(data)
    for list_index,out_list in enumerate(data):
        for e_index,value in enumerate(out_list):
            out_worksheet.write(list_index,e_index,value)
out_workbook.save(out_file)


'''
import pandas as pd
import os

BASE = os.path.dirname(os.path.abspath(__file__))
input_file = ''.join(BASE+'\\'+'sales_2013.xlsx')
out_file = ''.join(BASE+'\\'+'output'+'\\'+'test11.xls')
result = []
data_res = pd.read_excel(input_file,sheet_name=None)
for title,data in data_res.items():
    result.append(data.loc[:,['Customer Name','Sale Amount']])

rows = pd.concat(result,axis=0,ignore_index=True)  #垂直连接
writer = pd.ExcelWriter(out_file)
rows.to_excel(writer,sheet_name='2018_res',index=False)
writer.save()
'''