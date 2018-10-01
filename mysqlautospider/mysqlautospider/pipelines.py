# -*- coding: utf-8 -*-
import pymysql
from mysqlautospider.settings import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWD, MYSQL_DBNAME
from scrapy.exceptions import DropItem

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MysqlautospiderPipeline(object):
	def __init__(self):
		# 连接MySQL中的数据库scrapydb
		self.conn = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, passwd=MYSQL_PASSWD, db=MYSQL_DBNAME)
		# 定义一个set对象用于去重(set中的元素不允许重复)
		self.news_set = set()

	def process_item(self, item, spider):
		# 从Item实例中获取数据(一个Item对应一个页面)
		title = None if len(item['title']) is 0 or item['title'][0] is '' else item['title'][0].strip()
		keyword = '无' if len(item['keyword']) is 0 or item['keyword'][0] is '' else item['keyword'][0].strip()
		link = item['link']
		# 当请求的链接只用于跳转时，返回的内容为空且无法提取到标题信息
		if title is None:
			raise DropItem('Invalid Link: ', link)  # 链接无效
		# 避免重复入库
		if title in self.news_set:
			raise DropItem('Duplicate news found: ', title)  # 内容(item)重复
		else:
			self.news_set.add(title)
		# 根据蜘蛛名字构造对应的sql语句
		if spider.name is 'sinaspider':
			sql = "insert into sinanews(title,keyword,link) VALUES('" + title + "','" + keyword + "','" + link + "')"
		elif spider.name is 'guanchaspider':
			sql = "insert into guanchanews(title,keyword,link) VALUES('" + title + "','" + keyword + "','" + link + "')"
		else:
			return item
		# 通过query执行该sql语句
		self.conn.query(sql)
		self.conn.commit()  # 执行INSERT等增删改操作后要调用commit()提交事务
		return item

	def close_spider(self, spider):
		self.conn.close()
