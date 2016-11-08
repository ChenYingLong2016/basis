# coding = utf-8
'''
Created on 2016年11月6日
@author: 陈应龙
'''

#这只是输出一个大概错误，具体原因就不清楚
try:
	f = open('hello.text')
	print(f.read())
	f.close()
except OSError:
	print('文件出错啦T_T')

#这个输出把具体原因也说出来了
try:
	f = open('hello.text')
	print(f.read())
	f.close()
#把错误的原因作为一个变量reason，
except OSError as reason:
	#将变量reason作为字符串输出
	print('文件错误T_T\n错误原因：' + str(reason))

#捕获一类型错误的返回
try:
	sum = 1+'1'
except TypeError as reason:
	#将变量reason作为字符串输出
	print('类型错误T_T\n错误原因：' + str(reason))

#包含多个异常，不输出具体异常原因是什么
try:
	f = open('hello.text')
	print(f.read())
	f.close()
except (OSError,TypeError):
	print('出错啦T_T')

#finally用法，无论如何，finally里面的语句都会被执行
try:
	f = open('hello.text','w') #文件不存在，会新建这个文件
	print(f.write('写入一行文字。')) #向文件写入文字
	sum = 1+'1'  #发生错误
#	f.close()  #这不会被执行，可是文件是打开的，没有被关闭，所有写入文件都是在内存里，不会被保存，太多就会造成内存溢出
except (OSError,TypeError):
	print('出错啦T_T')
finally:
	f.close() #即使上面发生错误，保证打开的文件被执行关闭

#直接发生异常关键字raise，也可以在后面加上想显示的异常
raise ZeroDivisionError('除数为零异常')
