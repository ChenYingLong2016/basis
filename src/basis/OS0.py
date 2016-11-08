# coding = utf-8
'''
Created on 2016年11月5日
@author: 陈应龙
'''

#OS模块python实现跨平台的模块
import os
import random
secret = random.randint(1,10)
print(secret)

print(os.getcwd()) #返回当前工作目录
#把目录下的文件打印出来
print(os.listdir('C:\\Users\\Administrator.WQ-20160501NYYU\\Desktop\\py\\basis\src\\basis'))


