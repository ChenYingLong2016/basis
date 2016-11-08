# coding = utf-8
'''
Created on 2016年11月5日
@author: 陈应龙
'''

f = open('C:\\Users\\Administrator.WQ-20160501NYYU\\Desktop\\py\\2.txt')
boy = []
girl = []
for each_line in f:	
	role,line_said = each_line.split(':',1)	
	if role == '男说':
		boy.append(line_said)
		boy_file = open('C:\\Users\\Administrator.WQ-20160501NYYU\\Desktop\\py\\boy.txt','w')#当遇到打开不存在文件，该文件就会被自动创建
		boy_file.writelines(boy)
		boy_file.close()
	if role == '女说':
		girl.append(line_said)
		girl_file = open('C:\\Users\\Administrator.WQ-20160501NYYU\\Desktop\\py\\girl.txt','w')
		girl_file.writelines(girl)
		girl_file.close()
f.close()	

#带有======分隔符的我暂时解决不了，因为python3.5.2返回的是错误，在学习视频中python3.3.3中返回是正确值，都是同样代码。
''' 
def  save_file(boy,girl,count):
	file_name_boy = 'boy_' + str(count)+'.txt'
	file_name_girl = 'girl_' + str(count)+'.txt'

	boy_file = open(file_name_boy,'w')
	girl_file = open(file_name_girl,'w')

	boy_file.writelines(boy)
	girl_file.writelines(girl)

	boy_file.close()
	girl_file.close()

def split_file(file_name):
	f = open(file_name)
	boy = []
	girl = []
	count = 1
	for each_line in f:
		if each_line[:6] != '======':  #我自己做的文本文件里面开始========是并列两行，应该算四行，所以出现四个文件，其中两个是空文件，list[0]加空文件出现错误
	#		role = each_line.split(':',1)[0] #只打印这个不会报错，可是会把最后一部分也打印出来
			#下面这一行错误想到一个可能，就是来到======行时，没有冒号：，分割时不可能有下标1的部分，这行不能用冒号：来分割。
			#可是这也没法解释为什么第二个=====下面的文字没有被分割
	#		line_said = each_line.split(':',1)[1] #这一行总是报错，list index out of range，列表超出范围，不能把第二个=====后面文字显示出来，这里返回值是空，所以列表报错
			role,line_said = each_line.split(':',1) #这里的冒号:一定要用英文，用中文无法分割
	#		print(role,len(role))
			print(line_said)		
			if role == '男说':
				boy.append(line_said)
			if role == '女说':
				girl.append(line_said)
		else:
			save_file(boy,girl,count)

			boy = []
			girl = []
			count += 1
	save_file(boy,girl,count)

	f.close()
split_file('C:\\Users\\Administrator.WQ-20160501NYYU\\Desktop\\py\\1.txt')
'''