# -*- coding: utf-8 -*-
from mysqlautospider.items import MysqlautospiderItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class GuanchaspiderSpider(CrawlSpider):
    name = 'guanchaspider'
    allowed_domains = ['guancha.cn']  # 通常一个蜘蛛负责爬取一个站点
    start_urls = ['http://www.guancha.cn/',
                  'https://user.guancha.cn/']

    rules = (
        Rule(LinkExtractor(allow=('/.*?/[0-9]{4}.[0-9]{2}.[0-9]{2}.[0-9]{6}.shtml.*?'), allow_domains=('www.guancha.cn')),
             callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=('/main/content\?id=.*?'), allow_domains=('user.guancha.cn')),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = MysqlautospiderItem()
        # 通过XPath表达式提取新闻网页中受关注的数据信息(一个Item对应一个页面)
        item['title'] = response.xpath('/html/head/title/text()').extract()
        item['keyword'] = response.xpath('/html/head/meta[@name="Keywords"]/@content').extract()
        item['link'] = response.url  # 直接从response响应中获取对应的url链接
        # 将Item数据传递到实体管道(pipelines.py)中
        return item
