# coding = utf-8
'''
Created on 2016年11月1日
@author: 陈应龙
'''

#汉诺塔经典的递归游戏，或者经典的递归算法，递归定义
#这个是理解困难的地方就是内部参数传递的变化
#形参的变化我还是难以理解。难理解部分就是x,y,z变化关系
#这个理解应该是由小到大，需要停下来慢慢理解
#偶数第一步由X到Z，奇数第一步由X到Y
def hanoi(n,x,y,z):
	if n == 1:
		print(x,'-->',z)
	else:
		hanoi(n-1,x,z,y) #将n-1移动到y上
		print(x,'-->',z) #将最大一片由X移动到上，应该替换为hanoi(1,x,y,z)
		hanoi(n-1,y,x,z) #将n-1移动到z上
n  = int(input('请输入汉诺塔层数：'))
print(hanoi(n,'X','Y','Z'))
#这运行会返回一个None，这是为什么？下面的代码就没有None返回
#这个函数没有设定返回值

'''
#网上的python代码，这是最简洁的代码,其它编程语言代码都比这要多。
#使用下面输入方法步数变少，显示不完整
def hanoi0(m,a,b,c):
    if n==1:
        print(a,'-->',c)
    else:
        hanoi(m-1,a,c,b)#将前n-1个盘子从a移动到b上
        hanoi(1,a,b,c)#将最底下的最后一个盘子从a移动到c上
        hanoi(m-1,b,a,c)#将b上的n-1个盘子移动到c上
m=int(input('请输入汉诺塔的层数：'))
hanoi0(m,'A','B','C')
'''