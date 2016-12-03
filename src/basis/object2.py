# coding = utf-8
'''
Created on 2016年11月13日
@author: 陈应龙
'''

#继承，括号里的类为父类
import random as r

class Fish:
	def __init__(self):
		self.x = r.randint(0,10)
		self.y = r.randint(0,10)

	def move(self):
		self.x -= 1
		print('我的位置是：',self.x,self.y)

class Goldfish(Fish):
	pass
class Carp(Fish):
	pass
class Salmon(Fish):
	pass
class Shark(Fish):
	def __init__(self):
		#Fish.__init__(self) 调用未绑定的父类方法，这里有一个和父类同样的方法，就会替代父类方法
		super().__init__() #调用父类方法
		self.hungry = True
	def eat(self):
		if self.hungry:
			print('吃货梦想就是一刻不停的吃')
			self.hungry = False
		else:
			print('太饱了，吃不下去！')

fish = Fish()
fish.move()
goldfish = Goldfish()
goldfish.move()
shark = Shark()
shark.eat()
shark.move()


#多重继承
class Base1:
	def foo1(self):
		print('我是foo1,我为Base1代言....')
class Base2:
	def foo2(self):
		print('我是foo2,我为Base2代言....')
class Base(Base1,Base2): #把多个父类放入括号就行，可是这样容易发生的问题就是出错不知道具体地方，因此尽量不要用这样的编码方式
	pass
c = Base()
c.foo1()
c.foo2()