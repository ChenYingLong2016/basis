# coding = utf-8
'''
Created on 2016年10月29日
@author: 陈应龙
'''

# 这个循环就把前面两个循环的问题解决了，简洁清楚，又节省CPU。elif为else if缩写。
score = int(input('请输入一个分数：'))
if 100 >= score >= 90:
    print('A')
elif 90 > score >= 80:
    print('B')
elif 80 > score >= 60:
    print('C')
elif 60 > score >= 0:
    print('D')
else:
    print('输入错误')