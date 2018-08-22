#!/usr/bin/env python 这是啥？
#-*- coding: utf-8 -*-
__author__ = '呃 lgnlgnlgnlgn@163.com'

import urllib
import urllib.error
import urllib.request


def download(url, num_retries=2):
    print('Downloading:', url)
    try:
        html = urllib.request.urlopen(url).read()
    except urllib.error.URLError as e:
        print('Download error:', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, num_retries - 1)
    return html


download('http://www.meetup222.com')


def clear():
    '''该函数用于清屏 '''
    print(u'内容较多，显示3秒后翻页')
    time.sleep(3)
    OS = platform.system()
    if (OS == u'Windows'):
        os.system('cls')
    else:
        os.system('clear')


def linkBaidu():
    url = 'http://www.baidu.com'
    try:
        response = urllib.request.urlopen(url, timeout=3)
    except urllib.error.URLError:
        print(u"网络地址错误")
        exit()
    with open('./baidu.txt', 'w') as fp:
        fp.write(response.read())
    print(u"获取url信息，response.geturl() \n: %s" % response.geturl())
    print(u"获取返回代码，response.getcode() \n: %s" % response.getcode())
    print(u"获取返回信息，response.info() \n: %s" % response.info())
    print(u"获取的网页内容已存入当前目录的baidu.txt中，请自行查看")


if __name__ == '__main__':
    linkBaidu()
