#code=utf-8
from imdbcraw import *
from dbcraw import *
import threading
import time
def main():
	localtime = time.localtime(time.time())
	print(localtime)
	name = '海王'
	t1 = threading.Thread(target=imdbcrawer,args=(name,))
	t2 = threading.Thread(target=dbcrawer,args=(name,))
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	localtime = time.localtime(time.time())
	print(localtime)
	print('完成')
if __name__ == '__main__':
	main()
