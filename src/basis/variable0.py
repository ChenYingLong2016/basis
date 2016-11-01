# coding = utf-8
'''
Created on 2016年10月30日
@author: 陈应龙
'''

def discounts(price,rate):
	final_price = price*rate
	#在局部变量中可以调用全局变量
	#print('试图打印局部变量old_price的值:',old_price)
	#这里是在这个函数体里新建了一个old_price的新变量，存储位置和外面的那个old_price不同，相同名字但是不同变量，函数体全部存储在一个堆栈里，外面的变量作用域比里面要大。
	old_price = 50
	print('修改后old_price的值是1：',old_price)
	return final_price

old_price = float(input('请输入原价：'))
rate = float(input('请输入折扣率：'))
new_price = discounts(old_price,rate)
print('修改后old_price的值是2：',old_price)
print('打折后价格是：',new_price)
#执行下面这句话会报错，final_price这变量只在函数调用范围
#print('试图打印局部变量final_price的值',final_price)