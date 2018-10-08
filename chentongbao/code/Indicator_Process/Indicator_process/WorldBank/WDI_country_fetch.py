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


def country_fectch1(mdbuffer):
    # head_row = mdbuffer[0]
    # columnNumber = len(mdbuffer[0])
    # 获取mdbuffer中的元素个数
    rowNumber = len(mdbuffer)
    # 读取列表中的元素
    counrty_set = []
    for row in range(1, rowNumber):
        item = mdbuffer[row]
        counrty_set.append(item[0].strip())
    return set(counrty_set)

def indicator_fetch_WDI(mdbuffer):
    # head_row = mdbuffer[0]
    # columnNumber = len(mdbuffer[0])
    # 获取mdbuffer中的元素个数
    rowNumber = len(mdbuffer)
    # 读取列表中的元素
    indicator_set = []
    for row in range(1, rowNumber):
        item = mdbuffer[row]
        indicator_set.append(item[2].strip())
    return set(indicator_set)

def indicator_fetch(filenames):
    # 存放csv中读取的数据
    indicators = []
    for filename in filenames:
        try:
            csvHand = open(filename, "r+", encoding='utf-8', errors='ignore')
            # 创建读取csv文件句柄
            readcsv = csv.reader(csvHand)
  #跳过第一行
            next(readcsv)
            indicators.append((next(readcsv)[1]).strip())
        except Exception as e:
            print("Read Excel  error:", e)
        finally:
            # 关闭csv文件
            print(filename + "finished")
            csvHand.close()
    return indicators

def country_fetch(filenames):
    # 存放csv中读取的数据
    countryName = []
    for filename in filenames:
        try:
            csvHand = open(filename, "r+", encoding='utf-8', errors='ignore')
            # 创建读取csv文件句柄
            readcsv = csv.reader(csvHand)
  #跳过第一行
            next(readcsv)
            if code_dictionary.get(next(readcsv)[0]) == None:
                # print('---' + item[0])
                countryName.append(next(readcsv)[0].strip())
                # propertyJson["Country"] = item[0]
            else:
                countryName.append(code_dictionary.get(next(readcsv)[0]).strip()).strip()
                # propertyJson["Country"] = code_dictionary.get(item[0])

        except Exception as e:
            print("Read Excel  error:", e)
        finally:
            # 关闭csv文件
            print(filename + "finished")
            csvHand.close()
    return set(countryName)

code_dictionary = convertCountryCode('D:\\DataLab_Project\\Code\\Indicator_process\\ITU\\ISO_CODE.csv')
# result = indicator_fetch(getAllFile('D:\\DataLab_Project\\data\\open_data\\oecd_test'))
# result = country_fectch1(readInToArray(getAllFile('D:\\DataLab_Project\\data\\open_data\\worldbank\\worldbank1')))
result = indicator_fetch_WDI(readInToArray(getAllFile('D:\\DataLab_Project\\data\\open_data\\worldbank\\worldbank')))
print(result)
# readIntoMongo(file)
# print(len(file))