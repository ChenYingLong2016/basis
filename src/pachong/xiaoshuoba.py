# coding = utf-8
'''
Created on 2016年10月29日
@author: 陈应龙
'''

import urllib
import re

class BDBT:
	def __init__(self,baseURL,seeLZ):
		self.baseURL = baseUrl #类的参数不能使用
		self,seeLZ = '?see_lz' + str(seeLz)
	
	#获取该页贴子的代码
	def getpage(self,pageNum):
		try:
			url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
			request = urllib.request(url)
			reponse = request.urlopen(request)
			return reponse.read()

		except Exception,e:

	#匹配标题
	def Title(self,pageNum):
		html = self.getpage(pageNum) #调用获取源代码
		reg = re.compile(r'<title>【原创】(.*?)。') #compile提高效率方法
		items = re.findall(reg,html)
		for item in items:
			f = open('text1.txt','w')
			f.write('标题'+'\t'+item)
			f.close()
		return items

	#匹配正文
	def Title(self,pageNum):
		html = self.getpage(pageNum) #调用获取源代码
		reg = re.compile(r'class="d_post_content j_d_post_content "(.*?)</div><br>') #compile提高效率方法
		req = re.findall(reg,html)
		for i in req:
			
			
		return items 

