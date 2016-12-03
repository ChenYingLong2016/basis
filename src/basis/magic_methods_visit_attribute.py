# coding = utf-8
'''
Created on 2016年11月19日
@author: 陈应龙
'''

'''没有x = property(getsize,setsize,delsize)，
del c.x后的c.size输出还是10，加入之后，如下面
就会报出没有c.size属性错误
class C:
	def __init__(self,size=10):
		self.size = size
	def getsize(self):
		return self.size
	def setsize(self,value):
		self.size = value
	def delsize(self):
		del self.size
	
c = C()
c.x = 1
print(c.x) #结果为1
print(c.size) #结果为10
del c.x
#print(c.size) #结果依然为10
'''
class C:
	def __init__(self,size=10):
		self.size = size
	def getsize(self):
		return self.size
	def setsize(self,value):
		self.size = value
	def delsize(self):
		del self.size
	x = property(getsize,setsize,delsize)
c = C()
c.x = 1
print(c.x) #结果为1
print(c.size) #结果为1
del c.x
#print(c.size) AttributeError: 'C' object has no attribute 'size'

'''不同参数传入调用的是不同函数
__getattr__(self,name)
定义当用户试图获取一个不存在属性时行为
__getattribute__(self,name)
定义当该类的属性被访问时行为
__setattr__(self,name,value)
定义当一个属性被设置时行为
__delattr__(self,name)
定义当一个属性被删除时行为
'''
#这些方法在调用时容易陷入递归调用的死循环，要小心
class A:
	def __getattribute__(self,name):
		print('getattribute')
		return super().__getattribute__(name)
	def __getattr__(self,name):
		print('getattr')
	def __setattr__(self,name,value):
		print('setattr')
		return super().__setattr__(name,value)
	def __delattr__(self,name):
		print('delattr')
		return super().__delattr__(name)
a = A()
print(a.x) #没有print输出getattribute,getattr,有之后多输出一个None
a.x = 1
print(a.x)  #没有print输出getattribute，有输出getattribute和1
del a.x #输出delattr

'''输入宽高求面积
super()没有后括号，报错为
TypeError:  expected 2 arguments, got 1
所以括号一定要记得输入。
原理上我还没有理解。'''
class Rectangle:
	def __init__(self,width=0,height=0):
		self.width = width
		self.height = height
	def __setattr__(self,name,value):
		if name == 'square':
			self.width = value
			self.height = value
		else:
			super().__setattr__(name,value)
	def getArea(self):
		return self.width * self.height
rect = Rectangle(3,4)
print('长方形面积是：',rect.getArea())
print(rect.__dict__)
rect.square = 5
print(rect.width)
print(rect.height)
print(rect.getArea())
print(rect.__dict__)
