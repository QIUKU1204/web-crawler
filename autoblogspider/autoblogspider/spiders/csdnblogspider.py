# -*- coding: utf-8 -*-
import scrapy
import re
import urllib.request
from autoblogspider.items import AutoblogspiderItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request


class CsdnblogspiderSpider(CrawlSpider):
    name = 'csdnblogspider'
    allowed_domains = ['blog.csdn.net']
    start_urls = ['https://blog.csdn.net/']  # 由parse_start_url方法处理，而不是parse_item方法

    rules = (
        Rule(LinkExtractor(allow=('https://blog.csdn.net/.*?'), restrict_xpaths=('//dd[@class="name"]'),
                           allow_domains=('blog.csdn.net')), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=('https://blog.csdn.net/.*?'), restrict_xpaths=('//div[@class="bottom_con con clearfix"]'),
                           allow_domains=('blog.csdn.net')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = AutoblogspiderItem()
        # 通过XPath表达式与正则表达式的组合提取关注的数据
        item['author'] = response.xpath('//a[@id="uid"]/text()').extract()
        title_pattern = '<span class="article-type type.*?</span>(.*?)</a>'
        item['title'] = re.compile(title_pattern, re.S).findall(response.body.decode('utf-8'))
        item['link'] = response.xpath('//h4[@class=""]/a/@href').extract()
        hits_pattern = '<span class="read-num">阅读数：([0-9]{1,})</span>'
        comments_pattern = '<span class="read-num">评论数：([0-9]{1,})</span>'
        item['hits'] = re.compile(hits_pattern).findall(response.body.decode('utf-8'))
        item['comments'] = re.compile(comments_pattern).findall(response.body.decode('utf-8'))
        # 通过yield语句返回item，再次调用parse_item方法将继续执行yield语句之后的内容
        yield item
        url_split = response.url.split('/')
        if len(url_split) is not 4:
            return  # 若当前页不是博文列表首页，则结束此次调用
        # 获取该用户的博文总页数
        archive_pattern1 = '<ul class="archive-list">(.*?)</ul>'
        archive_block = re.compile(archive_pattern1, re.S).findall(response.body.decode('utf-8'))
        archive_pattern2 = '<span class="count float-right">(.*?)篇</span>'
        archive_list = re.compile(archive_pattern2).findall(archive_block[0])
        # 计算文章总数
        new_list = [int(i) for i in archive_list]
        article_num = sum(new_list)
        # 通过文章数/每页显示数得到总页数
        page_num = article_num//20 + 1 if article_num/20 > article_num//20 else article_num//20
        for i in range(2, int(page_num)+1):
            # 构造下一页博文列表的链接
            next_url = response.url + '/article/list/' + str(i)
            yield Request(next_url, callback=self.parse_item, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; \
            WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36 Maxthon/5.1.3.2000'})

        # return item
