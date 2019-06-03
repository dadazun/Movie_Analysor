#coding:utf-8
from pyecharts import options as opts
from pyecharts.charts import Page, Parallel
from pyecharts.globals import SymbolType
from pyecharts.charts import Page, Pie
def IMDB_months(movie_name):
	filename=movie_name+'\\'+movie_name+'Dy.txt'
	with open(filename,'r+',encoding='utf-8') as f:
		year_1 = f.read()
		years=year_1.split()
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
	month_list=time.items()
	pie=(
		Pie()
		.add(
			"",month_list,radius=["40%", "75%"])
		.set_global_opts(
			title_opts=opts.TitleOpts(title=movie_name+" IMDB“D龄”分布图",subtitle='单位:月'),
			toolbox_opts=opts.ToolboxOpts(is_show=True),
			legend_opts=opts.LegendOpts(
			orient="vertical", pos_top="15%", pos_left="2%"
			),
		 )
		.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
		)
	pie.render(movie_name+'\\'+movie_name+'IMDB饼图.html')
	
IMDB_months('复仇者联盟4')



		

