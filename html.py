#!/usr/bin/python
import urllib,urllib2
import re
def a(url):
    page=urllib2.urlopen(url)
    return page.read()

def image(html):
    b=re.compile(r'<img hidefocus="true" src="//(.*?)".*?>')
    list=b.findall(html)
    n=1
    for i in list:
        i='http://'+i
        print i
        urllib.urlretrieve(i,filename="%s.png" %n)
       
if __name__=='__main__':
    url='http://www.baidu.com'
    page=a(url)
    print image(page)
