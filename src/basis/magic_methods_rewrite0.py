# coding = utf-8
'''
Created on 2016年11月18日
@author: 陈应龙
'''


'''
重写python自带函数，如下面把相加，相减函数互相调换
'''
class New_int(int):
	def __add__(self,other):
		return int.__sub__(self,other)
	def __sub__(self,other):
		return int.__add__(self,other)
a = New_int(9)
b = New_int(6)
print(a + b) #显示结果为3
print(a - b) #显示结果为15

'''
魔法方法的从写一定要小心，否则就容易出现错误,
下面的代码就是出现RecursionError: maximum recursion
 depth exceeded while calling a Python object错误，
 递归错误，a本身传递给self已经自带加法，下面返回值
 还要相加就是递归，最后就是到最大递归数错误返回，
 下面程序可以更改后来用

class Try_int(int):
	def __add__(self,other):
		return self + other
	def __sub__(self,other):
		return self + other
a = Try_int(9)
b = Try_int(6)
print(a + b) 
'''
'''为什么在前面加上一个int就可以用了？
这是消除系统自带方法，这是两个不同类型,
<class '__main__.Try_int'> <class 'int'>,
这就是他们的类型，一个是类，一个是整型变量'''
class Try_int(int):
	def __add__(self,other):
		print(type(self),type(int(self)))
		return int(self) + int(other)
	def __sub__(self,other):
		return int(self) + int(other)
c = Try_int(9)
d = Try_int(6)
print(c + d) 

'''e后面跟着加号，代表它有自己方法,不会触发类里面的函数方法，
def __radd__(self,other)不被调用，可是1和后面的加号程序不认为
是1自带的方法，所以就调用f方法，而调用f就是执行类里的函数体，
这个函数体用的是减法，所以执行下来就是减法
'''
class Nint(int):
	def __radd__(self,other):
		return int.__sub__(self,other)
e = Nint(8)
f = Nint(6)
print(e + f) #返回值为14，执行加法
print(1 + f) #返回值为5，执行的是减法


'''下面两个类只有self,other位置不同，可是得到结果
是不同的数，也就是说在不同位置代表不同参数,
对于依赖位置的运算必须确定顺序，减法，除法等需要注意
参数位置决定结果。__sub__减法给的是第二个参数'''
class Dint(int):
	def __rsub__(self,other):
		return int.__sub__(self,other)
g = Dint(6) #g的赋值给的是other，other带减法
print(5 - g) #结果为1

class Dint0(int):
	def __rsub__(self,other):
		return int.__sub__(other,self)
h = Dint0(6) #h赋值也是给other，可是other没有给定计算方法，默认没有
print(5 - h) #结果为-1
