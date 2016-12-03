# coding = utf-8
'''
Created on 2016年11月25日
@author: 陈应龙
'''

'''yield代表生成器，函数暂停执行，下一次调用从
上一次中断地方开始执行，这与return不同是每次只执行
到yield结束，而return这是整个程序全部执行完'''
def myGen():
	print("生成器被执行！")
	yield 1
	yield 2
myG = myGen()
print(next(myG)) #这一句输出结果为:生成器被执行！，就是到第一个yield
print(next(myG)) #这一句输出结果为：2
#下面是for语句实现，也就是for自动调用next()方法
for i in myGen():
	print(i)


def fibs():
	a = 0
	b = 1
	while True:
		a,b = b,a + b
		yield a
for each in fibs():
	if each > 500:
		break
	print(each,end=' ')

'100以内可以被2整除，可是不能被3整除的数'
#这是一个列表推导式
a = [i for i in range(100) if not(i%2) and i%3]
print(a)
#字典推导式
b = {i : i % 2 == 0 for i in range(10)}
print(b)
#集合推导式
c = {i for i in [1,1,2,3,3,4,5,6,7,8,6,5,3,2,1]}
print(c)
#元祖推导式
d = (i for i in range(10))
print(next(d))
for each in d:
	print(each)


sum(i for i in range(100) if i % 2)
print(sum) #运行结果为<built-in function sum>
#这并不是希望的结果
fou each in 1:
	print(each)
