#coding:utf-8
from pyecharts import options as opts
from pyecharts.charts import Page, Parallel
from pyecharts.globals import SymbolType
from pyecharts.charts import Page, Pie
def db_months(movie_name):
	filename=movie_name+'\\'+movie_name+'dby.txt'
	with open(filename,'r+',encoding='utf-8') as f:
		year_1 = f.read()
		years=year_1.split()
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
	month_list=time.items()
	pie=(
		Pie()
		.add(
			"",month_list,radius=["40%", "75%"])
		.set_global_opts(
			title_opts=opts.TitleOpts(title="饼图" ,subtitle=None),
			toolbox_opts=opts.ToolboxOpts(is_show=True),
			legend_opts=opts.LegendOpts(
			orient="vertical", pos_top="15%", pos_left="2%"
			),
		 )
		.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
		)
	pie.render(movie_name+'\\'+movie_name+'douban饼图.html')
	
db_months('复仇者联盟4')



		

