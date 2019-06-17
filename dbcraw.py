#code=utf-8
import requests
from bs4 import BeautifulSoup
from re import compile
import time
import random
from fake_useragent import UserAgent

def dbcrawer(name):
	headers = {
	"User-Agent": UserAgent().random,
	}
	#创建会话窗口
	session = requests.Session()
	
	#模拟登陆(请输入用户的用户名与密码)
	data1 = {
	'name':'',
	'password':'',
	'remember':'false'
	} 
	url1 = r'https://accounts.douban.com/j/mobile/login/basic'
	session.post(url1,data=data1,headers=headers)
	#找到电影id(sid)
	url0 = r'https://www.douban.com/j/search_suggest?'
	data0 = {
	'debug':'true',
	'q':name
	}
	res0 = session.get(url0,headers=headers,params=data0)
	sid = compile(r'subject\\/(\d+)').search(res0.text).group(1)
	
	#每页20条，共爬取25页
	for page in range(25):
		try:
			res5 = session.get(r"https://movie.douban.com/subject/"+sid+r'/comments?start='+str(page*20)+r'&amp;limit=20&amp;sort=new_score&amp;status=P',headers=headers)
		except:
			print('豆瓣影评不足')
			break
		resp5 = BeautifulSoup(res5.content.decode('utf-8'),features="html.parser")
		#爬取影评
		with open(name+'\\'+name+'dbreview.txt','a',encoding='utf-8') as rv:
			sho5 = resp5.find_all("span",class_='short')#注意下划线，否则是re方法
			for so in sho5:
				rv.write(so.text)#此处获得的是tag的集合，循环获得字符串 [].string/text，text更优string多个返回none
		#爬取评分和日期
		scores = compile(r'allstar\d{2} rating" title="(\w+)"').finditer(res5.text)
		dates = compile(r'comment-time " title="(\d{4})-(\d{2})-(\d{2}) ').finditer(res5.text)
		with open(name+'\\'+name+'dbscores.txt','a',encoding='utf-8') as sc:
			for score,date in zip(scores,dates):
				sc.write(score.group(1)+' '+date.group(1)+'/'+date.group(2)+'/'+date.group(3)+',')
		time.sleep(4.8+random.random())
				
	#用户信息耗时
	for page in range(25):
		try:
			res5 = session.get(r"https://movie.douban.com/subject/"+sid+r'/comments?start='+str(page*20)+r'&amp;limit=20&amp;sort=new_score&amp;status=P',headers=headers)
		except:
			break
		resp5 = BeautifulSoup(res5.content.decode('utf-8'),features="html.parser")
		#获取用户页面
		urls = compile(r'(https://www.douban.com/people/\w+)/" class').finditer(res5.text)
		for url in urls:
			res11 = session.get(url.group(1),headers=headers)
			resp11 = BeautifulSoup(res11.content.decode('utf-8'),features="html.parser")
			#爬取地区
			with open(name+'\\'+name+'dbplaces.txt','a',encoding='utf-8') as plc:
				try:
					pl = resp11.find('div',class_='user-info').find('a').text
					pl2 = compile(r'[\u4e00-\u9fa5]+').search(pl).group()
					pl3 = compile(r'河北|山西|辽宁|吉林|黑龙江|江苏|浙江|安徽|福建|江西|山东|河南|湖北|广东|海南|湖南|四川|贵州|云南|陕西|甘肃|青海|台湾|内蒙古|广西|西藏|宁夏|新疆|台湾').sub('',pl)
					plc.write(pl3+' ')
				except:#AttributeError，以及网络问题
					pass
			#爬取用户豆龄
			with open(name+'\\'+name+'dby.txt','a',encoding='utf-8') as dy:
				try:
					dby = compile(r'(\d{4})-(\d{2})-(\d{2})加入').search(res11.text)
					dy.write(str((2019-int(dby.group(1)))*12+6-int(dby.group(2)))+' ')
				except:#AttributeError
					pass
			time.sleep(4.8+random.random())
			
if __name__ == '__main__':
	dbcrawer('憨豆特工')
			
	


	


