from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request

from jianshuhot.items import JianshuhotItem

#from scrapy.exceptions import CloseSpider


class jianshuhot(CrawlSpider):
    name = 'jianshuhot'
    start_urls = ['https://www.jianshu.com/c/V2CqjW?order_by=added_at&page=1']

    def parse(self, response):
        item = JianshuhotItem()
        selector = Selector(response)
        infos = selector.xpath('//div[@class="content"]')
        print(infos)
        # fp_test = open('D:/Github/webscraping/test_jianshu.txt', 'a+')
        # fp_test.write(infos)
        # print(infos)
        for info in infos:
            user = info.xpath('div/a[1]/text()').extract()[0]
            #time = info.xpath('a[1]/p/text()').extract()  #有时候内容为空，有索引会报错
            title = info.xpath('a[1]/text()').extract()[0]
            #view = info.xpath('div/text()').extract()[0]
            comment = info.xpath('div/a[2]/text()').extract()[0].strip()
            like = info.xpath('div/span[1]/text()').extract()[0].strip()
            gain = info.xpath('div/span[2]/text()').extract()

            if gain:
                gain = gain[0].strip()
            else:
                gain = '0'

            item['user'] = user
            item['title'] = title
            item['comment'] = comment
            item['like'] = like
            item['gain'] = gain
            yield item

        urls = [
            'https://www.jianshu.com/c/V2CqjW?order_by=added_at&page={}'.
            format(str(i)) for i in range(2, 3)
        ]
        for url in urls:
            yield Request(url, callback=self.parse)
