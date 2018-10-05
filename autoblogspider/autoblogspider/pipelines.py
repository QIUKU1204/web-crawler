# -*- coding: utf-8 -*-
import pymysql
from autoblogspider.settings import MYSQL_DBNAME, MYSQL_HOST, MYSQL_PASSWD, MYSQL_USER


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AutoblogspiderPipeline(object):
	def __init__(self):
		# 连接MySQL数据库
		self.conn = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, passwd=MYSQL_PASSWD, db=MYSQL_DBNAME)

	def process_item(self, item, spider):
		# PS:爬取到的第一篇文章并不属于当前用户
		start_pos = 1
		for j in range(start_pos, len(item['title'])):
			author = item['author'][0].strip()
			title = item['title'][j].strip()
			link = item['link'][j].strip()
			hits = item['hits'][j].strip()
			comments = item['comments'][j].strip()
			sql = "insert into csdnblogs(author,title,link,hits,comments) VALUES('" + author + "','" + title + "','" \
			      + link + "'," + hits + "," + comments + ")"
			self.conn.query(sql)
			self.conn.commit()
		return item

	def close_spider(self, spider):
		# 关闭数据库连接
		self.conn.close()
