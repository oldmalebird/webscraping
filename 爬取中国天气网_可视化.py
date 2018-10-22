import requests
from bs4 import BeautifulSoup
from pyecharts import Bar

ALL_DATA = []


def parse_page(url):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    #print(response.text)  #出现乱码，说明猜测错了解码方式
    text = response.content.decode('utf-8')
    soup = BeautifulSoup(text, 'html5lib')
    conMidtab = soup.find('div', class_='conMidtab')
    tables = conMidtab.find_all('table')
    for table in tables:

        trs = table.find_all('tr')[2:]
        for index, tr in enumerate(trs):
            tds = tr.find_all('td')
            city_td = tds[0]
            if index == 0:
                city_td = tds[1]
            city = list(city_td.stripped_strings)[0]  #获取所有子孙节点的文本，不加list是个生成器
            temp_td = tds[-2]
            min_temp = list(temp_td.stripped_strings)[0]
            ALL_DATA.append({'city': city, 'min_temp': int(min_temp)})
            #print({'city': city, 'min_temp': int(min_temp)})


def main():
    urls = [
        'http://www.weather.com.cn/textFC/hb.shtml',
        'http://www.weather.com.cn/textFC/db.shtml',
        'http://www.weather.com.cn/textFC/hd.shtml',
        'http://www.weather.com.cn/textFC/hz.shtml',
        'http://www.weather.com.cn/textFC/hn.shtml',
        'http://www.weather.com.cn/textFC/xb.shtml',
        'http://www.weather.com.cn/textFC/xn.shtml'
    ]
    for url in urls:
        parse_page(url)

    #分析数据
    ALL_DATA.sort(key=lambda data: data['min_temp'])
    data = ALL_DATA[0:10]
    chart_cities = list(map(lambda x: x['city'], data))
    chart_temps = list(map(lambda x: x['min_temp'], data))
    chart = Bar('中国天气最低气温排行榜')
    chart.add('', chart_cities, chart_temps)
    chart.render('temperature.html')


if __name__ == '__main__':
    main()
