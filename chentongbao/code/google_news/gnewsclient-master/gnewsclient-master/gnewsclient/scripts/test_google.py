from gnewsclient import gnewsclient
import json
import pymongo
import newspaper
import hashlib
import pandas as pd
'''
https://newspaper.readthedocs.io/en/latest/
https://anaconda.org/conda-forge/newspaper3k
https://github.com/nikhilkumarsingh/gnewsclient/blob/master/gnewsclient/gnewsclient.py
'''
#load countries data for all_countries.txt,return a []
client = gnewsclient()
R_contents = []
# google_paper = newspaper.build('https://www.google.com/search?q=china&source=lnms&tbm=nws&sa=X&ved=0ahUKEwjWoKH4gf7aAhUK5LwKHcMHAXIQ_AUICigB&biw=1366&bih=631')
# google_paper = newspaper.build('http://cnn.com')
# print (google_paper.size())
#
# for article in google_paper.articles:
#     print(article.url)
#
# cbs_paper = newspaper.build('http://cbs.com', memoize_articles=False)
# print (cbs_paper.size())

# article = newspaper.Article('https://www.google.com/search?q=china&source=lnms&tbm=nws&sa=X&ved=0ahUKEwjWoKH4gf7aAhUK5LwKHcMHAXIQ_AUICigB&biw=1366&bih=631')
# article.download()
# article.parse()
# print(article.text)
# cnn_paper = newspaper.build('http://cnn.com')
# for article in cnn_paper.articles:
#     print(article.url)
#
# for category in cnn_paper.category_urls():
#     print(category)
#
# import newspaper
# from newspaper import news_pool
#
# slate_paper = newspaper.build('http://slate.com')
# tc_paper = newspaper.build('http://techcrunch.com')
# espn_paper = newspaper.build('http://espn.com')
#
# papers = [slate_paper, tc_paper, espn_paper]
# news_pool.set(papers, threads_per_source=2) # (3*2) = 6 threads total
# news_pool.join()
# print(slate_paper.articles[10].html)

# from lxml import html
# import requests
#
# # Send request to get the web page
# response = requests.get('https://news.google.com/news/section?cf=all&pz=1&topic=b&siidp=b458d5455b7379bd8193a061024cd11baa97&ict=ln')
#
# # Check if the request succeeded (response code 200)
# if (response.status_code == 200):
#
# #Parse the html from the webpage
#     pagehtml = html.fromstring(response.text)
#
# # search for news headlines
#     news = pagehtml.xpath('//h2[@class="esc-lead-article-title"] \
#                       /a/span[@class="titletext"]/text()')
#
# # Print each news item in a new line
#     print("\n \n".join(news))
#
# tf = open("headlines.txt", "w")
#
# tf.write("\n \n".join(news).lower())
#
# tf.close()
# # puts as lower case in text file named headlines
#
# with open('headlines.txt', 'r') as inF:
#     for line in inF:
#         if 'inflation' in line:
#              print ("\n" + "    " + line)
# searches for 'inflation' (or whatever query) and prints in indented on a new line

import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

news_url="https://news.google.com/news/rss"
Client=urlopen(news_url)
xml_page=Client.read()
Client.close()

soup_page=soup(xml_page,"xml")
news_list=soup_page.findAll("item")
# Print news title, url and publish date
for news in news_list:
  print(news.title.text)
  print(news.link.text)
  print(news.pubDate.text)
  print("-"*60)


