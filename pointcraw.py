#code=utf-8
import requests
from bs4 import BeautifulSoup
from re import compile
import time
import random

def pointcrawer(name):
#等待imdbcraw创建文件夹
	time.sleep(0)
	r0 = requests.get(r'https://maoyan.com/query?kw='+name)
	mid = compile('a href="/films/(\d+)"').search(r0.text).group(1)
	print(mid)

if __name__ == '__main__':
	pointcrawer('复仇者联盟4')
