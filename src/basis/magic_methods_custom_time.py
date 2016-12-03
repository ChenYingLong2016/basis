# coding = utf-8
'''
Created on 2016年11月18日
@author: 陈应龙
'''

#简单定制
'''
基本要求：
--定制一个计时器类
--start和stop方法代表开始计时和停止计时
--假设计时器对象t1，print(t1)和直接调用t1都显示结果
--当计时器未启动或已经停止计时，调用stop会提示
--两个计时器对象可以进行相加：t1 + t2
--只能使用提供的有限资源
这程序只能在python shell里面运行，毕竟需要输入多个变量
'''

import time

class Mytime():
	def __init__(self):
		self.unit = ['年','月','天','小时','分钟','秒']
		self.prompt = '未开始计时！'
		self.lasted = []
		self.begin = 0
		self.end = 0


	def __str__(self):
		return self.prompt
	__repr__ = __str__

	def __add__(self,other):
		prompt = '总共运行了'
		result = []
		for index in range(6):
			result.append(self.lasted[index] + other.lasted[index])
			if result[index]:
				prompt += (str(result[index]) + self.unit[index])
		return prompt

	#开始计时
	def start(self):
		self.begin = time.localtime()
		self.prompt = '提示：请先调用stop停止计时'
		print('计时开始....')
	
	#停止计时
	def stop(self):
		if not self.begin:
			print('提示：请先调用start()进行计时')
		else:
			self.end = time.localtime()
			self._calc()
			print('计时结束！')

	#内部方法，计算运行时间
	def _calc(self):
		self.lasted = []
		self.prompt = '总共运行了'
		for index in range(6):
			self.lasted.append(self.end[index] - self.begin[index])
			if self.lasted[index]:
				self.prompt += (str(self.lasted[index]) + self.unit[index])
		#为下一轮计时初始化变量
		self.begin = 0
		self.end = 0
'''还有两个功能需要加入：
---假设开始时间是（2022年3月6日9时15分36秒），结束时间
   是（2025年4月5日8时17分30秒），得到结果为
  （3年1月-1日-1时2分-6秒），这当然需要转换为正常时间
----现在计算机速度都是非常快，而这最小时间计算为秒，
    在精度上来说根本就不够用。 
'''
