# coding = utf-8
'''
Created on 2016年10月29日
@author: 陈应龙
'''

import urllib.request
import urllib.parse
import json
import time

'''
while True:
    content = input('��������Ҫ���������(���롰q!���˳�����)��') 
    if content == 'q!':
        break
    
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=dict2.index'
    date  = {}
    date['type'] = 'AUTO'
    date['i'] = content
    date['doctype'] = 'json'
    date['xmlVersion'] = '1.8'
    date['keyfrom'] = 'fanyi.web'
    date['ue'] = 'UTF-8'
    date['action'] = 'FY_BY_CLICKBUTTON'
    date['typoResult'] = 'true'
    date = urllib.parse.urlencode(date).encode('utf-8')
    
    response = urllib.request.urlopen(url, date)
    html = response.read().decode('utf-8')
    
    target = json.loads(html)
    #['translateResult'][0][0]['tgt']
    print("��������%s"%(target['translateResult'][0][0]['tgt']))
    time.sleep(5)
'''
# _*_ coding:utf-8 _*_
while True:
    content = input("请输入翻译内容(按‘q’退出程序)：") 
    if content == 'q':
        break
       
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=dict2.index'
    date  = {}
    date['type'] = 'AUTO'
    date['i'] = content
    date['doctype'] = 'json'
    date['xmlVersion'] = '1.8'
    date['keyfrom'] = 'fanyi.web'
    date['ue'] = 'UTF-8'
    date['action'] = 'FY_BY_CLICKBUTTON'
    date['typoResult'] = 'true'
    date = urllib.parse.urlencode(date).encode('utf-8')
        
    response = urllib.request.urlopen(url, date)
    html = response.read().decode('utf-8')
        
    target = json.loads(html)
    #['translateResult'][0][0]['tgt']
    print("翻译结果:%s"%(target['translateResult'][0][0]['tgt']))
    time.sleep(5)