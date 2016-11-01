# coding = utf-8
'''
Created on 2016年10月31日
@author: 陈应龙
'''

#函数表达式lambda，这是用来简写函数的表达式
g = lambda x,y: x+y
print(g(3,4))

#上面的表达式与下面这个函数作用相同
#python在写脚本时使用上面的表达式可以精简代码
def f(x,y):
	return x + y
print(f(3,4))

