# coding = utf-8
'''
Created on 2016年10月29日
@author: 陈应龙
'''

# 这个找到分数就停止执行，可是问题就是容易造成悬挂else.
score = int(input('请输入一个分数：'))
if 100 >= score >= 90:
    print('A')
else:
    if 90 > score >= 80:
        print('B')
    else:
        if 80 > score >= 60:
            print('C')
        else:
            if 60 > score >= 0:
                print('D')
            else:
                if score < 0 or score >100:
                    print('输入错误')