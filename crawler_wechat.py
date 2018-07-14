# -*- coding: utf-8 -*-
# TODO: crawl WeChat files
# author=QIUKU

import queue
import re
import threading
import time
import urllib.error
import urllib.request
import random
from gener_func import use_proxy, no_proxy

# 创建url队列与url列表
url_queue = queue.Queue()
url_list = []

# 爬虫伪装为浏览器
headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36 Maxthon/5.1.3.2000')
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)


class GETURL(threading.Thread):
	def __init__(self, key, page_start, page_end, proxy_addr, url_queue):
		threading.Thread.__init__(self)
		self.key = key
		self.page_start = page_start
		self.page_end = page_end
		self.proxy_addr = random.choice(self.IP_pool)
		self.url_queue = url_queue

	# IP代理池
	IP_proxy_pool = [
		{'ip': '111.155.116.219:8123'},
		{'ip': '122.114.31.177:808'},
		{'ip': '123.207.30.131:80'},
		{'ip': '110.73.11.227:8123'},
		{'ip': '124.65.238.166:80'}
	]

	def run(self):
		try:
			page = self.page_start
			# 编码关键词
			key_code = urllib.request.quote(self.key)
			page_code = urllib.request.quote('&page=')
			i = 1
			for page in range(self.page_start, self.page_end + 1):
				url = 'http://weixin.sogou.com/weixin?type=2&query=' + key_code + page_code + str(page)
				data_listpage = no_proxy(url)
				# 搜狗防爬机制较为严格，国内的免费代理IP一般均无效
				# data_listpage = use_proxy(self.proxy_addr, url)
				if data_listpage is None:
					print('访问超时，爬取内容为空！')
					exit(1)

				# 使用国内免费代理IP进行爬取时，会出现以下错误
				if str(data_listpage).find('访问过于频繁') != -1:
					print('访问过于频繁，导致爬取失败，请更换代理IP！')
					exit(1)

				fp = open('wechat-artilcles/list' + str(i) + '.html', 'wb')
				fp.write(data_listpage.encode('utf-8', 'ignore'))
				fp.close()

				pattern_listpage = '<div class="txt-box">.*?(http://.*?)"'
				url_list.append(re.compile(pattern_listpage, re.S).findall(data_listpage))
				# print(url_list)
				print('第 ' + str(i) + ' 页资源链接爬取成功')
				i += 1

			for i in range(0, len(url_list)):
				if url_list[i] is []:
					print('没有提取到文章链接, 无法执行入队列操作')
				# 等待线程2，合理分配资源
				time.sleep(5)
				for j in range(0, len(url_list[i])):
					url = url_list[i][j]
					url = url.replace('amp;', '')
					print('第' + str(i) + 'i' + str(j) + 'j' + '次入队列')
					self.url_queue.put(url)
					self.url_queue.task_done()

		except urllib.error.URLError as e:
			if hasattr(e, 'code'):
				print(e.code)
			if hasattr(e, 'reason'):
				print(e.reason)
			time.sleep(2)
		except Exception as e:
			print('exception:' + str(e))
			time.sleep(2)


class GETCONTENT(threading.Thread):
	def __init__(self, proxy_addr, url_queue):
		threading.Thread.__init__(self)
		self.proxy_addr = proxy_addr
		self.url_queue = url_queue

	def run(self):

		i = 1

		while (True):
			try:
				url = self.url_queue.get()
				data_article = no_proxy(url)
				# 搜狗防爬机制较为严格，国内的免费代理IP一般均无效
				# data_article = use_proxy(self.proxy_addr, url)
				fp = open('wechat-artilcles/article' + str(i) + '.html', 'wb')
				fp.write(data_article.encode('utf-8', 'ignore'))
				fp.close()

				print('第' + str(i) + '篇文章处理完成')
				i += 1

			except urllib.error.URLError as e:
				if hasattr(e, 'code'):
					print(e.code)
				if hasattr(e, 'reason'):
					print(e.reason)
				time.sleep(2)
			except Exception as e:
				print('exception:' + str(e))
				time.sleep(2)

		print('微信文章全部爬取完成')


class CONTROL(threading.Thread):
	def __init__(self, url_queue):
		threading.Thread.__init__(self)
		self.url_queue = url_queue

	def run(self):
		while (True):
			print('程序执行中...')
			time.sleep(30)
			if self.url_queue.empty():
				print('程序执行完毕！')
				exit()


if __name__ == '__main__':
	key = '人工智能'
	page_start = 1
	page_end = 2
	# TODO: 待完善，使用IP代理池，自动更换代理IP
	proxy_addr = '60.255.186.169:8888'
	# 创建线程1对象并启动
	t1 = GETURL(key=key, page_start=page_start, page_end=page_end, proxy_addr=proxy_addr, url_queue=url_queue)
	t1.start()
	# 创建线程2对象并启动
	t2 = GETCONTENT(proxy_addr=proxy_addr, url_queue=url_queue)
	t2.start()
	# 创建线程3对象并启动
	t3 = CONTROL(url_queue=url_queue)
	t3.start()

