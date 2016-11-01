# coding = utf-8
'''
Created on 2016年10月30日
@author: 陈应龙
'''

from Tkinter import *

root = Tk()
lable = Label(root,text='',fg='',font=('',13))
lable.pack()
text1 = Text(root,width=20,height=5,font=('',13))

text2 = Text(root,width=20,height=5,font=('',13))
text2.insert(END,'')
button = Button(text='',fg='black')
lable.pack()
text1.pack()
text2.pack()
button.pack()
mainloop()