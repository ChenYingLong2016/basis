# coding = utf-8
'''
Created on 2016年12月4日
@author: 陈应龙
'''

import tkinter as tk

app = tk.Tk()
app.title('标题窗口')

theLabel = tk.Label(app,text='内容页窗口')
theLabel.pack()

app.mainloop()
