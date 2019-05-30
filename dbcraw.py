#code=utf-8
import requests
from bs4 import BeautifulSoup
from re import compile
import time
import random

def dbcrawer(name):
	headers = {
	"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
	}

	#创建会话窗口
	session = requests.Session()
	#模拟登陆，可利用cookie

	data1 = {
	'name':'13246812392',
	'password':'a123451234',
	'remember':'false'
	} 
	url1 = r'https://accounts.douban.com/j/mobile/login/basic'
	session.post(url1,data=data1,headers=headers)

	#搜索电影
	url3 = r'movie.douban.com/subject_search?'
	data3 = {
	'cat':'1002',
	'search_text':name
	}
	res3 = session.get(url3,headers=headers,params=data3)#在窗口输个网址,res3是对象.url是网址,.text是内容(.content内容.encode编码),还能查头等
	#text是自动编码content是字节码(给出子节点,若已经搜索出节点用str);非必要，在最终影评页面为必要,中文
	resp3 = BeautifulSoup(res3.content.decode('utf-8'),features="html.parser")#解析方法？

	#找到目标电影即首项
	#url4 = resp3.find("div",class_='result-list').find("a",href=True).attrs['href']#class是关键字,使用a['href']无子节点为nonetype
	#目标电影链接和打开后链接不一致，分析发现每部电影对应一个id(sid)，其他都一样
	url4 = resp3.find("div",class_='result-list').find("a",href=True)

	#找sid
	regex = compile(r'sid: (\d+)')
	sid = regex.search(str(url4)).group(1)

	#每页20条，共爬取25页
	for page in range(25):
		res5 = session.get(r"https://movie.douban.com/subject/"+sid+r'/comments?start='+str(page*20)+r'&amp;limit=20&amp;sort=new_score&amp;status=P',headers=headers)
		resp5 = BeautifulSoup(res5.content.decode('utf-8'),features="html.parser")
		#爬取影评
		with open(name+'dbreview.txt','a',encoding='utf-8') as rv:
			sho5 = resp5.find_all("span",class_='short')#注意下划线，否则是re方法
			for so in sho5:
				rv.write(so.text)#此处获得的是tag的集合，循环获得字符串 [].string/text，text更优string多个返回none
		#爬取评分和日期
		scores = compile(r'allstar\d{2} rating" title="(\w+)"').finditer(res5.text)
		dates = compile(r'comment-time " title="(\d{4})-(\d{2})-(\d{2}) ').finditer(res5.text)
		with open(name+'dbscores.txt','a',encoding='utf-8') as sc:
			for score,date in zip(scores,dates):
				sc.write(score.group(1)+' '+date.group(1)+'/'+date.group(2)+',')
				
	#用户信息耗时
	for page in range(25):
		res5 = session.get(r"https://movie.douban.com/subject/"+sid+r'/comments?start='+str(page*20)+r'&amp;limit=20&amp;sort=new_score&amp;status=P',headers=headers)
		resp5 = BeautifulSoup(res5.content.decode('utf-8'),features="html.parser")
		#获取用户页面
		urls = compile(r'(https://www.douban.com/people/\w+)/" class').finditer(res5.text)
		for url in urls:
			res11 = session.get(url.group(1),headers=headers)
			resp11 = BeautifulSoup(res11.content.decode('utf-8'),features="html.parser")
			#爬取地区
			with open(name+'dbplaces.txt','a',encoding='utf-8') as plc:
				try:
					pl = resp11.find('div',class_='user-info').find('a').text
					plc.write(pl+' ')
				except AttributeError:
					pass
			#爬取用户豆龄
			with open(name+'dby.txt','a',encoding='utf-8') as dy:
				try:
					dby = compile(r'(\d{4})-(\d{2})-(\d{2})加入').search(res11.text)
					dy.write(str((2019-int(dby.group(1)))*12+6-int(dby.group(2)))+' ')
				except AttributeError:
					pass
			#time.sleep(4+random.random())
				
	


	


