import requests
import lxml
from lxml import etree  # etree中包含了xpath语法

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
    'cookie':
    'usertrack=ezq0ZVzw7KMX8mSvAxcJAg==; _ntes_nnid=0369dc2c81c6d4802d5ec1cc832da21d,1559293102515; _ntes_nuid=0369dc2c81c6d4802d5ec1cc832da21d; _ga=GA1.2.1939300070.1559293105; vjuids=94c714af4.16b12232693.0.a3dcfa5515bfc; UM_distinctid=16ede774adcddf-05662424d5c9ef-3960720f-384000-16ede774adde04; s_n_f_l_n3=ffaf6e21556c8cc31582305564708; vjlast=1559377422.1582305565.23; _antanalysis_s_id=1582909351008; hb_MA-BFF5-63705950A31C_source=mooc.study.163.com; ne_analysis_trace_id=1585027045904; vinfo_n_f_l_n3=ffaf6e21556c8cc3.1.1.1559377407572.1559378021185.1585027058350; _gid=GA1.2.1754479866.1585027259; Hm_lvt_fbbd5a62f1db722ba672bc37a9bf6b05=1585025932,1585027077,1585027114,1585029500; Hm_lpvt_fbbd5a62f1db722ba672bc37a9bf6b05=1585029500; CNZZDATA1272960468=874441201-1585022667-null%7C1585028069; _gat_gtag_UA_106405703_18=1'
}


def getData():

    url = 'https://news.163.com/special/epidemic'
    print('正在爬取', url)
    html = requests.get(url, headers=headers)
    # print('html.text是',html.text)
    soup = etree.HTML(html.text)  #使用etree函数, soup中包含的就是xpath格式 的网页代码
    # 获取数据
    # print('soup是: ',soup)
    cover_data_china = soup.xpath(
        '//div[@class="cover_data_china"]/div[starts-with(@class,"cover")]')
    print('cover_data_china是: ', cover_data_china)
    for data in cover_data_china:
        title = data.xpath('h4/text')
        print(title)


def main():
    getData()


if __name__ == "__main__":
    print('开始爬取')
    main()
