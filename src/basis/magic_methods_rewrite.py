# coding = utf-8
'''
Created on 2016年11月17日
@author: 陈应龙
'''

'''魔法方法，总是被双下划线包围，如学过的__init__，
__init__这个方法返回值必须为None。这个方法的作用
终于想到了，就是函数必须被调用才会执行，可是这个方法
不需要调用也一样执行了。也就是说类里面不需要调用，
最先执行的就是__init__方法。'''

class Rectangle:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def getPeri(self):
		return (self.x + self.y) * 2
	def getArea(self):
		return self.x * self.y
rect = Rectangle(3,4)
print('长方形周长是：',rect.getPeri())
print('长方形面积是：',rect.getArea())


'''对象实例化调用的第一个方法是__new__,返回值是一个实例对象，
一般情况不需要重写__new__，需要重写的情况是继承一个不可改变对象，
如下面例子中str是程序默认字符串类，不可改变就需要这个方法重写,
这个可以说是新的构造一个方法'''
class Capstr(str):
	def __new__(cls,string):
		string = string.upper() #.upper()字符串方法把所有字符串变为大写
		return str.__new__(cls,string)
a = Capstr("I love nothing,do you understand!")
print(a)

