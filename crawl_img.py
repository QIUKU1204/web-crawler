# -*- coding: utf-8 -*-
# TODO: crawl smartPhone images in JD.com
# author=QIUKU

import re
import urllib.request
import urllib.error


def crawl_img(url, page_index):
	# bytes data
	html_origin = urllib.request.urlopen(url, timeout=5).read()
	html_origin = str(html_origin)  # bytes -> str

	pat1 = '<div id="plist".+?<div class="page clearfix">'
	html_filter = re.compile(pat1).findall(html_origin)
	html_filter = html_filter[0]

	# 此处使用()的作用: 匹配返回的列表的元素只含()中的内容，括号之前的内容和括号之后的内容都不会出现
	pat2 = '<img width="220" height="220" data-img="1" data-lazy-img="//(.+?\.jpg)">'
	img_urls = re.compile(pat2).findall(html_filter)
	pat3 = '<img width="220" height="220" data-img="1" data-lazy-img="//(.+?\.jpg)">'
	img_urls.extend(re.compile(pat3).findall(html_filter))
	print(img_urls)

	x = 1
	for img_url in img_urls:
		img_name = 'C:/Users/QIUKU/PycharmProjects/web-crawler/jd-mobilephone-imgs/' + str(page_index) + '-' + str(x) + '.jpg'
		img_url = 'http://' + img_url

		try:
			urllib.request.urlretrieve(url=img_url, filename=img_name)
		except urllib.error.URLError as e:
			if hasattr(e, 'code'):
				print(e.code)
				x += 1
			if hasattr(e, 'reason'):
				print(e.reason)
				x += 1
		x += 1


if __name__ == '__main__':
	for index in range(1, 160):
		url_img = 'https://list.jd.com/list.html?cat=9987,653,655&page=' + str(index)
		crawl_img(url_img, index)
