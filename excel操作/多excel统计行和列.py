
import glob,os
from xlrd import open_workbook

BASE = os.path.dirname(os.path.abspath(__file__))
input_dir = ''.join(BASE)
print(input_dir)
workbook_count = 0
for input_file in glob.glob(os.path.join(input_dir,'*.xlsx')):
    workbook = open_workbook(input_file)
    print('workbook:%s' % os.path.basename(input_file)) #获取文件名
    print('number of worsheets:%d'% workbook.nsheets) #获取excel中工作簿的个数
    for worksheet in workbook.sheets(): #遍历所有的工作簿，打印工作簿的名字，行，列数
        print('worksheet name:',worksheet.name,'\tRows:',worksheet.nrows,'\tCol:',worksheet.ncols)
    workbook_count += 1
print('Number of excel workbooks:%d'%(workbook_count))  #统计excel中工作簿的个数


