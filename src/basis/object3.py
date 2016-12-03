# coding = utf-8
'''
Created on 2016年11月14日
@author: 陈应龙
'''

#类的组合，我还是不怎么理解
'''这个的解释就是创建三个类，每个类都有不同属性，
可是这些类也有一点关联，如下面例子就是，池塘，乌龟，鱼，
鱼和乌龟很多属性相同，池塘和鱼，乌龟属性不同，可是鱼和乌龟都在池塘里，
这样关系创建的类就是下面样子'''
#类是不需要参数的，而函数是需要参数的，这就是类比函数强大的地方
class Turtle:
	def __init__(self,x):
		self.num = x
class Fish:
	def __init__(self,y):
		self.num = y
class Pool:
	def __init__(self,x,y):
		self.turtle = Turtle(x)
		self.fish =Fish(y)
	def print_num(self):
		#下面的语句为什么一定要加上num,不加报错？
		#这是因为上面的赋值语句么？我要打印的是一个整型变量，Turtle(x)这是给类传参，不是变量
		print('水池里有%d只乌龟，有%d条鱼。'%(self.turtle.num,self.fish.num))
pool = Pool(1,10)
pool.print_num()


'''类，类对象，实例对象，这是三个不同概念，
新创建是一个类，类创建完成后就变成一个类对象，
python一切皆对象，实例对象就是对类对象的使用'''
#类的绑定
class AA:
	def setxy(self,x,y):
		self.x = x
		self.y = y
	def printxy(self):
		print(self.x,self.y)
aa = AA()
print(aa.__dict__)
print(AA.__dict__)
#对于实例对象aa，有没有参数传入是不同的，可是对AA没有影响
aa.setxy(4,5)
print(aa.__dict__)
print(AA.__dict__)


'''没有self会参数错误，传入两个参数，错误提示为
需要三个参数，传入三个参数则需要四个参数，因为在这个
类里有一个隐藏参数self，在AA类的setxy方法里加上self，
可是下面不写成self.x = x，self.y = y，即使传入参数
aa里面的参数也没有改变,没有这个self，x,y值无法改变
因为有了self变成aa.x,aa.y,这当然可以改变，也就是把这个变量
也带到实例对象里，没有self，x,y就只是对象AA方法下面的一个变量'''
class AA:
	def setxy(self,x,y):
		x = x
		y = y
	def printxy(self):
		print(x,y)
aa = AA()
print(aa.__dict__)
print(AA.__dict__)
aa.setxy(4,5)
print(aa.__dict__)
print(AA.__dict__)