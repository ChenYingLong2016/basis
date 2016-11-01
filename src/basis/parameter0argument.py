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
test('a','等好久',3,5,9,6)


