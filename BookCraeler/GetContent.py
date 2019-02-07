#!/usr/bin/env python3
#coding=utf-8
# Author : faner
# Email  : soul.seule@gmail.com

import requests
from bs4 import BeautifulSoup


def ContentRequests(Contenturl):

    # 请求头
    headers = {
        'User-Agent':'Mozilla/5.0(Linux;X11)'
    }
    try:
        # 请求页面
        r = requests.get(url = Contenturl,timeout = 5,headers = headers)
        
        # 收集错误信息
        r.raise_for_status()

        # 修改text编码 
        if r.encoding == 'ISO-8859-1':
            r.encoding = r.apparent_encoding 
        
        return r.text
    except:
        return ""

def ContentText(clist,html):
    html_soup  = BeautifulSoup(html,'lxml')
    for Content in html_soup.find('div',{'id':'txtContent'}).children:
        if type(Content) != type(html_soup.div): 
            clist.append(Content.string)

def GetContent(url):

    ContentList = []
    ContentHtml = ContentRequests(url)
    ContentText(ContentList,ContentHtml)
    
    return ContentList

if __name__ == '__main__':

    objecturl = 'https://www.boquge.com/book/44491/139210603.html'
    GetContent(objecturl)

