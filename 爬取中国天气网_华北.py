import requests
from bs4 import BeautifulSoup


def parse_page(url):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    #print(response.text)  #出现乱码，说明猜测错了解码方式
    text = response.content.decode('utf-8')
    soup = BeautifulSoup(text, 'lxml')
    conMidtab = soup.find('div', class_='conMidtab')  #不明为什么这里是class_
    tables = conMidtab.find_all('talbe')


def main():
    url = 'http://www.weather.com.cn/textFC/hb.shtml'
    parse_page(url)


if __name__ == '__main__':
    main()
