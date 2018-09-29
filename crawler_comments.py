# -*- coding: utf-8 -*-
# TODO:批量爬取腾讯视频中某个视频的评论，并实现自动加载新评论
# author=QIUKU

import urllib.request
import http.cookiejar
import re
from gener_func import no_proxy

# 视频编号
vid = '2003591633'
# 爬取开始的评论ID
comid = '6423487579804267823'

# 构造相应的正则表达式
pattern_id = '"id":"(.*?)"'
pattern_user = '"nick":"(.*?)",'
pattern_content = '"content":"(.*?),'
# 第一层循环，每一次外层循环爬取一页
for i in range(1, 10):
	print('-' * 70)
	print('第' + str(i) + '页评论内容')
	# 构造爬取所需的url
	url = 'http://coral.qq.com/article/' + vid + '/comment?commentid=' + comid + '&reqnum=20'
	data = no_proxy(url)
	list_id = re.compile(pattern_id, re.S).findall(data)
	list_user = re.compile(pattern_user, re.S).findall(data)
	list_content = re.compile(pattern_content, re.S).findall(data)
	# 第二层循环，根据爬取结果提取并处理每条评论的信息，已知一页20条评论
	for j in range(0, len(list_user)):
		try:
			print('用户名：' + eval('u"' + list_user[j] + '"'))
		except Exception as e:
			print(e)
			print(list_user[j])

		try:
			print(str(j) + '.评论内容：\n' + eval('u"' + list_content[j]) + '')
		except Exception as e:
			print(e)
			print(list_content[j])

		print('\n')

	if len(list_id) is 0:
		print('...没有更多了')
		exit(0)
	# 将comid替换为当前页的最后一条评论的id，以实现自动加载
	comid = list_id[len(list_id) - 1]
