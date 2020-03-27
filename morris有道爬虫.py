'''
i: new
from: AUTO
to: AUTO
smartresult: dict
client: fanyideskweb
salt: 15852176002981
sign: f810ccab29be76b0d42616b82512e1a3
ts: 1585217600298
bv: 14d305bd116eced62d277e84edd279d3
doctype: json
version: 2.1
keyfrom: fanyi.web
action: FY_BY_CLICKBUTTION
'''

import time
import random
import math
import requests
import hashlib

keyword = '烦人'
# r = math.floor(time.time() * 1000)
# i = str(r) + str(int(random.random() * 10))
# bv = hashlib.md5(("5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36").encode('utf8')).hexdigest()
# salt = i
# ts = r
# sign = hashlib.md5(("fanyideskweb" + keyword + str(i) + "Nw(nmmbP%A-r6U3EUn]Aj").encode('utf8')).hexdigest()

r = math.floor(time.time() * 1000)
i = r + int(random.random() * 10)
salt = i
ts = r
sign = hashlib.md5(("fanyideskweb" + keyword + str(i) +
                    "Nw(nmmbP%A-r6U3EUn]Aj").encode('utf8')).hexdigest()
bv = hashlib.md5((
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"
).encode('utf8')).hexdigest()
print('r:', r)
print('i:', i)
print('sign', sign)
print('bv', bv)

data = {
    'i': 'new',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': salt,
    'sign': sign,
    'ts': ts,
    'bv': bv,
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION'
}
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
    'Referer':
    'http://fanyi.youdao.com/',
    'Cookie':
    'OUTFOX_SEARCH_USER_ID=1329932936@10.108.160.102; JSESSIONID=aaaII0ezBR_2WgkHGGsex; OUTFOX_SEARCH_USER_ID_NCOO=1292652703.445076; ___rl__test__cookies=1585233959575'
}

url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
html = requests.post(url, data=data, headers=headers)
print(html.json())
# Dataa = {
#     'i':keyword,
#     'from':' AUTO',
#     'to':' AUTO',
#     'smartresult':' dict',
#     'client':' fanyideskweb',
#     'salt': salt,
#     'sign':sign,
#     'ts':ts,
#     'bv':bv,
#     'doctype':' json',
#     'version':' 2.1',
#     'keyfrom':' fanyi.web',
#     'action':' FY_BY_CLICKBUTTION'
# }
# Headerss = {
#     'Accept': 'application/json, text/javascript, */*; q=0.01',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
#     'Referer': 'http://fanyi.youdao.com/',
#     'Cookie': 'OUTFOX_SEARCH_USER_ID=1329932936@10.108.160.102; JSESSIONID=aaaII0ezBR_2WgkHGGsex; OUTFOX_SEARCH_USER_ID_NCOO=1292652703.445076; ___rl__test__cookies=1585233959575',
#     'Origin': 'http://fanyi.youdao.com'

# }

# html = requests.post(url, data=Dataa, headers = Headerss)
# print(html.text)

# print('salt = ', salt)
# print('sign = ', sign)
# print('ts = ', r)
# print('bv = ', bv)
