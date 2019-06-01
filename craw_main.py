#code=utf-8
from imdbcraw import *
from dbcraw import *
import threading
import time
def main():
	localtime = time.localtime(time.time())
	print(localtime)
	name = '海王'
	targets = [imdbcrawer,dbcrawer]
	threads = []
	for target in targets:
		threads.append(threading.Thread(target=target,args=(name,)))
	for thread in threads:
		thread.start()
	for thread in threads:
		thread.join()
	localtime = time.localtime(time.time())
	print(localtime)
	print('完成')
if __name__ == '__main__':
	main()
