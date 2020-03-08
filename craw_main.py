#code=utf-8
import os
from imdbcraw import *
from dbcraw import *
from mtcraw import *
from rtcraw import *
import threading
import time
from picmaker import *

def main(name):

	localtime = time.localtime(time.time())
	print(localtime)

	print('爬虫运行中...')
	targets = [mtcrawer,rtcrawer,dbcrawer,imdbcrawer]
	threads = []
	for target in targets:
		threads.append(threading.Thread(target=target,args=(name,)))
	for thread in threads:
		thread.start()
	for thread in threads:
		thread.join()
	
	localtime = time.localtime(time.time())

	#上面爬虫，下面出图
	showing_pics(name)

	print(localtime)
	print('完成')

if __name__ == '__main__':
	#单独爬+出图，括号内电影名
	main('大侦探皮卡丘')
