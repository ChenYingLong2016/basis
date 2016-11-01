# coding = utf-8
'''
Created on 2016年10月29日
@author: 陈应龙
'''
#不带参数函数
def myfirstfunction():
	'就是打印两行字而已'
	print('haojiubujian') #就是打印两行字
	print(123456789)
myfirstfunction()

#带参数函数，而且函数本身-不打印结果，只是返回一个值。
def newfunction(num1,num2):
	return (num1 + num2)	
print(newfunction(3,5))

help(myfirstfunction)#打印引号里面的注释

