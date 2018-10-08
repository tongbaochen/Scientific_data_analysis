from urllib import request
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
import writeToTxt

#获取到了所有indicators跳转链接
def get_all_skiplink(path):
    resp = request.urlopen('http://apps.who.int/gho/data/node.imr')
    html_data = resp.read().decode('utf-8')
    soup = bs(html_data,'html.parser')
    tartget_list = soup.find_all('div',id = 'content')
    link_list = tartget_list[0].find_all('li')
    #获取到了所有得indicators跳转链接
    final_link = []
    for item in link_list:
        final_link.append(item.find_all('a')[0]['href'])
    final_l = set(final_link)
    writeToTxt.write_to_txt(final_l,'first_link')
    return final_l

#获取到了所有第二层的跳转链接
def get_all_second_link(final_link,path):
    second_link = []
    for item in final_link:
        file = ""
        file = path + item
        try:
            res = request.urlopen(file)
            res_html = res.read().decode('utf-8')
            soup = bs(res_html,'html.parser')
            tartget = soup.find_all('div',id = 'content')
            final = tartget[0].find_all('ul',class_ = "list_dash" )
            final_indicator = final[0].find_all('li')
            # print(final_indicator)
            # indicator = final_indicator[1].find_all('a')[0]["href"]
            # print(final_indicator[1])
            # 获取到目标下载链接indicator   view.main.52400
            indicator = final_indicator[1].find_all('a')[0]['href']
            print(indicator)
            second_link.append(indicator)
        except Exception as e:
            print(item + "request_error:", e)
        finally:
            pass
    second_l = set(second_link)
    writeToTxt.write_to_txt(second_l, 'second_link')
    return  second_l

# 获取到了所有csv下载链接
def get_all_csv_link(second_link,path):
    csv_link = []
    for item in second_link:
        # rel = request.urlopen(path + item)
        # data_html = rel.read().decode('utf-8')
        # s_soup = bs(data_html,'html.parser')
        '''处理iframe'''
        '''利用驱动，切入iframe,获取相应的html,再结合beautifulsoup进行处理'''
        try:
            driver = webdriver.Firefox()
            time.sleep(1)
            driver.get(path + item)
            driver.switch_to.frame('content_iframe')
            driver.switch_to.frame('passthrough')
            # elem = driver.find_element_by_xpath("/html/body/div/div/div")
            html = driver.page_source
            soup_html = bs(html,'html.parser')
            s = soup_html.find_all("div",class_ = "controls")
            m = s[0].find_all('a',class_ = "control")
            tartget_link = m[1]["href"]
            print(tartget_link)#target_link为目标csv的下载链接
            csv_link.append(tartget_link)
            # 退出并关闭窗口的每一个相关的驱动程序
            driver.quit()
        except Exception as e:
            print(item + "second_link_error:", e)
        finally:
            pass
    csv_l = set(csv_link)
    writeToTxt.write_to_txt(csv_l, 'csv_link')
    return csv_l

#传入下载链接数组，下载所有csv文件
def download(files,path):

    for file in files:
        name = file[file.find('GHO')+4:file.find('?')]
        try:
            resp = request.urlopen(file)
            # csvHand = open(pre+file+after, "r+", encoding='utf-8', errors='ignore')
            wf = open(name + '.csv', 'w')
            wf.write(resp.read().decode('gbk'))
            wf.close()
        except Exception as e:
            print("open error:", e)
        finally:
            # 关闭csv文件
            print(file + "finished")
            # csvHand.close()

path = 'http://apps.who.int/gho/data/'
# first = get_all_skiplink(path)
# second = get_all_second_link(writeToTxt.read_to_list('first_link.txt'),path)
# csvs = get_all_csv_link(writeToTxt.read_to_list('second_link.txt'),path)
# print('finished')
download(writeToTxt.read_to_list('download_link.txt'),path)

# print(first)
# print(second)
