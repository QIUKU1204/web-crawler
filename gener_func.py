# -*- coding: utf-8 -*-
# TODO: some generic callable functions
# author=QIUKU

import urllib.request


def use_proxy(proxy_addr, url):
	import urllib.request
	# 0. 修改请求头, 伪装成浏览器爬取
	headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36 Maxthon/5.1.3.2000')
	# 1. 使用 ProxyHandler() 设置对应的代理服务器信息
	proxy = urllib.request.ProxyHandler({'http': proxy_addr})
	# 2. Create an opener object from a list of handlers
	httphd = urllib.request.HTTPHandler(debuglevel=1)
	httpshd = urllib.request.HTTPSHandler(debuglevel=1)
	opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler, httphd, httpshd)
	opener.addheaders = [headers]
	# 3. 使用 install_opener() 创建全局默认的 opener 对象
	urllib.request.install_opener(opener)
	try:
		# decode('utf-8') == str(data)
		data = urllib.request.urlopen(url, timeout=20).read().decode('utf-8')  # bytes -> str
		# data = opener.open(url).read().decode('utf-8')
		return data
	except urllib.request.URLError as e:
		if hasattr(e, 'code'):
			print(e.code)
		if hasattr(e, 'reason'):
			print(e.reason)


__all__ = [use_proxy]

if __name__ == '__main__':
	proxy_addr = '115.209.174.129:22532'
	url = 'http://www.xicidaili.com/'
	data_ = use_proxy(proxy_addr=proxy_addr, url=url)
	print(len(data_))
	urllib.request.urlretrieve(url, filename='6.html')
