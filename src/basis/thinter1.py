# coding = utf-8
'''
Created on 2016年12月4日
@author: 陈应龙
'''

import tkinter as tk

class App:
	def __init__(self,master):
		frame = tk.Frame(master)
		frame.pack(side=tk.RIGHT,padx=10,pady=10)

		self.hi_there = tk.Button(frame,text='打招呼',bg='black',fg='white',command=self.say_hi)
		self.hi_there.pack()

	def say_hi(self):
		print('哈哈哈，我就爱这个色色的世界！')


root = tk.Tk()
app = App(root)

root.mainloop()

