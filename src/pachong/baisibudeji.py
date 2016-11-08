# coding = utf-8
'''
Created on 2016年11月6日
@author: 陈应龙
'''

import re,urllib

def get_url(page):
	pass

def get_html(url):
	return urllib.urlopen(url).read()

def download(mp4_url,path):
	print(path)
	path = "".join(path.split())
	urllib.urlretrieve(mp4_url,'%s')