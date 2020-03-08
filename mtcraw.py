#code=utf-8

import requests
from bs4 import BeautifulSoup
from re import compile
import time
import random
from fake_useragent import UserAgent

def mtcrawer(name):
	headers = {
	"User-Agent": UserAgent().random,
	}
	session = requests.Session()
	r1 = session.get(r'http://service-channel.mtime.com/Search.api?Ajax_CallBack=true&Ajax_CallBackType=Mtime.Channel.Services&Ajax_CallBackMethod=GetSuggestObjs&Ajax_CrossDomain=1&Ajax_RequestUrl=http%3A%2F%2Fwww.mtime.com%2F&t=1561530087063&Ajax_CallBackArgument0='+name+r'&Ajax_CallBackArgument1=365&Ajax_CallBackArgument2=0&_=1561530069025',headers=headers)
	res1 = r1.text
	id1 = compile(r'"id":(\d+)').search(res1).group(1)
	for page in range(10):
		res1=session.get(r'https://movie.mtime.com/'+id1+r'/reviews/short/new-'+str(page)+r'.html',headers=headers)
		resp1 = BeautifulSoup(res1.content.decode('utf-8'),features="html.parser")
		with open(name+'\\'+name+'dbreview.txt','a',encoding='utf-8') as rv:
			sho5 = resp1.find_all('h3')
			for so in sho5:
				rv.write(so.text)

if __name__ == '__main__':
	mtcrawer('复仇者联盟4')
