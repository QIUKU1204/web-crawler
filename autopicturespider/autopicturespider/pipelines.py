# -*- coding: utf-8 -*-
import urllib.request
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AutopicturespiderPipeline(object):
    def process_item(self, item, spider):
        # PS:实际上一个item实例中只包含了一张图片的信息
        for i in range(0, len(item['picurl'])):
            # 构造图片在本地存储的文件路径
            localpath = 'C:/Users/QIUKU/PycharmProjects/web-crawler/autopicturespider/data/' + item['picname'][i] + '.jpg'
            # 通过urllib.request.urlretrieve方法将原图片下载到本地
            urllib.request.urlretrieve(url=item['picurl'][i], filename=localpath)
        return item
