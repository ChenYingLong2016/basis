# coding = utf-8
'''
Created on 2016年11月23日
@author: 陈应龙
'''

'''
编写一个不可改变的自定义列表，要求记住列表中每个
元素被访问的次数
这个还差功能就是列表可以删除和增加，代码怎么写？
'''

class Countlist:
	def __init__(self,*args):
		self.values = [x for x in args]
		self.count = {}.fromkeys(range(len(self.values)),0)
	def __len__(self):
		return len(self.values)
	def __getitem__(self,key):
		self.count[key] += 1
		return self.values[key]
c1 = Countlist(1,3,5,7,9)
c2 = Countlist(0,2,4,6,8)
print(c1[1]) #第一次调用列表第二个元素值
print(c2[1]) #第一次调用列表第二个元素值
print(c1[1] + c2[2]) #第二次调用列表元素
print(c1.count) #输出的是列表里各个元素调用次数
print(c2.count) 
c1[1]
print(c1[1]) #第三次调用
