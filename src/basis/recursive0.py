# coding = utf-8
'''
Created on 2016年10月31日
@author: 陈应龙
'''

#递归在python中默认是不超过100层
#递归耗费资源，运行速度慢，可是在汉诺塔，谢尔宾斯基三角形，树结构方面有自己优势
#递归实现阶乘函数,递归容易出现死循环，递归是函数调用自己
def recurs(n):
	if n == 1:
		return 1
	else:
		return n*recurs(n-1)
number = int(input('请输入一个整数（递归实现）：'))
result = recurs(number)
print('%d 的阶乘是:%d'%(number,result))

#求阶乘函数
def f(x):
	n = x
	for i in range(1,x):
		n *= i
	return n
y = int(input('请输入一个整数（普通循环实现）：'))
result = f(y)
print('%d 的阶乘是:%d'%(y,result))
	
