# coding = utf-8
'''
Created on 2016年11月17日
@author: 陈应龙
'''

#整本小说爬取还差很多

import urllib.request
import re

'''
http://www.23wx.com/小说网站没法抓取，
使用的是<td class="L"><a href="16460818.html">第一章 山边小村</a></td>
这样方式来分别保存各个章节标题，<td class="L">这样用正则无法查找，
这样的标签可以用Scrapy框架来爬。

http://www.quanshu.net/这样的网站用下面普通方法就可以爬，
<li><a href="78850.html" title="第一章 山边小村，共2741字">第一章 山边小村</a></li>
使用来分割的是<li>标签，这样就可以用正则表达式来爬了。
'''
'''这可以由第一章开始抓取小说'''
url = 'http://www.quanshu.net/book/0/269/'
def get_urllist():
    html = urllib.request.urlopen(url).read()
    html = html.decode('gbk')
    #print(html)
    a = re.compile(r'<li><a href="(.*?)" title="(.*?)">(.*?)</a></li>')
    urllist = re.findall(a,html)
    return urllist
#print(get_urllist())    

def get_Content():
    i = len(get_urllist())
    while True:
        for i in get_urllist():
            urls = i[0]
            print(type(urls))
            title = i[2]
            title = title.replace('?','')
            html = urllib.request.urlopen(url + urls).read()
            html = html.decode('gbk')
            #括号为特殊字符，必须要用转义符号\,否则查找到的是一个空列表
            t = re.compile(r'style5\(\);</script>(.*?)<script type="text/javascript"')
            content = re.findall(t,html)[0]
            content = content.replace('&nbsp;','')
            content = content.replace('<br />','')
            os.chdir('C:\\Users\\Administrator.WQ-20160501NYYU\\Desktop\\frxxz')
            with open(title+'.txt','w') as f: #保证出现问题也能把打开文件关闭，使用的是with函数
                f.write(content)
    




'''
def get_Content():
    i += 0 
    print()
    html = urllib.request.urlopen(url +get_urllist()[i][0] ).read()
    html = html.decode('gbk')
    reg = r'style5();</script>(.*?)<script type="text/javascript">style6()'
'''
    

#long

'''
    html = html.decode('gbk').encode('utf-8')
    reg = r'<td class="L"><a href="(.*?)">.*?</a></td>'
    reg = re.compile(reg)
    urlilsit = re.findall(reg,text)     
    return urllist
    
def get_url():
    a = r'<td class="L"><a href="%d.html">(.*?)</a></td>'
    urllist = re.findall(a,html)
    return urllist
print(get_url())
    

if __name__ == '__main__':
    url = 'http://www.37zw.com/1/1429/'
    get_url(url_open(url))
'''


