import io
import sys
'''
https://www.cnblogs.com/ymjyqsx/p/6554817.html
https://www.cnblogs.com/xuxn/archive/2011/07/27/read-a-file-with-python.html
    '''

#load countries data for all_countries.txt,return a []
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

entry = readCountries('D:/DataLab_Project/gnewsclient-master/all_country.txt')
it = iter(entry)
for i in it:
    print(i)


