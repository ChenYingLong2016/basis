# coding = utf-8
'''
Created on 2016年10月31日
@author: 陈应龙
'''

#实现在35以上时，递归实现速度比迭代快很多

#迭代实现
def fib(n):
	n1 = 1
	n2 = 1
	n3 = 1

	if n<1:
		print('输入错误：')
		return -1
#循环里面的n1=n2,n2=n3这样写结果是262144错误，
#按照下面顺序写结果是6765
	while (n-2)>0:
		n3 = n2 + n1#n3=2,n3=3,n3=5
		n1 = n2 #n1=n2=1,n1=n2=2,n1=n2=3
		n2 = n3 #n2=n3=2,n2=n3=3,n1=n2=5
		n -= 1
	return n3
print(fib(20))#这结果是给程序员自己看的，要让别人看到需要return

#递归实现指定具体第几个斐波纳契数列的值
def recurs(n):
	if n - 2 <= 0:
		return 1
	else:
		return recurs(n-2)+recurs(n-1)
number = int(input('请输入一个整数（递归实现）：'))
result = recurs(number)
print('第 %d 个斐波那契数列的值是:%d'%(number,result))