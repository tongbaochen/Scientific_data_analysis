### 数据收集
**version: 20180505
### 背景
   数据库存储——以NoSQL为主，使用docker（一个容器，新量级的虚拟机），并建立mongodb集群，数据都存在mongodb的cluster中，此外，使用mysql来  存储元数据（如表的信息等)；
### 工作内容： 	
  - x,抓取公开的开放数据，如联合国的统计数据，铁路公里数、国民教育程度，国民生产总值等（用于建立模型来预测幸福度），并存在mongodb中；
  - Y，抓取Twitter，网上的文本数据，google news等，（可调api ，需翻墙，网页形式返回数据（按时间，国家，关键字等搜索）），返回网页后对其进行解析;   （进行汇总，后期用于情感分析，分析幸福感随时间的变化等）
  - 熟悉jupyter notebook，以后用于进行数据分析的主要环境，可让用户端访问运行。
### 实现方式
   使用scrapy,redis,mongodb,graphite实现的一个分布式网络爬虫,底层存储mongodb集群,分布式使用redis实现，从目标网址中爬取响应的数据存储到mongodb中。github上开源项目：https://github.com/gnemoug/distribute_crawler    
   - Eight data sources and the numbers of collected indicators
        - http://data.worldbank.org/indicator
        - http://www.ilo.org/ilostat
        - https://data.oecd.org/
        - http://stat.wto.org/Home/WSDBHome.aspx
        - http://www.who.int/gho/en/
        - http://fsi.fundforpeace.org/
        - http://www.itu.int/en/ITU-D/Statistics/
        - http://www.transparency.org/
### 任务清单
  - [x] 基本的爬虫工作原理
  - [x] python爬虫基础知识：XPath与lxml库
  - [ ] 基本的http抓取工具，scrapy框架
  - [ ] Bloom Filter: Bloom Filters by Example
  - [online] 爬取worldbank数据
  - [x] 爬取twitter数据             ## 备注：20+万用户的推文，暂存本地mongodb
  - [online] 爬取google news数据    ## 备注： google news api已经停用，无法直接调用api,需另寻方法爬取数据
  - [ ] 学习分布式爬虫的概念（学会怎样维护一个所有集群机器能够有效分享的分布式队列）如：简单的实现是python-rq: https://github.com/nvie/rq
  - [ ] rq和Scrapy的结合：darkrho/scrapy-redis · GitHub
  - [ ] 后续处理，网页析取(grangier/python-goose · GitHub)，存储(Mongodb)
### 参考资料  
   - python爬虫基础知识：XPath与lxml库
      https://blog.csdn.net/flyingfishmark/article/details/51272480
   - Python开发简单爬虫
      http://www.imooc.com/learn/563
   - scrapy框架初识：用scrapy爬豆瓣 https://blog.csdn.net/flyingfishmark/article/details/51316159
   - python网络数据采集 作者: [美] 米切尔 出版社: 人民邮电出版社
   - http://www.runoob.com/mongodb/mongodb-query.html
   - http://social-metrics.org/downloading-tweets-by-a-list-of-users-take3/
   - https://github.com/nikhilkumarsingh/gnewsclient
   - https://www.cnblogs.com/zhonghuasong/p/5976003.html
   - https://github.com/nikhilkumarsingh/gnewsclient/blob/master/CLI.md
   
   
