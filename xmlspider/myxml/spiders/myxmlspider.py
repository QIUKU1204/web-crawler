# -*- coding: utf-8 -*-
from myxml.items import MyxmlItem
from scrapy.spiders import XMLFeedSpider


class MyxmlspiderSpider(XMLFeedSpider):
	name = 'myxmlspider'
	allowed_domains = ['sina.com.cn',
	                   'iqianyue.com']
	start_urls = ['http://blog.sina.com.cn/rss/1615888477.xml',
	              'http://yum.iqianyue.com/weisuenbook/pyspd/part12/test.xml']
	iterator = 'iternodes'  # you can change this; see the docs
	itertag = 'rss'  # change it accordingly
	# itertag = 'person'  # change it accordingly

	def parse_node(self, response, node):
		item = MyxmlItem()
		# 利用XPath表达式从指定标签节点提取需要的信息，并存储到对应的Item实例中
		item['title'] = node.xpath('/rss/channel/item/title/text()').extract()
		item['link'] = node.xpath('/rss/channel/item/link/text()').extract()
		item['author'] = node.xpath('/rss/channel/item/author/text()').extract()
		# item['link'] = node.xpath('/person/email/text()')
		# 通过for循环输出存在Item实例中的信息
		print(item)
		return item
