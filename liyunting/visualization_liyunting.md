##  可视化 
**version: 0513**  
###  任务概述
对地球大数据分析系统进行可视化，表现为Google Earth三维视图，且在相应国家上叠加分析结果的统计图表。
###  实现方式
* 获得分析结果(如csv文件)  
* 使用D3.js动态加载csv文件，并对数据做绘图前预处理
* 使用D3.js框架绘制统计图（如柱状图）   
* 将绘制成的统计图转为图片格式（如JPEG、PNG）  
* 编写kml文件，在Google Earth上绘制出主要的国家，并设置初始视角    
* 将统计图的图片通过kml的GroundOverlay或者ScreenOverlay方式叠加到相应国家上    
* 通过kml的NetworkLink设置文件路径、刷新时间等可实现对网络kml文件的自动刷新     
* 由此实现当视角和统计图片改变时，Google Earth呈现的视图随之改变  
###  任务清单   
- [x]  熟悉系统主要功能和各部分之间的关系  
- [x]  熟悉javascript的基本语法    
- [x]  了解kml的基本标签和语法格式  
- [x]  了解D3.js和Google Earth  
- [x]  学习kml文件详细语法
- [x]  学习D3.js框架  
- [x]  能将kml文件载入Google Earth  
- [x]  能使用D3绘制简单统计图   
- [x]  能完成kml文件的编写 
- [x]  学习php的基础知识  
- [x]  详细阅读补充资料  
- [ ]  了解常用的数据查询接口工具  
- [ ]  能使用数据查询接口获得数据  
- [ ]  完成整体编码      
###  参考资料  
1. D3实现简单柱状图源码demo https://github.com/nelsonkuang/ant-admin/blob/master/src/components/charts/D3SimpleBarChart.js    
2. Scott Murray. 数据可视化实战：使用D3设计交互式图表[M]. 人民邮电出版社, 2013 
3. Google Earth KML中文说明 https://wenku.baidu.com/view/549116fd700abb68a982fb91.html?sxts=1525177521662   
4. 使用D3制作图表 https://www.imooc.com/learn/103  
5. D3.js入门教程 http://wiki.jikexueyuan.com/project/d3wiki/introduction.html  
6. KML教程 https://wenku.baidu.com/view/773edc42da38376baf1faee9.html 
7. php入门 https://www.imooc.com/learn/54   
8. D3.js加载csv文件绘图 https://blog.csdn.net/tianxuzhang/article/details/14121451 
9. D3.js导出svg图片 https://blog.csdn.net/xx123698/article/details/53580057  
