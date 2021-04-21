from selenium import webdriver
import time #클릭, 이동시 브라우저도 시간이 필요하기 때문에 시간 지연시키는 코드를 위해 사용
import urllib.request
import csv

def webCrawling() :
    
    # selenium에서 사용할 웹 드라이버 절대 경로 정보
    chromedriver = 'C:\dev\chromedriver.exe'
    # selenum의 webdriver에 앞서 설치한 chromedirver를 연동한다.
    driver = webdriver.Chrome(chromedriver)

    # driver로 특정 페이지를 크롤링한다.
    driver.get('https://2runzzal.com/')
    images = driver.find_elements_by_css_selector(".grid-item")

    ## Scroll down ##
    #SCROLL_PAUSE_SEC = 3

    # 스크롤 높이 가져옴
    #last_height = driver.execute_script("return document.body.scrollHeight")

    # while True:
    #     # 끝까지 스크롤 다운
    #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    #     # 1초 대기
    #     time.sleep(SCROLL_PAUSE_SEC)

    #     # 스크롤 다운 후 스크롤 높이 다시 가져옴
    #     new_height = driver.execute_script("return document.body.scrollHeight")
    #     if new_height == last_height:
    #         break
    #     last_height = new_height

    data = []
    #imgLen = len(images)

    cnt = 1

    ## 이미지 가져오기
    for i in range(5):
        img_data = []
        print(cnt)
        cnt += 1

        try:

            # # 이미지 페이지로 이동할 url 가져오기
            img_href = driver.find_elements_by_css_selector(".btn-view-zzal")[i].get_attribute("href")
            time.sleep(3)

            # # url 페이지로 이동
            driver.get(img_href)

            # # 이미지 src 가져오기
            img_src = driver.find_element_by_css_selector(".zzal-img").get_attribute("src")
            time.sleep(1)

            # # 이미지 tag 가져오기
            tagCnt = driver.find_elements_by_css_selector(".label.bg-tag.font-13")
            tagCnt = len(tagCnt)

            img_tag = []
            tag2str = ""
            for i in range(tagCnt):
                text = driver.find_element_by_xpath('//*[@id="zzal"]/div[2]/div/div[2]/div/div[%d]/a/span'%(i+1)).text
                if(len(tag2str) != 0) :
                    tag2str += ", " + text
                else :
                    tag2str = text
            img_tag.append(tag2str)

            
            img_data.append(img_src)
            img_data = img_data + img_tag

            data.append(img_data)
            driver.back()
            time.sleep(1)

        except:
            pass
    
    print(data)
    driver.close()
    return data

def list2csv(crawlingList) :
    # newline='' 설정이 없는 경우 row와 row 사이에 뉴라인이 한번 더 들어가게 됨
    
    f = open('tagData.csv', 'w', newline='')
    wr = csv.writer(f)
    for imgList in crawlingList:
        wr.writerow(imgList)
    f.close()

def csv2list() :
    data = []
    # encoding='utf-8-sig' 설정은 한글 깨짐 방지
    f = open('tagData.csv', 'r')
    rdr = csv.reader(f)
    for line in rdr:
        data.append(line)
    f.close

    return data



#list2csv(webCrawling())
#print("\n")
print(csv2list())