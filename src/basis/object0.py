# coding = utf-8
'''
Created on 2016年11月12日
@author: 陈应龙
'''

'''
类的三大特性，封装，继承，多态。
封装保护源码的安全，使用方便，减少代码量，而且可以使得多人共用一个代码块。
继承，一个新类可以继承其它类的方法
多态，同一个函数名在不同类里有不同功能
'''
#类名第一个字母必须大写，为了与函数区分
class Turtle():
	'类的一个例子'
	#属性
	weight = 10
	legs = 4
	shell = True
	mouth = '大嘴'
	color = 'green'

	#方法
	def climb(self):
		print('努力向前爬进行中......')

	def run(self):
		print('飞快的向前奔跑......')

	def bite(self):
		print('咬死你咬死你咬死......')

	def eat(self):
		print('吃饱才是第一要务^_^')

	def sleep(self):
		print('现在需要按时睡觉,晚安！')


#封装，类的调用，调用的是类里面的方法，也就是调用类里面的函数，这就是封装，只要调用方法名将就可以。
tt = Turtle()
tt.sleep()
tt.eat()
tt.bite()
tt.climb()
tt.run()
print(tt.legs) #直接调用类里面的一个属性Attribute


#继承,在类名括号加上已经存在的类，就会自动继承这个类有的各种方法
class MyList(list):
	pass
list0 = MyList()
list0.append(3)
list0.append(9)
list0.append(15)
print(list0)

#多态,同一个方法名，可是在不同类下，实现功能不一样
class A:
	def fun(self):
		return '我是小A....'
class B:
	def fun(self):
		return '我是小B....'
a = A()
b = B()
print(a.fun())
print(b.fun())