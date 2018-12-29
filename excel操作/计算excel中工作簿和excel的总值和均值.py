
import glob,os
from  xlwt import Workbook
from xlrd import open_workbook,xldate_as_tuple

BASE = os.path.dirname(os.path.abspath(__file__))
input_dir = ''.join(BASE)
out_file = ''.join(BASE+'\\'+'output'+'\\'+'test15.xls')
all_workbooks = glob.glob(os.path.join(input_dir,'*.xlsx'))
out_workbook = Workbook()
out_worksheet = out_workbook.add_sheet('sum_and_avg')
sale_index = 3
data = []
head = ['workbook','worksheet','worksheet_total','worksheet_avg','workbook_total','workbook_avg']
data.append(head)

for input_file in all_workbooks:
    with open_workbook(input_file) as workbook:
        list_totals = [] #一个excel表中的总值列表
        list_numbers = [] #一个excel表中的行统计
        workbook_out = []
        #计算一个excel中的一个工作表的总值和均值
        for worksheet in workbook.sheets():
            total_sales = 0
            number_sales = 0  #统计一个工作簿的行数
            worksheet_list = []
            worksheet_list.append(os.path.basename(input_file)) #添加文件名
            worksheet_list.append(worksheet.name) #添加excel中的工作簿名
            # print(worksheet_list)
            for row_index in range(1,worksheet.nrows): #遍历工作簿
                try:
                    total_sales += float(str(worksheet.cell_value(row_index,sale_index)).strip('$').replace(',',''))
                    number_sales += 1.
                except:
                    total_sales += 0.
                    number_sales += 0.
            avg_sales = '%.2f'%(total_sales/number_sales) #计算平均值
            worksheet_list.append(total_sales)
            worksheet_list.append(float(avg_sales))
            # print(worksheet_list)
            list_totals.append(total_sales)
            list_numbers.append(float(number_sales))
            workbook_out.append(worksheet_list)
        # print(list_totals,list_numbers)
        # print(workbook_out)
    #计算一个表的总值和均值
    workbook_total = sum(list_totals)
    workbok_avg = sum(list_totals)/sum(list_numbers)
    for list_value in workbook_out:
        list_value.append(workbook_total)
        list_value.append(workbok_avg)
    data.extend(workbook_out)
for list_index,out_list in enumerate(data):
    # print(list_index,out_list)
    for e_index,value in enumerate(out_list):
        out_worksheet.write(list_index,e_index,value)
out_workbook.save(out_file)


