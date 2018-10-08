#coding=utf8
import csv
import json
import pymongo
from pymongo import MongoClient
import pandas as pd


import  os

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


#返回国家代码（3位）转化为国家全称的查询字典
def convertCountryCode(filePath):

    csvHand = open(filePath, "r+", encoding='utf-8', errors='ignore')
    # 创建读取csv文件句柄
    readcsv = csv.reader(csvHand)
    # 存放csv中读取的数据
    mdbuffer = []
    relation = {}
    for row in readcsv:
        mdbuffer.append(row)
    rowNumber = len(mdbuffer)
    for row in range(1, rowNumber):
        item = mdbuffer[row]
        relation[item[2]] = item[0]
    # name = relation.get(code)
    return relation

def readInToArray(filenames):
    # 存放csv中读取的数据
    mdbuffer = []
    flag = 0
    for filename in filenames:
        try:
            # 用来存放json数据的列表
            dataDic = []
            dataresult = []
            # 打开csv文件，设置读的权限
            # csvHand=open(filename,"r")

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
    db = client.bigdata
    # 连接所用集合，也就是我们通常所说的表，test为表名
    collection = db.indicator
    # collection = db.test

    # client = MongoClient('10.0.86.60', 27017)
    # # 实际运行
    #
    # # 连接所需数据库,test为数据库名
    # db = client.bigdata_mongo
    # # 连接所用集合，也就是我们通常所说的表，test为表名
    # collection = db.indicator3


    #获取第一行
    head_row = mdbuffer[0]
    columnNumber = len(mdbuffer[0])
    # 获取mdbuffer中的元素个数
    rowNumber = len(mdbuffer)
    # 读取列表中的元素
    counrty = []
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
    for row in range(1, rowNumber):
    # for row in range(168476, rowNumber):

        # 设置json数据的属性值
        propertyJson = {}
        temp = {}
        item = mdbuffer[row]
        if code_dictionary.get(item[0]) == None:
            print('---'+item[0])
            propertyJson["Country"] = item[0]
        else:
            propertyJson["Country"] = code_dictionary.get(item[0])
        # propertyJson["Country"] = code_dictionary.get(item[0])
        propertyJson["Year"] = item[5].strip()
        propertyJson["Data_source"] = 'OECD'
        # propertyJson[head_row[column]] = item[column]
        for column in [2,3,4]:
            propertyJson[head_row[column]] = item[column]
        if item[6] == "":
            temp[item[1]] = ''
        else:
            temp[item[1]] = float(item[6])
        propertyJson["indicators"] = temp
        # print(temp)
        print(propertyJson)
        t = json.dumps(propertyJson)
        loaded_entry = json.loads(t)
        try:
            collection.insert_one(loaded_entry)
        except pymongo.errors.DuplicateKeyError as e:
            pass





code_dictionary = convertCountryCode('D:\\DataLab_Project\\Code\\Indicator_process\\ITU\\ISO_CODE.csv')
file = readInToArray(getAllFile('D:\\DataLab_Project\\data\\open_data\\oecd_data7'))
readIntoMongo(file)
print(len(file))