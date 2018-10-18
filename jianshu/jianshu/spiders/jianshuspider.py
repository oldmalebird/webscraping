from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request
from jianshu.items import JianshuItem
from scrapy.exceptions import CloseSpider
import json


class jianshu(CrawlSpider):
    name = 'jianshu'
    start_urls = [
        'https://www.jianshu.com/recommendations/collections?page=1&order_by=hot'
    ]

    def parse(self, response):
        item = JianshuItem()
        selector = Selector(response)
        infos = selector.xpath('//div[@class="collection-wrap"]')
        # print(type(infos))
        # fp_test = open('D:/Github/webscraping/test_jianshu.txt', 'a+')
        # fp_test.write(infos)
        print(infos)
        for info in infos:
            name = info.xpath('//a[1]/h4/text()').extract()[0]
            content = info.xpath('a[1]/p/text()').extract()  #有时候内容为空，有索引会报错
            article = info.xpath('div/a/text()').extract()[0]
            fans = info.xpath('div/text()').extract()[0]

            if content:
                content = content[0]
            else:
                content = ''

            item['name'] = name
            item['content'] = content
            item['article'] = article
            item['fans'] = fans
            yield item

        urls = [
            'https://www.jianshu.com/recommendations/collections?page={}&order_by=hot'.
            format(str(i)) for i in range(2, 3)
        ]
        for url in urls:
            yield Request(url, callback=self.parse)
