#coding=utf8
import csv
import json
import pymongo
from pymongo import MongoClient
import pprint

import  os

def MongoTest():
    # 建立MongoDB数据库连接
    # 远程数据库端

    client = MongoClient('10.0.86.60', 27017)
    # 连接所需数据库,test为数据库名
    db = client.bigdata_mongo
    # 连接所用集合，也就是我们通常所说的表，test为表名
    collection = db.indicator
    '''
    #本地数据库测试
    client = MongoClient('localhost', 27017)
    # 连接所需数据库,test为数据库名
    db = client.bigdata_mongo
    # 连接所用集合，test为表名
    collection = db.test
'''
    for element in collection.find():
        try:
            # print(element)
            # dd = json.loads(element)
            for key in element['indicators']:
                print(element['indicators'][key])
                element['indicators'][key] = convert(element['indicators'][key])
                # print(key)

                # print(convert(element['indicators'][key]))
            collection.save({'_id':element['_id'],
                            'indicators':element['indicators'],
                                   });
        except Exception as e:
            print(print(element))


def convert(orinal):
    if orinal == 'No data':  # 将缺省的数据填充为''空.
        return ''
    elif orinal == 'Elimination verified':  # 将缺省的数据填充为''空.
        return ''
    elif orinal == '':  # 将缺省的数据填充为''空.
        return ''
    elif orinal == 'No PC required':  # 将缺省的数据填充为''空.
        return ''
    elif orinal == 'Not applicable':  # 将缺省的数据填充为''空.
        return ''
    elif orinal == '..':  # 将缺省的数据填充为''空.
        return ''
    elif orinal == 'Not available':  # 将缺省的数据填充为''空.
        return ''
    elif orinal == '[  -  ]':  # 将缺省的数据填充为''空.
        return ''
    elif orinal == '[  -  1]':  # 将缺省的数据填充为''空.
        return ''
    # elif orinal == 'no':  # 将缺省的数据填充为''空.
    #     return ''
    # elif orinal == 'No':  # 将缺省的数据填充为''空.
    #     return ''
    elif orinal == 'NaN':  # 将缺省的数据填充为''空.
        return ''
    else:
        return float(orinal)


MongoTest()