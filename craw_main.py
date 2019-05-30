#code=utf-8
from imdbcraw import *
from dbcraw import *
import threading
def main():
	name = '复仇者联盟4'
	t1 = threading.Thread(target=imdbcrawer,args=(name,))
	t2 = threading.Thread(target=dbcrawer,args=(name,))
	t1.start()
	t2.start()
	t1.join()
	t2.join()
if __name__ == '__main__':
	main()
