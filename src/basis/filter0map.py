# coding = utf-8
'''
Created on 2016年10月31日
@author: 陈应龙
'''
#map与filter使用区别，这是两个不同数据处理方式
#过滤器filter，把需要的信息过滤只留下需要部分
#打印的是一个对象,打印结果为<filter object at 0x00000000010F7550>
print(filter(None,[1,3,0,False,True]))
#打印的是一个列表，打印结果是[1, 3, True]，即把假和0过滤掉
print(list(filter(None,[1,3,0,False,True])))

#返回奇数函数，打印结果是[1, 3, 5, 7, 9]
def odd(x):
	return x%2
temp = range(10)
show = filter(odd,temp)#函数调用不能加（）
print(list(show))
#一句话实现上面的整个过程，代码缩短，看起来很简洁
#返回X%2的值，X取值0到9，把X%2==0的过滤掉，把剩余的作为一个列表打印出来，最后就是指定范围奇数
print(list(filter(lambda x: x%2 , range(10))))

#把函数里面的每个值都加工，加工完返回一个新列表
print(list(map(lambda x: x%2 , range(10))))
