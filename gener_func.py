# -*- coding: utf-8 -*-
# TODO: some generic callable functions
# author=QIUKU

import urllib.request


def use_proxy(proxy_addr, url):
	# 0. 修改请求头, 伪装成浏览器
	headers = ('User-Agent',
	           'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36 Maxthon/5.1.3.2000')
	# 1. 使用 ProxyHandler() 设置对应的代理服务器信息
	proxy = urllib.request.ProxyHandler({'http': proxy_addr})
	# httphd = urllib.request.HTTPHandler(debuglevel=1)
	# httpshd = urllib.request.HTTPSHandler(debuglevel=1)
	# 2. Create an opener object from a list of handlers
	opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
	opener.addheaders = [headers]
	# 3. 使用 install_opener() 创建全局默认的 opener 对象
	urllib.request.install_opener(opener)
	try:
		# decode('utf-8') == str(data)
		data = urllib.request.urlopen(url, timeout=10).read().decode('utf-8', 'ignore')  # bytes -> str
		# data = opener.open(url).read().decode('utf-8')
		return data
	except urllib.request.URLError as e:
		if hasattr(e, 'code'):
			print(e.code)
		if hasattr(e, 'reason'):
			print(e.reason)


def no_proxy(url):
	headers = ('User-Agent',
	           'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36 Maxthon/5.1.3.2000')
	# 开启 DebugLog 调试日志
	# httphd = urllib.request.HTTPHandler(debuglevel=1)
	# httpshd = urllib.request.HTTPSHandler(debuglevel=1)
	# opener = urllib.request.build_opener(httphd, httpshd)
	opener = urllib.request.build_opener()
	opener.addheaders = [headers]
	urllib.request.install_opener(opener)
	try:
		data = urllib.request.urlopen(url, timeout=10).read().decode('utf-8', 'ignore')
		return data
	except urllib.request.URLError as e:
		if hasattr(e, 'code'):
			print(e.code)
		if hasattr(e, 'reason'):
			print(e.reason)


def generator():
	print('BeiJing!')
	yield 5
	print('ShangHai!')
	yield 6


__all__ = ['use_proxy', 'no_proxy', 'generator']

if __name__ == '__main__':
	# # TODO: 待完善，使用IP代理池，自动更换代理IP
	# proxy_addr_ = '60.255.186.169:8888'
	# url_ = 'http://www.xicidaili.com/'
	# data_ = use_proxy(proxy_addr=proxy_addr_, url=url_)
	# print(len(data_))
	# urllib.request.urlretrieve(url=url_, filename='HTML-Page/6.html')

	g = generator()
	# g.__next__()  # 输出'BeiJing!'
	# g.__next__()  # 输出'ShangHai!'
	print(g.__next__())  # 输出'BeiJing!'和5
	print(g.__next__())  # 输出'ShangHai!'和6
	# a = g.__next__()  # 输出'BeiJing!'
	# b = g.__next__()  # 输出'ShangHai!'
	# print(a)  # 输出5
	# print(b)  # 输出6
