"""改写异步代码
request改为asyncio 与 aiohttp 异步包

因为是异步代码, 需要标记async 每一个URL开启一个请求Session

在阻塞的地方标记await
抓取机制不变

防错不变

https://blog.csdn.net/brucewong0516/article/details/82697935

————————————————
事件循环机制分为以下几步骤:
1. 创建一个事件循环
2. 将异步函数加入事件队列
3. 执行事件队列, 直到最晚的一个事件被处理完毕后结束
4. 最后建议用 close() 方法关闭事件循环, 以彻底清理 loop 对象防止误用

原文链接：https://blog.csdn.net/Likianta/article/details/90123678

"""

import asyncio
import aiohttp
import time
from bs4 import BeautifulSoup
from urllib import parse

headerss = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
}


async def get_html(url):
    print('正在加载', url)

    async with aiohttp.ClientSession(headers=headerss) as session:
        async with session.get(url) as resp:
            print('来这儿')
            if resp.status == 200:
                print('获取页面成功')
                parse_html(await resp.text())
            else:
                print('Error:', resp.status)

            return


def parse_html(html):
    soup = BeautifulSoup(html, 'lxml')
    resultList = soup.select('table tbody tr')
    for one in resultList:
        title = one.select_one('td a').text
        url = one.select_one('td a')['href']
        url = parse.urljoin('https://s.weibo.com/', url)
        print(title, url)


if __name__ == '__main__':
    print('开始')
    start = time.time()
    # 记录带爬取的网站
    urls = [
        'https://s.weibo.com/top/summary?cate=realtimehot',
        'https://s.weibo.com/top/summary?cate=socialevent'
    ]

    # 创建任务列表
    task = []
    # 将异步函数添加到任务列表中
    for url in urls:
        task.append(get_html(url))

    #开启循环
    loop = asyncio.get_event_loop()
    # 开启任务, 直到结束
    loop.run_until_complete(asyncio.wait(task))

    # 结束后关闭循环
    loop.close()
    print(time.time() - start)
    print('结束')
