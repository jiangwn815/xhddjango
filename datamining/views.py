from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
import os
import copy
import csv,chardet,codecs
from .models import User
from openpyxl import Workbook, load_workbook


def index(request):
    return render(request, 'datacleaning/index.html')


# 打开某个csv文件并写入传入的sheet
def mergexl(file,ws):
    with open(file) as csvfile:
        csvreader = csv.reader(csvfile)
        for x, row in enumerate(csvreader):
            for y, value in enumerate(row):
                ws.cell(row=x+1, column=y+1, value=value)


# 将某文件转换为UTF-8编码
def toutf8(fn):
    newfile = ""
    if os.path.isfile(fn) and fn.endswith('.csv') and "utf8" not in fn:
        zippath = '/'.join(fn.split(r'/')[0:-1])
        newfile = os.path.join(zippath, fn.split(r'.')[0] + "utf8.csv") # 创建带有utf8的文件名
        fncharset = chardet.detect(open(fn, "rb").read())  # 检测文件编码方式
        print("Open file:{0} Charset:{1}".format(fn, fncharset))
        if fncharset["encoding"] not in ("GB2312", "gbk"):
            return
        with open(newfile, "wb") as csvutf8:  # w模式会把已存内容全部擦掉
            csvutf8.write(codecs.BOM_UTF8)  # 开头写入BOM防止win系统乱码

        with open(newfile, "a") as csvutf8:

            csvutf8writer = csv.writer(csvutf8, dialect='excel') # 准备读取csv文件
            with codecs.open(fn, "r", encoding="gbk") as csvfile: # 以gbk解码文件
                print("WORKING ON:", fn)
                csvreader = csv.reader(csvfile)
                for row in csvreader:
                    print(row)
                    csvutf8writer.writerow(row)
    if newfile:
        return newfile


def dealxlsx(request):
    ul = {}
    field_mapping = {"mobile_no": "服务号码",
                     "user_no": "用户编号",
                     "in_time": "入网时间",
                     "out_time": "离网时间",
                     "out_type": "离网类型",
                     "user_state": "用户状态",
                     "user_state_starttime": "当前状态开始时间",
                     "user_online_time":"用户在网时间（月）",
                     "double_seller": "双计人",
                     "brokerage_channel": "合作渠道",
                     "subscribe_plan": "租机计划",
                     "charge_plan": "资费名称",
                     "mainproduct_second": "主产品细类二级",
                     "singleproduct_sub": "单产品销售细类",
                     "seller_name": "用户发展员工",
                     "seller_channel_third": "用户发展三级部门",
                     "seller_channel_fifth": "用户发展五级部门",
                     "seller_channel_sixth": "用户发展六级部门"
                     }
    fpath = '/users/jwn/Desktop/工作文件/外呼/2017年3~11月下单妥投号码/merge.xlsx'
    print(fpath)
    wb = load_workbook(fpath)
    for sheet_name in wb.sheetnames:
        if sheet_name != "Sheet":
            print(sheet_name)
            ws = wb[sheet_name]
            users={}
            for cell in ws[1]:
                for key, field in copy.deepcopy(field_mapping).items():
                    if cell.value.endswith(field):
                        users[key] = cell.col_idx

            #print(field_mapping)
            for row in ws.iter_rows(min_row=2):
                for cell in row:
                    for key, idx in users.items():
                        if cell.col_idx == idx:
                            users[key] = cell.value
                User.objects.create(**users)
                # for cell in row:
                    # pass

    return JsonResponse(ul)


# 解压某目录下所有压缩文件
def bjdata(request):
    ul = {"utf8file":{}}
    zippath = '/users/jwn/Desktop/工作文件/外呼/2017年3~11月下单妥投号码'

    for filename in os.listdir(zippath):  # 遍历目标目录下所有文件和文件夹
        fn = os.path.join(zippath, filename)
        utf8file = toutf8(fn)  # 转化当前文件
        if utf8file:
            ul["utf8file"][utf8file.split('.')[0].split(r'/')[-1]] = utf8file

    wb = Workbook()
    for filename, filepath in ul["utf8file"].items():
        ws = wb.create_sheet(filename)  # 新建sheet
        mergexl(filepath, ws)

    wb.save(zippath+"/merge.xlsx")
    print("SHEET NAMES:", wb.sheetnames)

    return JsonResponse(ul)
