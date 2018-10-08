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


def CountryName(file):
    csvHand = open(file, "r+", encoding='utf-8', errors='ignore')
    # 创建读取csv文件句柄
    readcsv = csv.reader(csvHand)
    # 存放csv中读取的数据
    mdbuffer = []
    country = []
    for row in readcsv:
        mdbuffer.append(row)
    rowNumber = len(mdbuffer)
    for row in range(1, rowNumber):
        item = mdbuffer[row]
        country.append(item[0])
    return country
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

code_dictionary = convertCountryCode('D:\\DataLab_Project\\Code\\Indicator_process\\ITU\\ISO_CODE.csv')
# Name = CountryName('D:\\DataLab_Project\\data\\open_data\\nice\\DP_LIVE_30062018105015316.csv')
filenames = getAllFile('D:\\DataLab_Project\\data\\open_data\\oecd_data')
final_country = []
code = []
path = []
for filename in filenames:
    # final_country = CountryName(filename)
    name = set(CountryName(filename))
    for e in name:
        if code_dictionary.get(e) == None:
            code.append(e)
            path.append(filename)




print (set(code))
print (len(set(code)))
print(set(path))
print(len(set(path)))

    # print(filename)
# dis_name = set(final_country)
# for e in dis_name:
#     if code_dictionary.get(e) == None:
#         print(e)
    # else:
    #     print(code_dictionary.get(e))
# print(code_dictionary.get('AUT'))

# readIntoMongo(file)
# print(len(file))