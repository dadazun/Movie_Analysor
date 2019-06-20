#coding:utf-8
from pyecharts import options as opts
from pyecharts.charts import Page, Parallel, Pie, WordCloud, ThemeRiver, Geo
from pyecharts.globals import SymbolType, ChartType, ThemeType
from pyecharts import *
import jieba
import string
from collections import Counter
from wordcloud import STOPWORDS
from textblob import TextBlob
from snownlp import SnowNLP

def showing_pics(movie_name):
	#生成页面
	page=(
		Page(page_title=movie_name)
		)
		
	#豆瓣用户豆龄图
	#读取用户数据
	filename=movie_name+'\\'+movie_name+'dby.txt'
	with open(filename,'r+',encoding='utf-8') as f:
		year_1 = f.read()
		years=year_1.split()
	#进行分层分类
	time={'0<x<=25':0,'25<x<=50':0,'50<x<=75':0,'75<x<=100':0,'100<x<=125':0,'x>125':0}
	for x in years:	
		if int(x) < 25:
			time['0<x<=25']+=1
		elif int(x) < 50:
			time['25<x<=50']+=1
		elif int(x) < 75:
			time['50<x<=75']+=1
		elif int(x) < 100:
			time['75<x<=100']+=1
		elif int(x) < 125:
			time['100<x<=125']+=1
		else:
			time['x>125']+=1
	#整理数据
	month_list1=time.items()
	#出图
	dbmonth=(
		Pie(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
		.add(
			"",month_list1,radius=["40%", "75%"])
		.set_global_opts(
			title_opts=opts.TitleOpts(title=movie_name+" 豆瓣用户“豆龄”分布图" ,subtitle='单位:月'),
			toolbox_opts=opts.ToolboxOpts(is_show=True),
			legend_opts=opts.LegendOpts(
			orient="vertical", pos_top="15%", pos_left="2%"
			),
		 )
		.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
		)
		
		
	#IMDB用户D龄图
	#读取用户数据
	filename=movie_name+'\\'+movie_name+'Dy.txt'
	with open(filename,'r+',encoding='utf-8') as f:
		year_1 = f.read()
		years=year_1.split()
	#进行分类分层
	time={'0<x<=40':0,'40<x<=80':0,'80<x<=120':0,'120<x<=160':0,'160<x<=200':0,'x>200':0}
	for x in years:	
		if int(x) < 40:
			time['0<x<=40']+=1
		elif int(x) < 80:
			time['40<x<=80']+=1
		elif int(x) < 120:
			time['80<x<=120']+=1
		elif int(x) < 160:
			time['120<x<=160']+=1
		elif int(x) < 200:
			time['160<x<=200']+=1
		else:
			time['x>200']+=1
	#整理
	month_list2=time.items()
	#出图
	Dmonth=(
		Pie(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
		.add(
			"",month_list2,radius=["40%", "75%"])
		.set_global_opts(
			title_opts=opts.TitleOpts(title=movie_name+" IMDB“D龄”分布图",subtitle='单位:月'),
			toolbox_opts=opts.ToolboxOpts(is_show=True),
			legend_opts=opts.LegendOpts(
			orient="vertical", pos_top="15%", pos_left="2%"
			),
		 )
		.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
		)
		
		
	#英文词云图
	#读取数据
	filename=movie_name+'\\'+movie_name+'Dreview.txt'
	with open(filename,'r+',encoding='utf-8') as f:
		rev_1 = f.read()
		#处理标点
		for i in rev_1:
			if i in string.punctuation:
				rev_1=rev_1.replace(i," ")
		#分词+统计
		words=rev_1.split()
		words_dic=Counter(words)
	#删除一些高频词
	file_del='ban.txt'
	with open(file_del,'r+',encoding='utf-8') as d:
		del_1=d.read()
		Ban_list = del_1.split('\n')
	#处理数据
	words_list=[]
	for word,time in words_dic.items():
		if word.lower() in Ban_list or time < 35:
			continue
		else:
			a_word=(word.title(),time)
			words_list.append(a_word)
	#出图
	Eng_wordcloud=(
             WordCloud(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
             .add("", words_list, word_size_range=[20, 100],shape="diamond")
             .set_global_opts(title_opts=opts.TitleOpts(title=movie_name+" WordCloud",subtitle=None)
             ,toolbox_opts=opts.ToolboxOpts(is_show=True))
             )
             
             
	#中文词云图
	#读取爬取的文本文件
	filename=movie_name+'\\'+movie_name+'Dbreview.txt'
	with open(filename,'r+',encoding='utf-8') as f:
		rev_2 = f.read()
		#中文分词
		cut_douban =" ".join(jieba.cut(rev_2,cut_all=False))
		list_douban = cut_douban.split(' ')
		copy_list = []
		for word in list_douban:
			copy_list.append(word)
		#删除长度为1的文本
		for word in copy_list:
			if len(word) == 1:
				list_douban.remove(word)	
	stop=[]
	review_dic=Counter(list_douban)
	#利用文件删除一些意义不大的词
	file_stop='删除.txt'
	with open(file_stop,'r+',encoding='utf-8') as s:
		stop_1=s.read()
		stop=stop_1.split('\n')
	#整理
	word_list=[]
	for words,times in review_dic.items():
		if words in stop or times<9:
			continue
		else:
			b_word=(words,times)
			word_list.append(b_word)
	#出图
	Chn_wordcloud=(
				 WordCloud(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
				 .add("", word_list, word_size_range=[20, 100],shape="diamond")
				 .set_global_opts(title_opts=opts.TitleOpts(title=movie_name+" 中文词云图",subtitle=None)
				 ,toolbox_opts=opts.ToolboxOpts(is_show=True))
				 )
	
	
	#豆瓣用户评分图
	#读取数据
	with open(movie_name+'\\'+movie_name+'dbscores.txt','r+',encoding='utf-8') as m:
		allthings = m.read().split(',')
		del allthings[-1]
		all_date=[]
		points_dic={}
		#按评价进行分类
		for div in allthings:
			point,date = div.split()
			if date not in all_date:
				points_dic[date]={'很差':0,'较差':0,'还行':0,'推荐':0,'力荐':0}
				all_date.append(date)
			if point == '很差':
				points_dic[date]['很差']+=1
			elif point == '较差':
				points_dic[date]['较差']+=1
			elif point == '还行':
				points_dic[date]['还行']+=1
			elif point == '推荐':
				points_dic[date]['推荐']+=1
			else:
				points_dic[date]['力荐']+=1
		#处理数据		
		data = []	
		for month, grade in points_dic.items():
			for hzc, num in grade.items():
				counting = []
				counting.append(month)
				counting.append(num)
				counting.append(hzc)
				data.append(counting)
	#出图
	dbpoints=(
			   ThemeRiver(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
			   .add(
				   ['很差','较差','还行','推荐','力荐'],data,singleaxis_opts=opts.SingleAxisOpts(type_="time", pos_bottom="10%"),
				   )
			   .set_global_opts(title_opts=opts.TitleOpts(title=movie_name+" 豆瓣评价分布图" ,subtitle=None),
			   toolbox_opts=opts.ToolboxOpts(is_show=True),
			   datazoom_opts=[opts.DataZoomOpts(is_show=True,range_start=0,range_end=100)])
			   )
		
		
	#IMDB评分图
	#处理爬取的数据
	with open(movie_name+'\\'+movie_name+'Dscores.txt','r+',encoding='utf-8') as m:
		allthings = m.read().split(',')
		del allthings[-1]
		all_date=[]
		points_dic={}
		#按分数进行分类
		for div in allthings:
			point,date = div.split()
			if date not in all_date:
				points_dic[date]={'好评':0,'中评':0,'差评':0}
				all_date.append(date)
			if int(point) <= 3:
				points_dic[date]['差评']+=1
			elif int(point) >= 7:
				points_dic[date]['好评']+=1
			else:
				points_dic[date]['中评']+=1
		#整理便于出图		
		data = []	
		for month, grade in points_dic.items():
			for hzc, num in grade.items():
				counting = []
				counting.append(month)
				counting.append(num)
				counting.append(hzc)
				data.append(counting)
	#出图
	Dpoints=(
			   ThemeRiver(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
			   .add(
				   ['好评','中评','差评'],data,singleaxis_opts=opts.SingleAxisOpts(type_="time", pos_bottom="10%"),
				   )
			   .set_global_opts(title_opts=opts.TitleOpts(title=movie_name+" IMDB评价分布主题河流图",subtitle=None)
			   ,toolbox_opts=opts.ToolboxOpts(is_show=True),
			   datazoom_opts=[opts.DataZoomOpts(is_show=True,range_start=0,range_end=100)])
			   )
	
			   
	#热点图
	#读取城市数据
	with open(movie_name+'\\'+movie_name+'dbplaces.txt','r+',encoding='utf-8-sig') as f:
		heat_1 = f.read()
		for i in heat_1:
			if i in string.punctuation:
				heat_1=heat_1.replace(i,"")
		heat=heat_1.split()
		heat_dic=Counter(heat)
	#处理一些热点图数据库中没有的城市（此txt还要不停壮大）
	with open('no city.txt','r+',encoding='utf-8-sig') as e:
		no_city = e.read()
		no_city_list=no_city.split(' ')
	#整理数据
	heat_list=[]
	for place,times in heat_dic.items():
		if place in no_city_list:
			continue
		c_word=(place,times)
		heat_list.append(c_word)	
	#出图,反复产生图，来处理乱填地区的情况
		try:
			heat_map = (
					Geo(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
					.add_schema(maptype="china")
					.add("",heat_list)
					.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
					.set_global_opts(
							visualmap_opts=opts.VisualMapOpts(),
							title_opts=opts.TitleOpts(title=movie_name+" 豆瓣观影热点图",subtitle=None)
					,toolbox_opts=opts.ToolboxOpts(is_show=True))
					)
		except:
			a=heat_list.pop(-1)	
			
	#中文情感分析图
	with open(movie_name+'\\'+movie_name+"dbreview.txt",'r',encoding='utf-8') as f:
		#读取影评文件
		text = f.read()
		s = SnowNLP(text)
		chn_senti = []
		#进行情感分析并记录数据
		for sent in s.sentences:
			chn_senti.append(SnowNLP(sent).sentiments)
	times={'0<=x<=0.25':0,'0.25<x<=0.5':0,'0.5<x<=0.75':0,'0.75<x<=1':0}
	for x in chn_senti:
		if x < 0 or x > 1:
			continue
		elif x <= 0.25:
			times['0<=x<=0.25']+=1
		elif x <= 0.5:
			times['0.25<x<=0.5']+=1
		elif x <= 0.75:
			times['0.5<x<=0.75']+=1
		else:
			times['0.75<x<=1']+=1
	scores_list=times.items()
	#出图
	ch_motion=(
		Pie(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
		.add(
			"",scores_list,radius=["40%", "75%"])
		.set_global_opts(
			title_opts=opts.TitleOpts(title=movie_name+"豆瓣用户评论情感分析图",subtitle=None),
			toolbox_opts=opts.ToolboxOpts(is_show=True),
			legend_opts=opts.LegendOpts(
			orient="vertical", pos_top="15%", pos_left="2%"
			),
		 )
		.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
		)
		
	#英文情感分析图
	with open(movie_name+'\\'+movie_name+"Dreview.txt",'r',encoding='utf-8') as f:
		#读取影评文件
		text = f.read()
		blob = TextBlob(text)
		eng_senti = []
		#进行情感分析并记录数据
		for sent in blob.sentences:
			eng_senti.append(sent.sentiment.polarity)
	time={'-1<=x<=-0.5':0,'-0.5<x<=0':0,'0<x<=0.5':0,'0.5<x<=1':0}
	for x in eng_senti:
		if x < -1 or x > 1:
			continue
		elif x <= -0.5:
			time['-1<=x<=-0.5']+=1
		elif x<= 0:
			time['-0.5<x<=0']+=1
		elif x<= 0.5:
			time['0<x<=0.5']+=1
		else:
			time['0.5<x<=1']+=1
	score_list=time.items()
	#出图
	en_motion=(
		Pie(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
		.add(
			"",score_list,radius=["40%", "75%"])
		.set_global_opts(
			title_opts=opts.TitleOpts(title=movie_name+"IMDB用户评论情感分析图",subtitle=None),
			toolbox_opts=opts.ToolboxOpts(is_show=True),
			legend_opts=opts.LegendOpts(
			orient="vertical", pos_top="15%", pos_left="2%"
			),
		 )
		.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
		)
		
		
	#将图加入页面中
	page.add(dbmonth,Dmonth)
	page.add(Chn_wordcloud,Eng_wordcloud)
	page.add(dbpoints,Dpoints)
	page.add(ch_motion,en_motion)
	try:
		page.add(heat_map)
	except:
		pass
	page.render(movie_name+'\\'+movie_name+'数据图.html')
	
if __name__ == '__main__':
	showing_pics('功夫')



		

