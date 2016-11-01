# coding = utf-8
'''
Created on 2016年10月29日
@author: 陈应龙
'''

#break循环条件为真时跳出循环。没有break则下面这个循环无法跳出
#流氓软件的安装就是这种方式实现，关闭时跳出界面强逼安装为循环跳出条件。
bingo = '浓眉大眼好青年'
answer = '请输入我给自己贴的标签：'
while True:
	if answer == bingo:
		break
	answer = input('Sorry，错了，重新输入（只有输入正确才能推出）：')

print('恭喜输入正确！')
print('了解我的人你终于来了！')

#continue跳出本次循环，开始下一次循环，输出为2，1，4，3，6，5，8，7，10，9，这个例子第一个0不满足条件，所以0不打印，1满足条件故打印
#下面这个循环偶数都为i += 2打印，奇数都为continue上面的print()打印。
for i in range(10):
	if i%2 != 0:
		print(i)
		continue
	i += 2
	print(i)