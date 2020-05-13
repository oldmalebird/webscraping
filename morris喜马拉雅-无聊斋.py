import requests
import time
from bs4 import BeautifulSoup
from urllib import parse

headers = {
    'Host':
    'mobile.ximalaya.com',
    'Accept':
    '*/*',
    'Cookie':
    'domain=.ximalaya.com; path=/; channel=ios-b1; 1&_device=iPhone&04634CBF-1A3B-4A84-A733-E28EA96E0159&6.6.33; impl=com.gemd.iting; XUM=04634CBF-1A3B-4A84-A733-E28EA96E0159; c-oper=%E8%81%94%E9%80%9A; net-mode=WIFI; res=750%2C1334; 1&_token=51993087&A3F2445DDAE884E4E8CABEB7726C4BFEcDv37F3E8C5A73239ADD6CFEB9D11D11F76C6C2EBAFF18FB1D9C07BE1C33049A11B; idfa=04634CBF-1A3B-4A84-A733-E28EA96E0159; x_xmly_ts=1585563086776; x_xmly_resource=xm_source%3Ahistory%26xm_medium%3Asearch%26xm_term%3A%E6%97%A0%E8%81%8A%E6%96%8B%20%7C%20%E6%97%A0%E8%81%8A%E7%9A%84%E6%97%B6%E5%80%99%E5%90%AC%E4%B8%80%E5%90%AC; x_xmly_tid=730287978; device_model=iPhone8; XD=hR2pkdZCaUs9+TNAzuQPS95lW8Ccp38okC7O8NqjTea6gLjUYXtPo9QtjqVt0ztOgf0uhcC28bueENa12w+iPQ==; x-abtest-bucketIds=202993%2C203466%2C203002%2C203193%2C100088%2C203386%2C100030%2C203202%2C100467%2C203044%2C100105%2C202922%2C202929%2C203520%2C203343%2C203268%2C203091%2C203434%2C203045; freeFlowType=0; minorProtectionStatus=0',
    'User-Agent':
    'ting_v6.6.33_c5(CFNetwork, iOS 13.3, iPhone10,4)',
    'x-viewId':
    'UIView',
    'Accept-Language':
    'zh-cn',
    'Accept-Encoding':
    'gzip, deflate',
    'Connection':
    'keep-alive'
}


def get_json(url):
    html = requests.get(url, headers=headers)
    print(html)


if __name__ == "__main__":
    url = 'http://211.95.37.210/mobile/v1/album/track/ts-1585563086774?albumId=14302859&device=iPhone&isAsc=true&isQueryInvitationBrand=true&pageId=8&pageSize=20'

    for i in range(1, 8):
        temp = 'http://211.95.37.210/mobile/v1/album/track/ts-{}?albumId=14302859&device=iPhone&isAsc=true&isQueryInvitationBrand=true&pageId=8&pageSize=20'.format(
            time.time())
        time.sleep(1)
        get_json(temp)
