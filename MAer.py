#coding = utf-8
import tkinter as tk
import os

#设置按键command对应函数
def search_movie():
	#检查所要搜索的电影是否在数据库中
	movie_name=moviename.get()
	c_add = os.getcwd()
	if movie_name == '' or movie_name =='请输入电影名':
	    return 0
	else:
		path = c_add+'/'+movie_name
		if os.path.exists(path):
			c_add = os.getcwd()
			#此处要改！！！改掉图片名！！！
			os.startfile(c_add + '/' + movie_name+'/图1.png')
			os.startfile(c_add + '/' + movie_name+'/图2.png')
		#若不在库中，则弹窗提醒
		else:
			remind = tk.Toplevel()
			remind.title('Error!')
			remind_bg=tk.Canvas(remind, bg='white',height=210,width=350)
			remind_bg.pack()
			message = tk.Label(remind, text='你所搜索的电影信息尚未收集!',
			    font=('微软雅黑',18),bg='white',fg = '#00bff3')#00bff3
			message.place(x=175,y=85,anchor='center')
			
			back_file = tk.PhotoImage(file = 'back.png')
			backbutton = tk.Button(remind, image = back_file, command=remind.destroy)
			backbutton.place(x=175,y=150,anchor='center')
			remind.mainloop()



#设置窗口，名字，背景，标题等
window = tk.Tk()
window.title('电影分析')
window_bg = tk.Canvas(window, bg='white',height = 480,width = 800)
window_bg.pack(fill = 'both')
title_file=tk.PhotoImage(file= 'title.png')
title = tk.Label(window,image=title_file)
title.place(x=400,y=100,anchor='center')
writer=tk.Label(window,
    text = '制作者：Py三人行'+'\n'+'Movie Analyzer',
    font=('微软雅黑',10),
    bg = 'white',fg = '#66ccff'
    )
writer.place(x=400,y=400,anchor='center')

#设置搜索框以及对应文本
moviename = tk.StringVar()
moviename.set('请输入电影名')
entry_moviename = tk.Entry(window,textvariable=moviename,bd=2,font=('微软雅黑',22))
entry_moviename.place(x=360,y=250,anchor='center')
#设置搜索按键
search_file=tk.PhotoImage(file='search.png')
searchbutton = tk.Button(window,
    image=search_file,
    command = search_movie)
searchbutton.place(x=575,y=248,anchor='center')
#必要！
window.mainloop()
