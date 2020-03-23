import requests
import time
from bs4 import BeautifulSoup
from urllib import parse

headers = {
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}


def get_html(url):
    print("正在爬取:", url)
    html = requests.get(url, headers=headers)  #get特免获取源代码
    if html.status_code == 200:
        parse_html(html.text)
        print('获取页面成功')
    else:
        print('Error', html.status_code)

    return


def parse_html(html):
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.select(
        'table tbody tr')  #观察层级结构,使用soup的select方法, 返回关键字下的数据已list形式返回
    for tr in trs:
        title = tr.select_one('td a').text  #获取关键字的数据的文本
        url = tr.select_one('td a')['href']  #获取href开头的url
        url = parse.urljoin('https://s.weibo.com/',
                            url)  # 对url进行拼接,需要导入from urllib import parse
        print(title, url)
    pass


if __name__ == '__main__':
    start = time.time()  #记录开始时间, 需要导入time, 是个方法, 需要加()
    # url = 'https://s.weibo.com/top/summary?cate=realtimehot'
    # 刷两个链接
    urls = [
        'https://s.weibo.com/top/summary?cate=realtimehot',
        'https://s.weibo.com/top/summary?cate=socialevent'
    ]

    for url in urls:
        get_html(url)

    print(time.time() - start)  #计算运行时间
