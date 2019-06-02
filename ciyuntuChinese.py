#coding:utf-8
import matplotlib.pyplot as plt
from pyecharts import options as opts
from pyecharts.charts import Page, WordCloud
import jieba
import string
from collections import Counter
from wordcloud import STOPWORDS
def ciyun_ch(movie_name):
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
		if words in stop:
			continue
		else:
			b_word=(words,times)
			word_list.append(b_word)
	#出图
	words_cloud=(
				 WordCloud()
				 .add("", word_list, word_size_range=[20, 100],shape="diamond")
				 .set_global_opts(title_opts=opts.TitleOpts(title="WordCloud-Review",subtitle=None)
				 ,toolbox_opts=opts.ToolboxOpts(is_show=True))
				 )
	words_cloud.render(movie_name+'\\'+movie_name+'中文词云图.html')
	
ciyun_ch('复仇者联盟4')





