# coding = utf-8
'''
Created on 2016年11月14日
@author: 陈应龙
'''

'''类中的一些关键字'''
#issubclass,判断连个类是否有关系，有关系True，没关系False
class A:
	pass
class B(A):
	pass
print(issubclass(B,A)) #返回值为True
print(issubclass(B,B)) #返回值为True 
print(issubclass(B,object)) #返回值为True

class C:
	def __init__(self,x=0):
		self.x = x
c = C()
print(issubclass(B,C)) #返回值为False

#hasattr判断属性有无，有为True，没有为False
print(hasattr(c,'x')) #返回值为True
#print(hasattr(c,x))  #没有引号为错误写法

#getattr获得属性值，没有该属性报AttributeError：错误
print(getattr(c,'x'))
#在后面可以加上错误说明
print(getattr(c,'y','访问属性不存在.....'))

#setattr增加属性
setattr(c,'y','zuo')
print(getattr(c,'y','访问属性不存在.....'))

#delattr删除该属性
delattr(c,'y')
'''第一次删除为真,需要再加一次删除，程序才会报错
delattr(c,'y')'''

'''这个同样代码在python3.5版本里已经是不能用了，这个改变在文档里有说明，
错误原因为AttributeError: 'D' object has no attribute 'size'，
这一个错误我是还没有相通。
class D:
	def _init__(self,size=10):
		self.size = size
	def getSize(self):
		return self.size
	def setSize(self,value):
		sefl.size = value
	def delSize(self):
		del self,size
	x = property(getSize,setSize,delSize)
d = D()
d.getSize()
d.x
d.x = 16
d.size
d.getSize()
del d.x
'''
