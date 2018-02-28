# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 11:34:56 2017

@author: 13588
"""

import urllib
import re

def getAllLinks(url):
    html1=str(urllib.request.urlopen(url).read().decode('utf-8'))
    pat='<a class="cate-link" href="(http://.+?")>'
    allLink=re.compile(pat).findall(html1)
    allLinks=[]
    for link in allLink:
        allLinks.append(link.split('"')[0])
    return allLinks

getAllLinks('http://www.wandoujia.com/category/app')

def getAllDescLinks(url,page):
    url=url+'/'+str(page)
    print(url)
    html1=str(urllib.request.urlopen(url).read().decode('utf-8'))
    pat2='<ul id="j-tag-list" class="app-box clearfix">[\s\S]*<div class="pagination">'
    allLink=str(re.compile(pat2).findall(html1)).strip('\n').replace(' ','').replace('\\n','').replace('\\t','')
    allLink=allLink.split('<divclass="icon-wrap"><ahref="')
    allLinks=[]
    for i in range(1,len(allLink)):
        allLinks.append(allLink[i].split('"><imgsrc')[0])
    allLinks=list(set(allLinks))
    return allLinks

url='http://www.wandoujia.com/apps/fm.qingting.qtradio'
def getAppName(html):
    html1=str(urllib.request.urlopen(url).read().decode('utf-8'))
    pat3='<span class="title" itemprop="name">[\s\S]*</span>'
    string=str(re.compile(pat).findall(html1))
    name=''
    if string!='[]':
        name=string.split('>')[1].split('<')[0]
    return name

def getAppGroup(html):
    html1=str(urllib.request.urlopen(url).read().decode('utf-8'))
    pat4='<dd class="tag-box">[\s\S]*itemprop="SoftwareApplicationCategory"[\s\S]*</dd>'
    group=str(re.compile(pat4).findall(html1)).split('<dt>')[0]
    group=group.split('itemprop="SoftwareApplicationCategory"')
 
def getClass(html):#所属分类
    pat='<dd class="tag-box">[\s\S]*<dt>TAG</dt>'
    classfy1=str(re.compile(pat).findall(html1))
    classfy=[]
    if classfy1!='[]':
        classfy1=classfy1.split('appTag">')
        for i in range(1,len(classfy1)):
            classfy.append(classfy1[i].split('<')[0])
    return classfy 

    











