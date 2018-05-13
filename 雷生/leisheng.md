#  数据的存储与管理
##  工作进度：
1. 在ubuntu上使用docker创建apache服务器层                
2. 在docker基础上建立一个mongodb集群以及建立mysql数据库  
3. 在docker基础上搭建了基于zeppelin的mongodb服务，并进行了简单的测试

##  剩余任务：
远程数据互通

##  结构
1. Docker
2. └── test
3.     ├── mysqldata  数据库文件夹
4.     │   └── mysql
5.     ├── docker-compose.yml docker-compose配置文件
6.     ├── htdocs 网站文件夹
7.     │   ├── index.html
8.     │   └── index.php
9.     ├── log 日志文件
0.     │   └── nginx
1.     ├── mysql mysql构建文件
2.     │   └── Dockerfile
3.     └── php php构建文件
4.     │   └── nginx.conf
5.     └── zeppelin 
6.     │   └── zeppelin-mongodb-interpreter
7.     └── mongodbdata
8.         └── mongodb    

##  查询资料：
1. ubuntu16.04环境中安装docker：https://blog.csdn.net/dylloveyou/article/details/78233280
2. docker安装mysql以及mongodb：http://www.runoob.com/docker/docker-install-mysql.html
3. docker上部署mongodb集群：https://linux.cn/article-4832-1-rel.html
4. 数据仓库架构与设计：https://blog.csdn.net/trigl/article/details/68944434
5. Hadoop与MongoDB整合：https://blog.csdn.net/Dr_Guo/article/details/51698757
6. 使用 hadoop读写的mongodb：https://blog.csdn.net/u014595019/article/details/53065057
7. docker安装hadoop：https://blog.csdn.net/birdben/article/details/51724126
8. docker配置hive环境：https://blog.csdn.net/birdben/article/details/51759910
7. docker上的zeppelin-mongodb环境安装：https://github.com/bbonnin/zeppelin-mongodb-interpreter
