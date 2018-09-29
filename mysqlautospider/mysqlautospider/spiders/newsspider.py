# -*- coding: utf-8 -*-
# from mysqlautospider.mysqlautospider.items import MysqlautospiderItem
from mysqlautospider.items import MysqlautospiderItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class NewsspiderSpider(CrawlSpider):
	name = 'newsspider'
	allowed_domains = ['sina.com.cn']
	start_urls = ['http://news.sina.com.cn/']

	rules = (
		Rule(LinkExtractor(allow=('.*?/[0-9]{4}.[0-9]{2}.[0-9]{2}.doc-.*?shtml'), allow_domains=('sina.com.cn')),
		     callback='parse_item', follow=True),
	)

	def parse_item(self, response):
		item = MysqlautospiderItem()
		# 通过XPath表达式提取新闻网页中受关注的数据信息(一个Item对应一个页面)
		item['title'] = response.xpath('/html/head/title/text()').extract()
		item['keyword'] = response.xpath('/html/head/meta[@name="keywords"]/@content').extract()
		item['link'] = response.url  # 直接从response响应中获取对应的url链接
		# 将Item数据传递到实体管道(pipelines.py)中
		return item
