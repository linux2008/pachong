#!/usr/bin/python

import urllib2,urllib
import re
def getpage(num=1):
    url="http://www.qiushibaike.com/8hr/page/+str(num)"
    head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    one=urllib2.Request(url,headers=head)
    two=urllib2.urlopen(one)
    html=two.read()
    return html
def getcount(num=1):
    html=getpage()
    dic=[]
    rep=re.compile(r'<br/>')
    rep1=re.compile(r'</span>|<span>')
    page=re.compile(r'<div class="author.*?">.*?<a .*?>.*?<img src=".*?" alt="(.*?)"/>.*?<div class="content">(.*?)</div>.*?<div class="stats">.*?<i class=".*?">(\d+)</i>',re.S)
    items=page.findall(html)
    for item in items:
        count=item[1]
        countnu=rep.sub('\n',count)
        countnu1=rep1.sub('\n',countnu)
        dic.append([num,
                   item[0],
                   countnu1.strip(),
                   item[2]])
    return dic
if __name__=='__main__':
    dict=getcount()
    for di in dict:
        for i in di:
            print i 






