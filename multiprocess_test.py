# -*- coding: utf-8 -*-
# TODO:
# author=QIUKU

import os
import random
import time
import subprocess
from multiprocessing import Process,Pool


# 子进程要执行的函数
def run_proc(param):
	print('Run child process %s (%s)...' % (param, os.getpid()))
	for index in range(0, 23333):
		print('我是：', index)


def long_time_task(name):
	print('Run task %s (%s)...' % (name, os.getpid()))
	start = time.time()
	time.sleep(random.random() * 3)
	end = time.time()
	print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
	'''创建单个进程'''
	# print('Parent process %s.' % os.getpid())
	# cp = Process(target=run_proc, args=('xigua',))
	# print('Child process start.')
	# start_time = datetime.datetime.now()
	# cp.start()
	# cp.join()
	# end_time = datetime.datetime.now()
	# running_time = (end_time - start_time).total_seconds()
	# print("total running time is:", running_time, 'seconds')
	# print('Child process end.')

	'''创建进程池'''
	# print('Parent process %s.' % os.getpid())
	# process_pool = Pool()  # Pool的默认大小是CPU的核数
	# for i in range(5):
	# 	process_pool.apply_async(func=long_time_task, args=(i,))
	# print('Waiting for all subprocesses done...')
	# process_pool.close()   # 不允许向进程池中添加新的进程
	# process_pool.join()    # 等待所有子进程执行完毕
	# print('All subprocesses done.')

	'''使用subprocess 模块启动子进程'''
	# print('$ nslookup www.python.org')
	# r = subprocess.call(['nslookup', 'www.python.org'])  # 启动一个子进程，并让其调用系统函数nslookup
	# print('Exit code:', r)

	print('$ nslookup')
	p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
	print(output.decode('utf-8', 'ignore'))
	print('Exit code:', p.returncode)

	'''进程间通信(Queue、Pipes)'''
	# 操作系统提供了很多机制来实现进程间的通信
	# multiprocessing 模块则包装了这些底层的机制，提供Queue、Pipes等多种方式来交换数据
