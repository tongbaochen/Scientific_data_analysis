#coding=utf8
import csv
import json
import pymongo
from pymongo import MongoClient

import  os
#处理type8

# 遍历filepath下所有文件，包括子目录
def getAllFile(filepath):
    filenames = []
    files = os.listdir(filepath)
    for fi in files:
        fi_d = os.path.join(filepath,fi)
        if os.path.isdir(fi_d):
            getAllFile(fi_d)
        else:
            filenames.append(fi_d)
            # print(os.path.join(filepath,fi_d))
    return filenames
# 把csv文件的数据以每行作为一个元素存储到到mdbuffer[]数组中

def readInToArray(filenames):
    # 存放csv中读取的数据
    mdbuffer = []
    flag = 0
    for filename in filenames:
        try:
            # 打开csv文件，设置读的权限
            csvHand = open(filename, "r+", encoding='utf-8', errors='ignore')
            # 创建读取csv文件句柄
            readcsv = csv.reader(csvHand)
            # 把csv的数据读取到mdbuffer中
            if flag == 0 :
                for row in readcsv:
                    mdbuffer.append(row)
                    # print(row)
            else:
                # print(next(readcsv))
                #跳过表中的第一行
                next(readcsv)
                for row in readcsv:
                    mdbuffer.append(row)
        except Exception as e:
            print("Read Excel  error:", e)
        finally:
            # 关闭csv文件
            print(filename + "finished")
            csvHand.close()
        flag = 1
    return mdbuffer

def readIntoMongo(mdbuffer):
    # 建立MongoDB数据库连接
    # 远程数据库端
    client = MongoClient('36.26.80.184', 27017)
    # 连接所需数据库,test为数据库名
    db = client.bigdata_mongo
    # 连接所用集合，也就是我们通常所说的表，test为表名
    collection = db.indicators
    '''
      # 远程数据库端
    client = MongoClient('10.0.86.60', 27017)
    # 连接所需数据库,test为数据库名
    db = client.bigdata_mongo
    # 连接所用集合，也就是我们通常所说的表，test为表名
    collection = db.indicator

    '''
    '''
    #本地数据库测试
    client = MongoClient('localhost', 27017)
    # 连接所需数据库,test为数据库名
    db = client.bigdata_mongo
    # 连接所用集合，也就是我们通常所说的表，test为表名
    collection = db.test
'''
    #对数据表进行处理

    #获取第一行
    head_row1 = mdbuffer[0]
    #获取第二行
    head_row = mdbuffer[1]
    #获得列数
    columnNumber = len(mdbuffer[0])
    # 获取mdbuffer中的元素个数，即数据表的行数
    rowNumber = len(mdbuffer)
    # 处理首行数据
    kind = head_row1[3]
    counrty_set = []
    time = []
    time_set = []


    #跳过第一行
    '''
    for row in range(1, rowNumber):
        temp = {}
        item = mdbuffer[row]
        counrty.append(item[0])
        time.append(item[5])
    counrty_set = set(counrty)
    time_set = set(time)
    '''
    for row in range(2, rowNumber):
        # propertyJson用来设置每个document的json数据属性格式
        propertyJson = {}
        #temp用来设置每个indicators属性
        temp = {}
        #获取得一行数据
        item = mdbuffer[row]
        propertyJson["Country"] = item[0]
        propertyJson["Year"] = item[2]
        propertyJson["Data_source"] = 'WHO'
        for column in range(3,columnNumber):
            if column < len(item):
                if item[column].strip() == 'No data':  # 将缺省的数据填充为''空.
                    temp[kind + head_row[column].replace('.', '_')] = ''
                elif item[column] == 'Elimination verified':  # 将缺省的数据填充为''空.
                    temp[kind + head_row[column].replace('.', '_')] = ''
                elif item[column] == 'No PC required':  # 将缺省的数据填充为''空.
                    temp[kind + head_row[column].replace('.', '_')] = ''
                elif item[column] == 'Not applicable':  # 将缺省的数据填充为''空.
                    temp[kind + head_row[column].replace('.', '_')] = ''
                elif item[column] == '..':  # 将缺省的数据填充为''空.
                    temp[kind + head_row[column].replace('.', '_')] = ''
                elif item[column] == '':
                    temp[kind + head_row[column].replace('.', '_')] = ''
                elif item[column] == 'Not available':
                    temp[kind + head_row[column].replace('.', '_')] = ''
                elif item[column].strip() == '[  -  ]':
                    temp[kind + head_row[column].replace('.', '_')] = ''
                elif item[column].strip() == '[  -  1]':
                    temp[kind + head_row[column].replace('.', '_')] = ''
                elif item[column].strip() == '-':
                    temp[kind + head_row[column].replace('.', '_')] = ''
                else:  # 将字符串转化为float型数值
                    if item[column].find('[') != -1:
                        # print((item[column][:(item[column].find('[')-1)]).replace(' ',''))
                        temp[kind + head_row[column].replace('.', '_')] = float(
                            (item[column][:(item[column].find('[') - 1)]).replace(' ', ''))
                    # elif item[column].strip().find('[') == 0:
                    #     temp[head_row[column]] = ''
                    else:
                        temp[kind + head_row[column].replace('.', '_')] = float((item[column]).replace(' ', ''))

        propertyJson["indicators"] = temp
        print(propertyJson)
        #转换成josn的形式以便插入mongodb
        t = json.dumps(propertyJson)
        loaded_entry = json.loads(t)
        try:
            collection.insert_one(loaded_entry)
        except pymongo.errors.DuplicateKeyError as e:
            pass


files = getAllFile('D:\\DataLab_Project\\data\\open_data\\whoi\\type8')

for item in files:
    path = []
    path.append(item)
    file = readInToArray(path)
    readIntoMongo(file)
print(len(file))