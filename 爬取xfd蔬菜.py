import time
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import pymongo

client = MongoClient()  # mongodb server
xfd_veg_price = client.xfd_db.xfd_veg_price  # xfd_veg_price collection

# PRICE_DATA = []
headers = {
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':
    'gzip, deflate',
    'Accept-Language':
    'zh-CN,zh;q=0.9',
    'Cache-Control':
    'max-age=0',
    'Connection':
    'keep-alive',
    'Cookie':
    'UM_distinctid=166658c87bc270-05130348356c7d-2711938-2a3000-166658c87bd3c0; CNZZDATA5463821=cnzz_eid%3D1414737999-1539300290-http%253A%252F%252Fwww.xinfadi.com.cn%252F%26ntime%3D1540263448; Hs2u_2132_lastvisit=1540264789',
    'Host':
    'www.xinfadi.com.cn',
    'Referer':
    'http://www.xinfadi.com.cn/marketanalysis/1/list/1.shtml',
    'Upgrade-Insecure-Requests':
    '1',
    'user-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
}


def get_price(url):
    '''获取xfd蔬菜价格数据'''
    global DUPLICATE_FLAG
    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.content,
                         'lxml')  #soup= BeautifulSoup(req.content, 'lxml')
    pricetable = soup.find('table', attrs={'class': 'hq_table'})
    trs = pricetable.find_all('tr')[1:]
    for tr in trs:
        tds = tr.find_all('td')
        veg_name = list(tds[0].stripped_strings)[0]
        low_price = list(tds[1].stripped_strings)[0]
        avg_price = list(tds[2].stripped_strings)[0]
        high_price = list(tds[3].stripped_strings)[0]
        specification = list(tds[4].stripped_strings)[0]
        unit = list(tds[5].stripped_strings)[0]
        date = list(tds[6].stripped_strings)[0]
        #print(date, veg_name)
        if xfd_veg_price.find({
                'date': date,
                'veg_name': veg_name,
                'specification': specification
                #'low_price': low_price #感觉这个不行，会重复添加信息，只能用来过滤前三者信息重复的数据
        }).count() > 0:
            print(
                xfd_veg_price.find({
                    'date': date,
                    'veg_name': veg_name,
                    'specification': specification
                }).count())
            print(date, veg_name, specification)
            DUPLICATE_FLAG = True
            print('已爬取到已保存过的数据')
            break
        if (',' not in low_price) and (',' not in avg_price) and (
                ',' not in high_price):
            data = {
                'veg_name': veg_name,
                'low_price': float(low_price),
                'avg_price': float(avg_price),
                'high_price': float(high_price),
                'specification': specification,
                'unit': unit,
                'date': date
            }
            price_id = xfd_veg_price.insert(data)  #insert db


if __name__ == '__main__':
    # 列表生成器生成需要遍历的url
    DUPLICATE_FLAG = False
    urls = [
        'http://www.xinfadi.com.cn/marketanalysis/1/list/{}.shtml'.format(
            str(i)) for i in range(67, 2000)
    ]
    i = 1
    for url in urls:
        if DUPLICATE_FLAG == True:
            break
        get_price(url)
        print('已爬取第%d页' % i)
        i += 1
        time.sleep(3)
