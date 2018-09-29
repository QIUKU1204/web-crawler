# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

'''定义要提取、存储的结构化数据所对应的数据模型'''
class MyxmlItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	# 文章标题
	title = scrapy.Field()
	# 文章链接
	link = scrapy.Field()
	# 文章作者
	author = scrapy.Field()
