#coding=utf8
import csv
import json
import pymongo
from pymongo import MongoClient
import os
from bson.son import SON

# 建立MongoDB数据库连接
# 远程数据库端
client = MongoClient('36.26.80.184', 27017)
# 连接所需数据库,test为数据库名
db = client.bigdata_mongo
# 连接所用集合，也就是我们通常所说的表，test为表名
collection = db.indicators
'''
result = collection.aggregate([{'$match':{"Data_source": "fundforpeace"}},{'$group': {'_id': '','countries': { '$push': "$Country" }}}])
x = (list(result))
print(len(x))
y = set(x[0]['countries'])
final = []
for i in y:
    final.append(i.strip())
cou = set(final)
print(cou)
'''

'''
result = collection.aggregate([{'$match':{"Data_source": "fundforpeace"}},{'$group': {'_id': '','countries': { '$push': "$indicators" }}}])
x = (list(result))
y = (x[0]['countries'])
# print(y)
final = []
for i in y:
    for i in i.keys():
        final.append(i.strip())
cou = set(final)
print(cou)
'''
def findCountry(query,arg):
    result = collection.aggregate(query)
    x = (list(result))
    print(len(x))
    y = set(x[0]['arg'])
    final = []
    for i in y:
        final.append(i.strip())
    cou = set(final)
    return cou

def findIndicators(query,arg):
    result = collection.aggregate(query)
    x = (list(result))
    y = (x[0]['arg'])
    final = []
    for i in y:
        for i in i.keys():
            final.append(i.strip())
    cou = set(final)
    return cou

query1 = [{'$match':{"Data_source": "fundforpeace"}},{'$group': {'_id': '','arg': { '$push': "$Country" }}}]
query2 = [{'$match':{"Data_source": "fundforpeace"}},{'$group': {'_id': '','arg': { '$push': "$indicators" }}}]
query3 = [{'$match':{"Data_source": "fundforpeace"}},{'$group': {'_id': '','arg': { '$push': "$Year" }}}]

query4 = [{'$match':{"Data_source": "ITU"}},{'$group': {'_id': '','arg': { '$push': "$Country" }}}]
query5 = [{'$match':{"Data_source": "ITU"}},{'$group': {'_id': '','arg': { '$push': "$indicators" }}}]
query6 = [{'$match':{"Data_source": "ITU"}},{'$group': {'_id': '','arg': { '$push': "$Year" }}}]

query7 = [{'$match':{"Data_source": "OECD"}},{'$group': {'_id': '','arg': { '$push': "$Country" }}}]
query8 = [{'$match':{"Data_source": "OECD"}},{'$group': {'_id': '','arg': { '$push': "$indicators" }}}]
query9 = [{'$match':{"Data_source": "OECD"}},{'$group': {'_id': '','arg': { '$push': "$Year" }}}]

# query = [query7,query8,query9]
# for item in query:
#     indi = (findCountry(item,arg='arg'))
#     print(indi)
'''
print(findCountry(query7,arg='arg'))
print(findIndicators(query8,arg='arg'))
print(findCountry(query9,arg='arg'))
'''

query10 = [{'$match':{"Data_source": "WHO"}},{'$group': {'_id': '','arg': { '$push': "$Country" }}}]
query11 = [{'$match':{"Data_source": "WHO"}},{'$group': {'_id': '','arg': { '$push': "$indicators" }}}]
query12 = [{'$match':{"Data_source": "WHO"}},{'$group': {'_id': '','arg': { '$push': "$Year" }}}]

'''
print(findCountry(query10,arg='arg'))
print(findIndicators(query11,arg='arg'))
print(findCountry(query12,arg='arg'))
'''

query13 = [{'$match':{"Data_source": "WDI"}},{'$group': {'_id': '','arg': { '$push': "$Country" }}}]
query14 = [{'$match':{"Data_source": "WDI"}},{'$group': {'_id': '','arg': { '$push': "$indicators" }}}]
query15 = [{'$match':{"Data_source": "WDI"}},{'$group': {'_id': '','arg': { '$push': "$Year" }}}]


print(findCountry(query13,arg='arg'))
print(findIndicators(query14,arg='arg'))
print(findCountry(query15,arg='arg'))





