# coding = utf-8
'''
Created on 2016年12月3日
@author: 陈应龙
'''

import tkinter as tk

app = tk.Tk()
app.title('第一个窗口标题')

theLabel = tk.Label(app,text='第二个窗口程序')
theLabel.pack()  #没有这一句上面就无法显示，窗口位置调整

app.mainloop() #必须有这话，才会显示窗口
