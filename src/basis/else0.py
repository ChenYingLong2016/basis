# coding = utf-8
'''
Created on 2016年11月9日
@author: 陈应龙
'''

#while和else搭配，while语句里面为真则执行while里面，条件为假执行else
#这个实现就是干完了怎样，干不完就别想怎么样
def showMaxFactor(num):
	count = num // 2
	while count > 1:
		if num % count == 0:
			print('%d最大的约数是%d'%(num,count))
			break
		count -= 1
	else:
		print('%d是素数！'%num)

num = int(input('请输入一个数:'))
showMaxFactor(num)

#没有问题，那就干吧！
try:
	int('6352155')
except ValueError as reason:
	print('错误：'+str(reason))
else:
	print('一切正常!')

'''
#with抽象出文件中常用操作，打包在一起执行
#下面代码执行时，因为打开的是一个不存文件，故会报错，无法关闭
try:
	f = open('date.txt','w')
	for each_line in f:
		print(each_line)
except OSError as reason:
	print('错误：'+str(reason))
finally:
	f.close()
'''
    
#上面代码只需如此改动，就可以省去忘记关闭文件问题
try:
	with open('date.txt','w') as f:
            for each_line in f: #为什么这里会需要多一个空格缩进？这里是一个问题存在
                print(each_line)
except OSError as reason:
	print('错误：'+str(reason))





	