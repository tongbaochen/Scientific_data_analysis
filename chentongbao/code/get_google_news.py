from newsapi import NewsApiClient
import json
import pymongo
import hashlib
import pandas as pd
from gnewsclient import gnewsclient
import newspaper

# Init  you should set your own api_key param here!
newsapi = NewsApiClient(api_key='')

# /v2/everything
def get_aricles(keyword,sources,start_time,end_time):
    all_articles = newsapi.get_everything(q=keyword,
                                          sources=sources,
                                          # domains='bbc.co.uk,techcrunch.com,google.com',
                                          from_param=start_time,
                                          to=end_time,
                                          language='en',
                                          sort_by='relevancy',
                                          page_size=50
                                          )
    return  all_articles  #return a dic of containing all of the articles from google nes with keywords

#return countries data for all_countries.txt,return a []
def readCountries(filePath):
    countries = []
    #all_coutry.txt
    with open(filePath,encoding='gbk') as file:
        while 1:
            line = file.readline()
            if  line:
                countries.append(line.strip())
            else:
                break
    return countries

'''read the json object into dict '''

def readFromjsonToDic(R_contents,keyword):
    fields = "title link article_content country publishedAt".split()
    element = []
    for entry in R_contents:
        if type(entry) != type({}):
            print("entry is not a dictionary")
            print(type(entry))
            print(entry)
        r = {}
        for f in fields:
            r['title'] = entry['title']
            r['link'] = entry['url']
            # r['description'] = entry['description']
            r['country'] = keyword
            r['publishedAt'] = entry['publishedAt']
        article = newspaper.Article(r['link'])
        article.download()
        if article.download_state == 0 or article.download_state == 1:
            continue
            # print(article)
        article.parse()
        r['article_content'] = article.text
        element.append(r)

    return element

'''##### WRITE THE DATA INTO MONGODB -- LOOP OVER EACH google news'''
#pass in a list of
def writeIntoDb(article):
    for e in article:
        # i = i + 1
        t = json.dumps(e)
        load_r = json.loads(t)
        try:
            google_news.insert_one(load_r)
            # print(i)
        except pymongo.errors.DuplicateKeyError as e:
            pass


#MAKE CONNECTION TO MONGODB
import pymongo
from pymongo import MongoClient
client_mongo = MongoClient()
# DEFINE YOUR MONGODB DATABASE
db = client_mongo['google_news']
# CREATE ACCOUNTS COLLECTION (TABLE) IN YOUR DATABASE FOR TWITTER ACCOUNT-LEVEL DETAILS
# country = db['country']
# CREATE AN INDEX ON THE COLLECTION TO AVOID INSERTION OF DUPLICATES
# db.country.create_index([('country', pymongo.ASCENDING)], unique=True)
# DEFINE COLLECTION (TABLE) WHERE YOU'LL INSERT THE google article

google_news = db['news']
countries = readCountries('D:/Code/GitHub/project/Scientific_data_analysis/chentongbao/all_country.txt')
#set the time scale you want to get from.
date = [
        '2018-02-14', '2018-02-15', '2018-02-16','2018-02-17','2018-02-18','2018-02-19','2018-02-20','2018-02-21','2018-02-22','2018-02-23','2018-02-24',
        '2018-02-25','2018-02-26','2018-02-27', '2018-02-28',
        '2018-03-01','2018-03-02','2018-03-03','2018-03-04','2018-03-05','2018-03-06','2018-03-07','2018-03-08','2018-03-09','2018-03-10','2018-03-11','2018-03-12',
        '2018-03-13','2018-03-14', '2018-03-15', '2018-03-16','2018-03-17','2018-03-18','2018-03-19','2018-03-20','2018-03-21','2018-03-22','2018-03-23','2018-03-24',
        '2018-03-25','2018-03-26','2018-03-27', '2018-03-28','2018-03-29','2018-03-30','2018-03-31',
        '2018-04-01','2018-04-02','2018-04-03','2018-04-04','2018-04-05','2018-04-06','2018-04-07','2018-04-08','2018-04-09','2018-04-10','2018-04-11','2018-04-12',
        '2018-04-13','2018-04-14', '2018-04-15', '2018-04-16','2018-04-17','2018-04-18','2018-04-19','2018-04-20','2018-04-21','2018-04-22','2018-04-23','2018-04-24',
        '2018-04-25','2018-04-26','2018-04-27', '2018-04-28','2018-04-29','2018-04-30',
        '2018-04-01','2018-04-02','2018-04-03','2018-04-04','2018-04-05','2018-04-06','2018-04-07','2018-04-08','2018-04-09','2018-04-10','2018-04-11','2018-04-12',
        '2018-04-13','2018-04-14', '2018-04-15', '2018-04-16','2018-04-17','2018-04-18','2018-04-19','2018-04-20','2018-04-21','2018-04-22','2018-04-23','2018-04-24',
        '2018-04-25','2018-04-26','2018-04-27', '2018-04-28','2018-04-29','2018-04-30',
        '2018-05-01','2018-05-02','2018-05-03','2018-05-04','2018-05-05','2018-05-06','2018-05-07','2018-05-08','2018-05-09','2018-05-10','2018-05-11','2018-05-12',
        ]
for datetime in date:
    print (datetime)
    for nation in countries[:]:
        print(nation)
        dic = {}
        try:
            all_articles = get_aricles(keyword=nation,sources='google news',start_time=datetime,end_time=datetime)
        except Exception:
            continue
        r = {}
        j = 0
        for i in all_articles:
            r[j] = all_articles[i]
            j = j + 1
        dic = r[2]#[{'source': {'id': None, 'name': 'Thelancet.com'}, 'author': 'The Lancet', 'title': '[Editorial] Cancer drugs in China: affordability and creativity', 'description': 'Cancer is a major public healt
        article = []
        article = readFromjsonToDic(R_contents=dic,keyword=nation)
        writeIntoDb(article)
    print("finish" + datetime)
	
	




