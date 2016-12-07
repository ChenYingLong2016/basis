# coding = utf-8
'''
Created on 2016年12月4日
@author: 陈应龙
'''

from tkinter import *

def callback():
	var.set('你吹吧，有谁相信呢～')

root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set('成年人限制内容，未成年人请远离，\n到18岁以后才能看哦！')


textLabel = Label(frame1,textvariable=var,justify=LEFT)
textLabel.pack(side=LEFT)

photo = PhotoImage(file='1.gif')
imgLabel = Label(frame1,image=photo)
imgLabel.pack(side=RIGHT)

theButton = Button(frame2,text='我已满18岁',command=callback)
theButton.pack()

frame1.pack(padx=10,pady=10)
frame2.pack(padx=10,pady=10)


mainloop()
