from gnewsclient import gnewsclient
import json
import pymongo
import newspaper
import hashlib
import pandas as pd
'''
Cautions:
    can just get the news of current days from google news.
related urls:
    https://newspaper.readthedocs.io/en/latest/
    https://anaconda.org/conda-forge/newspaper3k
    https://github.com/nikhilkumarsingh/gnewsclient/blob/master/gnewsclient/gnewsclient.py
'''
#load countries data for all_countries.txt,return a []
def readCountries(filePath):
    countries = []
    with open(filePath,encoding='gbk') as file:
        while 1:
            line = file.readline()
            if  line:
                countries.append(line.strip())
            else:
                break
    return countries

#MAKE CONNECTION TO MONGODB
import pymongo
from pymongo import MongoClient
client = MongoClient()
# DEFINE YOUR MONGODB DATABASE
db = client['google_news_data']
# CREATE ACCOUNTS COLLECTION (TABLE) IN YOUR DATABASE FOR TWITTER ACCOUNT-LEVEL DETAILS
country = db['country']
# CREATE AN INDEX ON THE COLLECTION TO AVOID INSERTION OF DUPLICATES
# db.country.create_index([('country', pymongo.ASCENDING)], unique=True)

# DEFINE COLLECTION (TABLE) WHERE YOU'LL INSERT THE google article
google_news = db['google_news']
# CREATE UNIQUE INDEX FOR TABLE (TO AVOID DUPLICATES)
# db.google_news.create_index([('id_', pymongo.ASCENDING)], unique=True)

###### PART VI: LOOP OVER TWITTER HANDLES & DOWNLOAD TWEETS INTO MONGODB COLLECTION ######
# IF ACCOUNTS COLLECTION IS EMPTY READ IN CSV FILE AND ADD TO MONGODB
if country.count() < 1:
    data = pd.read_table('D:/DataLab_Project/gnewsclient-master/all_country.txt')
    print(data.head())
    n = len(data.index)
    df = data.reindex(index=range(n), columns=list(data.columns) + ['Unique_ID'])
    countries = []
    for i in range(n):
        countries.append(i + 1)
    s1 = pd.Series(countries, index=range(n))
    df["Unique_ID"] = s1
    print(df.head())

    # df = pd.read_csv('accounts1.csv')
    # df = pd.read_csv('accounts4.csv')
    records = json.loads(df.T.to_json()).values()#将csv转化为json
    print ("No account data in MongoDB, attempting to insert", len(records), "records")
    try:
        country.insert_many(records)#将记录存到mongodb中的表accounts中
    except pymongo.errors.BulkWriteError as e:
        print (e, '\n')
        #pass
else:
    print ("There are already", country.count(), "records in the *country* table")

country_account = country.distinct('country')#此处handle是唯一标识
print(country_account)

client = gnewsclient()
R_contents = []
# print(client.get_config())
# fields = 'title link img'.split()
fields = 'title link'.split()

for keyword in country_account[79:]:
    client.query = keyword
    R_contents = client.get_news()
    '''{'title': "No, the war in Afghanistan isn't a hopeless stalemate - The Conversation US", 'link': 'http://theconversation.com/no-the-war-in-afghanistan-isnt-a-hopeless-stalemate-91130', 'img': 'https://t0.gstatic.com/images?q=tbn:ANd9GcR2MX5jyRM7MWMX_BJkY2hOw_c7hADknZkB5vtQUs0yyOS-VCRrB_VnuN_Mz5en2Db5vQ3WQD1s9Q'}
{'title': 'Procession, funeral planned for northern Colorado soldier killed in ... - FOX31 Denver', 'link': 'http://kdvr.com/2018/05/10/procession-funeral-planned-for-northern-colorado-soldier-killed-in-afghanistan/', 'img': 'https://t2.gstatic.com/images?q=tbn:ANd9GcS5o0KAHkUwV-bfPDXgA69-cJEB-tLPLNeAfwsxjxTLxndCfoYMbYufotOYpcLN1nshKZnf2LI'}
{'title' '''
    '''
    for i in R_contents:
        print(i)
        '''
    element = []
    for entry in R_contents:
        r = {}#创造一个字典来存储json中的每个对象
        for f in fields:
            r[f] = ""
            r['title'] = entry['title']
            r['link'] = entry['link']#指向新闻文本的链接
        article = newspaper.Article(r['link'])
        # print(article)

        article.download()
        if article.download_state == 0 or article.download_state == 1:
            continue
            # print(article)

        article.parse()
        # print(article)
        r['article_content']= article.text
        # print(r['article_content'])
        r['country'] = keyword
        # print(r['country'])
        element.append(r)

    i = 0
    for e in element:
        i = i + 1
        # r['publish_date'] = article.publish_date
        # print(article.text)#将此文本对象存入mongodb中
        # exit()
        ##### WRITE THE DATA INTO MONGODB -- LOOP OVER EACH TWEET
        t = json.dumps(e)
        # print (t)
        load_r = json.loads(t)
        # print (load_r)
        try:
            google_news.insert_one(load_r)
            print(i)
        except pymongo.errors.DuplicateKeyError as e:
            pass

            # for key in r:
            #     print(key,'values:',r[key])
            #

    print(">>>>>>>>>>")
print("successfully")



