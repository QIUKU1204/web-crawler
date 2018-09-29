# -*- coding: utf-8 -*-
import scrapy
# from autospider.autospider.items import AutospiderItem
from autospider.items import AutospiderItem
from scrapy.http import Request

class AutospdSpider(scrapy.Spider):
    name = "autospd"
    allowed_domains = ["dangdang.com"]
    start_urls = ['http://category.dangdang.com/cp01.03.41.00.00.00.html']

    def parse(self, response):
        item = AutospiderItem()
        # 通过XPath表达式分别提取商品的名称、价格、链接、评论数等信息
        item['name'] = response.xpath('//a[@class="pic"]/@title').extract()
        item['price'] = response.xpath('//span[@class="search_now_price"]/text()').extract()
        item['link'] = response.xpath('//a[@class="pic"]/@href').extract()
        item['comnum'] = response.xpath('//a[@class="search_comment_num"]/text()').extract()
        # 提取完后返回item
        yield item
        # 关键技术:通过for循环自动爬取1 - 99页的商品数据
        for i in range(1, 100):
            # 构造要爬取的URL
            url = 'http://category.dangdang.com/pg' + str(i) + '-cp01.03.41.00.00.00.html'
            # 通过yield返回Request，并指定要爬取的URL和回调函数
            yield Request(url, callback=self.parse)
