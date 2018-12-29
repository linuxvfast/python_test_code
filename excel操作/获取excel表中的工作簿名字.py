import sys,os
from xlrd import open_workbook

BASE = os.path.dirname(os.path.abspath(__file__))
input_file = ''.join(BASE+'\\'+'sales_2013.xlsx')
# print(input_file)

workbook = open_workbook(input_file)
#获取工作簿的数量
print('Number of worksheets:',workbook.nsheets)
for worksheet in workbook.sheets():
    print('worksheet name:',worksheet.name,"\trows:",worksheet.nrows,"\tcols:",worksheet.ncols)
