#coding:utf-8
import os 
from pyecharts import options as opts
from pyecharts.globals import ChartType, SymbolType
from pyecharts.charts import Geo
from collections import Counter
import string
def hotpoint(movie_name):
	#读取城市数据
	with open(movie_name+'\\'+movie_name+'dbplaces.txt','r+',encoding='utf-8-sig') as f:
		heat_1 = f.read()
		for i in heat_1:
			if i in string.punctuation:
				heat_1=heat_1.replace(i,"")
		heat=heat_1.split()
		heat_dic=Counter(heat)
	#整理数据
	heat_list=[]
	for place,times in heat_dic.items():
		c_word=(place,times)
		heat_list.append(c_word)	
	#出图
	heat_map = (
			Geo()
			.add_schema(maptype="china")
			.add("",heat_list)
			.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
			.set_global_opts(
					visualmap_opts=opts.VisualMapOpts(),
					title_opts=opts.TitleOpts(title=movie_name+" 豆瓣观影热点图",subtitle=None)
			,toolbox_opts=opts.ToolboxOpts(is_show=True))
			)


	heat_map.render(movie_name+'\\'+movie_name+'dbhotpoint.html')
if __name__ == '__main__':
	hotpoint('复仇者联盟4')


