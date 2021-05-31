import csv

def list2csv(crawlingList) :
    # newline='' 설정이 없는 경우 row와 row 사이에 뉴라인이 한번 더 들어가게 됨
    f = open('imgData.csv', 'w', newline='', encoding='UTF-8')
    wr = csv.writer(f)
    for imgList in crawlingList:
        wr.writerow(imgList)
    f.close()

def readTag():

    data = []
    # encoding='utf-8-sig' 설정은 한글 깨짐 방지
    f = open('ImageData.csv', 'r', encoding='utf-8-sig')
    rdr = csv.reader(f)
    cnt = 1
    for line in rdr:
        data.append(line)
    f.close

    return data

list2csv(readTag())