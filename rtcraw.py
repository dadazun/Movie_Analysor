#code=utf-8
import requests
from bs4 import BeautifulSoup
from re import compile
import time
import random
from fake_useragent import UserAgent

def rtcrawer(name):
	headers = {
	"User-Agent": UserAgent().random,
	}
	session = requests.Session()
	#搜索豆瓣电影
	url0 = r'https://www.douban.com/j/search_suggest?'
	data0 = {
	'debug':'true',
	'q':name
	}
	res0 = session.get(url0,headers=headers,params=data0)
	sid = compile(r'subject\\/(\d+)').search(res0.text).group(1)

	#进入豆瓣电影首页
	res2 = session.get(r'https://movie.douban.com/subject/'+sid,headers=headers)
	#从豆瓣获得电影的imdb的网址
	regex2 = compile(r'https://www.imdb.com/title/([a-zA-Z]*\d*)')
	mid = regex2.search(res2.text).group(1)
	#从imdb获得电影的英文名
	r3 = session.get(r'https://www.imdb.com/title/'+mid+r'/')
	res3=BeautifulSoup(r3.text,features="html.parser")
	name000 = res3.find('h1').contents[0]
	name00 = str(name000)
	#修改为烂番茄链接的形式
	name0 = name00.lower().replace(': ','_').strip()

	for page in range(10):
		res2=session.get(r'https://www.rottentomatoes.com/m/'+name0+r'/reviews?page='+str(page),headers=headers)
		resp2=BeautifulSoup(res2.content.decode('utf-8'),features="html.parser")
		with open(name+'\\'+name+'Dreview.txt','a',encoding='utf-8') as rv:
			sho5=resp2.find_all('div',class_='the_review')
			for so in sho5:
				rv.write(so.text)
	

if __name__ == '__main__':
	rtcrawer('复仇者联盟4')
