# coding = utf-8
'''
Created on 2016年10月29日
@author: 陈应龙
'''

#这就是把列表遍历一遍，并且使用系统自带函数len打印出每个元素长度
member = ['崆峒派','大家这是为什么','不要乱摸','心平气和容易过日子']
for i in member:
	print(i,len(i))

#使用函数range(),这结果是0，1，2，3，4，五个数，由0开始
for a in range(5):
	print(a)

#2，3，4，5，即包含开始，结尾减1
for b in range(2,6):
	print(b)

#1,3,5,7,由1到9，每隔两个数取一个
for c in range(1,9,2):
	print(c)
