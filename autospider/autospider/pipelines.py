# -*- coding: utf-8 -*-
import codecs
import json


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AutospiderPipeline(object):
	def __init__(self):
		# 打开goods_data.json文件
		self.file = codecs.open('C:/Users/QIUKU\PycharmProjects/web-crawler/autospider/data/goods_data.json', 'wb',
		                        encoding='utf-8')

	def process_item(self, item, spider):
		# 对爬取到的item数据进行进一步处理
		# i = json.dumps(dict(item), ensure_ascii=False)
		# line = i + '\n'
		# 将处理过后的item数据写入json文件中
		for j in range(0, len(item['link'])):
			# 从item数据(即一页商品的数据)中获取每一件商品的详细信息
			name = item['name'][j]
			price = item['price'][j]
			link = item['link'][j]
			comnum = item['comnum'][j]
			# 将一件商品的各项信息重新组合在一起
			goods = {'书名': name, '售价': price, '商品链接': link, '评论数': comnum}
			# 先将goods转换为字典，再使用json.dumps()处理为json格式数据
			line = json.dumps(dict(goods), ensure_ascii=False) + '\n'
			self.file.write(line)
		return item

	def close_spider(self, spider):
		# 关闭goods_data.json文件
		self.file.close()
