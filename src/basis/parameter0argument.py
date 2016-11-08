# coding = utf-8
'''
Created on 2016年10月29日
@author: 陈应龙
'''

#形参使用方法，即需要的参数是在使用时输入
def saysome(name,word):
	print(name+'->'+word)
#默认的参数传递是按顺序传递
saysome('智者','主要的是洞见')
saysome('主要的是洞见','智者')
'为了保持输入结果不发生偏差，最好办法就是直接赋值给需要传递参数'
saysome(word = '主要的是洞见',name = '智者')

#可变参数，即不知道需要多少个参数，可以在需要时在加参数，在参数前加*号表示可变参数
def test(*params):
	print('参数长度：',len(params))
	print('这是参数里面第二个参数',params[1]) #下标表示第几个参数，没有下标则默认打印全部参数
	print('打印所有参数',*params) #如果需要打印所有传入参数，这里必须也使用可变参数
#下面的函数调用，如果没有输入中文会报错，而且输入中文也只显示第一个，即可变参数我还没有理解
#刚才理解才是错误，这个函数里面至少需要两个因素，否则没法打印第二个参数，打印的不是全体插入参数，只是第二个，以为的不可以不同变量认识是错误的
test('这个可以看得到不?',3,'m',6,8,'等好久') #这里其实有个问题，就是之能显示中文，英文和数字都没有显示


