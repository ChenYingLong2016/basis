# coding = utf-8
'''
Created on 2016年11月20日
@author: 陈应龙
'''

'''这是原本的描述符方法，
__get__(self,instance,owner)
访问属性，返回属性值
__set__(self,instance,value)
属性分配中调用，不返回任何内容
__delete__(self,instance)
控制删除操作，不返回任何内容
'''
class Originaldescriptor:
	def __get__(self,instance,owner):
		print('getting....',self,instance,owner)
	def __set__(self,instance,value):
		print('setting....',self,instance,value)
	def __delete__(self,instance):
		print('deleting....',self,instance)

class Test:
	x = Originaldescriptor()
test = Test()
test.x #这不需要print就显示结果，调用的是__get__函数
print(test) #这必须需要print，这是一个类实例对象
test.x = 'X-man' #调用__set__函数，后面还有属性说明
del test.x   #调用__delete__函数，后面还有属性说明



'''下面是自己设置之后描述符
'''
class Mydescriptor:
	def __init__(self,fget=None,fset=None,fdel=None):
		self.fget = fget
		self.fset = fset
		self.fdel = fdel
	def __get__(self,instance,owner):
		return self.fget(instance)
	def __set__(self,instance,value):
		self.fset(instance,value)
	def __delete__(self,instance):
		self.fdel(instance)
class C:
	def __init__(self):
		self._x = None #前面加下横线代表内部变量，不允许外部调用
	def getx(self):
		return self._x
	def setx(self,value):
		self._x = value
	def delx(self):
		del self._x
	x = Mydescriptor(getx,setx,delx)
c = C()
c.x = 'X-M'
print(c.x)  #只返回X-M
print(c._x) #只返回X-M
del c.x
#print(c.x)  AttributeError: 'C' object has no attribute '_x'


'''
---定义一个温度类，然后定义两个描述符类描述摄氏度和
    华氏度两个属性
---要求两个属性会自动进行转换，也就是说给摄氏度这个属性
   赋值，然后打印的华氏度是自动转换后结果
'''
class Celsius:
	def __init__(self,value = 26.0):
		self.value = float(value)
	def  __get__(self,instance,owenr):
		return self.value
	def __set__(self,instance,value):
		self.value = float(value)

class Fahrenheit:
	def __get__(self,instance,owner):
		return instance.cel*1.8 + 32
	def __set__(self,instance,value):
		instance.cel = (float(value)-32)/1.8

class Temperature:
	cel = Celsius()
	fah = Fahrenheit()

temp =Temperature()
print(temp.cel)
temp.cel = 30
print(temp.cel)
print(temp.fah)
temp.fah = 100
print(temp.cel)
print(temp.fah)
