# -*- coding: utf-8 -*-
# TODO: crawl content in qiushibaike.com
# author=QIUKU

import re
import urllib.request
import urllib.error
from gener_func import *


def get_content(proxy_addr, url, page_index):
	# 0. 调用 use_proxy 爬取url对应的网页
	data = use_proxy(proxy_addr=proxy_addr, url=url)
	# 1. 构建正则表达式
	pattern_user = '<h2>\n?(.*?)\n?</h2>'
	pattern_content = '<div class="content">\n?<span>(.*?)</span>'
	# 2. 匹配提取需要的内容
	user_list = re.compile(pattern_user).findall(data)
	content_list = re.compile(pattern_content, re.S).findall(data)
	# 3. 保存提取到的内容
	fh = open('wiki-content/wiki-' + str(page_index) + '.txt', 'w', encoding='utf-8')
	for user, content in zip(user_list, content_list):
		fh.write('发布用户:' + user + '\n')
		fh.write('段子内容:' + content + '\n')
		fh.write('---------------------------------------------\n')
	fh.close()


if __name__ == '__main__':
	for index in range(1, 10):
		proxy_addr_ = '61.135.217.7:80'
		url_ = 'https://www.qiushibaike.com/8hr/page/' + str(index)
		get_content(proxy_addr=proxy_addr_, url=url_, page_index=index)
