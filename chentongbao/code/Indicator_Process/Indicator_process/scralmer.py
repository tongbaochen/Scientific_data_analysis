from urllib import request
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time


path = 'http://apps.who.int/gho/data/'
resp = request.urlopen('http://apps.who.int/gho/data/node.imr')
html_data = resp.read().decode('utf-8')
# print(html_data)
soup = bs(html_data,'html.parser')
tartget_list = soup.find_all('div',id = 'content')
link_list = tartget_list[0].find_all('li')
# print(link_list[0])
# link = link_list[0].find_all('a')
# print(link)
# tartget = link[0]['href']
# print(tartget)

# print()
#获取到了所有得indicators跳转链接
final_link = []
for item in link_list:
    final_link.append(item.find_all('a')[0]['href'])

print(final_link)
'''
term = []
for item in final_link:
    start = item.find('node.imr.')
    end = item.find('?')
    term.append(item[start+9:end])
print(term)
'''
pre = "http://apps.who.int/gho/athena/data/GHO/"
after = "?filter=COUNTRY:*;SEX:*&x-sideaxis=COUNTRY;YEAR&x-topaxis=GHO;SEX&profile=crosstable&format=csv"
'''
for file in term:
    try:
        resp = request.urlopen(pre+file+after)
        # csvHand = open(pre+file+after, "r+", encoding='utf-8', errors='ignore')
        wf = open(file+'.csv','w')
        wf.write(resp.read().decode('gbk'))
        wf.close()
    except Exception as e:
        print("open error:", e)
    finally:
        # 关闭csv文件
        print(file + "finished")
        # csvHand.close()
    # break
    '''
file = 'http://apps.who.int/gho/data/node.imr.SA_0000001409?lang=en'
res = request.urlopen(file)
res_html = res.read().decode('utf-8')
soup = bs(res_html,'html.parser')
tartget = soup.find_all('div',id = 'content')
final = tartget[0].find_all('ul',class_ = "list_dash" )
final_indicator = final[0].find_all('li')
print(final_indicator)
# indicator = final_indicator[1].find_all('a')[0]["href"]
# print(final_indicator[1])
# 获取到目标下载链接indicator   view.main.52400
indicator = final_indicator[1].find_all('a')[0]['href']
print(indicator)
rel = request.urlopen(path + indicator)
data_html = rel.read().decode('utf-8')
s_soup = bs(data_html,'html.parser')
'''处理iframe'''
driver = webdriver.Firefox()
time.sleep(2)
driver.get(path + indicator)
driver.switch_to.frame('content_iframe')
driver.switch_to.frame('passthrough')
# elem = driver.find_element_by_xpath("/html/body/div/div/div")
html = driver.page_source
soup_html = bs(html,'html.parser')
s = soup_html.find_all("div",class_ = "controls")
m = s[0].find_all('a',class_ = "control")
tartget_link = m[1]["href"]
print(tartget_link)#target_link为目标csv的下载链接。
# print(elem)

# $("iframe").contents().find("body").html()
'''
filter = s_soup.find_all('iframe')
print(filter[0])
filter0 = filter[0].find_all('iframe')
print(filter0[0])
fin = filter0[0].find_all("div",class_ = "controls")
print(fin[0])
'''


# pre = 'http://apps.who.int/gho'
# after = '&x-sideaxis=COUNTRY;YEAR&x-topaxis=GHO;SEX&profile=crosstable&format=csv'
# print (pre+fin[2:]+after)
# print(indicator)
# link_list = tartget_list[0].find_all('li','class')
# print(tartget[0])





