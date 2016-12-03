# coding = utf-8
'''
Created on 2016年11月24日
@author: 陈应龙
'''

class Fibs:
	def __init__(self,n=10):
		self.a = 0 
		self.b = 1
		self.n = n
	def __iter__(self):
		return self
	def __next__(self):
		self.a,self.b = self.b,self.a + self.b
		if self.a > self.n:
			raise StopIteration
		return self.a
'''fibs0 = Fibs()
for each in fibs0:
	print(each)'''
fibs = Fibs(5)
for each in fibs:
	print(each)


'''for循环的while实现'''
string = 'Hello word!'
it = iter(string)
while True:
	try:
		each = next(it)
	except StopIteration:
		break
	print(each)
'''for循环两句语句实现，上面的while循环就需要好多,
for循环会自动调用迭代器'''
for each in string:
	print(each)


