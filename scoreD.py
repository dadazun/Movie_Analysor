#coding:utf-8
from pyecharts import options as opts
from pyecharts.charts import Page, ThemeRiver
from pyecharts.globals import ThemeType
def IMDBscore(movie_name):
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
	themeriver=(
			   ThemeRiver(init_opts=opts.InitOpts(theme=ThemeType.WESTEROS))
			   .add(
				   ['好评','中评','差评'],data,singleaxis_opts=opts.SingleAxisOpts(type_="time", pos_bottom="10%"),
				   )
			   .set_global_opts(title_opts=opts.TitleOpts(title=movie_name+" IMDB评价分布主题河流图",subtitle=None)
			   ,toolbox_opts=opts.ToolboxOpts(is_show=True),
			   datazoom_opts=[opts.DataZoomOpts(is_show=True,range_start=0,range_end=100)])
			   )

	themeriver.render(movie_name+'\\'+movie_name+'IMDBScore.html')
if __name__ == '__main__':
	IMDBscore('大侦探皮卡丘')
			
	
