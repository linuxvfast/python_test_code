import os
import sys
import argparse

try:
    from io import StringIO
except:
    import StringIO

import struct
import json
import csv
from pprint import pprint
def import_data(import_file):
    mask = '9s15s6s'
    data = []
    with open(import_file,'r') as f:
        for line in f:
            fields = struct.Struct(mask).unpack_from(bytes(line, encoding='utf-8'))
            data.append(list([f.strip() for f in fields]))
    return data

def write_data(data,export_format):
    if export_format == 'csv':
        return write_csv(data)
    elif export_format == 'json':
        return write_json(data)
    elif export_format == 'xlsx':
        return write_xlsx(data)
    else:
        raise Exception('Illegal format defined')

def write_csv(data):
    f = StringIO()
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)
    return f.getvalue()

def write_json(data):
    j = json.dumps([line.decode() for i in data for line in i]) #因为data读取出来是bytes，所以需要变成字符串
    return j

def write_xlsx(data):   #xlsx功能读取没有实现
    '''
    :param data: 需要写入的数据
    :return: 处理后的值
    '''
    from xlwt import Workbook
    book = Workbook()
    sheet1 = book.add_sheet('student')
    row = 0
    for line in data:
        col = 0
        for c in line:
            sheet1.write(row,col,c)
            col += 1
        row += 1
        if row >65535:
            print(sys.stderr,'limit rows in one sheet 65535')
            break
    f = StringIO()
    book.save(f)
    return f.getvalue()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('import_file',help='path to a fixed-width data file.')
    parser.add_argument('export_format',help='export format:json,csv,xlsx.')
    args = parser.parse_args()

    if args.import_file is None:
        print(sys.stderr,'you must specify path to import from.')
        sys.exit(1)

    if args.export_format not in ('csv','json','xlsx'):
        print(sys.stderr,'you must provide valid export file format.')
        sys.exit(1)

    if not os.path.isfile(args.import_file):
        print(sys.stderr,'given path is not a file:%s'%args.import_file)
        sys.exit(1)

    data = import_data(args.import_file)

    pprint(write_data(data,args.export_format))

