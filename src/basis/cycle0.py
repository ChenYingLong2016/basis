# coding = utf-8
'''
Created on 2016年10月29日
@auth.or: 陈应龙
'''

# 这个程序会从头到尾执行一遍，即哪怕是A内分数，下面的代码也会执行，无谓浪费CPU资源。
score = int(input('请输入一个分数：'))
if 100 >= score >= 90:
	print('A')
if 90 > score >= 80:
	print('B')
if 80 > score >= 60:
	print('C')
if 60 > score >= 0:
	print('D')
if score < 0 or score >100:
	print('输入错误')

