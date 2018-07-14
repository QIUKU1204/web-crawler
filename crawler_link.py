# -*- coding: utf-8 -*-
# TODO: crawl links on origin web-page
# author=QIUKU

import re
import urllib.request
import urllib.error
from gener_func import *


def get_link(proxy_addr, url_origin):
	# 0. 调用 use_proxy 爬取初始url网页
	data = use_proxy(proxy_addr=proxy_addr, url=url_origin)
	# 1. 构建提取链接的正则表达式
	pattern = '(//[^\s";]+\.[\w/]*)'
	# 2. 匹配提取网页源码中的url链接
	links = re.compile(pattern).findall(data)
	# 3. 使用集合set的自动去重功能
	link_list = list(set(links))
	return link_list


if __name__ == '__main__':
	url_ = 'https://blog.csdn.net/'
	proxy_addr_ = '61.135.217.7:80'
	link_list_ = get_link(proxy_addr=proxy_addr_, url_origin=url_)
	for link in link_list_:
		print('http:' + link)
