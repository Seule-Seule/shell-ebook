#!/usr/bin/env python3
#coding=utf-8
# Author : faner
# Email  : soul.seule@gmail.com

import os
import requests
from bs4 import BeautifulSoup
#from prettytable import PrettyTable


def ContentRequests(Contenturl):

    # 请求头
    headers = {
        'User-Agent':'Mozilla/5.0(Linux;X11)'
    }

    WhileEnd = 0
    while True:
        WhileEnd += 1
        try:
            # 请求页面
            r = requests.get(url = Contenturl,timeout = 5,headers = headers)
        
            # 收集错误信息
            r.raise_for_status()

            # 修改text编码 
            if r.encoding == 'ISO-8859-1':
                r.encoding = r.apparent_encoding 
            
            if r.status_code == 200:
                return r.text
        except:
            continue 
        if WhileEnd == 4:
            break

def ContentText(html):
    clist = []
    html_soup  = BeautifulSoup(html,'lxml')
    for Content in html_soup.find('div',{'id':'txtContent'}).children:
        if type(Content) != type(html_soup.div): 
            clist.append(Content.string)
    
    return clist

def GetTable(Url):
    ContentList = []
    ContentHtml = ContentRequests(Url)
    ContentList =  ContentText(ContentHtml)
    number = 1   
    for i in ContentList:
        number += 1
        print(i)
        if number == 30:
            break
    return

def GetContent(BookName,BookUrl):
    if os.sep == '/':
        clean = 'clear'
    else:
        clean = 'cls'
    os.system(clean)
    Bar = ['[ Home  ]','[ '+BookName+' ]','','']
    Print_Bar =  "\n" + "%s>%s>%s>%s"
    Print_Help = '\n\tNumber -> Enter recommendation. \
            \n\t  q    -> Enter exit. \
            \n\t'
    while True:
    
        os.system(clean)
        GetTable(BookUrl)
        print(Print_Help)
        print(Print_Bar % (Bar[0],Bar[1],Bar[2],Bar[3]),end = '')
        cmd = input()
        if cmd == 'q':
            return
        else:
            continue



if __name__ == '__main__':

    GetContent()

