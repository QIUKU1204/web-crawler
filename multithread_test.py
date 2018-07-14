# -*- coding: utf-8 -*-
# TODO: Python multi-thread test with GIL
# TODO: 验证: 在GIL限制下，同一时刻CPython解释器中只能运行一个Python线程
# author=QIUKU

import threading
import time
import os
import datetime


class A(threading.Thread):
	def __init__(self):
		# 初始化该线程对象
		threading.Thread.__init__(self)

	def run(self):
		for i in range(101):
			print("我是线程A")
			print(threading.currentThread())
		# time.sleep(1)


class B(threading.Thread):
	def __init__(self):
		# 初始化该线程对象
		threading.Thread.__init__(self)

	def run(self):
		for i in range(101):
			print("我是线程B")
			print(threading.currentThread())
		# time.sleep(1)


t1 = A()
t2 = B()
# 多线程 - 验证: 在GIL限制下，同一时刻CPython解释器只能运行一个Python线程
t1.start()
t2.start()
# 单线程
# t1.run()
# t2.run()
