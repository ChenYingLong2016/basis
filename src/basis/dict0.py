# coding = utf-8
'''
Created on 2016年11月1日
@author: 陈应龙
'''

#映射关系，dict={key:value}，下面是三种创建字典的方法，字典是大括号，列表中括号
dict0 = {1:'one','二':'two','三':'three'}
dict1 = dict(((1,'one'),('二','two'),('三','three')))
dict2 = dict(一='one',二='two',三='three')
print(dict0,dict1,dict2)
print(dict0['二'])
print(dict1['二'])
print(dict2['二'])

#改变字典里面的某个值
dict2['二'] = '不要再二'
print(dict2)

#字典里没有的值，则会把这组映射添加到字典里
dict0['si'] = '四'
print(dict0)