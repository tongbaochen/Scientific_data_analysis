import codecs

def write_to_txt(arr,fileName):
    try:
        f = codecs.open(fileName + '.txt','w','utf-8')
        for item in arr:
            f.write(str(item)+ '\r\n')
        f.close()
    except Exception as e:
        print("open error:", e)
    finally:
        # 关闭csv文件
        print(fileName + '.txt' + "finished")

#讲一个txt文件按照行来读取，写入一个list数组中,并将数组返回
def read_to_list(filename):
    with open(filename,'r') as f:
        data = f.readlines()
        result = []
        for line in data:
            result.append(line.rstrip())
        return result


# write_to_txt(['aaaa','bbbb','cccc','dddd'],'file')
# data =read_to_list('file.txt')
# print(data[2])
# for item in data:
    # print(item.rstrip())
    # print(item)

record1 = read_to_list('csv_link.txt')
# print(len(record1))
record2 = read_to_list('D:\DataLab_Project\Code\mongotest\data\csv_link.txt')
# print(len(record2))
for item in record1:
    record2.append(item)
record = set(record2)
# print(len(record))

write_to_txt(record,'download_link')