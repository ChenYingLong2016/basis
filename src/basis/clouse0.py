# coding = utf-8
'''
Created on 2016年10月30日
@author: 陈应龙
'''

#可以使用关键字nonlocal,还有一个关键字是globe，这都是把局部变量作为全局变量的关键字
#闭包概念，即在函数的内嵌函数里，用了和上一个作用域同样的变量名，python会屏蔽内嵌函数的同一个变量
def fun0():
	x = 3
	def fun1():
		nonlocal x
		x *= x
		return x
	return fun1() #在函数fun0外面是无法调用函数fun1
#type()是把没有把握的东西类型打印出来,一个必要的就必须在python的Shell下面，在其它开发环境就需要print
#函数调用时，type(fun0)是函数<class 'function'>，而type(fun0())是整型<class 'int'>
#在Shell下面，输入fun0()就显示结果9，可是在外面这些编译器里执行，要显示9必须用print()
#Shell与编译器显示不一样，我经常以为是自己编程问题，忘记是由于编译器问题原因。
print(fun0())

def funx(x):
	print('打印X：',x)
	def funy(y):
		print('打印Y：',y)
		return x*y
	return funy
#下面的print语句无法调用funy函数，可是可以使用如下方式给funy中的变量赋值。
#加上两个print语句，很清楚的就看到以下赋值方式给的是什么变量。
print(funx(3)(7))
