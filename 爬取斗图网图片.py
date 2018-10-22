import requests
from bs4 import BeautifulSoup
import os
import urllib


BASE_PAGE_URL = 'http://www.doutula.com/photo/list/?page='
PAGE_URL_LIST = [] #页面url

for i in range(1, 3):
    url = BASE_PAGE_URL + str(i)
    PAGE_URL_LIST.append(url)
print(PAGE_URL_LIST)


def download_img(url):
    split_list = url.split('/')
    filename = split_list.pop()
    path = os.path.join('images', filename)
    urllib.urlretrieve(url, filename=path)


def get_page(page_url):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
    }
    response = requests.get(page_url, headers=headers)
    content = response.content
    soup = BeautifulSoup(content, 'lxml')
    img_list = soup.find_all(
        'img', attrs={'class': 'img-responsive lazy image_dta'})
    for img in img_list:
        print(img['data-original'])
        download_img(img['data-original'])

def producer():

def customrer():


def main():
    #get_page(PAGE_URL_LIST[0])


    for page_url in PAGE_URL_LIST:
        print(page_url)
        get_page(page_url)


if __name__ == '__main__':
    main()
