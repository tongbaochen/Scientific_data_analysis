##  可视化 
**version: 0428**  
###  任务概述
对地球大数据分析系统进行可视化，表现为Google Earth三维视图，且在相应国家上叠加分析结果的统计图表。
###  实现方式 
* 编写kml文件，对Google Earth显示的地理位置、视角等进行设置  
* 通过数据查询接口从数据库获得分析结果  
* 使用D3.js框架绘制统计图（如柱状图）  
* 将统计图以js或图片的形式嵌入kml文件  
* 将kml文件载入Google Earth中，可以手动载入，也可编写Google Earth自动查询kml文件的脚本
###  任务清单   
- [x]  熟悉系统主要功能和各部分之间的关系  
- [x]  熟悉javascript的基本语法    
- [x]  了解kml的基本标签和语法格式  
- [x]  了解D3.js和Google Earth  
- [ ]  学习kml文件详细语法
- [x]  学习D3.js框架  
- [ ]  能将kml文件载入Google Earth  
- [x]  能使用D3绘制简单统计图   
- [ ]  能完成复杂kml文件的编写  
- [ ]  详细阅读补充资料  
- [ ]  了解常用的数据查询接口工具  
- [ ]  能使用数据查询接口获得数据  
- [ ]  完成整体编码      
###  参考资料  
1. D3实现简单柱状图源码demo https://github.com/nelsonkuang/ant-admin/blob/master/src/components/charts/D3SimpleBarChart.js  
2. Scott Murray. 数据可视化实战：使用D3设计交互式图表[M]. 人民邮电出版社, 2013 
3. Google Earth KML中文说明 https://blog.csdn.net/zhangjie_xiaoke/article/details/2222281  
4. 使用D3制作图表 https://www.imooc.com/learn/103
5. D3.js入门教程 http://wiki.jikexueyuan.com/project/d3wiki/introduction.html
