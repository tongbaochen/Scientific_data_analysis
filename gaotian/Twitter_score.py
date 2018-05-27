import pymongo
from nltk import tokenize
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# mongodb服务的地址和端口号
mongo_url = "127.0.0.1:27017"

# 连接到mongodb，如果参数不填，默认为“localhost:27017”
client = pymongo.MongoClient(mongo_url)

#连接到数据库
DATABASE = "CNIC_BigData"
db = client[DATABASE]

#连接到集合(表)
COLLECTION = "test2"
db_coll = db[COLLECTION ]

posts = db.test2
for post in posts.find({},{'_id':0,'text':1,'location':1,'date_inserted':1}):
    analyzer = SentimentIntensityAnalyzer()
    paragraph1 = post['text']
    paragraph2 = post['location']
    paragraph3 = post['date_inserted']
    sentence_list = tokenize.sent_tokenize(paragraph1)
    paragraphSentiments = 0.0
    for sentence in sentence_list:
        vs = analyzer.polarity_scores(sentence)
        print("{:-<69} {}".format(sentence, str(vs["compound"])))
        paragraphSentiments += vs["compound"]
    print("AVERAGE SENTIMENT FOR PARAGRAPH: \t" + str(round(paragraphSentiments / len(sentence_list), 4)) + '\n' + paragraph2 + '   ' + paragraph3)
    print("-"*60)

















#def print_stats(mine):
    #print( "MIC", mine.mic())

    #lists = [posts.post()]
#for list in lists:
    #print(list)
#df = pd.DataFrame(list)
#result = df.groupby(['location'])
#result.mean()print(result)
#print(df)

    #tweets_dic_by_location = defaultdict(list)

#for td in tweets_dic:
   #tweets_dic_by_location[td['location']].append(td)

#for l in tweets_dic_by_location['San Francisco']:
    #print(l)


#for location, items in groupby(tweets_dic, key=itemgetter('location')):
    #print(location)
    #for i in items:
        #print(' ', i)

