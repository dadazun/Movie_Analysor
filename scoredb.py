#coding:utf-8
from pyecharts import options as opts
from pyecharts.charts import Page, ThemeRiver
from pyecharts.globals import ThemeType
def dbscore(movie_name):
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
	themeriver=(
			   ThemeRiver(init_opts=opts.InitOpts(theme=ThemeType.WESTEROS))
			   .add(
				   ['很差','较差','还行','推荐','力荐'],data,singleaxis_opts=opts.SingleAxisOpts(type_="time", pos_bottom="10%"),
				   )
			   .set_global_opts(title_opts=opts.TitleOpts(title=movie_name+" 豆瓣评价分布图" ,subtitle=None),
			   toolbox_opts=opts.ToolboxOpts(is_show=True),
			   datazoom_opts=[opts.DataZoomOpts(is_show=True,range_start=0,range_end=100)])
			   )

	themeriver.render(movie_name+'\\'+movie_name+'dbScore.html')
if __name__ == '__main__':
	dbscore('大侦探皮卡丘')
			
	
