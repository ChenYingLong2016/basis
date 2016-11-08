# coding = utf-8
'''
Created on 2016年11月6日
@author: 陈应龙
'''

import pickle
my_list = [9527,3.1415,'abc','家在哪？',['another list']]
pickle_file = open('my_list.pkl','wb') #以二进制方式写入打开文件，没有则新建一个文件
pickle.dump(my_list,pickle_file) #把列表装入文件
pickle_file.close() #关闭文件
pickle_file = open('my_list.pkl','rb') #以二进制只读方式打开文件
my_list1 = pickle.load(pickle_file) #以load方式加载文件
print(my_list1)