#code=utf-8
import requests
from bs4 import BeautifulSoup
from re import compile
import time
import random

	
#获得影评页面
def imdbcrawer(name):
	headers = {
	"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
	}

	#创建会话窗口
	session = requests.Session()
	#模拟登陆，可利用cookie
	'''
	data1 = {
	'name':'13246812392',
	'password':'a123451234',
	'remember':'false'
	} 
	url1 = r'https://accounts.douban.com/j/mobile/login/basic'
	session.post(url1,data=data1,headers=headers)
	'''
	
	#搜索豆瓣电影
	url0 = r'https://www.douban.com/j/search_suggest?'
	data0 = {
	'debug':'true',
	'q':name
	}
	res0 = session.get(url0,headers=headers,params=data0)
	sid = compile(r'subject\\/(\d+)').search(res0.text).group(1)

	#进入豆瓣电影首页
	res2 = session.get('https://movie.douban.com/subject/'+sid,headers=headers)
	#获得电影的imdb的网址
	regex2 = compile(r'http://www.imdb.com/title/([a-zA-Z]*\d*)')
	mid = regex2.search(res2.text).group(1)

	url3 = r'https://www.imdb.com/title/'+mid+r'/reviews?spoiler=hide&sort=helpfulnessScore&dir=desc&ratingFilter=0'

	res3 = session.get(url3,headers=headers)
	resp3 = BeautifulSoup(res3.text,features="html.parser")

	mon={'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}
	DL=[]

	resp4 = resp3
	res4 = res3
	page = 0
	#每页25条，共爬20页500条
	while page<20:
		
		#爬取影评，筛去包含剧透的
		with open(name+'Dreview.txt','a',encoding='utf-8') as rv:
			lis4 = resp4.find_all("div",class_="text show-more__control")#获得标签集合
			for li in lis4:
				rv.write(li.text)
			
		
		#爬取评分
		with open(name+'Dscores.txt','a',encoding='utf-8') as sc:
			scores = compile(r'<span>(\d+)</span>').finditer(res4.text)
			dates = compile(r'<span class="review-date">(\d+) ([a-zA-Z]+) (\d+)</span>').finditer(res4.text)
			for score,date in zip(scores,dates):
				sc.write(score.group(1)+' '+str(date.group(3))+'/'+str(mon[date.group(2)])+',')
				
		#获取ajax加载的数据	
		try:
			pk = resp4.find('div',class_='load-more-data').attrs['data-key']
		except:
			print('imdb 影评数不足,豆瓣还在努力')
		try:
			url4 = r'https://www.imdb.com/title/'+mid+r'/reviews/_ajax?sort=helpfulnessScore&dir=desc&spoiler=hide&ratingFilter=0&ref_=undefined&paginationKey='+pk#mbffakl4gd45zswcrfg4cbaqu4ovkuqheyjg2efoy75dmv4chur2imliyopd6affyecdbnt6v7vsg
			res4 = session.get(url4,headers=headers)
			resp4 = BeautifulSoup(res4.text,features="html.parser")
		except:
			pass
		page += 1

	#最后运行D龄

	resp4 = resp3
	res4 = res3
	page = 0	
	while page<20:
		#爬取D龄,耗时
		with open(name+'Dy.txt','a',encoding='utf-8') as dy:
			regex10 = compile(r'/user/\w+/')#开发者工具所得与requests所得不同
			sites = regex10.findall(res4.text)
			for site in sites:
				try:
					res11 = session.get(r'https://www.imdb.com'+site,headers=headers)
					regex11 = compile(r'IMDb member since ([a-zA-Z]+) (\d+)')
					rdl = regex11.search(res11.text)
					dl = (2019-int(rdl.group(2)))*12+(6-mon[rdl.group(1)])
					dy.write(str(dl)+' ')
				except:
					pass
					
		#获取ajax加载的数据	
		try:
			pk = resp4.find('div',class_='load-more-data').attrs['data-key']
		except:
			print('imdb 影评数不足，豆瓣还在努力')
		try:
			url4 = r'https://www.imdb.com/title/'+mid+r'/reviews/_ajax?sort=helpfulnessScore&dir=desc&spoiler=hide&ratingFilter=0&ref_=undefined&paginationKey='+pk#mbffakl4gd45zswcrfg4cbaqu4ovkuqheyjg2efoy75dmv4chur2imliyopd6affyecdbnt6v7vsg
			res4 = session.get(url4,headers=headers)
			resp4 = BeautifulSoup(res4.text,features="html.parser")
		except:
			pass
		page += 1

			
if __name__ == '__main__':
	imdbcrawer('复仇者联盟4')
