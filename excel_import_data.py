
import xlrd

filename = 'example.xlsx'
wb = xlrd.open_workbook(filename=filename)
ws = wb.sheet_by_name('student')
dataset = []

#通过双for循环获取student表单中的内容
for line in range(ws.nrows): #ws.nrows获取总共的行数
    col = []
    for c in range(ws.ncols):#ws.ncols获取总共的列数
        col.append(ws.cell(line,c).value)
    dataset.append(col)

#格式化形式输出结果
from pprint import pprint
pprint(dataset)
