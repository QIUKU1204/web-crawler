# -*- coding: utf-8 -*-
# author=QIUKU

from scrapy.cmdline import execute
import os, sys

# 添加当前爬虫项目的绝对路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# 使用execute方法执行爬虫
execute(['scrapy', 'crawl', 'guanchaspider'])
