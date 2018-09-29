# -*- coding: utf-8 -*-
import pymysql
from mysqlautospider.settings import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWD, MYSQL_DBNAME

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MysqlautospiderPipeline(object):
	def __init__(self):
		# 连接MySQL中的数据库scrapydb
		self.conn = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, passwd=MYSQL_PASSWD, db=MYSQL_DBNAME)

	def process_item(self, item, spider):
		# 从Item实例中获取数据(一个Item对应一个页面)
		title = item['title'][0].strip()
		keyword = '无' if len(item['keyword']) is 0 or item['keyword'][0] is '' else item['keyword'][0].strip()
		link = item['link']
		# 构造插入数据的sql语句
		sql = "insert into sinanews(title,keyword,link) VALUES('" + title + "','" + keyword + "','" + link + "')"
		# 通过query执行该sql语句
		self.conn.query(sql)
		self.conn.commit()  # 执行INSERT等增删改操作后要调用commit()提交事务
		return item

	def close_spider(self, spider):
		self.conn.close()
