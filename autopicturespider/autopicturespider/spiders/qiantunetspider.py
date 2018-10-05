# -*- coding: utf-8 -*-
import re

from autopicturespider.items import AutopicturespiderItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class QiantunetspiderSpider(CrawlSpider):
	name = 'qiantunetspider'
	allowed_domains = ['58pic.com']
	start_urls = ['http://www.58pic.com/taob/']

	rules = (
		Rule(LinkExtractor(allow=('http://www.58pic.com/.*?/[0-9]{1,}\.html'), allow_domains=('www.58pic.com')),
		     callback='parse_item', follow=True),
	)

	def parse_item(self, response):
		item = AutopicturespiderItem()
		# 构造提取图片链接的正则表达式
		picurl_pattern = '<img data-src="(.*?)"'
		# UnicodeDecodeError: 'utf-8' codec can't decode byte.. -> 在decode()方法中设errors参数为'ignore'即可
		item['picurl'] = re.compile(picurl_pattern).findall(response.body.decode(encoding='utf-8', errors='ignore'))
		item['picname'] = response.xpath('//div[@class="fl detail-title"]/text()').extract()
		return item
