# coding = utf-8
'''
Created on 2016年11月12日
@author: 陈应龙
'''

#def函数必须有self，这是函数默认的第一个参数，把函数自身当成参数传递给调用者
class Ball:
	def setname(self,name):
		self.name = name
	def kick(self):
		#使用return比使用print要好，print只是为了程序员看，return代表程序返回值
		return '我是%s，该割小鸡鸡，谁踢我'%self.name
a = Ball()
a.setname('AA')
print(a.kick())
b = Ball()
b.setname('BB')
print(b.kick())
c = Ball()
c.setname('大兵')
print(c.kick())

#python魔法方法__init__，这只是其中一种,
#与上面相比，少了一行代码，而且可以直接传入参数
class Ball0:
	def __init__(self,name):
		self.name = name
	def kick(self):
		#使用return比使用print要好，print只是为了程序员看，return代表程序返回值
		return '我是%s，该割小鸡鸡，谁踢我'%self.name
d = Ball0('大兵')
print(d.kick())

'''
#私有变量和公有变量，在变量名前加双下横线就可以把变量变为私有变量
class Person():
	__name = '人'
p = Person()
#print(p.__name) 这返回错误没有__name属性
'''
#把类做如下改变就可以调用
class Person:
	__name = '人'
	def getName(self):
		return self.__name
p = Person()
#p.__name  这依然是没有这个属性
print(p.getName()) #当调用换成这样就可以调用__name变量，是类里自调用
#p.__Person__name  这个也是不可用形式
print(p._Person__name) #必须是一个下划线才可以，两个下划线就会报错。