#coding=utf8
import csv
import json
import pymongo
from pymongo import MongoClient
import os

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
'''
files = ["D:/DataLab_Project/data/open_data/worldbank/worldbank/HNP_StatsData.csv",
"D:/DataLab_Project/data/open_data/worldbank/worldbank/Gender_StatsData.csv",
"D:/DataLab_Project/data/open_data/worldbank/worldbank/WDIData.csv",
    "D:/DataLab_Project/data/open_data/worldbank/worldbank/EdStatsData.csv"

         ]
         '''

# files = ["D:/DataLab_Project/data/open_data/worldbank/worldbank/HNP_StatsData.csv"]
# files = ["D:/DataLab_Project/data/open_data/worldbank/worldbank/EdStatsData.csv"]

def readInToArray(filenames):
    # 存放csv中读取的数据
    mdbuffer = []
    try:
        #用来存放json数据的列表
        dataDic=[]
        dataresult = []
        #存放csv中读取的数据
        mdbuffer=[]
        #打开csv文件，设置读的权限
        # csvHand=open(filename,"r")
        csvHand = open(filenames,"r+",encoding = 'utf-8', errors = 'ignore')
        #创建读取csv文件句柄
        readcsv=csv.reader(csvHand)
        #把csv的数据读取到mdbuffer中
        for row in readcsv:
            mdbuffer.append(row)
            # print(row)
        #保存文件
    except Exception as e:
        print ("Read Excel  error:",e)
    finally:
        #关闭csv文件
        print (filenames + "finished")
        csvHand.close()
    return mdbuffer
'''
 def fileprocess(filename):
        with open(filename,"r+",encoding='utf-8',errors='ignore') as f:
            reader = csv.reader(f)
            head_row = next(reader)
            print(head_row)
            # for row in reader:
                # print(reader.line_num,row)
            return head_row
'''

def readIntoMongo(mdbuffer):
    # 建立MongoDB数据库连接
    # 远程数据库端
    client = MongoClient('36.26.80.184', 27017)
    # 连接所需数据库,test为数据库名
    db = client.bigdata
    # 连接所用集合，也就是我们通常所说的表，test为表名
    collection = db.indicators
    # collection = db.WDI
    '''
    client = MongoClient('10.0.86.60',27017)
    # 实际运行
    #连接所需数据库,test为数据库名
    db=client.bigdata_mongo
    #连接所用集合，也就是我们通常所说的表，test为表名
    collection=db.indicator2
    '''
    try:
        # 获取mdbuffer中的元素个数
        rowNumber = len(mdbuffer)
        head_row = mdbuffer[0]
        columnNumber = len(mdbuffer[0])

        for row in range(1,rowNumber):
            item = mdbuffer[row]
            for column in range(4,columnNumber):
                print(column)
                # 设置json数据的属性值
                propertyJson = {}
                temp = {}
                #indicator的索引
                if item[column] == "":
                    temp[item[2].replace(".", "_")] = ''
                else:
                    temp[item[2].replace(".", "_")] = float(item[column])

                propertyJson["Country"] = item[0]
                propertyJson["Year"] = head_row[column]
                propertyJson["Data_source"] = 'WDI'
                propertyJson[head_row[1]] = item[1]
                # 获得{indicators{a:,b:c:}}
                propertyJson["indicators"] = temp
                print(propertyJson)
                #propertyJson即是获取得到的一个document记录
                # self.dataresult.append(propertyJson.copy())
                # dataresuldt = self.dataresult
                #转化为json格式，再写入到mongo 中
                t = json.dumps(propertyJson)
                loaded_entry = json.loads(t)
                try:
                    collection.insert_one(loaded_entry)
                except pymongo.errors.DuplicateKeyError as e:
                    pass

    except Exception as e:
        print("Reading Data TO Dic Error:", e)


files = getAllFile("D:/DataLab_Project/data/open_data/worldbank/worldbank3")
for item in files:
    readIntoMongo(readInToArray(item))
    print('finished' + item)
