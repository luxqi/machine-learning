# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 09:47:48 2018

@author: 13588
"""

import urllib
import requests
import time
import json
import re
import csv
import random


def getProxies(proxie_url):
    proxies_header={
            'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Connection':'keep-alive',
            'Host':'www.xicidaili.com',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Mobile Safari/537.36'
            }
    proxie_html=requests.get(proxie_url,headers=proxies_header).text
    ip_list=[]
    ip_html=re.findall('(<td>)(\d+.\d+.\d+.\d+)(</td>)',proxie_html)
    duankou_html=re.findall('(<td>)(\d{2,5})(</td>)',proxie_html)
    for i in range(0,len(duankou_html)):
        a=duankou_html[i][1]
        b=ip_html[i][1]
        ip=b+':'+a
        if duankou_html[i][1]!='':
            ip_list.append(ip)
    return ip_list
            
        

def getUrl(url):
    url_list=[]
    for page in range(0,1000):
        parse={'callback':'fetchJSON_comment98vv2321',
               'productId':'3484659',
               'score':0,
               'sortType':5,
               'page':page,
               'pageSize':10,
               'isShadowSku':0,
               'rid':0,
               'fold':1}
        urls=url+urllib.parse.urlencode(parse)
        url_list.append(urls)
    return url_list

def getResponse(url):
    headers={'cookie':'mba_muid=15095199573661225532590; _jrda=1; __jdv=122270672|direct|-|none|-|1517540042813; __jda=122270672.15095199573661225532590.1509519957.1517540043.1517881094.6; __jdc=122270672; 3AB9D23F7A4B3C9B=NZFD2GYZAHIA5TN27IJ4B2YSW6SLTLEPB4RUKF6XAGI7NWX42MPEA6OOJB22SQX32JMHQENCOLAXQVL66VSKXQ63K4; __jdu=15095199573661225532590',
             'referer':'https://item.jd.com/3484659.html',
             'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Mobile Safari/537.36',
             'authority':'sclub.jd.com',
             'accept':'*/*',
             'accept-encoding':'gzip, deflate, br',
             'accept-language':'zh-CN,zh;q=0.9'
             }
    try:
        proxie_url='http://www.xicidaili.com'
        response=requests.get(url,headers=headers,proxies={'http':random.choice(getProxies(proxie_url))})
        if response.status_code==200:
            return response.text
        return None
    except requests.RequestException as e:
        return None
    
def getResult(html):
    html=re.sub('fetchJSON_comment98vv2321\(',' ',html)
    html = re.sub('\)\;\Z','',html) 
    result=json.loads(html)
    comment=result['comments']
    return comment

    
with open('C:/Users/13588/Desktop/content.csv','w+') as csvfile:
    writer=csv.writer(csvfile,lineterminator='\n')
    time.sleep(1)
    url_list=getUrl('https://sclub.jd.com/comment/productPageComments.action?')
    for url in url_list:
        html=getResponse(url)
        comment=getResult(html)
        for i in range(0,len(comment)):
            content=comment[i]['content']
            nickname=comment[i]['nickname']
            cust_id=comment[i]['id']
            creationTime=comment[i]['creationTime']
            writer.writerow([content,nickname,cust_id,creationTime])
        
    
    
    