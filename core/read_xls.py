import xlrd
from conf.settings import *
import os

print(BASE_PATH)

def read_excel(excel_path=BASE_PATH+"/conf/case.xlsx",sheet_name="Sheet1"):
    '''
    读取excel文件内容
    :param excel_path: xlsx文件的路径
    :param sheet_name: 表格名称
    :return: k-v的列表
    '''
    workbook = xlrd.open_workbook(excel_path)

    sheet = workbook.sheet_by_name(sheet_name)
    first_row = sheet.row_values(0)

    rows_length = sheet.nrows
    all_rows = []
    rows_dict = []
    for i in range(rows_length):
        if i == 0:
            continue
        all_rows.append(sheet.row_values(i))
    for row in all_rows:
        lis = dict(zip(first_row,row))
        rows_dict.append(lis)
    return rows_dict