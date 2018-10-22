import requests
from bs4 import BeautifulSoup
import os
import urllib
import threading

BASE_PAGE_URL = 'http://www.doutula.com/photo/list/?page='
PAGE_URL_LIST = []  #页面url
FACE_URL_LIST = []  #所有表情的url列表
gLock = threading.Lock()  #全局锁

for i in range(1, 3):
    url = BASE_PAGE_URL + str(i)
    PAGE_URL_LIST.append(url)
print(PAGE_URL_LIST)


def producer():
    while True:
        print(PAGE_URL_LIST, '@@@@@@@@@@@@')
        gLock.acquire()
        if len(PAGE_URL_LIST) == 0:
            gLock.release()
            break
        else:
            page_url = PAGE_URL_LIST.pop()
            gLock.release()
            headers = {
                'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
            }
            response = requests.get(page_url, headers=headers)
            content = response.content
            soup = BeautifulSoup(content, 'lxml')
            img_list = soup.find_all(
                'img', attrs={'class': 'img-responsive lazy image_dta'})
            #print(img_list)
            gLock.acquire()
            for img in img_list:
                url = img['data-original'][:-4]
                if not url.startswith('http'):
                    url = 'http:' + url
                FACE_URL_LIST.append(url)
                print(url)
            gLock.release()


def customer():
    while True:
        gLock.acquire()
        if len(FACE_URL_LIST) == 0:
            gLock.release()
            continue
        else:
            face_url = FACE_URL_LIST.pop()
            gLock.release()
            split_list = face_url.split('/')
            filename = split_list.pop()
            path = os.path.join(r'D:\Github\webscraping\doutula', filename)
            print(path)
            #             if not os.path.exists(path):
            #                 os.mkdir(path)
            urllib.request.urlretrieve(face_url, filename=path)


def main():
    #get_page(PAGE_URL_LIST[0])
    #创建3个多线程来作为生产者，爬取表情url
    for x in range(3):
        th = threading.Thread(target=producer)
        th.start()

    #创建5个现成作为消费者，去吧表情图片下载下来
    for x in range(5):
        th = threading.Thread(target=customer)
        th.start()


#     for page_url in PAGE_URL_LIST:
#         print(page_url)
#         get_page(page_url)

if __name__ == '__main__':
    main()
