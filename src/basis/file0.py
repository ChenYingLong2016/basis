# coding = utf-8
'''
Created on 2016年11月3日
@author: 陈应龙
'''

f = open('C:\\Users\\Administrator.WQ-20160501NYYU\\Desktop\\py\\1.txt')
print(f.read())
f.close #当读取完成时，文件指向是最后，此时只有把把文件关闭从新打开才能从头读取
f = open('C:\\Users\\Administrator.WQ-20160501NYYU\\Desktop\\py\\1.txt')
#print(f.read(6)) #读取前面的6个字节，一个汉字；两个字节

print(f.read(7)) #读取文件的前面7个字节
print(f.tell()) #读取文字字节数，
f.seek(2,0) #一个中文是两个字节，如果遇到把一个中文分成两半，则会报错，如这里1就会报编码错误
print(f.readline()) #读取整行文字
print(list(f)) #把文件里面内容转换为列表
f.seek(0,0) #必须回到开始，否则下面的迭代没有内容显示
#下面是系统推荐的迭代方式，可以快速把文件里面的内容按行打印出来
for each_line in f:
	print(each_line)
f.close

#这是必须新建一个文件才能写入，往上面文件写入报错
#上面不能写入，是少了‘W’，就是以写入方式打开，可是用这种方式打开会把原来文件内容清除，所以需要新建一个文件
f = open('C:\\Users\\Administrator.WQ-20160501NYYU\\Desktop\\py\\text.txt','w')
f.write('到底可不可以写入')
f.write('在写入一行新字符')
f.close
