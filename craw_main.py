#code=utf-8
import os
from imdbcraw import *
from dbcraw import *
import threading
import time
from ciyuntuChinese import *
from ciyuntuEnglish import *
from piedouban import *
from pieIMDB import *
from scoredb import *
from scoreD import *
from rediantu import *
def main(name):
	localtime = time.localtime(time.time())
	print(localtime)

	print('爬虫运行中...')
	targets = [imdbcrawer,dbcrawer]
	threads = []
	for target in targets:
		threads.append(threading.Thread(target=target,args=(name,)))
	for thread in threads:
		thread.start()
	for thread in threads:
		thread.join()
	
	localtime = time.localtime(time.time())

	#上面爬虫，下面出图
	ciyun_ch(name)
	ciyun_en(name)
	db_months(name)
	IMDB_months(name)
	dbscore(name)
	IMDBscore(name)
	hotpoint(name)

	print(localtime)
	print('完成')

if __name__ == '__main__':
	#单独爬+出图，括号内电影名
	main('大侦探皮卡丘')
