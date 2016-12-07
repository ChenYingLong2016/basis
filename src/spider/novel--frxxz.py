# coding = utf-8
'''
Created on 2016年11月17日
@author: 陈应龙
'''

#整本小说爬取还差很多

import urllib.request
import re,os

'''
http://www.23wx.com/小说网站没法抓取，
使用的是<td class="L"><a href="16460818.html">第一章 山边小村</a></td>
这样方式来分别保存各个章节标题，<td class="L">这样用正则无法查找，
这样的标签可以用Scrapy框架来爬。

http://www.quanshu.net/这样的网站用下面普通方法就可以爬，
<li><a href="78850.html" title="第一章 山边小村，共2741字">第一章 山边小村</a></li>
使用来分割的是<li>标签，这样就可以用正则表达式来爬了。
'''
url = 'http://www.quanshu.net/book/0/269/'
def get_urllist():
	html = urllib.request.urlopen(url).read()
	html = html.decode('gbk','ignore')
	#print(html)
	a = re.compile(r'<li><a href="(.*?)" title="(.*?)">(.*?)</a></li>')
	urllist = re.findall(a,html)
	return urllist
#print(get_urllist())

def get_Content():
	
	while True:
		os.mkdir('凡人修仙传')
		os.chdir('凡人修仙传')
		for i in get_urllist():
			n = []
			urls = i[0]
			#print(type(urls))
			n.append(urls)
			#print('第一个',n)
			title = i[2]
			title = title.replace('?','')
			#print('第二个',n)
			html = urllib.request.urlopen(url + urls).read()
			html = html.decode('gbk','ignore')
		    #括号为特殊字符，必须要用转义符号\,否则查找到的是一个空列表
			t = re.compile(r'style5\(\);</script>(.*?)<script type="text/javascript"')
			content = re.findall(t,html)[0]
			content = content.replace('&nbsp;','')
			content = content.replace('<br />','')
#			os.mkdir('凡人修仙传')这样每次都会创建一个目录，最后是一个循环嵌套的目录结构，
#			os.chdir('凡人修仙传')
			with open(title+'.txt','w') as f: #保证出现问题也能把打开文件关闭，使用的是with函数
				f.write(content)
			if urls == '9388271.html':
				break
get_Content()

